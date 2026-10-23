---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/delta/
title: Install the Delta Lake component on a cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:52.560319+00:00
---

# Install the Delta Lake component on a cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/delta/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Install the Delta Lake component on a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to install and configure the [Delta Lake](https://delta.io/) optional component on a Managed Service for Apache Spark cluster. When enabled, the Delta Lake component installs the necessary libraries and sets up Spark and Hive to work with Delta Lake.

**Note:** Delta Lake `4.x`, which is included in Managed Service for Apache Spark image version `3.0`, doesn't support Hive.

To learn more about other available optional components in Managed Service for Apache Spark, see [Available optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components).

## Compatible Managed Service for Apache Spark image versions

You can install the Delta Lake component on Managed Service for Apache Spark clusters created with Managed Service for Apache Spark image version [2.2.46](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.2) and later image versions.

See [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the Delta Lake component version included in Managed Service for Apache Spark image releases.

## Delta Lake related properties

When you create a Managed Service for Apache Spark cluster with the Delta Lake component enabled, the following Spark properties are configured to work with Delta Lake.

Config file | Property | Default value  
---|---|---  
`/etc/spark/conf/spark-defaults.conf` |  `spark.sql.extensions` | `io.delta.sql.DeltaSparkSessionExtension`  
`/etc/spark/conf/spark-defaults.conf` | `spark.sql.catalog.spark_catalog` |  `org.apache.spark.sql.delta.catalog.DeltaCatalog`  
  
## Install the component

Install the component when you create a Managed Service for Apache Spark cluster using the Google Cloud console, Google Cloud CLI, or the Dataproc API.

### Google Cloud console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Delta**.
  5. Click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Delta Lake component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--optional-components` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --optional-components=DELTA \
        --region=REGION \
        ... other flags
    

Notes:

  * CLUSTER_NAME: Specify the name of the cluster.
  * REGION: Specify a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be located.



### REST API

The Delta Lake component can be specified through the Dataproc API using the [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

## Usage examples

This section provides data read and write examples using Delta Lake tables.

### Delta Lake table

### Write to a Delta Lake table

You can use the [Spark DataFrame ](https://spark.apache.org/docs/latest/sql-programming-guide.html) to write data to a Delta Lake table. The following examples create a `DataFrame` with sample data, create a `my_delta_table` Delta Lake table In Cloud Storage, and then write the data to the Delta Lake table.

#### PySpark
    
    
    # Create a DataFrame with sample data.
    data = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
    
    # Create a Delta Lake table in Cloud Storage.
    spark.sql("""CREATE TABLE IF NOT EXISTS my_delta_table (
        id long,
        name string)
    USING delta
    LOCATION 'gs://delta-gcs-demo/example-prefix/default/my_delta_table'""")
    
    # Write the DataFrame to the Delta Lake table in Cloud Storage.
    data.writeTo("my_delta_table").append()
    

#### Scala
    
    
    // Create a DataFrame with sample data.
    val data = Seq((1, "Alice"), (2, "Bob")).toDF("id", "name")
    
    // Create a Delta Lake table in Cloud Storage.
    spark.sql("""CREATE TABLE IF NOT EXISTS my_delta_table (
        id integer,
        name string)
    USING delta
    LOCATION 'gs://delta-gcs-demo/example-prefix/default/my_delta_table'""")
    
    // Write the DataFrame to the Delta Lake table in Cloud Storage.
    data.write.format("delta").mode("append").saveAsTable("my_delta_table")
    

#### Spark SQL
    
    
    CREATE TABLE IF NOT EXISTS my_delta_table (
        id integer,
        name string)
    USING delta
    LOCATION 'gs://delta-gcs-demo/example-prefix/default/my_delta_table';
    
    INSERT INTO my_delta_table VALUES ("1", "Alice"), ("2", "Bob");
    

### Read from a Delta Lake table

The following examples read the `my_delta_table` and display its contents.

#### PySpark
    
    
    # Read the Delta Lake table into a DataFrame.
    df = spark.table("my_delta_table")
    
    # Display the data.
    df.show()
    

#### Scala
    
    
    // Read the Delta Lake table into a DataFrame.
    val df = spark.table("my_delta_table")
    
    // Display the data.
    df.show()
    

#### Spark SQL
    
    
    SELECT * FROM my_delta_table;
    

### Hive with Delta Lake

### Write to a Delta Table in Hive.

**Warning:** Delta Lake has stopped built-in support for Hive in version 4.x. Managed Service for Apache Spark 3.0 includes Delta 4.2. Therefore, Hive integration with Delta Lake is not supported on Managed Service for Apache Spark 3.0. The following instructions apply only to Managed Service for Apache Spark image versions 2.x.

The Managed Service for Apache Spark Delta Lake optional component is pre-configured to work with Hive external tables.

For more information, see [Hive connector](https://docs.delta.io/delta-more-connectors/#apache-hive).

#### Run the examples in a beeline client.
    
    
    beeline -u jdbc:hive2://

#### Create a Spark Delta Lake table.

The Delta Lake table must be created using Spark before a Hive external table can reference it.
    
    
    CREATE TABLE IF NOT EXISTS my_delta_table (
        id integer,
        name string)
    USING delta
    LOCATION 'gs://delta-gcs-demo/example-prefix/default/my_delta_table';
    
    INSERT INTO my_delta_table VALUES ("1", "Alice"), ("2", "Bob");
    

#### Create a Hive external table.
    
    
    SET hive.input.format=io.delta.hive.HiveInputFormat;
    SET hive.tez.input.format=io.delta.hive.HiveInputFormat;
    
    CREATE EXTERNAL TABLE deltaTable(id INT, name STRING)
    STORED BY 'io.delta.hive.DeltaStorageHandler'
    LOCATION 'gs://delta-gcs-demo/example-prefix/default/my_delta_table';
    

Notes:

  * The `io.delta.hive.DeltaStorageHandler` class implements the Hive data source APIs. It can load a Delta table and extract its metadata. If the table schema in the `CREATE TABLE` statement is not consistent with the underlying Delta Lake metadata, an error is thrown.



### Read from a Delta Lake table in Hive.

To read data from a Delta table, use a `SELECT` statement:
    
    
    SELECT * FROM deltaTable;
    

#### Drop a Delta Lake table.

To drop a Delta table, use the `DROP TABLE` statement:
    
    
    DROP TABLE deltaTable;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
