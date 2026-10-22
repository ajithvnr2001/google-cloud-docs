---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-table-snapshot/
title: create a snapshot of a BigQuery table \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:01.176166+00:00
---

# create a snapshot of a BigQuery table  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-table-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  create a snapshot of a BigQuery table Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates creating a snapshot table from a managed BigQuery table.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # TODO(developer): Set table_id to the ID of the table to create.
    source_table_id = "your-project.your_dataset.your_table_name"
    snapshot_table_id = "your-project.your_dataset.snapshot_table_name"
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    copy_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[CopyJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig.html)()
    copy_config.[operation_type](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig.html#google_cloud_bigquery_job_CopyJobConfig_operation_type) = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[OperationType](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.OperationType.html).[SNAPSHOT](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.OperationType.html#google_cloud_bigquery_job_OperationType_SNAPSHOT)
    
    copy_job = client.[copy_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_copy_table)(
        sources=source_table_id,
        destination=snapshot_table_id,
        job_config=copy_config,
    )
    copy_job.result()
    
    print("Created table snapshot {}".format(snapshot_table_id))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
