---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic/
title: Update a Google Cloud Managed Service for Apache Kafka topic \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:07.539553+00:00
---

# Update a Google Cloud Managed Service for Apache Kafka topic  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Update a Google Cloud Managed Service for Apache Kafka topic Stay organized with collections  Save and categorize content based on your preferences. 

After a topic is created, you can edit the topic configuration to update these properties: the number of partitions and topic configurations that don't default to the properties already set at the cluster-level. You can only increase the number of partitions, you cannot decrease it.

To update a single topic, you can use the Google Cloud console, the Google Cloud CLI, the client library, the Managed Kafka API, or the open source Apache Kafka APIs.

## Required roles and permissions to edit a topic

To get the permissions that you need to edit a topic, ask your administrator to grant you the Managed Kafka Topic Editor(`roles/managedkafka.topicEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to edit a topic. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to edit a topic:

  * Update a topic: `managedkafka.topics.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Edit a topic

To edit a topic, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

The clusters you created in a project are listed.

  2. Click the cluster to which the topic that you want to edit belongs.

The **Cluster details** page opens. In the cluster details page, for the **Resources** tab, the topics are listed.

  3. Click the topic that you want to edit.

The **Topic details** page opens.

  4. To make your edits, click **Edit**.

  5. Click **Save** after the changes.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/update) command:
         
         gcloud managed-kafka topics update TOPIC_ID \
           --cluster=CLUSTER_ID \
           --location=LOCATION_ID \
           --partitions=PARTITIONS \
           --configs=CONFIGS
         

This command modifies the configuration of an existing topic in the specified Managed Service for Apache Kafka cluster. You can use this command to increase the number of partitions and update topic-level configuration settings.

Replace the following:

     * TOPIC_ID: The ID of the topic.
     * CLUSTER_ID: The ID of the cluster containing the topic.
     * LOCATION_ID: The location of the cluster.
     * PARTITIONS: Optional: The updated number of partitions for the topic. You can only increase the number of partitions, you cannot decrease it.
     * CONFIGS: Optional: A list of configuration settings to update. Specify as a comma-separated list of key-value pairs. For example, `retention.ms=604800000,retention.bytes=10000000`.



###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster 
  * `CLUSTER_ID`: the ID of the cluster 
  * `TOPIC_ID`: the ID of the topic 
  * `UPDATE_MASK`: which fields to update, as a comma-separated list of fully qualified names. Example: `partitionCount`
  * `PARTITION_COUNT`: the updated number of partitions for the topic 



HTTP method and URL: 
    
    
    PATCH https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID?updateMask=UPDATE_MASK

Request JSON body: 
    
    
    {
      "name": "TOPIC_ID",
      "partitionCount": PARTITION_COUNT
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID?updateMask=UPDATE_MASK"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC_ID?updateMask=UPDATE_MASK" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.managedkafka.v1.OperationMetadata",
        "createTime": "CREATE_TIME",
        "target": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
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
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func updateTopic(w io.Writer, projectID, region, clusterID, topicID string, partitionCount int32, configs map[string]string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	// topicID := "my-topic"
    	// partitionCount := 20
    	// configs := map[string]string{"min.insync.replicas":"1"}
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	topicPath := fmt.Sprintf("%s/topics/%s", clusterPath, topicID)
    	TopicConfig := managedkafkapb.Topic{
    		Name:           topicPath,
    		PartitionCount: partitionCount,
    		Configs:        configs,
    	}
    	paths := []string{"partition_count", "configs"}
    	updateMask := &fieldmaskpb.FieldMask{
    		Paths: paths,
    	}
    
    	req := &managedkafkapb.UpdateTopicRequest{
    		UpdateMask: updateMask,
    		Topic:      &TopicConfig,
    	}
    	topic, err := client.UpdateTopic(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.UpdateTopic got err: %w", err)
    	}
    	fmt.Fprintf(w, "Updated topic: %#v\n", topic)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import com.google.cloud.managedkafka.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html);
    import com.google.cloud.managedkafka.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html);
    import com.google.cloud.managedkafka.v1.[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateTopicRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;
    
    public class UpdateTopic {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        String topicId = "my-topic";
        int partitionCount = 200;
        Map<String, String> configs =
            new HashMap<String, String>() {
              {
                put("min.insync.replicas", "1");
              }
            };
        updateTopic(projectId, region, clusterId, topicId, partitionCount, configs);
      }
    
      public static void updateTopic(
          String projectId,
          String region,
          String clusterId,
          String topicId,
          int partitionCount,
          Map<String, String> configs)
          throws Exception {
        [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html) topic =
            [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html).newBuilder()
                .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html).of(projectId, region, clusterId, topicId).toString())
                .[setPartitionCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.Builder.html#com_google_cloud_managedkafka_v1_Topic_Builder_setPartitionCount_int_)(partitionCount)
                .putAllConfigs(configs)
                .build();
        String[] paths = {"partition_count", "configs"};
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(Arrays.asList(paths)).build();
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create()) {
          [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateTopicRequest.html) request =
              [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateTopicRequest.html).newBuilder().setUpdateMask(updateMask).setTopic(topic).build();
          // This operation is being handled synchronously.
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html) response = managedKafkaClient.updateTopic(request);
          System.out.printf("Updated topic: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic.html#com_google_cloud_managedkafka_v1_Topic_getName__)());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaClient.updateCluster got err: %s", e.getMessage());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    from google.protobuf import field_mask_pb2
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    # topic_id = "my-topic"
    # partition_count = 20
    # configs = {"min.insync.replicas": "1"}
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    topic = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[Topic](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Topic.html)()
    topic.name = client.[topic_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_topic_path)(project_id, region, cluster_id, topic_id)
    topic.partition_count = partition_count
    topic.configs = configs
    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.extend(["partition_count", "configs"])
    
    # For a list of editable fields, one can check https://cloud.google.com/managed-kafka/docs/create-topic#properties.
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[UpdateTopicRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateTopicRequest.html)(
        update_mask=update_mask,
        topic=topic,
    )
    
    try:
        response = client.[update_topic](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_update_topic)(request=request)
        print("Updated topic:", response)
    except NotFound as e:
        print(f"Failed to update topic {topic_id} with error: {e.message}")
    

## Configure message retention

Kafka stores messages in _log segment files_. By default, Kafka deletes segment files after a retention period or when a partition exceeds a data size threshold. You can change this behavior by enabling log compaction. If log compaction is enabled, then Kafka only keeps the latest value for each key.

Google Cloud Managed Service for Apache Kafka uses _tiered storage_ , which means that completed log segments are stored remotely, rather than local storage. To learn more about tiered storage, see [Tiered Storage](https://kafka.apache.org/37/operations/tiered-storage) in the Apache Kafka documentation.

### Set the retention values

If log compaction is not enabled, then the following settings control how Kafka stores log segment files:

  * `retention.ms`: The maximum length of time to save segment files, in milliseconds.
  * `retention.bytes`: The maximum number of bytes to store per partition. If the data in a partition exceeds this value, then Kafka discards older segment files.



Caution. If you override the default retention period (`retention.ms`), avoid setting it too short (for example, less than 48 hours). A shorter retention time can reduce storage costs, but increases the risk of data loss if consumers fall behind or if service disruptions occur. Ensure that your retention period is long enough to cover potential delays in downstream processing or incident resolution windows.

To update these settings, use either the gcloud CLI or the Kafka CLI:

###  gcloud 

To set the message retention, run the [`gcloud managed-kafka topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/update) command.
    
    
    gcloud managed-kafka topics update TOPIC_ID \
      --cluster=CLUSTER_ID \
      --location=LOCATION_ID \
      --configs=retention.ms=RETENTION_PERIOD,retention.bytes=MAX_BYTES
    

Replace the following:

  * TOPIC_ID: The ID of the topic.
  * CLUSTER_ID: The ID of the cluster containing the topic.
  * LOCATION_ID: The location of the cluster.
  * RETENTION_PERIOD: The maximum amount of time to store segment files, in milliseconds.
  * MAX_BYTES: The maximum number of bytes to store, per partition.



###  Kafka CLI 

Before running this command, install the Kafka command-line tools on a Compute Engine VM. The VM must be able to reach a subnet that is connected to your Managed Service for Apache Kafka cluster. Follow the instructions in [ Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart). 

Run the `kafka-configs.sh` command:
    
    
    kafka-configs.sh --alter \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties \
      --entity-type topics \
      --entity-name TOPIC_ID \
      --add-config retention.ms=RETENTION_PERIOD,retention.bytes=MAX_BYTES
    

Replace the following:

  * BOOTSTRAP_ADDRESS: The [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address) of the Managed Service for Apache Kafka cluster.
  * TOPIC_ID: The ID of the topic.
  * RETENTION_PERIOD: The maximum amount of time to store segment files, in milliseconds.
  * MAX_BYTES: The maximum number of bytes to store, per partition.



### Enable log compaction

If log compaction is enabled, then Kafka only stores the latest message for each key in the topic. In addition, only local storage is used for that topic. Messages written to the topic are never moved to remote storage.

**Caution:** Log compaction combined with a very large key space can result in out-of-disk errors, because the number of messages with unique keys can exhaust the broker's disk capacity. For more information, see [Out-of-disk errors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-clusters#out-of-disk_errors).

Log compaction is disabled by default. To enable log compaction for a topic, set the `cleanup.policy` configuration to `"compact"`, as follows:

###  gcloud 

Run the [`gcloud managed-kafka topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/update) command.
    
    
    gcloud managed-kafka topics update TOPIC_ID \
      --cluster=CLUSTER_ID \
      --location=LOCATION_ID \
      --configs=cleanup.policy=compact
    

Replace the following:

  * TOPIC_ID: The ID of the topic.
  * CLUSTER_ID: The ID of the cluster containing the topic.
  * LOCATION_ID: The location of the cluster.



###  Kafka CLI 

Before running this command, install the Kafka command-line tools on a Compute Engine VM. The VM must be able to reach a subnet that is connected to your Managed Service for Apache Kafka cluster. Follow the instructions in [ Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart). 

Run the `kafka-configs.sh` command:
    
    
    kafka-configs.sh --alter \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties \
      --entity-type topics \
      --entity-name TOPIC_ID \
      --add-config cleanup.policy=compact
    

Replace the following:

  * BOOTSTRAP_ADDRESS: The [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address) of the Managed Service for Apache Kafka cluster.
  * TOPIC_ID: The ID of the topic.



## Limitations

  * You can't override topic configurations for remote storage, such as `remote.storage.enable`.

  * You can't override topic configurations for log segment files, such as `segment.bytes`.

  * Enabling log compaction for a topic implicitly disables tiered storage for that topic. All log files for the topic are stored locally.




## What's next?

  * [Delete a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-topic)

  * [List all consumer groups](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-consumer-groups)

  * [View a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-consumer-group)

  * [Delete a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-consumer-group)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
