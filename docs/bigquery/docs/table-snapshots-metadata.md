---
url: https://docs.cloud.google.com/bigquery/docs/table-snapshots-metadata/
title: View table snapshot metadata \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:33:55.005407+00:00
---

# View table snapshot metadata  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/table-snapshots-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View table snapshot metadata

This document describes how to view the metadata for a BigQuery table snapshot in the Google Cloud console, by querying the [`TABLE_SNAPSHOTS`](https://docs.cloud.google.com/bigquery/docs/information-schema-snapshots) view of the `INFORMATION_SCHEMA` table, by using the [`bq show`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_show) command, or by calling the [`tables.get`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/get) API. It is intended for users who are familiar with BigQuery [tables](https://docs.cloud.google.com/bigquery/docs/tables-intro) and [table snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro).

## Permissions and roles

This section describes the [Identity and Access Management (IAM) permission](https://docs.cloud.google.com/bigquery/docs/access-control#bq-permissions) that you need to view the metadata for a table snapshot, and the [predefined IAM roles](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery) that grant those permissions.

### Permissions

To view a table snapshot's metadata, you need the following permission:

**Permission** | **Resource**  
---|---  
` bigquery.tables.get ` | The table snapshot  
  
### Roles

The predefined BigQuery roles that provide the required permission are as follows:

**Role** | **Resource**  
---|---  
Any of the following:  
  
`bigquery.metadataViewer`  
`bigquery.dataViewer`  
`bigquery.dataEditor`  
`bigquery.dataOwner`  
`bigquery.admin` | The table snapshot  
  
## Get a table snapshot's metadata

The metadata for a table snapshot is similar to the metadata for a standard table, with the following differences:

  * An additional `baseTableReference` field identifies the base table that the snapshot was taken from.
  * The `type` field has the value `SNAPSHOT`.



You can view the metadata for a table snapshot by using one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In the **Explorer** pane, expand your project, click **Datasets** , and then click the dataset that has the table snapshot.

  4. Click **Overview > Tables**, and then click the name of the table snapshot.

  5. In the snapshot pane that appears, you can do the following:

     * Click the **Schema** tab to view the table snapshot's schema and policy tags.

     * Click the **Details** table to view the table snapshot's size, expiration, base table, snapshot time, and other information.




###  SQL 

To see metadata for a table snapshot, query the [`INFORMATION_SCHEMA.TABLE_SNAPSHOTS` view](https://docs.cloud.google.com/bigquery/docs/information-schema-snapshots):

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, enter the following statement:
         
         SELECT
           *
         FROM
           PROJECT_ID.DATASET_NAME.INFORMATION_SCHEMA.TABLE_SNAPSHOTS
         WHERE
           table_name = 'SNAPSHOT_NAME';

Replace the following: 

     * `PROJECT_ID`: the project ID of the project that contains the snapshot.
     * `DATASET_NAME`: the name of the dataset that contains the snapshot.
     * `SNAPSHOT_NAME`: the name of the snapshot.
  3. Click play_circle **Run**.




For more information about how to run queries, see [Run an interactive query](https://docs.cloud.google.com/bigquery/docs/running-queries#queries).

###  bq 

Enter the following command in the Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/bigquery?cloudshell=true)
    
    
    [bq show](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_show) \
    --format=prettyjson \
    PROJECT_ID:DATASET_NAME.SNAPSHOT_NAME

Replace the following: 

  * `PROJECT_ID`: the project ID of the project that contains the snapshot.
  * `DATASET_NAME`: the name of the dataset that contains the snapshot.
  * `SNAPSHOT_NAME`: the name of the snapshot.



The output is similar to the following:
    
    
    {
      "creationTime": "1593194331936",
       ...
      "snapshotDefinition": {
        "baseTableReference": {
          "datasetId": "myDataset",
          "projectId": "myProject",
          "tableId": "mytable"
        },
        "snapshotTime": "2020-06-26T17:58:50.815Z"
      },
      "tableReference": {
        "datasetId": "otherDataset",
        "projectId": "myProject",
        "tableId": "mySnapshot"
      },
      "type": "SNAPSHOT"
    }

###  API 

Call the [`tables.get`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/get) method with the following parameters:

**Parameter** | **Value**  
---|---  
`projectId` | The project ID of the project that contains the snapshot.  
`datasetId` | The name of the dataset that contains the snapshot.  
`tableId` | The name of the snapshot.  
  
The response body is similar to the following: 
    
    
    {
      "kind": "bigquery#table",
      "etag": "...",
      "id": "myProject:myDataset.mySnapshot",
      "selfLink": "https://content-bigquery.googleapis.com/bigquery/v2/projects/myProject/datasets/myDataset/tables/mySnapshot",
      "tableReference": {
        "projectId": "myProject",
        "datasetId": "myDataset",
        "tableId": "mySnapshot"
      },
      "description": "...",
      "schema": {
        "fields": [
          ...
        ]
      },
      "numBytes": "637931",
      "numLongTermBytes": "0",
      "numRows": "33266",
      "creationTime": "1593194331936",
      "lastModifiedTime": "1593194331936",
      "type": "SNAPSHOT",
      "location": "US",
      "snapshotDefinition": {
        "baseTableReference": {
          "projectId": "myProject",
          "datasetId": "otherDataset",
          "tableId": "myTable"
        },
        "snapshotTime": "2020-06-26T17:58:50.815Z"
      }
    }
    

## What's next

  * [Update a table snapshot's description, expiration date, or access policy](https://docs.cloud.google.com/bigquery/docs/table-snapshots-update).
  * [Delete a table snapshot](https://docs.cloud.google.com/bigquery/docs/table-snapshots-delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
