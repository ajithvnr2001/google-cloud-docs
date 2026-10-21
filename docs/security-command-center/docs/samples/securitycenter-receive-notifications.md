---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-receive-notifications/
title: Receive notifications \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:35.474282+00:00
---

# Receive notifications  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-receive-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Receive notifications Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to convert a Pub/Sub message into a notification message

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"bytes"
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"github.com/golang/protobuf/jsonpb"
    )
    
    func receiveMessages(w io.Writer, projectID string, subscriptionName string) error {
    	// projectID := "your-project-id"
    	// subsriptionName := "your-subscription-name"
    
    	ctx := context.Background()
    
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub := client.Subscription(subscriptionName)
    	cctx, cancel := context.WithCancel(ctx)
    	err = sub.Receive(cctx, func(ctx context.Context, msg *pubsub.Message) {
    		var notificationMessage = new(securitycenterpb.[NotificationMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv1_securitycenterpb_NotificationMessage))
    		jsonpb.Unmarshal(bytes.NewReader(msg.Data), notificationMessage)
    
    		fmt.Fprintln(w, "Got finding: ", notificationMessage.GetFinding())
    		msg.Ack()
    		cancel()
    	})
    	if err != nil {
    		return fmt.Errorf("Receive: %w", err)
    	}
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.cloud.securitycenter.v1.[NotificationMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationMessage.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class NotificationReceiver {
    
      private NotificationReceiver() {
      }
    
      public static void receiveNotificationMessages(String projectId, String subscriptionId) {
        // String projectId = "{your-project}";
        // String subscriptionId = "{your-subscription}";
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        try {
          [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber =
              [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, new NotificationMessageReceiver()).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
    
          // This sets the timeout value of the subscriber to 10s.
          subscriber.awaitTerminated(10_000, TimeUnit.MILLISECONDS);
        } catch (IllegalStateException | TimeoutException e) {
          System.out.println("Subscriber stopped: " + e);
        }
      }
    
      static class NotificationMessageReceiver implements [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) {
    
        @Override
        public void receiveMessage([PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) message, [AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html) consumer) {
          [NotificationMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationMessage.html).Builder notificationMessageBuilder = [NotificationMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationMessage.html).newBuilder();
    
          try {
            String jsonString = message.[getData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html#com_google_pubsub_v1_PubsubMessage_getData__)().toStringUtf8();
            [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(jsonString, notificationMessageBuilder);
    
            [NotificationMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationMessage.html) notificationMessage = notificationMessageBuilder.build();
            System.out.println(
                String.format("Config id: %s", notificationMessage.[getNotificationConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationMessage.html#com_google_cloud_securitycenter_v1_NotificationMessage_getNotificationConfigName__)()));
            System.out.println(String.format("Finding: %s", notificationMessage.[getFinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationMessage.html#com_google_cloud_securitycenter_v1_NotificationMessage_getFinding__)()));
          } catch ([InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) e) {
            System.out.println("Could not parse message: " + e);
          } finally {
            consumer.[ack](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html#com_google_cloud_pubsub_v1_AckReplyConsumer_ack__)();
          }
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    const {StringDecoder} = require('string_decoder');
    
    // projectId = 'your-project-id'
    // subscriptionId = 'your-subscription-id'
    
    const subscriptionName =
      'projects/' + projectId + '/subscriptions/' + subscriptionId;
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    function listenForMessages() {
      const subscription = pubSubClient.subscription(subscriptionName);
    
      // message.data is a buffer array of json
      // 1. Convert buffer to normal string
      // 2. Convert json to NotificationMessage object
      const messageHandler = message => {
        const jsonString = new StringDecoder('utf-8').write(message.data);
        const parsedNotificationMessage = JSON.parse(jsonString);
    
        console.log(parsedNotificationMessage);
        console.log(parsedNotificationMessage.finding);
    
        // ACK when done with message
        message.[ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)();
      };
    
      subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
    
      // Set timeout to 10 seconds
      setTimeout(() => {
        subscription.removeListener('message', messageHandler);
      }, 10000);
    }
    
    listenForMessages();

### PHP

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * @param string $projectId             Your Cloud Project ID
     * @param string $subscriptionId        Your subscription ID
     */
    function receive_notification(string $projectId, string $subscriptionId): void
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $subscription = $pubsub->subscription($subscriptionId);
    
        foreach ($subscription->pull() as $message) {
            printf('Message: %s' . PHP_EOL, $message->data());
            // Acknowledge the Pub/Sub message has been received, so it will not be pulled multiple times.
            $subscription->acknowledge($message);
        }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Requires https://cloud.google.com/pubsub/docs/quickstart-client-libraries#pubsub-client-libraries-python
    import concurrent
    
    from google.cloud import pubsub_v1
    from google.cloud.securitycenter_v1 import NotificationMessage
    from google.protobuf.json_format import ParseError
    
    # TODO: project_id = "your-project-id"
    # TODO: subscription_name = "your-subscription-name"
    
    def callback(message):
        # Print the data received for debugging purpose if needed
        print(f"Received message: {message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)}")
    
        try:
            notification_msg = NotificationMessage.from_json(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
            print(
                "Notification config name: "
                f"{notification_msg.notification_config_name}"
            )
            print(f"Finding: {notification_msg.finding}")
        except ParseError:
            print("Could not parse received message as a NotificationMessage.")
    
        # Ack the message to prevent it from being pulled again
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)
    
    streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
    
    print(f"Listening for messages on {subscription_path}...\n")
    try:
        streaming_pull_future.result(timeout=1)  # Block for 1 second
    except concurrent.futures.TimeoutError:
        streaming_pull_future.cancel()

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
