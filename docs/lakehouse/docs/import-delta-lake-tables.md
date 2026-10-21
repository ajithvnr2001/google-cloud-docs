---
url: https://docs.cloud.google.com/lakehouse/docs/import-delta-lake-tables/
title: Import Delta Lake tables into Lakehouse using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:54.730153+00:00
---

# Import Delta Lake tables into Lakehouse using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/import-delta-lake-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Import Delta Lake tables into Lakehouse using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Migrating Delta Lake tables into borderless Lakehouse can be complex and expensive if you have to move large volumes of data. The Dataflow job builder provides a low-code or no-code interface to import your Cloud Storage Delta Lake tables directly into Lakehouse. The existing data is copied over from the Delta Lake table to the target Lakehouse table using a Dataflow job that autoscales based on the volume of your data.

For new tables, Dataflow automatically creates the schema. For existing tables, the schema isn't modified, so the destination table schema must correctly map to the source Delta Lake table for the job to succeed.

Use the following connection details to import data from a Delta Lake table stored in Cloud Storage.

After you import this data, you have the option to enable continuous migration.

## Before you begin

To import Delta Lake table data, you need the following:

  1. Enable the Dataflow, BigQuery, and Lakehouse APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow.googleapis.com,bigquery.googleapis.com,biglake.googleapis.com)

  2. To get the permissions that you need to create the resources, ask your administrator to grant you the required Identity and Access Management (IAM) roles on your project.

  3. An existing Delta Lake table stored in a Cloud Storage bucket. The table directory must be a valid Delta Lake table root containing your Parquet data files and the `_delta_log/` transaction log directory.

  4. A Lakehouse Iceberg catalog, namespace, and [table](https://docs.cloud.google.com/biglake/docs/biglake-iceberg-tables) to import the data into.




## Support and limitations

Importing Delta Lake table data into Lakehouse using Dataflow has the following limitations:

  * You must use a batch pipeline job to use this feature.
  * For existing destination tables, the schema isn't modified. The destination table schema must correctly map to the source Delta Lake table schema.
  * The source data must be a valid Delta Lake table stored in Cloud Storage. The table root directory must contain the Parquet data files and the `_delta_log/` transaction log directory (containing JSON or Parquet log files) as created by Delta Lake.
  * Amazon S3 isn't supported for Delta Lake table sources.



## Import a Delta Lake table

To import a Delta Lake table into Lakehouse, complete the following steps:

  1. In the Google Cloud console, go to the **Lakehouse runtime catalog** page.

[Go to Lakehouse runtime catalog](https://console.cloud.google.com/biglake/metastore/catalogs)

  2. Select the catalog, namespace, and table you want to import data into.

  3. On the **Table details** page, click download**Import table** , and then select **From Delta Lake (Batch)**.

The Dataflow **Job builder** page opens with the **Delta Lake to Lakehouse** blueprint loaded.

  4. In the **Sources** section:

     1. To expand the **ReadFromDeltaLake** **Delta Lake table** source panel, click the keyboard_arrow_downexpander arrow.

     2. In the **Table path** field, enter the Cloud Storage URI of the root directory of the Delta Lake table (the directory containing the data files and the `_delta_log/` directory). For example, `gs://BUCKET_NAME/tables/TABLE_NAME`.

     3. Optional: In the **Hadoop configuration properties** field, configure any additional Hadoop configuration properties required to read from Cloud Storage. For example: `fs.gs.impl=com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem`.

     4. Click **Done**.

  5. In the **Sink** section:

     1. Optional: Review the **WriteToIceberg** **Lakehouse table** sink panel. The information in this panel, such as the Lakehouse table, catalog name, and warehouse location, is typically prepopulated.

     2. Click **Done**.

  6. In the **Dataflow options** section, click **Run job**.




If you need to further customize the Dataflow pipeline used to import Delta Lake tables, you can do that using the job builder form or the YAML editor.

### Examine the job output

After the job completes, you can verify that the data was copied to the Lakehouse table by querying it in BigQuery.

  1. In the Dataflow job list, check that the job status is **Succeeded**.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. If the job fails or has errors, check the [job logs or worker logs](https://docs.cloud.google.com/dataflow/docs/guides/logging) for details.

  3. In the Google Cloud console, go to the BigQuery **Studio** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  4. In the query editor, enter a SQL query to inspect the table. You can use the `PROJECT_ID.CATALOG.NAMESPACE.TABLE_NAME` convention to query:
         
         SELECT * FROM `PROJECT_ID`.`CATALOG`.`NAMESPACE`.`TABLE_NAME` LIMIT 10;
         

  5. Click play_arrow**Run**.

  6. Review the **Query results** to ensure the data was processed correctly.




## Optional. Enable continuous migration

To set up end-to-end continuous migration from Delta Lake to Lakehouse, complete the following sequence of operations:

  1. Enable the `delta.enableChangeDataFeed` property on the input Delta Lake table.
  2. Perform an initial table migration to a commit ID or timestamp after setting the `delta.enableChangeDataFeed` property.
  3. Run scheduled CDC jobs for subsequent data using a frequency (commit ID or timestamp range) chosen for your workload requirements.



For more information, see [Migrate Delta Lake change data capture (CDC) data into Lakehouse using Dataflow](https://docs.cloud.google.com/lakehouse/docs/migrate-delta-lake-cdc).

## What's next

  * Learn more in the [Introduction to Lakehouse tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/biglake/docs/about-lakehouse-iceberg-rest-catalog-tables).
  * Learn more about periodically [Migrating Delta Lake CDC data into Lakehouse](https://docs.cloud.google.com/lakehouse/docs/migrate-delta-lake-cdc).
  * Learn about [Change data capture ingestion in Lakehouse](https://docs.cloud.google.com/lakehouse/docs/change-data-capture).
  * Learn more about how to [Create a custom job with the job builder UI](https://docs.cloud.google.com/dataflow/docs/guides/job-builder-custom-job).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
