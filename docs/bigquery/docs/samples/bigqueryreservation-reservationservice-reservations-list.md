---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservations-list/
title: List reservations \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:59.907116+00:00
---

# List reservations  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservations-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List reservations Stay organized with collections  Save and categorize content based on your preferences. 

Lists all BigQuery reservations within a specified project and location.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Lists all reservations for the project in the specified location.
     *
     * A reservation provides computational resource guarantees, in the form of
     * slots, to users.
     *
     * @param {string} projectId Google Cloud project ID. for example 'example-project-id'
     * @param {string} location Google Cloud location. for example 'us-central1'
     */
    async function listReservations(projectId, location = 'us-central1') {
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
      };
    
      try {
        const [reservations] = await client.listReservations(request);
    
        if (reservations.length === 0) {
          console.log(
            `No reservations found in project ${projectId} in location ${location}.`,
          );
          return;
        }
    
        console.log(
          `Reservations in project ${projectId} in location ${location}:`,
        );
        for (const reservation of reservations) {
          console.log(`- Reservation: ${reservation.name}`);
          console.log(`  Slot capacity: ${reservation.slotCapacity}`);
          console.log(`  Ignore idle slots: ${reservation.ignoreIdleSlots}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(`Project or location not found: ${request.parent}`);
        } else {
          console.error('An error occurred while listing reservations:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def list_reservations(project_id: str, location: str):
        """Lists all reservations for a project and location.
    
        A reservation provides computational resource guarantees, in the form of
        slots, to users. This sample shows how to list existing reservations
        within a specific project and location.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the reservations, for example, us-central1.
        """
    
        parent = f"projects/{project_id}/locations/{location}"
    
        try:
            print(f"Listing reservations for parent: '{parent}':")
            for reservation in client.[list_reservations](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_list_reservations)(parent=parent):
                print(f"\tReservation: {reservation.name}")
                print(f"\tSlot capacity: {reservation.slot_capacity}")
    
            print("Finished listing reservations.")
        except exceptions.NotFound:
            print(
                f"Parent resource '{parent}' was not found. Please check your project ID and location."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
