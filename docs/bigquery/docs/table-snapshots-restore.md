---
url: https://docs.cloud.google.com/bigquery/docs/table-snapshots-restore/
title: Restore table snapshots \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:45:43.992042+00:00
---

# Restore table snapshots  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/table-snapshots-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Restore table snapshots

This document describes how to create a writeable table from a table snapshot by using the Google Cloud console, a `CREATE TABLE CLONE` query, a `bq cp` command, or the `jobs.insert` API. It is intended for users who are familiar with [table snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro).

## Permissions and roles

This section describes the [Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/bigquery/docs/access-control#bq-permissions) that you need to create a writeable table from a table snapshot, and the [predefined IAM roles](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery) that grant those permissions.

### Permissions

To create a writeable table from a table snapshot, you need the following permissions:

**Permission** | **Resource**  
---|---  
All of the following:  
  
`bigquery.tables.get`  
`bigquery.tables.getData`  
`bigquery.tables.restoreSnapshot`  
| The table snapshot that you want to copy into a writeable table.  
`bigquery.tables.create` | The dataset that contains the destination table.  
  
### Roles

The predefined BigQuery roles that provide the required permissions are as follows:

**Role** | **Resource**  
---|---  
Any of the following:  
  
`bigquery.dataEditor`  
`bigquery.dataOwner`  
`bigquery.admin` | The table snapshot that you want to copy into a writeable table.  
Any of the following:  
  
`bigquery.dataEditor`  
`bigquery.dataOwner`  
`bigquery.admin` | The dataset that contains the destination table.  
  
## Restore a table snapshot

To create a writeable table from a snapshot, specify the table snapshot that you want to copy and the destination table. The destination table can be a new table, or you can overwrite an existing table with the table snapshot.

### Restore to a new table

You can restore a table snapshot into a new table by using one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In the **Explorer** pane, expand the project, click **Datasets** , and then click the dataset that contains the table snapshot that you want to restore from.

  4. Click **Overview > Tables**, and then click the name of the table snapshot.

  5. In the table snapshot pane that appears, click update **Restore**.

![Restore table from snapshot](https://docs.cloud.google.com/static/bigquery/images/snapshot-restore.png)

  6. In the **Restore snapshot** pane that appears, enter the **Project** , **Dataset** , and **Table** information for the new table.

  7. Click **Save**.




###  SQL 

Use the [`CREATE TABLE CLONE` DDL statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_clone_statement):

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, enter the following statement:
         
         CREATE TABLE TABLE_PROJECT_ID.TABLE_DATASET_NAME.NEW_TABLE_NAME
         CLONE SNAPSHOT_PROJECT_ID.SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME;

Replace the following: 

     * `TABLE_PROJECT_ID`: the project ID of the project in which to create the new table.
     * `TABLE_DATASET_NAME`: the name of the dataset in which to create the new table.
     * `NEW_TABLE_NAME`: the name of the new table.
     * `SNAPSHOT_PROJECT_ID`: the project ID of the project that contains the snapshot you are restoring from.
     * `SNAPSHOT_DATASET_NAME`: the name of the dataset that contains the snapshot you are restoring from.
     * `SNAPSHOT_NAME`: the name of the snapshot you are restoring from.
  3. Click play_circle **Run**.




For more information about how to run queries, see [Run an interactive query](https://docs.cloud.google.com/bigquery/docs/running-queries#queries).

###  bq 

Enter the following command in the Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/bigquery?cloudshell=true)
    
    
    [bq cp](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_cp) \
    --restore \
    --no_clobber \
    SNAPSHOT_PROJECT_ID:SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME \
    TABLE_PROJECT_ID:TABLE_DATASET_NAME.NEW_TABLE_NAME

Replace the following: 

  * `SNAPSHOT_PROJECT_ID`: the project ID of the project that contains the snapshot you are restoring from.
  * `SNAPSHOT_DATASET_NAME`: the name of the dataset that contains the snapshot you are restoring from.
  * `SNAPSHOT_NAME`: the name of the snapshot you are restoring from.
  * `TABLE_PROJECT_ID`: the project ID of the project in which to create the new table.
  * `TABLE_DATASET_NAME`: the name of the dataset in which to create the new table.
  * `NEW_TABLE_NAME`: the name of the new table.



The `--no_clobber` flag instructs the command to fail if the destination table already exists.

###  API 

Call the [`jobs.insert`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert) method with the following parameters:

**Parameter** | **Value**  
---|---  
`projectId` | The project ID of the project to bill for this operation.  
Request body | 
    
    
    {
      "configuration": {
        "copy": {
          "sourceTables": [
            {
              "projectId": "SNAPSHOT_PROJECT_ID",
              "datasetId": "SNAPSHOT_DATASET_NAME",
              "tableId": "SNAPSHOT_NAME"
            }
          ],
          "destinationTable": {
            "projectId": "TABLE_PROJECT_ID",
            "datasetId": "TABLE_DATASET_NAME",
            "tableId": "NEW_TABLE_NAME"
          },
          "operationType": "RESTORE",
          "writeDisposition": "WRITE_EMPTY"
        }
      }
    }  
  
Replace the following: 

  * `SNAPSHOT_PROJECT_ID`: the project ID of the project that contains the snapshot you are restoring from.
  * `SNAPSHOT_DATASET_NAME`: the name of the dataset that contains the snapshot you are restoring from.
  * `SNAPSHOT_NAME`: the name of the snapshot you are restoring from.
  * `TABLE_PROJECT_ID`: the project ID of the project in which to create the new table.
  * `TABLE_DATASET_NAME`: the name of the dataset in which to create the new table.
  * `NEW_TABLE_NAME`: the name of the new table.



If an expiration is not specified, then the destination table expires after the default table expiration time for the dataset that contains the destination table.

### Overwrite an existing table

You can overwrite an existing table with a table snapshot by using one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

  3. In the **Explorer** pane, expand the project, click **Datasets** , and then click the dataset that contains the table snapshot that you want to restore from.

  4. Click **Overview > Tables**, and then click the name of the table snapshot.

  5. In the table snapshot pane that appears, click **Restore**.

![Restore table from snapshot](https://docs.cloud.google.com/static/bigquery/images/snapshot-restore.png)

  6. In the **Restore snapshot** pane that appears, enter the **Project** , **Dataset** , and **Table** information for the existing table.

  7. Select **Overwrite table if it exists**.

  8. Click **Save**.




###  SQL 

Use the [`CREATE TABLE CLONE` DDL statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_clone_statement):

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, enter the following statement:
         
         CREATE OR REPLACE TABLE TABLE_PROJECT_ID.TABLE_DATASET_NAME.TABLE_NAME
         CLONE SNAPSHOT_PROJECT_ID.SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME;

Replace the following: 

     * `TABLE_PROJECT_ID`: the project ID of the project in which to create the new table.
     * `TABLE_DATASET_NAME`: the name of the dataset that contains the table you are overwriting.
     * `TABLE_NAME`: the name of the table you are overwriting.
     * `SNAPSHOT_PROJECT_ID`: the project ID of the project that contains the snapshot you are restoring from.
     * `SNAPSHOT_DATASET_NAME`: the name of the dataset that contains the snapshot you are restoring from.
     * `SNAPSHOT_NAME`: the name of the snapshot you are restoring from.
  3. Click play_circle **Run**.




For more information about how to run queries, see [Run an interactive query](https://docs.cloud.google.com/bigquery/docs/running-queries#queries).

###  bq 

Enter the following command in the Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/bigquery?cloudshell=true)
    
    
    [bq cp](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_cp) \
    --restore \
    --force \
    SNAPSHOT_PROJECT_ID:SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME \
    TABLE_PROJECT_ID:TABLE_DATASET_NAME.TABLE_NAME

Replace the following: 

  * `SNAPSHOT_PROJECT_ID`: the project ID of the project that contains the snapshot you are restoring from.
  * `SNAPSHOT_DATASET_NAME`: the name of the dataset that contains the snapshot you are restoring from.
  * `SNAPSHOT_NAME`: the name of the snapshot you are restoring from.
  * `TABLE_PROJECT_ID`: the project ID of the project in which to create the new table.
  * `TABLE_DATASET_NAME`: the name of the dataset that contains the table you are overwriting.
  * `TABLE_NAME`: the name of the table you are overwriting.



###  API 

Call the [`jobs.insert`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert) method with the following parameters:

**Parameter** | **Value**  
---|---  
`projectId` | The project ID of the project to bill for this operation.  
Request body | 
    
    
    {
      "configuration": {
        "copy": {
          "sourceTables": [
            {
              "projectId": "SNAPSHOT_PROJECT_ID",
              "datasetId": "SNAPSHOT_DATASET_NAME",
              "tableId": "SNAPSHOT_NAME"
            }
          ],
          "destinationTable": {
            "projectId": "TABLE_PROJECT_ID",
            "datasetId": "TABLE_DATASET_NAME",
            "tableId": "TABLE_NAME"
          },
          "operationType": "RESTORE",
          "writeDisposition": "WRITE_TRUNCATE"
        }
      }
    }  
  
Replace the following: 

  * `SNAPSHOT_PROJECT_ID`: the project ID of the project that contains the snapshot you are restoring from.
  * `SNAPSHOT_DATASET_NAME`: the name of the dataset that contains the snapshot you are restoring from.
  * `SNAPSHOT_NAME`: the name of the snapshot you are restoring from.
  * `TABLE_PROJECT_ID`: the project ID of the project in which to create the new table.
  * `TABLE_DATASET_NAME`: the name of the dataset that contains the table you are overwriting.
  * `TABLE_NAME`: the name of the table you are overwriting.



If an expiration is not specified, then the destination table expires after the default table expiration time for the dataset that contains the destination table.

## What's next

  * [List the table snapshots of a specified base table](https://docs.cloud.google.com/bigquery/docs/table-snapshots-list#list_the_table_snapshots_of_a_specified_base_table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
