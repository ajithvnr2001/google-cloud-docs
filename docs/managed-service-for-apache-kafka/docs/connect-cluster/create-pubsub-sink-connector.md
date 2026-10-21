---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector/
title: Create a Pub/Sub Sink connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:17.470097+00:00
---

# Create a Pub/Sub Sink connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Pub/Sub Sink connector Stay organized with collections  Save and categorize content based on your preferences. 

Pub/Sub Sink connectors stream messages from Kafka topics to Pub/Sub topics, which lets you integrate your Kafka-based applications with Pub/Sub.

Use cases for Pub/Sub Sink connectors include the following:

  * Event-driven architectures. Trigger Pub/Sub processing from messages published to Kafka.

  * Service integration. Send data from Kafka to other Google Cloud services or applications that consume from Pub/Sub.

  * Trigger real-time notifications or actions based on processed data.




## Before you begin

Before creating a Pub/Sub Sink connector, ensure you have the following:

  * [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster) for your Connect cluster. This is the primary Kafka cluster associated with the Connect cluster. This is also the source cluster that forms one end of the connector pipeline.

  * [Create a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) to host your Pub/Sub Sink connector.

  * [Create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-client-library).

  * [Create and configure a Kafka topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic) within the source cluster. Data moves from this Kafka topic to the destination Pub/Sub topic.




### Required roles and permissions

To get the permissions that you need to create a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connector:

  * Create a connector: `managedkafka.connectors.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant permissions to publish to the Pub/Sub topic

The Managed Kafka service account must have permission to publish messages to the Pub/Sub topic. Grant the **Pub/Sub Publisher** (`roles/pubsub.publisher`) role to the service account on the project containing the Pub/Sub topic.

The Managed Kafka service account has the following format: `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where PROJECT_NUMBER is the project number of the Connect cluster.

If your Connect cluster is in a different project from your Managed Service for Apache Kafka cluster, see [ Create a Connect cluster in a different project](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#create-a-connect-cluster-in-a-different-project).

## How a Pub/Sub Sink connector works

A Pub/Sub Sink connector pulls messages from one or more Kafka topics and publishes them to a Pub/Sub topic.

Here's a detailed breakdown of how the Pub/Sub Sink connector copies data:

  * The connector consumes messages from one or more Kafka topics within the source cluster.

  * The connector writes messages to the target Pub/Sub topic ID that is specified by using the `cps.topic` configuration property. This is a required property.

  * The connector also requires the Google Cloud project containing the Pub/Sub topic to be specified by using the `cps.project` configuration property. This is a required property.

  * The connector can optionally also use a custom Pub/Sub endpoint that is specified by using the `cps.endpoint` property. The default endpoint is `"pubsub.googleapis.com:443"`.

  * To optimize performance, the connector buffers messages before publishing them to Pub/Sub. You can configure `maxBufferSize`, `maxBufferBytes`, `maxDelayThresholdMs`, `maxOutstandingRequestBytes`, and `maxOutstandingMessages` to control the buffering.

  * A Kafka record has three components: headers, keys, values. The connector uses key and value converters to transform the Kafka message data into the format expected by Pub/Sub. When using struct or map value schemas, the `messageBodyName` property specifies the field or key to use as the Pub/Sub message body.

  * The connector can include the Kafka topic, partition, offset, and timestamp as message attributes by using the `metadata.publish` property as set to `true`.

  * The connector can include Kafka message headers as Pub/Sub message attributes by using the `headers.publish` property as set to `true`.

  * The connector can include an ordering key for Pub/Sub messages by using the `orderingKeySource` property. Options for its value include `"none"` (default), `"key"`, and `"partition"`.

  * The `tasks.max` property controls the level of parallelism for the connector. Increasing `tasks.max` can improve throughput, but the actual parallelism is limited by the number of partitions in the Kafka topics.




## Properties of a Pub/Sub Sink connector

When creating a Pub/Sub Sink connector, you need to specify the following properties.

### Connector name

A unique name for the connector within the Connect cluster. For guidelines on naming resources, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

### Connector plugin type

Select **Pub/Sub Sink** as the connector plugin type. This determines the direction of data flow which is from Kafka _to_ Pub/Sub and the specific connector implementation used. If you don't use the user interface to configure the connector, you must also specify the connector class.

### Kafka topics

The Kafka topics from which the connector consumes messages. You can specify one or more topics, or use a regular expression to match multiple topics. For example, `topic.*` to match all topics starting with "topic". These topics must exist within the Managed Service for Apache Kafka cluster associated with your Connect cluster.

### Pub/Sub topic

The existing Pub/Sub topic to which the connector publishes messages. Ensure the Connect cluster service account has the `roles/pubsub.publisher` role on the topic's project, as described in Before you begin.

### Configuration

This section lets you specify additional, connector-specific configuration properties.

Since data in Kafka topics can be in various formats like Avro, JSON, or raw bytes, a key part of the configuration involves specifying converters. Converters translate data from the format used in your Kafka topics into the standardized, internal format of Kafka Connect. The Pub/Sub Sink connector then takes this internal data and transforms it into the format required by Pub/Sub before writing it.

For more general information about the role of converters in Kafka Connect, supported converter types, and common configuration options, see [converters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#converters).

Here are some configs specific to the Pub/Sub Sink connector:

  * **`cps.project`** : Specifies the Google Cloud project ID that contains the Pub/Sub topic.

  * **`cps.topic`** : Specifies the Pub/Sub topic to which data is published.

  * **`cps.endpoint`** : Specifies the Pub/Sub endpoint to use.




For a list of the available configuration properties specific to this connector, see the [Pub/Sub Sink connector configs](https://github.com/googleapis/java-pubsub-group-kafka-connector?tab=readme-ov-file#sink-connector).

## Create a Pub/Sub Sink connector

Before you create a connector, review the documentation for Properties of a Pub/Sub Sink connector.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster for which you want to create the connector.

The **Connect cluster details** page is displayed.

  3. Click **Create connector**.

The **Create Kafka connector** page is displayed.

  4. For the connector name, enter a string.

For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  5. For **Connector plugin** , select **Pub/Sub Sink**.

  6. Under **Topics** , choose either **Select a list of Kafka topics** or **Use a topic regex**. Then, select or enter the Kafka topic(s) from which this connector consumes messages. These topics are in your _associated Kafka cluster_.

  7. For **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic to which this connector publishes messages. The topic is displayed in the full resource name format: `projects/{project}/topics/{topic}`.

  8. (Optional) Configure additional settings in the **Configurations** section. This is where you would specify properties like `tasks.max`, `key.converter`, and `value.converter`, as discussed in the previous section.

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

     * CONFIG_FILE: The path to the YAML configuration file for the connector.

Here is an example of a configuration file for the Pub/Sub Sink connector:
    
    connector.class: "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector"
    name: "CPS_SINK_CONNECTOR_ID"
    tasks.max: "1"
    topics: "GMK_TOPIC_ID"
    value.converter: "org.apache.kafka.connect.storage.StringConverter"
    key.converter: "org.apache.kafka.connect.storage.StringConverter"
    cps.topic: "CPS_TOPIC_ID"
    cps.project: "GCP_PROJECT_ID"
    

Replace the following:

     * CPS_SINK_CONNECTOR_ID: The ID or name of the Pub/Sub Sink connector. For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a connector is immutable.

     * GMK_TOPIC_ID: The ID of the Managed Service for Apache Kafka topic from which data is read by the Pub/Sub Sink connector.

     * CPS_TOPIC_ID: The ID of the Pub/Sub topic to which data is published.

     * GCP_PROJECT_ID: The ID of the Google Cloud project where your Pub/Sub topic resides.




###  Terraform 

You can use a Terraform resource to create a [connector](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_connector).
    
    
    resource "google_managed_kafka_connector" "example-pubsub-sink-connector" {
      project         = data.google_project.default.project_id
      connector_id    = "my-pubsub-sink-connector"
      connect_cluster = google_managed_kafka_connect_cluster.default.connect_cluster_id
      location        = "us-central1"
    
      configs = {
        "connector.class" = "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector"
        "name"            = "my-pubsub-sink-connector"
        "tasks.max"       = "3"
        "topics"          = "TOPIC_NAME"
        "cps.topic"       = "CPS_TOPIC_NAME"
        "cps.project"     = "CPS_PROJECT_NAME"
        "value.converter" = "org.apache.kafka.connect.storage.StringConverter"
        "key.converter"   = "org.apache.kafka.connect.storage.StringConverter"
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
    
    // createPubSubSinkConnector creates a Pub/Sub Sink connector.
    func createPubSubSinkConnector(w io.Writer, projectID, region, connectClusterID, connectorID, topics, valueConverter, keyConverter, cpsTopic, cpsProject, tasksMax string, opts ...option.ClientOption) error {
    	// TODO(developer): Update with your config values. Here is a sample configuration:
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "CPS_SINK_CONNECTOR_ID"
    	// topics := "GMK_TOPIC_ID"
    	// valueConverter := "org.apache.kafka.connect.storage.StringConverter"
    	// keyConverter := "org.apache.kafka.connect.storage.StringConverter"
    	// cpsTopic := "CPS_TOPIC_ID"
    	// cpsProject := "GCP_PROJECT_ID"
    	// tasksMax := "3"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s", projectID, region, connectClusterID)
    
    	// Pub/Sub Sink sample connector configuration
    	config := map[string]string{
    		"connector.class": "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector",
    		"name":            connectorID,
    		"tasks.max":       tasksMax,
    		"topics":          topics,
    		"value.converter": valueConverter,
    		"key.converter":   keyConverter,
    		"cps.topic":       cpsTopic,
    		"cps.project":     cpsProject,
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
    	fmt.Fprintf(w, "Created Pub/Sub sink connector: %s\n", resp.Name)
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
    
    public class CreatePubSubSinkConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-pubsub-sink-connector";
        String pubsubProjectId = "my-pubsub-project-id";
        String pubsubTopicName = "my-pubsub-topic";
        String kafkaTopicName = "kafka-topic";
        String connectorClass = "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector";
        String maxTasks = "3";
        String valueConverter = "org.apache.kafka.connect.storage.StringConverter";
        String keyConverter = "org.apache.kafka.connect.storage.StringConverter";
        createPubSubSinkConnector(
            projectId,
            region,
            connectClusterId,
            connectorId,
            pubsubProjectId,
            pubsubTopicName,
            kafkaTopicName,
            connectorClass,
            maxTasks,
            valueConverter,
            keyConverter);
      }
    
      public static void createPubSubSinkConnector(
          String projectId,
          String region,
          String connectClusterId,
          String connectorId,
          String pubsubProjectId,
          String pubsubTopicName,
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
        configMap.put("topics", kafkaTopicName);
        configMap.put("value.converter", valueConverter);
        configMap.put("key.converter", keyConverter);
        configMap.put("cps.topic", pubsubTopicName);
        configMap.put("cps.project", pubsubProjectId);
    
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
          System.out.printf("Created Pub/Sub Sink connector: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html#com_google_cloud_managedkafka_v1_Connector_getName__)());
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
        "connector.class": "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector",
        "name": connector_id,
        "tasks.max": tasks_max,
        "topics": topics,
        "value.converter": value_converter,
        "key.converter": key_converter,
        "cps.topic": cps_topic,
        "cps.project": cps_project,
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

## What's next?

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
