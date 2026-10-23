---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-error-listener/
title: Subscribe with error listener \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:35.050461+00:00
---

# Subscribe with error listener  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-error-listener/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Subscribe with error listener Stay organized with collections  Save and categorize content based on your preferences. 

Handles errors when subscribing throws an error.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Receive messages from a pull subscription](https://docs.cloud.google.com/pubsub/docs/pull-messages)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    auto sample = [](pubsub::Subscriber subscriber) {
      return subscriber
          .Subscribe([&](pubsub::Message const& m, pubsub::AckHandler h) {
            std::cout << "Received message " << m << "\n";
            std::move(h).ack();
            PleaseIgnoreThisSimplifiesTestingTheSamples();
          })
          // Setup an error handler for the subscription session
          .then([](future<google::cloud::Status> f) {
            std::cout << "Subscription session result: " << f.get() << "\n";
          });
    };

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class SubscriberErrorListenerSample
    {
        public async Task<int> SubscriberErrorListener(string projectId, string subscriptionId)
        {
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
            [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html) subscriber = await [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_CreateAsync_Google_Cloud_PubSub_V1_SubscriptionName_)(subscriptionName);
    
            int messageCount = 0;
            try
            {
                Task startTask = subscriber.[StartAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StartAsync_Google_Cloud_PubSub_V1_SubscriptionHandler_)(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, CancellationToken cancel) =>
                {
                    string text = message.Data.ToStringUtf8();
                    Console.WriteLine($"Message {message.MessageId}: {text}");
                    Interlocked.Increment(ref messageCount);
                    return Task.FromResult([SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack));
                });
                // Run for 5 seconds.
                await Task.Delay(5000);
                await subscriber.[StopAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StopAsync_Google_Cloud_PubSub_V1_SubscriberClient_ShutdownOptions_System_Threading_CancellationToken_)(CancellationToken.None);
                // Wait for the StartAsync call to finish
                await startTask;
            }
            // Catch unrecoverable failures.
            catch (Exception e)
            {
                Console.WriteLine($"Message: {e.Message}");
                Console.WriteLine($"StackTrace: {e.StackTrace}");
            }
            return messageCount;
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
    )
    
    func pullMsgsError(w io.Writer, projectID, subID string) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// If the service returns a non-retryable error, Receive returns that error after
    	// all of the outstanding calls to the handler have returned.
    	// client.Subscriber can be passed a subscription ID (e.g. "my-sub") or
    	// a fully qualified name (e.g. "projects/my-project/subscriptions/my-sub").
    	// If a subscription ID is provided, the project ID from the client is used.
    	sub := client.Subscriber(subID)
    	err = sub.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		fmt.Fprintf(w, "Got message: %q\n", string(msg.Data))
    		msg.Ack()
    	})
    	if err != nil {
    		return fmt.Errorf("Receive: %w", err)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.core.[ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html);
    import com.google.api.gax.core.[InstantiatingExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.common.util.concurrent.MoreExecutors;
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SubscribeWithErrorListenerExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
    
        subscribeWithErrorListenerExample(projectId, subscriptionId);
      }
    
      public static void subscribeWithErrorListenerExample(String projectId, String subscriptionId) {
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        // Instantiate an asynchronous message receiver.
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage message, AckReplyConsumer consumer) -> {
              // Handle incoming message, then ack the received message.
              System.out.println("Id: " + message.getMessageId());
              System.out.println("Data: " + message.getData().toStringUtf8());
              consumer.ack();
            };
    
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = null;
        try {
          // Provides an executor service for processing messages.
          [ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html) executorProvider =
              [InstantiatingExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.html).newBuilder().[setExecutorThreadCount](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html#com_google_api_gax_core_InstantiatingExecutorProvider_Builder_setExecutorThreadCount_int_)(4).build();
    
          subscriber =
              [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver)
                  .setExecutorProvider(executorProvider)
                  .build();
    
          // Listen for unrecoverable failures.
          subscriber.addListener(
              new [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).Listener() {
                public void failed([Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).State from, Throwable failure) {
                  System.out.println("Unrecoverable subscriber failure:" + failure.getStackTrace());
                }
              },
              MoreExecutors.directExecutor());
    
          // Start the subscriber.
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
          System.out.printf("Listening for messages on %s:\n", subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)());
          // Allow the subscriber to run for 30s unless an unrecoverable error occurs.
          subscriber.awaitTerminated(30, TimeUnit.SECONDS);
        } catch (TimeoutException timeoutException) {
          // Shut down the subscriber after 30s. Stop receiving messages.
          subscriber.stopAsync();
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Subscribes with an error listener
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $subscriptionId  The ID of the subscription.
     */
    function subscriber_error_listener(
        string $projectId,
        string $topicName,
        string $subscriptionId
    ): void {
    
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $subscription = $pubsub->subscription($subscriptionId, $topicName);
    
        try {
            $messages = $subscription->pull();
            foreach ($messages as $message) {
                printf('PubSub Message: %s' . PHP_EOL, $message->data());
                $subscription->acknowledge($message);
            }
        } catch (\Exception $e) { // Handle unrecoverable exceptions
            printf('Exception Message: %s' . PHP_EOL, $e->getMessage());
            printf('StackTrace: %s' . PHP_EOL, $e->getTraceAsString());
        }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription_id
    
    listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) do |received_message|
      puts "Received message: #{received_message.data}"
      received_message.[acknowledge!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
    end
    
    # Propagate exception from child threads to the main thread as soon as it is
    # raised. Exceptions happened in the callback thread are collected in the
    # callback thread pool and do not propagate to the main thread
    Thread.abort_on_exception = true
    
    begin
      listener.[start](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-MessageListener.html)
      # Let the main thread sleep for 60 seconds so the thread for listening
      # messages does not quit
      sleep 60
      listener.stop.wait!
    rescue StandardError => e
      puts "Exception #{e.inspect}: #{e.message}"
      raise "Stopped listening for messages."
    end

### Rust
    
    
    use google_cloud_pubsub::client::Subscriber;
    use std::time::Duration;
    
    pub async fn sample(project_id: &str, subscription_id: &str) -> anyhow::Result<()> {
        let subscription_name = format!("projects/{project_id}/subscriptions/{subscription_id}");
        let client = Subscriber::builder().build().await?;
        let mut stream = client.subscribe(subscription_name).build();
    
        // Terminate the example after 10 seconds.
        let shutdown_token = stream.shutdown_token();
        let shutdown = tokio::spawn(async move {
            tokio::time::sleep(Duration::from_secs(10)).await;
            shutdown_token.shutdown().await;
        });
    
        println!("listening for messages...");
    
        while let Some((m, h)) = stream
            .next()
            .await
            .transpose()
            .inspect_err(|e| println!("error receiving messages: {e:?}"))?
        {
            println!("received message: {m:?}");
            h.ack();
        }
        shutdown.await?;
    
        println!("done listening for messages");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
