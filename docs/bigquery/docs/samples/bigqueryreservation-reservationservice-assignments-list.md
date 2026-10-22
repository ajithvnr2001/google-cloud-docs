---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-assignments-list/
title: List all assignments for a reservation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:30.841252+00:00
---

# List all assignments for a reservation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-assignments-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List all assignments for a reservation Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of all assignments for a specified BigQuery reservation. An assignment connects a project, folder, or organization to a reservation.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const reservationServiceClient = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Lists assignments.
     * An assignment lets a project, folder, or organization use slots from a
     * specified reservation. By using a wildcard `-` for the reservation ID,
     * this sample lists all assignments for a given project and location.
     *
     * @param {string} projectId The ID of the project. Example: 'example-project-id'
     * @param {string} location The location of the reservation. Example: 'us-central1'
     */
    async function listAssignments(projectId, location = 'us-central1') {
      const request = {
        parent: `projects/${projectId}/locations/${location}/reservations/-`,
      };
    
      try {
        const iterable = reservationServiceClient.[listAssignmentsAsync](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/v1.reservationserviceclient.html)(request);
        console.log(`Assignments in parent "${request.parent}":`);
    
        let found = false;
        for await (const assignment of iterable) {
          found = true;
          console.log(`- ${assignment.name}`);
          console.log(`  - Assignee: ${assignment.assignee}`);
          console.log(`  - Job Type: ${assignment.jobType}`);
        }
    
        if (!found) {
          console.log('  No assignments found.');
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(`Parent resource not found: ${request.parent}`);
        } else {
          console.error('Error listing assignments:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    
    def list_assignments(
        project_id: str,
        location: str,
        reservation_id: str,
    ):
        """Lists all assignments for a reservation.
    
        This sample shows how to list all assignments in a given reservation.
        To list all assignments in a given location, across all reservations,
        use a wildcard `-` for the reservation ID.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the assignments , for example, 'us-central1'.
            reservation_id: The ID of the reservation to list assignments for, or "-"
                to list all assignments for the project and location.
        """
        client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
        parent = client.[reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_reservation_path)(project_id, location, reservation_id)
    
        try:
            print(f"Listing assignments for parent: '{parent}'")
            assignment_list = client.[list_assignments](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_list_assignments)(parent=parent)
    
            found_assignments = False
            for assignment in assignment_list:
                found_assignments = True
                print(f"  Got assignment: {assignment.name}")
    
            if not found_assignments:
                print("No assignments found.")
    
        except exceptions.NotFound:
            print(f"Parent resource '{parent}' not found.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
