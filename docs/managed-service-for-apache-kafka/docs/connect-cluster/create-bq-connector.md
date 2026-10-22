---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector/
title: Create a BigQuery Sink connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:46.653459+00:00
---

# Create a BigQuery Sink connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a BigQuery Sink connector Stay organized with collections  Save and categorize content based on your preferences. 

BigQuery Sink connectors stream data from Kafka to BigQuery tables, enabling real-time data ingestion and analysis within BigQuery.

Use cases for BigQuery Sink connectors include the following:

  * Data warehousing. Load streaming data into BigQuery for analytics and reporting.

  * Populate BigQuery tables that power real-time dashboards.




## Before you begin

Before creating a BigQuery Sink connector, ensure you have the following:

  * [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster) for your Connect cluster. This cluster is the primary Kafka cluster associated with the Connect cluster. This cluster is also the source cluster that forms one end of the BigQuery Sink connector pipeline.

  * [Create a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) to host your BigQuery Sink connector.

  * [Create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets) to store the data streamed from Kafka.

  * [Create and configure a Kafka topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic) within the source cluster. Data moves from this Kafka topic to the destination BigQuery dataset.




### Required roles and permissions

To get the permissions that you need to create a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connector:

  * Create a connector: `managedkafka.connectors.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant permissions to write to the BigQuery table

The Managed Kafka service account must have permission to write messages to the BigQuery table. Grant the **BigQuery Data Editor** (`roles/bigquery.dataEditor`) role to the service account on the project containing the table.

The Managed Kafka service account has the following format: `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where PROJECT_NUMBER is the project number of the Connect cluster.

If your Connect cluster is in a different project from your Managed Service for Apache Kafka cluster, see [ Create a Connect cluster in a different project](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#create-a-connect-cluster-in-a-different-project).

## Key configuration parameters

The following are recommendations for configurations for the BigQuery sink connector.

### Queue size

The `queueSize` setting controls the maximum number of write requests to BigQuery. By default, this value isn't configured, which can result in out-of-memory errors in the Connect cluster. We recommend configuring this value to reduce the chance of such errors. The items in the queue are write requests, and don't correspond directly to a number of messages or bytes. Thefore, the recommend value is difficult to know in advance.

When messages are polled from Kafka, the connector splits the work based on their destination table. If all the messages in a poll are to be written to a single table, only one work item is be added. But if the messages in a poll are being written to three tables, for example, then three work items are added. The size of a work item can be roughly estimated based on the message poll configurations, the size of the Kafka messages, and the number of tables being written to.

## Schemas for a BigQuery Sink connector

The BigQuery Sink connector uses the configured value converter (`value.converter`) to parse Kafka record values into fields. Then it writes the fields to columns of the same name in the BigQuery table.

The connector requires a schema to operate. The schema can be provided in the following ways:

  * **Message-based schema** : The schema is included as part of each message.
  * **Table-based schema** : The connector infers the message schema from the BigQuery table schema.
  * **Schema registry** : The connector reads the schema from a schema registry, such as [Managed Service for Apache Kafka schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)).



The next sections describe these options.

### Message-based schema

In this mode, each Kafka record includes a JSON schema. The connector uses the schema to write the record data as a BigQuery table row.

To use message-based schemas, set the following properties on the connector:

  * `value.converter=org.apache.kafka.connect.json.JsonConverter`
  * `value.converter.schemas.enable=true`



Example Kafka record value:
    
    
    {
      "schema": {
        "type": "struct",
        "fields": [
          {
            "field": "user",
            "type": "string",
            "optional": false
          },
          {
            "field": "age",
            "type": "int64",
            "optional": false
          }
        ]
      },
      "payload": {
        "user": "userId",
        "age": 30
      }
    }
    

If the destination table already exists, the BigQuery table schema must be compatible with the embedded message schema. If `autoCreateTables=true`, the connector automatically creates the destination table if needed. For more information, see Table creation.

If you want the connector to update the BigQuery table schema as message schemas change, set `allowNewBigQueryFields`, `allowSchemaUnionization`, or `allowBigQueryRequiredFieldRelaxation` to `true`.

### Table-based schema

In this mode, the Kafka records contain plain JSON data without an explicit schema. The connector infers the schema from the destination table.

Requirements:

  * The BigQuery table must already exist.
  * The Kafka record data must be compatible with the table schema.
  * This mode doesn't support dynamic schema updates based on incoming messages.



To use table-based schemas, set the following properties on the connector:

  * `value.converter=org.apache.kafka.connect.json.JsonConverter`
  * `value.converter.schemas.enable=false`
  * `bigQueryPartitionDecorator=false`



If the BigQuery table uses [time-based partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#ingestion_time) with daily partitioning, `bigQueryPartitionDecorator` can be `true`. Otherwise, set this property to `false`.

Example Kafka record value:
    
    
    {
      "user": "userId",
      "age": 30
    }
    

### Schema registry

In this mode, each Kafka record contains Apache Avro data, and the message schema is stored in a schema registry.

To use the BigQuery Sink connector with a schema registry, set the following properties on the connector:

  * `value.converter=io.confluent.connect.avro.AvroConverter`
  * `value.converter.schema.registry.url=SCHEMA_REGISTRY_URL`



Replace `SCHEMA_REGISTRY_URL` with the URL of the schema registry.

To use the connector with Managed Service for Apache Kafka schema registry, set the following property:

  * `value.converter.bearer.auth.credentials.source=GCP`



For more information, see [Use Kafka Connect with schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-schema-registry).

## Apache Iceberg managed tables

The BigQuery Sink connector supports [Apache Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/iceberg-tables) (hereafter, _Iceberg managed tables_) as a sink target.

Iceberg managed tables provide the foundation for building open-format lakehouses on Google Cloud. Iceberg managed tables offer the same fully managed experience as BigQuery tables, but store data in customer-owned storage buckets using Parquet to be interoperable with Apache Iceberg open table formats.

For information on how to create an Apache Iceberg table, see [Create an Apache Iceberg table](https://docs.cloud.google.com/bigquery/docs/iceberg-tables#create-iceberg-tab).

## Create a BigQuery Sink connector

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster where you want to create the connector.

  3. Click **Create connector**.

  4. For the connector name, enter a string.

For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  5. For **Connector plugin** , select **BigQuery Sink**.

  6. In the **Topics** section, specify the Kafka topics to read from. You can specify a list of topics or a regular expression to match against topic names.

     * Option 1: Choose **Select a list of Kafka topics**. In the **Kafka topics** list, select one or more topics. Click **OK**.

     * Option 2: Choose **Use a topic regex**. In the **Topic regex** field, enter a regular expression.

  7. Click **Dataset** and specify a BigQuery dataset. You can choose an existing dataset or create a new one.

  8. Optional: In the **Configurations** box, add configuration properties or edit the default properties. For more information, see Configure the connector.

  9. Select the **Task restart policy**. For more information, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).

  10. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka connectors create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create) command:
         
         gcloud managed-kafka connectors create CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID \
             --config-file=CONFIG_FILE
         

Replace the following:

     * CONNECTOR_ID: The ID or name of the connector. For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a connector is immutable.

     * LOCATION: The location where you create the connector. This must be the same location where you created the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster).

     * CONNECT_CLUSTER_ID: The ID of the Connect cluster where the connector is created.

     * CONFIG_FILE: The path to the YAML configuration file for the BigQuery Sink connector.

Here is an example of a configuration file for the BigQuery Sink connector:
    
    name: "BQ_SINK_CONNECTOR_ID"
    project: "GCP_PROJECT_ID"
    topics: "GMK_TOPIC_ID"
    tasks.max: 3
    connector.class: "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector"
    key.converter: "org.apache.kafka.connect.storage.StringConverter"
    value.converter: "org.apache.kafka.connect.json.JsonConverter"
    value.converter.schemas.enable: "false"
    defaultDataset: "BQ_DATASET_ID"
    

Replace the following:

     * BQ_SINK_CONNECTOR_ID: The ID or name of the BigQuery Sink connector. For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a connector is immutable.

     * GCP_PROJECT_ID: The ID of the Google Cloud project where your BigQuery dataset resides.

     * GMK_TOPIC_ID: The ID of the Managed Service for Apache Kafka topic from which the data flows to the BigQuery Sink connector.

     * BQ_DATASET_ID: The ID of the BigQuery dataset that acts as the sink for the pipeline.




###  Terraform 

You can use a Terraform resource to create a [connector](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_connector).
    
    
    resource "google_managed_kafka_connector" "example-bigquery-sink-connector" {
      project         = data.google_project.default.project_id
      connector_id    = "my-bigquery-sink-connector"
      connect_cluster = google_managed_kafka_connect_cluster.default.connect_cluster_id
      location        = "us-central1"
    
      configs = {
        "name"                           = "my-bigquery-sink-connector"
        "project"                        = data.google_project.default.project_id
        "topics"                         = "GMK_TOPIC_ID"
        "tasks.max"                      = "3"
        "connector.class"                = "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector"
        "key.converter"                  = "org.apache.kafka.connect.storage.StringConverter"
        "value.converter"                = "org.apache.kafka.connect.json.JsonConverter"
        "value.converter.schemas.enable" = "false"
        "defaultDataset"                 = "BQ_DATASET_ID"
      }
    
      provider = google-beta
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    )
    
    // createBigQuerySinkConnector creates a BigQuery Sink connector.
    func createBigQuerySinkConnector(w io.Writer, projectID, region, connectClusterID, connectorID, topics, tasksMax, keyConverter, valueConverter, valueConverterSchemasEnable, defaultDataset string, opts ...option.ClientOption) error {
    	// TODO(developer): Update with your config values. Here is a sample configuration:
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "BQ_SINK_CONNECTOR_ID"
    	// topics := "GMK_TOPIC_ID"
    	// tasksMax := "3"
    	// keyConverter := "org.apache.kafka.connect.storage.StringConverter"
    	// valueConverter := "org.apache.kafka.connect.json.JsonConverter"
    	// valueConverterSchemasEnable := "false"
    	// defaultDataset := "BQ_DATASET_ID"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s", projectID, region, connectClusterID)
    
    	// BigQuery Sink sample connector configuration
    	config := map[string]string{
    		"name":                           connectorID,
    		"project":                        projectID,
    		"topics":                         topics,
    		"tasks.max":                      tasksMax,
    		"connector.class":                "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector",
    		"key.converter":                  keyConverter,
    		"value.converter":                valueConverter,
    		"value.converter.schemas.enable": valueConverterSchemasEnable,
    		"defaultDataset":                 defaultDataset,
    	}
    
    	connector := &managedkafkapb.Connector{
    		Name:    fmt.Sprintf("%s/connectors/%s", parent, connectorID),
    		Configs: config,
    	}
    
    	req := &managedkafkapb.CreateConnectorRequest{
    		Parent:      parent,
    		ConnectorId: connectorID,
    		Connector:   connector,
    	}
    
    	resp, err := client.CreateConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created BigQuery sink connector: %s\n", resp.Name)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html);
    import com.google.cloud.managedkafka.v1.[Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class CreateBigQuerySinkConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-bigquery-sink-connector";
        String bigqueryProjectId = "my-bigquery-project-id";
        String datasetName = "my-dataset";
        String kafkaTopicName = "kafka-topic";
        String maxTasks = "3";
        String connectorClass = "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector";
        String keyConverter = "org.apache.kafka.connect.storage.StringConverter";
        String valueConverter = "org.apache.kafka.connect.json.JsonConverter";
        String valueSchemasEnable = "false";
        createBigQuerySinkConnector(
            projectId,
            region,
            connectClusterId,
            connectorId,
            bigqueryProjectId,
            datasetName,
            kafkaTopicName,
            maxTasks,
            connectorClass,
            keyConverter,
            valueConverter,
            valueSchemasEnable);
      }
    
      public static void createBigQuerySinkConnector(
          String projectId,
          String region,
          String connectClusterId,
          String connectorId,
          String bigqueryProjectId,
          String datasetName,
          String kafkaTopicName,
          String maxTasks,
          String connectorClass,
          String keyConverter,
          String valueConverter,
          String valueSchemasEnable)
          throws Exception {
    
        // Build the connector configuration
        Map<String, String> configMap = new HashMap<>();
        configMap.put("name", connectorId);
        configMap.put("project", bigqueryProjectId);
        configMap.put("topics", kafkaTopicName);
        configMap.put("tasks.max", maxTasks);
        configMap.put("connector.class", connectorClass);
        configMap.put("key.converter", keyConverter);
        configMap.put("value.converter", valueConverter);
        configMap.put("value.converter.schemas.enable", valueSchemasEnable);
        configMap.put("defaultDataset", datasetName);
    
        [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) connector =
            [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html).newBuilder()
                .setName([ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, connectClusterId, connectorId).toString())
                .putAllConfigs(configMap)
                .build();
    
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html) request =
              [CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html).newBuilder()
                  .setParent([ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html).of(projectId, region, connectClusterId).toString())
                  .[setConnectorId](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.Builder.html#com_google_cloud_managedkafka_v1_CreateConnectorRequest_Builder_setConnectorId_java_lang_String_)(connectorId)
                  .setConnector(connector)
                  .build();
    
          // This operation is being handled synchronously.
          [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) response = managedKafkaConnectClient.createConnector(request);
          System.out.printf("Created BigQuery Sink connector: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html#com_google_cloud_managedkafka_v1_Connector_getName__)());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.createConnector got err: %s\n", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        ManagedKafkaConnectClient,
    )
    from google.cloud.managedkafka_v1.types import Connector, CreateConnectorRequest
    
    connect_client = ManagedKafkaConnectClient()
    parent = connect_client.connect_cluster_path(project_id, region, connect_cluster_id)
    
    configs = {
        "name": connector_id,
        "project": project_id,
        "topics": topics,
        "tasks.max": tasks_max,
        "connector.class": "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector",
        "key.converter": key_converter,
        "value.converter": value_converter,
        "value.converter.schemas.enable": value_converter_schemas_enable,
        "defaultDataset": default_dataset,
    }
    
    connector = Connector()
    connector.name = connector_id
    connector.configs = configs
    
    request = CreateConnectorRequest(
        parent=parent,
        connector_id=connector_id,
        connector=connector,
    )
    
    try:
        operation = connect_client.create_connector(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        response = operation.result()
        print("Created Connector:", response)
    except GoogleAPICallError as e:
        print(f"The operation failed with error: {e}")

After you create a connector, you can edit, delete, pause, stop, or restart the connector.

## Configure the connector

This section describes some configuration properties that you can set on the connector. For a complete list of the properties that are specific to this connector, see [BigQuery Sink connector configs](https://github.com/Aiven-Open/bigquery-connector-for-apache-kafka/blob/main/docs/sink-connector-config-options.rst).

### Table name

By default, the connector uses the topic name as the BigQuery table name. To use a different table name, set the `topic2TableMap` property with the following format:
    
    
    topic2TableMap=TOPIC_1:TABLE_1,TOPIC_2:TABLE_2,...
    

### Table creation

The BigQuery Sink connector can create the destination tables if they don't exist.

  * If `autoCreateTables=true`, the connector attempts to create any BigQuery tables that don't exist. This setting is the default behavior.

  * If `autoCreateTables=false`, the connector doesn't create any tables. If a destination table doesn't exist, then an error occurs.




When `autoCreateTables` is `true`, you can use the following configuration properties for more fine-grained control over how the connector creates and configures new tables:

  * `allBQFieldsNullable`
  * `clusteringPartitionFieldNames`
  * `convertDoubleSpecialValues`
  * `partitionExpirationMs`
  * `sanitizeFieldNames`
  * `sanitizeTopics`
  * `timestampPartitionFieldName`



For information about these properties, see [BigQuery Sink connector configs](https://github.com/Aiven-Open/bigquery-connector-for-apache-kafka/blob/main/docs/sink-connector-config-options.rst).

### Kafka metadata

You can map additional data from Kafka such as metadata information and key information into the BigQuery table by configuring the `kafkaDataFieldName` and `kafkaKeyFieldName` fields respectively. Examples of metadata information include the Kafka topic, partition, offset, and insert time.

## What's next?

  * [Write Kafka messages to BigQuery](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-write-to-bigquery)

  * [Troubleshoot a BigQuery Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-bq-connector-config)

  * [Pause, resume, stop, and restart a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/pause-resume-stop-restart-connector)

  * [List all connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connectors)

  * [View the details of a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connector)

  * [Update a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
