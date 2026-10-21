---
url: https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-stored-procedures/
title: Use the Lakehouse runtime catalog with Apache Spark stored procedures \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:53:17.429058+00:00
---

# Use the Lakehouse runtime catalog with Apache Spark stored procedures  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-stored-procedures/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Use the Lakehouse runtime catalog with Apache Spark stored procedures Stay organized with collections  Save and categorize content based on your preferences. 

[Apache Spark stored procedures](https://docs.cloud.google.com/bigquery/docs/spark-procedures) execute jobs within _borderless Lakehouse_. By connecting to the _Lakehouse runtime catalog_ , these procedures run Spark SQL commands directly against your underlying data warehouse.

**Note:** The custom Apache Iceberg catalog for BigQuery is a legacy integration option. If you're building new workloads, we recommend using the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), which implements the open standard Apache Iceberg REST Catalog API, supports multiple-bucket catalogs, and offers features such as [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending).

## Before you begin

  1. Enable billing for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  2. Enable the BigQuery and Dataproc APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataproc.googleapis.com)




### Required roles

To use Apache Spark stored procedures, review the required roles for [stored procedures](https://docs.cloud.google.com/bigquery/docs/spark-procedures#required_roles) and grant the necessary roles.

To get the permissions that you need to use Apache Spark and stored procedures with the Lakehouse runtime catalog as a metadata service, ask your administrator to grant you the following IAM roles: 

  * Create Lakehouse runtime catalog tables in Apache Spark: 
    * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the Spark Connection service account in the project
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the Spark Connection service account in the project
  * Query Lakehouse runtime catalog tables in BigQuery : 
    * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the project
    * [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`) on the project
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create and run a stored procedure

The following example shows you how to create and run a stored procedure with the Lakehouse runtime catalog.

  1. Go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, add the following sample code for the [`CREATE PROCEDURE` statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_procedure).
         
         CREATE OR REPLACE PROCEDURE
         `PROJECT_ID.BQ_DATASET_ID.PROCEDURE_NAME`()
         WITH CONNECTION `PROJECT_ID.REGION.SPARK_CONNECTION_ID` OPTIONS (engine='SPARK',
         runtime_version='1.1',
         properties=[("spark.sql.catalog.CATALOG_NAME.warehouse",
         "WAREHOUSE_DIRECTORY"),
         ("spark.sql.catalog.CATALOG_NAME.gcp_location",
         "LOCATION"),
         ("spark.sql.catalog.CATALOG_NAME.gcp_project",
         "PROJECT_ID"),
         ("spark.sql.catalog.CATALOG_NAME",
         "org.apache.iceberg.spark.SparkCatalog"),
         ("spark.sql.catalog.CATALOG_NAME.catalog-impl",
         "org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog"),
         ("spark.jars.packages",
         "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1")],
         jar_uris=["gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar"])
         LANGUAGE python AS R"""
         from pyspark.sql import SparkSession
         spark = SparkSession \
         .builder \
         .appName("Lakehouse runtime catalog Iceberg") \
         .getOrCreate()
         spark.sql("USE CATALOG_NAME;")
         spark.sql("CREATE NAMESPACE IF NOT EXISTS NAMESPACE_NAME;")
         spark.sql("USE NAMESPACE_NAME;")
         spark.sql("CREATE TABLE TABLE_NAME (id int, data string) USING ICEBERG LOCATION 'WAREHOUSE_DIRECTORY'")
         spark.sql("DESCRIBE TABLE_NAME;")
         spark.sql("INSERT INTO TABLE_NAME VALUES (1, \"first row\");")
         spark.sql("SELECT * from TABLE_NAME;")
         spark.sql("ALTER TABLE TABLE_NAME ADD COLUMNS (newDoubleCol double);")
         spark.sql("DESCRIBE TABLE_NAME;")
         """;
         CALL `PROJECT_ID.BQ_DATASET_ID.PROCEDURE_NAME`();

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `BQ_DATASET_ID`: the ID of the dataset in BigQuery that contains the procedure.
     * `PROCEDURE_NAME`: the name of the procedure that you're creating or replacing.
     * `REGION`: the location of your Apache Spark connection.
     * `LOCATION`: the location of your BigQuery resources.
     * `SPARK_CONNECTION_ID`: the ID of your Apache Spark connection.
     * `CATALOG_NAME`: the name of the catalog that you're using.
     * `WAREHOUSE_DIRECTORY`: the URI of the Cloud Storage folder that contains your data warehouse.
     * `NAMESPACE_NAME`: the namespace that you're using.



## What's next

  * Set up [optional Lakehouse runtime catalog features](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
