---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-with-ordering-keys/
title: Publish with ordering keys \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:05.677897+00:00
---

# Publish with ordering keys  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-with-ordering-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Publish with ordering keys Stay organized with collections  Save and categorize content based on your preferences. 

Publishes messages with an ordering key. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Publish messages to topics](https://docs.cloud.google.com/pubsub/docs/publisher)



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
        auto message_id =
            publisher.Publish(pubsub::MessageBuilder{}
                                  .SetData("Hello World! [" + datum.data + "]")
                                  .SetOrderingKey(datum.ordering_key)
                                  .Build());
        std::string ack_id = datum.ordering_key + "#" + datum.data;
        done.push_back(message_id.then([ack_id](future<StatusOr<std::string>> f) {
          auto id = f.get();
          if (!id) throw std::move(id).status();
          std::cout << "Message " << ack_id << " published with id=" << *id
                    << "\n";
        }));
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
    
    public class PublishOrderedMessagesAsyncSample
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
                // Sending messages to the same region ensures they are received in order even when multiple publishers are used.
                Endpoint = "us-east1-pubsub.googleapis.com:443",
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
    	"sync"
    	"sync/atomic"
    
    	"cloud.google.com/go/pubsub/v2"
    	"google.golang.org/api/option"
    )
    
    func publishWithOrderingKey(w io.Writer, projectID, topicID string) {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    
    	// Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering key are in the same region.
    	// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
    	client, err := pubsub.NewClient(ctx, projectID,
    		option.WithEndpoint("us-east1-pubsub.googleapis.com:443"))
    	if err != nil {
    		fmt.Fprintf(w, "pubsub.NewClient: %v", err)
    		return
    	}
    	defer client.Close()
    
    	var wg sync.WaitGroup
    	var totalErrors uint64
    
    	// client.Publisher can be passed a topic ID (e.g. "my-topic") or
    	// a fully qualified name (e.g. "projects/my-project/topics/my-topic").
    	// If a topic ID is provided, the project ID from the client is used.
    	// Reuse this publisher for all publish calls to send messages in batches.
    	publisher := client.Publisher(topicID)
    	publisher.EnableMessageOrdering = true
    
    	messages := []struct {
    		message     string
    		orderingKey string
    	}{
    		{
    			message:     "message1",
    			orderingKey: "key1",
    		},
    		{
    			message:     "message2",
    			orderingKey: "key2",
    		},
    		{
    			message:     "message3",
    			orderingKey: "key1",
    		},
    		{
    			message:     "message4",
    			orderingKey: "key2",
    		},
    	}
    
    	for _, m := range messages {
    		result := publisher.Publish(ctx, &pubsub.Message{
    			Data:        []byte(m.message),
    			OrderingKey: m.orderingKey,
    		})
    
    		wg.Add(1)
    		go func(res *pubsub.PublishResult) {
    			defer wg.Done()
    			// The Get method blocks until a server-generated ID or
    			// an error is returned for the published message.
    			_, err := res.Get(ctx)
    			if err != nil {
    				// Error handling code can be added here.
    				fmt.Printf("Failed to publish: %s\n", err)
    				atomic.AddUint64(&totalErrors, 1)
    				return
    			}
    		}(result)
    	}
    
    	wg.Wait()
    
    	if totalErrors > 0 {
    		fmt.Fprintf(w, "%d of 4 messages did not publish successfully", totalErrors)
    		return
    	}
    
    	fmt.Fprint(w, "Published 4 messages with ordering keys successfully\n")
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
    
    public class PublishWithOrderingKeys {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Choose an existing topic.
        String topicId = "your-topic-id";
    
        publishWithOrderingKeysExample(projectId, topicId);
      }
    
      public static void publishWithOrderingKeysExample(String projectId, String topicId)
          throws IOException, InterruptedException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        // Create a publisher and set message ordering to true.
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher =
            [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName)
                // Sending messages to the same region ensures they are received in order
                // even when multiple publishers are used.
                .setEndpoint("us-east1-pubsub.googleapis.com:443")
                .setEnableMessageOrdering(true)
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
          // When finished with the publisher, shutdown to free up resources.
          publisher.shutdown();
          publisher.awaitTermination(1, TimeUnit.MINUTES);
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\MessageBuilder;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Publishes a message for a Pub/Sub topic.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     */
    function publish_with_ordering_keys($projectId, $topicName)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $topic = $pubsub->topic($topicName);
        foreach (range(1, 5) as $i) {
            $topic->publish((new MessageBuilder(['orderingKey' => 'foo']))
                ->setData('message' . $i)->build(), ['enableMessageOrdering' => true]);
        }
    
        print('Message published' . PHP_EOL);
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
                              ordering_key: "ordering-key"
    end
    
    # Stop the async_publisher to send all queued messages immediately.
    publisher.[async_publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html).stop!
    puts "Messages published with ordering key."

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
    
        let publish_futures = [
            ("message1", "key1"),
            ("message2", "key2"),
            ("message3", "key1"),
            ("message4", "key2"),
        ]
        .map(|(data, ordering_key)| {
            publisher.publish(
                Message::new()
                    .set_data(data.as_bytes())
                    .set_ordering_key(ordering_key),
            )
        });
    
        for publish_future in publish_futures {
            let message_id = publish_future
                .await
                .inspect_err(|e| eprintln!("error publishing message: {e:?}"))?;
            println!("published message with ID: {message_id}");
        }
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
