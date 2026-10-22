---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-datatransferservice-transferlogs-list/
title: Get log messages for a transfer run \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:33.651710+00:00
---

# Get log messages for a transfer run  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-datatransferservice-transferlogs-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get log messages for a transfer run Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves all log messages produced during a specific BigQuery Data Transfer Service transfer run.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {
      DataTransferServiceClient,
    } = require('[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)();
    
    /**
     * Lists log messages for a transfer run.
     * Transfer runs are created for each transfer configuration, and they may have associated log messages.
     *
     * @param {string} projectId Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location The geographic location of the transfer configuration (for example, 'us-central1').
     * @param {string} transferConfigId The transfer configuration ID (for example, '1234a-5678-9b12c').
     * @param {string} runId The transfer run ID (for example, 'd123e-4567-89b0c-1d23e').
     */
    async function listTransferLogs(projectId, location, transferConfigId, runId) {
      const parent = client.[projectLocationTransferConfigRunPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/v1.datatransferserviceclient.html)(
        projectId,
        location,
        transferConfigId,
        runId,
      );
      const request = {
        parent,
      };
    
      try {
        const [logs] = await client.listTransferLogs(request);
    
        if (logs.length === 0) {
          console.error(`No transfer logs found for ${parent}.`);
          return;
        }
    
        console.log(`Found ${logs.length} transfer log entries:`);
        for (const log of logs) {
          console.log(
            `  [${log.severity}] ${new Date(
              log.messageTime.seconds * 1000,
            ).toISOString()}: ${log.messageText}`,
          );
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(`Transfer run not found: ${runId}`);
        } else {
          console.error('Error listing transfer logs:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def list_transfer_logs(
        project_id: str, location: str, transfer_config_id: str, run_id: str
    ) -> None:
        """Prints the transfer logs for a given transfer run.
    
        This sample shows how to retrieve the logs for a specific transfer run,
        which can be useful for debugging and monitoring transfer jobs.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the transfer configuration (e.g., 'us-central1').
            transfer_config_id: The ID of the transfer configuration.
            run_id: The ID of the transfer run.
        """
    
        parent = client.[run_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_run_path)(
            f"{project_id}/locations/{location}", transfer_config_id, run_id
        )
    
        try:
            pager = client.[list_transfer_logs](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_list_transfer_logs)(parent=parent)
    
            print(f"Logs for transfer run {run_id}:")
            for log in pager:
                print(f"  - {log.severity.name}: {log.message_text}")
    
        except google.api_core.exceptions.NotFound:
            print(
                f"Error: Transfer run '{run_id}' not found in project '{project_id}' location '{location}'."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
