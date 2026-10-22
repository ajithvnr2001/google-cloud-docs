---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector/
title: Update a connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:22.880140+00:00
---

# Update a connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Update a connector Stay organized with collections  Save and categorize content based on your preferences. 

You can edit a connector to update its configuration, such as changing the topics it reads from or writes to, modifying data transformations, or adjusting error handling settings.

To update a connector in a Connect cluster, you can use the Google Cloud console, the gcloud CLI, the Managed Service for Apache Kafka client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to update the connectors.

## Before you begin

Before updating a connector, review its existing configuration and understand the potential impact of any changes you make.

## Required roles and permissions to update a connector

To get the permissions that you need to edit a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on the project containing the Connect cluster. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to edit a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to edit a connector:

  * Grant the update connector permission on the parent Connect cluster: `managedkafka.connectors.update`
  * Grant the list connectors permission on the parent Connect cluster: This permission is only required for updating a connector using the Google Cloud console 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Editable properties of a connector

The editable properties of a connector depend on its type. Here's a summary of the editable properties for the supported connector types:

### MirrorMaker 2.0 Source connector

  * **Comma-separated topic names or topic regex** : The topics to be replicated.

For more information about the property, see [Topic names](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector#topic-names-or-regular-expressions).

  * **Configuration** : Additional configuration settings for the connector.

For more information about the property, see [ Configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector#configuration).

  * **Task restart policy** : The policy for restarting failed connector tasks.

For more information about the property, see [ Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).




### BigQuery Sink connector

  * **Topics** : The Kafka topics from which to stream data. 

For more information about the property, see [Topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector#topics).

  * **Dataset** : The BigQuery dataset to store the data. 

For more information about the property, see [Dataset](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector#dataset).

  * **Configuration** : Additional configuration settings for the connector. 

For more information about the property, see [Configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector#configuration).

  * **Task restart policy** : The policy for restarting failed connector tasks. 

For more information about the property, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).




### Cloud Storage Sink connector

  * **Topics** : The Kafka topics from which to stream data. 

For more information about the property, see [Topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector#topics).

  * **Cloud Storage bucket** : The Cloud Storage bucket to store the data. 

For more information about the property, see [Bucket](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector#gcs-bucket).

  * **Configuration** : Additional configuration settings for the connector. 

For more information about the property, see [Configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector#configuration).

  * **Task restart policy** : The policy for restarting failed connector tasks. 

For more information about the property, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).




### Pub/Sub Source connector

  * **Pub/Sub subscription** : The Pub/Sub subscription from which to receive messages. 
  * **Kafka topic** : The Kafka topic to which to stream messages. 
  * **Configuration** : Additional configuration settings for the connector. For more information, see [ Configure the connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector#configuration). 
  * **Task restart policy** : The policy for restarting failed connector tasks. For more information, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy). 



### Pub/Sub Sink connector

  * **Topics** : The Kafka topics from which to stream messages. 

For more information about the property, see [Topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector#kafka-topics).

  * **Pub/Sub topic** : The Pub/Sub topic to which to send messages. 

For more information about the property, see [Pub/Sub topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector#pubsub-topic).

  * **Configuration** : Additional configuration settings for the connector. 

For more information about the property, see [Configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector#configuration).

  * **Task restart policy** : The policy for restarting failed connector tasks. 

For more information about the property, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).




## Update a connector

Updating a connector may cause a temporary interruption in data flow while the changes are applied.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster that hosts the connector you want to update.

The **Connect cluster details** page is displayed.

  3. On the **Resources** tab, find the connector in the list and click its name.

You are redirected to the **Connector details** page.

  4. Click **Edit**.

  5. Update the required properties for the connector. The available properties vary depending on the connector type.

  6. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connectors update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/update) command to update a connector:

You can update a connector's configuration using either the `--configs` flag with comma-separated key-value pairs or the `--config-file` flag with a path to a JSON or YAML file.

Here is the syntax that uses the `--configs` flag with comma-separated key-value pairs.
         
         gcloud managed-kafka connectors update CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID \
             --configs=KEY1=VALUE1,KEY2=VALUE2...
         

Here is the syntax that uses the `--config-file` flag with a path to a JSON or YAML file.
         
         gcloud managed-kafka connectors update CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID \
             --config-file=PATH_TO_CONFIG_FILE
         

Replace the following:

     * CONNECTOR_ID: Required. The ID of the connector you want to update.
     * LOCATION: Required. The location of the Connect cluster containing the connector.
     * CONNECT_CLUSTER_ID: Required. The ID of the Connect cluster containing the connector.
     * KEY1=VALUE1,KEY2=VALUE2...: Comma-separated configuration properties to update. For example, `tasks.max=2,value.converter.schemas.enable=true`.
     * PATH_TO_CONFIG_FILE: The path to a JSON or YAML file containing the configuration properties to update. For example, `config.json`.

Example command using `--configs`:
    
    gcloud managed-kafka connectors update test-connector \
        --location=us-central1 \
        --connect-cluster=test-connect-cluster \
        --configs=tasks.max=2,value.converter.schemas.enable=true
    

Example command using `--config-file`. The following is a sample file that is named `update_config.yaml`:
    
    tasks.max: 3
    topic: updated-test-topic
    

The following is a sample command that uses the file:
    
    gcloud managed-kafka connectors update test-connector \
        --location=us-central1 \
        --connect-cluster=test-connect-cluster \
        --config-file=update_config.yaml
    




### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func updateConnector(w io.Writer, projectID, region, connectClusterID, connectorID string, config map[string]string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "my-connector"
    	// config := map[string]string{"tasks.max": "6"}
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	connectorPath := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s/connectors/%s", projectID, region, connectClusterID, connectorID)
    	connector := &managedkafkapb.Connector{
    		Name:    connectorPath,
    		Configs: config,
    	}
    	paths := []string{"configs"}
    	updateMask := &fieldmaskpb.FieldMask{
    		Paths: paths,
    	}
    
    	req := &managedkafkapb.UpdateConnectorRequest{
    		UpdateMask: updateMask,
    		Connector:  connector,
    	}
    	resp, err := client.UpdateConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.UpdateConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Updated connector: %#v\n", resp)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class UpdateConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-connect-cluster";
        String connectorId = "my-connector";
        // The new value for the 'tasks.max' configuration.
        String maxTasks = "5";
        updateConnector(projectId, region, clusterId, connectorId, maxTasks);
      }
    
      public static void updateConnector(
          String projectId, String region, String clusterId, String connectorId, String maxTasks)
          throws IOException {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          Map<String, String> configMap = new HashMap<>();
          configMap.put("tasks.max", maxTasks);
    
          [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) connector =
              [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html).newBuilder()
                  .setName([ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, clusterId, connectorId).toString())
                  .putAllConfigs(configMap)
                  .build();
    
          // The field mask specifies which fields to update. Here, we update the 'config' field.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("config").build();
    
          // This operation is handled synchronously.
          [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) updatedConnector = managedKafkaConnectClient.updateConnector(connector, updateMask);
          System.out.printf("Updated connector: %s\n", updatedConnector.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html#com_google_cloud_managedkafka_v1_Connector_getName__)());
          System.out.println(updatedConnector.getAllFields());
    
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.updateConnector got err: %s\n", e.getMessage());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html),
    )
    from google.cloud.managedkafka_v1.types import [Connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Connector.html)
    from google.protobuf import field_mask_pb2
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    # connector_id = "my-connector"
    # configs = {
    #     "tasks.max": "6",
    #     "value.converter.schemas.enable": "true"
    # }
    
    connect_client = ManagedKafkaConnectClient()
    
    connector = Connector()
    connector.name = connect_client.[connector_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connector_path)(
        project_id, region, connect_cluster_id, connector_id
    )
    connector.configs = configs
    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.append("config")
    
    # For a list of editable fields, one can check https://cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector#editable-properties.
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[UpdateConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateConnectorRequest.html)(
        update_mask=update_mask,
        connector=connector,
    )
    
    try:
        operation = connect_client.[update_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_update_connector)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        response = operation.result()
        print("Updated connector:", response)
    except GoogleAPICallError as e:
        print(f"The operation failed with error: {e}")
    
    
    
    You can also update the connector's task restart policy without
    including the configuration, by using the `--task-restart-min-backoff`
    and `--task-restart-max-backoff` flags. For example:
    
    ```sh
    gcloud managed-kafka connectors update test-connector \
      --location=us-central1 \
      --connect-cluster=test-connect-cluster \
      --task-restart-min-backoff="60s" \
      --task-restart-max-backoff="90s"
    

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
