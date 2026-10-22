---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples/managedkafka-update-consumergroup/
title: Update a Kafka consumer group \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:15.690101+00:00
---

# Update a Kafka consumer group  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples/managedkafka-update-consumergroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples)



#  Update a Kafka consumer group Stay organized with collections  Save and categorize content based on your preferences. 

Update a Kafka consumer group

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Update a Google Cloud Managed Service for Apache Kafka consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-consumer-group)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Python API reference documentation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=apachekafkaforbigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
