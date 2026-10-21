---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-datatransferservice-datasource-get/
title: Get a data source \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:12.686232+00:00
---

# Get a data source  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-datatransferservice-datasource-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a data source Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves information for a specific data source, such as Google Ads or YouTube, supported by the BigQuery Data Transfer Service.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {DataTransferServiceClient} =
      require('[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)();
    
    /**
     * Retrieves a supported data source and returns its settings.
     * This sample shows how to get a data source's details, to understand its parameters and capabilities before creating a transfer.
     *
     * @param {string} projectId The project ID to use, for example 'example-project-id'
     * @param {string} location The location to use, for example 'us-central1'
     * @param {string} dataSourceId The data source ID to use, for example 'google_cloud_storage'
     */
    async function getDataSource(projectId, location, dataSourceId) {
      const name = client.[projectLocationDataSourcePath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/v1.datatransferserviceclient.html)(
        projectId,
        location,
        dataSourceId,
      );
    
      const request = {
        name,
      };
    
      try {
        const [dataSource] = await client.getDataSource(request);
        console.log(`Data source ${dataSource.name} retrieved:`);
        console.log(`  Display Name: ${dataSource.displayName}`);
        console.log(`  Description: ${dataSource.description}`);
        console.log(`  Data Source ID: ${dataSource.dataSourceId}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Data source ${dataSourceId} not found in project ${projectId} in location ${location}.`,
          );
        } else {
          console.error(`Error getting data source ${dataSourceId}:`, err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def get_data_source(project_id: str, data_source_id: str) -> None:
        """Retrieves a data source definition by name.
    
        This sample shows how to get a data source definition, which includes its
        display name, description, and other properties.
    
        Args:
            project_id: The Google Cloud project ID.
            data_source_id: The data source ID, for example, 'google_cloud_storage'.
        """
        name = client.[data_source_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_data_source_path)(project=project_id, data_source=data_source_id)
    
        try:
            response = client.[get_data_source](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_get_data_source)(name=name)
            print(f"Retrieved data source: {response.name}")
            print(f"Display Name: {response.display_name}")
            print(f"Description: {response.description}")
            print(f"Client ID: {response.client_id}")
            print(f"Supports custom schedule: {response.supports_custom_schedule}")
        except google.api_core.exceptions.NotFound:
            print(f"Error: Data source '{name}' was not found.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
