---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-get-topic/
title: Get Lite topic \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:54.897746+00:00
---

# Get Lite topic  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-get-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Get Lite topic Stay organized with collections  Save and categorize content based on your preferences. 

Print name, retention config, and partition config of a Lite topic.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage Lite topics](https://docs.cloud.google.com/pubsub/lite/docs/topics)



## Code sample

### Go

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func getTopic(w io.Writer, projectID, region, location, topicID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, location, topicID)
    	topic, err := client.Topic(ctx, topicPath)
    	if err != nil {
    		return fmt.Errorf("client.Topic got err: %w", err)
    	}
    	fmt.Fprintf(w, "Got topic: %#v\n", *topic)
    	return nil
    }
    

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.proto.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html);
    import java.util.concurrent.ExecutionException;
    
    public class GetTopicExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing topic.
        String topicId = "your-topic-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = true;
    
        getTopicExample(cloudRegion, zoneId, projectNumber, topicId, regional);
      }
    
      public static void getTopicExample(
          String cloudRegion, char zoneId, long projectNumber, String topicId, boolean regional)
          throws Exception {
    
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
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html) topic = adminClient.getTopic(topicPath).get();
          long numPartitions = adminClient.getTopicPartitionCount(topicPath).get();
          System.out.println(topic.getAllFields() + "\nhas " + numPartitions + " partition(s).");
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) notFound) {
            System.out.println("This topic is not found.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [TopicPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.TopicPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # regional = True
    
    location = None
    if regional:
        #  A region.
        location = CloudRegion(cloud_region)
    else:
        #  A zone.
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    topic_path = TopicPath(project_number, location, topic_id)
    
    client = AdminClient(cloud_region)
    try:
        response = client.[get_topic](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_get_topic)(topic_path)
        num_partitions = client.[get_topic_partition_count](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_get_topic_partition_count)(topic_path)
        print(f"{response.name} has {num_partitions} partition(s).")
    except NotFound:
        print(f"{topic_path} not found.")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
