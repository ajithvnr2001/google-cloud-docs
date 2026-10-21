---
url: https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-apache-kaftka-for-bigquery/
title: Migrate from Pub/Sub Lite to Google Cloud Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:23:07.658867+00:00
---

# Migrate from Pub/Sub Lite to Google Cloud Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-apache-kaftka-for-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Migrate from Pub/Sub Lite to Google Cloud Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document details how to migrate data from a Pub/Sub Lite topic to a [Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) topic.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. Verify that you have the permissions required to complete this guide. 

  6. Enable the Pub/Sub Lite, Cloud Pub/Sub, and Managed Service for Apache Kafka APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable pubsublite.googleapis.com pubsub.googleapis.com managedkafka.googleapis.com

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. Verify that you have the permissions required to complete this guide. 

  11. Enable the Pub/Sub Lite, Cloud Pub/Sub, and Managed Service for Apache Kafka APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable pubsublite.googleapis.com pubsub.googleapis.com managedkafka.googleapis.com

  12. Identify the Pub/Sub Lite topic and subscription to migrate.
  13. Create a Managed Service for Apache Kafka cluster in the same region as your Pub/Sub Lite topic. For more information, see [Create a Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster). 
  14. Create a Kafka topic to replace the Pub/Sub Lite topic and subscription. 
  15. Create a Kafka Connect cluster, with the Kafka cluster as the primar cluster. For more information, see [Create a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster). 
  16. Upgrade your dependencies to the latest version:

     * Java: Use version 1.16.1 or higher of `java-pubsublite`. 
     * Go: Ensure the `pscompat.ManagedKafka` backend is available. 



### Required roles and permissions

To get the permissions that you need to set up Pub/Sub Lite migration, ask your administrator to grant you the following IAM roles on project: 

  * [Managed Kafka Client ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)
  * [Pub/Sub Lite Subscriber ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)
  * [Pub/Sub Lite Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)
  * [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Migration workflow

The migration has several phases that you complete in order:

  1. Set up replication. Create a pipeline that moves messages published to Pub/Sub Lite into a Kafka topic.

  2. Migrate consumers. Update your consumers to read from Kafka.

  3. Migrate publishers. Update your publishers to write to Kafka.

  4. Decommission. Delete the replication pipeline and the Pub/Sub Lite topic.




Throughout the migration, your application code uses the same `Publisher` and `Subscriber` types in Java, or the same `pscompat.PublisherClient` and `pscompat.SubscriberClient` types in Go. The switch to Managed Service for Apache Kafka is accomplished by setting a flag in your publisher and consumer code.

## Set up replication

Replication uses the following components:

  * **Pub/Sub Lite export subscription** : Streams messages from a Pub/Sub Lite topic to a Pub/Sub topic. For more information, see [Export Pub/Sub Lite messages to Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub).

  * **Pub/Sub bridge topic and subscription** : The staging area that Kafka Connect reads from.

  * **Kafka Connect** : Uses a [Pub/Sub Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector) to pull messages from the Pub/Sub subscription and write them to Kafka. For more information, see [Replicate Pub/Sub messages to Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-pubsub).




### Preserve ordering

To preserve message ordering, set `kafka.key.attribute=orderingKey` on the Pub/Sub Source connector. With this setting, the connector uses the Pub/Sub ordering key as the Kafka message key.

Because Kafka routes messages to partitions by key hash, all messages sharing an ordering key are written to the same Kafka partition. The export subscription preserves the Pub/Sub Lite `orderingKey` as the ordering key in the Pub/Sub message, so this setting preserves the per-key ordering established in Pub/Sub Lite.

### Partition affinity

To ensure that messages from a given Pub/Sub Lite partition are always written to the same Kafka partition, do the following:

  * Create the Kafka topic with the same number of partitions as the Pub/Sub Lite topic.

  * Set `kafka.partition.scheme=hash_key` in the Pub/Sub Source connector.




The timestamp-based offset translation strategy for migrating consumers relies on this behavior.

### Connector configuration

The following example shows the recommended configuration settings for the Pub/Sub Source connector:
    
    
    {
      "connector.class": "com.google.pubsub.kafka.source.CloudPubSubSourceConnector",
      "cps.project": "PROJECT_ID",
      "cps.subscription": "BRIDGE_SUBSCRIPTION",
      "kafka.topic": "KAFKA_TOPIC",
      "kafka.key.attribute": "orderingKey",
      "kafka.partition.scheme": "hash_key",
      "kafka.partition.count": "PARTITION_COUNT",
      "kafka.record.headers": "true",
      "key.converter": "org.apache.kafka.connect.storage.StringConverter",
      "value.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
      "tasks.max": "MAXIMUM_TASK_COUNT"
    }
    

Replace the following:

  * `PROJECT_ID`: The ID of the Google Cloud project that contains the Pub/Sub subscription.

  * `BRIDGE_SUBSCRIPTION`: The ID of the Pub/Sub subscription.

  * `KAFKA_TOPIC`: The name of the Kafka topic.

  * `PARTITION_COUNT`: The number of Kafka topic partitions. Use the Pub/Sub Lite partition count.

  * `MAXIMUM_TASK_COUNT`: The maximum number of parallel tasks in the connector. The value should be equal to or less than `PARTITION_COUNT`.




### Verify replication

Before migrating any clients, perform the following steps to confirm that the replication pipeline is working:

  1. Run the [`gcloud managed-kafka connectors describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/describe) command.
         
         gcloud managed-kafka connectors describe CONNECTOR_NAME \
             --connect_cluster=CONNECT_CLUSTER \
             --location=REGION \
             --project=PROJECT \
             --format="value(state)"
         

Replace the following:

     * `CONNECTOR_NAME`: The name of the Pub/Sub Source connector.

     * `CONNECT_CLUSTER`: The name of the Connect cluster.

     * `REGION`: The location of the Connect cluster.

     * `PROJECT`: The name of the Google Cloud project that contains the Connect cluster.

If the connector is running, the output is `RUNNING`. Otherwise, it means there is a problem with the connector. For troubleshooting tips, see [Troubleshoot a Pub/Sub connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-pubsub-connector).

  2. Publish a test message to the Pub/Sub Lite topic and read it back from the Kafka topic, by using a tool such as `kafka-console-consumer` or a basic client application. The Kafka message key should equal the Pub/Sub Lite ordering key.




## Migrate consumers

Based on your tolerance for duplicates and interruptions in publishing, use one the following strategies to migrate your consumers:

Strategy | Duplication risk | Publishing interruption | Required consumer capability  
---|---|---|---  
Clean cut-over | None | Yes | Standard  
Timestamp-based offset translation | Duplicates might occur | No | Idempotent consumers  
  
### Clean cut-over

Use this strategy when you can briefly stop publishing.

  1. Stop the publisher.
  2. Let Pub/Sub Lite consumers drain. Process all remaining Pub/Sub Lite messages.
  3. Stop the Pub/Sub Lite consumers.
  4. Wait for replication to finish: 
     * In the Pub/Sub bridge subscription, `num_undelivered_messages` reaches zero.
     * In the destination Kafka topic, offsets stop growing.
  5. Seek the Kafka consumer group to the end (latest) on every partition.



### Timestamp-based offset translation

Use this strategy if you can't pause publishing. Consumers must be idempotent, because messages published between the earliest and latest committed Pub/Sub Lite timestamps are re-delivered.

  1. Stop the Pub/Sub Lite consumers. (_Don't_ stop the publisher yet.)

  2. For each partition, translate the Pub/Sub Lite committed offset (for example, _T=980_) to the corresponding Kafka offset, which is the first Kafka message at or after the Pub/Sub Lite publish time on the same partition. Use the Offset migration orchestrator to automate this step.

  3. Set the Kafka consumer group to those offsets.




After the orchestrator commits offsets and validation passes, switch your consumers to Managed Service for Apache Kafka, as described in the next section. Consumers resume from the migrated position.

### Switch consumers to Managed Service for Apache Kafka

The latest Pub/Sub Lite client libraries accept a flag to set the backend to Managed Service for Apache Kafka. By setting this flag and supplying the Kafka connection details, the same consumer that you used for Pub/Sub Lite becomes a Managed Service for Apache Kafka consumer.

During migration, run two sets of consumers, one that reads from Pub/Sub Lite, and one that reads from Managed Service for Apache Kafka. Compare what each consumer receives to confirm they have parity. At that point, you can decommission the Pub/Sub Lite consumers.

The following code examples show how to configure a consumer for Managed Service for Apache Kafka:

###  Java 
    
    
    import com.google.cloud.pubsublite.*;
    import com.google.cloud.pubsublite.cloudpubsub.*;
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.Map;
    
    String projectId  = "PROJECT_ID";
    String region     = "us-central1";
    String gmkCluster = "GMK_CLUSTER_ID";
    String gmkTopic   = "GMK_TOPIC";
    
    Map<String, Object> kafkaProperties =
        GmkUtils.buildGmkKafkaProperties(projectId, region, gmkCluster);
    // Optional: start from earliest if no group offset is committed yet.
    kafkaProperties.put("auto.offset.reset", "earliest");
    
    // In GMK mode the SubscriptionName is used as both the Kafka topic and the
    // consumer group ID. Use a stable name; consumers sharing it share the load.
    [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscriptionPath = [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
        .setProject([ProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectId.html).of(projectId))
        .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region))
        .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html).of(gmkTopic))
        .build();
    
    [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver = (PubsubMessage message, com.google.cloud.pubsub.v1.AckReplyConsumer ack) -> {
      System.out.println("Received: " + [message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__).getData().toStringUtf8());
      ack.ack();
    };
    
    [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html) flowControl = [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html).builder()
        .setBytesOutstanding(10L * 1024 * 1024)
        .setMessagesOutstanding(1000L)
        .build();
    
    [SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html) settings = [SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html).newBuilder()
        .setSubscriptionPath(subscriptionPath)
        .setReceiver(receiver)
        .setMessagingBackend(MessagingBackend.MANAGED_KAFKA)
        .setKafkaProperties(kafkaProperties)
        .setPerPartitionFlowControlSettings(flowControl)
        .build();
    
    [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).create(settings);
    subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
    // ... receive messages ...
    // subscriber.stopAsync().awaitTerminated();
    

###  Go 
    
    
    import (
        "context"
        "fmt"
    
        "cloud.google.com/go/pubsub"
        "cloud.google.com/go/pubsublite/pscompat"
        "github.com/IBM/sarama"
    )
    
    ctx := context.Background()
    bootstrap := pscompat.[BuildGMKBootstrapServer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_BuildGMKBootstrapServer)("PROJECT_ID", "us-central1", "GMK_CLUSTER_ID")
    
    saramaCfg, err := pscompat.[NewGMKSaramaConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_NewGMKSaramaConfig)(ctx)
    if err != nil { panic(err) }
    // Optional: read from earliest when no group offset is committed yet.
    saramaCfg.Consumer.Offsets.Initial = sarama.OffsetOldest
    
    settings := pscompat.ReceiveSettings{
        Backend: pscompat.[ManagedKafka](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_PubSubLite_ManagedKafka),
        KafkaConfig: &pscompat.KafkaSubscribeConfig{
            BootstrapServers: bootstrap,
            TopicName:        "GMK_TOPIC",
            SubscriptionName: "GMK_CONSUMER_GROUP", // also the Kafka group ID
            SaramaConfig:     saramaCfg,
        },
    }
    
    // The first arg is the PSL subscription path; it is unused when Backend is
    // ManagedKafka, so any non-empty value is fine.
    sub, err := pscompat.NewSubscriberClientWithSettings(ctx, "unused", settings)
    if err != nil { panic(err) }
    
    err = sub.Receive(ctx, func(_ context.Context, m *pubsub.Message) {
        fmt.Printf("Received: %s (key=%s)\n", string(m.Data), m.OrderingKey)
        m.Ack()
    })
    if err != nil { panic(err) }
    

## Migrate publishers

To migrate your publishers, set the backend to Managed Service for Apache Kafka, similar to the updates described in the previous section for consumers.

When you deploy the new publisher code, start with a non-production environment. Optionally, if your downstream consumers tolerate duplicate messages, run the Kafka publishers in parallel with the Pub/Sub Lite publishers and verify parity, before you decommission the Pub/Sub Lite publishers.

The following code examples show how to configure a publisher for Managed Service for Apache Kafka:

###  Java
    
    
    import com.google.cloud.pubsublite.*;
    import com.google.cloud.pubsublite.cloudpubsub.*;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.Map;
    
    String projectId  = "PROJECT_ID";
    String region     = "us-central1";
    String gmkCluster = "GMK_CLUSTER_ID";
    String gmkTopic   = "GMK_TOPIC";
    
    Map<String, Object> kafkaProperties =
        GmkUtils.buildGmkKafkaProperties(projectId, region, gmkCluster);
    
    [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html) topicPath = [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html).newBuilder()
        .setProject([ProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectId.html).of(projectId))
        .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region))
        .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(gmkTopic))
        .build();
    
    [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html) settings = [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html).newBuilder()
        .setTopicPath(topicPath)
        .setMessagingBackend(MessagingBackend.MANAGED_KAFKA)
        .setKafkaProperties(kafkaProperties)
        .build();
    
    [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html) publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html).create(settings);
    publisher.startAsync().awaitRunning();
    
    [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) message = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder()
        .setData([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)("hello from java-pubsublite/GMK"))
        .[setOrderingKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setOrderingKey_java_lang_String_)("user-123")   // becomes the Kafka message key
        .putAttributes("source", "java-client")
        .build();
    
    String messageId = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)(message).get();
    System.out.println("Published: " + messageId);
    
    publisher.[stopAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.wire.ApiServiceUtils.html#com_google_cloud_pubsublite_internal_wire_ApiServiceUtils_stopAsync_java_lang_Iterable___extends_com_google_api_core_ApiService__)().awaitTerminated();
    

###  Go 
    
    
    import (
        "context"
        "fmt"
    
        "cloud.google.com/go/pubsub"
        "cloud.google.com/go/pubsublite/pscompat"
    )
    
    ctx := context.Background()
    bootstrap := pscompat.[BuildGMKBootstrapServer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_BuildGMKBootstrapServer)("PROJECT_ID", "us-central1", "GMK_CLUSTER_ID")
    
    settings := pscompat.PublishSettings{
        Backend: pscompat.[ManagedKafka](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_PubSubLite_ManagedKafka),
        KafkaConfig: &pscompat.KafkaPublishConfig{
            BootstrapServers: bootstrap,
            TopicName:        "GMK_TOPIC",
        },
    }
    
    // First arg is the PSL topic path; ignored in ManagedKafka mode.
    pub, err := pscompat.NewPublisherClientWithSettings(ctx, "unused", settings)
    if err != nil { panic(err) }
    defer pub.Stop()
    
    result := pub.Publish(ctx, &pubsub.Message{
        Data:        []byte("hello from pscompat/GMK"),
        OrderingKey: "user-123", // becomes the Kafka message key
        Attributes:  map[string]string{"source": "go-client"},
    })
    id, err := result.Get(ctx)
    if err != nil { panic(err) }
    fmt.Println("Published:", id)
    

## Decommission Pub/Sub Lite resources

When every publisher and consumer is using Managed Service for Apache Kafka and you observe steady-state operation, decommission your Pub/Sub Lite resources as follows:

  1. Stop the Pub/Sub Source connector and delete it.
  2. Delete the Pub/Sub bridge topic and subscription.
  3. Delete the Pub/Sub Lite export subscription.
  4. Delete the Pub/Sub Lite topic and any remaining Pub/Sub Lite subscriptions.



## Authentication

Both client libraries authenticate to Managed Service for Apache Kafka with `SASL_SSL` / `OAUTHBEARER` using [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc):

  * **Java** : `GmkUtils.buildGmkKafkaProperties` returns a property map preconfigured with:

    * `sasl.mechanism=OAUTHBEARER`
    * `sasl.login.callback.handler.class=com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler`
    * The correct `sasl.jaas.config`

Make sure the Kafka authorization callback handler from `managed-kafka-auth-login-handler` is on your classpath.

  * **Go** : `pscompat.NewGMKSaramaConfig(ctx)` returns a `*sarama.Config` with TLS enabled and a built-in `sarama.AccessTokenProvider` backed by `golang.org/x/oauth2/google.FindDefaultCredentials`. You can pass this config to `KafkaConfig.SaramaConfig`, or leave it `nil` and let the library build one.




The underlying principal must have the `roles/managedkafka.client` role and any topic-level ACLs on the Managed Service for Apache Kafka cluster.

## Operational checklist

Use the following checklist to track the migration steps.

Pub/Sub Lite export subscription created and exporting to the bridge topic.

Pub/Sub Source connector running and configured with `kafka.key.attribute=orderingKey`.

Kafka topic partition count matches Pub/Sub Lite topic partition count.

Side-by-side consumer comparison shows parity for representative traffic.

Offset migration returns `SUCCESS` with `validated=true` on every partition.

Post-migration backlog on Managed Service for Apache Kafka is shrinking, not growing.

Publishers are switched and producing the expected Kafka message keys.

Pub/Sub Lite replication pipeline is deleted.

## Offset migration orchestrator

Use the following code to implement the timestamp-based offset translation strategy for migrating consumers.

###  Java 
    
    
    import com.google.cloud.pubsublite.*;
    import com.google.cloud.pubsublite.cloudpubsub.GmkUtils;
    import com.google.cloud.pubsublite.internal.*;
    import com.google.cloud.pubsublite.internal.OffsetMigrationHelper.MigrationResult;
    import java.util.*;
    
    String projectId   = "PROJECT_ID";
    String region      = "us-central1";
    String pslTopic    = "PSL_TOPIC";
    String pslSub      = "PSL_SUBSCRIPTION";
    String gmkCluster  = "GMK_CLUSTER_ID";
    String gmkTopic    = "GMK_TOPIC";
    int partitionCount = 3;
    
    [CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html) pslZone = [CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region), 'a');
    [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html) pslTopicPath = [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html).newBuilder()
        .setProject([ProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectId.html).of(projectId)).setLocation(pslZone)
        .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html).of(pslTopic)).build();
    [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) pslSubPath = [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
        .setProject([ProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectId.html).of(projectId)).setLocation(pslZone)
        .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html).of(pslSub)).build();
    [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) gmkSubPath = [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
        .setProject([ProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectId.html).of(projectId)).setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region))
        .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html).of(gmkTopic)).build();
    
    Map<String, Object> gmkProperties =
        GmkUtils.buildGmkKafkaProperties(projectId, region, gmkCluster);
    
    [CursorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.CursorClient.html)        pslCursor   = [CursorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.CursorClient.html).create(
        [CursorClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.CursorClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region)).build());
    [TopicStatsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.TopicStatsClient.html)    pslStats    = [TopicStatsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.TopicStatsClient.html).create(
        [TopicStatsClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.TopicStatsClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region)).build());
    KafkaTopicStatsClient kafkaStats = new KafkaTopicStatsClient([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region), gmkProperties);
    KafkaCursorClient   kafkaCursor = new KafkaCursorClient([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(region), gmkProperties);
    
    MigrationOrchestrator orchestrator = MigrationOrchestrator.newBuilder()
        .setPslCursorClient(pslCursor)
        .setPslTopicStatsClient(pslStats)
        .setKafkaTopicStatsClient(kafkaStats)
        .setKafkaCursorClient(kafkaCursor)
        .setPslTopicPath(pslTopicPath)
        .setPslSubscriptionPath(pslSubPath)
        .setKafkaSubscriptionPath(gmkSubPath)
        .setKafkaTopicName(gmkTopic)
        .[setPartitionCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicPartitions.Builder.html#com_google_cloud_pubsublite_proto_TopicPartitions_Builder_setPartitionCount_long_)(partitionCount)
        .setDryRun(false)        // set true to preview without committing
        .setValidate(true)       // re-read committed offsets after reset
        .build();
    
    MigrationOrchestrator.Result result = orchestrator.execute();
    System.out.println(result.getSummary());
    for (Map.Entry<Partition, MigrationResult> e : result.getPartitionResults().entrySet()) {
      MigrationResult r = e.getValue();
      System.out.printf("partition=%d pslOffset=%d kafkaOffset=%d status=%s validated=%b%n",
          e.getKey().value(), r.getPslOffset(), r.getKafkaOffset(), r.getStatus(), r.isValidated());
    }
    

###  Go 
    
    
    import (
        "context"
        "fmt"
        "log"
    
        vkit "cloud.google.com/go/pubsublite/apiv1"
        "cloud.google.com/go/pubsublite/pscompat"
        "google.golang.org/api/option"
    )
    
    const (
        projectID    = "PROJECT_ID"
        region       = "us-central1"
        pslTopic     = "PSL_TOPIC"
        pslSub       = "PSL_SUBSCRIPTION"
        gmkCluster   = "GMK_CLUSTER_ID"
        gmkTopic     = "GMK_TOPIC"
        gmkGroupID   = "GMK_CONSUMER_GROUP"   // your application's Kafka consumer group
        partitions   = 3
    )
    
    ctx := context.Background()
    pslZone := region + "-a"
    pslTopicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s",        projectID, pslZone, pslTopic)
    pslSubPath   := fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", projectID, pslZone, pslSub)
    bootstrap    := pscompat.[BuildGMKBootstrapServer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_BuildGMKBootstrapServer)(projectID, region, gmkCluster)
    pslEndpoint  := fmt.Sprintf("%s-pubsublite.googleapis.com:443", region)
    
    pslCursor,  _ := vkit.[NewCursorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/apiv1.html#cloud_google_com_go_pubsublite_apiv1_CursorClient_NewCursorClient)(ctx,     option.WithEndpoint(pslEndpoint))
    pslStats,   _ := vkit.[NewTopicStatsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/apiv1.html#cloud_google_com_go_pubsublite_apiv1_TopicStatsClient_NewTopicStatsClient)(ctx, option.WithEndpoint(pslEndpoint))
    kafkaStats, _ := pscompat.[NewKafkaTopicStatsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_KafkaTopicStatsClient_NewKafkaTopicStatsClient)(ctx,
        &pscompat.[KafkaTopicStatsClientConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_KafkaTopicStatsClientConfig){BootstrapServers: bootstrap})
    kafkaCursor,_ := pscompat.[NewKafkaCursorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_KafkaCursorClient_NewKafkaCursorClient)(ctx,
        &pscompat.[KafkaCursorClientConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_KafkaCursorClientConfig){BootstrapServers: bootstrap})
    defer pslCursor.Close(); defer pslStats.Close()
    defer kafkaStats.Close(); defer kafkaCursor.Close()
    
    parts := make([]int32, partitions)
    for i := range parts {
        parts[i] = int32(i)
    }
    
    cfg := &pscompat.[MigrationConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_MigrationConfig){
        PSLCursorClient:     pslCursor,
        PSLTopicStatsClient: pslStats,
        PSLTopicPath:        pslTopicPath,
        PSLSubscriptionPath: pslSubPath,
        KafkaTopicStats:     kafkaStats,
        KafkaCursor:         kafkaCursor,
        KafkaTopicName:      gmkTopic,
        KafkaGroupID:        gmkGroupID,
        Partitions:          parts,
        DryRun:              false, // set true to preview
        Validate:            true,  // re-read committed offsets after reset
    }
    
    orch := pscompat.[NewMigrationOrchestrator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_MigrationOrchestrator_NewMigrationOrchestrator)(cfg)
    summary, err := orch.[Execute](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/pscompat.html#cloud_google_com_go_pubsublite_pscompat_MigrationOrchestrator_Execute)(ctx)
    if err != nil { log.Fatal(err) }
    fmt.Print(summary.Summary)
    for _, p := range parts {
        r := summary.PartitionResults[p]
        fmt.Printf("partition=%d pslOffset=%d kafkaOffset=%d status=%s validated=%t\n",
            p, r.PSLOffset, r.KafkaOffset, r.Status, r.Validated)
    }
    

## What's next

  * [Managed Service for Apache Kafka overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)
  * [Kafka Connect overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview)
  * [Pub/Sub Lite Client for Java](https://github.com/googleapis/java-pubsublite) (GitHub)
  * [`pubsublite/pscompat` package](https://pkg.go.dev/cloud.google.com/go/pubsublite/pscompat)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
