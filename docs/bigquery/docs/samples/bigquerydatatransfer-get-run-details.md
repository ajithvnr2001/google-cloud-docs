---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-get-run-details/
title: Get a transfer run \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:03.305281+00:00
---

# Get a transfer run  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-get-run-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a transfer run Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves information about a specific transfer run from the BigQuery Data Transfer Service.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage transfers](https://docs.cloud.google.com/bigquery/docs/working-with-transfers)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[GetTransferRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.GetTransferRunRequest.html);
    import com.google.cloud.bigquery.datatransfer.v1.[TransferRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferRun.html);
    import java.io.IOException;
    
    // Sample to get run details from transfer config.
    public class RunDetails {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // runId examples:
        // `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` or
        // `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}`
        String runId = "MY_RUN_ID";
        runDetails(runId);
      }
    
      public static void runDetails(String runId) throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) dataTransferServiceClient = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [GetTransferRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.GetTransferRunRequest.html) request = [GetTransferRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.GetTransferRunRequest.html).newBuilder().setName(runId).build();
          [TransferRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferRun.html) run = dataTransferServiceClient.getTransferRun(request);
          System.out.print("Run details retrieved successfully :" + [run](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog.html#com_google_api_gax_rpc_Watchdog_run__).[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferRun.html#com_google_cloud_bigquery_datatransfer_v1_TransferRun_getName__)() + "\n");
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.print("Run details not found." + ex.toString());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {
      DataTransferServiceClient,
    } = require('[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)();
    
    /**
     * Gets a transfer run.
     * A transfer run represents a single execution of a data transfer configuration.
     *
     * @param {string} projectId The Google Cloud project ID, for example 'example-project-id'.
     * @param {string} location The location of the transfer config, for example 'us-central1'.
     * @param {string} transferConfigId The ID of the transfer configuration, for example '1234a-5678-9012b'.
     * @param {string} runId The ID of the transfer run, for example 'abcdef-0123-4567-8901-fedcba987654'.
     */
    async function getTransferRun(
      projectId,
      location = 'us-central1',
      transferConfigId = '1234a-5678-9012b',
      runId = 'abcdef-0123-4567-8901-fedcba987654',
    ) {
      const name = client.[projectLocationTransferConfigRunPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/v1.datatransferserviceclient.html)(
        projectId,
        location,
        transferConfigId,
        runId,
      );
      const request = {
        name,
      };
    
      try {
        const [run] = await client.getTransferRun(request);
        console.log(`Got transfer run: ${run.name}`);
        console.log(`  Data Source Id: ${run.dataSourceId}`);
        if (run.runTime && run.runTime.seconds) {
          console.log(
            `  Run time: ${new Date(run.runTime.seconds * 1000).toISOString()}`,
          );
        }
        console.log(`  State: ${run.state}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(`Transfer run ${name} not found.`);
        } else {
          console.error(`Error getting transfer run ${name}:`, err);
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def get_transfer_run(
        project_id: str,
        location: str,
        transfer_config_id: str,
        run_id: str,
    ) -> None:
        """Gets information about a transfer run.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the transfer run, for example, 'us' or 'europe-west1'.
            transfer_config_id: The transfer configuration ID.
            run_id: The transfer run ID.
        """
        run_name = client.[run_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_run_path)(
            project=f"{project_id}/locations/{location}",
            transfer_config=transfer_config_id,
            run=run_id,
        )
    
        try:
            transfer_run = client.[get_transfer_run](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_get_transfer_run)(name=run_name)
            print(f"Got transfer run: {transfer_run.name}")
            print(f"State: {transfer_run.state.name}")
        except google.api_core.exceptions.NotFound:
            print(f"Error: Transfer run '{run_name}' not found.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
