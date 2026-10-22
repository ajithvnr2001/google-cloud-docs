---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-quickstart-publisher/
title: Publish \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:07.666657+00:00
---

# Publish  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-quickstart-publisher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Publish Stay organized with collections  Save and categorize content based on your preferences. 

Publish messages to a single-partition Lite topic and resolve the publish futures asynchronously. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Publishing messages to Lite topics](https://docs.cloud.google.com/pubsub/lite/docs/publishing)
  * [Quickstart: Publish and receive messages in Pub/Sub by using the client libraries](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



## Code sample

### Go

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"sync"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsublite/pscompat"
    	"golang.org/x/sync/errgroup"
    )
    
    func main() {
    	// NOTE: Set these flags for an existing Pub/Sub Lite topic when running this
    	// sample.
    	projectID := flag.String("project_id", "", "Cloud Project ID")
    	zone := flag.String("zone", "", "Cloud Zone where the topic resides, e.g. us-central1-a")
    	topicID := flag.String("topic_id", "", "Existing Pub/Sub Lite topic")
    	messageCount := flag.Int("message_count", 100, "The number of messages to send")
    	flag.Parse()
    
    	ctx := context.Background()
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", *projectID, *zone, *topicID)
    
    	// Create the publisher client.
    	publisher, err := pscompat.NewPublisherClient(ctx, topicPath)
    	if err != nil {
    		log.Fatalf("pscompat.NewPublisherClient error: %v", err)
    	}
    
    	// Ensure the publisher will be shut down.
    	defer publisher.Stop()
    
    	// Collect any messages that need to be republished with a new publisher
    	// client.
    	var toRepublish []*pubsub.Message
    	var toRepublishMu sync.Mutex
    
    	// Publish messages. Messages are automatically batched.
    	g := new(errgroup.Group)
    	for i := 0; i < *messageCount; i++ {
    		msg := &pubsub.Message{
    			Data: []byte(fmt.Sprintf("message-%d", i)),
    		}
    		result := publisher.Publish(ctx, msg)
    
    		g.Go(func() error {
    			// Get blocks until the result is ready.
    			id, err := result.Get(ctx)
    			if err != nil {
    				// NOTE: A failed PublishResult indicates that the publisher client
    				// encountered a fatal error and has permanently terminated. After the
    				// fatal error has been resolved, a new publisher client instance must
    				// be created to republish failed messages.
    				fmt.Printf("Publish error: %v\n", err)
    				toRepublishMu.Lock()
    				toRepublish = append(toRepublish, msg)
    				toRepublishMu.Unlock()
    				return err
    			}
    
    			// Metadata decoded from the id contains the partition and offset.
    			metadata, err := pscompat.ParseMessageMetadata(id)
    			if err != nil {
    				fmt.Printf("Failed to parse message metadata %q: %v\n", id, err)
    				return err
    			}
    			fmt.Printf("Published: partition=%d, offset=%d\n", metadata.Partition, metadata.Offset)
    			return nil
    		})
    	}
    	if err := g.Wait(); err != nil {
    		fmt.Printf("Publishing finished with error: %v\n", err)
    	}
    	fmt.Printf("Published %d messages\n", *messageCount-len(toRepublish))
    
    	// Print the error that caused the publisher client to terminate (if any),
    	// which may contain more context than PublishResults.
    	if err := publisher.Error(); err != nil {
    		fmt.Printf("Publisher client terminated due to error: %v\n", publisher.Error())
    	}
    }
    

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.cloudpubsub.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html);
    import com.google.cloud.pubsublite.cloudpubsub.[PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class PublisherExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing topic for the publish example to work.
        String topicId = "your-topic-id";
        long projectNumber = Long.parseLong("123456789");
        int messageCount = 100;
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        publisherExample(cloudRegion, zoneId, projectNumber, topicId, messageCount, regional);
      }
    
      // Publish messages to a topic.
      public static void publisherExample(
          String cloudRegion,
          char zoneId,
          long projectNumber,
          String topicId,
          int messageCount,
          boolean regional)
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
                .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(topicId))
                .build();
    
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html) publisher = null;
        List<ApiFuture<String>> futures = new ArrayList<>();
    
        try {
          [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html) publisherSettings =
              [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html).newBuilder().setTopicPath(topicPath).build();
    
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html).create(publisherSettings);
    
          // Start the publisher. Upon successful starting, its state will become RUNNING.
          publisher.startAsync().awaitRunning();
    
          for (int i = 0; i < messageCount; i++) {
            String message = "message-" + i;
    
            // Convert the message to a byte string.
            [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
            [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().setData(data).build();
    
            // Publish a message. Messages are automatically batched.
            ApiFuture<String> future = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)(pubsubMessage);
            futures.add(future);
          }
        } finally {
          ArrayList<MessageMetadata> metadata = new ArrayList<>();
          List<String> ackIds = [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[allAsList](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_allAsList_java_lang_Iterable___extends_com_google_api_core_ApiFuture___extends_V___)(futures).get();
          for (String id : ackIds) {
            // Decoded metadata contains partition and offset.
            metadata.add([MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html).[decode](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html#com_google_cloud_pubsublite_MessageMetadata_decode_java_lang_String_)(id));
          }
          System.out.println(metadata + "\nPublished " + ackIds.size() + " messages.");
    
          if (publisher != null) {
            // Shut down the publisher.
            publisher.stopAsync().awaitTerminated();
            System.out.println("Publisher is shut down.");
          }
        }
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
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    topic_path = TopicPath(project_number, location, topic_id)
    
    # PublisherClient() must be used in a `with` block or have __enter__() called before use.
    with PublisherClient() as publisher_client:
        data = "Hello world!"
        api_future = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).publish(topic_path, data.encode("utf-8"))
        # result() blocks. To resolve API futures asynchronously, use add_done_callback().
        message_id = api_future.result()
        message_metadata = MessageMetadata.decode(message_id)
        print(
            f"Published a message to {topic_path} with partition {message_metadata.partition.value} and offset {message_metadata.cursor.offset}."
        )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
