---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-create/
title: Create a BigQuery reservation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:15.088785+00:00
---

# Create a BigQuery reservation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a BigQuery reservation Stay organized with collections  Save and categorize content based on your preferences. 

Creates a reservation in a specified project and location. A reservation represents a block of dedicated BigQuery query processing capacity that can be allocated for your organization's workloads.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Creates a new reservation.
     * A reservation provides computational resource guarantees, in the form of
     * slots, to users. A slot is a unit of computational power in BigQuery.
     *
     * @param {string} projectId Google Cloud project ID, for example 'example-project-id'.
     * @param {string} location The geographic location where the reservation should reside, for example 'us-central1'.
     * @param {string} reservationId The ID of the reservation to create, for example 'example-reservation'.
     */
    async function createReservation(
      projectId,
      location = 'us-central1',
      reservationId = 'example-reservation',
    ) {
      const parent = `projects/${projectId}/locations/${location}`;
      const request = {
        parent,
        reservationId,
        reservation: {
          slotCapacity: 100,
          ignoreIdleSlots: false,
        },
      };
    
      try {
        const [createdReservation] = await client.createReservation(request);
        console.log(`Created reservation: ${createdReservation.name}`);
        console.log(`  Slot capacity: ${createdReservation.slotCapacity}`);
      } catch (err) {
        if (err.code === status.ALREADY_EXISTS) {
          console.log(
            `Reservation ${reservationId} already exists in project ${projectId} at location ${location}.`,
          );
        } else {
          console.error(`Error creating reservation ${reservationId}:`, err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def create_reservation(project_id: str, location: str, reservation_id: str):
        """Creates a reservation.
    
        A reservation is a mechanism used to guarantee slots to users.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the reservation, for example, "us-central1".
            reservation_id: The ID of the reservation to create. It must only contain
                lower case alphanumeric characters or dashes. It must start with a
                letter and must not end with a dash. Its maximum length is 64
                characters.
        """
    
        parent = f"projects/{project_id}/locations/{location}"
        reservation = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[Reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.Reservation.html)(
            slot_capacity=100,
            ignore_idle_slots=True,
        )
    
        try:
            response = client.[create_reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_create_reservation)(
                parent=parent,
                reservation_id=reservation_id,
                reservation=reservation,
            )
            print(f"Created reservation: {response.name}")
        except AlreadyExists:
            print(
                f"Reservation '{reservation_id}' already exists in location '{location}'."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
