---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-sync-pull-with-lease/
title: Subscribe with synchronous pull and lease management \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:09.651809+00:00
---

# Subscribe with synchronous pull and lease management  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-sync-pull-with-lease/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Subscribe with synchronous pull and lease management Stay organized with collections  Save and categorize content based on your preferences. 

Uses synchronous pull to receive messages and modify their acknowledge deadlines.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Extend ack time with lease management](https://docs.cloud.google.com/pubsub/docs/lease-management)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    using System.Collections.Generic;
    
    public class PullMessageWithLeaseManagementSample
    {
        public int PullMessageWithLeaseManagement(string projectId, string subscriptionId, bool acknowledge)
        {
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriberClient = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
    
            var ackIds = new List<string>();
            try
            {
                [PullResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PullResponse.html) response = subscriberClient.[Pull](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Pull_Google_Cloud_PubSub_V1_PullRequest_Google_Api_Gax_Grpc_CallSettings_)(subscriptionName, maxMessages: 20);
    
                // Print out each received message.
                foreach ([ReceivedMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.ReceivedMessage.html) msg in response.[ReceivedMessages](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PullResponse.html#Google_Cloud_PubSub_V1_PullResponse_ReceivedMessages))
                {
                    ackIds.[Add](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html#Grpc_Core_Metadata_Add_Grpc_Core_Metadata_Entry_)(msg.[AckId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.ReceivedMessage.html#Google_Cloud_PubSub_V1_ReceivedMessage_AckId));
                    string text = msg.Message.[Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html#Google_Cloud_PubSub_V1_PubsubMessage_Data).ToStringUtf8();
                    Console.WriteLine($"Message {msg.Message.MessageId}: {text}");
    
                    // Modify the ack deadline of each received message from the default 10 seconds to 30.
                    // This prevents the server from redelivering the message after the default 10 seconds
                    // have passed.
                    subscriberClient.[ModifyAckDeadline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_ModifyAckDeadline_Google_Cloud_PubSub_V1_ModifyAckDeadlineRequest_Google_Api_Gax_Grpc_CallSettings_)(subscriptionName, new List<string> { msg.[AckId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.ReceivedMessage.html#Google_Cloud_PubSub_V1_ReceivedMessage_AckId) }, 30);
                }
                // If acknowledgement required, send to server.
                if (acknowledge && ackIds.Count > 0)
                {
                    subscriberClient.[Acknowledge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Acknowledge_Google_Cloud_PubSub_V1_AcknowledgeRequest_Google_Api_Gax_Grpc_CallSettings_)(subscriptionName, ackIds);
                }
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) ex) when (ex.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html).[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[Unavailable](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable))
            {
                // UNAVAILABLE due to too many concurrent pull requests pending for the given subscription.
            }
            return ackIds.[Count](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html#Grpc_Core_Metadata_Count);
        }
    }

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.stub.GrpcSubscriberStub;
    import com.google.cloud.pubsub.v1.stub.[SubscriberStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriberGrpc.SubscriberStub.html);
    import com.google.cloud.pubsub.v1.stub.SubscriberStubSettings;
    import com.google.pubsub.v1.[AcknowledgeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.AcknowledgeRequest.html);
    import com.google.pubsub.v1.[ModifyAckDeadlineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ModifyAckDeadlineRequest.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PullRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullRequest.html);
    import com.google.pubsub.v1.[PullResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullResponse.html);
    import com.google.pubsub.v1.[ReceivedMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ReceivedMessage.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class SubscribeSyncWithLeaseExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
        Integer numOfMessages = 10;
    
        subscribeSyncWithLeaseExample(projectId, subscriptionId, numOfMessages);
      }
    
      public static void subscribeSyncWithLeaseExample(
          String projectId, String subscriptionId, Integer numOfMessages)
          throws IOException, InterruptedException {
        SubscriberStubSettings subscriberStubSettings =
            SubscriberStubSettings.newBuilder()
                .setTransportChannelProvider(
                    SubscriberStubSettings.defaultGrpcTransportProviderBuilder()
                        .setMaxInboundMessageSize(20 << 20) // 20 MB
                        .build())
                .build();
    
        try ([SubscriberStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriberGrpc.SubscriberStub.html) subscriber = GrpcSubscriberStub.create(subscriberStubSettings)) {
    
          String subscriptionName = [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).format(projectId, subscriptionId);
    
          [PullRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullRequest.html) pullRequest =
              [PullRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullRequest.html).newBuilder()
                  .setMaxMessages(numOfMessages)
                  .setSubscription(subscriptionName)
                  .build();
    
          // Use pullCallable().futureCall to asynchronously perform this operation.
          [PullResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullResponse.html) pullResponse = subscriber.pullCallable().call(pullRequest);
    
          // Stop the program if the pull response is empty to avoid acknowledging
          // an empty list of ack IDs.
          if (pullResponse.[getReceivedMessagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullResponse.html#com_google_pubsub_v1_PullResponse_getReceivedMessagesList__)().isEmpty()) {
            System.out.println("No message was pulled. Exiting.");
            return;
          }
    
          List<String> ackIds = new ArrayList<>();
          for ([ReceivedMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ReceivedMessage.html) message : pullResponse.[getReceivedMessagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullResponse.html#com_google_pubsub_v1_PullResponse_getReceivedMessagesList__)()) {
            ackIds.add(message.getAckId());
    
            // Modify the ack deadline of each received message from the default 10 seconds to 30.
            // This prevents the server from redelivering the message after the default 10 seconds
            // have passed.
            [ModifyAckDeadlineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ModifyAckDeadlineRequest.html) modifyAckDeadlineRequest =
                [ModifyAckDeadlineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ModifyAckDeadlineRequest.html).newBuilder()
                    .setSubscription(subscriptionName)
                    .addAckIds(message.getAckId())
                    .setAckDeadlineSeconds(30)
                    .build();
    
            subscriber.modifyAckDeadlineCallable().call(modifyAckDeadlineRequest);
          }
    
          // Acknowledge received messages.
          [AcknowledgeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.AcknowledgeRequest.html) acknowledgeRequest =
              [AcknowledgeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.AcknowledgeRequest.html).newBuilder()
                  .setSubscription(subscriptionName)
                  .addAllAckIds(ackIds)
                  .build();
    
          // Use acknowledgeCallable().futureCall to asynchronously perform this operation.
          subscriber.acknowledgeCallable().call(acknowledgeRequest);
          System.out.println(pullResponse.[getReceivedMessagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PullResponse.html#com_google_pubsub_v1_PullResponse_getReceivedMessagesList__)());
        }
      }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription_id
    new_ack_deadline = 30
    processed = false
    
    # The subscriber pulls a specified number of messages.
    received_messages = subscriber.pull immediate: false, max: 1
    # Obtain the first message.
    message = received_messages.first
    
    # Send the message to a non-blocking worker that starts a long-running
    # process, such as writing the message to a table, which may take longer than
    # the default 10-second acknowledge deadline.
    Thread.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) do
      sleep 15
      processed = true
      puts "Finished processing \"#{message.data}\"."
    end
    
    loop do
      sleep 1
      if processed
        # If the message has been processed, acknowledge the message.
        message.[acknowledge!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
        puts "Done."
        # Exit after the message is acknowledged.
        break
      else
        # If the message has not yet been processed, reset its ack deadline.
        message.[modify_ack_deadline!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html) new_ack_deadline
        puts "Reset ack deadline for \"#{message.data}\" for " \
             "#{new_ack_deadline} seconds."
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
