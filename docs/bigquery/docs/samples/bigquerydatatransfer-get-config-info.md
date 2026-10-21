---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-get-config-info/
title: Get a transfer configuration \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:13.022435+00:00
---

# Get a transfer configuration  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-get-config-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a transfer configuration Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves the details for a transfer configuration from the BigQuery Data Transfer Service, such as its schedule and destination.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage transfers](https://docs.cloud.google.com/bigquery/docs/working-with-transfers)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[GetTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.GetTransferConfigRequest.html);
    import com.google.cloud.bigquery.datatransfer.v1.[TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html);
    import java.io.IOException;
    
    // Sample to get config info.
    public class GetTransferConfigInfo {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String configId = "MY_CONFIG_ID";
        // i.e projects/{project_id}/transferConfigs/{config_id}` or
        // `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`
        getTransferConfigInfo(configId);
      }
    
      public static void getTransferConfigInfo(String configId) throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) dataTransferServiceClient = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [GetTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.GetTransferConfigRequest.html) request =
              [GetTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.GetTransferConfigRequest.html).newBuilder().setName(configId).build();
          [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) info = dataTransferServiceClient.getTransferConfig(request);
          System.out.print("Config info retrieved successfully." + info.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html#com_google_cloud_bigquery_datatransfer_v1_TransferConfig_getName__)() + "\n");
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.print("config not found." + ex.toString());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {DataTransferServiceClient} =
      require('[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)();
    
    /**
     * Gets a transfer configuration for a BigQuery data transfer.
     * A transfer configuration contains all metadata needed to perform a data transfer.
     *
     * @param {string} projectId The Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location The Google Cloud region (for example, 'us-central1').
     * @param {string} configId The transfer configuration ID (for example, '1234a567-b89c-12d3-45e6-f789g01h23i4').
     */
    async function getTransferConfig(projectId, location, configId) {
      const name = client.[projectLocationTransferConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/v1.datatransferserviceclient.html)(
        projectId,
        location,
        configId,
      );
      const request = {
        name,
      };
    
      try {
        const [config] = await client.getTransferConfig(request);
        console.log(`Got transfer config: ${config.name}`);
        console.log(`  Display Name: ${config.displayName}`);
        console.log(`  Data Source ID: ${config.dataSourceId}`);
        console.log(`  Destination Dataset ID: ${config.destinationDatasetId}`);
        console.log(`  State: ${config.state}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Transfer config ${configId} not found in project ${projectId} in location ${location}.`,
          );
        } else {
          console.error(`Error getting transfer config ${configId}:`, err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def get_transfer_config(
        project_id: str,
        location: str,
        transfer_config_id: str,
    ) -> None:
        """Gets information about a data transfer configuration.
    
        This sample demonstrates how to retrieve the details of a BigQuery
        Data Transfer Service configuration, which contains metadata about a
        data transfer, such as its schedule and destination.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the transfer config, for example "us-central1"
            transfer_config_id: The transfer configuration ID
        """
    
        try:
            transfer_config_name = client.[transfer_config_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_transfer_config_path)(
                project=f"{project_id}/locations/{location}",
                transfer_config=transfer_config_id,
            )
            transfer_config = client.[get_transfer_config](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_get_transfer_config)(name=transfer_config_name)
    
            print(f"Got transfer config: {transfer_config.name}")
            print(f"Display name: {transfer_config.display_name}")
            print(f"Destination dataset: {transfer_config.destination_dataset_id}")
            print(f"Data source: {transfer_config.data_source_id}")
            if "time_based_schedule" in transfer_config.schedule_options_v2:
                print(
                    f"Schedule: {transfer_config.schedule_options_v2.time_based_schedule.schedule}"
                )
            else:
                print("Schedule: None")
        except google.api_core.exceptions.NotFound:
            print(f"Error: Transfer config '{transfer_config_name}' not found.")
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
