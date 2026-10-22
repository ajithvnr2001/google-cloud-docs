---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connectors/
title: List all connectors \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:22.234052+00:00
---

# List all connectors  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List all connectors Stay organized with collections  Save and categorize content based on your preferences. 

Listing all connectors running in a Connect cluster provides an overview of the data integrations that are configured. You can monitor the health and status of your connectors, identify potential issues, and manage your data flows effectively.

To list all connectors in a Connect cluster, you can use the Google Cloud console, the gcloud CLI, the Managed Service for Apache Kafka client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to list the connectors.

## Required roles and permissions to list all connectors

To get the permissions that you need to list all connectors, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list all connectors. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list all connectors:

  * Grant the list connectors permission on the parent Connect cluster: `managedkafka.connectors.list`
  * Grant the get connector details permission on the parent Connect cluster: `managedkafka.connectors.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View all connectors

This view provides a quick way to monitor the status of your connectors and identify any that require attention. You can then drill down into individual connectors to view their details and configurations if needed.

###  Console 

  1. In the Google Cloud console, go to the **Connect clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster for which you want to list the connectors.

The **Connect cluster details** page is displayed.

  3. The **Resources** tab displays a list of all connectors running in the cluster. The list includes the following information for each connector:

     * **Name** : The name of the connector.
     * **State** : The operational state of the connector. For example, Running, Failed.
     * **Connector type** : The type of connector plugin.

You can use the **Filter** option to search for specific connectors by name.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connectors list`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/list) command to list connectors:
         
         gcloud managed-kafka connectors list CONNECT_CLUSTER_ID \
             --location=LOCATION
         

  3. To further refine the list of connectors, you can use additional flags:
         
         gcloud managed-kafka connectors list CONNECT_CLUSTER_ID \
             --location=LOCATION \
             [--filter=EXPRESSION] \
             [--limit=LIMIT] \
             [--page-size=PAGE_SIZE] \
             [--sort-by=SORT_BY]
         

Replace the following:

     * CONNECT_CLUSTER_ID: Required. The ID of the Connect cluster containing the connectors you want to list.
     * LOCATION: Required. The location of the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) containing the connectors that you want to list.
     * EXPRESSION: (Optional) A Boolean filter expression to apply to the list. If the expression evaluates to `True`, the item is included in the list. For more details and examples, run `gcloud topic filters`.

Examples:

       * To list only connectors that are in the 'RUNNING' state:
             
             --filter="state=RUNNING"
             

       * To list only 'Pub/Sub Sink' connectors:
             
             --filter="connector_plugin='Pub/Sub Sink'"
             

       * To list connectors with a name containing 'prod':
             
             --filter="name ~ 'prod'"
             

       * To list connectors that are either 'FAILED' or are 'Pub/Sub Source' plugins:
             
             --filter="state=FAILED OR connector_plugin='Pub/Sub Source'"
             

     * LIMIT: (Optional) The maximum number of connectors to display. If not specified, all connectors are listed.

     * PAGE_SIZE: (Optional) The number of results to display per page. If not specified, the service determines a suitable page size.

     * SORT_BY: (Optional) A comma-separated list of fields to sort by. The default sort order is ascending. To sort in descending order, prefix the field with `~`. Supported fields are likely `name` and `state`.




Example command with sorting:
    
    
    gcloud managed-kafka connectors list test-connect-cluster \
        --location=us-central1 \
        --sort-by=~state,name
    

Example command with filtering and limiting:
    
    
    gcloud managed-kafka connectors list test-connect-cluster \
        --location=us-central1 \
        --filter="state=RUNNING AND connector_plugin='Pub/Sub Sink'" \
        --limit=5
    

Example output:
    
    
    NAME                                    STATE     CONNECTOR_PLUGIN
    pubsub-sink-connector                   RUNNING   Pub/Sub Sink
    another-pubsub-sink                     RUNNING   Pub/Sub Sink
    prod-pubsub-sink                        RUNNING   Pub/Sub Sink
    

### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func listConnectors(w io.Writer, projectID, region, connectClusterID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s", projectID, region, connectClusterID)
    	req := &managedkafkapb.ListConnectorsRequest{
    		Parent: parent,
    	}
    	connectorIter := client.ListConnectors(ctx, req)
    	for {
    		connector, err := connectorIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("connectorIter.Next() got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got connector: %v", connector)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html);
    import com.google.cloud.managedkafka.v1.[Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import java.io.IOException;
    
    public class ListConnectors {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-connect-cluster";
        listConnectors(projectId, region, clusterId);
      }
    
      public static void listConnectors(String projectId, String region, String clusterId)
          throws IOException {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html) parent = [ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html).of(projectId, region, clusterId);
          // This operation is handled synchronously.
          for ([Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) connector : managedKafkaConnectClient.listConnectors(parent).iterateAll()) {
            System.out.println(connector.getAllFields());
          }
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.listConnectors got err: %s\n", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html),
    )
    from google.api_core.exceptions import GoogleAPICallError
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    
    connect_client = ManagedKafkaConnectClient()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ListConnectorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectorsRequest.html)(
        parent=connect_client.[connect_cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connect_cluster_path)(project_id, region, connect_cluster_id),
    )
    
    try:
        response = connect_client.[list_connectors](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_list_connectors)(request=request)
        for connector in response:
            print("Got connector:", connector)
    except GoogleAPICallError as e:
        print(f"Failed to list connectors with error: {e}")
    

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
