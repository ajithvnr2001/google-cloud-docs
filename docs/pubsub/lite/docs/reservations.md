---
url: https://docs.cloud.google.com/pubsub/lite/docs/reservations/
title: Create and manage Lite reservations \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:09.813176+00:00
---

# Create and manage Lite reservations  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Create and manage Lite reservations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document explains how to use and manage Pub/Sub Lite reservations. This document also explains the concept of capacity units and how to determine how many you require to accommodate the throughput of your application.

**Key Point:** Understand the terms **Lite reservations** and **capacity units**. Learn how to calculate capacity units for a Lite reservation. Create, edit, list, or delete a Lite reservation by using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

## Overview of Lite reservations

Lite reservations provision and dynamically share throughput capacity among one or multiple Lite topics in a region. These topics may be regional or zonal Lite topics. Using Lite reservations is a better option than setting the throughput capacity of individual Lite topics. With Lite reservations, you manage and monitor fewer resources. Also, you don't have to choose the throughput capacity of individual Lite topics.

To use a Lite reservation, you attach a Lite topic that is in the same region to the specific Lite reservation. You can attach a single Lite reservation to both zonal and regional Lite topics. All the partitions in a Lite topic that is attached to a Lite reservation dynamically consume from the throughput capacity provisioned in the Lite reservation. If you do specify a Lite reservation for a Lite topic, you can also include rate limits to limit the throughput capacity of each partition of the Lite topic.

## Overview of capacity units

The throughput capacity of a Lite reservation is provisioned in **capacity units**.

One capacity unit corresponds to the following throughput:

Lite topic type | Publish throughput in MiBps | Subscribe throughput in MiBps  
---|---|---  
Zonal | 1 | 2  
Regional | 0.25 | 0.5  
**Note:** Storage capacity must be configured for each individual Lite topic.

## Guidelines to name a reservation

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

## Guidelines for using a Lite reservation

Provisioning throughput with Lite reservations is _required_ for regional Lite topics and is _optional_ for zonal Lite topics. A Lite reservation is a regional resource.

Keep the following in mind when you are planning to configure a Lite reservation:

  * The number of capacity units needed for a Lite reservation must equal the peak throughput you expect in any given minute across all topics and subscriptions in that Lite reservation.

  * When the combined throughput of all the Lite topics in a Lite reservation reaches its capacity, publishing and delivery are throttled. The Pub/Sub Lite servers stop sending messages to the clients, and messages get buffered in the publisher client. You can set up an alert for `reservation/throughput_capacity/utilization` to let you know when the reservation is in danger of being throttled so that you can increase the reservation size.

  * You can update the throughput of the reservations as often as you like. Changes take effect in under a minute. However, if you decrease a reservation's throughput, you are continued to be charged for the higher amount for a 24-hour period. Pub/Sub Lite is inherently a pay-for-capacity system, where scale-ups are instantaneous and scale-downs are possible.

  * All Lite topics attached to a Lite reservation consume from the same pool of throughput capacity. It's therefore possible for a Lite topic to suddenly use a large amount of throughput capacity, starving other Lite topics and preventing them from publishing or receiving messages. If you require complete isolation across Lite topics, you can attach them to independent reservations.




### Impact of partitions on a Lite reservation

The total number of partitions across all Lite topics in a Lite reservation must be not greater than the number of capacity units reserved. For example, you cannot attach a Lite reservation of 10 capacity units to a Lite topic or a set of Lite topics whose total number of partitions is greater than 10.

### Calculate capacity units for a Lite reservation

The size of a Lite reservation is defined by the number of capacity units. The following examples illustrate how to estimate the capacity required for individual Lite topics.

**Note:** The sum of the throughput across multiple Lite topics usually has a lower peak than the sum of the peaks of the throughput of individual Lite topics. Since reservations deal with the sum of the throughput across multiple Lite topics, these are a cost effective way to manage throughput.

  1. Determine the peak publish throughput.

Estimate the peak in the throughput of all the Lite topics attached to the Lite reservation. A rough estimate for the throughput is sufficient since you can always update the size of the reservation.

  2. Determine the peak subscribe throughput.

The peak subscribe throughput is computed similarly to the peak publish throughput. However, consider that your subscribers don't necessarily need to receive messages at the peak rate of the publishers. If delays in processing are acceptable, Pub/Sub Lite allows you to buffer messages and process them at a steady rate. At the same time, you may want to have more subscribe capacity than publish capacity to accommodate the occasional downtime of subscribers.

  3. Determine the total number of capacity units required.

The table in the preceding section specifies the number of MiBps that a capacity unit can accommodate for different operations. The following is the formula to calculate the capacity units required for a sample Lite reservation:

     * Peak publish throughput of the zonal Lite topics = `Pz MiBps`
     * Peak publish throughput of the regional Lite topics = `Pr MiBps`
     * Peak subscribe throughput of the zonal Lite topics = `Sz MiBps`
     * Peak subscribe throughput of the regional Lite topics = `Sr MiBps`

Number of capacity units required = `(Pz / 1 MiBps) + (Pr/0.25 MiBps) + (Sz/2 MiBps) + (Sr/0.5 MiBps)`

If the number is not whole, you must round up the value.




## Configure throughput capacity without a Lite reservation

**Note:** This section applies to zonal Lite topics only.

  * **Topic publish throughput capacity** : You can specify 4 to 16 MiBps of throughput capacity, and the value must be an integer.

  * **Topic subscribe throughput capacity** : You can specify 4 to 32 MiBps of throughput capacity, and the value must be an integer.




For subscribe throughput, we recommend that you provision your throughput capacity to equal the product of your expected publish throughput and the number of subscriptions on your topic.

Publisher and subscriber capacity provisioned for an individual topic are not interchangeable. For this reason, we recommend always using reservations.

There are differences in billing when provisioning capacity directly for topics instead of using reservations. See the [Pub/Sub Lite pricing page](https://cloud.google.com/pubsub/pricing#lite) for details.

## Create a Lite reservation

A Lite reservation must be in the same project and region as any Lite topics that are attached to it. For a list of the available zones and regions, see [Pub/Sub Lite locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).

You can create a Lite reservation with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Reservations** page.

[Go to Lite Reservations](https://console.cloud.google.com/cloudpubsub/liteReservation)

  2. Click **Create Lite reservation**.

  3. Select a region.

  4. Enter a **Lite reservation ID**.

  5. Provision the amount of throughput capacity units.

  6. Click **Create**.




### gcloud

To create a Lite reservation, use the [`gcloud pubsub lite-reservations create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create) command:
    
    
    gcloud pubsub lite-reservations create myRes \
      --location=us-central1 \
      --throughput-capacity=INTEGER_NUMBER_OF_UNITS
    
    
    gcloud pubsub lite-topics create myTopic \
      --throughput-reservation=myRez \
      --zone=ZONE \
      --location=us-central1a \
      --partitions \
      --storage

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func createReservation(w io.Writer, projectID, region, reservationID string, throughputCapacity int) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// reservationID := "my-reservation"
    	// throughputCapacity := 4
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	reservationPath := fmt.Sprintf("projects/%s/locations/%s/reservations/%s", projectID, region, reservationID)
    	res, err := client.CreateReservation(ctx, pubsublite.[ReservationConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_ReservationConfig){
    		Name:               reservationPath,
    		ThroughputCapacity: throughputCapacity,
    	})
    	if err != nil {
    		return fmt.Errorf("client.CreateReservation got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created reservation: %s\n", res.Name)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html);
    import com.google.cloud.pubsublite.[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html);
    import com.google.cloud.pubsublite.proto.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html);
    import java.util.concurrent.ExecutionException;
    
    public class CreateReservationExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        long projectNumber = Long.parseLong("123456789");
        String cloudRegion = "your-cloud-region";
        String reservationId = "your-reservation-id";
        // Each unit of throughput capacity supports up to 1 MiB/s of published messages or
        // 2 MiB/s of subscribed messages.
        int throughputCapacity = 4;
    
        createReservationExample(projectNumber, cloudRegion, reservationId, throughputCapacity);
      }
    
      public static void createReservationExample(
          long projectNumber, String cloudRegion, String reservationId, int throughputCapacity)
          throws Exception {
    
        [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html) reservationPath =
            [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion))
                .setName([ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html).of(reservationId))
                .build();
    
        [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html) reservation =
            [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html).newBuilder()
                .setName(reservationPath.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html#com_google_cloud_pubsublite_ReservationPath_toString__)())
                .setThroughputCapacity(throughputCapacity)
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html) response = adminClient.createReservation(reservation).get();
          System.out.println(response.getAllFields() + " created successfully.");
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) alreadyExists) {
            System.out.println("This reservation already exists.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html), Reservation
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [ReservationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.ReservationPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # reservation_id = "your-reservation-id"
    # Each unit of throughput capacity supports up to 1 MiB/s of published messages
    # or 2 MiB/s of subscribed messages. Must be a positive integer.
    # throughput_capacity = 4
    
    cloud_region = CloudRegion(cloud_region)
    reservation_path = ReservationPath(project_number, cloud_region, reservation_id)
    
    reservation = Reservation(
        name=str(reservation_path),
        throughput_capacity=throughput_capacity,
    )
    
    client = AdminClient(cloud_region)
    try:
        response = client.[create_reservation](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_create_reservation)(reservation)
        print(f"{response.name} created successfully.")
    except AlreadyExists:
        print(f"{reservation_path} already exists.")

## Update a Lite reservation

You can update the number of capacity units configured for a Lite reservation.

You can update a Lite reservation with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Reservations** page.

[Go to Lite Reservations](https://console.cloud.google.com/cloudpubsub/liteReservation)

  2. Click the Lite reservation ID.

  3. In the Lite reservation details page, click **Edit**.




### gcloud

To update a Lite reservation, use the [`gcloud pubsub lite-reservations update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/update) command:
    
    
    gcloud pubsub lite-reservations update RESERVATION_ID \
      --location=REGION \
      --throughput-capacity=THROUGHPUT_CAPACITY

Replace the following:

  * RESERVATION_ID: the ID of the Lite reservation
  * REGION: the region of the reservation
  * THROUGHPUT_CAPACITY: The reservation throughput capacity.



### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func updateReservation(w io.Writer, projectID, region, reservationID string, throughputCapacity int) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// reservationID := "my-reservation-id"
    	// throughputCapacity := 8
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	reservationPath := fmt.Sprintf("projects/%s/locations/%s/reservations/%s", projectID, region, reservationID)
    	config := pubsublite.[ReservationConfigToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_ReservationConfigToUpdate){
    		Name:               reservationPath,
    		ThroughputCapacity: throughputCapacity,
    	}
    	updatedCfg, err := client.UpdateReservation(ctx, config)
    	if err != nil {
    		return fmt.Errorf("client.UpdateReservation got err: %w", err)
    	}
    	fmt.Fprintf(w, "Updated reservation: %#v\n", updatedCfg)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html);
    import com.google.cloud.pubsublite.[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html);
    import com.google.cloud.pubsublite.proto.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html);
    import java.util.concurrent.ExecutionException;
    
    public class UpdateReservationExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        long projectNumber = Long.parseLong("123456789");
        String cloudRegion = "your-cloud-region";
        String reservationId = "your-reservation-id";
        // Each unit of throughput capacity supports up to 1 MiB/s of published messages or
        // 2 MiB/s of subscribed messages.
        int throughputCapacity = 8;
    
        updateReservationExample(projectNumber, cloudRegion, reservationId, throughputCapacity);
      }
    
      public static void updateReservationExample(
          long projectNumber, String cloudRegion, String reservationId, int throughputCapacity)
          throws Exception {
    
        [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html) reservationPath =
            [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion))
                .setName([ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html).of(reservationId))
                .build();
    
        com.google.protobuf.FieldMask fieldMask =
            com.google.protobuf.FieldMask.newBuilder().addPaths("throughput_capacity").build();
    
        [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html) reservation =
            [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html).newBuilder()
                .setName(reservationPath.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html#com_google_cloud_pubsublite_ReservationPath_toString__)())
                .setThroughputCapacity(throughputCapacity)
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html) reservationBeforeUpdate = adminClient.getReservation(reservationPath).get();
          System.out.println("Before update: " + reservationBeforeUpdate.getAllFields());
    
          [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html) reservationAfterUpdate =
              adminClient.updateReservation(reservation, fieldMask).get();
          System.out.println("After update: " + reservationAfterUpdate.getAllFields());
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) notFound) {
            System.out.println("This reservation is not found.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html), Reservation
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [ReservationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.ReservationPath.html)
    from google.protobuf.field_mask_pb2 import FieldMask
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # reservation_id = "your-reservation-id"
    # Each unit of throughput capacity supports up to 1 MiB/s of published messages
    # or 2 MiB/s of subscribed messages. Must be a positive integer.
    # throughput_capacity = 8
    
    cloud_region = CloudRegion(cloud_region)
    reservation_path = ReservationPath(project_number, cloud_region, reservation_id)
    
    # Defines which fields to update in the reservation.
    field_mask = FieldMask(paths=["throughput_capacity"])
    
    reservation = Reservation(
        name=str(reservation_path), throughput_capacity=throughput_capacity
    )
    
    client = AdminClient(cloud_region)
    try:
        response = client.[get_reservation](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_get_reservation)(reservation_path)
        print(f"Before update: {response}")
    
        response = client.[update_reservation](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_update_reservation)(reservation, field_mask)
        print(f"After update: {response}")
    except NotFound:
        print(f"{reservation_path} is not found.")

## Get Lite reservation details

You can get details about a Lite reservation using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Reservations** page.

[Go to Lite Reservations](https://console.cloud.google.com/cloudpubsub/liteReservation)

  2. Click the Lite reservation ID.




### gcloud

To get details about a Lite reservation, use the [`gcloud pubsub lite-reservations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/describe) command:
    
    
    gcloud pubsub lite-reservations describe RESERVATION_ID \
      --location=REGION

Replace the following:

  * RESERVATION_ID: the ID of the Lite reservation
  * REGION: the region of the reservation



### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func getReservation(w io.Writer, projectID, region, reservationID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// reservationID := "my-reservation"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	reservationPath := fmt.Sprintf("projects/%s/locations/%s/reservations/%s", projectID, region, reservationID)
    	res, err := client.Reservation(ctx, reservationPath)
    	if err != nil {
    		return fmt.Errorf("client.Reservation got err: %w", err)
    	}
    	fmt.Fprintf(w, "Got reservation: %#v\n", res)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html);
    import com.google.cloud.pubsublite.[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html);
    import com.google.cloud.pubsublite.proto.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html);
    import java.util.concurrent.ExecutionException;
    
    public class GetReservationExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        long projectNumber = Long.parseLong("123456789");
        String cloudRegion = "your-cloud-region";
        String reservationId = "your-reservation-id";
    
        getReservationExample(projectNumber, cloudRegion, reservationId);
      }
    
      public static void getReservationExample(
          long projectNumber, String cloudRegion, String reservationId) throws Exception {
        [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html) reservationPath =
            [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion))
                .setName([ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html).of(reservationId))
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html) response = adminClient.getReservation(reservationPath).get();
          long throughputCapacity = response.[getThroughputCapacity](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html#com_google_cloud_pubsublite_proto_Reservation_getThroughputCapacity__)();
          System.out.println(
              response.getAllFields()
                  + "\nhas "
                  + throughputCapacity
                  + " units of throughput capacity.");
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) notFound) {
            System.out.println("This reservation is not found.");
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
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [ReservationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.ReservationPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # reservation_id = "your-reservation-id"
    
    cloud_region = CloudRegion(cloud_region)
    reservation_path = ReservationPath(project_number, cloud_region, reservation_id)
    
    client = AdminClient(cloud_region)
    try:
        response = client.[get_reservation](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_get_reservation)(reservation_path)
        print(
            f"{response.name} has {response.throughput_capacity} units of throughput capacity."
        )
    except NotFound:
        print(f"{reservation_path} is not found.")

## List Lite reservations

### Console

  * Go to the **Lite Reservations** page.

[Go to Lite Reservations](https://console.cloud.google.com/cloudpubsub/liteReservation)




### gcloud

To view a list of the Lite reservations in a project, use the [`gcloud pubsub lite-reservations list`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/list) command:
    
    
    gcloud pubsub lite-reservations list \
      --location=REGION

Replace the following:

  * REGION: the region of the reservation



### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    	"google.golang.org/api/iterator"
    )
    
    func listReservations(w io.Writer, projectID, region string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    	resIter := client.[Reservations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_AdminClient_Reservations)(ctx, parent)
    	for {
    		res, err := resIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("resIter.Next() got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got reservation config: %v", res)
    	}
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.proto.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html);
    import java.util.List;
    
    public class ListReservationsExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        long projectNumber = Long.parseLong("123456789");
        String cloudRegion = "your-cloud-region";
    
        listReservationsExample(projectNumber, cloudRegion);
      }
    
      public static void listReservationsExample(long projectNumber, String cloudRegion)
          throws Exception {
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        [LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html) locationPath =
            [LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion))
                .build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          List<Reservation> reservations = adminClient.listReservations(locationPath).get();
          for ([Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation.html) reservation : reservations) {
            System.out.println(reservation.getAllFields());
          }
          System.out.println(reservations.size() + " reservation(s) listed in " + locationPath + ".");
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [LocationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.LocationPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    
    location_path = LocationPath(project_number, cloud_region)
    
    client = AdminClient(cloud_region)
    response = client.[list_reservations](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_list_reservations)(location_path)
    
    for reservation in response:
        print(reservation)
    
    print(f"{len(response)} reservation(s) listed in your project and location.")

## Delete a Lite reservation

You can delete Lite reservations with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API. In order to delete a reservation, it must not contain any topics. You can attach existing topics to a different reservation, then delete the reservation.

### Console

  1. Go to the **Lite Reservations** page.

[Go to Lite Reservations](https://console.cloud.google.com/cloudpubsub/liteReservation)

  2. Click the Lite reservation ID.

  3. In the Lite reservation details page, click **Delete**.

  4. In the dialog that appears, click **Delete** to confirm that you want to delete the Lite reservation.




### gcloud

To delete a Lite reservation, use the [`gcloud pubsub lite-reservations delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/delete) command:
    
    
    gcloud pubsub lite-reservations delete RESERVATION_ID \
      --location=REGION

Replace the following:

  * RESERVATION_ID: the ID of the Lite reservation
  * REGION: the region of the reservation



### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func deleteReservation(w io.Writer, projectID, region, reservationID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// reservationID := "my-reservation"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	reservationPath := fmt.Sprintf("projects/%s/locations/%s/reservations/%s", projectID, region, reservationID)
    	err = client.DeleteReservation(ctx, reservationPath)
    	if err != nil {
    		return fmt.Errorf("client.DeleteReservation got err: %w", err)
    	}
    	fmt.Fprint(w, "Deleted reservation")
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html);
    import com.google.cloud.pubsublite.[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html);
    import java.util.concurrent.ExecutionException;
    
    public class DeleteReservationExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        long projectNumber = Long.parseLong("123456789");
        String cloudRegion = "your-cloud-region";
        String reservationId = "your-reservation-id";
    
        deleteReservationExample(projectNumber, cloudRegion, reservationId);
      }
    
      public static void deleteReservationExample(
          long projectNumber, String cloudRegion, String reservationId) throws Exception {
    
        [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html) reservationPath =
            [ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion))
                .setName([ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ReservationName.html).of(reservationId))
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        // If a reservation has topics attached, you must delete the topics before deleting
        // the reservation.
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          adminClient.deleteReservation(reservationPath).get();
          System.out.println(reservationPath + " deleted successfully.");
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) notFound) {
            System.out.println("This reservation is not found.");
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
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [ReservationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.ReservationPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # reservation_id = "your-reservation-id"
    
    cloud_region = CloudRegion(cloud_region)
    reservation_path = ReservationPath(project_number, cloud_region, reservation_id)
    
    client = AdminClient(cloud_region)
    try:
        client.[delete_reservation](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_delete_reservation)(reservation_path)
        print(f"{reservation_path} deleted successfully.")
    except NotFound:
        print(f"{reservation_path} not found.")

## What's next

  * Learn about [Pub/Sub Lite pricing](https://cloud.google.com/pubsub/pricing#lite).
  * Create a [Lite topic](https://docs.cloud.google.com/pubsub/lite/docs/topics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
