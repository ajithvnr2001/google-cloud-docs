---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-get/
title: Get a reservation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:57.855976+00:00
---

# Get a reservation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a reservation Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a specified BigQuery reservation. Use this to check a reservation's details, such as its slot capacity and whether it ignores idle slots.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Returns information about the reservation.
     * A reservation provides computational resource guarantees, in the form of
     * slots, to users. A slot is a unit of computational power in BigQuery.
     *
     * @param {string} projectId Google Cloud Project ID, for example 'example-project-id'.
     * @param {string} location The geographic location where the reservation resides, for example 'us-central1'.
     * @param {string} reservationId The ID of the reservation to retrieve, for example 'example-reservation'.
     */
    async function getReservation(
      projectId,
      location = 'us-central1',
      reservationId = 'example-reservation',
    ) {
      const request = {
        name: client.[reservationPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/v1.reservationserviceclient.html)(projectId, location, reservationId),
      };
    
      try {
        const [reservation] = await client.getReservation(request);
        console.log(`Got reservation: ${reservation.name}`);
        console.log(`  Slot capacity: ${reservation.slotCapacity}`);
        console.log(`  Ignore idle slots: ${reservation.ignoreIdleSlots}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `Reservation '${reservationId}' not found in project '${projectId}' location '${location}'.`,
          );
        } else {
          console.error('Error getting reservation:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def get_reservation(project_id: str, location: str, reservation_id: str):
        """Gets information about a reservation.
    
        A reservation is a mechanism used to guarantee slots to users.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the reservation, for example, "us-central1".
            reservation_id: The ID of the reservation to retrieve.
        """
    
        name = client.[reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_reservation_path)(project_id, location, reservation_id)
    
        try:
            reservation = client.[get_reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_get_reservation)(name=name)
            print(f"Retrieved reservation: {reservation.name}")
            print(f"\tSlot capacity: {reservation.slot_capacity}")
            print(f"\tIgnore idle slots: {reservation.ignore_idle_slots}")
        except exceptions.NotFound:
            print(f"Reservation '{reservation_id}' not found.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
