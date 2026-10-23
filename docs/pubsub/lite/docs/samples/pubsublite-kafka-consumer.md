---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-kafka-consumer/
title: Receive messages in Apache Kafka \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:14.192056+00:00
---

# Receive messages in Apache Kafka  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-kafka-consumer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Receive messages in Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

Receive messages from a Pub/Sub Lite subscription using a shim for the Kafka Consumer API

## Code sample

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.cloudpubsub.[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html);
    import com.google.cloud.pubsublite.kafka.[ConsumerSettings](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings.html);
    import java.time.Duration;
    import java.util.Arrays;
    import java.util.Base64;
    import java.util.HashSet;
    import java.util.Set;
    import org.apache.kafka.clients.consumer.Consumer;
    import org.apache.kafka.clients.consumer.ConsumerRecord;
    import org.apache.kafka.clients.consumer.ConsumerRecords;
    
    public class ConsumerExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Use an existing Pub/Sub Lite topic and subscription.
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
        // Using the project number here is required for constructing a Pub/Sub Lite
        // topic path that the Kafka consumer can use.
        long projectNumber = Long.parseLong("123456789");
    
        consumerExample(cloudRegion, zoneId, projectNumber, topicId, subscriptionId);
      }
    
      public static void consumerExample(
          String cloudRegion, char zoneId, long projectNumber, String topicId, String subscriptionId) {
    
        [CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html) location = [CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId);
    
        [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html) topicPath =
            [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html).newBuilder()
                .setLocation(location)
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html).of(topicId))
                .build();
    
        [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscription =
            [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
                .setLocation(location)
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html).of(subscriptionId))
                .build();
    
        [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html) flowControlSettings =
            [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html).builder()
                // 50 MiB. Must be greater than the allowed size of the largest message (1 MiB).
                .setBytesOutstanding(50 * 1024 * 1024L)
                // 10,000 outstanding messages. Must be >0.
                .setMessagesOutstanding(10000L)
                .build();
    
        [ConsumerSettings](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings.html) settings =
            [ConsumerSettings](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings.html).newBuilder()
                .setSubscriptionPath(subscription)
                .setPerPartitionFlowControlSettings(flowControlSettings)
                .setAutocommit(true)
                .build();
    
        Set<ConsumerRecord<byte[], byte[]>> hashSet = new HashSet<>();
        try (Consumer<byte[], byte[]> consumer = settings.[instantiate](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings.html#com_google_cloud_pubsublite_kafka_ConsumerSettings_instantiate__)()) {
          // The consumer can only subscribe to the topic that it is associated to.
          // If this is the only subscriber for this subscription, it will take up
          // to 90s for the subscriber to warm up.
          consumer.subscribe(Arrays.asList([topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)()));
          while (true) {
            ConsumerRecords<byte[], byte[]> records = consumer.poll(Duration.ofMillis(100));
            for (ConsumerRecord<byte[], byte[]> record : records) {
              long offset = record.offset();
              String value = Base64.getEncoder().encodeToString(record.value());
              hashSet.add(record);
              System.out.printf("Received %s: %s%n", offset, value);
            }
            // Early exit. Remove entirely to keep the consumer alive indefinitely.
            if (hashSet.size() >= 10) {
              System.out.println("Received 10 messages.");
              break;
            }
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
