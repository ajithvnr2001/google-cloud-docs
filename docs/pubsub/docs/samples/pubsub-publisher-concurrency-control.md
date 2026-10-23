---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publisher-concurrency-control/
title: Publish with concurrency control \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:18.032554+00:00
---

# Publish with concurrency control  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publisher-concurrency-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Publish with concurrency control Stay organized with collections  Save and categorize content based on your preferences. 

Configures a publisher to have different numbers of threads for publishing messages and processing message futures. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control-messages)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::GrpcBackgroundThreadPoolSizeOption;
    using ::google::cloud::Options;
    using ::google::cloud::StatusOr;
    [](std::string project_id, std::string topic_id) {
      auto topic = pubsub::Topic(std::move(project_id), std::move(topic_id));
      // Override the default number of background (I/O) threads. By default the
      // library uses `std::thread::hardware_concurrency()` threads.
      auto options = Options{}.set<GrpcBackgroundThreadPoolSizeOption>(8);
      auto publisher = pubsub::Publisher(
          pubsub::MakePublisherConnection(std::move(topic), std::move(options)));
    
      std::vector<future<void>> ids;
      for (char const* data : {"1", "2", "3", "go!"}) {
        ids.push_back(
            publisher.Publish(pubsub::MessageBuilder().SetData(data).Build())
                .then([data](future<StatusOr<std::string>> f) {
                  auto s = f.get();
                  if (!s) return;
                  std::cout << "Sent '" << data << "' (" << *s << ")\n";
                }));
      }
      publisher.Flush();
      // Block until they are actually sent.
      for (auto& id : ids) id.get();
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    )
    
    func publishSingleGoroutine(w io.Writer, projectID, topicID, msg string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// msg := "Hello World"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// client.Publisher can be passed a topic ID (e.g. "my-topic") or
    	// a fully qualified name (e.g. "projects/my-project/topics/my-topic").
    	// If a topic ID is provided, the project ID from the client is used.
    	publisher := client.Publisher(topicID)
    	publisher.PublishSettings.NumGoroutines = 1
    
    	result := publisher.Publish(ctx, &pubsub.Message{Data: []byte(msg)})
    	// Block until the result is returned and a server-generated
    	// ID is returned for the published message.
    	id, err := result.Get(ctx)
    	if err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    	fmt.Fprintf(w, "Published a message; msg ID: %v\n", id)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.core.[ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html);
    import com.google.api.gax.core.[InstantiatingExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    
    public class PublishWithConcurrencyControlExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
    
        publishWithConcurrencyControlExample(projectId, topicId);
      }
    
      public static void publishWithConcurrencyControlExample(String projectId, String topicId)
          throws IOException, ExecutionException, InterruptedException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null;
        List<ApiFuture<String>> messageIdFutures = new ArrayList<>();
    
        try {
          // Provides an executor service for processing messages. The default
          // `executorProvider` used by the publisher has a default thread count of
          // 5 * the number of processors available to the Java virtual machine.
          [ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html) executorProvider =
              [InstantiatingExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.html).newBuilder().[setExecutorThreadCount](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html#com_google_api_gax_core_InstantiatingExecutorProvider_Builder_setExecutorThreadCount_int_)(4).build();
    
          // `setExecutorProvider` configures an executor for the publisher.
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName).setExecutorProvider(executorProvider).build();
    
          // schedule publishing one message at a time : messages get automatically batched
          for (int i = 0; i < 100; i++) {
            String message = "message " + i;
            [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
            [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(data).build();
    
            // Once published, returns a server-assigned message id (unique within the topic)
            ApiFuture<String> messageIdFuture = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubMessage);
            messageIdFutures.add(messageIdFuture);
          }
        } finally {
          // Wait on any pending publish requests.
          List<String> messageIds = [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[allAsList](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_allAsList_java_lang_Iterable___extends_com_google_api_core_ApiFuture___extends_V___)(messageIdFutures).get();
    
          System.out.println("Published " + messageIds.size() + " messages with concurrency control.");
    
          if (publisher != null) {
            // When finished with the publisher, shutdown to free up resources.
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
        }
      }
    }
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    publisher = pubsub.[publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id, async: {
      threads: {
        # Use exactly one thread for publishing message and exactly one thread
        # for executing callbacks
        publish:  1,
        callback: 1
      }
    }
    
    publisher.[publish_async](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) "This is a test message." do |result|
      raise "Failed to publish the message." unless result.succeeded?
      puts "Message published asynchronously."
    end
    
    # Stop the async_publisher to send all queued messages immediately.
    publisher.[async_publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html).stop.wait!

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
