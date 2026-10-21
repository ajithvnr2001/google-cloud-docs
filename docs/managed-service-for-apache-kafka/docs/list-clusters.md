---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-clusters/
title: List your Google Cloud Managed Service for Apache Kafka clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:21.228517+00:00
---

# List your Google Cloud Managed Service for Apache Kafka clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List your Google Cloud Managed Service for Apache Kafka clusters Stay organized with collections  Save and categorize content based on your preferences. 

To list your clusters, you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to list a cluster.

## Required roles and permissions to list your clusters

To get the permissions that you need to list your clusters, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list your clusters. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list your clusters:

  * List clusters: `managedkafka.clusters.list`
  * Get cluster details: `managedkafka.clusters.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List your clusters

To list all your clusters in a project, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. The clusters you created in a project are listed. The page lets you view the following cluster properties:

     * **Cluster name** : The unique identifier for your Managed Service for Apache Kafka cluster. You can use it to reference the cluster in various operations.
     * **Cluster state** : Indicates the current [operational status](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rpc/google.cloud.managedkafka.v1#google.cloud.managedkafka.v1.Cluster.State) of the cluster, such as **Active**.
     * **Region** : The geographical location where your cluster is hosted.
     * **Bootstrap URL** : The [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address) that Kafka clients use to connect to the cluster.
     * **Memory** : The total amount of memory allocated to the cluster. This determines the capacity for handling message traffic and storage.
     * **vCPU** : The number of vCPUs assigned to the cluster. This affects the cluster's processing power and ability to handle concurrent operations.
     * **Labels** : Key-value pairs that you can attach to the cluster for organization, filtering, and automation purposes.
  3. Optional: To find the cluster associated with a specific bootstrap address, enter the bootstrap URL in the **Filter** field.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka clusters list`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/list) command:
         
         gcloud managed-kafka clusters list --location=LOCATION \
             --limit=LIMIT
         

To find the cluster associated with a specific bootstrap address, filter by the `bootstrapAddress` field:
         
         gcloud managed-kafka clusters list --location=LOCATION \
             --filter="bootstrapAddress:BOOTSTRAP_ADDRESS"
         

Replace the following:

     * LOCATION: The location (region) of the cluster, such as `us-central1`. The region is also included as the third dot-separated segment of the bootstrap URL.
     * LIMIT: The maximum number of clusters to list.
     * BOOTSTRAP_ADDRESS: The bootstrap URL or hostname of the cluster.



###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster 



HTTP method and URL: 
    
    
    GET https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "clusters": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID",
          "createTime": "CREATE_TIME",
          "updateTime": "UPDATE_TIME",
          "capacityConfig": {
            "vcpuCount": "CPU_COUNT",
            "memoryBytes": "MEMORY"
          },
          "rebalanceConfig": {},
          "gcpConfig": {
            "accessConfig": {
              "networkConfigs": [
                {
                  "subnet": "projects/PROJECT_ID/locations/LOCATION/subnetworks/SUBNET_ID"
                }
              ]
            }
          },
          "state": "ACTIVE",
          "satisfiesPzi": false,
          "satisfiesPzs": false,
          "tlsConfig": {
            "trustConfig": {}
          },
          "updateOptions": {}
        }
      ]
    }
    

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
    
    func listClusters(w io.Writer, projectID, region string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	locationPath := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    	req := &managedkafkapb.ListClustersRequest{
    		Parent: locationPath,
    	}
    	clusterIter := client.ListClusters(ctx, req)
    	for {
    		res, err := clusterIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("clusterIter.Next() got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got cluster: %v", res)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html);
    import com.google.cloud.managedkafka.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import java.io.IOException;
    
    public class ListClusters {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        listClusters(projectId, region);
      }
    
      public static void listClusters(String projectId, String region) throws Exception {
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create()) {
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html).of(projectId, region);
          // This operation is being handled synchronously.
          for ([Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html) cluster : managedKafkaClient.listClusters(locationName).iterateAll()) {
            System.out.println(cluster.getAllFields());
          }
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaClient.listClusters got err: %s", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ListClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListClustersRequest.html)(
        parent=client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_common_location_path)(project_id, region),
    )
    
    response = client.[list_clusters](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_list_clusters)(request=request)
    for cluster in response:
        print("Got cluster:", cluster)
    

## What's next?

  * [Monitor your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster).

  * [View your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster).

  * [Create a topic within your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic).

  * [Edit a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster).

  * [Delete your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-cluster).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
