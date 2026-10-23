---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-create-topic/
title: Create Lite topic \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:16.279372+00:00
---

# Create Lite topic  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-create-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Create Lite topic Stay organized with collections  Save and categorize content based on your preferences. 

Create a single-partition Lite topic and configure its retention period, per partition storage, and publishing throughput scaling factor. 

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
    
    func createTopic(w io.Writer, projectID, region, location, topicID, reservation string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1" // see https://cloud.google.com/pubsub/lite/docs/locations
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	// topicID := "my-topic"
    	// reservation := "projects/my-project-id/reservations/my-reservation"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	const gib = 1 << 30
    
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, location, topicID)
    	// For ranges of fields in TopicConfig, see https://pkg.go.dev/cloud.google.com/go/pubsublite/#TopicConfig
    	topic, err := client.CreateTopic(ctx, pubsublite.[TopicConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_TopicConfig){
    		Name:                       topicPath,
    		PartitionCount:             2, // Must be >= 1 and cannot decrease after creation.
    		PublishCapacityMiBPerSec:   4,
    		SubscribeCapacityMiBPerSec: 8,
    		PerPartitionBytes:          30 * gib,
    		RetentionDuration:          pubsublite.[InfiniteRetention](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_InfiniteRetention),
    		ThroughputReservation:      reservation,
    	})
    	if err != nil {
    		return fmt.Errorf("client.CreateTopic got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic: %#v\n", topic)
    	return nil
    }
    

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html);
    import com.google.cloud.pubsublite.[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.proto.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html);
    import com.google.cloud.pubsublite.proto.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html).PartitionConfig;
    import com.google.cloud.pubsublite.proto.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html).PartitionConfig.Capacity;
    import com.google.cloud.pubsublite.proto.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html).ReservationConfig;
    import com.google.cloud.pubsublite.proto.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html).RetentionConfig;
    import com.google.protobuf.util.[Durations](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Durations.html);
    import java.util.concurrent.ExecutionException;
    
    public class CreateTopicExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'a';
        String topicId = "your-topic-id";
        String reservationId = "your-reservation-id";
        long projectNumber = Long.parseLong("123456789");
        int partitions = 1;
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        createTopicExample(
            cloudRegion, zoneId, projectNumber, topicId, reservationId, partitions, regional);
      }
    
      public static void createTopicExample(
          String cloudRegion,
          char zoneId,
          long projectNumber,
          String topicId,
          String reservationId,
          int partitions,
          boolean regional)
          throws Exception {
    
        [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html) reservationPath =
            [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion))
                .setName([ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html).of(reservationId))
                .build();
    
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
    
        [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html) topic =
            [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html).newBuilder()
                .setPartitionConfig(
                    PartitionConfig.newBuilder()
                        // Set throughput capacity per partition in MiB/s.
                        .setCapacity(
                            Capacity.newBuilder()
                                // Must be 4-16 MiB/s.
                                .setPublishMibPerSec(4)
                                // Must be 4-32 MiB/s.
                                .setSubscribeMibPerSec(8)
                                .build())
                        .setCount(partitions))
                .setRetentionConfig(
                    RetentionConfig.newBuilder()
                        // How long messages are retained.
                        .setPeriod([Durations](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Durations.html).[fromDays](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Durations.html#com_google_protobuf_util_Durations_fromDays_long_)(1))
                        // Set storage per partition to 30 GiB. This must be 30 GiB-10 TiB.
                        // If the number of bytes stored in any of the topic's partitions grows
                        // beyond this value, older messages will be dropped to make room for
                        // newer ones, regardless of the value of `period`.
                        .setPerPartitionBytes(30 * 1024 * 1024 * 1024L))
                .setReservationConfig(
                    ReservationConfig.newBuilder()
                        .setThroughputReservation(reservationPath.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html#com_google_cloud_pubsublite_ReservationPath_toString__)())
                        .build())
                .setName([topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)())
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html) response = adminClient.createTopic(topic).get();
          if (regional) {
            System.out.println(response.getAllFields() + " (regional topic) created successfully.");
          } else {
            System.out.println(response.getAllFields() + " (zonal topic) created successfully.");
          }
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) alreadyExists) {
            System.out.println("This topic already exists.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html), Topic
    from google.cloud.pubsublite.types import (
        [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html),
        [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html),
        [ReservationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.ReservationPath.html),
        [TopicPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.TopicPath.html),
    )
    from google.protobuf.duration_pb2 import Duration
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # reservation_id = "your-reservation-id"
    # num_partitions = 1
    # regional = True
    
    cloud_region = CloudRegion(cloud_region)
    reservation_path = ReservationPath(project_number, cloud_region, reservation_id)
    
    topic_path = None
    if regional:
        #  A regional topic.
        topic_path = TopicPath(project_number, cloud_region, topic_id)
    else:
        #  A zonal topic
        topic_path = TopicPath(
            project_number, CloudZone(cloud_region, zone_id), topic_id
        )
    
    topic = Topic(
        name=str(topic_path),
        partition_config=Topic.PartitionConfig(
            # A topic must have at least one partition.
            count=num_partitions,
            # Set throughput capacity per partition in MiB/s.
            capacity=Topic.PartitionConfig.Capacity(
                # Set publish throughput capacity per partition to 4 MiB/s. Must be >= 4 and <= 16.
                publish_mib_per_sec=4,
                # Set subscribe throughput capacity per partition to 4 MiB/s. Must be >= 4 and <= 32.
                subscribe_mib_per_sec=8,
            ),
        ),
        retention_config=Topic.RetentionConfig(
            # Set storage per partition to 30 GiB. This must be in the range 30 GiB-10TiB.
            # If the number of byptes stored in any of the topic's partitions grows beyond
            # this value, older messages will be dropped to make room for newer ones,
            # regardless of the value of `period`.
            per_partition_bytes=30 * 1024 * 1024 * 1024,
            # Allow messages to be retained for 7 days.
            period=Duration(seconds=60 * 60 * 24 * 7),
        ),
        reservation_config=Topic.ReservationConfig(
            throughput_reservation=str(reservation_path),
        ),
    )
    
    client = AdminClient(cloud_region)
    try:
        response = client.[create_topic](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_create_topic)(topic)
        if regional:
            print(f"{response.name} (regional topic) created successfully.")
        else:
            print(f"{response.name} (zonal topic) created successfully.")
    except AlreadyExists:
        print(f"{topic_path} already exists.")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
