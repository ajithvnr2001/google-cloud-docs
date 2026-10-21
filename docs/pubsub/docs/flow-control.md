---
url: https://docs.cloud.google.com/pubsub/docs/flow-control/
title: Handle transient spikes with flow control \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:03.270908+00:00
---

# Handle transient spikes with flow control  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/flow-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Handle transient spikes with flow control Stay organized with collections  Save and categorize content based on your preferences. 

Data pipelines sometimes get spikes in published traffic. The traffic spikes can overwhelm subscribers unless you're prepared for it. A simple solution to avoiding traffic spikes is to dynamically increase Pub/Sub subscriber resources to process more messages. However, this solution might drive up costs or not work instantaneously. For example, you might require many VMs.

Flow control on the subscriber side lets the subscriber regulate the rate at which messages are ingested. Flow control thus handles traffic spikes without driving up costs or until the subscriber is scaled up.

Flow control is an available feature in the Pub/Sub [high-level client library](https://docs.cloud.google.com/pubsub/docs/pull#high_client_library). You can also implement your own flow control programming when you're using a [low-level client library](https://docs.cloud.google.com/pubsub/docs/pull#low_client_library).

Key point: If you get sudden spikes of traffic for published messages, use flow control in your pull subscriber client to address the transient spikes.

The need for flow control indicates that messages are being published at a higher rate than they are being consumed. If this scenario is a persistent state, rather than a transient spike in message volume, consider increasing the number of subscriber client instances.

## Flow control configuration

Flow control lets you configure the maximum number of bytes allocated for outstanding requests, and the maximum number of outstanding messages permitted. Set these limits according to the throughput capacity of your client machines.

The default values for the flow control variables and the names of the variables might differ across client libraries. For example, in the Java client library, the following variables configure flow control:

  * **setMaxOutstandingElementCount().** Defines the maximum number of messages for which Pub/Sub has not received acknowledgments or negative acknowledgments.

  * **setMaxOutstandingRequestBytes().** Defines the maximum size of messages for which Pub/Sub has not received acknowledgments or negative acknowledgments.




If the limit for `setMaxOutstandingElementCount()` or `setMaxOutstandingRequestBytes()` is crossed, the subscriber client does not pull more messages. This behavior continues until the messages that are already pulled get acknowledged or negatively acknowledged. We can thus align throughput with the cost associated with running more subscribers.

## Code samples for flow control

To control the rate at which the subscriber client receives messages, use the flow control features of the subscriber. These flow control features are illustrated in the following samples:

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::Options;
    using ::google::cloud::StatusOr;
    auto sample = [](std::string project_id, std::string subscription_id) {
      // Change the flow control watermarks, by default the client library uses
      // 0 and 1,000 for the message count watermarks, and 0 and 10MiB for the
      // size watermarks. Recall that the library stops requesting messages if
      // any of the high watermarks are reached, and the library resumes
      // requesting messages when *both* low watermarks are reached.
      auto constexpr kMiB = 1024 * 1024L;
      auto subscriber = pubsub::Subscriber(pubsub::MakeSubscriberConnection(
          pubsub::Subscription(std::move(project_id), std::move(subscription_id)),
          Options{}
              .set<pubsub::MaxOutstandingMessagesOption>(1000)
              .set<pubsub::MaxOutstandingBytesOption>(8 * kMiB)));
    
      auto session = subscriber.Subscribe(
          [](pubsub::Message const& m, pubsub::AckHandler h) {
            std::move(h).ack();
            std::cout << "Received message " << m << "\n";
            PleaseIgnoreThisSimplifiesTestingTheSamples();
          });
      return std::make_pair(subscriber, std::move(session));
    };

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class PullMessagesWithFlowControlAsyncSample
    {
        public async Task<int> PullMessagesWithFlowControlAsync(string projectId, string subscriptionId, bool acknowledge)
        {
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
            int messageCount = 0;
            [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html) subscriber = await new [SubscriberClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClientBuilder.html)
            {
                SubscriptionName = subscriptionName,
                Settings = new SubscriberClient.Settings
                {
                    AckExtensionWindow = TimeSpan.FromSeconds(4),
                    AckDeadline = TimeSpan.FromSeconds(10),
                    FlowControlSettings = new [FlowControlSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.FlowControlSettings.html)(maxOutstandingElementCount: 100, maxOutstandingByteCount: 10240)
                }
            }.BuildAsync();
            // SubscriberClient runs your message handle function on multiple
            // threads to maximize throughput.
            Task startTask = subscriber.[StartAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StartAsync_Google_Cloud_PubSub_V1_SubscriptionHandler_)(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, [CancellationToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html#Google_Api_Gax_Grpc_CallSettings_CancellationToken) cancel) =>
            {
                string text = message.Data.ToStringUtf8();
                Console.WriteLine($"Message {message.MessageId}: {text}");
                Interlocked.Increment(ref messageCount);
                return Task.FromResult(acknowledge ? [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack) : [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Nack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Nack));
            });
            // Run for 5 seconds.
            await Task.Delay(5000);
            await subscriber.[StopAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StopAsync_Google_Cloud_PubSub_V1_SubscriberClient_ShutdownOptions_System_Threading_CancellationToken_)([CancellationToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html#Google_Api_Gax_Grpc_CallSettings_CancellationToken).None);
            // Lets make sure that the start task finished successfully after the call to stop.
            await startTask;
            return messageCount;
        }
    }

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    )
    
    func pullMsgsFlowControlSettings(w io.Writer, projectID, subID string) error {
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
    	// MaxOutstandingMessages is the maximum number of unprocessed messages the
    	// subscriber client will pull from the server before pausing. This also configures
    	// the maximum number of concurrent handlers for received messages.
    	//
    	// For more information, see https://cloud.google.com/pubsub/docs/pull#streamingpull_dealing_with_large_backlogs_of_small_messages.
    	sub.ReceiveSettings.MaxOutstandingMessages = 100
    	// MaxOutstandingBytes is the maximum size of unprocessed messages,
    	// that the subscriber client will pull from the server before pausing.
    	sub.ReceiveSettings.MaxOutstandingBytes = 1e8
    	err = sub.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		fmt.Fprintf(w, "Got message: %q\n", string(msg.Data))
    		msg.Ack()
    	})
    	if err != nil {
    		return fmt.Errorf("sub.Receive: %w", err)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.gax.batching.[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowControlSettings.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SubscribeWithFlowControlSettingsExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
    
        subscribeWithFlowControlSettingsExample(projectId, subscriptionId);
      }
    
      public static void subscribeWithFlowControlSettingsExample(
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
    
        // The subscriber will pause the message stream and stop receiving more messsages from the
        // server if any one of the conditions is met.
        [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowControlSettings.html) flowControlSettings =
            [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowControlSettings.html).newBuilder()
                // 1,000 outstanding messages. Must be >0. It controls the maximum number of messages
                // the subscriber receives before pausing the message stream.
                .setMaxOutstandingElementCount(1000L)
                // 100 MiB. Must be >0. It controls the maximum size of messages the subscriber
                // receives before pausing the message stream.
                .setMaxOutstandingRequestBytes(100L * 1024L * 1024L)
                .build();
    
        try {
          subscriber =
              [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver)
                  .setFlowControlSettings(flowControlSettings)
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const maxInProgress = 5;
    // const timeout = 10;
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function subscribeWithFlowControlSettings(
      subscriptionNameOrId,
      maxInProgress,
      timeout,
    ) {
      const subscriberOptions = {
        flowControl: {
          maxMessages: maxInProgress,
        },
      };
    
      // References an existing subscription.
      // Note that flow control settings are not persistent across subscribers.
      const subscription = pubSubClient.subscription(
        subscriptionNameOrId,
        subscriberOptions,
      );
    
      console.log(
        `Subscriber to subscription ${subscription.name} is ready to receive messages at a controlled volume of ${maxInProgress} messages.`,
      );
    
      const messageHandler = message => {
        console.log(`Received message: ${message.id}`);
        console.log(`\tData: ${message.data}`);
        console.log(`\tAttributes: ${message.attributes}`);
    
        // "Ack" (acknowledge receipt of) the message
        message.[ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)();
      };
    
      subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
    
      // Wait a while for the subscription to run. (Part of the sample only.)
      setTimeout(async () => {
        await subscription.close();
      }, timeout * 1000);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const maxInProgress = 5;
    // const timeout = 10;
    
    // Imports the Google Cloud client library
    import {Message, PubSub, SubscriberOptions} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function subscribeWithFlowControlSettings(
      subscriptionNameOrId: string,
      maxInProgress: number,
      timeout: number,
    ) {
      const subscriberOptions: SubscriberOptions = {
        flowControl: {
          maxMessages: maxInProgress,
        },
      };
    
      // References an existing subscription.
      // Note that flow control settings are not persistent across subscribers.
      const subscription = pubSubClient.subscription(
        subscriptionNameOrId,
        subscriberOptions,
      );
    
      console.log(
        `Subscriber to subscription ${subscription.name} is ready to receive messages at a controlled volume of ${maxInProgress} messages.`,
      );
    
      const messageHandler = (message: Message) => {
        console.log(`Received message: ${message.id}`);
        console.log(`\tData: ${message.data}`);
        console.log(`\tAttributes: ${message.attributes}`);
    
        // "Ack" (acknowledge receipt of) the message
        message.ack();
      };
    
      subscription.on('message', messageHandler);
    
      // Wait a while for the subscription to run. (Part of the sample only.)
      setTimeout(async () => {
        await subscription.close();
      }, timeout * 1000);
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from concurrent.futures import TimeoutError
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    # Number of seconds the subscriber should listen for messages
    # timeout = 5.0
    
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    def callback(message: pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
        print(f"Received {message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)!r}.")
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    # Limit the subscriber to only have ten outstanding messages at a time.
    flow_control = pubsub_v1.types.[FlowControl](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.FlowControl.html)(max_messages=10)
    
    streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(
        subscription_path, callback=callback, flow_control=flow_control
    )
    print(f"Listening for messages on {subscription_path}..\n")
    
    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription_id
    
    listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) inventory: 10 do |received_message|
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
    use std::time::Duration;
    
    pub async fn sample(project_id: &str, subscription_id: &str) -> anyhow::Result<()> {
        let subscription_name = format!("projects/{project_id}/subscriptions/{subscription_id}");
        let client = Subscriber::builder().build().await?;
        let mut stream = client
            .subscribe(subscription_name)
            // The server pauses message delivery to the application when either
            // this many messages, or this many bytes are outstanding. A message is
            // outstanding until it has been acked or nacked.
            .set_max_outstanding_messages(1000)
            .set_max_outstanding_bytes(10 * 1024 * 1024) // 10 MB
            .build();
    
        // Terminate the example after 10 seconds.
        let shutdown_token = stream.shutdown_token();
        let shutdown = tokio::spawn(async move {
            tokio::time::sleep(Duration::from_secs(10)).await;
            shutdown_token.shutdown().await;
        });
    
        println!("listening for messages...");
    
        while let Some((message, handler)) = stream.next().await.transpose()? {
            println!("received message: {message:?}");
            handler.ack();
        }
        shutdown.await?;
    
        println!("done listening for messages");
        Ok(())
    }

## What's next

Read about the other delivery options you can configure for a subscription:

  * [Handle message failures with subscription retry policy](https://docs.cloud.google.com/pubsub/docs/handling-failures#subscription_retry_policy)

  * [Forward undelivered messages to a dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic)

  * [Replay previously-acked messages or purge messages](https://docs.cloud.google.com/pubsub/docs/replay-overview)

  * [Extend ack time with lease management](https://docs.cloud.google.com/pubsub/docs/lease-management)

  * [Receive messages in order](https://docs.cloud.google.com/pubsub/docs/ordering)

  * [Filter messages by their attributes](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter)

  * [Receive and acknowledge messages exactly-once](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)

  * [Process more messages with concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
