---
url: https://docs.cloud.google.com/bigquery/docs/read-lakehouse-iceberg-rest-catalog-tables-spark/
title: Read Apache Iceberg managed tables with Apache Spark \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:44:49.343003+00:00
---

# Read Apache Iceberg managed tables with Apache Spark  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/read-lakehouse-iceberg-rest-catalog-tables-spark/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Read Apache Iceberg managed tables with Apache Spark

The following sections describe how to read managed tables using Apache Iceberg managed tables (hereafter _Iceberg managed tables_) with Apache Spark.

## Before you begin

  * Understand the different types of BigLake tables and the implications of using them, in the [ BigLake table overview](https://docs.cloud.google.com/biglake/docs/biglake-tables).

  * Before reading Iceberg managed tables with Apache Spark, ensure that you have set up a [Cloud resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection) to a storage bucket. Your connection needs write permissions on the storage bucket, as specified in the following Required roles section. For more information about required roles and permissions for connections, see [Manage connections](https://docs.cloud.google.com/bigquery/docs/working-with-connections).




## Required roles

To get the permissions that you need to let BigQuery manage tables in your project, ask your administrator to grant you the following IAM roles: 

  * To query data: 
    * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on your project
    * [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`) on your project
  * Grant the connection service account the following roles so it can read and write data in Cloud Storage: 
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the bucket
    * [Storage Legacy Bucket Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`) on the bucket



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let BigQuery manage tables in your project. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let BigQuery manage tables in your project:

  * `bigquery.connections.delegate` on your project
  * `bigquery.jobs.create` on your project
  * `bigquery.readsessions.create` on your project
  * `bigquery.tables.get` on your project
  * `bigquery.tables.getData` on your project
  * `storage.buckets.get` on your bucket
  * `storage.objects.create` on your bucket
  * `storage.objects.delete` on your bucket
  * `storage.objects.get` on your bucket
  * `storage.objects.list` on your bucket



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Read Iceberg managed tables with Apache Spark

The following sample sets up your environment to use Spark SQL with Apache Iceberg, and then executes a query to fetch data from a specified Iceberg managed table.
    
    
    spark-sql \
      --packages org.apache.iceberg:iceberg-spark-runtime-ICEBERG_VERSION_NUMBER \
      --conf spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog \
      --conf spark.sql.catalog.CATALOG_NAME.type=hadoop \
      --conf spark.sql.catalog.CATALOG_NAME.warehouse='BUCKET_PATH' \
    
    # Query the table
    SELECT * FROM CATALOG_NAME.FOLDER_NAME;

Replace the following:

  * ICEBERG_VERSION_NUMBER: the current version of Apache Spark Iceberg runtime. Download the latest version from [Spark Releases](https://iceberg.apache.org/releases/).
  * CATALOG_NAME: the catalog to reference your Iceberg managed table.
  * BUCKET_PATH: the path to the bucket containing the table files. For example, `gs://mybucket/`.
  * FOLDER_NAME: the folder containing the table files. For example, `myfolder`.



## What's next

  * [Manage metadata snapshots](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery#create-iceberg-table-snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
