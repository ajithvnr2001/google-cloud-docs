---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-concurrency-control/
title: Subscribe with concurrency control \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:04.301421+00:00
---

# Subscribe with concurrency control  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-concurrency-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Subscribe with concurrency control Stay organized with collections  Save and categorize content based on your preferences. 

Configures number of threads for receiving messages and processing message callbacks.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Process more messages with concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::GrpcBackgroundThreadPoolSizeOption;
    using ::google::cloud::Options;
    using ::google::cloud::StatusOr;
    auto sample = [](std::string project_id, std::string subscription_id) {
      // Create a subscriber with 16 threads handling I/O work, by default the
      // library creates `std::thread::hardware_concurrency()` threads.
      auto subscriber = pubsub::Subscriber(pubsub::MakeSubscriberConnection(
          pubsub::Subscription(std::move(project_id), std::move(subscription_id)),
          Options{}
              .set<pubsub::MaxConcurrencyOption>(8)
              .set<GrpcBackgroundThreadPoolSizeOption>(16)));
    
      // Create a subscription where up to 8 messages are handled concurrently. By
      // default the library uses `std::thread::hardware_concurrency()` as the
      // maximum number of concurrent callbacks.
      auto session = subscriber.Subscribe(
          [](pubsub::Message const& m, pubsub::AckHandler h) {
            // This handler executes in the I/O threads, applications could use,
            // std::async(), a thread-pool, or any other mechanism to transfer the
            // execution to other threads.
            std::cout << "Received message " << m << "\n";
            std::move(h).ack();
            PleaseIgnoreThisSimplifiesTestingTheSamples();
          });
      return std::make_pair(subscriber, std::move(session));
    };

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class SubscriberConcurrencyControlSample
    {
        public async Task<int> SubscribeWithConcurrencyControlAsync(string projectId, string subscriptionId)
        {
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
    
            [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html) subscriber = await new [SubscriberClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClientBuilder.html)
            {
                SubscriptionName = subscriptionName,
                // Normally the number of clients depends on the number of processors.
                // Here we explicitly request 2 concurrent clients instead.
                ClientCount = 2
            }.BuildAsync();
    
            int count = 0;
            Task startTask = subscriber.[StartAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StartAsync_Google_Cloud_PubSub_V1_SubscriptionHandler_)(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, CancellationToken cancellationToken) =>
            {
                string text = message.Data.ToStringUtf8();
                Console.WriteLine($"Received message: {text}");
                Interlocked.Increment(ref count);
                return Task.FromResult([SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack));
            });
            // Run for 10 seconds.
            await Task.Delay(10_000);
            await subscriber.[StopAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StopAsync_Google_Cloud_PubSub_V1_SubscriberClient_ShutdownOptions_System_Threading_CancellationToken_)(CancellationToken.None);
            // Lets make sure that the start task finished successfully after the call to stop.
            await startTask;
            return count;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"sync/atomic"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    )
    
    func pullMsgsConcurrencyControl(w io.Writer, projectID, subID string) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// client.Subscriber can be passed a subscription ID (e.g. "my-sub") or
    	// a fully qualified name (e.g. "projects/my-project/subscriptions/my-sub").
    	// If a subscription ID is provided, the project ID from the client is used.
    	sub := client.Subscriber(subID)
    	// NumGoroutines determines the number of streams sub.Receive will spawn to pull
    	// messages. It is recommended to set this to 1, unless your throughput
    	// is greater than 10 MB/s, as even having 1 stream can still result in
    	// messages being handled asynchronously.
    	sub.ReceiveSettings.NumGoroutines = 1
    	// MaxOutstandingMessages limits the number of concurrent handlers of messages.
    	// In this case, up to 8 unacked messages can be handled concurrently.
    	sub.ReceiveSettings.MaxOutstandingMessages = 8
    
    	// Receive messages for 10 seconds, which simplifies testing.
    	// Comment this out in production, since `Receive` should
    	// be used as a long running operation.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	var received int32
    
    	// Receive blocks until the context is cancelled or an error occurs.
    	err = sub.Receive(ctx, func(_ context.Context, msg *pubsub.Message) {
    		atomic.AddInt32(&received, 1)
    		msg.Ack()
    	})
    	if err != nil {
    		return fmt.Errorf("sub.Receive returned error: %w", err)
    	}
    	fmt.Fprintf(w, "Received %d messages\n", received)
    
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
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SubscribeWithConcurrencyControlExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
    
        subscribeWithConcurrencyControlExample(projectId, subscriptionId);
      }
    
      public static void subscribeWithConcurrencyControlExample(
          String projectId, String subscriptionId) {
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
          // Provides an executor service for processing messages. The default `executorProvider` used
          // by the subscriber has a default thread count of 5.
          [ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html) executorProvider =
              [InstantiatingExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.html).newBuilder().[setExecutorThreadCount](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html#com_google_api_gax_core_InstantiatingExecutorProvider_Builder_setExecutorThreadCount_int_)(4).build();
    
          // `setParallelPullCount` determines how many StreamingPull streams the subscriber will open
          // to receive message. It defaults to 1. `setExecutorProvider` configures an executor for the
          // subscriber to process messages. Here, the subscriber is configured to open 2 streams for
          // receiving messages, each stream creates a new executor with 4 threads to help process the
          // message callbacks. In total 2x4=8 threads are used for message processing.
          subscriber =
              [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver)
                  .[setParallelPullCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.Builder.html#com_google_cloud_pubsub_v1_Subscriber_Builder_setParallelPullCount_int_)(2)
                  .setExecutorProvider(executorProvider)
                  .build();
    
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

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription_id
    
    # Use 2 threads for streaming, 4 threads for executing callbacks and 2 threads
    # for sending acknowledgements and/or delays
    listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) streams: 2, threads: {
      callback: 4,
      push:     2
    } do |received_message|
      puts "Received message: #{received_message.data}"
      received_message.[acknowledge!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
    end
    
    listener.[start](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-MessageListener.html)
    # Let the main thread sleep for 60 seconds so the thread for listening
    # messages does not quit
    sleep 60
    listener.stop.wait!

### Rust
    
    
    use google_cloud_pubsub::client::Subscriber;
    use google_cloud_pubsub::subscriber::MessageStream;
    use std::time::Duration;
    
    pub async fn sample(project_id: &str, subscription_id: &str) -> anyhow::Result<()> {
        // Assume an available concurrency of 2 for this sample.
        const NCPU: usize = 2;
    
        let subscription_name = format!("projects/{project_id}/subscriptions/{subscription_id}");
        let client = Subscriber::builder()
            // Configure the subscriber to use multiple gRPC channels. This lets the
            // client multiplex its open streams and its acknowledgement RPCs.
            .with_grpc_subchannel_count(NCPU)
            .build()
            .await?;
        let tasks: Vec<_> = (0..2 * NCPU)
            .map(|i| {
                // Pub/Sub caps the throughput of a single stream to 10 MB/s. To achieve
                // higher throughput, you should open multiple streams.
                let stream = client.subscribe(&subscription_name).build();
                tokio::spawn(subscribe_task(i, stream))
            })
            .collect();
    
        for t in tasks {
            t.await??;
        }
        println!("done listening for messages");
        Ok(())
    }
    
    async fn subscribe_task(index: usize, mut stream: MessageStream) -> anyhow::Result<()> {
        // Terminate the example after 10 seconds.
        let shutdown_token = stream.shutdown_token();
        let shutdown = tokio::spawn(async move {
            tokio::time::sleep(Duration::from_secs(10)).await;
            shutdown_token.shutdown().await;
        });
    
        println!("listening for messages on stream {index}...");
    
        while let Some((m, h)) = stream.next().await.transpose()? {
            println!("received message: {m:?}");
            h.ack();
        }
        shutdown.await?;
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
