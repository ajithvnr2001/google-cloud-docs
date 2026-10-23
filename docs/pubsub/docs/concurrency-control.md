---
url: https://docs.cloud.google.com/pubsub/docs/concurrency-control/
title: Process more messages with concurrency control \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:39.617565+00:00
---

# Process more messages with concurrency control  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/concurrency-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Process more messages with concurrency control Stay organized with collections  Save and categorize content based on your preferences. 

**Key Point:** Concurrency control lets you configure the number of threads or streams that the Pub/Sub client library uses to pull messages. With more threads, you can process more messages concurrently.

Concurrency control is an available feature in the Pub/Sub [high-level client library](https://docs.cloud.google.com/pubsub/docs/pull#high_client_library). You can also implement your own concurrency control when you're using a [low-level library](https://docs.cloud.google.com/pubsub/docs/pull#low_client_library).

Support for concurrency control depends on the programming language of the client library. For language implementations that support parallel threads, such as C++, Go, and Java, the client libraries make a default choice for the number of threads.

This choice might not be optimal for your application. For example, if your subscriber application is not keeping up with the incoming message volume and is not CPU-bound, you must increase the thread count. For CPU-intensive message processing operations, reducing the number of threads might be appropriate.

This page explains the concept of concurrency control and how to set up the feature for your subscriber clients. To configure your publisher clients for concurrency control, see [Concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control-messages).

## Concurrency control configurations

The default values for the concurrency control variables and the names of the variables might differ across client libraries. For more information, see the [API Reference documentation](https://docs.cloud.google.com/pubsub/docs/reference/libraries#additional_resources). For example, in the Java client library, the methods to configure concurrency control are `setParallelPullCount()`, `setExecutorProvider()`, `setSystemExecutorProvider()`, and `setChannelProvider()`.

  * **setParallelPullCount()** lets you decide how many streams to open. You can open more streams if your subscriber client can handle more data than is sent on a single stream, which is 10 MBps.

  * **setExecutorProvider()** lets you customize the executor provider used for processing messages. For example, you can change the executor provider to one that returns a single, shared executor with a limited number of threads across multiple subscriber clients. This configuration helps to limit the number of threads created. The total number of threads used for concurrency control depends on the executor provider passed in the client library and the parallel pull count.

  * **setSystemExecutorProvider()** lets you customize the executor provider used for [lease management](https://docs.cloud.google.com/pubsub/docs/lease-management). Typically, you don't configure this value unless you want to use the same executor provider in `setExecutorProvider` and `setSystemExecutorProvider`. For example, you can use the same executor provider if you have a number of low-throughput subscriptions. Using the same value limits the number of threads in the client.

  * **setChannelProvider()** lets you customize the channel provider used for opening connections to Pub/Sub. Typically, you don't configure this value unless you want to use the same channel across multiple subscriber clients. Reusing a channel across too many clients might result in `GOAWAY` or `ENHANCE_YOUR_CALM` errors. If you see these errors in your application's logs or [Cloud Logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), create more channels.




## Code samples for concurrency control

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
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

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
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

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
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

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
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

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
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

Read about the other delivery options you can configure for a subscription:

  * [Handle transient spikes with flow control](https://docs.cloud.google.com/pubsub/docs/flow-control)

  * [Handle message failures with subscription retry policy](https://docs.cloud.google.com/pubsub/docs/handling-failures#subscription_retry_policy)

  * [Forward undelivered messages to a dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic)

  * [Replay previously-acked messages or purge messages](https://docs.cloud.google.com/pubsub/docs/replay-overview)

  * [Extend ack time with lease management](https://docs.cloud.google.com/pubsub/docs/lease-management)

  * [Receive messages in order](https://docs.cloud.google.com/pubsub/docs/ordering)

  * [Filter messages by their attributes](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter)

  * [Receive and acknowledge messages exactly-once](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
