---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-bireservation-get/
title: Get a BI reservation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:54.430941+00:00
---

# Get a BI reservation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-bireservation-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a BI reservation Stay organized with collections  Save and categorize content based on your preferences. 

Gets the details of a specified BI reservation from the BigQuery Reservation API.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Retrieves a BI reservation.
     * A BI reservation is a singleton resource in a location.
     * @param {string} projectId Google Cloud project ID, for example 'example-project-id'.
     * @param {string} location Google Cloud location, for example 'US'.
     */
    async function getBiReservation(projectId, location = 'US') {
      const name = client.[biReservationPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/v1.reservationserviceclient.html)(projectId, location);
      const request = {
        name,
      };
    
      try {
        const [reservation] = await client.getBiReservation(request);
        console.log(`Got BI reservation: ${reservation.name}`);
        console.log(`  Size: ${reservation.size} bytes`);
        if (reservation.updateTime) {
          const updateTime = new Date(
            reservation.updateTime.seconds * 1000 +
              reservation.updateTime.nanos / 1000000,
          );
          console.log(`  Last updated: ${updateTime.toISOString()}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `BI reservation not found for project ${projectId} in location ${location}.`,
          );
        } else {
          console.error('Error getting BI reservation:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    
    def get_bi_reservation(project_id: str, location: str):
        """Gets a BI reservation.
    
        A BI reservation is a singleton resource. It is not created explicitly, but
        can be updated to enable BI Engine.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the BI reservation , for example, us-central1.
        """
        client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
        name = client.[bi_reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_bi_reservation_path)(project_id, location)
    
        try:
            reservation = client.[get_bi_reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_get_bi_reservation)(name=name)
            print(f"Got BI reservation: {reservation.name}")
            print(f"\tSize: {reservation.size} bytes")
            print(f"\tUpdated at: {reservation.update_time}")
        except NotFound:
            print(
                f"BI reservation not found for project '{project_id}' in location '{location}'."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
