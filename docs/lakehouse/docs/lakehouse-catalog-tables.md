---
url: https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-tables/
title: Use the Lakehouse runtime catalog with tables in BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:53:16.475887+00:00
---

# Use the Lakehouse runtime catalog with tables in BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Use the Lakehouse runtime catalog with tables in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

BigQuery lets you create and manage [standard (built-in) tables](https://docs.cloud.google.com/bigquery/docs/tables), [BigQuery managed Apache Iceberg tables](https://docs.cloud.google.com/bigquery/docs/iceberg-tables), and [external Apache Iceberg tables](https://docs.cloud.google.com/bigquery/docs/iceberg-external-tables). You can then configure an Apache Spark session with the Lakehouse runtime catalog to access and query these tables directly from Managed Service for Apache Spark workloads.

**Note:** The custom Apache Iceberg catalog for BigQuery is a legacy integration option. If you're building new workloads, we recommend using the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), which implements the open standard Apache Iceberg REST Catalog API, supports multiple-bucket catalogs, and offers features such as [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending).

## Before you begin

  1. Enable billing for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  2. Enable the BigQuery and Dataproc APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataproc.googleapis.com)




### Required roles

To get the permissions that you need to use Managed Service for Apache Spark with the Lakehouse runtime catalog as a metadata store, ask your administrator to grant you the following IAM roles: 

  * Create Lakehouse runtime catalog tables in Apache Spark: 
    * [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) on the Managed Service for Apache Spark service account in the project
    * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the Managed Service for Apache Spark service account in the project
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the Managed Service for Apache Spark service account in the project
  * Query Lakehouse runtime catalog tables in BigQuery: 
    * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the project
    * [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`) on the project
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Connect to a table

  1. Create a [dataset](https://docs.cloud.google.com/bigquery/docs/datasets) in the Google Cloud console.
         
         CREATE SCHEMA `PROJECT_ID`.DATASET_NAME;

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project to create the dataset.
     * `DATASET_NAME`: a name for your dataset.
  2. Create a [Cloud resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection).

  3. Create a standard BigQuery table.
         
         CREATE TABLE `PROJECT_ID`.DATASET_NAME.TABLE_NAME (name STRING,id INT64);

Replace the following:

     * `TABLE_NAME`: a name for your table.
  4. Insert data into the standard BigQuery table.
         
         INSERT INTO `PROJECT_ID`.DATASET_NAME.TABLE_NAME VALUES ('test_name1', 123),('test_name2', 456),('test_name3', 789);

  5. Create a [BigQuery managed Apache Iceberg table](https://docs.cloud.google.com/bigquery/docs/iceberg-tables#iceberg-table-workflows).

For example, to create a table, run the following `CREATE` statement.
         
         CREATE TABLE `PROJECT_ID`.DATASET_NAME.ICEBERG_TABLE_NAME(
         name STRING,id INT64
         )
         WITH CONNECTION `CONNECTION_NAME`
         OPTIONS (
         file_format = 'PARQUET',
         table_format = 'ICEBERG',
         storage_uri = 'STORAGE_URI');

Replace the following:

     * `ICEBERG_TABLE_NAME`: a name for your managed Apache Iceberg table. For example, `iceberg_managed_table`.
     * `CONNECTION_NAME`: the name of your connection. You created this in the previous step. For example, `myproject.us.myconnection`.
     * `STORAGE_URI`: a fully qualified Cloud Storage URI. For example, `gs://mybucket/table`.
  6. Insert data into the BigQuery managed Apache Iceberg table.
         
         INSERT INTO `PROJECT_ID`.DATASET_NAME.ICEBERG_TABLE_NAME VALUES ('test_name1', 123),('test_name2', 456),('test_name3', 789);

  7. Create an [external Apache Iceberg table](https://docs.cloud.google.com/bigquery/docs/iceberg-external-tables).

For example, to create an external Apache Iceberg table, run the following `CREATE` statement.
         
         CREATE OR REPLACE EXTERNAL TABLE  `PROJECT_ID`.DATASET_NAME.READONLY_ICEBERG_TABLE_NAME
         WITH CONNECTION `CONNECTION_NAME`
         OPTIONS (
           format = 'ICEBERG',
           uris =
             ['BUCKET_PATH'],
           require_partition_filter = FALSE);

Replace the following:

     * `READONLY_ICEBERG_TABLE_NAME`: a name for your read-only table.
     * `BUCKET_PATH`: the path to the Cloud Storage bucket that contains the data for the external table, in the format `['gs://bucket_name/[folder_name/]file_name']`.
  8. From Apache Spark, query the standard table, BigQuery managed Apache Iceberg table, and external Apache Iceberg table.
         
         from pyspark.sql import SparkSession
         
         # Create a spark session
         spark = SparkSession.builder \
         .appName("Lakehouse runtime catalog Iceberg") \
         .config("spark.sql.catalog.CATALOG_NAME", "org.apache.iceberg.spark.SparkCatalog") \
         .config("spark.sql.catalog.CATALOG_NAME.catalog-impl", "org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog") \
         .config("spark.sql.catalog.CATALOG_NAME.gcp_project", "PROJECT_ID") \
         .config("spark.sql.catalog.CATALOG_NAME.gcp_location", "LOCATION") \
         .config("spark.sql.catalog.CATALOG_NAME.warehouse", "WAREHOUSE_DIRECTORY") \
         .getOrCreate()
         spark.conf.set("viewsEnabled","true")
         
         # Use the Lakehouse runtime catalog
         spark.sql("USE `CATALOG_NAME`;")
         spark.sql("USE NAMESPACE DATASET_NAME;")
         
         # Configure spark for temp results
         spark.sql("CREATE namespace if not exists MATERIALIZATION_NAMESPACE");
         spark.conf.set("materializationDataset","MATERIALIZATION_NAMESPACE")
         
         # List the tables in the dataset
         df = spark.sql("SHOW TABLES;")
         df.show();
         
         # Query the tables
         sql = """SELECT * FROM DATASET_NAME.TABLE_NAME"""
         df = spark.read.format("bigquery").load(sql)
         df.show()
         
         sql = """SELECT * FROM DATASET_NAME.ICEBERG_TABLE_NAME"""
         df = spark.read.format("bigquery").load(sql)
         df.show()
         
         sql = """SELECT * FROM DATASET_NAME.READONLY_ICEBERG_TABLE_NAME"""
         df = spark.read.format("bigquery").load(sql)
         df.show()

Replace the following:

     * `WAREHOUSE_DIRECTORY`: the URI of the Cloud Storage folder that's connected to your BigQuery managed Apache Iceberg table and your external Apache Iceberg table.
     * `CATALOG_NAME`: the name of the catalog that you're using.
     * `MATERIALIZATION_NAMESPACE`: the namespace for storing temp results.
  9. Run the Apache Spark script using Managed Service for Apache Spark.
         
         gcloud dataproc batches submit pyspark SCRIPT_PATH \
           --version=2.2 \
           --project=PROJECT_ID \
           --region=REGION \
           --deps-bucket=YOUR_BUCKET \

Replace the following:

     * `SCRIPT_PATH`: the path to the script that the batch job uses.
     * `PROJECT_ID`: the ID of the Google Cloud project to run the batch job in.
     * `REGION`: the region where your workload runs.
     * `YOUR_BUCKET`: the location of the Cloud Storage bucket to upload workload dependencies. The `gs://` URI prefix of the bucket is not required. You can specify the bucket path or bucket name, for example, `mybucketname1`.



## What's next

  * Set up [optional Lakehouse runtime catalog features](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
