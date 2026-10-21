---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-bireservation-update/
title: Update a BI reservation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:08.433828+00:00
---

# Update a BI reservation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-bireservation-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Update a BI reservation Stay organized with collections  Save and categorize content based on your preferences. 

Update the size of an existing BI reservation. The BigQuery BI Engine uses BI reservations to run fast, in-memory analysis.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Updates a BI reservation.
     * A singleton BI reservation always exists with a default size of 0. To reserve
     * BI capacity, you must update the reservation to an amount greater than 0. To
     * release BI capacity, set the reservation size to 0.
     *
     * @param {string} projectId Google Cloud Project ID, for example 'example-project-id'
     * @param {string} location Google Cloud Location, for example 'US'
     */
    async function updateBiReservation(projectId, location = 'US') {
      const biReservation = {
        name: client.[biReservationPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/v1.reservationserviceclient.html)(projectId, location),
        // Set the reservation size in bytes. This example sets it to 2 GiB.
        size: 2 * 1024 * 1024 * 1024,
      };
      const updateMask = {
        paths: ['size'],
      };
    
      const request = {
        biReservation,
        updateMask,
      };
    
      try {
        const [updatedReservation] = await client.updateBiReservation(request);
        console.log(`Updated BI reservation: ${updatedReservation.name}`);
        console.log(`  Size: ${updatedReservation.size} bytes`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `BI Reservation not found for project ${projectId} in location ${location}.`,
          );
        } else {
          console.error('Error updating BI reservation:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    from google.protobuf import field_mask_pb2
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def update_bi_reservation(project_id: str, location: str):
        """Updates a BI reservation.
    
        A singleton BI reservation always exists with default size 0.
        To reserve BI capacity, update the reservation to an amount
        greater than 0. To release BI capacity, set the reservation size to 0.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the BI reservation, for example, us-central1.
        """
    
        name = client.[bi_reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_bi_reservation_path)(project=project_id, location=location)
        bi_reservation = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[types](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.html).[BiReservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.BiReservation.html)()
        bi_reservation.name = name
    
        # The size of a BI reservation is measured in bytes. 2 GB is used here.
        bi_reservation.size = 2 * 10**9
        update_mask = field_mask_pb2.FieldMask(paths=["size"])
    
        try:
            response = client.[update_bi_reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_update_bi_reservation)(
                bi_reservation=bi_reservation, update_mask=update_mask
            )
            print(f"Updated BI reservation: {response.name}")
            print(f"New size is {response.size} bytes.")
        except exceptions.NotFound:
            print(
                f"BI reservation not found for project '{project_id}' in location '{location}'."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
