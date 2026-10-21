---
url: https://docs.cloud.google.com/bigquery/docs/table-snapshots-delete/
title: Delete table snapshots \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:32:54.744243+00:00
---

# Delete table snapshots  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/table-snapshots-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete table snapshots

This document describes how to delete a table snapshot by using the Google Cloud console, a [`DROP SNAPSHOT TABLE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#drop_snapshot_table_statement) GoogleSQL statement, a [`bq rm`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_rm) command, or a BigQuery API [`tables.delete`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/delete) call. It also provides information about how to recover a table snapshot that was deleted or that expired in the past seven days. It is intended for users who are familiar with [table snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro).

## Permissions and roles

This section describes the [Identity and Access Management (IAM) permission](https://docs.cloud.google.com/bigquery/docs/access-control#bq-permissions) that you need to delete a table snapshot, and the [predefined IAM roles](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery) that grant those permissions.

### Permissions

To delete a table snapshot, you need the following permission:

**Permission** | **Resource**  
---|---  
`bigquery.tables.deleteSnapshot` | The table snapshot that you want to delete  
  
### Roles

The predefined BigQuery roles that provide the required permissions are as follows:

**Role** | **Resource**  
---|---  
Any of the following:  
  
`bigquery.dataOwner`  
`bigquery.admin` | The table snapshot that you want to delete.  
  
## Delete a table snapshot

Delete a table snapshot as you would delete a standard table. You don't need to delete a table snapshot that has expired.

You can delete a table snapshot by using one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **BigQuery** page.



[Go to BigQuery](https://console.cloud.google.com/bigquery)

  1. In the left pane, click explore **Explorer** :

![Image of the highlighted Explorer pane button.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  2. In the **Explorer** pane, expand your project, click **Datasets** , and then click the dataset that has the table snapshot.

  3. Click **Overview > Tables**, and then click the name of the table snapshot.

  4. In the details pane that appears, click **Delete**.

  5. In the dialog that appears, type `delete`, and then click **Delete** again.




###  SQL 

Use the [`DROP SNAPSHOT TABLE` DDL statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#drop_snapshot_table_statement):

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, enter the following statement:
         
         DROP SNAPSHOT TABLE PROJECT_ID.DATASET_NAME.SNAPSHOT_NAME;

Replace the following: 

     * `PROJECT_ID`: the project ID of the project that contains the snapshot.
     * `DATASET_NAME`: the name of the dataset that contains the snapshot.
     * `SNAPSHOT_NAME`: the name of the snapshot.
  3. Click play_circle **Run**.




For more information about how to run queries, see [Run an interactive query](https://docs.cloud.google.com/bigquery/docs/running-queries#queries).

###  bq 

Enter the following command in the Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/bigquery?cloudshell=true)
    
    
    [bq rm](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_rm) \
    PROJECT_ID:DATASET_NAME.SNAPSHOT_NAME

Replace the following: 

  * `PROJECT_ID`: the project ID of the project that contains the snapshot.
  * `DATASET_NAME`: the name of the dataset that contains the snapshot.
  * `SNAPSHOT_NAME`: the name of the snapshot.



###  API 

Call the [`tables.delete`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/delete) method with the following parameters:

**Parameter** | **Value**  
---|---  
`projectId` | The project ID of the project that contains the snapshot.  
`datasetId` | The name of the dataset that contains the snapshot.  
`tableId` | The name of the snapshot.  
  
## Restore a deleted or expired table snapshot

You can recover a table snapshot that was deleted or that expired in the past seven days in the same way that you recover a standard table. For more information, see [Restore table snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-restore).

## What's next

  * [Create monthly snapshots of a table by using a service account that runs a scheduled query](https://docs.cloud.google.com/bigquery/docs/table-snapshots-scheduled).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
