---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-use-emulator/
title: Use emulator \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:53:06.455432+00:00
---

# Use emulator  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-use-emulator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Use emulator Stay organized with collections  Save and categorize content based on your preferences. 

Configures your code to use the emulator instead of the real Pub/Sub service. Applies to C# and Java. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Testing apps locally with the emulator](https://docs.cloud.google.com/pubsub/docs/emulator)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class EmulatorSupportSample
    {
        public async Task WithEmulatorAsync(string projectId, string topicId, string subscriptionId)
        {
            // Use EmulatorDetection.EmulatorOrProduction to create service clients that will
            // that will connect to the PubSub emulator if the PUBSUB_EMULATOR_HOST environment
            // variable is set, but will otherwise connect to the production environment.
    
            // Create the PublisherServiceApiClient using the PublisherServiceApiClientBuilder
            // and setting the EmulatorDection property.
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisherService = await new [PublisherServiceApiClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClientBuilder.html)
            {
                EmulatorDetection = [EmulatorDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html).[EmulatorOrProduction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html#Google_Api_Gax_EmulatorDetection_EmulatorOrProduction)
            }.BuildAsync();
    
            // Use the client as you'd normally do, to create a topic in this example.
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = new [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html)(projectId, topicId);
            publisherService.[CreateTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_CreateTopic_Google_Cloud_PubSub_V1_Topic_Google_Api_Gax_Grpc_CallSettings_)(topicName);
    
            // Create the SubscriberServiceApiClient using the SubscriberServiceApiClientBuilder
            // and setting the EmulatorDection property.
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriberService = await new [SubscriberServiceApiClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClientBuilder.html)
            {
                EmulatorDetection = [EmulatorDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html).[EmulatorOrProduction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html#Google_Api_Gax_EmulatorDetection_EmulatorOrProduction)
            }.BuildAsync();
    
            // Use the client as you'd normally do, to create a subscription in this example.
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html)(projectId, subscriptionId);
            subscriberService.[CreateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_CreateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Api_Gax_Grpc_CallSettings_)(subscriptionName, topicName, pushConfig: null, ackDeadlineSeconds: 60);
    
            // Create the PublisherClient using PublisherClientBuilder to set the EmulatorDetection property.
            [PublisherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) publisher = await new [PublisherClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClientBuilder.html)
            {
                TopicName = topicName,
                EmulatorDetection = [EmulatorDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html).[EmulatorOrProduction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html#Google_Api_Gax_EmulatorDetection_EmulatorOrProduction)
            }.BuildAsync();
            // Use the client as you'd normally do, to send a message in this example.
            await publisher.[PublishAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_PublishAsync_Google_Cloud_PubSub_V1_PubsubMessage_)("Hello, Pubsub");
            await publisher.[ShutdownAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_ShutdownAsync_System_Threading_CancellationToken_)(TimeSpan.FromSeconds(15));
    
            // Create the SubscriberClient using SubscriberClientBuild to set the EmulatorDetection property.
            [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html) subscriber = await new [SubscriberClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClientBuilder.html)
            {
                SubscriptionName = subscriptionName,
                EmulatorDetection = [EmulatorDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html).[EmulatorOrProduction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.EmulatorDetection.html#Google_Api_Gax_EmulatorDetection_EmulatorOrProduction)
            }.BuildAsync();
            List<PubsubMessage> receivedMessages = new List<PubsubMessage>();
    
            // Use the client as you'd normally do, to listen for messages in this example.
            await subscriber.[StartAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StartAsync_Google_Cloud_PubSub_V1_SubscriptionHandler_)((msg, cancellationToken) =>
            {
                receivedMessages.Add(msg);
                Console.WriteLine($"Received message {msg.MessageId} published at {msg.PublishTime.ToDateTime()}");
                Console.WriteLine($"Text: '{msg.Data.ToStringUtf8()}'");
                // In this example we stop the subscriber when the message is received.
                // You may leave the subscriber running, and it will continue to received published messages
                // if any.
                // This is non-blocking, and the returned Task may be awaited.
                subscriber.[StopAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StopAsync_Google_Cloud_PubSub_V1_SubscriberClient_ShutdownOptions_System_Threading_CancellationToken_)(TimeSpan.FromSeconds(15));
                // Return Reply.Ack to indicate this message has been handled.
                return Task.FromResult([SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack));
            });
        }
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    String hostport = System.getenv("PUBSUB_EMULATOR_HOST");
    ManagedChannel channel = ManagedChannelBuilder.forTarget(hostport).usePlaintext().build();
    try {
      TransportChannelProvider channelProvider =
          FixedTransportChannelProvider.create(GrpcTransportChannel.create(channel));
      CredentialsProvider credentialsProvider = NoCredentialsProvider.create();
    
      // Set the channel and credentials provider when creating a `TopicAdminClient`.
      // Similarly for SubscriptionAdminClient
      TopicAdminClient topicClient =
          TopicAdminClient.create(
              TopicAdminSettings.newBuilder()
                  .setTransportChannelProvider(channelProvider)
                  .setCredentialsProvider(credentialsProvider)
                  .build());
    
      TopicName topicName = TopicName.of("my-project-id", "my-topic-id");
      // Set the channel and credentials provider when creating a `Publisher`.
      // Similarly for Subscriber
      Publisher publisher =
          Publisher.newBuilder(topicName)
              .setChannelProvider(channelProvider)
              .setCredentialsProvider(credentialsProvider)
              .build();
    } finally {
      channel.shutdown();
    }

### Rust
    
    
    use google_cloud_auth::credentials::anonymous::Builder as Anonymous;
    use google_cloud_pubsub::client::{Publisher, TopicAdmin};
    use google_cloud_pubsub::model::Message;
    
    pub async fn sample(project_id: &str, topic_id: &str) -> anyhow::Result<()> {
        let emulator_host = std::env::var("PUBSUB_EMULATOR_HOST")?;
        let endpoint = format!("http://{emulator_host}");
    
        let topic_admin = TopicAdmin::builder()
            .with_endpoint(&endpoint)
            .with_credentials(Anonymous::new().build())
            .build()
            .await?;
        let topic = topic_admin
            .create_topic()
            .set_name(format!("projects/{project_id}/topics/{topic_id}"))
            .send()
            .await?;
        println!("created topic: {}", topic.name);
    
        let publisher = Publisher::builder(topic.name)
            .with_endpoint(&endpoint)
            .with_credentials(Anonymous::new().build())
            .build()
            .await?;
        let message_id = publisher
            .publish(Message::new().set_data("Hello, Emulator!"))
            .await?;
        println!("published message with ID: {message_id}");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
