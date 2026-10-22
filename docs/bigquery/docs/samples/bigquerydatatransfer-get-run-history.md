---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-get-run-history/
title: List transfer runs \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:07.665538+00:00
---

# List transfer runs  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-get-run-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List transfer runs Stay organized with collections  Save and categorize content based on your preferences. 

Lists all runs for a BigQuery Data Transfer Service transfer configuration.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage transfers](https://docs.cloud.google.com/bigquery/docs/working-with-transfers)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[ListTransferRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListTransferRunsRequest.html);
    import java.io.IOException;
    
    // Sample to get run history from transfer config.
    public class RunHistory {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String configId = "MY_CONFIG_ID";
        // i.e projects/{project_id}/transferConfigs/{config_id}` or
        // `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`
        runHistory(configId);
      }
    
      public static void runHistory(String configId) throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) dataTransferServiceClient = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [ListTransferRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListTransferRunsRequest.html) request =
              [ListTransferRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListTransferRunsRequest.html).newBuilder().setParent(configId).build();
          dataTransferServiceClient
              .listTransferRuns(request)
              .iterateAll()
              .forEach(run -> System.out.print("Success! Run ID :" + [run](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog.html#com_google_api_gax_rpc_Watchdog_run__).getName() + "\n"));
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.println("Run history not found due to error." + ex.toString());
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
     * Lists transfer runs for a given transfer configuration.
     *
     * This sample shows how to list all the transfer runs for a specific transfer
     * configuration, to monitor and audit data transfer jobs.
     *
     * @param {string} projectId The Google Cloud project ID, for example 'example-project-id'.
     * @param {string} location The Google Cloud region, for example 'us-central1'.
     * @param {string} configId The BigQuery Transfer Service config ID, for example 'example-config-id'.
     */
    async function listTransferRuns(projectId, location, configId) {
      const parent = `projects/${projectId}/locations/${location}/transferConfigs/${configId}`;
      const request = {
        parent,
      };
    
      try {
        const [transferRuns] = await client.listTransferRuns(request);
        if (transferRuns.length === 0) {
          console.error(
            `No transfer runs found in project ${projectId} for ${location}.`,
          );
          return;
        }
        console.log(`Transfer runs for config '${configId}':`);
        for (const run of transferRuns) {
          console.log(`\nTransfer Run: ${run.name}`);
          console.log(`  Data Source Id: ${run.dataSourceId}`);
          if (run.runTime && run.runTime.seconds) {
            console.log(
              `  Run time: ${new Date(run.runTime.seconds * 1000).toISOString()}`,
            );
          }
          console.log(`  State: ${run.state}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(`Transfer run not found: ${parent}`);
        } else {
          console.error('Error listing transfer runs:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def list_transfer_runs(project_id: str, transfer_config_id: str, location: str) -> None:
        """Lists transfer runs for a given transfer configuration.
    
        This method retrieves a history of runs for a specific data transfer job.
    
        Args:
            project_id: The Google Cloud project ID.
            transfer_config_id: The data transfer configuration ID.
            location: The geographic location of the transfer configuration (e.g., 'us-central1').
        """
    
        parent = client.[transfer_config_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_transfer_config_path)(
            project=f"{project_id}/locations/{location}",
            transfer_config=transfer_config_id,
        )
        request = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[ListTransferRunsRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.ListTransferRunsRequest.html)(
            parent=parent,
        )
    
        try:
            pager = client.[list_transfer_runs](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_list_transfer_runs)(request=request)
            for run in pager:
                print(f"  Run: {run.name}, State: {run.state.name}")
        except google.api_core.exceptions.NotFound:
            print(
                f"Error: Transfer configuration not found: '{parent}'."
                "Please verify that the project ID, location, and transfer config ID are correct."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
