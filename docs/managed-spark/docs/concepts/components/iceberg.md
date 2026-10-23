---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/iceberg/
title: Managed Service for Apache Spark optional Iceberg component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:14.335127+00:00
---

# Managed Service for Apache Spark optional Iceberg component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/iceberg/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Iceberg component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Iceberg when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes how you can optionally install the Iceberg component on a Managed Service for Apache Spark cluster.

## Overview

[Apache Iceberg](https://iceberg.apache.org/) is an open table format for large analytic datasets. It brings the reliability and simplicity of SQL tables to Big Data, while making it possible for engines such as Spark, Trino, PrestoDB, Flink, and Hive to safely work with the same tables at the same time.

When installed on a Managed Service for Apache Spark cluster, the [Apache Iceberg](https://iceberg.apache.org/) component installs Iceberg libraries and configures Spark and Hive to work with Iceberg on the cluster.

### Key Iceberg features

Iceberg features include the following:

  * **Schema evolution:** Add, remove, or rename columns without rewriting the entire table.
  * **Time travel:** Query historical table snapshots for auditing or rollback purposes.
  * **Hidden partitioning:** Optimize data layout for faster queries without exposing partition details to users.
  * **ACID transactions:** Ensure data consistency and prevent conflicts.



## Compatible Managed Service for Apache Spark image versions

You can install the Iceberg component on Managed Service for Apache Spark clusters created with [2.2.47](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.2) and later image versions. The Iceberg version installed on the cluster is listed in the [2.2 release versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.2) page.

**Note:** Managed Service for Apache Spark image version `3.0` includes Hive 4.2, which supports Iceberg through the Iceberg REST catalog.

## Iceberg related properties

When you create a Managed Service for Apache Spark with Iceberg cluster, the following Spark and Hive properties are configured to work with Iceberg.

### 2.x image version

The following Spark and Hive properties are configured on Managed Service for Apache Spark `2.x` clusters when the Iceberg component is installed:

Config file | Property | Default value  
---|---|---  
`/etc/spark/conf/spark-defaults.conf` | `spark.sql.extensions` | `org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions`  
`spark.driver.extraClassPath` | `/usr/lib/iceberg/lib/iceberg-spark-runtime-spark-version_scala-version.jar`  
`spark.executor.extraClassPath` | `/usr/lib/iceberg/lib/iceberg-spark-runtime-spark-version_scala-version.jar`  
`/etc/hive/conf/hive-site.xml` | `hive.aux.jars.path` | `file:///usr/lib/iceberg/lib/iceberg-hive-runtime.jar`  
`iceberg.engine.hive.enabled` | `true`  
  
### 3.0 image version

The following Spark and Hive properties are configured on Managed Service for Apache Spark `3.0` clusters when the Iceberg component is installed:

Config file | Property | Default value  
---|---|---  
`/etc/spark/conf/spark-defaults.conf` | `spark.sql.extensions` | `org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions`  
`spark.sql.catalog.default_iceberg` | `org.apache.iceberg.spark.SparkCatalog`  
`spark.sql.catalog.default_iceberg.type` | `rest`  
`spark.sql.catalog.default_iceberg.uri` | `env:ICEBERG_REST_CATALOG_URI`  
`/etc/hive/conf/hive-site.xml` | `iceberg.engine.hive.enabled` | `true`  
  
## Install the Iceberg optional component

Install the Iceberg component when you [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster). The [Managed Service for Apache Spark cluster image version list](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions) pages show the Iceberg component version included in the latest Managed Service for Apache Spark cluster image versions.

### Google Cloud console

To create a Managed Service for Apache Spark cluster that installs the Iceberg component, complete the following steps in the Google Cloud console:

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Iceberg**.
  5. Click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that installs the Iceberg component, use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--optional-components` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --optional-components=ICEBERG \
         other flags ...
    

Replace the following:

  * CLUSTER_NAME: The new cluster name.
  * REGION: The [cluster region](https://docs.cloud.google.com/compute/docs/regions-zones#available).



### REST API

To create a Managed Service for Apache Spark cluster that installs the Iceberg optional component, specify the Iceberg [`SoftwareConfig.Component`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

## Use Iceberg tables with Spark and Hive

After creating a Managed Service for Apache Spark cluster that has the Iceberg optional component installed on the cluster, you can use Spark and Hive to read and write Iceberg table data.

### Spark

### Configure a Spark session for Iceberg

You can use the gcloud CLI command locally, or the `spark-shell` or `pyspark` REPLs (Read-Eval-Print Loops) running on the dataproc cluster master node to enable Iceberg's Spark extensions and set up the Spark catalog to use Iceberg tables.

### gcloud

Run the following gcloud CLI example in a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) to submit a Spark job and set Spark properties to configure the Spark session for Iceberg.
    
    
    gcloud dataproc jobs submit spark  \
        --cluster=CLUSTER_NAME \
        --region=REGION \
        --properties="spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions" \
        --properties="spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog" \
        --properties="spark.sql.catalog.CATALOG_NAME.type=hadoop" \
        --properties="spark.sql.catalog.CATALOG_NAME.warehouse=gs://BUCKET/FOLDER" \
         other flags ...
    

Replace the following:

  * CLUSTER_NAME: The cluster name.
  * REGION: The [Compute Engine](https://docs.cloud.google.com/compute/docs/regions-zones#available) region.
  * CATALOG_NAME: Iceberg catalog name.
  * BUCKET and FOLDER: The Iceberg catalog location in Cloud Storage.



### spark-shell

To configure a Spark session for Iceberg using the `spark-shell` REPL on the Managed Service for Apache Spark cluster, complete the following steps:

  1. Use [SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the master node of the Managed Service for Apache Spark cluster.

  2. Run the following command in the SSH session terminal to configure the Spark session for Iceberg.



    
    
    spark-shell \
        --conf "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions" \
        --conf "spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog" \
        --conf "spark.sql.catalog.CATALOG_NAME.type=hadoop" \
        --conf "spark.sql.catalog.CATALOG_NAME.warehouse=gs://BUCKET/FOLDER"
    

Replace the following:

  * CLUSTER_NAME: The cluster name.
  * REGION: The [Compute Engine](https://docs.cloud.google.com/compute/docs/regions-zones#available) region.
  * CATALOG_NAME: Iceberg catalog name.
  * BUCKET and FOLDER: The Iceberg catalog location in Cloud Storage.



### pyspark shell

To configure a Spark session for Iceberg using the `pyspark` REPL on the Managed Service for Apache Spark cluster, complete the following steps:

  1. Use [SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the master node of the Managed Service for Apache Spark cluster.

  2. Run the following command in the SSH session terminal to configure the Spark session for Iceberg:



    
    
    pyspark \
        --conf "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions" \
        --conf "spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog" \
        --conf "spark.sql.catalog.CATALOG_NAME.type=hadoop" \
        --conf "spark.sql.catalog.CATALOG_NAME.warehouse=gs://BUCKET/FOLDER"
    

Replace the following:

  * CLUSTER_NAME: The cluster name.
  * REGION: The [Compute Engine](https://docs.cloud.google.com/compute/docs/regions-zones#available) region.
  * CATALOG_NAME: Iceberg catalog name.
  * BUCKET and FOLDER: The Iceberg catalog location in Cloud Storage.



**Note:** To configure Spark to use Hive Metastore as the Iceberg catalog in Managed Service for Apache Spark 3.0+, use the following properties: * `spark.sql.catalog.<CATALOG_NAME>.type=rest` * `spark.sql.catalog.<CATALOG_NAME>.uri=env:ICEBERG_REST_CATALOG_URI` * (For Kerberos enabled clusters) `spark.sql.catalog.<CATALOG_NAME>.token=env:ICEBERG_REST_CATALOG_TOKEN`

### Write data to an Iceberg Table

You can write data to an Iceberg table using Spark. The following code snippets create a [`DataFrame`](https://spark.apache.org/docs/latest/sql-programming-guide.html#datasets-and-dataframes) with sample data, create an Iceberg table in Cloud Storage, and then write the data to the Iceberg table.

### PySpark
    
    
    # Create a DataFrame with sample data.
    data = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
    
    # Create an Iceberg table in Cloud Storage.
    spark.sql("""CREATE TABLE IF NOT EXISTS CATALOG_NAME.NAMESPACE.TABLE_NAME (
        id integer,
        name string)
    USING iceberg
    LOCATION 'gs://BUCKET/FOLDER/NAMESPACE/TABLE_NAME'""")
    
    # Write the DataFrame to the Iceberg table in Cloud Storage.
    data.writeTo("CATALOG_NAME.NAMESPACE.TABLE_NAME").append()
    

### Scala
    
    
    // Create a DataFrame with sample data.
    val data = Seq((1, "Alice"), (2, "Bob")).toDF("id", "name")
    
    // Create an Iceberg table in Cloud Storage.
    spark.sql("""CREATE TABLE IF NOT EXISTS CATALOG_NAME.NAMESPACE.TABLE_NAME (
        id integer,
        name string)
    USING iceberg
    LOCATION 'gs://BUCKET/FOLDER/NAMESPACE/TABLE_NAME'""")
    
    // Write the DataFrame to the Iceberg table in Cloud Storage.
    data.writeTo("CATALOG_NAME.NAMESPACE.TABLE_NAME").append()
    

### Read data from an Iceberg Table

You can read data from an Iceberg table using Spark. The following code snippets read the table, and then display its contents.

### PySpark
    
    
    # Read Iceberg table data into a DataFrame.
    df = spark.read.format("iceberg").load("CATALOG_NAME.NAMESPACE.TABLE_NAME")
    # Display the data.
    df.show()
    

### Scala
    
    
    // Read Iceberg table data into a DataFrame.
    val df = spark.read.format("iceberg").load("CATALOG_NAME.NAMESPACE.TABLE_NAME")
    
    // Display the data.
    df.show()
    

### Spark SQL
    
    
    SELECT * FROM CATALOG_NAME.NAMESPACE.TABLE_NAME
    

### Hive

### Create an Iceberg Table in Hive

**Warning:** Iceberg does not support Hive 4.2 directly. Support is available using the Iceberg REST catalog supported by Hive. The following instructions using `HiveIcebergStorageHandler` apply only to Managed Service for Apache Spark image versions 2.x.

Managed Service for Apache Spark clusters pre-configure Hive to work with Iceberg.

To run the code snippets in this section, complete the following steps;

  1. Use [SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the master node of your Managed Service for Apache Spark cluster.

  2. Bring up `beeline` in the SSH terminal window.
         
         beeline -u jdbc:hive2://
         




You can create an unpartitioned or partitioned Iceberg table in Hive.

### Unpartitioned table

Create an unpartitioned Iceberg table in Hive.
    
    
    CREATE TABLE my_table (
      id INT,
      name STRING,
      created_at TIMESTAMP
    ) STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler';
    

### Partitioned table

Create a partitioned Iceberg table in Hive by specifying the partition columns in the `PARTITIONED BY` clause.
    
    
    CREATE TABLE my_partitioned_table (
      id INT,
      name STRING
    ) PARTITIONED BY (date_sk INT)
    STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler';
    

## Insert data into an Iceberg Table in Hive

You can insert data into an Iceberg table using standard Hive `INSERT` statements.
    
    
    SET hive.execution.engine=mr;
    
    INSERT INTO my_table
    SELECT 1, 'Alice', current_timestamp();
    

**Limitations**

  * The MR (MapReduce) execution engine only is supported for DML (data manipulation language) operations.
  * MR execution is deprecated in Hive `3.1.3`.



## Read data from an Iceberg Table in Hive

To read data from an Iceberg table, use a `SELECT` statement.
    
    
    SELECT * FROM my_table;
    

## Drop an Iceberg table in Hive.

To drop an Iceberg table in Hive, use the `DROP TABLE` statement.
    
    
    DROP TABLE my_table;
    

## What's next

  * See the [Iceberg Quick Start guide](https://iceberg.apache.org/docs/latest/spark-getting-started/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
