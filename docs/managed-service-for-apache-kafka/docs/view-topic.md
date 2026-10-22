---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-topic/
title: View a Google Cloud Managed Service for Apache Kafka topic \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:13.474096+00:00
---

# View a Google Cloud Managed Service for Apache Kafka topic  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  View a Google Cloud Managed Service for Apache Kafka topic Stay organized with collections  Save and categorize content based on your preferences. 

To view the detailed information about a single topic, you can use the Google Cloud console, the Google Cloud CLI, the client library, the Managed Kafka API, or the open source Apache Kafka APIs.

## Required roles and permissions to view a topic

To get the permissions that you need to view a topic, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view a topic. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view a topic:

  * List topics: `managedkafka.topics.list`
  * Get topic: `managedkafka.topics.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Topic properties in the console

In the console, you can view the following topic properties:

  * **Configurations** : This tab provides general configuration details about the topic, including the following:

    * **Name** : The unique identifier of the topic within the cluster.

    * **Partitions** : The number of partitions in the topic. Partitions divide the topic's data into segments for scalability and parallelism.

    * **Replicas** : The number of copies (replicas) maintained for each partition to ensure data redundancy and availability.

    * **Cluster** : The name of the Managed Service for Apache Kafka cluster to which the topic belongs.

    * **Region** : The Google Cloud region where the cluster and the topic is located.

    * **Non-default topic parameters** : Any topic-level configuration overrides that have been set for the topic, different from the cluster-wide defaults.

  * **Monitoring** : This tab provides visual charts that display key metrics related to the topic's activity and performance. These charts include the following:

    * **Byte count** : A time-series chart showing the rate at which bytes are produced or sent to the topic. This indicates the volume of data published to the topic over time. The corresponding metric is `managedkafka.googleapis.com/byte_in_count`.

    * **Request count** : A time-series chart representing the rate of requests made to the topic. It reflects the overall activity and usage of the topic. The related metric is `managedkafka.googleapis.com/topic_request_count`.

    * **Log segments by partition** : This chart displays the number of active log segments for each partition within the topic. Log segments are the physical files on disk where Kafka stores the topic data. The relevant metric is `managedkafka.googleapis.com/log_segments`.

  * **Consumer groups** : This section lists the consumer groups that are subscribed to the topic. A consumer group is a set of consumers that work together to read messages from the topic.




## View a topic

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

The clusters that you created in a project are listed.

  2. Click the cluster for which you want to see the topics.

The cluster details page is displayed. In the cluster details page, for the **Resources** tab, the topics are listed.

  3. To view a specific topic, click the topic name.

The topic details page is displayed. 




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka topics describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/describe) command:
         
         gcloud managed-kafka topics describe TOPIC_ID \
           --cluster=CLUSTER_ID --location=LOCATION_ID
         

This command fetches and displays comprehensive details about the specified topic. This information includes its configuration settings, such as the number of partitions, replication factor, and any topic-level configuration overrides.

Replace the following:

     * TOPIC_ID: The ID of the topic.
     * CLUSTER_ID: The ID of the cluster containing the topic.
     * LOCATION_ID: The location of the cluster.



The `gcloud managed-kafka topics describe` command displays minimal information about a topic, such as the partition count and the replication factor. To get more detailed information, including partition assignments and the full set of configuration settings, use the `kafka-topics.sh` command-line tool.

###  Kafka CLI 

Before running this command, install the Kafka command-line tools on a Compute Engine VM. The VM must be able to reach a subnet that is connected to your Managed Service for Apache Kafka cluster. Follow the instructions in [ Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart). 

To view details about a topic, run the `kafka-topics.sh --describe` command:
    
    
    kafka-topics.sh --describe \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties \
      --topic TOPIC_ID
    

Replace the following:

  * BOOTSTRAP_ADDRESS: The [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address) of the Managed Service for Apache Kafka cluster.
  * TOPIC_ID: The ID of the topic.



This command returns a subset of the topic's properties, including the following:

  * Partition count
  * Replication factor
  * Partition assignments
  * Dynamic configuration (settings that you have explicitly set)
  * Static configuration (settings that are applied when the cluster is started)



To view the complete set of configuration settings for a topic, including settings with default values, run the `kafka-configs.sh --describe` command:
    
    
    kafka-configs.sh --describe \
    --bootstrap-server=BOOTSTRAP_ADDRESS \
    --command-config client.properties \
    --entity-type topics \
    --entity-name TOPIC_ID \
    --all
    

The output is a list of settings as key-value pairs. The `--all` flag returns all configuration settings. To get a list of only dynamic configuration settings, omit the `--all` flag.

###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster 
  * `CLUSTER_ID`: the ID of the cluster 
  * `TOPIC_ID`: the ID of the topic 



HTTP method and URL: 
    
    
    GET https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID",
      "partitionCount": PARTITION_COUNT,
      "replicationFactor": REPLICATION_FACTOR
    }
    

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
    
    func getTopic(w io.Writer, projectID, region, clusterID, topicID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	topicPath := fmt.Sprintf("%s/topics/%s", clusterPath, topicID)
    	req := &managedkafkapb.GetTopicRequest{
    		Name: topicPath,
    	}
    	topic, err := client.GetTopic(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetTopic got err: %w", err)
    	}
    	fmt.Fprintf(w, "Got topic: %#v\n", topic)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import com.google.cloud.managedkafka.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html);
    import com.google.cloud.managedkafka.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html);
    import java.io.IOException;
    
    public class GetTopic {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        String topicId = "my-topic";
        getTopic(projectId, region, clusterId, topicId);
      }
    
      public static void getTopic(String projectId, String region, String clusterId, String topicId)
          throws Exception {
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create()) {
          // This operation is being handled synchronously.
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html) topic =
              managedKafkaClient.getTopic([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html).of(projectId, region, clusterId, topicId));
          System.out.println(topic.getAllFields());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaClient.getTopic got err: %s", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    # topic_id = "my-topic"
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    topic_path = client.[topic_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_topic_path)(project_id, region, cluster_id, topic_id)
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[GetTopicRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetTopicRequest.html)(
        name=topic_path,
    )
    
    try:
        topic = client.[get_topic](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_get_topic)(request=request)
        print("Got topic:", topic)
    except NotFound as e:
        print(f"Failed to get topic {topic_id} with error: {e.message}")
    

## What's next?

  * [Delete a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-topic)

  * [Edit a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic)

  * [List all consumer groups](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-consumer-groups)

  * [View a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-consumer-group)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
