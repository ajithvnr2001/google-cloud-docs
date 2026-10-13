---
url: https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-features/
title: Additional Lakehouse runtime catalog features \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:43.802462+00:00
---

# Additional Lakehouse runtime catalog features  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-features/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Additional Lakehouse runtime catalog features Stay organized with collections  Save and categorize content based on your preferences. 

To customize your _Lakehouse runtime catalog_ configuration, you can use the following additional features:

  * Apache Spark Iceberg procedures.
  * The filter option for unsupported tables.
  * BigQuery connection overrides.
  * Access control policies for Apache Iceberg tables managed by Lakehouse runtime catalog.



## Use Apache Iceberg Spark procedures

To use [Apache Spark procedures](https://iceberg.apache.org/docs/1.5.1/spark-procedures/), you must include [Apache Iceberg SQL extensions](https://iceberg.apache.org/docs/1.5.1/spark-configuration/#sql-extensions) in your Apache Spark configuration. For example, you can create a procedure to roll back to a previous state.

#### Use interactive Apache Spark SQL to roll back to a previous state

You can use an Apache Spark procedure to create, modify, and roll back a table to its previous state. For example:

  1. Create an Apache Spark table:
         
         spark-sql \
            --jars https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR \
            --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
            --conf spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog \
            --conf spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog \
            --conf spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID \
            --conf spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_DIRECTORY

Replace the following:

     * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Apache Iceberg custom catalog plugin to use. Depending on your Apache Iceberg version number, select one of the following: 
       * Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
       * Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
     * `CATALOG_NAME`: the catalog name that references your Apache Spark table.
     * `PROJECT_ID`: the ID of the Google Cloud project.

     * `WAREHOUSE_DIRECTORY`: the URI of the Cloud Storage folder where your data warehouse is stored.
    
    USE `CATALOG_NAME`;
    CREATE NAMESPACE NAMESPACE_NAME;
    USE NAMESPACE NAMESPACE_NAME;
    CREATE TABLE NAMESPACE_NAME.TABLE_NAME (id int, data string) USING ICEBERG LOCATION 'WAREHOUSE_DIRECTORY';
    INSERT INTO NAMESPACE_NAME.TABLE_NAME VALUES (1, "first row");
    DESCRIBE EXTENDED TABLE_NAME;

Replace the following:

     * `NAMESPACE_NAME`: the namespace name that references your Apache Spark table.
     * `TABLE_NAME`: a table name that references your Apache Spark table.

The output contains details about the table configuration:
    
    ...
    Table Properties [current-snapshot-id=1659239298328512231,format=iceberg/parquet,format-version=2,write.parquet.compression-codec=zstd]
    ...

  2. Alter the table again, and then roll it back to the previously created snapshot `1659239298328512231`:
         
         ALTER TABLE TABLE_NAME ADD COLUMNS (newDoubleCol double);
         INSERT INTO TABLE_NAME VALUES (2, "second row", 2.5);
         SELECT * FROM TABLE_NAME;
         CALL CATALOG_NAME.system.set_current_snapshot('NAMESPACE_NAME.TABLE_NAME', SNAPSHOT_ID);
         SELECT * FROM TABLE_NAME;

Replace the following:

     * `SNAPSHOT_ID`: the ID of the snapshot you are rolling back to.

The output is similar to the following:
    
    1 first row
    Time taken: 0.997 seconds, Fetched 1 row(s)




## Filter unsupported tables from table listing functions

When you use Apache Spark SQL with the Lakehouse runtime catalog, the `SHOW TABLES` command shows all the tables in the specified namespace, even those that aren't compatible with Apache Spark.

To only display supported tables, turn on the `filter_unsupported_tables` option:
    
    
    spark-sql
      --jars https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR \
      --conf spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog \
      --conf spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog \
      --conf spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID \
      --conf spark.sql.catalog.CATALOG_NAME.gcp_location=LOCATION \
      --conf spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_DIRECTORY \
      --conf spark.sql.catalog.CATALOG_NAME.filter_unsupported_tables="true"

Replace the following:

  * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Apache Iceberg custom catalog plugin to use. Depending on your Apache Iceberg version number, select one of the following: 
    * Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
    * Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
  * `CATALOG_NAME`: the name of the Apache Spark catalog to use.
  * `PROJECT_ID`: the ID of the Google Cloud project to use.
  * `LOCATION`: the location of the BigQuery resources.
  * `WAREHOUSE_DIRECTORY`: the Cloud Storage folder to use as the data warehouse.



## Set a BigQuery connection override

You can use BigQuery connections to access data stored outside of BigQuery, such as in Cloud Storage.

To set a BigQuery connection override that provides access to a Cloud Storage bucket, complete the following steps:

  1. In your BigQuery project, create a new connection to your Cloud Storage resource. This connection defines how BigQuery accesses your data.

  2. Grant the user or service account accessing the data the `roles/bigquery.connectionUser` role on the connection.

Make sure that the connection resource shares the same location as the target resources in BigQuery. For more information, see [Manage connections](https://docs.cloud.google.com/bigquery/docs/working-with-connections).

  3. Specify the connection in your Apache Iceberg table with the `bq_connection` property:
         
         CREATE TABLE TABLE_NAME (id int, data string) USING ICEBERG LOCATION 'WAREHOUSE_DIRECTORY' TBLPROPERTIES ('bq_connection'='projects/PROJECT_ID/locations/LOCATION/connections/CONNECTION_ID');

Replace the following:

     * `TABLE_NAME`: a table name for your Apache Spark table.
     * `WAREHOUSE_DIRECTORY`: the URI of the Cloud Storage bucket that stores your data.
     * `PROJECT_ID`: the ID of the Google Cloud project to use.
     * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the connection.
     * `CONNECTION_ID`: the ID of the connection.



## Set access control policies

You can enable fine-grained access control (FGAC) on a managed Iceberg table in BigQuery by configuring access control policies. You can only set access control policies on tables that use a BigQuery connection override. You can set these policies in the following ways:

  * [Column-level security](https://docs.cloud.google.com/bigquery/docs/column-level-security)
  * [Row-level security](https://docs.cloud.google.com/bigquery/docs/managing-row-level-security)
  * [Data masking](https://docs.cloud.google.com/bigquery/docs/column-data-masking)



After you configure your FGAC policies, you can query the table from Apache Spark using the following example:
    
    
    from pyspark.sql import SparkSession
    
    # Create a Spark session
    spark = SparkSession.builder \
    .appName("Lakehouse runtime catalog Iceberg") \
    .config("spark.sql.catalog.CATALOG_NAME", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.CATALOG_NAME.catalog-impl", "org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog") \
    .config("spark.sql.catalog.CATALOG_NAME.gcp_project", "PROJECT_ID") \
    .config("spark.sql.catalog.CATALOG_NAME.gcp_location", "LOCATION") \
    .config("spark.sql.catalog.CATALOG_NAME.warehouse", "WAREHOUSE_DIRECTORY") \
    .getOrCreate()
    
    spark.sql("USE `CATALOG_NAME`;")
    
    # Configure spark for storing temp results
    spark.conf.set("viewsEnabled","true")
    spark.sql("CREATE NAMESPACE IF NOT EXISTS MATERIALIZATION_NAMESPACE");
    spark.conf.set("materializationDataset","MATERIALIZATION_NAMESPACE")
    
    spark.sql("USE NAMESPACE DATASET_NAME;")
    
    sql = """SELECT * FROM DATASET_NAME.ICEBERG_TABLE_NAME"""
    df = spark.read.format("bigquery").load(sql)
    df.show()

Replace the following:

  * `CATALOG_NAME`: the name of your catalog.
  * `PROJECT_ID`: the ID of the project that contains your BigQuery resources.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the BigQuery resources.
  * `WAREHOUSE_DIRECTORY`: the URI of the Cloud Storage folder that contains your data warehouse.
  * `MATERIALIZATION_NAMESPACE`: the namespace where you want to store temporary results.
  * `DATASET_NAME`: the name of your dataset that contains the table that you are querying.
  * `ICEBERG_TABLE_NAME`: the name of the table that you're querying.



## What's next

  * [Create and manage resources in the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/manage-lakehouse-catalog-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
