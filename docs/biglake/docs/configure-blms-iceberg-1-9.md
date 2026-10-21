---
url: https://docs.cloud.google.com/biglake/docs/configure-blms-iceberg-1-9/
title: Configure the Lakehouse runtime catalog for Managed Service for Apache Spark using Apache Iceberg 1.9 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:48.303962+00:00
---

# Configure the Lakehouse runtime catalog for Managed Service for Apache Spark using Apache Iceberg 1.9  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/biglake/docs/configure-blms-iceberg-1-9/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Configure the Lakehouse runtime catalog for Managed Service for Apache Spark using Apache Iceberg 1.9 Stay organized with collections  Save and categorize content based on your preferences. 

Configuring the _Custom Apache Iceberg catalog for BigQuery_ to connect with the _Lakehouse runtime catalog_ enables the use of [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) clusters or [ Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs) to create a single, shared catalog.

As part of _borderless Lakehouse_ , this setup lets you use either a [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) cluster or [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs) to create a single, shared catalog.

Once configured, this metadata layer works with open source engines like Apache Spark and Apache Flink to manage your open table formats.

## Before you begin

  1. Enable billing for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  2. Enable the BigQuery and Managed Service for Apache Spark APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataproc.googleapis.com)

  3. Understand how the [Lakehouse runtime catalog works](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-stored-procedures).




### Required roles

To get the permissions that you need to configure the Lakehouse runtime catalog, ask your administrator to grant you the following IAM roles: 

  * Create a Managed Service for Apache Spark cluster: [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) on the Compute Engine default service account in the project 
  * Create Lakehouse runtime catalog tables: 
    * [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) on the Managed Service for Apache Spark VM service account in the project
    * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the Dataproc VM service account in the project
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the Dataproc VM service account in the project
  * Query Lakehouse runtime catalog tables: 
    * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the project
    * [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`) on the project
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure the Lakehouse runtime catalog with Managed Service for Apache Spark

You can configure the Lakehouse runtime catalog with Managed Service for Apache Spark using either Apache Spark or Apache Flink:

###  Apache Spark 

  1. Configure a new cluster. To create a new Managed Service for Apache Spark cluster, run the following [`gcloud dataproc clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create), which contains the settings that you need to use the Lakehouse runtime catalog:
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --project=PROJECT_ID \
             --region=LOCATION \
             --single-node

Replace the following:

     * `CLUSTER_NAME`: a name for your Managed Service for Apache Spark cluster.
     * `PROJECT_ID`: the ID of the Google Cloud project where you're creating the cluster.
     * `LOCATION`: the Compute Engine region where you're creating the cluster.
  2. Submit an Apache Spark job using one of the following methods:

###  Google Cloud CLI 
         
         gcloud dataproc jobs submit spark-sql \
           --project=PROJECT_ID \
           --cluster=CLUSTER_NAME \
           --region=REGION \
           --jars=https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR \
           --properties=spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog,\
           spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog,\
           spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID,\
           spark.sql.catalog.CATALOG_NAME.gcp_location=LOCATION,\
           spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_DIRECTORY \
           --execute="SPARK_SQL_COMMAND"

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project that contains the Managed Service for Apache Spark cluster.
     * `CLUSTER_NAME`: the name of the Managed Service for Apache Spark cluster that you're using to run the Apache Spark SQL job.
     * `REGION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your cluster is located.
     * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Apache Iceberg custom catalog plugin to use. Depending on your Apache Iceberg version number, select one of the following: 
       * Apache Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
       * Apache Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
     * `LOCATION`: the location of the BigQuery resources.
     * `CATALOG_NAME`: the name of the Apache Spark catalog to use with your SQL job.
     * `WAREHOUSE_DIRECTORY`: the Cloud Storage folder that contains your data warehouse. This value starts with `gs://`.
     * `SPARK_SQL_COMMAND`: the Apache Spark SQL query that you want to run. This query includes the commands to create your resources. For example, to create a namespace and table.

###  spark-sql CLI 

     1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

     2. To connect to a Managed Service for Apache Spark VM instance, click **SSH** in the row that lists the Managed Service for Apache Spark cluster main VM instance name, which is the cluster name followed by an `-m` suffix. The output is similar to the following:
            
            Connected, host fingerprint: ssh-rsa ...
            Linux cluster-1-m 3.16.0-0.bpo.4-amd64 ...
            ...
            example-cluster@cluster-1-m:~$
            

     3. In the terminal, run the following initialization command for the Lakehouse runtime catalog:
            
            spark-sql \
              --jars https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR \
              --conf spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog \
              --conf spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog \
              --conf spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID \
              --conf spark.sql.catalog.CATALOG_NAME.gcp_location=LOCATION \
              --conf spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_DIRECTORY

Replace the following:

     * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Apache Iceberg custom catalog plugin to use. Depending on your Apache Iceberg version number, select one of the following: 
       * Apache Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
       * Apache Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
     * `CATALOG_NAME`: the name of the Apache Spark catalog that you're using with your SQL job.
     * `PROJECT_ID`: the Google Cloud project ID for the Lakehouse runtime catalog that your Apache Spark catalog links with.
     * `LOCATION`: the Google Cloud location for the Lakehouse runtime catalog.
     * `WAREHOUSE_DIRECTORY`: the Cloud Storage folder that contains your data warehouse. This value starts with `gs://`.

After you successfully connect to the cluster, your Apache Spark terminal displays the `spark-sql` prompt, which you can use to submit Apache Spark jobs.
    
    spark-sql (default)>
    




###  Apache Flink 

  1. [Create a Managed Service for Apache Spark cluster with the optional Apache Flink component enabled](https://docs.cloud.google.com/dataproc/docs/concepts/components/flink), and ensure that you're using Managed Service for Apache Spark `2.2` or later.

  2. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. In the list of virtual machine instances, click **SSH** to connect to the main Managed Service for Apache Spark cluster VM instance, which is listed as the cluster name followed by an `-m` suffix.

  4. Configure the Custom Apache Iceberg catalog for BigQuery plugin for the Lakehouse runtime catalog:
         
         FLINK_VERSION=1.19
         ICEBERG_VERSION=1.6.1
         
         cd /usr/lib/flink
         
         sudo wget -c https://repo.maven.apache.org/maven2/org/apache/iceberg/iceberg-flink-runtime-${FLINK_VERSION}/${ICEBERG_VERSION}/iceberg-flink-runtime-${FLINK_VERSION}-${ICEBERG_VERSION}.jar -P lib
         
         sudo gcloud storage cp gs://spark-lib/bigquery/iceberg-bigquery-catalog-${ICEBERG_VERSION}-1.0.2.jar lib/

  5. Start the Apache Flink session on YARN:
         
         HADOOP_CLASSPATH=`hadoop classpath`
         
         sudo bin/yarn-session.sh -nm flink-dataproc -d
         
         sudo bin/sql-client.sh embedded \
         -s yarn-session

  6. Create a catalog in Apache Flink:
         
         CREATE CATALOG CATALOG_NAME WITH (
         'type'='iceberg',
         'warehouse'='WAREHOUSE_DIRECTORY',
         'catalog-impl'='org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog',
         'gcp_project'='PROJECT_ID',
         'gcp_location'='LOCATION'
         );

Replace the following:

     * `CATALOG_NAME`: the Apache Flink catalog identifier, which is linked to the Lakehouse runtime catalog.
     * `WAREHOUSE_DIRECTORY`: the base path for the warehouse directory (the Cloud Storage folder where Apache Flink creates files). This value starts with `gs://`.
     * `PROJECT_ID`: the project ID for the Lakehouse runtime catalog that the Apache Flink catalog links with.
     * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the BigQuery resources.



Your Apache Flink session is now connected to the Lakehouse runtime catalog, and you can run Apache Flink SQL commands.

### Manage Lakehouse runtime catalog resources

Now that you're connected to the Lakehouse runtime catalog, you can create and view resources based on the metadata stored in the Lakehouse runtime catalog.

For example, try running the following commands in your interactive Apache Flink SQL session to create an Apache Iceberg database and table.

  1. Use the Custom Apache Iceberg catalog for BigQuery:
         
         USE CATALOG CATALOG_NAME;

Replace `CATALOG_NAME` with your Apache Flink catalog identifier.

  2. Create a database, which creates a dataset in BigQuery:
         
         CREATE DATABASE IF NOT EXISTS DATABASE_NAME;

Replace `DATABASE_NAME` with the name of your new database.

  3. Use the database that you created:
         
         USE DATABASE_NAME;

  4. Create an Apache Iceberg table. The following creates an example sales table:
         
         CREATE TABLE IF NOT EXISTS ICEBERG_TABLE_NAME (
           order_number BIGINT,
           price        DECIMAL(32,2),
           buyer        ROW<first_name STRING, last_name STRING>,
           order_time   TIMESTAMP(3)
         );

Replace `ICEBERG_TABLE_NAME` with a name for your new table.

  5. View table metadata:
         
         DESCRIBE EXTENDED ICEBERG_TABLE_NAME;

  6. List tables in the database:
         
         SHOW TABLES;




### Ingest data into your table

After you create an Apache Iceberg table in the previous section, you can use Apache Flink DataGen as a data source to ingest real-time data into your table. The following steps are an example of this workflow:

  1. Create a temporary table using DataGen:
         
         CREATE TEMPORARY TABLE DATABASE_NAME.TEMP_TABLE_NAME
         WITH (
           'connector' = 'datagen',
           'rows-per-second' = '10',
           'fields.order_number.kind' = 'sequence',
           'fields.order_number.start' = '1',
           'fields.order_number.end' = '1000000',
           'fields.price.min' = '0',
           'fields.price.max' = '10000',
           'fields.buyer.first_name.length' = '10',
           'fields.buyer.last_name.length' = '10'
         )
         LIKE DATABASE_NAME.ICEBERG_TABLE_NAME (EXCLUDING ALL);

Replace the following:

     * `DATABASE_NAME`: the name of the database to store your temporary table.
     * `TEMP_TABLE_NAME`: a name for your temporary table.
     * `ICEBERG_TABLE_NAME`: the name of the Apache Iceberg table that you created in the previous section.
  2. Set the parallelism to 1:
         
         SET 'parallelism.default' = '1';

  3. Set the checkpoint interval:
         
         SET 'execution.checkpointing.interval' = '10second';

  4. Set the checkpoint:
         
         SET 'state.checkpoints.dir' = 'hdfs:///flink/checkpoints';

  5. Start the real-time streaming job:
         
         INSERT INTO ICEBERG_TABLE_NAME SELECT * FROM TEMP_TABLE_NAME;

The output is similar to the following:
         
         [INFO] Submitting SQL update statement to the cluster...
         [INFO] SQL update statement has been successfully submitted to the cluster:
         Job ID: 0de23327237ad8a811d37748acd9c10b
         

  6. To check the status of the streaming job, do the following:

     1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/dataproc/clusters)

     2. Select your cluster.

     3. Click the **Web interfaces** tab.

     4. Click the **YARN ResourceManager** link.

     5. In the **YARN ResourceManager** interface, find your Apache Flink session, and click the **ApplicationMaster** link under **Tracking UI**.

     6. In the **Status** column, confirm that your job status is **Running**.

  7. Query streaming data in the Apache Flink SQL client:
         
         SELECT * FROM ICEBERG_TABLE_NAME
         /*+ OPTIONS('streaming'='true', 'monitor-interval'='3s')*/
         ORDER BY order_time desc
         LIMIT 20;

  8. Query streaming data in BigQuery:
         
         SELECT * FROM `DATABASE_NAME.ICEBERG_TABLE_NAME`
         ORDER BY order_time desc
         LIMIT 20;

  9. Terminate the streaming job in the Apache Flink SQL client:
         
         STOP JOB 'JOB_ID';

Replace `JOB_ID` with the job ID that was displayed in the output when you created the streaming job.




## Configure the Lakehouse runtime catalog with Managed Service for Apache Spark

You can configure the Lakehouse runtime catalog with Managed Service for Apache Spark using either Apache Spark SQL or PySpark.

###  Apache Spark SQL 

  1. Create a SQL file with the Apache Spark SQL commands that you want to run in the Lakehouse runtime catalog. For example, this command creates a namespace and a table:
         
         CREATE NAMESPACE `CATALOG_NAME`.NAMESPACE_NAME;
         CREATE TABLE `CATALOG_NAME`.NAMESPACE_NAME.TABLE_NAME (id int, data string) USING ICEBERG LOCATION 'WAREHOUSE_DIRECTORY';

Replace the following:

     * `CATALOG_NAME`: the catalog name that references your Apache Spark table.
     * `NAMESPACE_NAME`: the namespace name that references your Apache Spark table.
     * `TABLE_NAME`: a table name for your Apache Spark table.
     * `WAREHOUSE_DIRECTORY`: the URI of the Cloud Storage folder where your data warehouse is stored.
  2. Submit an Apache Spark SQL batch job by running the following [`gcloud dataproc batches submit spark-sql` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql):
         
         gcloud dataproc batches submit spark-sql SQL_SCRIPT_PATH \
             --project=PROJECT_ID \
             --region=REGION \
             --subnet=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
             --deps-bucket=BUCKET_PATH \
             --properties="spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog, \
             spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog, \
             spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID, \
             spark.sql.catalog.CATALOG_NAME.gcp_location=LOCATION, \
             spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_DIRECTORY"

Replace the following:

     * `SQL_SCRIPT_PATH`: the path to the SQL file that the batch job uses.
     * `PROJECT_ID`: the ID of the Google Cloud project to run the batch job in.
     * `REGION`: the region where your workload runs.
     * `SUBNET_NAME` (optional): the name of a VPC subnet in the `REGION` that meets the [session subnet requirements](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/network).
     * `BUCKET_PATH`: the location of the Cloud Storage bucket to upload workload dependencies. The `WAREHOUSE_DIRECTORY` is located in this bucket. The `gs://` URI prefix of the bucket is not required. You can specify the bucket path or bucket name, for example, `mybucketname1`.
     * `LOCATION`: the location to run the batch job in.

For more information on submitting Apache Spark batch jobs, see [Run an Apache Spark batch workload](https://docs.cloud.google.com/dataproc-serverless/docs/quickstarts/spark-batch).




### PySpark

  1. Create a Python file with the PySpark commands that you want to run in the Lakehouse runtime catalog.

For example, the following command sets up an Apache Spark environment to interact with Apache Iceberg tables stored in the Lakehouse runtime catalog. The command then creates a new namespace and an Apache Iceberg table within that namespace.
         
         from pyspark.sql import SparkSession
         
         spark = SparkSession.builder \
         .appName("Lakehouse runtime catalog Iceberg") \
         .config("spark.sql.catalog.CATALOG_NAME", "org.apache.iceberg.spark.SparkCatalog") \
         .config("spark.sql.catalog.CATALOG_NAME.catalog-impl", "org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog") \
         .config("spark.sql.catalog.CATALOG_NAME.gcp_project", "PROJECT_ID") \
         .config("spark.sql.catalog.CATALOG_NAME.gcp_location", "LOCATION") \
         .config("spark.sql.catalog.CATALOG_NAME.warehouse", "WAREHOUSE_DIRECTORY") \
         .getOrCreate()
         
         spark.sql("USE `CATALOG_NAME`;")
         spark.sql("CREATE NAMESPACE IF NOT EXISTS NAMESPACE_NAME;")
         spark.sql("USE NAMESPACE_NAME;")
         spark.sql("CREATE TABLE TABLE_NAME (id int, data string) USING ICEBERG LOCATION 'WAREHOUSE_DIRECTORY';")

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project to run the batch job in.
     * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) where the BigQuery resources are located.
     * `CATALOG_NAME`: the catalog name that references your Apache Spark table.
     * `TABLE_NAME`: a table name for your Apache Spark table.
     * `WAREHOUSE_DIRECTORY`: the URI of the Cloud Storage folder where your data warehouse is stored.
     * `NAMESPACE_NAME`: the namespace name that references your Apache Spark table.
  2. Submit the batch job using the following [`gcloud dataproc batches submit pyspark` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark):
         
         gcloud dataproc batches submit pyspark PYTHON_SCRIPT_PATH \
             --version=2.2 \
             --project=PROJECT_ID \
             --region=REGION \
             --deps-bucket=BUCKET_PATH \
             --properties="spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog,spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog,spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID,spark.sql.catalog.CATALOG_NAME.gcp_location=LOCATION,spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_DIRECTORY"

Replace the following:

     * `PYTHON_SCRIPT_PATH`: the path to the Python script that the batch job uses.
     * `PROJECT_ID`: the ID of the Google Cloud project to run the batch job in.
     * `REGION`: the region where your workload runs.
     * `BUCKET_PATH`: the location of the Cloud Storage bucket to upload workload dependencies. The `gs://` URI prefix of the bucket is not required. You can specify the bucket path or bucket name, for example, `mybucketname1`.

For more information on submitting PySpark batch jobs, see the [PySpark gcloud reference](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark).




## What's next

  * [Create and manage resources](https://docs.cloud.google.com/lakehouse/docs/manage-lakehouse-catalog-resources).
  * Set up [optional Lakehouse runtime catalog features](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
