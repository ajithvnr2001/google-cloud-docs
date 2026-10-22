---
url: https://docs.cloud.google.com/bigtable/docs/import-export/
title: Import and export data \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:10.397498+00:00
---

# Import and export data  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Import and export data

Bigtable lets you import and export datasets to support workload migrations, batch processing, and integrations with other analytics services. You can choose from managed pipelines, streaming ingestion methods, or command-line tools to move data between Bigtable and external storage systems.

## Import data into Bigtable

You can import data into Bigtable in one of the following ways:

BigQuery
    To import BigQuery data into Bigtable, see [Export data to Bigtable (reverse ETL)](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable) in the BigQuery documentation. 
    You can run continuous queries on your BigQuery data and export the results to Bigtable in real time using reverse ETL. For more information, see [Introduction to continuous queries](https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction) in the BigQuery documentation. 
Pub/Sub
    You can stream messages from Pub/Sub directly to a Bigtable table using [Pub/Sub Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions) ([Preview](https://cloud.google.com/products#product-launch-stages)). This method lets you write streaming messages to Bigtable without needing a separate subscriber like Dataflow.

## Move or copy data using a template

You can use the following Dataflow templates to move or copy data between Bigtable and other sources or destinations.

### BigQuery

The following Dataflow template lets you export data from BigQuery to Bigtable.

  * [BigQuery to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-bigtable)



### Apache Cassandra to Bigtable

The following Dataflow template lets you export data from Apache Cassandra to Bigtable.

  * [Apache Cassandra to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cassandra-to-bigtable)



### Avro files

The following Dataflow templates allow you to export data from Bigtable as Avro files and then import the data back into Bigtable. You can execute the templates by using the Google Cloud CLI or the Google Cloud console. The [source code](https://github.com/GoogleCloudPlatform/DataflowTemplates/tree/main/v1/src/main/java/com/google/cloud/teleport/bigtable) is on GitHub.

  * [Bigtable to Cloud Storage Avro](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#cloudbigtabletoavrofile)
  * [Cloud Storage Avro to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#avrofiletocloudbigtable)



### Parquet files

The following Dataflow templates allow you to export data from Bigtable as Parquet files and then import the data back into Bigtable. You can execute the templates by using the gcloud CLI or the Google Cloud console. The [source code](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/src/main/java/com/google/cloud/teleport/bigtable/BigtableToParquet.java) is on GitHub.

  * [Bigtable to Cloud Storage Parquet](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#cloudbigtabletoparquetfile)
  * [Cloud Storage Parquet to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#parquetfiletocloudbigtable)



### SequenceFiles

The following Dataflow templates allow you to export data from Bigtable as SequenceFiles and then import the data back into Bigtable. You can execute the templates by using the Google Cloud CLI or the Google Cloud console.

  * [Bigtable to Cloud Storage SequenceFile](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#cloudbigtabletosequencefile)
  * [Cloud Storage SequenceFile to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#sequencefiletocloudbigtable)



## Import from the Tables page

You can execute many of the import methods described on this page using the Google Cloud console. Import the following types of data from the **Tables** page:

  * CSV data
  * BigQuery data
  * Data that you can import with the Dataflow job builder. This includes the following types of data: 
    * Pub/Sub messages
    * BigQuery table data
    * CSV files, JSON files, and text files in Cloud Storage
    * PostgreSQL, MySQL, Oracle, and SQL Server table data
  * Data that you can import with the Dataflow template. This includes the following types of data:

    * Avro files
    * Cassandra keyspaces and tables
    * Parquet files
    * SequenceFile files



###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table you want to import.

  3. Click **Tables** in the left pane.

The **Tables** page displays a list of tables in the instance.

  4. Next to the name of the table that you want to import data into, click the more_vert **Table action** menu.

  5. Click **Import data** , and then select the type of data that you want to import:

     * If you select CSV, the `cbt` CLI terminal window opens. For more information, see the Import CSV data section of this document.
     * If you select BigQuery, BigQuery Studio opens. Fill out the reverse ETL query and run it.
     * If you select the Dataflow job builder, then the job builder opens. For more information, see [Job builder UI overview](https://docs.cloud.google.com/dataflow/docs/guides/job-builder).
     * If you select Avro, Parquet, SequenceFile, or Cassandra, the console displays a partly completed Dataflow template. Fill out the job template and click **Run job**.



## Export from the Tables page

You can execute some of the export methods described on this page using the Google Cloud console. Export the following types of data from the **Tables** page:

  * Avro files
  * Parquet files
  * SequenceFile files




###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table you want to export.

  3. Click **Tables** in the left pane.

The **Tables** page displays a list of tables in the instance.

  4. Next to the name of the table, click the more_vert **Table action** menu.

  5. Click **Export data** , and then select the file type that you want to export.

The console displays a partly completed Dataflow template.

  6. Fill out the job template and click **Run job**.




## Import CSV data

You can import data from a CSV file into a Bigtable table by using the `cbt` CLI . To do this, you need to make sure that your environment, such as Cloud Shell, can access the CSV file. You can get your CSV file into Cloud Shell in one of the following ways:

**Upload a local CSV file** :

  1. In Cloud Shell, click the more_vert **More** menu and select **Upload**.
  2. Select the CSV file from your local machine.
  3. After you upload the file, refer to the file by its name in the `cbt` CLI command.



**Copy a CSV file from Cloud Storage** :

The `cbt` CLI does not directly support importing from a Cloud Storage bucket. You must first copy the CSV file from Cloud Storage to your Cloud Shell environment. For more information, see [Upload an object to a bucket](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object).

After the CSV file is available in your environment, use the `cbt` CLI command to import the data. For a sample command, see [Batch write many rows based on the input file](https://docs.cloud.google.com/bigtable/docs/cbt-reference#batch_write_many_rows_based_on_the_input_file).

## What's next

  * [Create, copy, or restore from a Bigtable backup.](https://docs.cloud.google.com/bigtable/docs/backups)
  * [Explore concepts related to designing a Bigtable schema.](https://docs.cloud.google.com/bigtable/docs/schema-design)
  * [Migrate to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
