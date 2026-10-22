---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-exactly-once/
title: Subscribe with exactly once delivery \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:59.303263+00:00
---

# Subscribe with exactly once delivery  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-exactly-once/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Subscribe with exactly once delivery Stay organized with collections  Save and categorize content based on your preferences. 

Receive messages from a subscription with exactly once delivery enabled.

## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    auto sample = [](pubsub::Subscriber subscriber) {
      return subscriber.Subscribe(
          [&](pubsub::Message const& m, pubsub::ExactlyOnceAckHandler h) {
            std::cout << "Received message " << m << "\n";
            std::move(h).ack().then([id = m.message_id()](auto f) {
              auto status = f.get();
              std::cout << "Message id " << id
                        << " ack() completed with status=" << status << "\n";
            });
            PleaseIgnoreThisSimplifiesTestingTheSamples();
          });
    };

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Collections.Concurrent;
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    using static Google.Cloud.PubSub.V1.SubscriberClient;
    
    public class ExactlyOnceDeliverySubscriberAsyncSample
    {
        public async Task<IEnumerable<string>> ExactlyOnceDeliverySubscriberAsync(string projectId, string subscriptionId)
        {
            // subscriptionId should be the ID of an exactly-once delivery subscription.
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
            [SubscriberClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClientBuilder.html) builder = new [SubscriberClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClientBuilder.html)()
            {
                SubscriptionName = subscriptionName,
                Endpoint = "us-west1-pubsub.googleapis.com:443"
            };
            [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html) subscriber = await builder.[BuildAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClientBuilder.html#Google_Cloud_PubSub_V1_SubscriberClientBuilder_BuildAsync_System_Threading_CancellationToken_)();
            // To get the status of ACKnowledge (ACK) or Not ACKnowledge (NACK) request in exactly once delivery subscriptions,
            // create a subscription handler that inherits from Google.Cloud.PubSub.V1.SubscriptionHandler. 
            // For more information see Google.Cloud.PubSub.V1.SubscriptionHandler reference docs here:
            // https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionHandler
            var subscriptionHandler = new SampleSubscriptionHandler();
            Task subscriptionTask = subscriber.[StartAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StartAsync_Google_Cloud_PubSub_V1_SubscriptionHandler_)(subscriptionHandler);
            // The subscriber will be running until it is stopped.
            await Task.Delay(5000);
            await subscriber.[StopAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StopAsync_Google_Cloud_PubSub_V1_SubscriberClient_ShutdownOptions_System_Threading_CancellationToken_)(CancellationToken.None);
            // Let's make sure that the start task finished successfully after the call to stop.
            await subscriptionTask;
            return subscriptionHandler.SuccessfulAckedIds;
        }
    
        // Sample handler to handle messages and ACK/NACK responses.
        public class SampleSubscriptionHandler : SubscriptionHandler
        {
            public ConcurrentBag<string> SuccessfulAckedIds { get; } = new ConcurrentBag<string>();
    
            /// <summary>
            /// The function that processes received messages. It should be thread-safe.
            /// Return <see cref="Reply.Ack"/> to ACKnowledge the message (meaning it won't be received again).
            /// Return <see cref="Reply.Nack"/> to Not ACKnowledge the message (meaning it will be received again).
            /// From the point of view of message acknowledgement, throwing an exception is equivalent to returning <see cref="Reply.Nack"/>.
            /// </summary>
            public override async Task<Reply> HandleMessage([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, CancellationToken cancellationToken)
            {
                string text = message.[Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html#Google_Cloud_PubSub_V1_PubsubMessage_Data).ToStringUtf8();
                Console.WriteLine($"Message {message.[MessageId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html#Google_Cloud_PubSub_V1_PubsubMessage_MessageId)}: {text}");
                return await Task.FromResult([Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack));
            }
    
            /// <summary>
            /// This method will receive responses for all acknowledge requests.
            /// </summary>
            public override void HandleAckResponses(IReadOnlyList<AckNackResponse> responses)
            {
                foreach (var response in responses)
                {
                    if (response.Status == [AcknowledgementStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.AcknowledgementStatus.html).[Success](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.AcknowledgementStatus.html#Google_Cloud_PubSub_V1_AcknowledgementStatus_Success))
                    {
                        SuccessfulAckedIds.Add(response.MessageId);
                    }
    
                    string result = response.Status switch
                    {
                        AcknowledgementStatus.Success => $"MessageId {response.MessageId} successfully acknowledged.",
                        AcknowledgementStatus.PermissionDenied => $"MessageId {response.MessageId} failed to acknowledge due to a permission denied error.",
                        AcknowledgementStatus.FailedPrecondition => $"MessageId {response.MessageId} failed to acknowledge due to a failed precondition.",
                        AcknowledgementStatus.InvalidAckId => $"MessageId {response.MessageId} failed to acknowledge due an invalid or expired AckId.",
                        AcknowledgementStatus.Other => $"MessageId {response.MessageId} failed to acknowledge due to an unknown reason.",
                        _ => $"Unknown acknowledgement status for messageId {response.MessageId}."
                    };
    
                    Console.WriteLine(result);
                }
            }
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	"google.golang.org/api/option"
    )
    
    // receiveMessagesWithExactlyOnceDeliveryEnabled instantiates a subscriber client.
    // This differs from regular subscribing since you must call msg.AckWithResult()
    // or msg.NackWithResult() instead of the regular Ack/Nack methods.
    // When exactly once delivery is enabled on the subscription, the message is
    // guaranteed to not be delivered again if the ack result succeeds.
    func receiveMessagesWithExactlyOnceDeliveryEnabled(w io.Writer, projectID, subID string) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    
    	// Pub/Sub's exactly once delivery guarantee only applies when subscribers connect to the service in the same region.
    	// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
    	client, err := pubsub.NewClient(ctx, projectID, option.WithEndpoint("us-west1-pubsub.googleapis.com:443"))
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// client.Subscriber can be passed a subscription ID (e.g. "my-sub") or
    	// a fully qualified name (e.g. "projects/my-project/subscriptions/my-sub").
    	// If a subscription ID is provided, the project ID from the client is used.
    	sub := client.Subscriber(subID)
    	// Set MinDurationPerAckExtension high to avoid any unintentional
    	// acknowledgment expirations (e.g. due to network events).
    	// This can lead to high tail latency in case of client crashes.
    	sub.ReceiveSettings.MinDurationPerAckExtension = 600 * time.Second
    
    	// Receive messages for 10 seconds, which simplifies testing.
    	// Comment this out in production, since `Receive` should
    	// be used as a long running operation.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    	err = sub.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		fmt.Fprintf(w, "Got message: %q\n", string(msg.Data))
    		r := msg.AckWithResult()
    		// Block until the result is returned and a pubsub.AcknowledgeStatus
    		// is returned for the acked message.
    		status, err := r.Get(ctx)
    		if err != nil {
    			fmt.Fprintf(w, "MessageID: %s failed when calling result.Get: %v", msg.ID, err)
    		}
    
    		switch status {
    		case pubsub.AcknowledgeStatusSuccess:
    			fmt.Fprintf(w, "Message successfully acked: %s", msg.ID)
    		case pubsub.AcknowledgeStatusInvalidAckID:
    			fmt.Fprintf(w, "Message failed to ack with response of Invalid. ID: %s", msg.ID)
    		case pubsub.AcknowledgeStatusPermissionDenied:
    			fmt.Fprintf(w, "Message failed to ack with response of Permission Denied. ID: %s", msg.ID)
    		case pubsub.AcknowledgeStatusFailedPrecondition:
    			fmt.Fprintf(w, "Message failed to ack with response of Failed Precondition. ID: %s", msg.ID)
    		case pubsub.AcknowledgeStatusOther:
    			fmt.Fprintf(w, "Message failed to ack with response of Other. ID: %s", msg.ID)
    		default:
    		}
    	})
    	if err != nil {
    		return fmt.Errorf("got err from sub.Receive: %w", err)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[AckReplyConsumerWithResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumerWithResponse.html);
    import com.google.cloud.pubsub.v1.[AckResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckResponse.html);
    import com.google.cloud.pubsub.v1.[MessageReceiverWithAckResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiverWithAckResponse.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.Future;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SubscribeWithExactlyOnceConsumerWithResponseExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
    
        subscribeWithExactlyOnceConsumerWithResponseExample(projectId, subscriptionId);
      }
    
      public static void subscribeWithExactlyOnceConsumerWithResponseExample(
          String projectId, String subscriptionId) {
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        // Instantiate an asynchronous message receiver using `AckReplyConsumerWithResponse`
        // instead of `AckReplyConsumer` to get a future that tracks the result of the ack call.
        // When exactly once delivery is enabled on the subscription, the message is guaranteed
        // to not be delivered again if the ack future succeeds.
        [MessageReceiverWithAckResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiverWithAckResponse.html) receiverWithResponse =
            (PubsubMessage message, AckReplyConsumerWithResponse consumerWithResponse) -> {
              try {
                // Handle incoming message, then ack the message, and receive an ack response.
                System.out.println("Message received: " + message.getData().toStringUtf8());
                Future<AckResponse> ackResponseFuture = consumerWithResponse.ack();
    
                // Retrieve the completed future for the ack response from the server.
                AckResponse ackResponse = ackResponseFuture.get();
    
                switch (ackResponse) {
                  case SUCCESSFUL:
                    // Success code means that this MessageID will not be delivered again.
                    System.out.println("Message successfully acked: " + message.getMessageId());
                    break;
                  case INVALID:
                    System.out.println(
                        "Message failed to ack with a response of Invalid. Id: "
                            + message.getMessageId());
                    break;
                  case PERMISSION_DENIED:
                    System.out.println(
                        "Message failed to ack with a response of Permission Denied. Id: "
                            + message.getMessageId());
                    break;
                  case FAILED_PRECONDITION:
                    System.out.println(
                        "Message failed to ack with a response of Failed Precondition. Id: "
                            + message.getMessageId());
                    break;
                  case OTHER:
                    System.out.println(
                        "Message failed to ack with a response of Other. Id: "
                            + message.getMessageId());
                    break;
                  default:
                    break;
                }
              } catch (InterruptedException | ExecutionException e) {
                System.out.println(
                    "MessageId: " + message.getMessageId() + " failed when retrieving future");
              } catch (Throwable t) {
                System.out.println("Throwable caught" + t.getMessage());
              }
            };
    
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = null;
        try {
          // Pub/Sub's exactly once delivery guarantee only applies when subscribers connect to the
          // service in the same region.
          // For list of locational endpoints for Pub/Sub, see
          // https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
          subscriber =
              [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiverWithResponse)
                  .setEndpoint("us-west1-pubsub.googleapis.com:443")
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

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Subscribe and pull messages from a subscription
     * with `Exactly Once Delivery` enabled.
     *
     * @param string $projectId
     * @param string $subscriptionId
     */
    function subscribe_exactly_once_delivery(
        string $projectId,
        string $subscriptionId
    ): void {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
            // use the apiEndpoint option to set a regional endpoint
            'apiEndpoint' => 'us-west1-pubsub.googleapis.com:443'
        ]);
    
        $subscription = $pubsub->subscription($subscriptionId);
        $messages = $subscription->pull();
    
        foreach ($messages as $message) {
            // When exactly once delivery is enabled on the subscription,
            // the message is guaranteed to not be delivered again if the ack succeeds.
            // Passing the `returnFailures` flag retries any temporary failures received
            // while acking the msg and also returns any permanently failed msgs.
            // Passing this flag on a subscription with exactly once delivery disabled
            // will always return an empty array.
            $failedMsgs = $subscription->acknowledge($message, ['returnFailures' => true]);
    
            if (empty($failedMsgs)) {
                printf('Acknowledged message: %s' . PHP_EOL, $message->data());
            } else {
                // Either log or store the $failedMsgs to be retried later
            }
        }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new \
      project_id: project_id,
      endpoint: "us-west1-pubsub.googleapis.com:443"
    subscriber = pubsub.subscriber subscription_id
    
    listener = subscriber.listen do |received_message|
      puts "Received message: #{received_message.data}"
      # Pass in callback to access the acknowledge result.
      # For subscription with Exactly once delivery disabled the result will be
      # success always.
      received_message.acknowledge! do |result|
        puts "Acknowledge result's status: #{result.status}"
      end
    end
    
    listener.start
    # Let the main thread sleep for 60 seconds so the thread for listening
    # messages does not quit
    sleep 60
    listener.stop.wait!

### Rust
    
    
    use google_cloud_pubsub::client::Subscriber;
    use google_cloud_pubsub::subscriber::handler::Handler;
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
    
        let mut tasks = Vec::new();
        println!("Listening for messages...");
        while let Some((m, Handler::ExactlyOnce(h))) = stream.next().await.transpose()? {
            println!("Received message: {m:?}");
            tasks.push(tokio::spawn(async move {
                // We spawn a background task so that receiving the next message
                // is not blocked on the server confirming the ack for this
                // message.
                //
                // You might choose to use a work queue in your application.
                match h.confirmed_ack().await {
                    Ok(()) => println!(
                        "Confirmed ack for message={m:?}. The message will not be redelivered."
                    ),
                    Err(e) => println!("Failed to confirm ack for message={m:?} with error={e:?}"),
                }
            }));
        }
        shutdown.await?;
        println!("Done listening for messages");
    
        for t in tasks {
            t.await?;
        }
        println!("Done acking messages");
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
