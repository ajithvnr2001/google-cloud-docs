---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connect-cluster/
title: List your Connect clusters \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:15:25.544509+00:00
---

# List your Connect clusters  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connect-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List your Connect clusters Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Kafka lets you view the operational status, resource allocation, and configuration details for all of your Connect clusters. This consolidated view helps you to manage your Connect clusters in one place.

To list your Connect clusters, you can use the Google Cloud console, the gcloud CLI, the client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to list Connect clusters.

## Required roles and permissions to list your Connect clusters

To get the permissions that you need to list your Connect clusters, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list your Connect clusters. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list your Connect clusters:

  * Grant the list clusters permission on the specified location: `managedkafka.connectClusters.list`
  * Grant the get cluster details permission on the specified location: `managedkafka.connectClusters.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View your Connect clusters

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. The clusters you created in a project are listed. The page lets you view the following cluster properties:

     * **Name** : The unique identifier for your Connect cluster. You can use it to reference the Connect cluster in various operations.
     * **State** : Indicates the current operational status of the Connect cluster, such as **Active**.
     * **Location** : The geographical location where your Connect cluster is hosted.
     * **Update time** : The time the Connect cluster was last updated.
     * **vCPUs** : The number of vCPUs assigned to the Connect cluster.
     * **Memory** : The total amount of memory allocated to the Connect cluster.
     * **Primary Kafka cluster** : The Managed Service for Apache Kafka cluster associated with the Connect cluster.
     * **Labels** : Key-value pairs that you can attach to the Connect cluster for organization, filtering, and automation purposes.



###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connect-clusters list`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/list) command to list Connect clusters:
         
         gcloud managed-kafka connect-clusters list \
             --location=LOCATION
         

  3. To further refine the list of Connect clusters, you can use additional flags:
         
         gcloud managed-kafka connect-clusters list \
             --location=LOCATION \
             [--filter=EXPRESSION] \
             [--limit=LIMIT] \
             [--page-size=PAGE_SIZE] \
             [--sort-by=SORT_BY]
         

Replace the following:

     * LOCATION: Required. The location of the Connect clusters you want to list.

     * EXPRESSION: (Optional) A boolean filter expression to apply to the list. If the expression evaluates to `True`, the item is included in the list. For more details and examples, run `gcloud topic filters`.

     * LIMIT: (Optional) The maximum number of Connect clusters to display. If not specified, all Connect clusters are listed.

     * PAGE_SIZE: (Optional) The number of results to display per page. If not specified, the service determines a suitable page size.

     * SORT_BY: (Optional) A comma-separated list of fields to sort by. The default sort order is ascending. To sort in descending order, prefix the field with `~`.




Example output:
    
    
    NAME                   VCPU  MEMORY_BYTES  STATE   NETWORK
    connect-cluster-alpha  3     3221225472    ACTIVE
    connect-cluster-beta   3     3221225472    ACTIVE
    
    

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
    
    func listConnectClusters(w io.Writer, projectID, region string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	locationPath := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    	req := &managedkafkapb.ListConnectClustersRequest{
    		Parent: locationPath,
    	}
    	clusterIter := client.ListConnectClusters(ctx, req)
    	for {
    		res, err := clusterIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("clusterIter.Next() got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got connect cluster: %v", res)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html);
    import com.google.cloud.managedkafka.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import java.io.IOException;
    
    public class ListConnectClusters {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        listConnectClusters(projectId, region);
      }
    
      public static void listConnectClusters(String projectId, String region) throws Exception {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = 
            [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html).of(projectId, region);
          // This operation is being handled synchronously.
          for ([ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html) connectCluster : managedKafkaConnectClient
              .listConnectClusters(locationName).iterateAll()) {
            System.out.println(connectCluster.getAllFields());
          }
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.listConnectClusters got err: %s\n", 
              e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
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
    
    connect_client = ManagedKafkaConnectClient()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ListConnectClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectClustersRequest.html)(
        parent=connect_client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_common_location_path)(project_id, region),
    )
    
    response = connect_client.[list_connect_clusters](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_list_connect_clusters)(request=request)
    for cluster in response:
        try:
            print("Got Connect cluster:", cluster)
        except GoogleAPICallError as e:
            print(f"Failed to list Connect clusters with error: {e}")
    

## What's next?

  * [View a Connect clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connect-cluster)

  * [Update a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connect-cluster)

  * [Delete a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/delete-connect-cluster)

  * [An overview of connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
