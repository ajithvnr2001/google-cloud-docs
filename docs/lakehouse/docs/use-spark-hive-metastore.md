---
url: https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore/
title: Set up Spark and Hive with the Lakehouse runtime catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:50:05.271864+00:00
---

# Set up Spark and Hive with the Lakehouse runtime catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up Spark and Hive with the Lakehouse runtime catalog Stay organized with collections  Save and categorize content based on your preferences. 

The Lakehouse runtime catalog lets you run Apache Spark and Apache Hive workloads with unified metadata so that you can query your tables directly in BigQuery. To manage these workloads, you create an Apache Hive catalog endpoint, configure your Spark sessions to connect to the metastore, and run Spark jobs to generate queryable tables.

## Before you begin

  1. Read [About Hive Catalogs in Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore) to understand how Spark connects to the Lakehouse runtime catalog.
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

To get the permissions that you need to use Lakehouse runtime catalog, ask your administrator to grant you the following IAM roles on your project: 

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

To use the Lakehouse runtime catalog with Spark and Hive, you follow this general workflow:

  1. Create a Lakehouse Hive catalog endpoint.
  2. Configure your Spark session by using your preferred tool (such as Managed Service for Apache Spark or BigQuery Studio).
  3. Perform database and table operations within your Spark session.
  4. Submit batch workloads to Managed Service for Apache Spark and query the resulting tables directly from BigQuery.



## Create a Lakehouse Hive catalog

To use the Lakehouse runtime catalog with Spark and Hive, you must first create a Hive catalog.

A Lakehouse Hive catalog is a collection of Hive databases. Before you run Spark jobs, create a catalog to register it with Lakehouse Metastore. The catalog has a name and a Cloud Storage location where the Hive data resides.

###  Console 

  1. In the Google Cloud console, open the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click **Create catalog**.

  3. Select **Lakehouse runtime catalog**.

  4. For **Catalog type** , select **Hive Metastore**.

  5. In the **Select a Cloud Storage bucket** field, enter the name of the Cloud Storage bucket to use with your catalog. Alternatively, click **Browse** to choose an existing bucket or create a new one.

  6. For **Catalog ID** , give a name to your Lakehouse Hive catalog.

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

  * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.

  * `PROJECT_ID`: your Google Cloud project ID.

  * `REGION`: the primary region of the metastore. For single-region buckets, it should match the bucket region. For dual-region or multi-region buckets, it should be one of the constituent regions and where the primary replica of the metastore is intended. The other region becomes the secondary replica.

  * `DESCRIPTION`: a description of the catalog.




### curl

  1. To create a Hive catalog, run the following command:


    
    
    curl -X POST -s -i -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -d '{"locationUri": "gs://GCS_WAREHOUSE_PATH", "description": "DESCRIPTION"}' \
        -H "Content-Type: application/json" \
        "https://biglake.googleapis.com/hive/v1/projects/PROJECT_ID/catalogs?hiveCatalogId=LAKEHOUSE_CATALOG_ID&primary_location=REGION"
    

Replace the following:

  * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

  * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.

  * `PROJECT_ID`: your Google Cloud project ID.

  * `REGION`: the primary region of the metastore. For single-region buckets, it should match the bucket region. For dual-region or multi-region buckets, it should be one of the constituent regions and where the primary replica of the metastore is intended. The other region becomes the secondary replica.

To route Hive catalog requests directly to a specific region for data residency and sovereignty requirements, you can use [regional endpoints](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints) (`https://biglake.LOCATION.rep.googleapis.com`).

  * `DESCRIPTION`: a description of the catalog.




## Configure and use Spark and Hive

To use the Lakehouse runtime catalog, you must configure your Spark session with specific properties. You can set these properties when you create a Managed Service for Apache Spark cluster or specify them each time you create a session.

### Spark configuration properties

Configure your Spark session or job submission with the following properties to connect to the Apache Hive catalog endpoint:

Property | Value | Description  
---|---|---  
`spark.hive.metastore.client.factory.class` | `com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory` | Configures Spark to use the Lakehouse runtime catalog Hive client factory.  
`spark.hive.metastore.blms.project.id` | `PROJECT_ID` | Specifies the Google Cloud project ID that contains the Hive catalog.  
`spark.hive.metastore.blms.catalog.default` | `LAKEHOUSE_CATALOG_ID` | Specifies the default Hive catalog ID in the Lakehouse runtime catalog.  
`spark.hive.metastore.warehouse.dir` | `gs://GCS_WAREHOUSE_PATH` | Specifies the Cloud Storage URI for the Hive warehouse directory.  
`spark.sql.catalogImplementation` | `hive` | Enables Hive catalog support in the Spark session.  
`spark.sql.addPartitionInBatch.size` | `900` | Optional: sets the maximum batch size for partition ingestion operations. For more information, see [Partition batch size](https://docs.cloud.google.com/lakehouse/docs/spark-hive-limitations#partition-size).  
`spark.sql.extensions` | `io.delta.sql.DeltaSparkSessionExtension` | Optional: enables Delta Lake SQL extensions when using [Delta tables](https://docs.cloud.google.com/lakehouse/docs/use-spark-delta-tables) with a Hive catalog.  
`spark.sql.catalog.spark_catalog` | `org.apache.spark.sql.delta.catalog.DeltaCatalog` | Optional: configures the Delta catalog implementation when using [Delta tables](https://docs.cloud.google.com/lakehouse/docs/use-spark-delta-tables) with a Hive catalog.  
  
Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.

  * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

  * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.




### Run Spark and Hive queries

After the session is established, you can perform operations such as listing existing databases, creating databases, defining tables, and inserting data:

### spark-sql

  1. Use [SSH to connect to your Managed Service for Apache Spark cluster's primary node](https://docs.cloud.google.com/dataproc/docs/concepts/accessing/ssh).
  2. Run `spark-sql` on the command line with the following properties to start an interactive Spark SQL session:
         
         spark-sql \
             --conf spark.hive.metastore.client.factory.class=com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory \
             --conf spark.hive.metastore.blms.project.id=PROJECT_ID \
             --conf spark.hive.metastore.blms.catalog.default=LAKEHOUSE_CATALOG_ID \
             --conf spark.hive.metastore.warehouse.dir=gs://GCS_WAREHOUSE_PATH
         

  3. After the session starts, Spark connects to Lakehouse runtime catalog.

Run the following commands to create and query resources:
         
         -- Show all the databases in the current project.
         SHOW DATABASES;
         
         -- Create a database.
         CREATE DATABASE spark_blms_database;
         
         -- Create a Parquet datasource table.
         CREATE TABLE spark_blms_database.parquet_quick_start (id INT, name STRING) USING PARQUET;
         
         -- Insert data into the table.
         INSERT INTO TABLE spark_blms_database.parquet_quick_start VALUES (1, 'my-first-user');
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.




### Jupyter Notebook

  1. Complete the instructions to [run a Jupyter notebook on a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc/docs/concepts/components/jupyter#install_jupyter).
  2. Access the Jupyter web interface from the **Web interfaces** tab of the cluster's details page in the Google Cloud console.
  3. In a new notebook, create a Spark session and then run the following queries:
         
         from pyspark.sql import SparkSession
         
         # If a Spark session exists, stop it first by running spark.stop()
         spark = SparkSession.builder\
             .master("local")\
             .appName("Lakehouse runtime catalog tutorial")\
             .config("spark.hive.metastore.client.factory.class", "com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory")\
             .config("spark.hive.metastore.blms.project.id", "PROJECT_ID")\
             .config("spark.hive.metastore.warehouse.dir", "gs://GCS_WAREHOUSE_PATH")\
             .config("spark.hive.metastore.blms.catalog.default", "LAKEHOUSE_CATALOG_ID")\
             .getOrCreate()
         
         # Show all the databases.
         df = spark.sql("SHOW DATABASES;")
         df.show()
         
         # Create a database.
         spark.sql("CREATE DATABASE jupyter_blms_db")
         
         # Create a Parquet datasource table.
         spark.sql("CREATE TABLE jupyter_blms_db.parquet_table(id INT, name STRING) USING PARQUET")
         
         # Insert data into the table.
         spark.sql("INSERT INTO TABLE jupyter_blms_db.parquet_table VALUES (1, 'my-first-user');")
         
         # Query from table.
         spark.sql("SELECT * FROM jupyter_blms_db.parquet_table;").show()
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.




###  BigQuery notebook 

  1. In the Google Cloud console, go to **BigQuery**.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, click **\+ ADD** , and then click **Python notebook**.

  3. In a code cell, configure the Managed Service for Apache Spark session and Lakehouse runtime catalog properties:
         
         from google.cloud.dataproc_spark_connect import DataprocSparkSession
         from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
         import os
         
         os.environ['DATAPROC_SPARK_CONNECT_DEFAULT_DATASOURCE'] = ""
         
         session = Session()
         session.environment_config.execution_config.ttl = {"seconds": 864000}
         session.runtime_config.version = "2.3"
         session.runtime_config.properties = {
          "spark.hive.metastore.blms.project.id": "PROJECT_ID",
          "spark.hive.metastore.blms.catalog.default": "LAKEHOUSE_CATALOG_ID",
          "spark.hive.metastore.warehouse.dir": "gs://GCS_WAREHOUSE_PATH",
          "spark.hive.metastore.client.factory.class": "com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory",
          "spark.sql.catalogImplementation": "hive"
         }
         
         spark = DataprocSparkSession.builder.dataprocSessionConfig(session).getOrCreate()
         print("Spark session created successfully")
         

  4. In another code cell, create a database and table:
         
         # Create a database
         spark.sql("CREATE DATABASE bq_spark_blms_database;")
         
         # Create a parquet datasource table
         spark.sql("CREATE TABLE bq_spark_blms_database.parquet_quick_start (id INT, name STRING) USING PARQUET;")
         
         # Insert data into the table
         spark.sql("INSERT INTO TABLE bq_spark_blms_database.parquet_quick_start VALUES (1, 'my-first-user');")
         
         # Query from table
         spark.sql("select * from bq_spark_blms_database.parquet_quick_start;").show()
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.




### Hive CLI

To use the Hive CLI, you must configure it to connect to the metastore. You can do this in one of two ways:

  * **Option 1: Permanent configuration.** Update the `/etc/hive/conf/hive-site.xml` file on your primary node.
  * **Option 2: Temporary configuration.** Provide configuration flags when you start the CLI.



To configure the CLI and run your query session, follow these steps:

  1. Use [SSH to connect to your Managed Service for Apache Spark cluster's primary node](https://docs.cloud.google.com/dataproc/docs/concepts/accessing/ssh).
  2. Depending on your configuration method, do one of the following:

     * **To configure permanently (Option 1):**

       1. Open `/etc/hive/conf/hive-site.xml` on the primary node and add the following properties:
              
              <property>
                  <name>hive.metastore.blms.project.id</name>
                  <value>PROJECT_ID</value>
                  <description></description>
              </property>
              
              <property>
                  <name>hive.metastore.client.factory.class</name>
                  <value>com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory</value>
                  <description></description>
              </property>
              <property>
                  <name>hive.metastore.blms.catalog.default</name>
                  <value>LAKEHOUSE_CATALOG_ID</value>
                  <description></description>
              </property>
              <property>
                  <name>hive.metastore.warehouse.dir</name>
                  <value>gs://GCS_WAREHOUSE_PATH</value>
                  <description></description>
              </property>
              

       2. Start the Hive CLI:
              
              hive
              

     * **To configure temporarily on startup (Option 2):** Start the Hive CLI with configuration flags:
           
           hive \
           --hiveconf hive.metastore.blms.project.id="PROJECT_ID" \
           --hiveconf hive.metastore.blms.catalog.default="LAKEHOUSE_CATALOG_ID" \
           --hiveconf hive.metastore.client.factory.class=com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory \
           --hiveconf hive.metastore.warehouse.dir="gs://GCS_WAREHOUSE_PATH"
           

  3. Then, run the following commands in the Hive CLI session:
         
         show databases;
         create database hive_query_test;
         create table hive_query_test.parquet_table (id INT, name STRING) stored as PARQUET;
         select * from hive_query_test.parquet_table;
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.




## Submit a Managed Service for Apache Spark batch job

You can submit a PySpark batch workload to Managed Service for Apache Spark that uses the Lakehouse runtime catalog.

This PySpark snippet initializes a Spark session configured to connect with the Lakehouse runtime catalog. It sets essential properties such as the Lakehouse client factory, Google Cloud project ID, default catalog, and warehouse directory. After establishing the session, the code demonstrates how to list existing databases, create a new database, and define a Parquet-formatted table within that database by using Spark SQL commands.

  1. Create a Python file with a PySpark job:
         
         from pyspark.sql import SparkSession
         
         spark = (
             SparkSession.builder.appName("Lakehouse runtime catalog tutorial")
             .config(
                "spark.hive.metastore.client.factory.class",
         "com.google.cloud.bigquery.metastore.client.BigLakeMetastoreClientFactory")
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
         spark.sql("CREATE DATABASE dp_serverless_test")
         
         # Create a Parquet datasource table.
         spark.sql(
                 "CREATE TABLE dp_serverless_test.parquet_table(id INT, name STRING) USING"
                 " PARQUET"
             )
         
         # Query from table.
         spark.sql("SELECT * from  dp_serverless_test.parquet_table").show()
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `LAKEHOUSE_CATALOG_ID`: the Hive catalog name.

     * `GCS_WAREHOUSE_PATH`: the Cloud Storage path that stores your Hive warehouse.

  2. Submit the batch job:
         
         gcloud dataproc batches submit pyspark PYTHON_SCRIPT_FILE \
             --version=2.2 \
             --project=PROJECT_ID \
             --region=REGION \
             --deps-bucket=gs://CLOUD_STORAGE_BUCKET
         

Replace the following:

     * `PYTHON_SCRIPT_FILE`: The path to the PySpark application file. It can be a local path or the Cloud Storage object path.
     * `PROJECT_ID`: Your project ID.
     * `REGION`: The region to run the batch job in.
     * `CLOUD_STORAGE_BUCKET`: The name of the Cloud Storage bucket used to stage any workload's dependencies.



## Query the table from BigQuery

After you create resources from Spark in the Lakehouse runtime catalog, you can query them from BigQuery Studio.

  1. In the Google Cloud console, go to **BigQuery**.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, enter the following statement:
         
         SELECT * FROM `PROJECT_ID.LAKEHOUSE_CATALOG_ID.DATABASE_NAME.TABLE_NAME`;
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `LAKEHOUSE_CATALOG_ID`: your Hive catalog name.
     * `DATABASE_NAME`: your database name.
     * `TABLE_NAME`: your table name.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
