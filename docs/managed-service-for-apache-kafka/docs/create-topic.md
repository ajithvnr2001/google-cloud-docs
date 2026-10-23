---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic/
title: Create a Google Cloud Managed Service for Apache Kafka topic \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:09.115973+00:00
---

# Create a Google Cloud Managed Service for Apache Kafka topic  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Google Cloud Managed Service for Apache Kafka topic Stay organized with collections  Save and categorize content based on your preferences. 

In Managed Service for Apache Kafka, messages are organized in topics. A topic is made up of partitions. A partition is an ordered, immutable sequence of records that is owned by a single broker within a Kafka cluster. You must create a topic to publish or consume messages.

To create a topic you can use the Google Cloud console, the Google Cloud CLI, the client library, the Managed Kafka API, or the open source Apache Kafka APIs.

## Before you begin

You must first create a cluster before creating a topic. Ensure that you have set up the following:

  * [A Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).



## Required roles and permissions to create a topic

To get the permissions that you need to create a topic, ask your administrator to grant you the [Managed Kafka Topic Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a topic. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a topic:

  * Create a topic: `managedkafka.topics.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Properties of a Managed Service for Apache Kafka topic

When you create or update a Managed Service for Apache Kafka topic, you must specify the following properties.

### Topic name

The name of the Managed Service for Apache Kafka topic that you are creating. For guidelines on how to name a topic, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a topic is immutable.

### Partition count

The number of partitions in the topic. You can edit a topic to increase the partition count for a topic, but you cannot decrease it. Increasing the number of partitions for a topic that uses a key might change how messages are distributed.

### Replication factor

The number of replicas for each partition. If you don't specify the value, the cluster's default replication factor is used.

A higher replication factor can improve data consistency in the event of broker failures, as data is replicated to multiple brokers. For production environments, a replication factor of 3 or higher is recommended. Higher replica counts increase local storage and data transfer costs for the topic. However, they don't increase the persistent storage costs. The replication factor cannot exceed the number of available brokers.

**Note:** Managed Service for Apache Kafka clusters have the broker configuration values as `min.insync.replicas=2` and `default.replication.factor=3`. If you set a lower replication factor than 3 for the topic, you must also set a topic config override as `min.insync.replicas=1`.

### Other parameters

You can also set other Apache Kafka topic-level configuration parameters. These are specified as `key=value` pairs that override the cluster defaults.

Configurations related to topics have a server default and an optional per-topic override. The format is a comma-separated list of `KEY=VALUE` pairs, where `KEY` is the name of the Kafka topic configuration property, and `VALUE` is the required setting.These key-value pairs help you override the cluster defaults. Examples include `flush.ms=10` and `compression.type=producer`.

Caution. If you override the default retention period (`retention.ms`), avoid setting it too short (for example, less than 48 hours). A shorter retention time can reduce storage costs, but increases the risk of data loss if consumers fall behind or if service disruptions occur. Ensure that your retention period is long enough to cover potential delays in downstream processing or incident resolution windows.

For a list of all supported topic-level configurations, see [Topic-level configs](https://kafka.apache.org/37/configuration/topic-level-configs/) in the Apache Kafka documentation.

## Create a topic

Before you create a topic, review the topic properties.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the cluster for which you want to create a topic.

The **Cluster details** page opens.

  3. In the cluster details page, click **Create Topic**.

The **Create Kafka topic** page opens.

  4. For the **Topic name** , enter a string.

  5. For **Partition count** , enter the number of partitions you want or keep the default value.

  6. For **Replication factor** , enter the replication factor you want or keep the default value.

  7. (Optional) To alter any topic configurations, add them as comma-separated key-value pairs in the **Configurations** field.

  8. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create) command:
         
         gcloud managed-kafka topics create TOPIC_ID \
             --cluster=CLUSTER_ID --location=LOCATION_ID \
             --partitions=PARTITIONS \
             --replication-factor=REPLICATION_FACTOR \
             --configs=CONFIGS
         

Replace the following:

     * TOPIC_ID: The name of the topic.
     * CLUSTER: The name of the cluster where you want to create the topic.
     * LOCATION: The region of the cluster.
     * PARTITIONS: The number of partitions for the topic.
     * REPLICATION_FACTOR: The replication factor for the topic.
     * CONFIGS: Topic-level optional parameters. Specify as comma-separated key-value pairs. For example, `compression.type=producer`.



###  Kafka CLI 

Before running this command, install the Kafka command-line tools on a Compute Engine VM. The VM must be able to reach a subnet that is connected to your Managed Service for Apache Kafka cluster. Follow the instructions in [ Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart). 

Run the `kafka-topics.sh` command as follows:
    
    
    kafka-topics.sh --create --if-not-exists \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties \
      --topic TOPIC_ID \
      --partitions PARTITIONS \
      --replication-factor REPLICATION_FACTOR
    

Replace the following:

  * BOOTSTRAP_ADDRESS: The [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address) of the Managed Service for Apache Kafka cluster.

  * TOPIC_ID: The name of the topic.

  * PARTITIONS: The number of partitions for the topic.

  * REPLICATION_FACTOR: The replication factor for the topic.




###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster 
  * `CLUSTER_ID`: the ID of the cluster 
  * `TOPIC_ID`: the ID of the topic 
  * `PARTITION_COUNT`: the number of partitions for the topic 
  * `REPLICATION_FACTOR`: the number of replicas of each partition 



HTTP method and URL: 
    
    
    POST https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics?topicId=TOPIC_ID

Request JSON body: 
    
    
    {
      "name": "TOPIC_ID",
      "partitionCount": PARTITION_COUNT,
      "replicationFactor": REPLICATION_FACTOR
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics?topicId=TOPIC_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics?topicId=TOPIC_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID",
      "partitionCount": PARTITION_COUNT,
      "replicationFactor": REPLICATION_FACTOR
    }
    

###  Terraform 

You can use a Terraform resource to create a [topic](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_topic).
    
    
    resource "google_managed_kafka_topic" "default" {
      project            = data.google_project.default.project_id # Replace this with your project ID in quotes
      topic_id           = "my-topic-id"
      cluster            = google_managed_kafka_cluster.default.cluster_id
      location           = "us-central1"
      partition_count    = 2
      replication_factor = 3
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

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
    
    func createTopic(w io.Writer, projectID, region, clusterID, topicID string, partitionCount, replicationFactor int32, configs map[string]string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	// topicID := "my-topic"
    	// partitionCount := 10
    	// replicationFactor := 3
    	// configs := map[string]string{"min.insync.replicas":"1"}
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	topicPath := fmt.Sprintf("%s/topics/%s", clusterPath, topicID)
    	topicConfig := &managedkafkapb.Topic{
    		Name:              topicPath,
    		PartitionCount:    partitionCount,
    		ReplicationFactor: replicationFactor,
    		Configs:           configs,
    	}
    
    	req := &managedkafkapb.CreateTopicRequest{
    		Parent:  clusterPath,
    		TopicId: topicID,
    		Topic:   topicConfig,
    	}
    	topic, err := client.CreateTopic(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateTopic got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic: %s\n", topic.Name)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html);
    import com.google.cloud.managedkafka.v1.[CreateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateTopicRequest.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import com.google.cloud.managedkafka.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html);
    import com.google.cloud.managedkafka.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class CreateTopic {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        String topicId = "my-topic";
        int partitionCount = 100;
        int replicationFactor = 3;
        Map<String, String> configs =
            new HashMap<String, String>() {
              {
                put("min.insync.replicas", "2");
              }
            };
        createTopic(projectId, region, clusterId, topicId, partitionCount, replicationFactor, configs);
      }
    
      public static void createTopic(
          String projectId,
          String region,
          String clusterId,
          String topicId,
          int partitionCount,
          int replicationFactor,
          Map<String, String> configs)
          throws Exception {
        [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html) topic =
            [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html).newBuilder()
                .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html).of(projectId, region, clusterId, topicId).toString())
                .[setPartitionCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.Builder.html#com_google_cloud_managedkafka_v1_Topic_Builder_setPartitionCount_int_)(partitionCount)
                .[setReplicationFactor](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.Builder.html#com_google_cloud_managedkafka_v1_Topic_Builder_setReplicationFactor_int_)(replicationFactor)
                .putAllConfigs(configs)
                .build();
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create()) {
          [CreateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateTopicRequest.html) request =
              [CreateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateTopicRequest.html).newBuilder()
                  .setParent([ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html).of(projectId, region, clusterId).toString())
                  .[setTopicId](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateTopicRequest.Builder.html#com_google_cloud_managedkafka_v1_CreateTopicRequest_Builder_setTopicId_java_lang_String_)(topicId)
                  .setTopic(topic)
                  .build();
          // This operation is being handled synchronously.
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html) response = managedKafkaClient.createTopic(request);
          System.out.printf("Created topic: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html#com_google_cloud_managedkafka_v1_Topic_getName__)());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaClient.createTopic got err: %s", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    # topic_id = "my-topic"
    # partition_count = 10
    # replication_factor = 3
    # configs = {"min.insync.replicas": "1"}
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    topic = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[Topic](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Topic.html)()
    topic.name = client.[topic_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_topic_path)(project_id, region, cluster_id, topic_id)
    topic.partition_count = partition_count
    topic.replication_factor = replication_factor
    # For a list of configs, one can check https://kafka.apache.org/documentation/#topicconfigs
    topic.configs = configs
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[CreateTopicRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateTopicRequest.html)(
        parent=client.[cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_cluster_path)(project_id, region, cluster_id),
        topic_id=topic_id,
        topic=topic,
    )
    
    try:
        response = client.[create_topic](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_create_topic)(request=request)
        print("Created topic:", response.name)
    except AlreadyExists as e:
        print(f"Failed to create topic {topic.name} with error: {e.message}")
    

## What's next?

  * [Monitor your topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster)

  * [List your topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-topics)

  * [View a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-topic)

  * [Edit a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic)

  * [Delete a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-topic)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
