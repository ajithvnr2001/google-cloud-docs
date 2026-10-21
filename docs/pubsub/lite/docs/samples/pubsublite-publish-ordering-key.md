---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-publish-ordering-key/
title: Publish with ordering keys \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:24.984593+00:00
---

# Publish with ordering keys  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-publish-ordering-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Publish with ordering keys Stay organized with collections  Save and categorize content based on your preferences. 

Publish messages with an ordering key. Ordering keys are hashed to map to a partition. Messages of the same ordering key get published to the same partition. If the partition is filled up, oldest messages get written over.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Publishing messages to Lite topics](https://docs.cloud.google.com/pubsub/lite/docs/publishing)



## Code sample

### Go

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsublite/pscompat"
    )
    
    func publishWithOrderingKey(w io.Writer, projectID, zone, topicID string, messageCount int) error {
    	// projectID := "my-project-id"
    	// zone := "us-central1-a"
    	// topicID := "my-topic"
    	// messageCount := 10
    	ctx := context.Background()
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, zone, topicID)
    
    	// Create the publisher client.
    	publisher, err := pscompat.NewPublisherClient(ctx, topicPath)
    	if err != nil {
    		return fmt.Errorf("pscompat.NewPublisherClient error: %w", err)
    	}
    
    	// Ensure the publisher will be shut down.
    	defer publisher.Stop()
    
    	// Messages of the same ordering key will always get published to the same
    	// partition. When OrderingKey is unset, messages can get published to
    	// different partitions if more than one partition exists for the topic.
    	var results []*pubsub.[PublishResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_PublishResult)
    	for i := 0; i < messageCount; i++ {
    		r := publisher.Publish(ctx, &pubsub.Message{
    			OrderingKey: "test_ordering_key",
    			Data:        []byte(fmt.Sprintf("message-%d", i)),
    		})
    		results = append(results, r)
    	}
    
    	// Print publish results.
    	var publishedCount int
    	for _, r := range results {
    		// Get blocks until the result is ready.
    		id, err := r.Get(ctx)
    		if err != nil {
    			// NOTE: A failed PublishResult indicates that the publisher client
    			// encountered a fatal error and has permanently terminated. After the
    			// fatal error has been resolved, a new publisher client instance must be
    			// created to republish failed messages.
    			fmt.Fprintf(w, "Publish error: %v\n", err)
    			continue
    		}
    
    		// Metadata decoded from the id contains the partition and offset.
    		metadata, err := pscompat.ParseMessageMetadata(id)
    		if err != nil {
    			return fmt.Errorf("failed to parse message metadata %q: %w", id, err)
    		}
    		fmt.Fprintf(w, "Published: partition=%d, offset=%d\n", metadata.Partition, metadata.Offset)
    		publishedCount++
    	}
    
    	fmt.Fprintf(w, "Published %d messages with ordering key\n", publishedCount)
    	return publisher.Error()
    }
    

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.cloudpubsub.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html);
    import com.google.cloud.pubsublite.cloudpubsub.[PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.ExecutionException;
    
    public class PublishWithOrderingKeyExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing topic for the publish example to work.
        String topicId = "your-topic-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        publishWithOrderingKeyExample(cloudRegion, zoneId, projectNumber, topicId, regional);
      }
    
      // Publish a message to a topic with an ordering key.
      public static void publishWithOrderingKeyExample(
          String cloudRegion, char zoneId, long projectNumber, String topicId, boolean regional)
          throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), ExecutionException, InterruptedException {
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html) topicPath =
            [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation(location)
                .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html).of(topicId))
                .build();
    
        [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html) publisherSettings =
            [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html).newBuilder().setTopicPath(topicPath).build();
    
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html) publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html).create(publisherSettings);
    
        // Start the publisher. Upon successful starting, its state will become RUNNING.
        publisher.startAsync().awaitRunning();
    
        String message = "message-with-ordering-key";
    
        // Convert the message to a byte string.
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
        [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage =
            [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder()
                .setData(data)
                // Messages of the same ordering key will always get published to the
                // same partition. When OrderingKey is unset, messages can get published
                // to different partitions if more than one partition exists for the topic.
                .[setOrderingKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setOrderingKey_java_lang_String_)("testing")
                .build();
    
        // Publish a message.
        ApiFuture<String> future = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)(pubsubMessage);
    
        // Shut down the publisher.
        publisher.stopAsync().awaitTerminated();
    
        String ackId = future.get();
        [MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html) metadata = [MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html).[decode](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html#com_google_cloud_pubsublite_MessageMetadata_decode_java_lang_String_)(ackId);
        System.out.println("Published a message with ordering key:\n" + metadata);
      }
    }

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.pubsublite.cloudpubsub import [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)
    from google.cloud.pubsublite.types import (
        CloudRegion,
        CloudZone,
        MessageMetadata,
        TopicPath,
    )
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # num_messages = 100
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    topic_path = TopicPath(project_number, location, topic_id)
    
    # PublisherClient() must be used in a `with` block or have __enter__() called before use.
    with PublisherClient() as publisher_client:
        for message in range(num_messages):
            data = f"{message}"
            # Messages of the same ordering key will always get published to the same partition.
            # When ordering_key is unset, messsages can get published ot different partitions if
            # more than one partition exists for the topic.
            api_future = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).publish(
                topic_path, data.encode("utf-8"), ordering_key="testing"
            )
            # result() blocks. To resolve api futures asynchronously, use add_done_callback().
            message_id = api_future.result()
            message_metadata = MessageMetadata.decode(message_id)
            print(
                f"Published {data} to partition {message_metadata.partition.value} and offset {message_metadata.cursor.offset}."
            )
    
    print(
        f"Finished publishing {num_messages} messages with an ordering key to {str(topic_path)}."
    )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
