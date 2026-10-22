---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-consumer-group/
title: Update a Google Cloud Managed Service for Apache Kafka consumer group \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:38.198947+00:00
---

# Update a Google Cloud Managed Service for Apache Kafka consumer group  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-consumer-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Update a Google Cloud Managed Service for Apache Kafka consumer group Stay organized with collections  Save and categorize content based on your preferences. 

You can update a Google Cloud Managed Service for Apache Kafka consumer group to modify the offsets for a list of topic partitions. This lets you control which messages the consumers in the group receive.

To update a consumer group, you can use the Google Cloud CLI, the client library, the Managed Kafka API, or the open source Apache Kafka APIs. The Google Cloud console is not supported for editing a consumer group.

## Before you begin

To update a consumer group, first ensure it is not actively consuming messages. A consumer group is automatically deleted by Kafka if it has never consumed any messages, or when the last committed offset has expired after `offsets.retention.minutes`.

Follow these steps before you update a consumer group:

  1. Send some messages to the topic from which your consumer group is reading messages.

  2. Start your consumer group to process a few messages.

  3. Stop all your consumers from consuming messages. To stop a consumer, press `Control+C`.




For more information about sending and consuming messages, see [Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).

### Required roles and permissions to update a consumer group

To get the permissions that you need to edit your consumer groups, ask your administrator to grant you the [Managed Kafka Consumer Group Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to edit your consumer groups. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to edit your consumer groups:

  * Update consumer groups: `managedkafka.consumerGroups.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant the service agent READ access

In order to update consumer group offsets, the service agent requires access to the READ operation on the topic and consumer group resources. This access is configured with [Apache Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls).

If you have not configured any Apache Kafka ACLs for the consumer group and its topic within the cluster, the service agent has ambient access to these resources. You can skip this section.

If Apache Kafka ACLs are configured for the consumer group and its topic within the cluster, the service agent requires explicit ACL access for the READ operation for both resources. To do so, add ACL entries granting the service agent access to the READ operation on the relevant consumer group and topic. Follow these steps:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  4. Run the [ `gcloud managed-kafka acls add-acl-entry`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/add-acl-entry) command:
         
         gcloud managed-kafka acls add-acl-entry CONSUMER_GROUP_ACL_ID \
           --cluster=CLUSTER_ID \
           --location=LOCATION \
           --principal=User:__AUTH_TOKEN__service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com \
           --operation=READ
           --permission-type=ALLOW
           --host=*
         
         
           gcloud managed-kafka acls add-acl-entry TOPIC_ACL_ID \
           --cluster=CLUSTER_ID \
           --location=LOCATION \
           --principal=User:__AUTH_TOKEN__service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com \
           --operation=READ
           --permission-type=ALLOW
           --host=*

Replace the following:

     * `CONSUMER_GROUP_ACL_ID` (required): the unique ID of the Managed Service for Apache Kafka ACL resource where you want to add the ACL entry for the consumer group. To apply the access to all consumer groups, use `allConsumerGroups`. Or, for a specific consumer group, use `consumerGroup/CONSUMER_GROUP_NAME`. 
     * `TOPIC_ACL_ID` (required): the unique ID of the Managed Service for Apache Kafka ACL resource where you want to add the ACL entry for the topic. To apply the access to all topics, use `allTopics`. Or, for a specific topic, use `topic/TOPIC_NAME`. 
     * `CLUSTER_ID` (required): the ID of the cluster containing the ACL resource.
     * `LOCATION` (required): the region where the cluster is located. See [Supported locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations).
     * `PROJECT_NUMBER` (required): the project number of the project where the cluster is located. This is used to build the principal name of the service agent for the ACL entry.



For more information about adding an ACL entry, see [Add an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry).

## Update a consumer group

Ensure you have completed the steps in the Before you begin section.

To update a consumer group, follow these steps:

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [ `gcloud managed-kafka consumer-groups update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update) command:
         
         gcloud managed-kafka consumer-groups update CONSUMER_GROUP_ID \
             --cluster=CLUSTER_ID \
             --location=LOCATION \
             --topics-file=TOPICS_FILE

Replace the following:

  3. CLUSTER_ID: The ID or name of the cluster.

  4. LOCATION: The location of the cluster.

  5. CONSUMER_GROUP_ID: The ID or name of the consumer group.

  6. TOPICS_FILE: This setting specifies the location of the file containing the configuration of topics to be updated for the consumer group. The file can be in JSON or YAML format. It can be a file path or directly include the JSON or YAML content.

The topic file uses a JSON structure to represent a `ConsumerGroup` topics map, in the form `{ topicName1: {ConsumerPartitionMetadata}, topicName2:{ConsumerPartitionMetadata}}`. For each topic, `ConsumerPartitionMetadata` provides the offset and metadata for each partition.

To set the offset for a single partition (partition 0) in a topic named `topic1` to 10, the JSON configuration would look like:`{"topic1": {"partitions": { 0 : { "offset": 10, "metadata": ""}}}}`

The following is an example of the contents of a `topics.json` file:
         
         {
           "projects/PROJECT_NUMBER/locations/LOCATION/clusters/CLUSTER_NAME/TOPICS/TOPIC_NAME": {
             "partitions": {
               "1": {
                 "offset": "1",
                 "metadata": "metadata"
               },
               "2": {
                 "offset": "1",
                 "metadata": "metadata"
               }
             }
           },
           "projects/PROJECT_NUMBER/locations/LOCATION/clusters/CLUSTER_NAME/TOPICS/OTHER_TOPIC_NAME": {
             "partitions": {
               "1": {
                 "offset": "1",
                 "metadata": "metadata"
               }
             }
           }
         }

  7. TOPIC_PATH: When specifying topics in JSON or YAML file, include the full topic path which can be obtained from running the `gcloud managed-kafak topics describe` command and of the format `projects/PROJECT_NUMBER/locations/LOCATION/clusters/CLUSTER_ID/topics/topic`. .




### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func updateConsumerGroup(w io.Writer, projectID, region, clusterID, consumerGroupID, topicPath string, partitionOffsets map[int32]int64, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	// consumerGroupID := "my-consumer-group"
    	// topicPath := "my-topic-path"
    	// partitionOffsets := map[int32]int64{1: 10, 2: 20, 3: 30}
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	consumerGroupPath := fmt.Sprintf("%s/consumerGroups/%s", clusterPath, consumerGroupID)
    
    	partitionMetadata := make(map[int32]*managedkafkapb.ConsumerPartitionMetadata)
    	for partition, offset := range partitionOffsets {
    		partitionMetadata[partition] = &managedkafkapb.ConsumerPartitionMetadata{
    			Offset: offset,
    		}
    	}
    	topicConfig := map[string]*managedkafkapb.ConsumerTopicMetadata{
    		topicPath: {
    			Partitions: partitionMetadata,
    		},
    	}
    	consumerGroupConfig := managedkafkapb.ConsumerGroup{
    		Name:   consumerGroupPath,
    		Topics: topicConfig,
    	}
    	paths := []string{"topics"}
    	updateMask := &fieldmaskpb.FieldMask{
    		Paths: paths,
    	}
    
    	req := &managedkafkapb.UpdateConsumerGroupRequest{
    		UpdateMask:    updateMask,
    		ConsumerGroup: &consumerGroupConfig,
    	}
    	consumerGroup, err := client.UpdateConsumerGroup(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.UpdateConsumerGroup got err: %w", err)
    	}
    	fmt.Fprintf(w, "Updated consumer group: %#v\n", consumerGroup)
    	return nil
    }
    

### Java
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConsumerGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroup.html);
    import com.google.cloud.managedkafka.v1.[ConsumerGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroupName.html);
    import com.google.cloud.managedkafka.v1.[ConsumerPartitionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerPartitionMetadata.html);
    import com.google.cloud.managedkafka.v1.[ConsumerTopicMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerTopicMetadata.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import com.google.cloud.managedkafka.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html);
    import com.google.cloud.managedkafka.v1.[UpdateConsumerGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateConsumerGroupRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class UpdateConsumerGroup {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        String topicId = "my-topic";
        String consumerGroupId = "my-consumer-group";
        Map<Integer, Integer> partitionOffsets =
            new HashMap<Integer, Integer>() {
              {
                put(1, 10);
                put(2, 20);
                put(3, 30);
              }
            };
        updateConsumerGroup(projectId, region, clusterId, topicId, consumerGroupId, partitionOffsets);
      }
    
      public static void updateConsumerGroup(
          String projectId,
          String region,
          String clusterId,
          String topicId,
          String consumerGroupId,
          Map<Integer, Integer> partitionOffsets)
          throws Exception {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.TopicName.html).of(projectId, region, clusterId, topicId);
        [ConsumerGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroupName.html) consumerGroupName =
            [ConsumerGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroupName.html).of(projectId, region, clusterId, consumerGroupId);
    
        Map<Integer, ConsumerPartitionMetadata> partitions =
            new HashMap<Integer, [ConsumerPartitionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerPartitionMetadata.html)>() {
              {
                for (Entry<Integer, Integer> partitionOffset : partitionOffsets.entrySet()) {
                  ConsumerPartitionMetadata partitionMetadata =
                      [ConsumerPartitionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerPartitionMetadata.html).newBuilder()
                          .[setOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerPartitionMetadata.Builder.html#com_google_cloud_managedkafka_v1_ConsumerPartitionMetadata_Builder_setOffset_long_)(partitionOffset.getValue())
                          .build();
                  put(partitionOffset.getKey(), partitionMetadata);
                }
              }
            };
        ConsumerTopicMetadata topicMetadata =
            ConsumerTopicMetadata.newBuilder().putAllPartitions(partitions).build();
        ConsumerGroup consumerGroup =
            ConsumerGroup.newBuilder()
                .setName(consumerGroupName.toString())
                .putTopics(topicName.toString(), topicMetadata)
                .build();
        FieldMask updateMask = FieldMask.newBuilder().addPaths("topics").build();
    
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = ManagedKafkaClient.create()) {
          [UpdateConsumerGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateConsumerGroupRequest.html) request =
              [UpdateConsumerGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateConsumerGroupRequest.html).newBuilder()
                  .setUpdateMask(updateMask)
                  .setConsumerGroup(consumerGroup)
                  .build();
          // This operation is being handled synchronously.
          [ConsumerGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroup.html) response = managedKafkaClient.updateConsumerGroup(request);
          System.out.printf("Updated consumer group: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroup.html#com_google_cloud_managedkafka_v1_ConsumerGroup_getName__)());
        } catch (IOException | ApiException e) {
          System.err.printf("managedKafkaClient.updateConsumerGroup got err: %s", e.getMessage());
        }
      }
    }
    

### Python
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    from google.protobuf import field_mask_pb2
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    # consumer_group_id = "my-consumer-group"
    # topic_path = "my-topic-path"
    # partition_offsets = {10: 10}
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    consumer_group = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ConsumerGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerGroup.html)()
    consumer_group.name = client.[consumer_group_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_consumer_group_path)(
        project_id, region, cluster_id, consumer_group_id
    )
    
    topic_metadata = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ConsumerTopicMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerTopicMetadata.html)()
    for partition, offset in partition_offsets.items():
        partition_metadata = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ConsumerPartitionMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerPartitionMetadata.html)(offset=offset)
        topic_metadata.partitions[partition] = partition_metadata
    consumer_group.topics = {
        topic_path: topic_metadata,
    }
    
    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.append("topics")
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[UpdateConsumerGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateConsumerGroupRequest.html)(
        update_mask=update_mask,
        consumer_group=consumer_group,
    )
    
    try:
        response = client.[update_consumer_group](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_update_consumer_group)(request=request)
        print("Updated consumer group:", response)
    except NotFound as e:
        print(f"Failed to update consumer group {consumer_group_id} with error: {e.message}")
    

## What's next?

  * [View a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-consumer-group).

  * [Delete a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-consumer-group).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
