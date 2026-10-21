---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector/
title: Create a Pub/Sub Source connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:17.182399+00:00
---

# Create a Pub/Sub Source connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Pub/Sub Source connector Stay organized with collections  Save and categorize content based on your preferences. 

Pub/Sub Source connectors stream messages from Pub/Sub to Kafka, which lets you integrate Pub/Sub with your Kafka-based applications and data pipelines.

Use cases for Pub/Sub Source connectors include the following:

  * Real-time data ingestion. Publish data from cloud services or other applications to Pub/Sub and then replicate the data to Kafka for stream processing.

  * Event-driven architectures. Trigger Kafka-based processing from messages published to Pub/Sub.




The connector reads messages from a Pub/Sub subscription, converts each message into a Kafka record, and writes the records to a Kafka topic. By default, the connector creates Kafka records as follows:

  * The Kafka record key is `null`.
  * The Kafka record value is the Pub/Sub message data as bytes.
  * The Kafka record headers are empty.



However, you can configure this behavior. For more information, see Configure the connector.

## Before you begin

Before creating a Pub/Sub Source connector, ensure you have the following:

  * A [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic) with a subscription.

  * A [Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).

  * A [Kafka topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic) within the Kafka cluster.

  * A [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster). When you create the Connect cluster, set the Managed Service for Apache Kafka cluster as the [primary Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#kafka-cluster).




### Required roles and permissions

To get the permissions that you need to create a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connector:

  * Create a connector: `managedkafka.connectors.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant permissions to read from Pub/Sub

The Managed Kafka service account must have permission to read messages from the Pub/Sub subscription. Grant the following IAM roles to the service account on the project containing the Pub/Sub subscription:

  * **Pub/Sub Subscriber** (`roles/pubsub.subscriber`)
  * **Pub/Sub Viewer** (`roles/pubsub.viewer`)



The Managed Kafka service account has the following format: `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where PROJECT_NUMBER is the project number of the Connect cluster.

If your Connect cluster is in a different project from your Managed Service for Apache Kafka cluster, see [ Create a Connect cluster in a different project](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#create-a-connect-cluster-in-a-different-project).

## Create a Pub/Sub Source connector

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster where you want to create the connector.

  3. Click **Create connector**.

  4. For the connector name, enter a string.

For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  5. For **Connector plugin** , select **Pub/Sub Source**.

  6. In the **Cloud Pub/Sub subscription** list, select a Pub/Sub subscription. The connector pulls messages from this subscription. The subscription is displayed as a full resource name: `projects/{project}/subscriptions/{subscription}`.

  7. In the **Kafka topic** list, select the Kafka topic where messages are written.

  8. Optional: In the **Configurations** box, add configuration properties or edit the default properties. For more information, see Configure the connector.

  9. Select the **Task restart policy**. For more information, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).

  10. Click **Create**.




###  gcloud 

  1. Run the [`gcloud managed-kafka connectors create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create) command:
         
         gcloud managed-kafka connectors create CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID \
             --config-file=CONFIG_FILE
         

Replace the following:

     * CONNECTOR_ID: The ID or name of the connector. For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a connector is immutable.

     * LOCATION: The location of the Connect cluster.

     * CONNECT_CLUSTER_ID: The ID of the Connect cluster where the connector is created.

     * CONFIG_FILE: The path to a YAML or JSON configuration file.




Here is an example of a configuration file:
    
    
    connector.class: "com.google.pubsub.kafka.source.CloudPubSubSourceConnector"
    cps.project: "PROJECT_ID"
    cps.subscription: "PUBSUB_SUBSCRIPTION_ID"
    kafka.topic: "KAFKA_TOPIC_ID"
    value.converter: "org.apache.kafka.connect.converters.ByteArrayConverter"
    key.converter: "org.apache.kafka.connect.storage.StringConverter"
    tasks.max: "3"
    

Replace the following:

  * PROJECT_ID: The ID of the Google Cloud project where the Pub/Sub subscription resides.

  * PUBSUB_SUBSCRIPTION_ID: The ID of the Pub/Sub subscription to pull data from.

  * KAFKA_TOPIC_ID: The ID of the Kafka topic where data is written.




The `cps.project`, `cps.subscription`, and `kafka.topic` configuration properties are required. For additional configuration options, see Configure the connector.

###  Terraform 

You can use a Terraform resource to create a [connector](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_connector).
    
    
    resource "google_managed_kafka_connector" "example-pubsub-source-connector" {
      project         = data.google_project.default.project_id
      connector_id    = "my-pubsub-source-connector"
      connect_cluster = google_managed_kafka_connect_cluster.default.connect_cluster_id
      location        = "us-central1"
    
      configs = {
        "connector.class"  = "com.google.pubsub.kafka.source.CloudPubSubSourceConnector"
        "name"             = "my-pubsub-source-connector"
        "tasks.max"        = "3"
        "kafka.topic"      = "GMK_TOPIC_ID"
        "cps.subscription" = "CPS_SUBSCRIPTION_ID"
        "cps.project"      = data.google_project.default.project_id
        "value.converter"  = "org.apache.kafka.connect.converters.ByteArrayConverter"
        "key.converter"    = "org.apache.kafka.connect.storage.StringConverter"
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
    
    // createPubSubSourceConnector creates a Pub/Sub Source connector.
    func createPubSubSourceConnector(w io.Writer, projectID, region, connectClusterID, connectorID, kafkaTopic, cpsSubscription, cpsProject, tasksMax, valueConverter, keyConverter string, opts ...option.ClientOption) error {
    	// TODO(developer): Update with your config values. Here is a sample configuration:
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "CPS_SOURCE_CONNECTOR_ID"
    	// kafkaTopic := "GMK_TOPIC_ID"
    	// cpsSubscription := "CPS_SUBSCRIPTION_ID"
    	// cpsProject := "GCP_PROJECT_ID"
    	// tasksMax := "3"
    	// valueConverter := "org.apache.kafka.connect.converters.ByteArrayConverter"
    	// keyConverter := "org.apache.kafka.connect.storage.StringConverter"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s", projectID, region, connectClusterID)
    
    	// Pub/Sub Source sample connector configuration
    	config := map[string]string{
    		"connector.class":  "com.google.pubsub.kafka.source.CloudPubSubSourceConnector",
    		"name":             connectorID,
    		"tasks.max":        tasksMax,
    		"kafka.topic":      kafkaTopic,
    		"cps.subscription": cpsSubscription,
    		"cps.project":      cpsProject,
    		"value.converter":  valueConverter,
    		"key.converter":    keyConverter,
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
    	fmt.Fprintf(w, "Created Pub/Sub source connector: %s\n", resp.Name)
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
    
    public class CreatePubSubSourceConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-pubsub-source-connector";
        String pubsubProjectId = "my-pubsub-project-id";
        String subscriptionName = "my-subscription";
        String kafkaTopicName = "pubsub-topic";
        String connectorClass = "com.google.pubsub.kafka.source.CloudPubSubSourceConnector";
        String maxTasks = "3";
        String valueConverter = "org.apache.kafka.connect.converters.ByteArrayConverter";
        String keyConverter = "org.apache.kafka.connect.storage.StringConverter";
        createPubSubSourceConnector(
            projectId,
            region,
            connectClusterId,
            connectorId,
            pubsubProjectId,
            subscriptionName,
            kafkaTopicName,
            connectorClass,
            maxTasks,
            valueConverter,
            keyConverter);
      }
    
      public static void createPubSubSourceConnector(
          String projectId,
          String region,
          String connectClusterId,
          String connectorId,
          String pubsubProjectId,
          String subscriptionName,
          String kafkaTopicName,
          String connectorClass,
          String maxTasks,
          String valueConverter,
          String keyConverter)
          throws Exception {
    
        // Build the connector configuration
        Map<String, String> configMap = new HashMap<>();
        configMap.put("connector.class", connectorClass);
        configMap.put("name", connectorId);
        configMap.put("tasks.max", maxTasks);
        configMap.put("kafka.topic", kafkaTopicName);
        configMap.put("cps.subscription", subscriptionName);
        configMap.put("cps.project", pubsubProjectId);
        configMap.put("value.converter", valueConverter);
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
          System.out.printf("Created Pub/Sub Source connector: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html#com_google_cloud_managedkafka_v1_Connector_getName__)());
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
        "connector.class": "com.google.pubsub.kafka.source.CloudPubSubSourceConnector",
        "name": connector_id,
        "tasks.max": tasks_max,
        "kafka.topic": kafka_topic,
        "cps.subscription": cps_subscription,
        "cps.project": cps_project,
        "value.converter": value_converter,
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

This section describes some configuration properties that you can set on the connector.

For a complete list of the properties that are specific to this connector, see [Pub/Sub Source connector configs](https://github.com/googleapis/java-pubsub-group-kafka-connector?tab=readme-ov-file#source-connector).

### Pull mode

The pull mode specifies how the connector retrieves Pub/Sub messages. The following modes are supported:

  * **Pull mode** (default). Messages are pulled in batches. To enable this mode, set `cps.streamingPull.enabled=false.` To configure the batch size, set the `cps.maxBatchSize` property.

For more information about pull mode, see [Pull API](https://docs.cloud.google.com/pubsub/docs/pull#pull-api).

  * **Streaming Pull mode**. Enables the maximum throughput and lowest latency when retrieving messages from Pub/Sub. To enable this mode, set `cps.streamingPull.enabled=true`.

For more information about streaming pull mode, see [StreamingPull API](https://docs.cloud.google.com/pubsub/docs/pull#streamingpull-api).

If streaming pull is enabled, you can tune the performance by setting the following configuration properties:

    * `cps.streamingPull.flowControlBytes`: The maximum number of outstanding message bytes per task.
    * `cps.streamingPull.flowControlMessages`: The maximum number of outstanding messages per task.
    * `cps.streamingPull.maxAckExtensionMs`: The maximum amount of time the connector extends the subscribe deadline, in milliseconds.
    * `cps.streamingPull.maxMsPerAckExtension`: The maximum amount of time the connector extends the subscribe deadline per extension, in milliseconds.
    * `cps.streamingPull.parallelStreams`: The number of streams to pull messages from the subscription.



### Pub/Sub endpoint

By default, the connector uses the global Pub/Sub endpoint. To specify an endpoint, set the `cps.endpoint` property to the endpoint address. For more information about endpoints, see [Pub/Sub endpoints](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#pubsub_endpoints).

### Kafka partitions

By default, the connector writes to a single partition in the topic. To specify how many partitions the connector writes to, set the `kafka.partition.count` property. The value must not exceed the topic's [partition count](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic#partition-count).

To specify how the connector assigns messages to partitions, set the `kafka.partition.scheme` property. For more information, see [Pub/Sub Source connector configs](https://github.com/googleapis/java-pubsub-group-kafka-connector?tab=readme-ov-file#source-connector).

### Converters

Set the key converter to `org.apache.kafka.connect.storage.StringConverter`.

Depending on the connector configuration, set the value converter to one of the following:

  * `org.apache.kafka.connect.converters.ByteArrayConverter`
  * `org.apache.kafka.connect.json.JsonConverter`



For more information, see Record value.

## Message conversion

The Pub/Sub Source connector converts Pub/Sub messages to Kafka records. The following sections describe the conversion process.

### Record key

The key converter must be `org.apache.kafka.connect.storage.StringConverter`.

  * By default, record keys are `null`.

  * To use a Pub/Sub [message attribute](https://docs.cloud.google.com/pubsub/docs/publisher#using-attributes) as the key, set `kafka.key.attribute` to the name of the attribute. For example, `kafka.key.attribute=username`.

  * To use the Pub/Sub [ordering key](https://docs.cloud.google.com/pubsub/docs/publisher#using-ordering-keys) as the key, set `kafka.key.attribute=orderingKey`.




### Record headers

By default, record headers are empty.

If `kafka.record.headers` is `true`, Pub/Sub message attributes are written as record headers. To include the ordering key, set `cps.makeOrderingKeyAttribute=true`.

### Record value

Record values are written either as byte arrays or as `struct` types.

#### Byte array record values

If either `kafka.record.headers` is `true`, or the Pub/Sub message has no custom attributes, the connector writes the message data as a byte array. Set the value converter to `org.apache.kafka.connect.converters.ByteArrayConverter`.

#### Struct record values

If `kafka.record.headers` is `false` and the message has at least one custom attribute, the connector writes the record value as a `struct`. Set the value converter to `org.apache.kafka.connect.json.JsonConverter`.

The `struct` contains the following fields:

  * `message`: The Pub/Sub message data, as bytes.

  * A field for each Pub/Sub message attribute. To include the ordering key, set `cps.makeOrderingKeyAttribute=true`.




For example, if the message has a `username` attribute, the record value looks like the following:
    
    
    {
      "message":"MESSAGE_DATA",
      "username":"Alice"
    }
    

If `value.converter.schemas.enable` is `true`, the `struct` includes both the payload and the schema:
    
    
    {
      "schema":
        {
          "type":"struct",
          "fields": [
            {
              "type":"bytes",
              "optional":false,
              "field":"message"
            },
            {
              "type":"string",
              "optional":false,
              "field":"username"
            }
          ],
          "optional":false
        },
        "payload": {
          "message":"MESSAGE_DATA",
          "username":"Alice"
        }
    }
    

## What's next?

  * [Replicate Pub/Sub messages to Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-pubsub)

  * [Troubleshoot a Pub/Sub connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-pubsub-connector)

  * [Pause, resume, stop, and restart a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/pause-resume-stop-restart-connector)

  * [List all connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connectors)

  * [View the details of a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connector)

  * [Update a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
