---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector/
title: Create a Cloud Storage Sink connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:55.273054+00:00
---

# Create a Cloud Storage Sink connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Cloud Storage Sink connector Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Storage Sink connector streams data from Managed Service for Apache Kafka to a Cloud Storage, which lets you store and process large volumes of data in a cost-effective and scalable manner.

Typical use cases for this connector include:

  * Data lake ingestion. Store Kafka data in a data lake for long-term archival and batch processing.

  * Archive data to meet regulatory requirements.




## Before you begin

Before creating a Cloud Storage Sink connector, ensure you have the following:

  * [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster) for your Connect cluster. This is the primary Kafka cluster associated with the Connect cluster. This is also the source cluster that forms one end of the connector pipeline.

  * [Create a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) to host your Cloud Storage Sink connector.

  * [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the data streamed from Kafka.

  * [Create and configure a Kafka topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic) within the source cluster. Data moves from this Kafka topic to the destination Cloud Storage bucket.




### Required roles and permissions

To get the permissions that you need to create a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connector:

  * Create a connector: `managedkafka.connectors.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant permissions to write to the Cloud Storage bucket

The Managed Kafka service account must have the following permissions to write messages to the Cloud Storage bucket:

  * `storage.objects.create`
  * `storage.objects.delete`



Grant the **Storage Object User** (`roles/storage.objectUser`) role to the service account on the project containing the Cloud Storage bucket.

The Managed Kafka service account has the following format: `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where PROJECT_NUMBER is the project number of the Connect cluster.

If your Connect cluster is in a different project from your Managed Service for Apache Kafka cluster, see [ Create a Connect cluster in a different project](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#create-a-connect-cluster-in-a-different-project).

## Create a Cloud Storage Sink connector

To create a Cloud Storage Sink connector, perform the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster for which you want to create the connector.

The **Connect cluster details** page is displayed.

  3. Click **Create connector**.

The **Create Kafka connector** page is displayed.

  4. For the connector name, enter a string.

For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  5. For **Connector plugin** , select **Cloud Storage Sink**.

  6. Specify the **Topics** from which you can stream data.

  7. Choose the **Storage Bucket** to store the data.

  8. (Optional) Configure additional settings in the **Configuration** section.

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

     * `CONNECTOR_ID`: The ID or name of the connector. For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a connector is immutable.

     * `LOCATION`: The location where you create the connector. This must be the same location where you created the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster).

     * `CONNECT_CLUSTER_ID`: The ID of the Connect cluster where the connector is created.

     * `CONFIG_FILE`: The path to the YAML configuration file for the connector.

Here is an example of a configuration file for the Cloud Storage Sink connector:
    
    connector.class: "io.aiven.kafka.connect.gcs.GcsSinkConnector"
    gcs.bucket.name: "BUCKET_NAME"
    gcs.credentials.default: "true"
    format.output.type: "json"
    key.converter: "org.apache.kafka.connect.storage.StringConverter"
    value.converter: "org.apache.kafka.connect.json.JsonConverter"
    value.converter.schemas.enable: "false"
    topics: "TOPIC_LIST"
    tasks.max: "3"
    

Replace the following:

     * `BUCKET_NAME`: The name of the Cloud Storage bucket to write to.

     * `TOPIC_LIST`: A comma-separated list of Kafka topics to read from. The list can also include regular expressions.




###  Terraform 

You can use a Terraform resource to create a [connector](https://registry.%0Aterraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_%0Aconnector).
    
    
    resource "google_managed_kafka_connector" "example-cloud-storage-sink-connector" {
      project         = data.google_project.default.project_id
      connector_id    = "my-gcs-sink-connector"
      connect_cluster = google_managed_kafka_connect_cluster.default.connect_cluster_id
      location        = "us-central1"
    
      configs = {
        "connector.class"                = "io.aiven.kafka.connect.gcs.GcsSinkConnector"
        "tasks.max"                      = "3"
        "topics"                         = "GMK_TOPIC_ID"
        "gcs.bucket.name"                = "GCS_BUCKET_NAME"
        "gcs.credentials.default"        = "true"
        "format.output.type"             = "json"
        "name"                           = "my-gcs-sink-connector"
        "value.converter"                = "org.apache.kafka.connect.json.JsonConverter"
        "value.converter.schemas.enable" = "false"
        "key.converter"                  = "org.apache.kafka.connect.storage.StringConverter"
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
    
    // createCloudStorageSinkConnector creates a Cloud Storage Sink connector.
    func createCloudStorageSinkConnector(w io.Writer, projectID, region, connectClusterID, connectorID, topics, gcsBucketName, tasksMax, formatOutputType, valueConverter, valueConverterSchemasEnable, keyConverter, gcsCredentialsDefault string, opts ...option.ClientOption) error {
    	// TODO(developer): Update with your config values. Here is a sample configuration:
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "GCS_SINK_CONNECTOR_ID"
    	// topics := "GMK_TOPIC_ID"
    	// gcsBucketName := "GCS_BUCKET_NAME"
    	// tasksMax := "3"
    	// formatOutputType := "json"
    	// valueConverter := "org.apache.kafka.connect.json.JsonConverter"
    	// valueConverterSchemasEnable := "false"
    	// keyConverter := "org.apache.kafka.connect.storage.StringConverter"
    	// gcsCredentialsDefault := "true"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s", projectID, region, connectClusterID)
    
    	config := map[string]string{
    		"connector.class":                "io.aiven.kafka.connect.gcs.GcsSinkConnector",
    		"tasks.max":                      tasksMax,
    		"topics":                         topics,
    		"gcs.bucket.name":                gcsBucketName,
    		"gcs.credentials.default":        gcsCredentialsDefault,
    		"format.output.type":             formatOutputType,
    		"name":                           connectorID,
    		"value.converter":                valueConverter,
    		"value.converter.schemas.enable": valueConverterSchemasEnable,
    		"key.converter":                  keyConverter,
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
    	fmt.Fprintf(w, "Created Cloud Storage sink connector: %s\n", resp.Name)
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
    
    public class CreateCloudStorageSinkConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-gcs-sink-connector";
        String bucketName = "my-gcs-bucket";
        String kafkaTopicName = "kafka-topic";
        String connectorClass = "io.aiven.kafka.connect.gcs.GcsSinkConnector";
        String maxTasks = "3";
        String gcsCredentialsDefault = "true";
        String formatOutputType = "json";
        String valueConverter = "org.apache.kafka.connect.json.JsonConverter";
        String valueSchemasEnable = "false";
        String keyConverter = "org.apache.kafka.connect.storage.StringConverter";
        createCloudStorageSinkConnector(
            projectId,
            region,
            connectClusterId,
            connectorId,
            bucketName,
            kafkaTopicName,
            connectorClass,
            maxTasks,
            gcsCredentialsDefault,
            formatOutputType,
            valueConverter,
            valueSchemasEnable,
            keyConverter);
      }
    
      public static void createCloudStorageSinkConnector(
          String projectId,
          String region,
          String connectClusterId,
          String connectorId,
          String bucketName,
          String kafkaTopicName,
          String connectorClass,
          String maxTasks,
          String gcsCredentialsDefault,
          String formatOutputType,
          String valueConverter,
          String valueSchemasEnable,
          String keyConverter)
          throws Exception {
    
        // Build the connector configuration
        Map<String, String> configMap = new HashMap<>();
        configMap.put("connector.class", connectorClass);
        configMap.put("tasks.max", maxTasks);
        configMap.put("topics", kafkaTopicName);
        configMap.put("gcs.bucket.name", bucketName);
        configMap.put("gcs.credentials.default", gcsCredentialsDefault);
        configMap.put("format.output.type", formatOutputType);
        configMap.put("name", connectorId);
        configMap.put("value.converter", valueConverter);
        configMap.put("value.converter.schemas.enable", valueSchemasEnable);
        configMap.put("key.converter", keyConverter);
    
        [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) connector = [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html).newBuilder()
            .setName(
                [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, connectClusterId, connectorId).toString())
            .putAllConfigs(configMap)
            .build();
    
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html) request = [CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html).newBuilder()
              .setParent([ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html).of(projectId, region, connectClusterId).toString())
              .[setConnectorId](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.Builder.html#com_google_cloud_managedkafka_v1_CreateConnectorRequest_Builder_setConnectorId_java_lang_String_)(connectorId)
              .setConnector(connector)
              .build();
    
          // This operation is being handled synchronously.
          [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) response = managedKafkaConnectClient.createConnector(request);
          System.out.printf("Created Cloud Storage Sink connector: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html#com_google_cloud_managedkafka_v1_Connector_getName__)());
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
        "connector.class": "io.aiven.kafka.connect.gcs.GcsSinkConnector",
        "tasks.max": tasks_max,
        "topics": topics,
        "gcs.bucket.name": gcs_bucket_name,
        "gcs.credentials.default": "true",
        "format.output.type": format_output_type,
        "name": connector_id,
        "value.converter": value_converter,
        "value.converter.schemas.enable": value_converter_schemas_enable,
        "key.converter": key_converter,
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

For a complete list of the properties that are specific to this connector, see [Configuration](https://aiven-open.github.io/cloud-storage-connectors-for-apache-kafka/gcs-sink-connector/index.html#Configuration) in the Cloud Storage Sink connector documentation.

### Output fields

By default, the connector writes only the record value from each Kafka record. To include record keys or headers, set the `format.output.fields` property to a comma-separated list of fields to include. The supported fields are `key`, `value`, `headers`, and `timestamp`. For example:
    
    
    format.output.fields=key,value,headers
    

### Output formats

The connector supports writing Kafka records in CSV, JSON, and Parquet format. The following sections describe how to configure the output format.

#### CSV format

To write CSV files to Cloud Storage, set `format.output.type=csv`. Use the following converters:

  * Key converter: `org.apache.kafka.connect.storage.StringConverter` or `org.apache.kafka.connect.json.JsonConverter`

  * Value converter: `org.apache.kafka.connect.converters.ByteArrayConverter`




#### JSON format

To write JSON-formatted files to Cloud Storage, set `format.output.type` to one of the following values:

  * `json`: Each output file contains a single array of JSON objects, where each JSON object represents one Kafka record.

  * `jsonl`: The connector writes each Kafka record as a JSON object on a separate line.




The following example shows how the connector writes a Kafka record in JSON format:
    
    
    {"headers":[{"key":"k1","value":"v1"},{"key":"k2","value":"v2"}],"value":"Hello world","key":"my-key"}
    

If you set the key or value converter to `org.apache.kafka.connect.converters.ByteArrayConverter`, then the connector writes that field as a base64-encoded value.

The connector doesn't include a JSON schema in the output, even if `value.converter.schemas.enable` is `true`.

#### Parquet format

To write Parquet files to Cloud Storage, set `format.output.type=parquet`.

If the key or value converter is `org.apache.kafka.connect.json.JsonConverter`, then the JSON data must include a schema. Set the converter's `schemas.enable` property to `true`.

For JSON data, the connector writes the data as a `struct` type in the Parquet file. For example, if the Kafka record value has a field named `userid`, the connector writes a column named `value.userid`. To flatten the column names, set `format.output.envelope=false`. If `format.output.envelope` is `false`, then `format.output.fields` must specify a single output field.

### Cloud Storage file settings

The following settings control how the connector writes files to Cloud Storage.

  * `gcs.bucket.name`: Required. Specifies the name of the Cloud Storage bucket where the connector writes data.

  * `file.compression.type`: Specifies the compression type for the output files. Examples are `gzip`, `snappy`, `zstd`, and `none`. The default value is `none`.

  * `file.name.prefix`: Specifies a prefix to be added to the name of each file. The default value is empty (`""`).

  * `file.name.template`: Specifies a template for the filename. The connector supports placeholder variables for the template, such as `{{topic}}` for topic name and `{{partition}}` for partition number. For more information, see the [Cloud Storage Sink connector documentation](https://aiven-open.github.io/cloud-storage-connectors-for-apache-kafka/gcs-sink-connector/index.html).

  * `file.max.records`: The maximum number of records to write to a single file. If the value is 0, there is no specific maximum. The default value is 0.

  * `file.max.bytes`: The maximum file size to write, in bytes. If the value is 0, there is no specific maximum. The default value is 0.




### Record grouping

When the Cloud Storage Sink connector writes Kafka records, by default it groups the records by topic and partition. For example, records from partition 0 of topic `my-topic` are written to files named `my-topic-0-OFFSET`, where `OFFSET` is the starting offset.

If the `file.name.template` parameter includes the `{{key}}` placeholder variable, then the connector groups records by key. In this mode, the connector writes a separate file for each record key. The connector overwrites each file with the latest record for that key.

### Credentials

The `gcs.credentials.default` property must be set to `true`. This setting enables the connector to discover Google Cloud credentials automatically.

## What's next?

  * [Troubleshoot a Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-cloud-storage-connector)

  * [Pause, resume, stop, and restart a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/pause-resume-stop-restart-connector)

  * [List all connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connectors)

  * [View the details of a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connector)

  * [Update a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
