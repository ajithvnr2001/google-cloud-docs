---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connector/
title: View a connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:14.824265+00:00
---

# View a connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  View a connector Stay organized with collections  Save and categorize content based on your preferences. 

Viewing a connector's details lets you inspect its configuration, operational state, task restart policy, and monitor its performance metrics.

To view the details of a connector in a Connect cluster, you can use the Google Cloud console, the gcloud CLI, the Managed Service for Apache Kafka client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to view the connectors.

## Required roles and permissions to view a connector

To get the permissions that you need to view a connector, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view a connector:

  * Grant the list connectors permission on the parent Connect cluster: `managedkafka.connectors.list`
  * Grant the get connector details permission on the parent Connect cluster: `managedkafka.connectors.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View connector details

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster that hosts the connector you want to view.

The **Connect cluster details** page is displayed.

  3. On the **Resources** tab, find the connector in the list and click its name. You are redirected to the **Connector details** page.

  4. The **Connector details** page displays the following tabs:

     * **Configuration** : Shows the connector's configuration, including: 
       * **Name** : The name of the connector.
       * **State** : The operational state of the connector. For example, Running.
       * **Task restart policy** : The policy for restarting failed tasks. For example, whether to restart failed tasks or not, and with which backoff settings.
       * **Configuration properties** : A list of key-value pairs defining the connector's configuration.
     * **Monitoring** : Provides graphs for monitoring the connector, such as: 
       * **Task error count** : The number of tasks that have encountered errors.
       * **Active task count** : The number of tasks that are currently active.

This page also includes buttons to **edit** , **delete** , **pause** , **stop** , and **restart** the connector.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connectors describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/describe) command to describe a connector:
         
         gcloud managed-kafka connectors describe CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID
         

Replace the following:

     * CONNECTOR_ID: Required. The ID of the connector you want to describe.
     * LOCATION: Required. The location of the Connect cluster containing the connector.
     * CONNECT_CLUSTER_ID: Required. The ID of the Connect cluster containing the connector.



Example command:
    
    
    gcloud managed-kafka connectors describe test-connector \
      --location=us-central1 \
      --connect-cluster=test-connect-cluster
    

Example output:
    
    
    config:
      connector.class: com.google.cloud.kafka.connect.pubsub.PubsubSinkConnector
      kafka.topic.regex: .*
      key.converter: org.apache.kafka.connect.storage.StringConverter
      project: test-project
      tasks.max: '1'
      topic: test-pubsub-topic
      value.converter: org.apache.kafka.connect.json.JsonConverter
      value.converter.schemas.enable: 'false'
    createTime: '2024-03-13T05:17:34.123456Z'
    labels:
      test-label-key: test-label-value
    name: projects/test-project/locations/us-central1/connectClusters/test-connect-cluster/connectors/test-connector
    state: RUNNING
    taskRestartPolicy: RESTART_WITH_EXPONENTIAL_BACKOFF
    updateTime: '2024-03-13T05:18:15.987654Z'
    

### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func getConnector(w io.Writer, projectID, region, connectClusterID, connectorID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "my-connector"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	connectorPath := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s/connectors/%s", projectID, region, connectClusterID, connectorID)
    	req := &managedkafkapb.GetConnectorRequest{
    		Name: connectorPath,
    	}
    	connector, err := client.GetConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Got connector: %#v\n", connector)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import java.io.IOException;
    
    public class GetConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-connect-cluster";
        String connectorId = "my-connector";
        getConnector(projectId, region, clusterId, connectorId);
      }
    
      public static void getConnector(
          String projectId, String region, String clusterId, String connectorId) throws IOException {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html) name = [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, clusterId, connectorId);
          // This operation is handled synchronously.
          [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) connector = managedKafkaConnectClient.getConnector(name);
          System.out.println(connector.getAllFields());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.getConnector got err: %s\n", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html)
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    # connector_id = "my-connector"
    
    connect_client = ManagedKafkaConnectClient()
    
    connector_path = connect_client.[connector_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connector_path)(
        project_id, region, connect_cluster_id, connector_id
    )
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[GetConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetConnectorRequest.html)(
        name=connector_path,
    )
    
    try:
        connector = connect_client.[get_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_get_connector)(request=request)
        print("Got connector:", connector)
    except NotFound as e:
        print(f"Failed to get connector {connector_id} with error: {e}")
    

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
