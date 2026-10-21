---
url: https://docs.cloud.google.com/pubsub/lite/docs/topics/
title: Create and manage Lite topics \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:08.950515+00:00
---

# Create and manage Lite topics  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/topics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Create and manage Lite topics Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document explains how to create, view, and delete a Pub/Sub Lite topic.

**Key Point:** Understand the properties of a **Lite topic** and the differences between a **regional Lite** and a **zonal Lite** topic. Create, edit, list, or delete a Lite topic by using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

## Overview of a Lite topic

A Pub/Sub Lite service requires a topic to which publishers can send messages so that subscribers can receive those messages. Within Pub/Sub Lite, you can choose to create a zonal or regional Lite topic.

A zonal Lite and a regional Lite topic differ only in the way they replicate data. All other topic properties are the same as described in a later section of this document.

### Data replication in a Lite topic

Pub/Sub Lite regional topics store data in two zones of a single region. Pub/Sub Lite zonal topics replicate data within just one zone. Pub/Sub Lite replicates data asynchronously. 

The availability of Pub/Sub Lite depends on the availability of its underlying components, which include both the application frontend and storage.

The availability of a Pub/Sub Lite **zonal** topic depends on the availability of both the application frontend and storage in its configured zone. If the application frontend or storage experiences a zonal failure, the zonal Lite topic becomes unavailable for the duration of the outage.

The availability of a Pub/Sub Lite **regional** topic depends on the availability of the application frontend and storage in its configured region. The following types of failure are possible:

  * If the application frontend **or** storage experiences a zonal failure, the regional Lite topic remains available.

  * If both the application frontend and storage experience a zonal failure, the regional Lite topic remains available as long as both the components don't start failing at the same time.

  * If both the application frontend and storage fail simultaneously, the regional Lite topic remains unavailable for the duration of the outage. During this time, clients may fail to publish or consume messages, but messages are still delivered in the right order.




A regional Lite topic provides protection from most types of single-zone failures. However in some rare cases, the asynchronous nature of replication may cause a simultaneous failure of multiple components in a single zone. As a result, a regional Lite topic becomes unavailable.

### Properties of a Lite topic

Lite topics have the following properties:

  * **Number of partitions.** A partition is the basic unit of parallelism in Pub/Sub Lite. A Lite topic can have one or more partitions.

  * **Capacity of a partition.** The capacity of a partition is described by the following three properties:

    * **Publish throughput (MiBps).** The maximum rate at which you can publish messages.

    * **Subscribe throughput (MiBps).** The maximum rate at which messages are forwarded to Lite subscriptions.

    * **Storage (GiB).** The maximum size of the messages in the partition. The minimum configurable capacity of a partition is 30 GiB.

  * **Storage capacity of a Lite topic.** All the partitions in a Lite topic have the same configured storage capacity. The total storage capacity of a Lite topic is the sum of the storage capacity of all the partitions in the topic. For example, if a Lite topic has 8 partitions and each partition is of size 30 GiB, the total storage capacity of the Lite topic is 240 GiB (8 x 30).

  * **Throughput capacity of a Lite topic.** Throughput capacity consists of the total publish and subscribe throughput capacity of all the partitions in the Lite topic. Even if you have a topic that, in aggregate, can support 1 GiBps of publish throughput, it is the per-partition publish limit that effectively limits throughput.

  * **Limit of subscriber client and subscriptions.** Pub/Sub Lite supports a single subscriber client for a single partition and a single subscription. For example, a subscription to a topic with 5 partitions can have, at most, 5 subscriber clients that consume messages from it. If more subscriber clients are configured, the excess clients remain idle. The same topic with 2 subscriptions can have up to 10 subscriber clients, 5 clients for each subscription.

  * **Reservations.** A reservation is the easiest way to provision and manage throughput capacity for a number of topics. Provisioning throughput capacity with reservations is _required_ for regional Lite and is _optional_ for zonal Lite topics.

If you do not use reservations for a zonal Lite topic, you must explicitly provision the publish and subscribe throughput capacity of the topic. Without a reservation, all the partitions in a Lite topic have the same configured throughput capacity. To know more, see [Configure throughput capacity without reservations](https://docs.cloud.google.com/pubsub/lite/docs/reservations#configure_throughput_capacity_without_reservations).


**Note:** You might be able to publish messages to your zonal "Lite topics" using gcloud publish commands by not configuring the reservation parameter to the "Lite topics". When using API and especially using client publishers and consumers, the reservation parameter is required.

  * **Storage configuration.** To configure storage, you must specify both the storage capacity and optionally, the message retention period.

    * **Message retention period.** The maximum amount of time for which a Lite topic stores messages. If you don't specify a message retention period, the Lite topic stores messages until you exceed the storage capacity.

    * **Storage capacity.** The Pub/Sub Lite topic capacity is determined by the number of partitions in the topic and the storage capacity of each partition. Storage per partition is the amount of storage, in bytes, for each partition. Note that regional Lite topics use two bytes of storage capacity for each byte published. Zonal Lite topics use one byte of storage capacity for each byte published.

If you exceed the storage capacity, the Pub/Sub Lite service continues to publish messages. However, in order to create more storage capacity, the oldest messages from the partition are deleted. The deletion of the oldest messages occurs even if the messages are within the message retention period. The service never deletes messages before their TTL expires, unless their removal is necessary to make space for newly published messages. For information about how capacity relates to pricing, see [Pub/Sub Lite pricing](https://cloud.google.com/pubsub/pricing#lite).




## Guidelines to name a topic

A Pub/Sub Lite resource name uniquely identifies a Pub/Sub Lite resource, such as a topic, subscription, or reservation. The resource name must fit the following format:

`projects/project-identifier/collection/ID`

  * `project-identifier`: Must be the project ID or project number, available from the Google Cloud console. For example, `my-cool-project` is a project ID. `123456789123` is a project number.

  * `collection`: Must be one of `topics`, `subscriptions`, or `reservations`.

  * `ID`: Must conform to the following guidelines:

    * Not begin with the string `goog`
    * Start with a letter
    * Contain between 3 and 255 characters
    * Contain only the following characters: Letters `[A-Za-z]`, numbers `[0-9]`, dashes `-`, underscores `_`, periods `.`, tildes `~`, plus signs `+`, and percent signs `%`

You can use the special characters in the preceding list in resource names without URL-encoding. However, you must ensure that any other special characters are properly encoded or decoded when you use them in URLs. For example, `mi-tópico` is an invalid _ID_. However, `mi-t%C3%B3pico` is valid. This format is important when you make REST calls.




**Note:** The [ client libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries) can take different approaches to naming resources, such as specifying the _project-identifier_ and the _ID_ in separate fields.

## Increase throughput capacity of a Lite topic

If you don't use Lite reservations, you can set the throughput capacity of each partition of any zonal Lite topic to a value set by the following limits:

  * Publish throughput between 4 and 16 MiBps

  * Subscribe throughput between 4 and 32 MiBps




These limits also apply to partitions associated with a Lite reservation. With reservations, each partition can consume any throughput capacity within the specified limits, as long as the total capacity of the reservation is not exceeded. Optionally, you can set a lower limit on the actual throughput per partition to make your traffic more predictable.

You can increase the number of partitions in a topic to scale it horizontally. The number of partitions in a topic cannot be decreased.

When you change the number of partitions, the relative order of messages is not preserved. Internally, messages are assigned to partitions using a hash function. Updating the number of partitions in a topic changes this hash function. Messages with the same key published after the partition count update are likely to be mapped to a different partition than those published before the update.

Additionally, the topic resize takes a few seconds to propagate to all the publishers. There is a short time when some publishers use the new hash function and some are still using the old one.

## Increase storage capacity of a Lite topic

You can increase or decrease the amount of storage in a Lite topic. The Lite topic provisions the same amount of storage to each partition. If you increase the storage to 60 GiB, each of the partitions gets 60 GiB of storage.

If you decrease the amount of storage in a Lite topic, the Pub/Sub Lite service removes the oldest messages first.

For information about how capacity relates to pricing, see [Pub/Sub Lite pricing](https://docs.cloud.google.com/pubsub/lite/pricing)

## Create a Lite topic

You can create Lite topics with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

For a list of the available regions and zones, see [Pub/Sub Lite locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).

### Console

  1. Go to the **Lite Topics** page.

[Go to Lite Topics](https://console.cloud.google.com/cloudpubsub/liteTopic)

  2. Click **Create Lite topic**.

     1. To create a zonal Lite topic, select a region and a zone within the region.

     2. To create a regional Lite topic, select a region.

You cannot update the location after a topic is created.

  3. In the **Name** section, enter a **Lite topic ID**.

The Lite topic name includes the Lite topic ID, the location, and the project number.

  4. In the **Throughput** section:

     1. Select or create a [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations).

This is _optional_ for a zonal Lite topic and _required_ for a regional Lite topic.

     2. Enter the peak publish throughput and the peak subscribe throughput.

A number of partitions are set automatically based on your inputs. You can edit this number after you save the topic.

  5. In the **Message storage** section:

     1. Enter the storage per partition.

     2. Select one of the two options for the message retention period.

  6. Review the changes and click **Create**.




### gcloud

To create a Lite topic, use the [`gcloud pubsub lite-topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create) command:
    
    
    gcloud pubsub lite-topics create TOPIC_ID \
      --location=LOCATION \
      --partitions=NUMBER_OF_PARTITIONS \
      --per-partition-bytes=STORAGE_PER_PARTITION \
      [--throughput-reservation=RESERVATION_NAME \]
      [--message-retention-period=MESSAGE_RETENTION_PERIOD]

Replace the following:

  * TOPIC_ID: the ID of the Lite topic

  * LOCATION: the name of [a location that Pub/Sub Lite supports](https://docs.cloud.google.com/pubsub/lite/docs/locations)

  * NUMBER_OF_PARTITIONS: an integer for the number of partitions in the Lite topic

  * STORAGE_PER_PARTITION: the amount of storage for each partition, such as `30GiB`

  * RESERVATION_NAME: the fully qualified path of a Lite [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations) such as `projects/123456789/locations/us-west1/reservations/my-reservation`

  * MESSAGE_RETENTION_PERIOD: the amount of time the Lite topic stores messages, such as `1d` or `2w`




If the request is successful, the command line displays a confirmation:
    
    
    Created [TOPIC_ID].
    

### Protocol

To create a Lite topic, send a `POST` request like the following:
    
    
    POST https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region to store the Lite topic in

  * PROJECT_NUMBER: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project to create the Lite topic in

  * LOCATION: the name of [a location that Pub/Sub Lite supports](https://docs.cloud.google.com/pubsub/lite/docs/locations)

  * TOPIC_ID: the ID of the Lite topic




Specify the following fields in the request body:
    
    
    {
      "partitionConfig": {
           "count": NUMBER_OF_PARTITIONS,
           "capacity": {
             "publishMibPerSec": publish_CAPACITY,
             "subscribeMibPerSec": subscribe_CAPACITY,
           }
      },
      "retentionConfig": {
           "perPartitionBytes": STORAGE_PER_PARTITION,
           "period": MESSAGE_RETENTION_PERIOD,
      },
      "reservationConfig": {
           "throughputReservation": RESERVATION_NAME
      }
    }

Replace the following:

  * NUMBER_OF_PARTITIONS: an integer for the number of partitions in the Lite topic

  * STORAGE_PER_PARTITION: the amount of storage for each partition, such as `30GiB`

  * publish_CAPACITY: an integer for the publish throughput capacity of each partition

  * subscribe_CAPACITY: an integer for the subscribe throughput capacity of each partition

  * MESSAGE_RETENTION_PERIOD: the amount of time the Lite topic stores messages, such as `1d` or `2w`

  * RESERVATION_NAME: the fully qualified path of a Lite [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations) such as `projects/123456789/locations/us-west1/reservations/my-reservation`




If the request is successful, the response is the Lite topic in JSON format:
    
    
    {
      "name": projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID,
      "partitionConfig": {
           "count": NUMBER_OF_PARTITIONS,
           "capacity": {
             "publishMibPerSec": publish_CAPACITY,
             "subscribeMibPerSec": subscribe_CAPACITY,
           }
      },
      "retentionConfig": {
           "perPartitionBytes": STORAGE_PER_PARTITION,
           "period": MESSAGE_RETENTION_PERIOD,
      },
      "reservationConfig": {
           "throughputReservation": RESERVATION_NAME
      }
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
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

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
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

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
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

After creating the Lite topic, you can scale the per-partition throughput and storage capacity. You can also increase, but not decrease the number of partitions.

## Update a Lite topic

You can update the following properties of a Lite topic:

  * The reservation associated with the Lite topic

  * The number of partitions in the topic (can only be increased)

  * The publish and subscribe throughput capacity limits

  * The storage per partition

  * The type of message retention




Before you scale either the throughput capacity or the storage capacity of a topic, refer to [Scale throughput capacity](https://docs.cloud.google.com/pubsub/lite/docs/topics#throughput) and [Scale storage capacity](https://docs.cloud.google.com/pubsub/lite/docs/topics#storage).

You can update a Lite topic with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Topics** page.

[Go to Lite Topics](https://console.cloud.google.com/cloudpubsub/liteTopic)

  2. Click the Lite topic ID.

  3. Click **Edit**.

  4. You can make any or all the following updates:

     * Use a different reservation. For zonal topics, you can opt to not use a reservation.
     * Enter the number of partitions. This value can be increased but not decreased.
     * Enable or disable the maximum allowed publish and subscribe throughput.
     * For zonal topics, update the reserved publish and subscribe throughput. For topics with a reservation attached, the updated throughput reflects the new maximum limit.
     * Edit the storage capacity per partition.
     * Edit the message retention period.
  5. Click **Update**.




### gcloud

To update a Lite topic, use the [`gcloud pubsub lite-topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update) command:
    
    
    gcloud pubsub lite-topics update TOPIC_ID \
      --location=LOCATION \
      --partitions=NUMBER_OF_PARTITIONS \
      --per-partition-publish-mib=publish_CAPACITY \
      --per-partition-subscribe-mib=subscribe_CAPACITY \
      --per-partition-bytes=STORAGE_PER_PARTITION \
      --message-retention-period=MESSAGE_RETENTION_PERIOD

Replace the following:

  * TOPIC_ID: the ID of the Lite topic

  * LOCATION: the name of the location that the Lite topic is in

  * NUMBER_OF_PARTITIONS: the number of partitions to configure for the Lite topic.

  * publish_CAPACITY: an integer for the publish throughput capacity of each partition

  * subscribe_CAPACITY: an integer for the subscribe throughput capacity of each partition

  * STORAGE_PER_PARTITION: the amount of storage for each partition, such as `30GiB`

  * MESSAGE_RETENTION_PERIOD: the amount of time the Lite topic stores messages, such as `1d` or `2w`




If the request is successful, the command line displays the Lite topic:
    
    
    name: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    partitionConfig:
      count: NUMBER_OF_PARTITIONS
      capacity:
        publishMibPerSec: publish_CAPACITY
        subscribeMibPerSec: subscribe_CAPACITY
    retentionConfig:
      perPartitionBytes: STORAGE_PER_PARTITION
      period: MESSAGE_RETENTION_PERIOD
    

### Protocol

To update a Lite topic, send a `PATCH` request like the following:
    
    
    PATCH https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID?updateMask=partitionConfig.capacity,retentionConfig.perPartitionBytes,retentionConfig.period,partitionConfig.count
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region that the Lite topic is in

  * PROJECT_NUMBER: the project number of the project with the Lite topic

  * LOCATION: the name of the location that the Lite topic is in

  * TOPIC_ID: the ID of the Lite topic




Specify the following fields in the request body:
    
    
    {
      "partitionConfig": {
          "count": NUMBER_OF_PARTITIONS,
          "capacity": {
             "publishMibPerSec": publish_CAPACITY,
             "subscribeMibPerSec": subscribe_CAPACITY,
          }
       },
       "retentionConfig": {
           "perPartitionBytes": STORAGE_PER_PARTITION,
           "period": MESSAGE_RETENTION_PERIOD,
       },
    }

Replace the following:

  * publish_CAPACITY: an integer for the publish throughput capacity of each partition

  * subscribe_CAPACITY: an integer for the subscribe throughput capacity of each partition

  * STORAGE_PER_PARTITION: the amount of storage for each partition, such as `30GiB`

  * MESSAGE_RETENTION_PERIOD: the amount of time the Lite topic stores messages, such as `1d` or `2w`

  * NUMBER_OF_PARTITIONS: the number of partitions to configure for the Lite topic.




If the request is successful, the response is the Lite topic in JSON format:
    
    
    {
      "name": projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID,
      "partitionConfig": {
          "count": NUMBER_OF_PARTITIONS,
          "capacity": {
             "publishMibPerSec": publish_CAPACITY,
             "subscribeMibPerSec": subscribe_CAPACITY,
          }
       },
       "retentionConfig": {
           "perPartitionBytes": STORAGE_PER_PARTITION,
           "period": MESSAGE_RETENTION_PERIOD,
       },
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func updateTopic(w io.Writer, projectID, region, location, topicID, reservation string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
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
    
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, location, topicID)
    	// For ranges of fields in TopicConfigToUpdate, see https://pkg.go.dev/cloud.google.com/go/pubsublite/#TopicConfigToUpdate
    	config := pubsublite.[TopicConfigToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_TopicConfigToUpdate){
    		Name:                       topicPath,
    		PartitionCount:             3, // Partition count cannot decrease.
    		PublishCapacityMiBPerSec:   8,
    		SubscribeCapacityMiBPerSec: 16,
    		PerPartitionBytes:          60 * 1024 * 1024 * 1024,
    		RetentionDuration:          24 * time.Hour,
    		ThroughputReservation:      reservation,
    	}
    	updatedCfg, err := client.UpdateTopic(ctx, config)
    	if err != nil {
    		return fmt.Errorf("client.UpdateTopic got err: %w", err)
    	}
    	fmt.Fprintf(w, "Updated topic: %v\n", updatedCfg)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
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
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[Durations](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Durations.html);
    import java.util.Arrays;
    import java.util.concurrent.ExecutionException;
    
    public class UpdateTopicExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        String topicId = "your-topic-id";
        String reservationId = "your-reservation-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = true;
    
        updateTopicExample(cloudRegion, zoneId, projectNumber, topicId, reservationId, regional);
      }
    
      public static void updateTopicExample(
          String cloudRegion,
          char zoneId,
          long projectNumber,
          String topicId,
          String reservationId,
          boolean regional)
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
    
        [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html) reservationPath =
            [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion))
                .setName([ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html).of(reservationId))
                .build();
    
        Iterable<String> iterablePaths =
            Arrays.asList(
                "partition_config.scale",
                "retention_config.per_partition_bytes",
                "retention_config.period",
                "reservation_config.throughput_reservation");
    
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(iterablePaths).build();
    
        [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html) topic =
            [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html).newBuilder()
                .setPartitionConfig(
                    PartitionConfig.newBuilder()
                        .setCapacity(
                            Capacity.newBuilder()
                                .setPublishMibPerSec(16)
                                .setSubscribeMibPerSec(32)
                                .build())
                        .build())
                .setRetentionConfig(
                    RetentionConfig.newBuilder()
                        // Set storage per partition to 32 GiB. This must be 30 GiB-10 TiB.
                        // If the number of bytes stored in any of the topic's partitions grows
                        // beyond this value, older messages will be dropped to make room for
                        // newer ones, regardless of the value of `period`.
                        // Be careful when decreasing storage per partition as it may cause
                        // lost messages.
                        .setPerPartitionBytes(32 * 1024 * 1024 * 1024L)
                        .setPeriod([Durations](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Durations.html).fromDays(7)))
                .setReservationConfig(
                    ReservationConfig.newBuilder()
                        .setThroughputReservation(reservationPath.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html#com_google_cloud_pubsublite_ReservationPath_toString__)())
                        .build())
                .setName([topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)())
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html) topicBeforeUpdate = adminClient.getTopic(topicPath).get();
          System.out.println("Before update: " + topicBeforeUpdate.getAllFields());
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html) topicAfterUpdate = adminClient.updateTopic(topic, fieldMask).get();
          System.out.println("After update: " + topicAfterUpdate.getAllFields());
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

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html), Topic
    from google.cloud.pubsublite.types import (
        [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html),
        [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html),
        [ReservationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.ReservationPath.html),
        [TopicPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.TopicPath.html),
    )
    from google.protobuf.duration_pb2 import Duration
    from google.protobuf.field_mask_pb2 import FieldMask
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # reservation_id = "your-reservation-id"
    # regional = True
    
    location = None
    if regional:
        #  A region.
        location = CloudRegion(cloud_region)
    else:
        #  A zone.
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    topic_path = TopicPath(project_number, location, topic_id)
    reservation_path = ReservationPath(project_number, cloud_region, reservation_id)
    
    # Defines which topic fields to update.
    field_mask = FieldMask(
        paths=[
            "partition_config.capacity",
            "retention_config.per_partition_bytes",
            "retention_config.period",
            "reservation_confing.throughput_reservation",
        ]
    )
    
    # Defines how to update the topic fields.
    topic = Topic(
        name=str(topic_path),
        partition_config=Topic.PartitionConfig(
            capacity=Topic.PartitionConfig.Capacity(
                publish_mib_per_sec=16,
                subscribe_mib_per_sec=32,
            )
        ),
        retention_config=Topic.RetentionConfig(
            # Set storage per partition to 32 GiB. This must be in the range 30 GiB-10TiB.
            # If the number of byptes stored in any of the topic's partitions grows beyond
            # this value, older messages will be dropped to make room for newer ones,
            # regardless of the value of `period`.
            # Be careful when decreasing storage per partition as it may cuase lost messages.
            per_partition_bytes=32 * 1024 * 1024 * 1024,
            # Allow messages to be stored for 14 days.
            period=Duration(seconds=60 * 60 * 24 * 14),
        ),
        reservation_config=Topic.ReservationConfig(
            throughput_reservation=str(reservation_path),
        ),
    )
    
    client = AdminClient(cloud_region)
    try:
        response = client.[update_topic](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_update_topic)(topic, field_mask)
        print(f"{response.name} updated successfully.")
    except NotFound:
        print(f"{topic_path} not found.")

## View Lite topic details

You can get details about a Lite topic using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Topics** page.

[Go to Lite Topics](https://console.cloud.google.com/cloudpubsub/liteTopic)

  2. Click the Lite topic ID.




### gcloud

To get details about a Lite topic, use the [`gcloud pubsub lite-topics describe`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/describe) command:
    
    
    gcloud pubsub lite-topics describe TOPIC_ID \
    --location=LOCATION

Replace the following:

  * TOPIC_ID: the ID of the Lite topic

  * LOCATION: the name of the location that the Lite topic is in




If the request is successful, the command line displays the Lite topic:
    
    
    name: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    partitionConfig:
      count: NUMBER_OF_PARTITIONS
      capacity:
        publishMibPerSec: publish_CAPACITY
        subscribeMibPerSec: subscribe_CAPACITY
    retentionConfig:
      perPartitionBytes: STORAGE_PER_PARTITION
      period: MESSAGE_RETENTION_PERIOD
    

### Protocol

To get details about a Lite topic, send a `GET` request like the following:
    
    
    GET https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region that the Lite topic is in

  * PROJECT_NUMBER: the project number of the project with the Lite topic

  * LOCATION: the name of the location that the Lite topic is in

  * TOPIC_ID: the ID of the Lite topic




If the request is successful, the response is the Lite topic in JSON format:
    
    
    {
      "name": projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID,
      "partitionConfig": {
          "count": NUMBER_OF_PARTITIONS,
          "capacity": {
             "publishMibPerSec": publish_CAPACITY,
             "subscribeMibPerSec": subscribe_CAPACITY,
          }
       },
       "retentionConfig": {
           "perPartitionBytes": STORAGE_PER_PARTITION,
           "period": MESSAGE_RETENTION_PERIOD,
       },
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
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

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
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

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
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

## List Lite topics

You can list Lite topics in a project using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  * To view a list of the Lite topics in a project, go to the **Lite Topics** page.

[Go to Lite Topics](https://console.cloud.google.com/cloudpubsub/liteTopic)




### gcloud

  * To list the Lite topics in a project, use the [`gcloud pubsub lite-topics list`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list) command:


    
    
    gcloud pubsub lite-topics list \
      --location=LOCATION

Replace LOCATION with the name of the location that the Lite topic is in.

If the request is successful, the command line displays the Lite topics:
    
    
    ---
    name: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    partitionConfig:
      count: NUMBER_OF_PARTITIONS
      capacity:
        publishMibPerSec: publish_CAPACITY
        subscribeMibPerSec: subscribe_CAPACITY
    retentionConfig:
      perPartitionBytes: STORAGE_PER_PARTITION
      period: MESSAGE_RETENTION_PERIOND
    ---
    name: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    partitionConfig:
      count: NUMBER_OF_PARTITIONS
      capacity:
        publishMibPerSec: publish_CAPACITY
        subscribeMibPerSec: subscribe_CAPACITY
    retentionConfig:
      perPartitionBytes: STORAGE_PER_PARTITION
      period: MESSAGE_RETENTION_PERIOND
    

### Protocol

To list the Lite topics in a project, send a `GET` request like the following:
    
    
    GET https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/topics
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region that the Lite topic is in

  * PROJECT_NUMBER: the project number of the project with the Lite topic




If the request is successful, the response is a list of Lite topics in JSON format:
    
    
    {
      "topics": [
          {
              "name": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
          },
          {
              "name": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
          }
      ]
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    	"google.golang.org/api/iterator"
    )
    
    func listTopics(w io.Writer, projectID, region, zone string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// zone := "us-central1-a"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, zone)
    	topicIter := client.[Topics](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_AdminClient_Topics)(ctx, parent)
    	for {
    		topic, err := topicIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("topicIter.Next got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got topic: %#v\n", topic)
    	}
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.proto.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html);
    import java.util.List;
    
    public class ListTopicsExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = true;
    
        listTopicsExample(cloudRegion, zoneId, projectNumber, regional);
      }
    
      public static void listTopicsExample(
          String cloudRegion, char zoneId, long projectNumber, boolean regional) throws Exception {
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html) locationPath =
            [LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation(location)
                .build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          List<Topic> topics = adminClient.listTopics(locationPath).get();
          for ([Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic.html) topic : topics) {
            System.out.println(topic.getAllFields());
          }
          System.out.println(topics.size() + " topic(s) listed.");
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [LocationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.LocationPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # regional = True
    
    location = None
    if regional:
        #  A region.
        location = CloudRegion(cloud_region)
    else:
        #  A zone.
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    location_path = LocationPath(project_number, location)
    
    client = AdminClient(cloud_region)
    response = client.[list_topics](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_list_topics)(location_path)
    
    for topic in response:
        print(topic)
    
    print(f"{len(response)} topic(s) listed in your project and location.")

## Delete a Lite topic

You can delete Lite topics with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

**Caution:** Deletion is permanent. Once deleted, topics cannot be restored.

### Console

  1. Go to the **Lite Topics** page.

[Go to Lite Topics](https://console.cloud.google.com/cloudpubsub/liteTopic)

  2. Click the Lite topic ID.

  3. In the **Lite topic details** page, click **Delete**.

  4. In the field that appears, enter `delete` to confirm that you want to delete the Lite topic.

  5. Click **Delete**.




### gcloud

To delete a Lite topic, use the [`gcloud pubsub lite-topics delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/delete) command:

  1. Run the `delete` command:
         
         gcloud pubsub lite-topics delete TOPIC_ID \
          --location=LOCATION

Replace the following:

     * TOPIC_ID: the ID of the Lite topic

     * LOCATION: the name of the location that the Lite topic is in

  2. To confirm, type `Y`.




If the request is successful, the response is the following:
    
    
    Deleted topic [TOPIC_ID].
    

### Protocol

To delete a Lite topic, send a `DELETE` request like the following:
    
    
    DELETE https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region that the Lite topic is in

  * PROJECT_NUMBER: the project number of the project with the Lite topic

  * LOCATION: the name of the location that the Lite topic is in

  * TOPIC_ID: the ID of the Lite topic




If the request is successful, the response is an empty JSON object.

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func deleteTopic(w io.Writer, projectID, region, location, topicID string) error {
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
    	err = client.DeleteTopic(ctx, topicPath)
    	if err != nil {
    		return fmt.Errorf("client.DeleteTopic got err: %w", err)
    	}
    	fmt.Fprint(w, "Deleted topic\n")
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import java.util.concurrent.ExecutionException;
    
    public class DeleteTopicExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing topic.
        String topicId = "your-topic-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        deleteTopicExample(cloudRegion, zoneId, projectNumber, topicId, regional);
      }
    
      public static void deleteTopicExample(
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
          adminClient.deleteTopic(topicPath).get();
          if (regional) {
            System.out.println([topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)() + " (regional topic) deleted successfully.");
          } else {
            System.out.println([topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)() + " (zonal topic) deleted successfully.");
          }
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

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [TopicPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.TopicPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # regional = True
    
    cloud_region = CloudRegion(cloud_region)
    topic_path = None
    if regional:
        #  A regional topic.
        topic_path = TopicPath(project_number, cloud_region, topic_id)
    else:
        #  A zonal topic
        topic_path = TopicPath(
            project_number, CloudZone(cloud_region, zone_id), topic_id
        )
    
    client = AdminClient(cloud_region)
    try:
        client.[delete_topic](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_delete_topic)(topic_path)
        if regional:
            print(f"{topic_path} (regional topic) deleted successfully.")
        else:
            print(f"{topic_path} (zonal topic) deleted successfully.")
    except NotFound:
        print(f"{topic_path} not found.")

If you delete a Lite topic, you can't publish messages to it. The Lite subscriptions to the Lite topic still exist, but you can't receive messages from the Lite subscriptions.

## What's Next

  * [Publish messages](https://docs.cloud.google.com/pubsub/lite/docs/publishing) to a Lite topic.
  * [Create a Lite subscription](https://docs.cloud.google.com/pubsub/lite/docs/subscriptions) to a Lite topic.
  * [Receive messages](https://docs.cloud.google.com/pubsub/lite/docs/subscribing) from a Lite subscription.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
