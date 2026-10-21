---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-resume-publish-with-ordering-keys/
title: Resume publishing with ordering keys \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:07.884351+00:00
---

# Resume publishing with ordering keys  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-resume-publish-with-ordering-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Resume publishing with ordering keys Stay organized with collections  Save and categorize content based on your preferences. 

When publishing with an ordering key fails, queued-up messages of the same ordering key in the publisher fail, as well as future publish requests of this ordering key. This sample shows how to resume publishing with ordering keys enabled when such failures occur.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Retry requests](https://docs.cloud.google.com/pubsub/docs/retry-requests)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::StatusOr;
    [](pubsub::Publisher publisher) {
      struct SampleData {
        std::string ordering_key;
        std::string data;
      } data[] = {
          {"key1", "message1"}, {"key2", "message2"}, {"key1", "message3"},
          {"key1", "message4"}, {"key1", "message5"},
      };
      std::vector<future<void>> done;
      for (auto& datum : data) {
        auto const& da = datum;  // workaround MSVC lambda capture confusion
        auto handler = [da, publisher](future<StatusOr<std::string>> f) mutable {
          auto const msg = da.ordering_key + "#" + da.data;
          auto id = f.get();
          if (!id) {
            std::cout << "An error has occurred publishing " << msg << "\n";
            publisher.ResumePublish(da.ordering_key);
            return;
          }
          std::cout << "Message " << msg << " published as id=" << *id << "\n";
        };
        done.push_back(
            publisher
                .Publish(pubsub::MessageBuilder{}
                             .SetData("Hello World! [" + datum.data + "]")
                             .SetOrderingKey(datum.ordering_key)
                             .Build())
                .then(handler));
      }
      publisher.Flush();
      // Block until all the messages are published (optional)
      for (auto& f : done) f.get();
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class ResumePublishSample
    {
        public async Task<int> PublishOrderedMessagesAsync(string projectId, string topicId, IEnumerable<(string, string)> keysAndMessages)
        {
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
    
            var customSettings = new PublisherClient.Settings
            {
                EnableMessageOrdering = true
            };
    
            [PublisherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) publisher = await new [PublisherClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClientBuilder.html)
            {
                TopicName = topicName,
                Settings = customSettings
            }.BuildAsync();
    
            int publishedMessageCount = 0;
            var publishTasks = keysAndMessages.Select(async keyAndMessage =>
            {
                try
                {
                    string message = await publisher.PublishAsync(keyAndMessage.Item1, keyAndMessage.Item2);
                    Console.WriteLine($"Published message {message}");
                    Interlocked.Increment(ref publishedMessageCount);
                }
                catch (Exception exception)
                {
                    Console.WriteLine($"An error occurred when publishing message {keyAndMessage.Item2}: {exception.Message}");
                    publisher.ResumePublish(keyAndMessage.Item1);
                }
            });
            await Task.WhenAll(publishTasks);
            // PublisherClient instance should be shutdown after use.
            // The TimeSpan specifies for how long to attempt to publish locally queued messages.
            await publisher.[ShutdownAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_ShutdownAsync_System_Threading_CancellationToken_)(TimeSpan.FromSeconds(15));
            return publishedMessageCount;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"google.golang.org/api/option"
    )
    
    func resumePublishWithOrderingKey(w io.Writer, projectID, topicID string) {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    
    	// Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering key are in the same region
    	// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
    	client, err := pubsub.NewClient(ctx, projectID,
    		option.WithEndpoint("us-east1-pubsub.googleapis.com:443"))
    	if err != nil {
    		fmt.Fprintf(w, "pubsub.NewClient: %v", err)
    		return
    	}
    	defer client.Close()
    
    	// client.Publisher can be passed a topic ID (e.g. "my-topic") or
    	// a fully qualified name (e.g. "projects/my-project/topics/my-topic").
    	// If a topic ID is provided, the project ID from the client is used.
    	// Reuse this publisher for all publish calls to send messages in batches.
    	publisher := client.Publisher(topicID)
    	publisher.EnableMessageOrdering = true
    	key := "some-ordering-key"
    
    	result := publisher.Publish(ctx, &pubsub.Message{
    		Data:        []byte("some-message"),
    		OrderingKey: key,
    	})
    	_, err = result.Get(ctx)
    	if err != nil {
    		// Fix internal state to make sure publishes with errors are not
    		// published out of order. This might mean moving messages to a queue
    		// and retrying those messages before publishing subsquent messages.
    		fmt.Printf("Failed to publish: %s\n", err)
    
    		// Resume publish on an ordering key that has had unrecoverable errors.
    		// After such an error publishes with this ordering key will fail
    		// until this method is called.
    		publisher.ResumePublish(key)
    	}
    
    	fmt.Fprint(w, "Published a message with ordering key successfully\n")
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutureCallback](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutureCallback.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.common.util.concurrent.MoreExecutors;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.util.LinkedHashMap;
    import java.util.Map;
    import java.util.concurrent.TimeUnit;
    
    public class ResumePublishWithOrderingKeys {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Choose an existing topic.
        String topicId = "your-topic-id";
    
        resumePublishWithOrderingKeysExample(projectId, topicId);
      }
    
      public static void resumePublishWithOrderingKeysExample(String projectId, String topicId)
          throws IOException, InterruptedException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        // Create a publisher and set message ordering to true.
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher =
            [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName)
                .setEnableMessageOrdering(true)
                .setEndpoint("us-east1-pubsub.googleapis.com:443")
                .build();
    
        try {
          Map<String, String> messages = new LinkedHashMap<String, String>();
          messages.put("message1", "key1");
          messages.put("message2", "key2");
          messages.put("message3", "key1");
          messages.put("message4", "key2");
    
          for (Map.Entry<String, String> entry : messages.entrySet()) {
            ByteString data = ByteString.copyFromUtf8(entry.getKey());
            PubsubMessage pubsubMessage =
                PubsubMessage.newBuilder().setData(data).setOrderingKey(entry.getValue()).build();
            ApiFuture<String> future = publisher.publish(pubsubMessage);
    
            // Add an asynchronous callback to handle publish success / failure.
            ApiFutures.addCallback(
                future,
                new ApiFutureCallback<String>() {
    
                  @Override
                  public void onFailure(Throwable throwable) {
                    if (throwable instanceof ApiException) {
                      ApiException apiException = ((ApiException) throwable);
                      // Details on the API exception.
                      System.out.println(apiException.getStatusCode().getCode());
                      System.out.println(apiException.isRetryable());
                    }
                    System.out.println("Error publishing message : " + pubsubMessage.getData());
                    // (Beta) Must call resumePublish to reset key and continue publishing with order.
                    publisher.resumePublish(pubsubMessage.getOrderingKey());
                  }
    
                  @Override
                  public void onSuccess(String messageId) {
                    // Once published, returns server-assigned message ids (unique within the topic).
                    System.out.println(pubsubMessage.getData() + " : " + messageId);
                  }
                },
                MoreExecutors.directExecutor());
          }
        } finally {
          publisher.shutdown();
          publisher.awaitTermination(1, TimeUnit.MINUTES);
        }
      }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    # Start sending messages in one request once the size of all queued messages
    # reaches 1 MB or the number of queued messages reaches 20
    publisher = pubsub.[publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id, async: {
      max_bytes:    1_000_000,
      max_messages: 20
    }
    
    publisher.enable_message_ordering!
    10.times do |i|
      publisher.[publish_async](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) "This is message ##{i}.",
                              ordering_key: "ordering-key" do |result|
        if result.succeeded?
          puts "Message ##{i} successfully published."
        else
          puts "Message ##{i} failed to publish"
          # Allow publishing to continue on "ordering-key" after processing the
          # failure.
          publisher.resume_publish "ordering-key"
        end
      end
    end
    
    # Stop the async_publisher to send all queued messages immediately.
    publisher.[async_publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html).stop!

### Rust
    
    
    use google_cloud_pubsub::client::Publisher;
    use google_cloud_pubsub::model::Message;
    
    pub async fn sample(project: &str, topic_id: &str) -> anyhow::Result<()> {
        let publisher = Publisher::builder(format!("projects/{project}/topics/{topic_id}"))
            // Pub/Sub's ordered delivery guarantee only applies when publishes for
            // an ordering key are in the same region.
            .with_endpoint("https://us-east1-pubsub.googleapis.com")
            .build()
            .await?;
    
        let ordering_key = "ordering-key";
        let result = publisher.publish(
            Message::new()
                .set_data("message")
                .set_ordering_key(ordering_key),
        );
    
        match result.await {
            Ok(message_id) => println!("published message with ID: {message_id}"),
            Err(e) => {
                // Fix internal state to make sure publishes with errors are not
                // published out of order. This might mean moving messages to a queue
                // and retrying those messages before publishing subsequent messages.
                println!("error publishing message: {e}");
    
                // Resume publish on an ordering key that has had unrecoverable errors.
                // After an error, publishes with this ordering key will fail
                // until this method is called.
                publisher.resume_publish(ordering_key);
            }
        }
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
