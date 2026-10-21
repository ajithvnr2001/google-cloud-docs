---
url: https://docs.cloud.google.com/pubsub/docs/compress-messages/
title: Compress messages \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:52.436359+00:00
---

# Compress messages  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/compress-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Compress messages Stay organized with collections  Save and categorize content based on your preferences. 

If you are using Pub/Sub to publish messages that amount to a lot of data, you can use [gRPC](https://grpc.io/) to compress your data to save networking costs before your publisher client sends out the publish request. The Pub/Sub compression for gRPC uses the [Gzip](https://en.wikipedia.org/wiki/Gzip) algorithm.

This document provides information about compressing messages published to a topic.

## About compressing messages

**Note:** gRPC client-side compression is supported in Java and C++.**Note:** gRPC compression does not contribute to Pub/Sub cost savings.

The [compression ratio](https://en.wikipedia.org/wiki/Data_compression_ratio) for using the gRPC client-side compression feature is different for different publisher clients and dependent on the following factors:

  * **Amount of data.** The compression ratio improves when the size of the payload increases from a few hundred bytes to many kilobytes of data. The batch settings of a publish request decide the amount of data that is included in each publish request. We recommend that you turn on batch settings in conjunction with gRPC compression to get the best results.

  * **Type of data.** Text-based data such as JSON or XML are more compressible compared to binary data such as images.




If your publisher client is on Google Cloud, you can use the [**Sent bytes** (`instance/network/sent_bytes_count`)](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#compute/instance/network/sent_bytes_count) metric to measure the publishing throughput in bytes. If your publisher client is on a different application, you must use the client-specific tools for making the measurement.

The code sample in this section shows a sample Java client library code snippet that also includes gRPC compression.

## Before you begin

Before configuring the publish workflow, ensure you have completed the following tasks:

  * Learn about [topics and the publishing workflow](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).
  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).



### Required roles

To get the permissions that you need to compress messages, ask your administrator to grant you the [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role on your topic. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You need [additional permissions](https://docs.cloud.google.com/pubsub/docs/access-control) to create or update topics and subscriptions.

## Compress a message

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace g = ::google::cloud;
    namespace pubsub = ::google::cloud::pubsub;
    [](std::string project_id, std::string topic_id) {
      auto topic = pubsub::Topic(std::move(project_id), std::move(topic_id));
      auto publisher = pubsub::Publisher(pubsub::MakePublisherConnection(
          std::move(topic),
          g::Options{}
              // Compress any batch of messages over 10 bytes. By default, no
              // messages are compressed, set this to 0 to compress all batches,
              // regardless of their size.
              .set<pubsub::CompressionThresholdOption>(10)
              // Compress using the GZIP algorithm. By default, the library uses
              // GRPC_COMPRESS_DEFLATE.
              .set<pubsub::CompressionAlgorithmOption>(GRPC_COMPRESS_GZIP)));
      auto message_id = publisher.Publish(
          pubsub::MessageBuilder{}.SetData("Hello World!").Build());
      auto done = message_id.then([](g::future<g::StatusOr<std::string>> f) {
        auto id = f.get();
        if (!id) throw std::move(id).status();
        std::cout << "Hello World! published with id=" << *id << "\n";
      });
      // Block until the message is published
      done.get();
    }

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    
    public class PublishWithGrpcCompressionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Choose an existing topic.
        String topicId = "your-topic-id";
    
        publishWithGrpcCompressionExample(projectId, topicId);
      }
    
      public static void publishWithGrpcCompressionExample(String projectId, String topicId)
          throws IOException, ExecutionException, InterruptedException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
        // Create a publisher and set enable compression to true.
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null;
        try {
          // Enable compression and configure the compression threshold to 10 bytes (default to 240 B).
          // Publish requests of sizes > 10 B (excluding the request headers) will get compressed.
          // The number of messages in a publish request is determined by publisher batch settings.
          // Batching is turned off by default, i.e. each publish request contains only one message.
          publisher =
              [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName)
                  .[setEnableCompression](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.Builder.html#com_google_cloud_pubsub_v1_Publisher_Builder_setEnableCompression_boolean_)(true)
                  .[setCompressionBytesThreshold](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.Builder.html#com_google_cloud_pubsub_v1_Publisher_Builder_setCompressionBytesThreshold_long_)(10L)
                  .build();
    
          byte[] bytes = new byte[1024];
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(bytes);
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(data).build();
    
          // Once published, returns a server-assigned message id (unique within the topic).
          // You can look up the actual size of the outbound data using the Java Logging API.
          // Configure logging properties as shown in
          // https://github.com/googleapis/java-pubsub/tree/main/samples/snippets/src/main/resources/logging.properties
          // and look for "OUTBOUND DATA" with "length=" in the output log.
          ApiFuture<String> messageIdFuture = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubMessage);
          String messageId = messageIdFuture.get();
          System.out.println("Published a compressed message of message ID: " + messageId);
        } finally {
          if (publisher != null) {
            // When finished with the publisher, shutdown to free up resources.
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
        }
      }
    }

## What's next

To learn how to configure advanced publishing options, see the following:

  * [Retry requests](https://docs.cloud.google.com/pubsub/docs/retry-requests)

  * [Flow control](https://docs.cloud.google.com/pubsub/docs/flow-control-messages)

  * [Concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control-messages)

  * [Batch messaging](https://docs.cloud.google.com/pubsub/docs/batch-messaging)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
