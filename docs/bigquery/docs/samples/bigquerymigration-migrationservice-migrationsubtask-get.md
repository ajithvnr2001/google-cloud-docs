---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-migrationservice-migrationsubtask-get/
title: Get a migration subtask \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:16.663057+00:00
---

# Get a migration subtask  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-migrationservice-migrationsubtask-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a migration subtask Stay organized with collections  Save and categorize content based on your preferences. 

Gets the details of a specific migration subtask from the BigQuery Migration Service. This is useful for checking the status or configuration of a component within a larger migration workflow.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
    /**
     * Gets a previously created migration subtask.
     *
     * A migration subtask is a single unit of work that is part of a migration workflow.
     *
     * @param {string} projectId The Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location The Google Cloud region where the migration workflow is located (for example, 'us').
     * @param {string} workflowId The ID of the migration workflow that contains the subtask (for example, '12345678-abcd-4372-a567-0e02b2c3d479').
     * @param {string} subtaskId The ID of the migration subtask to retrieve (for example, '98765432-dcba-4370-971e-7ff74afce823').
     */
    async function getMigrationSubtask(
      projectId,
      location = 'us',
      workflowId = '12345678-abcd-4372-a567-0e02b2c3d479',
      subtaskId = '98765432-dcba-4370-971e-7ff74afce823',
    ) {
      const name = client.migrationSubtaskPath(
        projectId,
        location,
        workflowId,
        subtaskId,
      );
      const request = {
        name,
      };
    
      try {
        const [subtask] = await client.getMigrationSubtask(request);
    
        console.log(`Migration subtask found: ${subtask.name}`);
        console.log(`  Type: ${subtask.type}`);
        console.log(`  State: ${subtask.state}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(`Migration subtask not found: ${name}`);
        } else {
          console.error('Error getting migration subtask:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest)
    
    
    client = [bigquery_migration_v2](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest).[MigrationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.services.migration_service.MigrationServiceClient.html)()
    
    
    def get_migration_subtask(
        project_id: str, location: str, workflow_id: str, subtask_id: str
    ) -> None:
        """Gets a previously created migration subtask.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the migration workflow, for example, "us".
            workflow_id: The ID of the migration workflow.
            subtask_id: The ID of the migration subtask.
        """
    
        name = client.[migration_subtask_path](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.services.migration_service.MigrationServiceClient.html#google_cloud_bigquery_migration_v2_services_migration_service_MigrationServiceClient_migration_subtask_path)(project_id, location, workflow_id, subtask_id)
    
        try:
            subtask = client.[get_migration_subtask](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.services.migration_service.MigrationServiceClient.html#google_cloud_bigquery_migration_v2_services_migration_service_MigrationServiceClient_get_migration_subtask)(name=name)
            print(f"Migration subtask found: {subtask.name}")
            print(f"State: {subtask.state.name}")
            print(f"Type: {subtask.type}")
        except NotFound:
            print(f"Migration subtask not found: {name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
