---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-quickstart-subscriber/
title: Subscribe \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:02:11.628214+00:00
---

# Subscribe  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-quickstart-subscriber/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Subscribe Stay organized with collections  Save and categorize content based on your preferences. 

Use a multi-partition and flow-controlled subscriber (a collection of subscribers) to subscribe to a multiple-partition topic and process messages asynchronously in callbacks.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Publish and receive messages in Pub/Sub by using the client libraries](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)
  * [Receiving messages from Lite subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/subscribing)



## Code sample

### Go

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"sync/atomic"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsublite/pscompat"
    )
    
    func main() {
    	// NOTE: Set these flags for an existing Pub/Sub Lite subscription containing
    	// published messages when running this sample.
    	projectID := flag.String("project_id", "", "Cloud Project ID")
    	zone := flag.String("zone", "", "Cloud Zone where the topic resides, e.g. us-central1-a")
    	subscriptionID := flag.String("subscription_id", "", "Existing Pub/Sub Lite subscription")
    	timeout := flag.Duration("timeout", 90*time.Second, "The duration to receive messages")
    	flag.Parse()
    
    	ctx := context.Background()
    	subscriptionPath := fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", *projectID, *zone, *subscriptionID)
    
    	// Configure flow control settings. These settings apply per partition.
    	// The message stream is paused based on the maximum size or number of
    	// messages that the subscriber has already received, whichever condition is
    	// met first.
    	settings := pscompat.ReceiveSettings{
    		// 10 MiB. Must be greater than the allowed size of the largest message
    		// (1 MiB).
    		MaxOutstandingBytes: 10 * 1024 * 1024,
    		// 1,000 outstanding messages. Must be > 0.
    		MaxOutstandingMessages: 1000,
    	}
    
    	// Create the subscriber client.
    	subscriber, err := pscompat.NewSubscriberClientWithSettings(ctx, subscriptionPath, settings)
    	if err != nil {
    		log.Fatalf("pscompat.NewSubscriberClientWithSettings error: %v", err)
    	}
    
    	// Listen for messages until the timeout expires.
    	log.Printf("Listening to messages on %s for %v...\n", subscriptionPath, *timeout)
    	cctx, cancel := context.WithTimeout(ctx, *timeout)
    	defer cancel()
    	var receiveCount int32
    
    	// Receive blocks until the context is cancelled or an error occurs.
    	if err := subscriber.Receive(cctx, func(ctx context.Context, msg *pubsub.Message) {
    		// NOTE: May be called concurrently; synchronize access to shared memory.
    		atomic.AddInt32(&receiveCount, 1)
    
    		// Metadata decoded from the message ID contains the partition and offset.
    		metadata, err := pscompat.ParseMessageMetadata(msg.ID)
    		if err != nil {
    			log.Fatalf("Failed to parse %q: %v", msg.ID, err)
    		}
    
    		fmt.Printf("Received (partition=%d, offset=%d): %s\n", metadata.Partition, metadata.Offset, string(msg.Data))
    		msg.Ack()
    	}); err != nil {
    		log.Fatalf("SubscriberClient.Receive error: %v", err)
    	}
    
    	fmt.Printf("Received %d messages\n", receiveCount)
    }
    

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.cloudpubsub.[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html);
    import com.google.cloud.pubsublite.cloudpubsub.[MessageTransforms](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.MessageTransforms.html);
    import com.google.cloud.pubsublite.cloudpubsub.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.cloud.pubsublite.cloudpubsub.[SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SubscriberExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing subscription for the subscribe example to work.
        String subscriptionId = "your-subscription-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        subscriberExample(cloudRegion, zoneId, projectNumber, subscriptionId, regional);
      }
    
      public static void subscriberExample(
          String cloudRegion, char zoneId, long projectNumber, String subscriptionId, boolean regional)
          throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscriptionPath =
            [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
                .setLocation(location)
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html).of(subscriptionId))
                .build();
    
        // The message stream is paused based on the maximum size or number of messages that the
        // subscriber has already received, whichever condition is met first.
        [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html) flowControlSettings =
            [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html).builder()
                // 10 MiB. Must be greater than the allowed size of the largest message (1 MiB).
                .setBytesOutstanding(10 * 1024 * 1024L)
                // 1,000 outstanding messages. Must be >0.
                .setMessagesOutstanding(1000L)
                .build();
    
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage message, AckReplyConsumer consumer) -> {
              System.out.println("Id : " + [MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html).[decode](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html#com_google_cloud_pubsublite_MessageMetadata_decode_java_lang_String_)([message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__).getMessageId()));
              System.out.println("Data : " + [message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__).getData().toStringUtf8());
              System.out.println("Ordering key : " + [message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__).getOrderingKey());
              System.out.println("Attributes : ");
              [message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__)
                  .getAttributesMap()
                  .forEach(
                      (key, value) -> {
                        if (key == MessageTransforms.PUBSUB_LITE_EVENT_TIME_TIMESTAMP_PROTO) {
                          Timestamp ts = MessageTransforms.decodeAttributeEventTime(value);
                          System.out.println(key + " = " + ts.toString());
                        } else {
                          System.out.println(key + " = " + value);
                        }
                      });
    
              // Acknowledge the message.
              consumer.ack();
            };
    
        [SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html) subscriberSettings =
            [SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html).newBuilder()
                .setSubscriptionPath(subscriptionPath)
                .setReceiver(receiver)
                // Flow control settings are set at the partition level.
                .setPerPartitionFlowControlSettings(flowControlSettings)
                .build();
    
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).create(subscriberSettings);
    
        // Start the subscriber. Upon successful starting, its state will become RUNNING.
        subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
    
        System.out.println("Listening to messages on " + [subscriptionPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslReadDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslReadDataSourceOptions_subscriptionPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html#com_google_cloud_pubsublite_SubscriptionPath_toString__)() + "...");
    
        try {
          System.out.println(subscriber.state());
          // Wait 90 seconds for the subscriber to reach TERMINATED state. If it encounters
          // unrecoverable errors before then, its state will change to FAILED and an
          // IllegalStateException will be thrown.
          subscriber.awaitTerminated(90, TimeUnit.SECONDS);
        } catch (TimeoutException t) {
          // Shut down the subscriber. This will change the state of the subscriber to TERMINATED.
          subscriber.[stopAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.wire.ApiServiceUtils.html#com_google_cloud_pubsublite_internal_wire_ApiServiceUtils_stopAsync_java_lang_Iterable___extends_com_google_api_core_ApiService__)().awaitTerminated();
          System.out.println("Subscriber is shut down: " + subscriber.state());
        }
      }
    }

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from concurrent.futures._base import TimeoutError
    from google.pubsub_v1 import PubsubMessage
    from google.cloud.pubsublite.cloudpubsub import [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)
    from google.cloud.pubsublite.types import (
        CloudRegion,
        CloudZone,
        FlowControlSettings,
        MessageMetadata,
        SubscriptionPath,
    )
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # subscription_id = "your-subscription-id"
    # timeout = 90
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    subscription_path = SubscriptionPath(project_number, location, subscription_id)
    # Configure when to pause the message stream for more incoming messages based on the
    # maximum size or number of messages that a single-partition subscriber has received,
    # whichever condition is met first.
    per_partition_flow_control_settings = FlowControlSettings(
        # 1,000 outstanding messages. Must be >0.
        messages_outstanding=1000,
        # 10 MiB. Must be greater than the allowed size of the largest message (1 MiB).
        bytes_outstanding=10 * 1024 * 1024,
    )
    
    def callback(message: PubsubMessage):
        message_data = message.data.decode("utf-8")
        metadata = MessageMetadata.decode(message.message_id)
        print(
            f"Received {message_data} of ordering key {message.ordering_key} with id {metadata}."
        )
        message.ack()
    
    # SubscriberClient() must be used in a `with` block or have __enter__() called before use.
    with SubscriberClient() as subscriber_client:
    
        streaming_pull_future = [subscriber_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.html).subscribe(
            subscription_path,
            callback=callback,
            per_partition_flow_control_settings=per_partition_flow_control_settings,
        )
    
        print(f"Listening for messages on {str(subscription_path)}...")
    
        try:
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError or KeyboardInterrupt:
            streaming_pull_future.cancel()
            assert streaming_pull_future.done()

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
