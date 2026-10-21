---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-kafka-producer/
title: Publish messages from Apache Kafka \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:45.528852+00:00
---

# Publish messages from Apache Kafka  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-kafka-producer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Publish messages from Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

Publish messages to a Pub/Sub Lite topic using a shim for the Kafka Producer API

## Code sample

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.kafka.[ProducerSettings](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ProducerSettings.html);
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.Future;
    import org.apache.kafka.clients.producer.Producer;
    import org.apache.kafka.clients.producer.ProducerRecord;
    import org.apache.kafka.clients.producer.RecordMetadata;
    
    public class ProducerExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Use an existing Pub/Sub Lite topic.
        String topicId = "your-topic-id";
        // Using the project number is required for constructing a Pub/Sub Lite
        // topic path that the Kafka producer can use.
        long projectNumber = Long.parseLong("123456789");
    
        producerExample(cloudRegion, zoneId, projectNumber, topicId);
      }
    
      public static void producerExample(
          String cloudRegion, char zoneId, long projectNumber, String topicId)
          throws InterruptedException, ExecutionException {
        [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html) topicPath =
            [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html).newBuilder()
                .setLocation([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId))
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html).of(topicId))
                .build();
    
        [ProducerSettings](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ProducerSettings.html) producerSettings =
            [ProducerSettings](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ProducerSettings.html).newBuilder().setTopicPath(topicPath).build();
    
        List<Future<RecordMetadata>> futures = new ArrayList<>();
        try (Producer<byte[], byte[]> producer = producerSettings.[instantiate](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ProducerSettings.html#com_google_cloud_pubsublite_kafka_ProducerSettings_instantiate__)()) {
          for (long i = 0L; i < 10L; i++) {
            String key = "demo";
            Future<RecordMetadata> future =
                producer.send(
                    new ProducerRecord(
                        [topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)(), [key](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_key__).getBytes(), ("message-" + i).getBytes()));
            futures.add(future);
          }
          for (Future<RecordMetadata> future : futures) {
            RecordMetadata meta = future.get();
            System.out.println(meta.offset());
          }
        }
        System.out.printf("Published 10 messages to %s%n", [topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)());
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
