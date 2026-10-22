---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-list-configs/
title: List data transfer configurations \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:45.700812+00:00
---

# List data transfer configurations  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-list-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List data transfer configurations Stay organized with collections  Save and categorize content based on your preferences. 

Lists all BigQuery Data Transfer Service transfer configurations for a given project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage transfers](https://docs.cloud.google.com/bigquery/docs/working-with-transfers)
  * [Scheduling queries](https://docs.cloud.google.com/bigquery/docs/scheduling-queries)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[ListTransferConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListTransferConfigsRequest.html);
    import com.google.cloud.bigquery.datatransfer.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html);
    import java.io.IOException;
    
    // Sample to get list of transfer config
    public class ListTransferConfigs {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        final String projectId = "MY_PROJECT_ID";
        listTransferConfigs(projectId);
      }
    
      public static void listTransferConfigs(String projectId) throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) dataTransferServiceClient = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html) parent = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html).of(projectId);
          [ListTransferConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListTransferConfigsRequest.html) request =
              [ListTransferConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListTransferConfigsRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html#com_google_cloud_bigquery_datatransfer_v1_ProjectName_toString__)()).build();
          dataTransferServiceClient
              .listTransferConfigs(request)
              .iterateAll()
              .forEach(config -> System.out.print("Success! Config ID :" + config.getName() + "\n"));
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.println("Config list not found due to error." + ex.toString());
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
     * Lists all transfer configurations for a project.
     * This shows how to iterate through all the transfer configurations in a project.
     *
     * @param {string} projectId Google Cloud Project ID (for example, 'example-project-id').
     * @param {string} [location="us-central1"] Google Cloud location (for example, 'us-central1').
     */
    async function listTransferConfigs(projectId, location = 'us-central1') {
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
      };
    
      try {
        const [configs] = await client.listTransferConfigs(request);
    
        if (configs.length === 0) {
          console.error(
            `No transfer configurations found in project '${projectId}' at location '${location}'.`,
          );
          return;
        }
    
        console.log(`Found ${configs.length} transfer configurations:`);
        for (const config of configs) {
          console.log(`\nConfiguration: ${config.name}`);
          console.log(`  Display Name: ${config.displayName}`);
          console.log(`  Data Source ID: ${config.dataSourceId}`);
          console.log(`  Destination Dataset ID: ${config.destinationDatasetId}`);
          console.log(`  State: ${config.state}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Project '${projectId}' not found or BigQuery Data Transfer API is not enabled.`,
          );
        } else {
          console.error('Error listing transfer configurations:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def list_transfer_configs(project_id: str, location: str) -> None:
        """Lists transfer configurations in a given project.
    
        This sample demonstrates how to list all transfer configurations in a project.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the transfer config, for example "us-central1"
        """
    
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_common_location_path)(project_id, location)
    
        try:
            for config in client.[list_transfer_configs](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_list_transfer_configs)(parent=parent):
                print(f"Name: {config.name}")
                print(f"Display Name: {config.display_name}")
                print(f"Data source: {config.data_source_id}")
                print(f"Destination dataset: {config.destination_dataset_id}")
                if "time_based_schedule" in config.schedule_options_v2:
                    print(
                        f"Schedule: {config.schedule_options_v2.time_based_schedule.schedule}"
                    )
                else:
                    print("Schedule: None")
                print("---")
        except google.api_core.exceptions.NotFound:
            print(
                f"Error: Project '{project_id}' not found or contains no transfer configs."
            )
        except google.api_core.exceptions.PermissionDenied:
            print(
                f"Error: Permission denied for project '{project_id}'. Please ensure you have the correct permissions."
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
