---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-iampolicy-get/
title: Get the IAM policy for a reservation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:56.767409+00:00
---

# Get the IAM policy for a reservation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-iampolicy-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get the IAM policy for a reservation Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves the Identity and Access Management (IAM) policy for a BigQuery reservation. The policy defines which principals have which roles, and is used to view the access control settings for the resource.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {
      ReservationServiceClient,
    } = require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Gets the IAM policy for a reservation.
     * An IAM policy is a collection of bindings that associates one or more members,
     * such as service accounts or users, with a single role.
     *
     * @param {string} projectId - Google Cloud project ID, for example "example-project-id".
     * @param {string} location - Location of the reservation, for example "us-central1".
     * @param {string} reservationId - ID of the reservation, for example "example-reservation".
     */
    async function getReservationIamPolicy(
      projectId,
      location = 'us-central1',
      reservationId = 'example-reservation',
    ) {
      const resource = `projects/${projectId}/locations/${location}/reservations/${reservationId}`;
      const request = {
        resource,
      };
    
      try {
        const [policy] = await client.getIamPolicy(request);
    
        console.log(`Policy for reservation ${reservationId}:`);
        if (policy.bindings && policy.bindings.length > 0) {
          console.log(JSON.stringify(policy.bindings, null, 2));
        } else {
          console.log('This reservation has no policy bindings.');
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `Reservation '${reservationId}' not found in project '${projectId}' at location '${location}'.`,
          );
        } else {
          console.error('Error getting IAM policy:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def get_reservation_iam_policy(project_id: str, location: str, reservation_id: str):
        """Gets the IAM policy for a reservation.
    
        An IAM policy is a collection of bindings that associates one or more
        principals with a single role. This sample demonstrates how to retrieve
        the policy for a reservation.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the reservation, such as "us-central1".
            reservation_id: The ID of the reservation to get the policy for.
        """
        resource = client.[reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_reservation_path)(project_id, location, reservation_id)
    
        try:
            policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_get_iam_policy)(resource=resource)
    
            print(f"Got IAM policy for reservation: {resource}")
            for binding in policy.bindings:
                print(f"  Role: {binding.role}")
                print(f"  Members: {binding.members}")
        except NotFound:
            print(f"Reservation not found: {resource}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
