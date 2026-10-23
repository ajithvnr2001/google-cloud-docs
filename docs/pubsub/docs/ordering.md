---
url: https://docs.cloud.google.com/pubsub/docs/ordering/
title: Order messages \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:06.582988+00:00
---

# Order messages  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/ordering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Order messages Stay organized with collections  Save and categorize content based on your preferences. 

Message ordering is a feature in Pub/Sub that lets you receive messages in your subscriber clients in the order that they were published by the publisher clients.

For example, assume that a publisher client in a region publishes messages 1, 2, and 3 in order. With message ordering, the subscriber client receives the published messages in the same order. To be delivered in order, the publisher client must publish the messages in the same [region](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#pubsub_endpoints). However, subscribers can connect to any region and the ordering guarantee is still maintained.

Message ordering is a useful feature for scenarios such as database change capture, user session tracking, and streaming applications where preserving the chronology of events is important.

This page explains the concept of message ordering and how to set up your subscriber clients to receive messages in order. To configure your publisher clients for message ordering, see [Use ordering keys to publish a message](https://docs.cloud.google.com/pubsub/docs/publisher#using-ordering-keys).

## Overview of message ordering

Ordering in Pub/Sub is determined by the following:

  * **Ordering key**. An _ordering key_ is a string that identifies related messages that should be ordered. Examples of ordering keys include customer IDs or the primary key of a row in a database. An ordering key can be up to 1 KB in length.

To achieve message ordering, set the same ordering key on all related messages that should be received in order. In addition, you must publish all messages with the same ordering key in the same region. For more information, see [Use ordering keys to publish a message](https://docs.cloud.google.com/pubsub/docs/publisher#using-ordering-keys).

Messages with an empty ordering key are not ordered.

  * **Enable message ordering**. To receive messages in order, you must enable message ordering in the subscription. For more information, see Enable message ordering.

If message ordering is not enabled, then a subscription receives messages without an expected ordering. For example, assume that subscriptions _A_ and _B_ are both attached to the same topic _T_ , and that ordering is enabled in subscription _A_ but not subscription _B_. Although both subscriptions receive the same set of messages from topic _T_ , ordering is only preserved for subscription _A_.




The publishing throughput on each ordering key is limited to 1 MBps. Throughput across all ordering keys on a topic is limited to the quota available in a [publish region](https://docs.cloud.google.com/pubsub/quotas). This limit can be increased to multiple GBps.

In general, if your solution requires publisher clients to send both ordered and unordered messages, create separate topics, one for ordered messages and the other for unordered messages.

## Considerations when using ordered messaging

The following list contains important information regarding the behavior of ordered messaging in Pub/Sub:

  * **Cardinality**. An ordering key is not equivalent to a partition in a partition-based messaging system, because ordering keys are expected to have a much higher cardinality than partitions.

  * **Within-key ordering** : Messages published with the same ordering key are expected to be received in order. Assume that for ordering key A, you publish messages 1, 2, and 3. With ordering enabled, 1 is expected to be delivered before 2 and 2 is expected to be delivered before 3.

  * **Across-key ordering** : Messages published with different ordering keys are not expected to be received in order. Assume you have ordering keys A and B. For ordering key A, messages 1 and 2 are published in order. For ordering key B, messages 3 and 4 are published in order. However, message 1 could arrive before or after message 4.

  * **Message redelivery** : Pub/Sub delivers each message [at least once](https://docs.cloud.google.com/pubsub/docs/subscription-overview#default_properties), so the Pub/Sub service might redeliver messages. Redeliveries of a message trigger redelivery of all subsequent messages for that key, even acknowledged ones. Assume that a subscriber client receives messages 1, 2, and 3 for a specific ordering key. If message 2 is redelivered (because the acknowledgment deadline expired or the best-effort acknowledgment did not persist in Pub/Sub), then message 3 is also redelivered. If both message ordering and a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) are enabled on a subscription, this behavior might not be true, as Pub/Sub forwards messages to dead-letter topics on a best-effort basis.

  * **Acknowledgment delays and dead-letter topics** : Unacknowledged messages for a given ordering key can potentially delay delivery of messages for other ordering keys, especially during server restarts or traffic changes. To maintain order across such events, ensure timely acknowledgment of all messages. If timely acknowledgment is not possible, consider using a dead-letter topic to prevent indefinite message holding. Be aware that order might not be preserved when messages are written to a dead-letter topic.

  * **Message affinity (streamingPull clients)** : Messages for the same key are usually delivered to the same streamingPull subscriber client. Affinity is expected when messages are outstanding for an ordering key to a specific subscriber client. If there are no outstanding messages, affinity might shift for load balancing or client disconnects.

To ensure smooth processing even with potential affinity changes, it's crucial to design your streamingPull application in a way that it can handle messages in any client for a given ordering key.

  * **Integration with Dataflow** : Don't enable message ordering for subscriptions when configuring Dataflow with Pub/Sub. Dataflow has its own mechanism for total message ordering, ensuring chronological order across all messages as part of windowing operations. This method of ordering differs from Pub/Sub's ordering key-based approach. Using ordering keys with Dataflow can potentially reduce pipeline performance.

  * **Automatic scaling** : Pub/Sub's ordered delivery scales to billions of ordering keys. A larger number of ordering keys allows more parallel delivery to subscribers since ordering applies to all the messages with the same ordering key.

  * **Performance tradeoffs** : Ordered delivery does come with some tradeoffs. Compared with unordered delivery, ordered delivery decreases publish availability and increases end-to-end message delivery latency. In the ordered delivery case, failover requires coordination to ensure the messages are written to and read in the correct order.

  * **Hot key** : When using message ordering, all messages with the same ordering key are sent to your subscriber client in the order they are received by the service. The user callback doesn't run until the callback completes for the previous message. The maximum throughput for messages sharing the same ordering key when delivering to subscribers is not limited by Pub/Sub , but by the processing speed of your subscriber client. A hot key occurs when a backlog builds on an individual ordering key because the number of messages produced per second exceeds the number of messages that the subscriber can process per second. To mitigate hot keys, use the most granular keys that you can and minimize per-message processing time. You can also monitor the `subscription/oldest_unacked_message_age` metric for a rising value, which might indicate a hot key.




For more information about how to use message ordering, see the following best-practices topics:

  * [Best practices for ordered messaging in publishing](https://docs.cloud.google.com/pubsub/docs/publish-best-practices#ordering)

  * [Best practices for ordered messaging in subscribing](https://docs.cloud.google.com/pubsub/docs/subscribe-best-practices#ordering)




## Subscriber client behavior for message ordering

Subscriber clients receive messages in the order they were published in a specific region. Pub/Sub supports different ways of receiving messages, such as subscriber clients connected to pull and push subscriptions. The client libraries use streamingPull (with the exception of PHP).

To learn more about these subscription types, see [Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber).

The following sections discuss what receiving messages in order means for each type of subscriber client.

### StreamingPull subscriber clients

When using the client libraries with streamingPull, you must specify a user callback that runs whenever a message is received by a subscriber client. With client libraries, for any given ordering key, the callback is run to completion on messages in the correct order. If the messages are acknowledged within that callback, all computations on a message occur in order. However, if the user callback schedules other asynchronous work on messages, the subscriber client must ensure that the asynchronous work is done in order. One option is to add messages to a local work queue that is processed in order.

### Pull subscriber clients

For subscriber clients connected to pull subscriptions, Pub/Sub message ordering supports the following:

  * All messages for an ordering key in the [PullResponse](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PullResponse) are in the proper order in the list.

  * Only one batch of messages can be outstanding for an ordering key at a time.




The requirement that only one batch of messages can be outstanding at a time is necessary to maintain ordered delivery since the Pub/Sub service can't ensure the success or latency of the response that it sends for a subscriber's pull request.

### Push subscriber clients

The restrictions on push are even tighter than those on pull. For a push subscription, Pub/Sub supports only one outstanding message for each ordering key at a time. Each message is sent to a push endpoint as a separate request. Thus, sending the requests out in parallel would have the same issue as delivering multiple batches of messages for the same ordering key to pull subscribers simultaneously. Push subscriptions might not be a good choice for topics where messages are frequently published with the same ordering key or where latency is extremely important.

### Export subscriber clients

Export subscriptions support ordered messages. For BigQuery subscriptions, messages with the same ordering key are written to their BigQuery table in order. For Cloud Storage subscriptions, messages with the same ordering key might not all be written to the same file. When within the same file, messages for an ordering key are in order. When spread across multiple files, later messages for an ordering key can appear in a file with a name that has an earlier timestamp than the timestamp in the name of the file with the earlier messages.

## Enable message ordering

To receive the messages in order, set the message ordering property on the subscription you receive messages from. Receiving messages in order might increase latency. You can't change the message ordering property after you create a subscription.

You can set the message ordering property when you create a subscription using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub API.

### Console

To create a subscription with the message ordering property, follow these steps:

  1. In the Google Cloud console, go to the **Subscriptions** page.



[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  1. Click **Create subscription**.

  2. Enter a **Subscription ID**.

  3. Choose a topic from which you want to receive messages.

  4. In the **Message ordering** section, select **Order messages with an ordering key**.

  5. Click **Create**.




### gcloud

To create a subscription with the message ordering property, use the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command and the `--enable-message-ordering` flag:
    
    
    gcloud pubsub subscriptions create SUBSCRIPTION_ID \
      --enable-message-ordering

Replace SUBSCRIPTION_ID with the ID of the subscription.

If the request is successful, the command line displays a confirmation:
    
    
    Created subscription [SUBSCRIPTION_ID].
    

### REST

To create a subscription with the message ordering property, send a `PUT` request like the following:
    
    
    PUT https://pubsub.googleapis.com/v1/projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID
    Authorization: Bearer $(gcloud auth application-default print-access-token)
    

Replace the following:

  * PROJECT_ID: the project ID of the project with the topic
  * SUBSCRIPTION_ID: the ID of the subscription



In the request body, specify the following:
    
    
    {
      "topic": TOPIC_ID,
      "enableMessageOrdering": true,
    }

Replace TOPIC_ID with the ID of the topic to attach to the subscription.

If the request is successful, the response is the subscription in JSON format:
    
    
    {
      "name": projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID,
      "topic": projects/PROJECT_ID/topics/TOPIC_ID,
      "enableMessageOrdering": true,
    }
    

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::SubscriptionAdminClient client,
       std::string const& project_id, std::string const& topic_id,
       std::string const& subscription_id) {
      google::pubsub::v1::Subscription request;
      request.set_name(
          pubsub::Subscription(project_id, subscription_id).FullName());
      request.set_topic(pubsub::Topic(project_id, topic_id).FullName());
      request.set_enable_message_ordering(true);
      auto sub = client.CreateSubscription(request);
      if (sub.status().code() == google::cloud::StatusCode::kAlreadyExists) {
        std::cout << "The subscription already exists\n";
        return;
      }
      if (!sub) throw std::move(sub).status();
    
      std::cout << "The subscription was successfully created: "
                << sub->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    
    public class CreateSubscriptionWithOrderingSample
    {
        public Subscription CreateSubscriptionWithOrdering(string projectId, string topicId, string subscriptionId)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            var topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            var subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
    
            var subscriptionRequest = new [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html)
            {
                SubscriptionName = subscriptionName,
                TopicAsTopicName = topicName,
                EnableMessageOrdering = true
            };
    
            [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html) subscription = null;
            try
            {
                subscription = subscriber.[CreateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_CreateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Api_Gax_Grpc_CallSettings_)(subscriptionRequest);
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e) when (e.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html).[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[AlreadyExists](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists))
            {
                // Already exists.  That's fine.
            }
            return subscription;
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
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    func createWithOrdering(w io.Writer, projectID, topic, subscription string) error {
    	// projectID := "my-project-id"
    	// topic := "projects/my-project-id/topics/my-topic"
    	// subscription := "projects/my-project/subscriptions/my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Message ordering can only be set when creating a subscription.
    	sub, err := client.SubscriptionAdminClient.CreateSubscription(ctx, &pubsubpb.Subscription{
    		Name:                  subscription,
    		Topic:                 topic,
    		EnableMessageOrdering: true,
    	})
    	if err != nil {
    		return fmt.Errorf("CreateSubscription: %w", err)
    	}
    	fmt.Fprintf(w, "Created subscription: %v\n", sub)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import java.io.IOException;
    
    public class CreateSubscriptionWithOrdering {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
    
        createSubscriptionWithOrderingExample(projectId, topicId, subscriptionId);
      }
    
      public static void createSubscriptionWithOrderingExample(
          String projectId, String topicId, String subscriptionId) throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
    
          [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) topicName = [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(projectId, topicId);
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription =
              subscriptionAdminClient.createSubscription(
                  [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html).newBuilder()
                      .setName(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)())
                      .setTopic(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html#com_google_pubsub_v1_ProjectTopicName_toString__)())
                      // Set message ordering to true for ordered messages in the subscription.
                      .setEnableMessageOrdering(true)
                      .build());
    
          System.out.println("Created a subscription with ordering: " + subscription.getAllFields());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function createSubscriptionWithOrdering(
      topicNameOrId,
      subscriptionNameOrId,
    ) {
      // Creates a new subscription
      await pubSubClient
        .topic(topicNameOrId)
        .createSubscription(subscriptionNameOrId, {
          enableMessageOrdering: true,
        });
      console.log(
        `Created subscription ${subscriptionNameOrId} with ordering enabled.`,
      );
      console.log(
        'To process messages in order, remember to add an ordering key to your messages.',
      );
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createSubscriptionWithOrdering(
      topicNameOrId: string,
      subscriptionNameOrId: string,
    ) {
      // Creates a new subscription
      await pubSubClient
        .topic(topicNameOrId)
        .createSubscription(subscriptionNameOrId, {
          enableMessageOrdering: true,
        });
      console.log(
        `Created subscription ${subscriptionNameOrId} with ordering enabled.`,
      );
      console.log(
        'To process messages in order, remember to add an ordering key to your messages.',
      );
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer): Choose an existing topic.
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "enable_message_ordering": True,
            }
        )
        print(f"Created subscription with ordering: {subscription}")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # topic_id        = "your-topic-id"
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    subscription = subscription_admin.create_subscription \
      name: pubsub.subscription_path(subscription_id),
      topic: pubsub.topic_path(topic_id),
      enable_message_ordering: true
    
    puts "Pull subscription #{subscription_id} created with message ordering."

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
    use google_cloud_pubsub::client::SubscriptionAdmin;
    
    pub async fn sample(
        client: &SubscriptionAdmin,
        project_id: &str,
        topic_id: &str,
        subscription_id: &str,
    ) -> anyhow::Result<()> {
        let subscription_name = format!("projects/{project_id}/subscriptions/{subscription_id}");
        let topic_name = format!("projects/{project_id}/topics/{topic_id}");
    
        let subscription = client
            .create_subscription()
            .set_name(subscription_name)
            .set_topic(topic_name)
            .set_enable_message_ordering(true)
            .send()
            .await?;
    
        println!("successfully created subscription {subscription:?}");
        Ok(())
    }

## What's next

  * Read the blog post about [ordered delivery](https://medium.com/google-cloud/google-cloud-pub-sub-ordered-delivery-1e4181f60bc8).

  * To continue publishing messages in the case of non-retryable errors, see [Retry requests with ordering keys](https://docs.cloud.google.com/pubsub/docs/retry-requests#retry_ordering).

  * Monitor your [subscription](https://docs.cloud.google.com/pubsub/docs/monitoring#maintain_a_healthy_subscription).

  * Read about publishing messages with [ordering keys](https://docs.cloud.google.com/pubsub/docs/publisher#using-ordering-keys).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
