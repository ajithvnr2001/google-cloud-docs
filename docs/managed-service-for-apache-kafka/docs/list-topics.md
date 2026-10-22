---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-topics/
title: List your Google Cloud Managed Service for Apache Kafka topics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:35.138772+00:00
---

# List your Google Cloud Managed Service for Apache Kafka topics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-topics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List your Google Cloud Managed Service for Apache Kafka topics Stay organized with collections  Save and categorize content based on your preferences. 

To list your topics in a cluster, you can use the Google Cloud console, the Google Cloud CLI, the client library, the Managed Kafka API, or the open source Apache Kafka APIs.

## Required roles and permissions to list your topics

To get the permissions that you need to list your topics, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list your topics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list your topics:

  * List topics: `managedkafka.topics.list`
  * Get topic: `managedkafka.topics.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List your topics

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

The clusters you created in a project are listed.

  2. Click the cluster for which you want to see the topics.

The cluster details page is displayed. In the cluster details page, for the **Resources** tab, the topics are listed.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka topics list`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/list) command:
         
         gcloud managed-kafka topics list CLUSTER_ID \
             --location=LOCATION_ID \
             --limit=LIMIT
         

This command retrieves a list of all topics present within the specified Managed Service for Apache Kafka cluster. You can use optional flags to filter, limit, and sort the output.

Replace the following:

     * CLUSTER_ID: The name of the cluster whose topics you want to list.
     * LOCATION_ID: The location of the cluster.
     * LIMIT: (Optional) The maximum number of topics to list.



###  Kafka CLI 

Before running this command, install the Kafka command-line tools on a Compute Engine VM. The VM must be able to reach a subnet that is connected to your Managed Service for Apache Kafka cluster. Follow the instructions in [ Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart). 

Run the `kafka-topics.sh` command as follows:
    
    
    kafka-topics.sh --list \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties
    

Replace the following:

  * BOOTSTRAP_ADDRESS: The [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address) of the Managed Service for Apache Kafka cluster.



###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster 
  * `CLUSTER_ID`: the ID of the cluster 



HTTP method and URL: 
    
    
    GET https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "topics": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/__remote_log_metadata",
          "partitionCount": 50,
          "replicationFactor": 3,
          "configs": {
            "remote.storage.enable": "false",
            "cleanup.policy": "delete",
            "retention.ms": "-1"
          }
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID",
          "partitionCount": 3,
          "replicationFactor": 3
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
    
    func listTopics(w io.Writer, projectID, region, clusterID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	req := &managedkafkapb.ListTopicsRequest{
    		Parent: clusterPath,
    	}
    	topicIter := client.ListTopics(ctx, req)
    	for {
    		res, err := topicIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("topicIter.Next() got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got topic: %v", res)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import com.google.cloud.managedkafka.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html);
    import java.io.IOException;
    
    public class ListTopics {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        listTopics(projectId, region, clusterId);
      }
    
      public static void listTopics(String projectId, String region, String clusterId)
          throws Exception {
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create()) {
          [ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html) clusterName = [ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html).of(projectId, region, clusterId);
          // This operation is being handled synchronously.
          for ([Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html) topic : managedKafkaClient.listTopics(clusterName).iterateAll()) {
            System.out.println(topic.getAllFields());
          }
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaClient.listTopics got err: %s", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
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
    # cluster_id = "my-cluster"
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ListTopicsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListTopicsRequest.html)(
        parent=client.[cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_cluster_path)(project_id, region, cluster_id),
    )
    
    response = client.[list_topics](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_list_topics)(request=request)
    for topic in response:
        print("Got topic:", topic)
    

**Note:** You might see a topic named `__remote_log_metadata` in the list. Managed Service for Apache Kafka creates this topic to support [Tiered storage](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview#storage). Don't delete this topic, as doing so prevents your cluster from reading and writing data.

## What's next?

  * [Monitor your topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster)

  * [View a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-topic)

  * [Edit a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic)

  * [Delete a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-topic)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
