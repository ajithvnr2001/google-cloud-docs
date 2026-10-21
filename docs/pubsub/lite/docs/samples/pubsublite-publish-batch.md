---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-publish-batch/
title: Publish with batch settings \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:15.072490+00:00
---

# Publish with batch settings  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-publish-batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Publish with batch settings Stay organized with collections  Save and categorize content based on your preferences. 

Publish messages with batch settings.

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
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsublite/pscompat"
    )
    
    func publishWithBatchSettings(w io.Writer, projectID, zone, topicID string, messageCount int) error {
    	// projectID := "my-project-id"
    	// zone := "us-central1-a"
    	// topicID := "my-topic"
    	// messageCount := 10
    	ctx := context.Background()
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, zone, topicID)
    
    	// Batch settings control how the publisher batches messages. These settings
    	// apply per partition.
    	// See https://pkg.go.dev/cloud.google.com/go/pubsublite/pscompat#pkg-variables
    	// for DefaultPublishSettings.
    	settings := pscompat.PublishSettings{
    		ByteThreshold:  5 * 1024, // 5 KiB
    		CountThreshold: 1000,     // 1,000 messages
    		DelayThreshold: 100 * time.Millisecond,
    	}
    
    	// Create the publisher client.
    	publisher, err := pscompat.NewPublisherClientWithSettings(ctx, topicPath, settings)
    	if err != nil {
    		return fmt.Errorf("pscompat.NewPublisherClientWithSettings error: %w", err)
    	}
    
    	// Ensure the publisher will be shut down.
    	defer publisher.Stop()
    
    	// Publish requests are sent to the server based on request size, message
    	// count and time since last publish, whichever condition is met first.
    	var results []*pubsub.[PublishResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_PublishResult)
    	for i := 0; i < messageCount; i++ {
    		r := publisher.Publish(ctx, &pubsub.Message{
    			Data: []byte(fmt.Sprintf("message-%d", i)),
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
    		fmt.Fprintf(w, "Published: %v\n", id)
    		publishedCount++
    	}
    
    	fmt.Fprintf(w, "Published %d messages with batch settings\n", publishedCount)
    	return publisher.Error()
    }
    

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.[batching](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Callables.html#com_google_api_gax_rpc_Callables__RequestT_ResponseT_batching_com_google_api_gax_rpc_UnaryCallable_RequestT_ResponseT__com_google_api_gax_rpc_BatchingCallSettings_RequestT_ResponseT__com_google_api_gax_rpc_ClientContext_).[BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.html);
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
    import org.threeten.bp.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    
    public class PublishWithBatchSettingsExample {
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
    
        publishWithBatchSettingsExample(
            cloudRegion, zoneId, projectNumber, topicId, messageCount, regional);
      }
    
      // Publish messages to a topic with batch settings.
      public static void publishWithBatchSettingsExample(
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
          // Batch settings control how the publisher batches messages
          long requestBytesThreshold = 5000L; // default : 3_500_000 bytes
          long messageCountBatchSize = 100L; // default : 1000L message
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) publishDelayThreshold = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofMillis(100); // default : 50 ms
    
          // Publish request get triggered based on request size, messages count & time since last
          // publish, whichever condition is met first.
          [BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.html) batchingSettings =
              [BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.html).newBuilder()
                  .[setRequestByteThreshold](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.Builder.html#com_google_api_gax_batching_BatchingSettings_Builder_setRequestByteThreshold_java_lang_Long_)(requestBytesThreshold)
                  .[setElementCountThreshold](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.Builder.html#com_google_api_gax_batching_BatchingSettings_Builder_setElementCountThreshold_java_lang_Long_)(messageCountBatchSize)
                  .[setDelayThreshold](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.Builder.html#com_google_api_gax_batching_BatchingSettings_Builder_setDelayThreshold_org_threeten_bp_Duration_)(publishDelayThreshold)
                  .build();
    
          [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html) publisherSettings =
              [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html).newBuilder()
                  .setTopicPath(topicPath)
                  .setBatchingSettings(batchingSettings)
                  .build();
    
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html).create(publisherSettings);
    
          // Start the publisher. Upon successful starting, its state will become RUNNING.
          publisher.startAsync().awaitRunning();
    
          for (int i = 0; i < messageCount; i++) {
            String message = "message-" + i;
    
            // Convert the message to a byte string.
            [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
            [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().setData(data).build();
    
            // Publish a message.
            ApiFuture<String> future = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)(pubsubMessage);
            futures.add(future);
          }
        } finally {
          ArrayList<MessageMetadata> metadata = new ArrayList<>();
          List<String> ackIds = [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[allAsList](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_allAsList_java_lang_Iterable___extends_com_google_api_core_ApiFuture___extends_V___)(futures).get();
          System.out.println("Published " + ackIds.size() + " messages with batch settings.");
    
          if (publisher != null) {
            // Shut down the publisher.
            publisher.stopAsync().awaitTerminated();
          }
        }
      }
    }

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.pubsub_v1.types import BatchSettings
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
    batch_setttings = BatchSettings(
        # 2 MiB. Default to 3 MiB. Must be less than 4 MiB gRPC's per-message limit.
        max_bytes=2 * 1024 * 1024,
        # 100 ms. Default to 50 ms.
        max_latency=0.1,
        # Default to 1000.
        max_messages=100,
    )
    
    # PublisherClient() must be used in a `with` block or have __enter__() called before use.
    with PublisherClient(
        per_partition_batching_settings=batch_setttings
    ) as publisher_client:
        for message in range(num_messages):
            data = f"{message}"
            api_future = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).publish(topic_path, data.encode("utf-8"))
            # result() blocks. To resolve API futures asynchronously, use add_done_callback().
            message_id = api_future.result()
            message_metadata = MessageMetadata.decode(message_id)
            print(
                f"Published {data} to partition {message_metadata.partition.value} and offset {message_metadata.cursor.offset}."
            )
    
    print(
        f"Finished publishing {num_messages} messages with batch settings to {str(topic_path)}."
    )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
