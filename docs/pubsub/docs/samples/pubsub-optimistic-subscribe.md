---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-optimistic-subscribe/
title: Optimistically subscribe without creating a subscription first \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:19.720132+00:00
---

# Optimistically subscribe without creating a subscription first  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-optimistic-subscribe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Optimistically subscribe without creating a subscription first Stay organized with collections  Save and categorize content based on your preferences. 

Minimizes administrative operations by first trying to subscribe and then creating a subscription if getting a NotFound error. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [General troubleshooting](https://docs.cloud.google.com/pubsub/docs/troubleshooting)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    auto process_response = [](gc::StatusOr<pubsub::PullResponse> response) {
      if (response) {
        std::cout << "Received message " << response->message << "\n";
        std::move(response->handler).ack();
        return gc::Status();
      }
      if (response.status().code() == gc::StatusCode::kUnavailable &&
          response.status().message() == "no messages returned") {
        std::cout << "No messages returned from Pull()\n";
        return gc::Status();
      }
      return response.status();
    };
    
    // Instead of checking if the subscription exists, optimistically try to
    // consume from the subscription.
    auto status = process_response(subscriber.Pull());
    if (status.ok()) return;
    if (status.code() != gc::StatusCode::kNotFound) throw std::move(status);
    
    // Since the subscription does not exist, create the subscription.
    pubsub_admin::SubscriptionAdminClient subscription_admin_client(
        pubsub_admin::MakeSubscriptionAdminConnection());
    google::pubsub::v1::Subscription request;
    request.set_name(
        pubsub::Subscription(project_id, subscription_id).FullName());
    request.set_topic(
        pubsub::Topic(project_id, std::move(topic_id)).FullName());
    auto sub = subscription_admin_client.CreateSubscription(request);
    if (!sub) throw std::move(sub).status();
    
    // Consume from the new subscription.
    status = process_response(subscriber.Pull());
    if (!status.ok()) throw std::move(status);

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class OptimisticSubscribeSample
    {
        public async Task<int> OptimisticSubscribe(string projectId, string topicId, string subscriptionId)
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
            // Catch exception when subscription is not found
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e) when (e.Status.StatusCode == StatusCode.NotFound)
            {
                Console.WriteLine($"Message: {e.Message}");
                Console.WriteLine($"StackTrace: {e.StackTrace}");
    
                [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriberServiceApiClient = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
                [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
                [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html) subscription = subscriberServiceApiClient.[CreateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_CreateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Api_Gax_Grpc_CallSettings_)(subscriptionName, topicName, pushConfig: null, ackDeadlineSeconds: 60);
                // Recursively call OptimisticSubscribe to restart the subscriber
                return await OptimisticSubscribe(projectId, topicId, subscriptionId);
            }
            return messageCount;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    )
    
    // optimisticSubscribe shows the recommended pattern for optimistically
    // assuming a subscription exists prior to receiving messages.
    func optimisticSubscribe(w io.Writer, projectID, topic, subscriptionName string) error {
    	// projectID := "my-project-id"
    	// topic := "projects/my-project-id/topics/my-topic"
    	// subscription := "projects/my-project/subscriptions/my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// client.Subscriber can be passed a subscription ID (e.g. "my-sub") or
    	// a fully qualified name (e.g. "projects/my-project/subscriptions/my-sub").
    	// If a subscription ID is provided, the project ID from the client is used.
    	sub := client.Subscriber(subscriptionName)
    
    	// Receive messages for 10 seconds, which simplifies testing.
    	// Comment this out in production, since `Receive` should
    	// be used as a long running operation.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	// Instead of checking if the subscription exists, optimistically try to
    	// receive from the subscription assuming it exists.
    	err = sub.Receive(ctx, func(_ context.Context, msg *pubsub.Message) {
    		fmt.Fprintf(w, "Got from existing subscription: %q\n", string(msg.Data))
    		msg.Ack()
    	})
    	if err != nil {
    		if st, ok := status.FromError(err); ok {
    			if st.Code() == codes.NotFound {
    				// If the subscription does not exist, then create the subscription.
    				subscription, err := client.SubscriptionAdminClient.CreateSubscription(ctx, &pubsubpb.Subscription{
    					Name:  subscriptionName,
    					Topic: topic,
    				})
    				if err != nil {
    					return err
    				}
    				fmt.Fprintf(w, "Created subscription: %q\n", subscriptionName)
    
    				// client.Subscriber can be passed a subscription ID (e.g. "my-sub") or
    				// a fully qualified name (e.g. "projects/my-project/subscriptions/my-sub").
    				// If a subscription ID is provided, the project ID from the client is used.
    				sub = client.Subscriber(subscription.GetName())
    				err = sub.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    					fmt.Fprintf(w, "Got from new subscription: %q\n", string(msg.Data))
    					msg.Ack()
    				})
    				if err != nil && !errors.Is(err, context.Canceled) {
    					return err
    				}
    			}
    		}
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.common.util.concurrent.MoreExecutors;
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class OptimisticSubscribeExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
        String topicId = "your-topic-id";
    
        optimisticSubscribeExample(projectId, subscriptionId, topicId);
      }
    
      public static void optimisticSubscribeExample(
          String projectId, String subscriptionId, String topicId) throws IOException {
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
          subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver).build();
    
          // Listen for resource NOT_FOUND errors and rebuild the  subscriber and restart subscribing
          // when the current subscriber encounters these errors.
          subscriber.addListener(
              new [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).Listener() {
                public void failed([Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).State from, Throwable failure) {
                  System.out.println(failure.getStackTrace());
                  if (failure instanceof [NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html)) {
                    try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient =
                        [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
                      [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
                      // Create a pull subscription with default acknowledgement deadline of 10 seconds.
                      // The client library will automatically extend acknowledgement deadlines.
                      [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription =
                          subscriptionAdminClient.createSubscription(
                              subscriptionName, topicName, [PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html).getDefaultInstance(), 10);
                      System.out.println("Created pull subscription: " + subscription.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html#com_google_pubsub_v1_Subscription_getName__)());
                      optimisticSubscribeExample(projectId, subscriptionId, topicId);
                    } catch (IOException err) {
                      System.out.println("Failed to create pull subscription: " + err.getMessage());
                    }
                  }
                }
              },
              MoreExecutors.directExecutor());
    
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
          System.out.printf("Listening for messages on %s:\n", subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)());
          subscriber.awaitTerminated(30, TimeUnit.SECONDS);
        } catch (IllegalStateException e) {
          // Prevent an exception from being thrown if it is the expected NotFoundException
          if (!(subscriber.failureCause() instanceof [NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html))) {
            throw e;
          }
        } catch (TimeoutException e) {
          subscriber.stopAsync();
        }
      }
    }
    

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Core\Exception\NotFoundException;
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Optimistically subscribes to a topic
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $subscriptionId  The ID of the subscription.
     */
    function optimistic_subscribe(
        string $projectId,
        string $topicName,
        string $subscriptionId
    ): void {
    
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $subscription = $pubsub->subscription($subscriptionId);
    
        try {
            $messages = $subscription->pull();
            foreach ($messages as $message) {
                printf('PubSub Message: %s' . PHP_EOL, $message->data());
                $subscription->acknowledge($message);
            }
        } catch (NotFoundException $e) { // Subscription is not found
            printf('Exception Message: %s' . PHP_EOL, $e->getMessage());
            printf('StackTrace: %s' . PHP_EOL, $e->getTraceAsString());
            // Create subscription and retry the pull. Any messages published before subscription creation would not be received.
            $pubsub->subscribe($subscriptionId, $topicName);
            optimistic_subscribe($projectId, $topicName, $subscriptionId);
        }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    
    # Propagate exception from child threads to the main thread as soon as it is
    # raised. Exceptions happened in the callback thread are collected in the
    # callback thread pool and do not propagate to the main thread
    Thread.abort_on_exception = true
    
    begin
      subscriber = pubsub.subscriber subscription_id
      listener   = subscriber.listen do |received_message|
        puts "Received message: #{received_message.data}"
        received_message.acknowledge!
      end
      listener.start
      # Let the main thread sleep for 60 seconds so the thread for listening
      # messages does not quit
      sleep 60
      listener.stop.wait!
    rescue Google::Cloud::NotFoundError => e
      puts "Subscription #{subscription_id} does not exist."
    
      subscription = pubsub.subscription_admin.create_subscription \
        name: pubsub.subscription_path(subscription_id),
        topic: pubsub.topic_path(topic_id)
    
      puts "Subscription #{subscription_id} created."
    end

### Rust
    
    
    use google_cloud_gax::error::rpc::Code;
    use google_cloud_pubsub::client::{Subscriber, SubscriptionAdmin};
    use std::time::Duration;
    
    pub async fn sample(project_id: &str, topic_id: &str, subscription_id: &str) -> anyhow::Result<()> {
        let subscription_name = format!("projects/{project_id}/subscriptions/{subscription_id}");
        let client = Subscriber::builder().build().await?;
    
        // Instead of checking if the subscription exists, optimistically try to
        // receive messages from it.
        let Err(e) = receive(&client, &subscription_name).await else {
            return Ok(());
        };
        // The stream returns a NOT_FOUND error if the subscription does not exist.
        if e.status().is_none_or(|s| s.code != Code::NotFound) {
            return Err(e.into());
        }
    
        // Since the subscription does not exist, create the subscription.
        let admin = SubscriptionAdmin::builder().build().await?;
        admin
            .create_subscription()
            .set_name(&subscription_name)
            .set_topic(format!("projects/{project_id}/topics/{topic_id}"))
            .send()
            .await?;
        println!("created subscription {subscription_name}");
    
        // Receive messages from the new subscription.
        receive(&client, &subscription_name).await?;
        Ok(())
    }
    
    async fn receive(client: &Subscriber, subscription_name: &str) -> google_cloud_pubsub::Result<()> {
        let mut stream = client.subscribe(subscription_name).build();
    
        // Terminate the example after 10 seconds.
        let shutdown_token = stream.shutdown_token();
        tokio::spawn({
            let shutdown_token = shutdown_token.clone();
            async move {
                tokio::time::sleep(Duration::from_secs(10)).await;
                shutdown_token.shutdown().await;
            }
        });
    
        println!("listening for messages on {subscription_name}...");
        while let Some((message, handler)) = stream.next().await.transpose()? {
            println!("received message: {message:?}");
            handler.ack();
        }
        // Wait for the shutdown to complete, so pending acks are flushed.
        shutdown_token.shutdown().await;
    
        println!("done listening for messages");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
