---
url: https://docs.cloud.google.com/datastream/docs/best-practices-move-table-to-another-region/
title: Migrate a CDC table to another region \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:18.585978+00:00
---

# Migrate a CDC table to another region  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/best-practices-move-table-to-another-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Resources ](https://docs.cloud.google.com/datastream/docs/quotas)



Send feedback 

#  Migrate a CDC table to another region Stay organized with collections  Save and categorize content based on your preferences. 

You can move a Datastream destination dataset to another BigQuery region or multi-region by using cross-region dataset replication. This workflow updates the location of an active change data capture (CDC) dataset while minimizing stream downtime and avoiding a full historical backfill from your source database.

During the migration, querying the secondary region might return incomplete or inaccurate results. For more information about migration limitations, see [Cross-region dataset replication](https://docs.cloud.google.com/bigquery/docs/data-replication#limitations).

## Before you begin

Before you start migrating your data to another region, consider the following:

  * Migration takes time, and you must temporarily pause the stream during the operation. To maintain data integrity, the source database must retain the change logs when the stream is paused. To estimate how long to pause the stream, combine the value of `max_staleness` in the dataset and the longest-running merge operation: 
    * For information about how long it might take for merge operations to finish, see [Recommended table `max_staleness` value](https://docs.cloud.google.com/bigquery/docs/change-data-capture#recommended-max-staleness).
    * To find the maximum `max_staleness` in the dataset, see [Determine the current `max_staleness` value of a table](https://docs.cloud.google.com/bigquery/docs/change-data-capture#determine-max-staleness) and adjust the query to your specific needs.
    * If the estimated pause is too long for your source database to support, you might want to consider temporarily reducing the value of `max_staleness` for the tables in the dataset.
  * Verify that the user performing the migration has sufficient BigQuery resources in the destination region (query reservation and background reservation). For more information about reservations, see [Reservation assignments](https://docs.cloud.google.com/bigquery/docs/reservations-intro#assignments).
  * Verify that the user performing the migration has sufficient permissions to perform this operation, such as [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) controls or [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).



## Migration steps

To initiate [dataset migration](https://docs.cloud.google.com/bigquery/docs/data-replication#migrate_datasets), use BigQuery data replication:

  1. In the Google Cloud console, go to the **BigQuery Studio** page.

[ Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

  2. Create a BigQuery dataset replica in the new region:
         
         ALTER SCHEMA DATASET_NAME
         ADD REPLICA 'NEW_REGION'
         OPTIONS(location='NEW_REGION');
         

Replace the following:

     * DATASET_NAME: the name of the dataset that you want to create.
     * NEW_REGION: the name of the region where you want to create your dataset. For example, `region-us`.
  3. Monitor the migration progress, and wait until the copy watermark in the replica is within a few minutes of the primary. You can run this query on the [BigQuery INFORMATION_SCHEMA](https://docs.cloud.google.com/bigquery/docs/information-schema-schemata-replicas#schema) to check the migration progress:
         
         SELECT
         catalog_name as project_id,
         schema_name as dataset_name,
         replication_time as dataset_replica_staleness
         FROM
         'NEW_REGION'.INFORMATION_SCHEMA.SCHEMATA_REPLICAS
         WHERE
         catalog_name = PROJECT_ID
         AND schema_name = DATASET_NAME
         AND location = NEW_REGION;
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * DATASET_NAME: the name of your dataset.
     * DATASET_REPLICA_STALENESS: the staleness configuration of the tables in the dataset replica that you created.
     * NEW_REGION: the region where you created your dataset.
  4. Pause the existing Datastream stream. For more information, see [Pause the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#pauseastream).

  5. Wait for the stream to drain and take note of the time when the stream entered the `PAUSED` state.

  6. Confirm that the latest CDC changes have been applied to the BigQuery table by checking the [`upsert_stream_apply_watermark`](https://docs.cloud.google.com/bigquery/docs/change-data-capture#monitor_table_upsert_operation_progress) for the table. Run the following query and ensure that the watermark timestamp is 10 minutes later then when the stream was paused:
         
         SELECT table_name, upsert_stream_apply_watermark
         FROM DATASET_NAME.INFORMATION_SCHEMA.TABLES
         

To run the query only for a specific table, add the following `WHERE` clause:
         
         WHERE table_name = 'TABLE_NAME'
         

Replace the following:

     * DATASET_NAME: the name of your dataset.
     * TABLE_NAME: optional. The table for which you want to check the `upsert_stream_apply_watermark`.
  7. Use the query from step 3 to verify that the new region copy watermark is later than the `upsert_stream_apply_watermark` captured in step 6.

  8. Optionally, manually compare several tables in the primary dataset in the original region with the replica in the new region to verify that all data is correctly copied.

  9. Promote the BigQuery dataset replica by running the following command in BigQuery Studio:
         
         ALTER SCHEMA DATASET_NAME
         SET OPTIONS(primary_replica = 'NEW_REGION');
         

Replace the following:

     * DATASET_NAME: the name of your dataset.
     * NEW_REGION: the region where you created your dataset.
  10. Optionally, if you no longer need the original dataset (now the replica), and don't want to incur extra charges, then go to BigQuery Studio and drop the original BigQuery dataset:
         
         ALTER SCHEMA DATASET_NAME DROP REPLICA IF EXISTS ORIGINAL_REGION;
         

Replace the following:

     * DATASET_NAME: the name of the original dataset.
     * ORIGINAL_REGION: the region of the original dataset.
  11. Create a new stream with the exact same configuration but with new BigQuery destination location.

  12. Start the new stream.

To prevent replicating duplicate events, start the stream from a specific position:

     * For MySQL and Oracle sources: you can identify the log position by examining the logs of the original stream and finding the last position from which the stream read successfully. For information about starting the stream from a specific position, see [Manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams#startastreamfromspecific).
     * For PostgreSQL sources: the new stream starts reading changes from the first log sequence number (LSN) in the replication slot. Because the original stream might have already processed some of these changes, manually change the pointer of the replication slot to the last LSN from which Datastream read. You can find this LSN in the Datastream consumer logs.
  13. Optionally, delete the original stream.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
