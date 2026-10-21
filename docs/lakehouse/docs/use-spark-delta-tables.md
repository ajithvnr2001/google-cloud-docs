---
url: https://docs.cloud.google.com/lakehouse/docs/use-spark-delta-tables/
title: Set up Spark with Delta tables \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:54.497669+00:00
---

# Set up Spark with Delta tables  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/use-spark-delta-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up Spark with Delta tables Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure Apache Spark with the Lakehouse runtime catalog to use Delta Lake tables. You learn how to create an Apache Hive catalog, configure Spark sessions to connect to the metastore, and run workloads to create and register Delta tables to query in BigQuery.

**Note:** You can't create a new Delta table directly through the Lakehouse runtime catalog Hive endpoint or by using Hive DDL. Instead, use a Delta-compatible engine like Apache Spark to create the underlying table files in Cloud Storage and register the table in the metastore. 

## Before you begin

  1. Read [About the Hive catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore).
  2. Review [Supported storage formats and data types](https://docs.cloud.google.com/lakehouse/docs/spark-hive-formats-types).
  3. Review [Limitations and considerations](https://docs.cloud.google.com/lakehouse/docs/spark-hive-limitations).

  4. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Lakehouse, Managed Service for Apache Spark APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,dataproc.googleapis.com)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Lakehouse, Managed Service for Apache Spark APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,dataproc.googleapis.com)




### Required roles

To get the permissions that you need to use Lakehouse runtime catalog with Delta tables, ask your administrator to grant you the following IAM roles on your project: 

  * Create a Managed Service for Apache Spark cluster: [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) 
  * Cluster service account: 
    * [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)
    * [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * Write access to all Lakehouse runtime catalog resources: [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`) 
  * Read-only access to all Lakehouse runtime catalog resources: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For instructions, see [Granting a single role](https://docs.cloud.google.com/iam/docs/grant-role-console).

## General workflow

To use the Lakehouse runtime catalog with Delta tables, follow this workflow:

  1. Create a Lakehouse Hive catalog.
  2. Configure your Spark session with the Lakehouse metastore client and Delta Lake dependencies.
  3. Create and populate Delta tables in Cloud Storage using Spark, which registers them with the metastore.
  4. Query the Delta tables from Apache Spark (read and write) or directly from BigQuery (read-only).



## Create a Lakehouse Hive catalog

To use the Lakehouse runtime catalog with Spark and Delta tables, create a Hive catalog.

A Lakehouse Hive catalog is a collection of Hive databases. Before running Spark jobs, create a catalog to register it with Lakehouse Metastore. The catalog requires a name and a Cloud Storage location for the data.

###  Console 

  1. In the Google Cloud console, open the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click **Create catalog**.

  3. Select **Lakehouse runtime catalog**.

  4. For **Catalog type** , select **Hive Metastore**.

  5. In the **Select a Cloud Storage bucket** field, enter the Cloud Storage bucket name for your catalog. Alternatively, click **Browse** to choose or create a bucket.

  6. For **Catalog ID** , enter a name for your Lakehouse Hive catalog.

  7. For **Primary location** , specify the same region as your bucket.

  8. Click **Create**.




### gcloud

To create a Hive catalog, run the following command:
    
    
    gcloud biglake hive catalogs create LAKEHOUSE_CATALOG_ID \
        --project=PROJECT_ID \
        --location-uri="gs://GCS_WAREHOUSE_PATH" \
        --primary-location=REGION \
        --description="DESCRIPTION"
    

Replace the following:

  * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

  * `GCS_WAREHOUSE_PATH`: the Cloud Storage path for your warehouse data.

  * `PROJECT_ID`: your Google Cloud project ID.

  * `REGION`: the primary region of the metastore. For single-region buckets, this matches the bucket region. For dual-region or multi-region buckets, specify a constituent region for the primary replica. The other region becomes the secondary replica.

  * `DESCRIPTION`: a description of the catalog.




## Configure Spark to use Delta tables

To use the Lakehouse runtime catalog with Delta tables, configure your Spark session with the Lakehouse metastore client factory and Delta Lake extensions.

### spark-sql

  1. Use [SSH to connect to your Managed Service for Apache Spark cluster's primary node](https://docs.cloud.google.com/dataproc/docs/concepts/accessing/ssh).
  2. Run `spark-sql` on the command line with the following properties to start an interactive Spark SQL session:
         
         spark-sql \
             --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
             --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
             --conf spark.hive.metastore.client.factory.class=com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory \
             --conf spark.hive.metastore.blms.project.id=PROJECT_ID \
             --conf spark.hive.metastore.blms.catalog.default=LAKEHOUSE_CATALOG_ID \
             --conf spark.hive.metastore.warehouse.dir=gs://GCS_WAREHOUSE_PATH
         

  3. After the session starts, Spark connects to Lakehouse runtime catalog.

Run the following commands to create and query Delta resources:
         
         -- Show all the databases in the current project.
         SHOW DATABASES;
         
         -- Create a database.
         CREATE DATABASE spark_delta_blms_database;
         
         -- Create a Delta data source table.
         CREATE TABLE spark_delta_blms_database.delta_quick_start (id INT, name STRING) USING DELTA;
         
         -- Insert data into the table.
         INSERT INTO TABLE spark_delta_blms_database.delta_quick_start VALUES (1, 'my-first-user');
         
         -- Query the Delta table.
         SELECT * FROM spark_delta_blms_database.delta_quick_start;
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your warehouse data.




### Jupyter Notebook

  1. [Run a Jupyter notebook on a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc/docs/concepts/components/jupyter#install_jupyter).
  2. Access the Jupyter web interface from the **Web interfaces** tab of the cluster's details page in the Google Cloud console.
  3. In a new notebook, create a Spark session configured for Delta Lake and run queries:
         
         from pyspark.sql import SparkSession
         
         # If a Spark session exists, stop it first by running spark.stop()
         spark = SparkSession.builder\
             .master("local")\
             .appName("Lakehouse runtime catalog Delta tutorial")\
             .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")\
             .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")\
             .config("spark.hive.metastore.client.factory.class", "com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory")\
             .config("spark.hive.metastore.blms.project.id", "PROJECT_ID")\
             .config("spark.hive.metastore.warehouse.dir", "gs://GCS_WAREHOUSE_PATH")\
             .config("spark.hive.metastore.blms.catalog.default", "LAKEHOUSE_CATALOG_ID")\
             .getOrCreate()
         
         # Show all the databases.
         df = spark.sql("SHOW DATABASES;")
         df.show()
         
         # Create a database.
         spark.sql("CREATE DATABASE jupyter_delta_blms_db")
         
         # Create a Delta data source table.
         spark.sql("CREATE TABLE jupyter_delta_blms_db.delta_table(id INT, name STRING) USING DELTA")
         
         # Insert data into the table.
         spark.sql("INSERT INTO TABLE jupyter_delta_blms_db.delta_table VALUES (1, 'my-first-user');")
         
         # Query from table.
         spark.sql("SELECT * FROM jupyter_delta_blms_db.delta_table;").show()
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your warehouse data.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.




###  BigQuery notebook 

  1. In the Google Cloud console, go to **BigQuery**.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, click **\+ ADD** , and then click **Python notebook**.

  3. In a code cell, configure the Managed Service for Apache Spark session with Delta extensions and Lakehouse runtime catalog properties:
         
         from google.cloud.dataproc_spark_connect import DataprocSparkSession
         from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
         import os
         
         os.environ['DATAPROC_SPARK_CONNECT_DEFAULT_DATASOURCE'] = ""
         
         session = Session()
         session.environment_config.execution_config.ttl = {"seconds": 864000}
         session.runtime_config.version = "2.3"
         session.runtime_config.properties = {
          "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
          "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
          "spark.hive.metastore.blms.project.id": "PROJECT_ID",
          "spark.hive.metastore.blms.catalog.default": "LAKEHOUSE_CATALOG_ID",
          "spark.hive.metastore.warehouse.dir": "gs://GCS_WAREHOUSE_PATH",
          "spark.hive.metastore.client.factory.class": "com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory",
          "spark.sql.catalogImplementation": "hive"
         }
         
         spark = DataprocSparkSession.builder.dataprocSessionConfig(session).getOrCreate()
         print("Spark session created successfully")
         

  4. In another code cell, create a database and Delta table:
         
         # Create a database
         spark.sql("CREATE DATABASE bq_spark_delta_database;")
         
         # Create a Delta data source table
         spark.sql("CREATE TABLE bq_spark_delta_database.delta_quick_start (id INT, name STRING) USING DELTA;")
         
         # Insert data into the table
         spark.sql("INSERT INTO TABLE bq_spark_delta_database.delta_quick_start VALUES (1, 'my-first-user');")
         
         # Query from table
         spark.sql("SELECT * FROM bq_spark_delta_database.delta_quick_start;").show()
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your warehouse data.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.




## Submit a Managed Service for Apache Spark batch job

You can submit a PySpark batch workload to Managed Service for Apache Spark to create and query Delta tables with the Lakehouse runtime catalog.

  1. Create a Python file with a PySpark job:
         
         from pyspark.sql import SparkSession
         
         spark = (
             SparkSession.builder.appName("Lakehouse runtime catalog Delta tutorial")
             .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
             .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
             .config(
                 "spark.hive.metastore.client.factory.class",
                 "com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory",
             )
             .config("spark.hive.metastore.blms.project.id", "PROJECT_ID")
             .config("spark.hive.metastore.blms.catalog.default", "LAKEHOUSE_CATALOG_ID")
             .config(
                 "spark.hive.metastore.warehouse.dir",
                 "gs://GCS_WAREHOUSE_PATH",
             )
             .enableHiveSupport()
             .getOrCreate()
         )
         
         # Show all the databases.
         spark.sql("SHOW DATABASES;").show()
         
         # Create a database.
         spark.sql("CREATE DATABASE dp_serverless_delta_db")
         
         # Create a Delta data source table.
         spark.sql(
             "CREATE TABLE dp_serverless_delta_db.delta_table(id INT, name STRING) USING DELTA"
         )
         
         # Insert data into the table.
         spark.sql("INSERT INTO TABLE dp_serverless_delta_db.delta_table VALUES (1, 'my-first-user');")
         
         # Query from table.
         spark.sql("SELECT * FROM dp_serverless_delta_db.delta_table;").show()
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your warehouse data.

  2. Submit the batch job:
         
         gcloud dataproc batches submit pyspark PYTHON_SCRIPT_FILE \
             --version=2.2 \
             --project=PROJECT_ID \
             --region=REGION \
             --deps-bucket=gs://CLOUD_STORAGE_BUCKET
         

Replace the following:

     * `PYTHON_SCRIPT_FILE`: the local or Cloud Storage path to the PySpark application file.
     * `PROJECT_ID`: your project ID.
     * `REGION`: the region to run the batch job in.
     * `CLOUD_STORAGE_BUCKET`: the Cloud Storage bucket for staging workload dependencies.



## Query Delta tables from BigQuery

After creating Delta tables from Spark in the Lakehouse runtime catalog, you can query them from BigQuery Studio.

Queries executed from BigQuery on Delta tables in the Hive catalog endpoint are read-only.

  1. In the Google Cloud console, go to **BigQuery**.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, enter the following statement:
         
         SELECT * FROM `PROJECT_ID.LAKEHOUSE_CATALOG_ID.DATABASE_NAME.TABLE_NAME`;
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `LAKEHOUSE_CATALOG_ID`: your Hive catalog name.
     * `DATABASE_NAME`: your database name.
     * `TABLE_NAME`: your Delta table name.



## Limitations

When using Delta tables with the Lakehouse runtime catalog Hive catalog endpoint, the following limitations apply:

  * **Read-only queries in BigQuery** : Queries on Delta tables from BigQuery are read-only. Perform data modifications, DML operations, and schema changes using Apache Spark.
  * **Placeholder schema on`GetHiveTable` and true schema inspection**: `GetHiveTable` calls for Delta tables return a placeholder schema instead of the actual table schema. To inspect the real schema of a Delta table, use Apache Spark. BigQuery computes a modified schema adapted for Dremel query execution, which isn't a 1:1 match with the real Delta table schema.
  * **Hive client incompatibility** : Hive clients (like the Hive CLI) don't support Delta tables with the Lakehouse runtime catalog Hive endpoint. Use Apache Spark to manage Delta tables, and Spark or BigQuery to query them.
  * **Catalog-managed operations unsupported** : Catalog-managed mode is unsupported for Delta tables. You can't create a Delta table using standalone metastore DDL. Instead, create Delta tables with external storage locations in Cloud Storage (for example, using Apache Spark) and register them in the catalog.
  * **BigQuery external Delta table limitations** : The Lakehouse runtime catalog Hive endpoint uses the same underlying query engine implementation as BigQuery external Delta Lake tables. All [external Delta Lake table limitations](https://docs.cloud.google.com/bigquery/docs/create-delta-lake-table#limitations) and [BigLake table limitations](https://docs.cloud.google.com/bigquery/docs/biglake-tables#limitations) apply. For example, Change Data Capture (CDC) operations and the BigQuery Storage Read API aren't supported, and `timestamp_ntz` is unsupported.



## What's next

  * [About the Hive catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore).
  * [Supported storage formats and data types](https://docs.cloud.google.com/lakehouse/docs/spark-hive-formats-types).
  * [Limitations and considerations for Hive catalogs](https://docs.cloud.google.com/lakehouse/docs/spark-hive-limitations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
