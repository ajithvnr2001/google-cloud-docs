---
url: https://docs.cloud.google.com/pubsub/docs/lease-management/
title: Extend ack time with lease management \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:52.536300+00:00
---

# Extend ack time with lease management  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/lease-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Extend ack time with lease management Stay organized with collections  Save and categorize content based on your preferences. 

When a message is delivered to a pull subscriber, the subscriber must process and acknowledge (ack) the message within the acknowledgment deadline. Else, the subscriber must extend the deadline with a call to modify the acknowledgment deadline.

The Pub/Sub [high-level client libraries](https://docs.cloud.google.com/pubsub/docs/pull#high_client_library) provide lease management as a feature that automatically extends the deadline of a message that has not yet been acknowledged. By default, the client libraries can extend the deadline to an hour by issuing periodic [modifyAckDeadline](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline) requests. The high-level client libraries for Python, Go, and Java use the 99th percentile of acknowledgment delay to determine the length of each extension.

Lease management lets you have more granular control over the acknowledgment deadline for messages compared to configuring the subscription-level property. If you're only using the subscription-level acknowledgment deadline, you have to balance the tradeoff between a low value and a high value. A low value increases the likelihood of duplicates and a high value delays the redelivery of failed messages. Determining the right value can be difficult, especially when the expected processing time for different messages varies greatly.

For more information about the properties of a subscription, including acknowledgment deadline, see [Subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties).

## Lease management configuration

You can configure the following properties in the [high-level client libraries](https://docs.cloud.google.com/pubsub/docs/pull#high_client_library) to control lease management.

  * **Maximum acknowledgment extension period.** The maximum amount of time for which the client library can extend the acknowledgment deadline of a message by using the `modify acknowledgment deadline` request. This property lets you determine how long you want the subscriber clients to process messages.

  * **Maximum duration for each acknowledgment extension.** The maximum amount of time by which to extend the acknowledgment deadline for each of the `modify acknowledgment deadline` requests. This property lets you define the amount of time Pub/Sub takes to redeliver a message. Redelivery occurs when the first subscriber processing the message crashes or becomes unhealthy and is no longer able to send the `modify acknowledgment deadline` request.

  * **Minimum duration for each acknowledgment extension.** The minimum amount of time by which to extend the acknowledgment deadline for each of the `modify acknowledgment deadline` requests. This property lets you specify the minimum amount of time that must pass before the redelivery of a message occurs.




Acknowledgment deadlines are not guaranteed to be respected unless you enable [exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery).

## Manually managing ack deadlines

We strongly encourage the use of the high-level client libraries. If these don't work, or you need to use unary pull, use the `modify acknowledgment deadline` request to extend their acknowledgment deadlines.

The C++ high-level client library is an exception which provides lease management when using unary pull. See the following samples for unary pull with lease management:

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
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

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    
    // Imports the Google Cloud client library. v1 is for the lower level
    // proto access.
    const {v1} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use.
    const subClient = new v1.[SubscriberClient](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/v1.subscriberclient.html)();
    
    async function synchronousPullWithLeaseManagement() {
      // The low level API client requires a name only.
      const formattedSubscription =
        subscriptionNameOrId.indexOf('/') >= 0
          ? subscriptionNameOrId
          : subClient.subscriptionPath(projectId, subscriptionNameOrId);
    
      // The maximum number of messages returned for this request.
      // Pub/Sub may return fewer than the number specified.
      const maxMessages = 1;
      const newAckDeadlineSeconds = 30;
      const request = {
        subscription: formattedSubscription,
        maxMessages: maxMessages,
        allowExcessMessages: false,
      };
    
      let isProcessed = false;
    
      // The worker function is meant to be non-blocking. It starts a long-
      // running process, such as writing the message to a table, which may
      // take longer than the default 10-sec acknowledge deadline.
      function worker(message) {
        console.log(`Processing "${message.message.data}"...`);
    
        setTimeout(() => {
          console.log(`Finished procesing "${message.message.data}".`);
          isProcessed = true;
        }, 30000);
      }
    
      // The subscriber pulls a specified number of messages.
      const [response] = await subClient.pull(request);
    
      // Obtain the first message.
      const message = response.receivedMessages[0];
    
      // Send the message to the worker function.
      worker(message);
    
      let waiting = true;
      while (waiting) {
        await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)(r => setTimeout(r, 10000));
        // If the message has been processed..
        if (isProcessed) {
          const ackRequest = {
            subscription: formattedSubscription,
            ackIds: [message.ackId],
          };
    
          //..acknowledges the message.
          await subClient.acknowledge(ackRequest);
          console.log(`Acknowledged: "${message.message.data}".`);
          // Exit after the message is acknowledged.
          waiting = false;
          console.log('Done.');
        } else {
          // If the message is not yet processed..
          const modifyAckRequest = {
            subscription: formattedSubscription,
            ackIds: [message.ackId],
            ackDeadlineSeconds: newAckDeadlineSeconds,
          };
    
          //..reset its ack deadline.
          await subClient.modifyAckDeadline(modifyAckRequest);
    
          console.log(
            `Reset ack deadline for "${message.message.data}" for ${newAckDeadlineSeconds}s.`,
          );
        }
      }
    }
    
    synchronousPullWithLeaseManagement().catch(console.error);

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    import logging
    import multiprocessing
    import sys
    import time
    
    from google.api_core import [retry](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html#google_cloud_pubsub_v1_types_PublisherOptions_retry)
    from google.cloud import pubsub_v1
    
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    processes = dict()
    
    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    response = subscriber.[pull](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client.html#google_cloud_pubsub_v1_subscriber_client_Client_pull)(
        request={"subscription": subscription_path, "max_messages": 3},
        retry=[retry](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html#google_cloud_pubsub_v1_types_PublisherOptions_retry).Retry(deadline=300),
    )
    
    if len(response.received_messages) == 0:
        return
    
    # Start a process for each message based on its size modulo 10.
    for message in response.received_messages:
        process = multiprocessing.Process(
            target=time.sleep, args=(sys.getsizeof(message) % 10,)
        )
        processes[process] = (message.[ack_id](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack_id), message.message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
        process.start()
    
    while processes:
        # Take a break every second.
        if processes:
            time.sleep(1)
    
        for process in list(processes):
            ack_id, msg_data = processes[process]
            # If the process is running, reset the ack deadline.
            if process.is_alive():
                subscriber.modify_ack_deadline(
                    request={
                        "subscription": subscription_path,
                        "ack_ids": [ack_id],
                        # Must be between 10 and 600.
                        "ack_deadline_seconds": 15,
                    }
                )
                logger.debug(f"Reset ack deadline for {msg_data}.")
    
            # If the process is complete, acknowledge the message.
            else:
                subscriber.[acknowledge](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client.html#google_cloud_pubsub_v1_subscriber_client_Client_acknowledge)(
                    request={"subscription": subscription_path, "ack_ids": [ack_id]}
                )
                logger.debug(f"Acknowledged {msg_data}.")
                processes.pop(process)
    print(
        f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}."
    )
    
    # Close the underlying gPRC channel. Alternatively, wrap subscriber in
    # a 'with' block to automatically call close() when done.
    subscriber.[close](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client.html#google_cloud_pubsub_v1_subscriber_client_Client_close)()

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
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

Read about the other delivery options you can configure for a subscription:

  * [Handle transient spikes with flow control](https://docs.cloud.google.com/pubsub/docs/flow-control)

  * [Handle message failures with subscription retry policy](https://docs.cloud.google.com/pubsub/docs/handling-failures#subscription_retry_policy)

  * [Forward undelivered messages to a dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic)

  * [Replay previously-acked messages or purge messages](https://docs.cloud.google.com/pubsub/docs/replay-overview)

  * [Receive messages in order](https://docs.cloud.google.com/pubsub/docs/ordering)

  * [Filter messages by their attributes](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter)

  * [Receive and acknowledge messages exactly-once](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)

  * [Process more messages with concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
