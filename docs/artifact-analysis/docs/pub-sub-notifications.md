---
url: https://docs.cloud.google.com/artifact-analysis/docs/pub-sub-notifications/
title: Configure Pub/Sub notifications \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:27.551147+00:00
---

# Configure Pub/Sub notifications  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/pub-sub-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Configure Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up notifications for updates to [notes](https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview#note) and [occurrences](https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview#occurrence).

Artifact Analysis provides notifications via Pub/Sub for vulnerabilities found by [automated scanning](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) and for other metadata. When a note or occurrence is created or updated, a message is published to the corresponding topic for each API version. Use the topic for the API version you are using.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Container Analysis API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=containeranalysis.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. Enable the Container Analysis API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=containeranalysis.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Learn [how to set up access control](https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control) for metadata in your project. Skip this step if you only consume metadata from occurrences created by Artifact Analysis container scanning.



## Create Pub/Sub topics

After you activate the Artifact Analysis API, Artifact Analysis automatically creates Pub/Sub topics with the following topic IDs:

  * `container-analysis-notes-v1`
  * `container-analysis-occurrences-v1`



If the topics were accidentally deleted or are missing, you can add them yourself. For example, the topics might be missing if your Google Cloud organization has an [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that requires encryption with customer-managed encryption keys (CMEK). When the Pub/Sub API is in the deny list of this constraint, services cannot automatically create topics with Google-owned and Google-managed encryption keys.

To create the topics with Google-owned and Google-managed encryption keys:

### Console

  1. Go to the Pub/Sub topics page in the Google Cloud console.

[Open the Pub/Sub topics page](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click **Create Topic**.

  3. Enter a Topic ID:
         
         container-analysis-notes-v1
         

so that the name matches URI:
         
         projects/PROJECT_ID/topics/container-analysis-notes-v1
         

where PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  4. Click **Create**.

  5. Enter a Topic ID:
         
         container-analysis-occurrences-v1
         

so that the name matches URI:
         
         projects/PROJECT_ID/topics/container-analysis-occurrences-v1
         




### gcloud

Run the following commands in your shell or terminal window:
    
    
    gcloud pubsub topics create projects/PROJECT_ID/topics/container-analysis-notes-v1
    gcloud pubsub topics create projects/PROJECT_ID/topics/container-analysis-occurrences-v1
    

**Note:** If this command returns a "Resource already exists in the project" error, the topic already exists.

To learn more about the `gcloud pubsub topics` command, see the [`topics` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics).

To create the topics with CMEK encryption, see the Pub/Sub [instructions for encrypting topics](https://docs.cloud.google.com/pubsub/docs/encryption#using-cmek).

Anytime a note or an occurrence is created or updated, a message is published to the respective topic, though you must also create a Pub/Sub subscription to listen for events and receive messages from the Pub/Sub service.

## Create Pub/Sub subscriptions

To listen to events, create a Pub/Sub subscription associated with the topic:

### Console

  1. Go to the Pub/Sub subscriptions page in the Google Cloud console.

[Open the Pub/Sub subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription/list)

  2. Click **Create Subscription**.

  3. Type a name for the subscription. For example, _notes_.

  4. Enter the URI of the topic for notes:
         
         projects/PROJECT_ID/topics/container-analysis-notes-v1
         

where PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  5. Click **Create**.

  6. Create another subscription for occurrences with the URI:
         
         projects/PROJECT_ID/topics/container-analysis-occurrences-v1
         




### gcloud

To receive Pub/Sub events, you must first create a subscription associated with the `container-analysis-occurrences-v1` topic:
    
    
    gcloud pubsub subscriptions create \
        --topic container-analysis-occurrences-v1 occurrences
    

Going forward, you can pull messages concerning your occurrences using your new subscription:
    
    
    gcloud pubsub subscriptions pull \
        --auto-ack occurrences
    

### Java

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/overview). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import com.google.pubsub.v1.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import io.grpc.StatusRuntimeException;
    import java.io.IOException;
    import java.lang.InterruptedException;
    import java.util.concurrent.TimeUnit;
    
    public class Subscriptions {
      // Handle incoming Occurrences using a Cloud Pub/Sub subscription
      public static int pubSub(String subId, long timeoutSeconds, String projectId)
          throws InterruptedException {
        // String subId = "my-occurrence-subscription";
        // long timeoutSeconds = 20;
        // String projectId = "my-project-id";
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = null;
        MessageReceiverExample receiver = new MessageReceiverExample();
    
        try {
          // Subscribe to the requested Pub/Sub channel
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subName = [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subId);
          subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subName, receiver).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
          // Sleep to listen for messages
          TimeUnit.SECONDS.sleep(timeoutSeconds);
        } finally {
          // Stop listening to the channel
          if (subscriber != null) {
            subscriber.stopAsync();
          }
        }
        // Print and return the number of Pub/Sub messages received
        System.out.println(receiver.messageCount);
        return receiver.messageCount;
      }
    
      // Custom class to handle incoming Pub/Sub messages
      // In this case, the class will simply log and count each message as it comes in
      static class MessageReceiverExample implements [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) {
        public int messageCount = 0;
    
        @Override
        public synchronized void receiveMessage([PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) message, [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) consumer) {
          // Every time a Pub/Sub message comes in, print it and count it
          System.out.println("Message " + messageCount + ": " + message.[getData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getData__)().toStringUtf8());
          messageCount += 1;
          // Acknowledge the message
          consumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
        }
      }
    
      // Creates and returns a Pub/Sub subscription object listening to the Occurrence topic
      public static [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) createOccurrenceSubscription(String subId, String projectId) 
          throws IOException, StatusRuntimeException, InterruptedException {
        // This topic id will automatically receive messages when Occurrences are added or modified
        String topicId = "container-analysis-occurrences-v1";
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html) subName = [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html).of(projectId, subId);
    
        [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) client = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create();
        [PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html) config = [PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html).getDefaultInstance();
        [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) sub = client.[createSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html#com_google_cloud_pubsub_v1_SubscriptionAdminClient_createSubscription__org_jspecify_annotations_Nullable_com_google_pubsub_v1_SubscriptionName__org_jspecify_annotations_Nullable_com_google_pubsub_v1_TopicName_com_google_pubsub_v1_PushConfig_int_)(subName, topicName, config, 0);
        return sub;
      }
    }

### Go

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Go API reference documentation](https://godoc.org/cloud.google.com/go/containeranalysis/apiv1). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"sync"
    	"time"
    
    	pubsub "cloud.google.com/go/pubsub"
    )
    
    // occurrencePubsub handles incoming Occurrences using a Cloud Pub/Sub subscription.
    func occurrencePubsub(w io.Writer, subscriptionID string, timeout time.Duration, projectID string) (int, error) {
    	// subscriptionID := fmt.Sprintf("my-occurrences-subscription")
    	// timeout := time.Duration(20) * time.Second
    	ctx := context.Background()
    
    	var mu sync.Mutex
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return -1, fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	// Subscribe to the requested Pub/Sub channel.
    	sub := client.Subscription(subscriptionID)
    	count := 0
    
    	// Listen to messages for 'timeout' seconds.
    	ctx, cancel := context.WithTimeout(ctx, timeout)
    	defer cancel()
    	err = sub.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		mu.Lock()
    		count = count + 1
    		fmt.Fprintf(w, "Message %d: %q\n", count, string(msg.Data))
    		msg.Ack()
    		mu.Unlock()
    	})
    	if err != nil {
    		return -1, fmt.Errorf("sub.Receive: %w", err)
    	}
    	// Print and return the number of Pub/Sub messages received.
    	fmt.Fprintln(w, count)
    	return count, nil
    }
    
    // createOccurrenceSubscription creates a new Pub/Sub subscription object listening to the Occurrence topic.
    func createOccurrenceSubscription(subscriptionID, projectID string) error {
    	// subscriptionID := fmt.Sprintf("my-occurrences-subscription")
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// This topic id will automatically receive messages when Occurrences are added or modified
    	topicID := "container-analysis-occurrences-v1"
    	topic := client.Topic(topicID)
    	config := pubsub.SubscriptionConfig{Topic: topic}
    	_, err = client.CreateSubscription(ctx, subscriptionID, config)
    	return fmt.Errorf("client.CreateSubscription: %w", err)
    }
    

### Node.js

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Node.js API reference documentation](https://googleapis.dev/nodejs/containeranalysis/latest/index.html). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample
     */
    // const projectId = 'your-project-id', // Your GCP Project ID
    // const subscriptionId = 'my-sub-id', // A user-specified subscription to the 'container-analysis-occurrences-v1' topic
    // const timeoutSeconds = 30 // The number of seconds to listen for the new Pub/Sub Messages
    
    // Import the pubsub library and create a client, topic and subscription
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)({projectId});
    const subscription = pubsub.subscription(subscriptionId);
    
    // Handle incoming Occurrences using a Cloud Pub/Sub subscription
    let count = 0;
    const messageHandler = message => {
      count++;
      message.[ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)();
    };
    
    // Listen for new messages until timeout is hit
    subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
    
    setTimeout(() => {
      subscription.removeListener('message', messageHandler);
      console.log(`Polled ${count} occurrences`);
    }, timeoutSeconds * 1000);

### Ruby

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id = "A user-specified identifier for the new subscription"
    # timeout_seconds = "The number of seconds to listen for new Pub/Sub messages"
    # project_id      = "Your Google Cloud project ID"
    
    require "google/cloud/pubsub"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) project_id: project_id
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    subscription = subscription_admin.create_subscription \
      name: pubsub.subscription_path(subscription_id),
      topic: pubsub.topic_path("container-analysis-occurrences-v1")
    
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription.name
    count = 0
    listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) do |received_message|
      count += 1
      # Process incoming occurrence here
      puts "Message #{count}: #{received_message.data}"
      received_message.[acknowledge!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
    end
    
    listener.[start](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-MessageListener.html)
    # Wait for incoming occurrences
    sleep timeout_seconds
    listener.stop.wait!
    
    subscription_admin.delete_subscription subscription: subscription.name
    
    # Print and return the total number of Pub/Sub messages received
    puts "Total Messages Received: #{count}"
    count

### Python

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud.pubsub import [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)
    from google.cloud.pubsub_v1.subscriber.message import [Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)
    
    
    def pubsub(subscription_id: str, timeout_seconds: int, project_id: str) -> int:
        """Respond to incoming occurrences using a Cloud Pub/Sub subscription."""
        # subscription_id := 'my-occurrences-subscription'
        # timeout_seconds = 20
        # project_id = 'my-gcp-project'
    
        client = SubscriberClient()
        subscription_name = client.subscription_path(project_id, subscription_id)
        receiver = MessageReceiver()
        client.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_name, receiver.pubsub_callback)
    
        # listen for 'timeout' seconds
        for _ in range(timeout_seconds):
            time.sleep(1)
        # print and return the number of pubsub messages received
        print(receiver.msg_count)
        return receiver.msg_count
    
    
    class MessageReceiver:
        """Custom class to handle incoming Pub/Sub messages."""
    
        def __init__(self) -> None:
            # initialize counter to 0 on initialization
            self.msg_count = 0
    
        def pubsub_callback(self, message: Message) -> None:
            # every time a pubsub message comes in, print it and count it
            self.msg_count += 1
            print(f"Message {self.msg_count}: {message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)}")
            message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    
    def create_occurrence_subscription(subscription_id: str, project_id: str) -> bool:
        """Creates a new Pub/Sub subscription object listening to the
        Container Analysis Occurrences topic."""
        # subscription_id := 'my-occurrences-subscription'
        # project_id = 'my-gcp-project'
    
        topic_id = "container-analysis-occurrences-v1"
        client = SubscriberClient()
        topic_name = f"projects/{project_id}/topics/{topic_id}"
        subscription_name = client.subscription_path(project_id, subscription_id)
        success = True
        try:
            client.create_subscription({"name": subscription_name, "topic": topic_name})
        except AlreadyExists:
            # if subscription already exists, do nothing
            pass
        else:
            success = False
        return success
    
    

Subscriber applications only receive messages that are published to the topic after the subscription is created.

Pub/Sub payloads are in JSON and their schema is as follows:

Notes:
    
    
    {
        "name": "projects/PROJECT_ID/notes/NOTE_ID",
        "kind": "NOTE_KIND",
        "notificationTime": "NOTIFICATION_TIME",
    }

Occurrences:
    
    
    {
        "name": "projects/PROJECT_ID/occurrences/OCCURRENCE_ID",
        "kind": "NOTE_KIND",
        "notificationTime": "NOTIFICATION_TIME",
    }

where:

  * NOTE_KIND is one of the values in [`NoteKind`](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/NoteKind)
  * NOTIFICATION_TIME is a timestamp in RFC 3339 UTC "Zulu" format, accurate to nanoseconds.



## View details

To learn more about a note or occurrence, you can access metadata stored in Artifact Analysis. For example, you can request all the details for a specific occurrence. See instructions in [Investigating Vulnerabilities](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities#single-occurrence).

## What's next

  * For instructions on how to use Artifact Analysis to store and manage your custom metadata, see [Create custom notes and occurrences](https://docs.cloud.google.com/artifact-analysis/docs/create-notes-occurrences).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
