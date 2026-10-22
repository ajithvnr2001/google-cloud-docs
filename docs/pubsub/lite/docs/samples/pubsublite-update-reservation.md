---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-update-reservation/
title: Update Lite Reservation \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:06.852755+00:00
---

# Update Lite Reservation  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-update-reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Update Lite Reservation Stay organized with collections  Save and categorize content based on your preferences. 

Update a Pub/Sub Lite reservation

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage Lite reservations](https://docs.cloud.google.com/pubsub/lite/docs/reservations)



## Code sample

### Go

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
