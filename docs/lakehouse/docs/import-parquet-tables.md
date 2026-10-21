---
url: https://docs.cloud.google.com/lakehouse/docs/import-parquet-tables/
title: Import Parquet files in storage into Lakehouse runtime catalog using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:59.953959+00:00
---

# Import Parquet files in storage into Lakehouse runtime catalog using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/import-parquet-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Import Parquet files in storage into Lakehouse runtime catalog using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

You can use a Dataflow job builder blueprint to add existing Apache Parquet files from cloud-based storage (Cloud Storage, Amazon S3, or Azure Blob Storage) to an Apache Iceberg table in borderless Lakehouse.

This process uses the [`IcebergAddFiles` transform](https://github.com/apache/beam/blob/master/sdks/java/io/iceberg/src/main/java/org/apache/beam/sdk/io/iceberg/AddFiles.java). If your Parquet files are in Cloud Storage, this transform registers the files with Lakehouse without moving or rewriting the underlying data. If your files are in an external storage system like Amazon S3, they are copied to Cloud Storage for faster querying through Lakehouse, and then registered.

Use the following connection details to add Parquet files from cloud-based storage to an Apache Iceberg table in Lakehouse.

## Before you begin

  1. Enable the Dataflow, BigQuery, and Lakehouse APIs.

  2. To get the permissions that you need to create the resources, ask your administrator to grant you the required Identity and Access Management (IAM) roles on your project.

  3. Create a Lakehouse catalog, namespace, and table to import data into.

  4. Create a cloud-based storage bucket (Cloud Storage, Amazon S3, or Azure Blob Storage) and upload your Parquet files to the bucket.

  5. If the cloud-based storage bucket you're using isn't Google's Cloud Storage, create a Cloud Storage bucket to store your job error logs.




## Support and limitations

Importing Parquet files in cloud-based storage to Lakehouse using Dataflow has the following limitations:

  * The source data must be in Apache Parquet format and stored in Cloud Storage, Amazon S3 or Azure Blob Storage.
  * This feature supports only batch pipelines.



## Import Parquet files to Lakehouse

Use the following steps to import Parquet files from cloud-based storage to an Iceberg table in Lakehouse using the Dataflow job builder UI.

  1. In the Google Cloud console, go to the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake/metastore/catalogs)

  2. Select the catalog, namespace, and table that you want to import data into.

  3. On the **Table details** page, click download**Import table** , and then select **From Apache Parquet files (Batch)**.

The Dataflow **Job builder** page opens.

  4. In the **Sources** section:

     1. Open the **CreateGlobalInput** source entry that is already created.

     2. In the **YAML source configuration** editor section, enter one or more paths to your Parquet files in the `elements` sequence.

To improve import efficiency, specify multiple sets of files (_globs_) when you're registering a large number of files. For example:
            
            reshuffle: true
            elements:**  -   gs://BUCKET_NAME/restaurant-data/2023/*.parquet
              -   gs://BUCKET_NAME/restaurant-data/2024/*.parquet**
            

     3. Click **Done**.

  5. In the **Transforms** section:

     1. Click the **IcebergAddFiles** transform section to open it.

     2. In the **Iceberg table** field, enter the namespace and table name. For example: NAMESPACE .TABLE_NAME .

     3. Under expand_more**Catalog properties** , configure the following items:

        1. **warehouse** : The Cloud Storage location of your catalog. For example, `gs://CATALOG_PATH`.

        2. **header.x-goog-user-project** : Your Google Cloud project ID: PROJECT_ID.

        3. Click **Done**.

     4. If you are migrating from Amazon S3 or Azure Blob Storage you need to provide additional configurations to copy Parquet files to Cloud Storage. This is not required if your files are already in Cloud Storage.

        1. Click the **CopyFilesToGCS** transform section to open it.

        2. Set the value of the **gcs_file_path** configuration parameter to provide the fully qualified Cloud Storage bucket to copy temporary files to. We recommend using the same Cloud Storage bucket used by the Lakehouse warehouse.

        3. Click **Done**.

        4. Click the **Dataflow Options** section to open it.

        5. If your Parquet files are in Amazon S3, click **add additional pipeline options** to provide Apache Beam [pipeline options related to S3](https://beam.apache.org/releases/pydoc/current/_modules/apache_beam/options/pipeline_options.html#S3Options). For example, **s3_region_name** , **s3_access_key_id** , **s3_secret_access_key** , and their corresponding values.

        6. If your Parquet files are in Azure Blob Storage, click **add additional pipeline options** to provide Apache Beam [pipeline options related to Azure](https://beam.apache.org/releases/pydoc/current/_modules/apache_beam/options/pipeline_options.html#AzureOptions). For example, **azure_connection_string** , **blob_service_endpoint** , **azure_managed_identity_client_id** , and their corresponding values.

  6. In the **Sinks** section:

     1. Click the **Write results** sink to open it.

     2. In the **JSON location** field, specify the Cloud Storage location and filename to write error results. For example:
            
            gs://BUCKET_NAME/errors/errors.json
            

     3. Click **Done**.

  7. In the **Dataflow Options** section, click **Run job**.




If you need to further customize the Dataflow pipeline used to register Parquet files, you can do that using the job builder form or the YAML editor.

### Examine the job output

After the job completes, you can verify that the data was registered with the Iceberg table by querying it in BigQuery.

  1. In the Dataflow job list, check that the job status is **Succeeded**.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. If the job fails or has errors, check the JSON error log file in Cloud Storage for details.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. In the Google Cloud console, go to the BigQuery **Studio** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  4. In the query editor, enter a SQL query to inspect the table. You can use `PROJECT_ID.CATALOG.NAMESPACE.TABLE_NAME` convention to query.
         
         SELECT * FROM `PROJECT_ID.CATALOG.NAMESPACE.TABLE_NAME` LIMIT 10
         

  5. Click play_arrow**Run**.

  6. Review the **Query results** to ensure the data was processed correctly.




## What's next

  * Learn more in [About Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-blms).
  * Learn more in the [Dataflow Job builder UI overview](https://docs.cloud.google.com/dataflow/docs/guides/job-builder).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
