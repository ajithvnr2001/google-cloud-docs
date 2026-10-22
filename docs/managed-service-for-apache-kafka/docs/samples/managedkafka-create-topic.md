---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples/managedkafka-create-topic/
title: Create a Kafka topic \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:16.063625+00:00
---

# Create a Kafka topic  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples/managedkafka-create-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples)



#  Create a Kafka topic Stay organized with collections  Save and categorize content based on your preferences. 

Create a Kafka topic

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a Google Cloud Managed Service for Apache Kafka topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic)



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

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Python API reference documentation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_managed_kafka_topic" "default" {
      project            = data.google_project.default.project_id # Replace this with your project ID in quotes
      topic_id           = "my-topic-id"
      cluster            = google_managed_kafka_cluster.default.cluster_id
      location           = "us-central1"
      partition_count    = 2
      replication_factor = 3
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=apachekafkaforbigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
