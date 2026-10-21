---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-update/
title: Update a reservation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:09.291897+00:00
---

# Update a reservation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Update a reservation Stay organized with collections  Save and categorize content based on your preferences. 

Update an existing BigQuery reservation to change its properties, such as its slot capacity.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Updates an existing reservation resource.
     * A reservation is a mechanism used to guarantee slots to users. This sample
     * shows how to change the slot capacity of a reservation.
     * @param {string} projectId Google Cloud project ID. for example 'example-project-id'.
     * @param {string} location Google Cloud location. for example 'us-central1'.
     * @param {string} reservationId ID of the reservation to update. for example 'example-reservation'.
     */
    async function updateReservation(
      projectId,
      location = 'us-central1',
      reservationId = 'example-group-reservation',
    ) {
      const request = {
        reservation: {
          name: client.[reservationPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/v1.reservationserviceclient.html)(projectId, location, reservationId),
          slotCapacity: 150,
        },
        updateMask: {
          paths: ['slot_capacity'],
        },
      };
    
      try {
        const [updatedReservation] = await client.updateReservation(request);
        console.log(`Updated reservation: ${updatedReservation.name}`);
        console.log(`  New slot capacity: ${updatedReservation.slotCapacity}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `Reservation "${reservationId}" not found in project "${projectId}" location "${location}".`,
          );
        } else {
          console.error(`Error updating reservation "${reservationId}":`, err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    from google.protobuf import field_mask_pb2
    
    
    def update_reservation(project_id: str, location: str, reservation_id: str):
        """Updates a reservation's slot capacity.
    
        A reservation must exist before it can be updated.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the reservation, for example, us-central1.
            reservation_id: The ID of the reservation to update.
        """
        client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
        reservation = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[types](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.html).[Reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.Reservation.html)()
        reservation.name = client.[reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_reservation_path)(project_id, location, reservation_id)
        reservation.slot_capacity = 200
        update_mask = field_mask_pb2.FieldMask(paths=["slot_capacity"])
    
        try:
            updated_reservation = client.[update_reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_update_reservation)(
                reservation=reservation, update_mask=update_mask
            )
            print(f"Updated reservation: {updated_reservation.name}")
            print(f"New slot capacity: {updated_reservation.slot_capacity}")
        except exceptions.NotFound:
            print(f"Reservation '{reservation_id}' was not found in location '{location}'.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
