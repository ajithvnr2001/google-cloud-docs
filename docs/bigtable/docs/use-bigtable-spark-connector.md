---
url: https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector/
title: Use the Bigtable Spark connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:54.153272+00:00
---

# Use the Bigtable Spark connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Bigtable Spark connector

The Bigtable Spark connector lets you read and write data to and from Bigtable. You can read data from your Spark application using Spark SQL and DataFrames. The following Bigtable operations are supported using the Bigtable Spark connector:

  * Write data
  * Read data
  * Create a new table



This document shows you how to convert a Spark SQL DataFrames table to a Bigtable table, and then compile and create a JAR file to submit a Spark job.

## Spark and Scala support status

The Bigtable Spark connector supports the following Scala versions:

  * [2.12](https://www.scala-lang.org/download/2.12.0.html)
  * [2.13](https://www.scala-lang.org/download/2.13.0.html)



The Bigtable Spark connector supports the following Spark versions:

  * [2.4.8](https://spark.apache.org/docs/2.4.8/#downloading)
  * [3.2.x](https://spark.apache.org/docs/3.2.3/#downloading)
  * [3.3.x](https://spark.apache.org/docs/3.3.1/#downloading)
  * [3.4.x](https://spark.apache.org/docs/3.4.1/#downloading)
  * [3.5.x](https://spark.apache.org/docs/3.5.1/)



The Bigtable Spark connector supports the following Managed Service for Apache Spark versions:

  * [1.5 image-version cluster](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-1.5)
  * [2.0 image-version cluster](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.0)
  * [2.1 image-version cluster](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.1)
  * [2.2 image-version cluster](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.2)
  * [2.3 image-version cluster](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3)
  * [Dataproc Serverless runtime version 1.0](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-versions#spark_runtime_version_10)



For more information, see [Managed Service for Apache Spark cluster image version lists](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-version-lists).

## Calculate costs

If you decide to use any of the following billable components of Google Cloud, you are billed for the resources that you use:

  * Bigtable (You are not charged for using the Bigtable emulator)
  * Managed Service for Apache Spark
  * Cloud Storage



[Managed Service for Apache Spark pricing](https://cloud.google.com/products/managed-service-for-apache-spark/pricing) applies to the use of Managed Service for Apache Spark on Compute Engine clusters. [Managed Service for Apache Spark Serverless pricing](https://cloud.google.com/products/managed-service-for-apache-spark/pricing) applies to workloads and sessions run on Managed Service for Apache Spark Serverless for Spark.

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Before you begin

Complete the following prerequisites before using the Bigtable Spark connector.

### Required roles

To get the permissions that you need to use Bigtable Spark connector, ask your administrator to grant you the following IAM roles on your project: 

  * Bigtable Administrator (`roles/bigtable.admin`)(Optional): lets you read or write data and create a new table. 
  * Bigtable User (`roles/bigtable.user`): lets you read or write data, but doesn't let you create a new table. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** The permissions associated with the `bigtable.admin` are the highest level of permissions. Use other Bigtable [predefined roles](https://docs.cloud.google.com/bigtable/docs/access-control) based on the level of access you want to grant.

If you are using Managed Service for Apache Spark or Cloud Storage, additional permissions might be required. For more information, see [Managed Service for Apache Spark permissions](https://docs.cloud.google.com/dataproc/docs/concepts/iam/iam) and [Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) permissions.

### Set up Spark

Apart from creating a Bigtable instance, you also need to set up your Spark instance. You can do so locally or select either of these options to use Spark with Managed Service for Apache Spark:

  * Managed Service for Apache Spark cluster
  * Managed Service for Apache Spark Serverless



For more information about choosing between a Managed Service for Apache Spark cluster or serverless option, see the [Managed Service for Apache Spark Serverless for Spark compared to Managed Service for Apache Spark on Compute Engine ](https://docs.cloud.google.com/dataproc-serverless/docs/overview#for_spark_compared_to_on) documentation.

### Download the connector JAR file

You can find the Bigtable Spark connector source code with examples in the [Bigtable Spark connector GitHub repository](https://github.com/GoogleCloudDataproc/spark-bigtable-connector).

Based on your Spark setup, you can access the JAR file as follows:

  * If you are running PySpark locally, you should download the connector's JAR file from the `gs://spark-lib/bigtable/spark-bigtable_SCALA_VERSION-CONNECTOR_VERSION.jar` Cloud Storage location.

Replace `SCALA_VERSION` with `2.12` or `2.13`, which are the only supported Scala versions, and replace the `CONNECTOR_VERSION` with the connector version that you want to use.

  * For Managed Service for Apache Spark cluster or serverless option, use the latest JAR file as an artifact that can be added in your Scala or Java Spark applications. For more information about using the JAR file as an artifact, see Manage dependencies.

  * If you are submitting your PySpark job to Managed Service for Apache Spark, use the [`gcloud dataproc jobs submit pyspark --jars` flag](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pyspark#--jars) to set the URI to the JAR file location in Cloud Storage—for example `gs://spark-lib/bigtable/spark-bigtable_SCALA_VERSION-CONNECTOR_VERSION.jar`.




## Determine compute type

For high-throughput read jobs, such as those executed by Spark applications, you can use Data Boost serverless compute to avoid impacting your application-serving clusters. Your Spark application must use version 1.1.0 or later of the Spark connector to use Data Boost.

To use Data Boost, you must create a Data Boost app profile and then provide the app profile ID for the `spark.bigtable.app_profile.id` Spark option when you add your Bigtable configuration to your Spark application. If you've already created an app profile for your Spark read jobs and you want to continue using it without changing your application code, you can convert the app profile to a Data Boost app profile. For more information, see [Convert an app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#convert-app-profile).

For more information, see the [Bigtable Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

For jobs that involve reads and writes, you can use your instance's cluster nodes for compute by specifying a standard app profile with your request.

## Identify or create an app profile to use

If you don't specify an app profile ID, the connector uses the default app profile.

We recommend that you use a unique app profile for each application that you run, including your Spark application. For more information about app profile types and settings, see the [App profiles overview](https://docs.cloud.google.com/bigtable/docs/app-profiles). For instructions, see [Create and configure app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles).

## Add Bigtable configuration to your Spark application

In your Spark application, add the Spark options that let you interact with Bigtable.

### Supported Spark options

Use the Spark options that are available as part of the `com.google.cloud.spark.bigtable` package.

Option name | Required | Default value | Meaning  
---|---|---|---  
`spark.bigtable.project.id` | Yes | N/A | Set the Bigtable project ID.  
`spark.bigtable.instance.id` | Yes | N/A | Set the Bigtable instance ID.  
`catalog` | Yes | N/A | Set the JSON format that specifies the conversion format between the DataFrame's SQL-like schema and the Bigtable table's schema.  
  
See Create table metadata in JSON format for more information.  
`spark.bigtable.app_profile.id` | No | `default` | Set the Bigtable app profile ID.  
`spark.bigtable.write.timestamp.milliseconds` | No | Current system time | Set the timestamp in milliseconds to use when writing a DataFrame to Bigtable.   
  
Note that since all rows in the DataFrame use the same timestamp, rows with the same row key column in the DataFrame persist as a single version in Bigtable as they share the same timestamp.  
`spark.bigtable.create.new.table` | No | `false` | Set to `true` to create a new table before writing to Bigtable.  
`spark.bigtable.read.timerange.start.milliseconds` or `spark.bigtable.read.timerange.end.milliseconds` | No | N/A | Set timestamps (in milliseconds since epoch time) to filter cells with a specific start and end date, respectively.  
`spark.bigtable.push.down.row.key.filters` | No | `true` | Set to `true` to allow simple row key filtering on the server-side. Filtering on compound row keys is implemented on the client-side.  
  
See Read a specific DataFrame row using a filter for more information.  
`spark.bigtable.read.rows.attempt.timeout.milliseconds` | No | 30m | Set the [timeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.stub.EnhancedBigtableStubSettings#com_google_cloud_bigtable_data_v2_stub_EnhancedBigtableStubSettings_readRowsSettings__) duration for a read rows attempt corresponding to one DataFrame partition in the Bigtable client for Java.  
`spark.bigtable.read.rows.total.timeout.milliseconds` | No | 12h | Set the [_total_ timeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.stub.EnhancedBigtableStubSettings#com_google_cloud_bigtable_data_v2_stub_EnhancedBigtableStubSettings_readRowsSettings__) duration for a read rows attempt corresponding to one DataFrame partition in the Bigtable client for Java.  
`spark.bigtable.mutate.rows.attempt.timeout.milliseconds` | No | 1m | Set the [timeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.stub.EnhancedBigtableStubSettings#com_google_cloud_bigtable_data_v2_stub_EnhancedBigtableStubSettings_bulkMutateRowsSettings__) duration for a mutate rows attempt corresponding to one DataFrame partition in the Bigtable client for Java.  
`spark.bigtable.mutate.rows.total.timeout.milliseconds` | No | 10m | Set the [_total_ timeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.stub.EnhancedBigtableStubSettings#com_google_cloud_bigtable_data_v2_stub_EnhancedBigtableStubSettings_bulkMutateRowsSettings__) duration for a mutate rows attempt corresponding to one DataFrame partition in the Bigtable client for Java.  
`spark.bigtable.batch.mutate.size` | No | `100` | Set to the number of mutations in each batch. The maximum value you can set is `100000`.  
`spark.bigtable.enable.batch_mutate.flow_control` | No | `false` | Set to `true` to enable [flow control](https://docs.cloud.google.com/bigtable/docs/writes#flow-control) for batch mutations.  
  
### Create table metadata in JSON format

The Spark SQL DataFrames table format must be converted into a Bigtable table using a string with JSON format. This string JSON format makes the data format compatible with Bigtable. You can pass the JSON format in your application code using the `.option("catalog", catalog_json_string)` option.

As an example, consider the following DataFrame table and the corresponding Bigtable table.

In this example, the `name` and `birthYear` columns in the DataFrame are grouped together under the `info` column family and renamed to `name` and `birth_year`, respectively. Similarly, the `address` column is stored under the `location` column family with the same column name. The `id` column from the DataFrame is converted to the Bigtable row key.

The row keys don't have a dedicated column name in Bigtable and in this example, `id_rowkey` is only used to indicate to the connector that this is the row key column. You can use any name for the row key column and make sure that you use the same name when you declare the `"rowkey":"column_name"` field in the JSON format.

DataFrame |  | Bigtable table = t1  
---|---|---  
Columns | Row key | Column families  
info | location   
Columns | Columns  
id | name | birthYear | address | id_rowkey | name | birth_year | address  
  
The JSON format for the catalog is as follows:
    
    
        """
        {
          "table": {"name": "t1"},
          "rowkey": "id_rowkey",
          "columns": {
            "id": {"cf": "rowkey", "col": "id_rowkey", "type": "string"},
            "name": {"cf": "info", "col": "name", "type": "string"},
            "birthYear": {"cf": "info", "col": "birth_year", "type": "long"},
            "address": {"cf": "location", "col": "address", "type": "string"}
          }
        }
        """
    

The keys and values used in the JSON format are the following:

Catalog key | Catalog value | JSON Format  
---|---|---  
table | Name of the Bigtable table. | `"table":{"name":"t1"}`  
  
If the table does not exist, use `.option("spark.bigtable.create.new.table", "true")` to create a table.  
rowkey | Name of the column that will be used as the Bigtable row key. Ensure that the column name of the DataFrame column is used as the row key—for example, `id_rowkey`.   
  
Compound keys are also accepted as row keys. For example, `"rowkey":"name:address"`. This approach might result in row keys that require a full table scan for all read requests. | `"rowkey":"id_rowkey"`,  
columns | Mapping of each DataFrame column into the corresponding Bigtable column family (`"cf"`) and column name (`"col"`). The column name can be different from the column name in the DataFrame table. Supported data types include `string`, `long`, and `binary`. | `"columns": {"id": {"cf": "rowkey", "col": "id_rowkey", "type": "string"}, "name": {"cf": "info", "col": "name", "type": "string"}, "birthYear": {"cf":"info", "col": "birth_year", "type": "long"}, "address": {"cf": "location", "col": "address", "type":"string"}}"`   
  
In this example, `id_rowkey` is the row key, and `info` and `location` are the column families.  
  
### Supported data types

The connector supports using `string`, `long`, and `binary` (byte array) types in the catalog. Until support for other types such as `int`and `float` is added, you can manually convert such data types to byte arrays (Spark SQL's `BinaryType`) before using the connector to write them to Bigtable.

In addition, you can use Avro for serialize complex types, such as `ArrayType`. For more information, see Serialize complex data types using Apache Avro.

### Write to Bigtable

Use the `.write()` function and the supported options to write your data to Bigtable.

### Java

The following code from the [GitHub repository](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/tree/main/examples) uses Java and Maven to write to Bigtable.
    
    
      String catalog = "{" +
            "\"table\":{\"name\":\"" + tableName + "\"," +
            "\"tableCoder\":\"PrimitiveType\"}," +
            "\"rowkey\":\"wordCol\"," +
            "\"columns\":{" +
            "\"word\":{\"cf\":\"rowkey\", \"col\":\"wordCol\", \"type\":\"string\"}," +
            "\"count\":{\"cf\":\"example_family\", \"col\":\"countCol\", \"type\":\"long\"}" +
            "}}".replaceAll("\\s+", "");
    
    …
    
      private static void writeDataframeToBigtable(Dataset<Row> dataframe, String catalog,
            String createNewTable) {
          dataframe
              .write()
              .format("bigtable")
              .option("catalog", catalog)
              .option("spark.bigtable.project.id", projectId)
              .option("spark.bigtable.instance.id", instanceId)
              .option("spark.bigtable.create.new.table", createNewTable)
              .save();
        }
    

### Python

The following code from the [GitHub repository](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/tree/main/examples) uses Python to write to Bigtable.
    
    
      catalog = ''.join(("""{
            "table":{"name":" """ + bigtable_table_name + """
            ", "tableCoder":"PrimitiveType"},
            "rowkey":"wordCol",
            "columns":{
              "word":{"cf":"rowkey", "col":"wordCol", "type":"string"},
              "count":{"cf":"example_family", "col":"countCol", "type":"long"}
            }
            }""").split())
      …
    
      input_data = spark.createDataFrame(data)
      print('Created the DataFrame:')
      input_data.show()
    
      input_data.write \
            .format('bigtable') \
            .options(catalog=catalog) \
            .option('spark.bigtable.project.id', bigtable_project_id) \
            .option('spark.bigtable.instance.id', bigtable_instance_id) \
            .option('spark.bigtable.create.new.table', create_new_table) \
            .save()
      print('DataFrame was written to Bigtable.')
    
      …
    

### Read from Bigtable

Use the `.read()` function to check whether the table was successfully imported into Bigtable.

### Java
    
    
      …
      private static Dataset<Row> readDataframeFromBigtable(String catalog) {
          Dataset<Row> dataframe = spark
              .read()
              .format("bigtable")
              .option("catalog", catalog)
              .option("spark.bigtable.project.id", projectId)
              .option("spark.bigtable.instance.id", instanceId)
              .load();
          return dataframe;
        }
    

### Python
    
    
      …
    
      records = spark.read \
            .format('bigtable') \
            .option('spark.bigtable.project.id', bigtable_project_id) \
            .option('spark.bigtable.instance.id', bigtable_instance_id) \
            .options(catalog=catalog) \
            .load()
    
      print('Reading the DataFrame from Bigtable:')
      records.show()
    

## Compile your project

Generate the JAR file that is used to run a job in either a Managed Service for Apache Spark cluster, Managed Service for Apache Spark Serverless, or local Spark instance. You can compile the JAR file locally and then use it to submit a job. The path to the compiled JAR is set as the `PATH_TO_COMPILED_JAR` environment variable when you submit a job.

This step doesn't apply to PySpark applications.

### Manage dependencies

The Bigtable Spark connector supports the following dependency management tools:

  * [Maven](https://maven.apache.org/install.html)
  * [sbt](https://www.scala-sbt.org/download.html)
  * [Gradle](https://gradle.org/install/)



### Compile the JAR file

### Maven

  1. Add the `spark-bigtable` dependency to your pom.xml file.
         
         <dependencies>
         <dependency>
           <groupId>com.google.cloud.spark.bigtable</groupId>
           <artifactId>spark-bigtable_SCALA_VERSION</artifactId>
           <version>0.1.0</version>
         </dependency>
         </dependencies>
         

  2. Add the [Maven Shade plugin](https://maven.apache.org/plugins/maven-shade-plugin/) to your `pom.xml` file to create an uber JAR:
         
         <plugins>
           <plugin>
             <groupId>org.apache.maven.plugins</groupId>
             <artifactId>maven-shade-plugin</artifactId>
             <version>3.2.4</version>
             <executions>
               <execution>
                 <phase>package</phase>
                 <goals>
                   <goal>shade</goal>
                 </goals>
               </execution>
             </executions>
           </plugin>
         </plugins>
         

  3. Run `mvn clean install` command to generate a JAR file.




### sbt

  1. Add the `spark-bigtable` dependency to your `build.sbt` file:
         
         libraryDependencies += "com.google.cloud.spark.bigtable" % "spark-bigtable_SCALA_VERSION" % "0.1.0{""}}"

  2. Add the `sbt-assembly` plugin to your `project/plugins.sbt` or `project/assembly.sbt` file to create an Uber JAR file.
         
         addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.1.1")

  3. Run the `sbt clean assembly` command to generate the JAR file.




### Gradle

  1. Add the `spark-bigtable` dependency to your `build.gradle` file.
         
         dependencies {
         implementation group: 'com.google.cloud.bigtable', name: 'spark-bigtable_SCALA_VERSION', version: '0.1.0'
         }

  2. Add the [Shadow](https://imperceptiblethoughts.com/shadow/) plugin in your `build.gradle` file to create an uber JAR file:
         
         plugins {
         id 'com.github.johnrengelman.shadow' version '8.1.1'
         id 'java'
         }

  3. See the [Shadow plugin's](https://imperceptiblethoughts.com/shadow/introduction/) documentation for more configuration and JAR compilation information.


**Note:** See [Gradle](https://docs.gradle.org/current/userguide/working_with_files.html#sec:creating_uber_jar_example) documentation, for detailed information about creating an uber JAR file with Gradle.

## Submit a job

Submit a Spark job using either Managed Service for Apache Spark, Managed Service for Apache Spark Serverless, or a local Spark instance to launch your application.

### Set runtime environment

Set the following environment variables.
    
    
          #Google Cloud
          export BIGTABLE_SPARK_PROJECT_ID=PROJECT_ID
          export BIGTABLE_SPARK_INSTANCE_ID=INSTANCE_ID
          export BIGTABLE_SPARK_TABLE_NAME=TABLE_NAME
          export BIGTABLE_SPARK_DATAPROC_CLUSTER=DATAPROC_CLUSTER
          export BIGTABLE_SPARK_DATAPROC_REGION=DATAPROC_REGION
          export BIGTABLE_SPARK_DATAPROC_ZONE=DATAPROC_ZONE
    
          #Managed Service for Apache Spark Serverless
          export BIGTABLE_SPARK_SUBNET=SUBNET
          export BIGTABLE_SPARK_GCS_BUCKET_NAME=GCS_BUCKET_NAME
    
          #Scala/Java
          export PATH_TO_COMPILED_JAR=PATH_TO_COMPILED_JAR
    
          #PySpark
          export GCS_PATH_TO_CONNECTOR_JAR=GCS_PATH_TO_CONNECTOR_JAR
          export PATH_TO_PYTHON_FILE=PATH_TO_PYTHON_FILE
          export LOCAL_PATH_TO_CONNECTOR_JAR=LOCAL_PATH_TO_CONNECTOR_JAR
    

Replace the following:

  * PROJECT_ID: The permanent identifier for the Bigtable project.
  * INSTANCE_ID: The permanent identifier for the Bigtable instance.
  * TABLE_NAME: The permanent identifier for the table.
  * DATAPROC_CLUSTER: The permanent identifier for the Managed Service for Apache Spark cluster.
  * DATAPROC_REGION: The Managed Service for Apache Spark region that contains one of the clusters in your Managed Service for Apache Spark instance—for example, `northamerica-northeast2`.
  * DATAPROC_ZONE: The zone where the Managed Service for Apache Spark cluster runs.
  * SUBNET: The full resource path of the [subnet](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network).
  * GCS_BUCKET_NAME: The Cloud Storage bucket to upload Spark workload dependencies.
  * PATH_TO_COMPILED_JAR: The full or relative path to the compiled JAR—for example, `/path/to/project/root/target/<compiled_JAR_name>` for Maven.
  * GCS_PATH_TO_CONNECTOR_JAR: The `gs://spark-lib/bigtable` Cloud Storage bucket, where the `spark-bigtable_SCALA_VERSION-CONNECTOR_VERSION.jar` file is located.
  * PATH_TO_PYTHON_FILE: For PySpark applications, the path to the Python file that will be used to write data to and read data from Bigtable.
  * LOCAL_PATH_TO_CONNECTOR_JAR: For PySpark applications, path to the downloaded Bigtable Spark connector JAR file.



### Submit a Spark job

For Managed Service for Apache Spark instances or your local Spark setup, run a Spark job to upload data to Bigtable.

**Note:** The following examples use environment variables that you configure for your environment, such as `$BIGTABLE_SPARK_PROJECT_ID` in Java or Scala, or `--bigtableProjectId=$BIGTABLE_SPARK_PROJECT_ID` in PySpark. For more information, see the Set runtime environment section of this document.

#### Managed Service for Apache Spark cluster

Use the compiled JAR file and create a Managed Service for Apache Spark cluster job that reads and writes data from and to Bigtable.

  1. Create a Managed Service for Apache Spark cluster. The following example shows a sample command to create a Managed Service for Apache Spark v2.0 cluster with Debian 10, two worker nodes, and default configurations.
         
         gcloud dataproc clusters create \
           $BIGTABLE_SPARK_DATAPROC_CLUSTER --region $BIGTABLE_SPARK_DATAPROC_REGION \
           --zone $BIGTABLE_SPARK_DATAPROC_ZONE \
           --master-machine-type n2-standard-4 --master-boot-disk-size 500 \
           --num-workers 2 --worker-machine-type n2-standard-4 --worker-boot-disk-size 500 \
           --image-version 2.0-debian10 --project $BIGTABLE_SPARK_PROJECT_ID
         

**Note:** Make sure that you include a logging framework compatible with the SLF4J logging API. For PySpark applications, use the   
`--packages` option to specify the logging package, such as `reload4j`, when you submit the Spark job. For Scala and Java applications, include the logging package in your dependency management tool. If you don't include this package, then the `java.lang.NoClassDefFoundError: org/slf4j/impl/StaticLoggerBinder` error occurs.
  2. Submit a job.

### Scala/Java

The following example shows the `spark.bigtable.example.WordCount` class that includes the logic to create a test table in DataFrame, write the table to Bigtable, and then count the number of words in the table.
         
         gcloud dataproc jobs submit spark \
             --cluster=$BIGTABLE_SPARK_DATAPROC_CLUSTER \
             --region=$BIGTABLE_SPARK_DATAPROC_REGION \
             --class=spark.bigtable.example.WordCount \
             --jar=$PATH_TO_COMPILED_JAR \
             -- \
             $BIGTABLE_SPARK_PROJECT_ID \
             $BIGTABLE_SPARK_INSTANCE_ID \
             $BIGTABLE_SPARK_TABLE_NAME \
         

### PySpark
         
         gcloud dataproc jobs submit pyspark \
             --cluster=$BIGTABLE_SPARK_DATAPROC_CLUSTER \
             --region=$BIGTABLE_SPARK_DATAPROC_REGION \
             --jars=$GCS_PATH_TO_CONNECTOR_JAR \
             --properties='spark.jars.packages=org.slf4j:slf4j-reload4j:1.7.36' \
             $PATH_TO_PYTHON_FILE \
             -- \
             --bigtableProjectId=$BIGTABLE_SPARK_PROJECT_ID \
             --bigtableInstanceId=$BIGTABLE_SPARK_INSTANCE_ID \
             --bigtableTableName=$BIGTABLE_SPARK_TABLE_NAME \
         




#### Managed Service for Apache Spark Serverless

Use the compiled JAR file and create a Managed Service for Apache Spark job that reads and writes data from and to Bigtable with a Managed Service for Apache Spark Serverless instance.

### Scala/Java
    
    
      gcloud dataproc batches submit spark \
      --region=$BIGTABLE_SPARK_DATAPROC_REGION \
      --subnet=$BIGTABLE_SPARK_SUBNET --version=1.1 \
      --deps-bucket=gs://$BIGTABLE_SPARK_GCS_BUCKET_NAME --jar=$PATH_TO_COMPILED_JAR \
      --  \
      $BIGTABLE_SPARK_PROJECT_ID \
      $BIGTABLE_SPARK_INSTANCE_ID \
      $BIGTABLE_SPARK_TABLE_NAME
    

### PySpark
    
    
      gcloud dataproc batches submit pyspark $PATH_TO_PYTHON_FILE \
      --region=$BIGTABLE_SPARK_DATAPROC_REGION \
      --subnet=$BIGTABLE_SPARK_SUBNET --version=1.1 \
      --deps-bucket=gs://$BIGTABLE_SPARK_GCS_BUCKET_NAME \
      --jars=$GCS_PATH_TO_CONNECTOR_JAR \
      --properties='spark.jars.packages=org.slf4j:slf4j-reload4j:1.7.36' \
      -- \
      --bigtableProjectId=$BIGTABLE_SPARK_PROJECT_ID \
      --bigtableInstanceId=$BIGTABLE_SPARK_INSTANCE_ID \
      --bigtableTableName=$BIGTABLE_SPARK_TABLE_NAME
    

**Note:** If you encounter a `Specify a network which contains subnetworks to enable 'internal_ip_only'` error while submitting a job to Managed Service for Apache Spark Serverless, try creating a new subnet. For more information about creating a new subnet, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

#### Local Spark

Use the downloaded JAR file and create a Spark job that reads and writes data from and to Bigtable with a local Spark instance. You can also use the Bigtable emulator to submit the Spark job.

##### Use the Bigtable emulator

If you decide to use the Bigtable emulator, then follow these steps:

  1. Run the following command to start the emulator:
         
         gcloud beta emulators bigtable start
         

By default, the emulator chooses `localhost:8086`.

  2. Set the `BIGTABLE_EMULATOR_HOST` environment variable:
         
         export BIGTABLE_EMULATOR_HOST=localhost:8086
         

  3. Submit the Spark job.




For more information about using the Bigtable emulator, see [Test using the emulator](https://docs.cloud.google.com/bigtable/docs/emulator).

##### Submit a Spark job

Use the `spark-submit` command to submit a Spark job regardless of whether you are using a local Bigtable emulator.

### Scala/Java
    
    
      spark-submit $PATH_TO_COMPILED_JAR \
      $BIGTABLE_SPARK_PROJECT_ID \
      $BIGTABLE_SPARK_INSTANCE_ID \
      $BIGTABLE_SPARK_TABLE_NAME
    

### PySpark
    
    
      spark-submit \
      --jars=$LOCAL_PATH_TO_CONNECTOR_JAR \
      --packages=org.slf4j:slf4j-reload4j:1.7.36 \
      $PATH_TO_PYTHON_FILE \
      --bigtableProjectId=$BIGTABLE_SPARK_PROJECT_ID \
      --bigtableInstanceId=$BIGTABLE_SPARK_INSTANCE_ID \
      --bigtableTableName=$BIGTABLE_SPARK_TABLE_NAME
    
    

### Verify the table data

Run the following `cbt` CLI command to verify the data is written to Bigtable. The `cbt` CLI is a component of the Google Cloud CLI. For more information, see the [ `cbt` CLI overview](https://docs.cloud.google.com/bigtable/docs/cbt-overview).
    
    
        cbt -project=$BIGTABLE_SPARK_PROJECT_ID -instance=$BIGTABLE_SPARK_INSTANCE_ID \
        read $BIGTABLE_SPARK_TABLE_NAME
    

## Additional solutions

Use the Bigtable Spark connector for specific solutions, such as serializing complex Spark SQL types, reading specific rows, and generating client-side metrics.

### Read a specific DataFrame row using a filter

When using DataFrames to read from Bigtable, you can specify a [filter](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.filter.html) to only read specific rows. Simple filters such as `==`, `<=`, and `startsWith` on the row key column are applied on the server side to avoid a full-table scan. Filters on compound row keys or complex filters such as the `LIKE` filter on the row key column are applied at the client side.

If you are reading large tables, we recommend using simple row key filters to avoid performing a full-table scan. The following sample statement shows how to read using a simple filter. Make sure that in your Spark filter, you use the name of the DataFrame column that is converted to the row key:
    
    
        dataframe.filter("id == 'some_id'").show()
      

When applying a filter, use the DataFrame column name instead of the Bigtable table column name.

### Serialize complex data types using Apache Avro

The Bigtable Spark connector provides support for using Apache Avro to serialize complex [Spark SQL types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html), such as `ArrayType`, `MapType`, or `StructType`. Apache Avro provides data serialization for record data that is commonly used for processing and storing complex data structures.

Use a syntax such as `"avro":"avroSchema"` to specify that a column in Bigtable should be encoded using Avro. You can then use `.option("avroSchema", avroSchemaString)` when reading from or writing to Bigtable to specify the Avro schema corresponding to that column in string format. You can use different option names—for example, `"anotherAvroSchema"` for different columns and pass Avro schemas for multiple columns.
    
    
    def catalogWithAvroColumn = s"""{
                        |"table":{"name":"ExampleAvroTable"},
                        |"rowkey":"key",
                        |"columns":{
                        |"col0":{"cf":"rowkey", "col":"key", "type":"string"},
                        |"col1":{"cf":"cf1", "col":"col1", "avro":"avroSchema"}
                        |}
                        |}""".stripMargin
    

### Use client-side metrics

Since the Bigtable Spark connector is based on the [Bigtable Client for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), client-side metrics are enabled inside the connector by default. You can refer to the [client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics) documentation to find more details on accessing and interpreting these metrics.

### Use the Bigtable client for Java with low-level RDD functions

Since the Bigtable Spark connector is based on the [Bigtable client for Java](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable), you can directly use the client in your Spark applications and perform distributed read or write requests within the low-level RDD functions such as `mapPartitions` and `foreachPartition`.

To use the Bigtable client for Java classes, append the `com.google.cloud.spark.bigtable.repackaged` prefix to the package names. For example, instead of using the class name as `com.google.cloud.bigtable.data.v2.BigtableDataClient`, use `com.google.cloud.spark.bigtable.repackaged.com.google.cloud.bigtable.data.v2.BigtableDataClient`.

For more information about the Bigtable client for Java, see the [Bigtable client for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview).

## What's next

  * [Learn how to tune your Spark job in Managed Service for Apache Spark.](https://docs.cloud.google.com/dataproc/docs/support/spark-job-tuning)
  * Use [classes from the Bigtable client for Java](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable) with the Bigtable Spark connector.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
