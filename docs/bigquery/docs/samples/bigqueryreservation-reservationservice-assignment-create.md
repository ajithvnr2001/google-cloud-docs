---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-assignment-create/
title: Create a reservation assignment \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:03:02.963586+00:00
---

# Create a reservation assignment  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-assignment-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a reservation assignment Stay organized with collections  Save and categorize content based on your preferences. 

Create an assignment to map a project, folder, or organization to a BigQuery reservation.

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
     * Creates an assignment to assign a project to a reservation.
     * A reservation assignment lets a project submit jobs of a certain type
     * using slots from the specified reservation.
     *
     * @param {string} projectId Google Cloud Project ID that owns the reservation, for example 'example-project-id'.
     * @param {string} location Google Cloud Location, for example 'us-central1'.
     * @param {string} reservationId The ID of the reservation to which the project will be assigned, for example 'example-reservation'.
     */
    async function createAssignment(
      projectId,
      location = 'us-central1',
      reservationId = 'example-reservation',
    ) {
      const parent = client.[reservationPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/v1.reservationserviceclient.html)(projectId, location, reservationId);
      const request = {
        parent,
        assignment: {
          assignee: `projects/${projectId}`,
          jobType: '[QUERY](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/protos.google.cloud.bigquery.reservation.v1.assignment.jobtype.html)',
        },
      };
    
      try {
        const [assignment] = await client.createAssignment(request);
        console.log(`Created assignment: ${assignment.name}`);
        console.log(`  Assignee: ${assignment.assignee}`);
        console.log(`  Job Type: ${assignment.jobType}`);
      } catch (err) {
        if (err.code === status.ALREADY_EXISTS) {
          console.log(
            `Assignment for project ${projectId} to reservation ${reservationId} already exists.`,
          );
        } else {
          console.error('Error creating assignment:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def create_assignment(project_id: str, location: str, reservation_id: str):
        """Creates a new assignment for a reservation.
    
        This shows how to create an assignment that gives a project access to
        a reservation.
    
        Args:
            project_id: The Google Cloud project ID of the reservation owner.
            location: The geographic location of the reservation, for example, "US".
            reservation_id: The ID of the reservation to create the assignment in.
        """
    
        parent = client.[reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_reservation_path)(project_id, location, reservation_id)
        assignee = f"projects/{project_id}"
        assignment = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[Assignment](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.Assignment.html)(
            assignee=assignee,
            job_type=[bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[Assignment](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.Assignment.html).[JobType](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.Assignment.JobType.html).QUERY,
        )
    
        try:
            created_assignment = client.[create_assignment](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_create_assignment)(
                parent=parent, assignment=assignment
            )
            print(f"Created assignment: {created_assignment.name}")
        except exceptions.AlreadyExists:
            print(f"Assignment for project {project_id} and job type QUERY already exists.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
