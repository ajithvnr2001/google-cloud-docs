---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-bigquerywrite-writestream-get/
title: Get write stream details \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:08.882360+00:00
---

# Get write stream details  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-bigquerywrite-writestream-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get write stream details Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves information about an existing BigQuery write stream. Use this to check the state and schema of a stream before appending data.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {BigQueryWriteClient} = require('[@google-cloud/bigquery-storage](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [BigQueryWriteClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)();
    
    /**
     * Gets information about a single write stream.
     *
     * @param {string} projectId The project ID of the table. e.g. 'my-project'
     * @param {string} datasetId The dataset ID of the table. e.g. 'my_dataset'
     * @param {string} tableId The ID of the table. e.g. 'my_table'
     */
    async function getWriteStream(projectId, datasetId, tableId) {
    
      const streamId = "[_default](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)";
      const name = client.writeStreamPath(projectId, datasetId, tableId, streamId);
    
      const request = {
        name,
      };
    
      try {
        const [response] = await client.getWriteStream(request);
    
        console.log(`Got write stream: ${response.name}`);
        console.log(`Stream type: ${response.type}`);
        console.log(`Stream location: ${response.location}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(`Write stream ${name} not found.`);
        } else {
          console.error('Error getting write stream:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_storage_v1](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest)
    
    
    def get_write_stream(
        project_id: str, dataset_id: str, table_id: str, stream_id: str
    ) -> None:
        """Gets information about a single write stream.
    
        Args:
            project_id: The project id.
            dataset_id: The dataset id
            table_id: The table id
            stream_id: The stream id
        """
        client = [bigquery_storage_v1](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest).BigQueryWriteClient()
        stream_name = (
            f"projects/{project_id}/datasets/{dataset_id}"
            f"/tables/{table_id}/streams/{stream_id}"
        )
    
        try:
            stream = [client](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.client.html).[get_write_stream](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.services.big_query_write.BigQueryWriteClient.html#google_cloud_bigquery_storage_v1_services_big_query_write_BigQueryWriteClient_get_write_stream)(name=stream_name)
    
            print(f"Got write stream: {stream.name}")
            print(f"Stream type: {stream.Type(stream.type_).name}")
    
        except google.api_core.exceptions.NotFound:
            print(f"Write stream not found: {stream_name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
