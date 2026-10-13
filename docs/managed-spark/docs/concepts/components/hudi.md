---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/hudi/
title: Managed Service for Apache Spark optional Hudi component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:46.151011+00:00
---

# Managed Service for Apache Spark optional Hudi component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/hudi/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Hudi component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Hudi when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes how you can optionally install the Hudi component on a Managed Service for Apache Spark cluster.

When installed on a Managed Service for Apache Spark cluster, the [Apache Hudi](https://hudi.apache.org/docs/overview) component installs Hudi libraries and configures Spark and Hive in the cluster to work with Hudi.

## Compatible Managed Service for Apache Spark image versions

You can install the Hudi component on Managed Service for Apache Spark clusters created with the following Managed Service for Apache Spark image versions:

  * [2.0.54+](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.0)
  * [2.1.2+](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1)
  * [2.2.31+](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.2)

**Note:** Hudi is not available in Managed Service for Apache Spark image version `3.0`.

## Hudi related properties

When you create a Managed Service for Apache Spark with Hudi cluster, the following Spark and Hive properties are configured to work with Hudi.

Config file | Property | Default value  
---|---|---  
`/etc/spark/conf/spark-defaults.conf` | `spark.serializer` | `org.apache.spark.serializer.KryoSerializer` | `spark.sql.catalog.spark_catalog` | `org.apache.spark.sql.hudi.catalog.HoodieCatalog`  
`spark.sql.extensions` | `org.apache.spark.sql.hudi.HoodieSparkSessionExtension`  
`spark.driver.extraClassPath` | `/usr/lib/hudi/lib/hudi-sparkspark-version-bundle_scala-version-hudi-version.jar`  
`spark.executor.extraClassPath` | `/usr/lib/hudi/lib/hudi-sparkspark-version-bundle_scala-version-hudi-version.jar`  
`/etc/hive/conf/hive-site.xml` | `hive.aux.jars.path` | `file:///usr/lib/hudi/lib/hudi-hadoop-mr-bundle-version.jar`  
  
## Install the component

Install the Hudi component when you create a Managed Service for Apache Spark cluster.

The [Managed Service for Apache Spark image release version pages](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions) list the Hudi component version included in each Managed Service for Apache Spark image release.

### Google Cloud console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Hudi**.
  5. Click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Hudi component, use the command with the `--optional-components` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --optional-components=HUDI \
        --image-version=DATAPROC_VERSION \
        --properties=PROPERTIES
    

Replace the following:

  * CLUSTER_NAME: Required. The new cluster name.
  * REGION: Required. The [cluster region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * DATAPROC_IMAGE: Optional. You can use this optional this flag to specify a non-default Managed Service for Apache Spark image version (see [Default Managed Service for Apache Spark image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#default_dataproc_image_version)).
  * PROPERTIES: Optional. You can use this optional this flag to set [Hudi component properties](https://hudi.apache.org/docs/basic_configurations), which are specified with the [`hudi:` file-prefix](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#file-prefixed_properties_table) Example: `properties=hudi:hoodie.datasource.write.table.type=COPY_ON_WRITE`). 
    * Hudi component version property: You can optionally specify the [`dataproc:hudi.version` property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc_service_properties_table). **Note:** The Hudi component version is set by Managed Service for Apache Spark to be compatible with the Managed Service for Apache Spark cluster image version. If you set this property, cluster creation can fail if the specified version is not compatible with the cluster image.
    * Spark and Hive properties: Managed Service for Apache Spark sets Hudi-related Spark and Hive properties when the cluster is created. You don't need to set them when creating the cluster or submitting jobs.



### REST API

The Hudi component can be installed through the Dataproc API using [`SoftwareConfig.Component`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

## Submit a job to read and write Hudi tables

After creating a cluster with the Hudi component, you can submit Spark and Hive jobs that read and write Hudi tables.

`gcloud CLI` example:
    
    
    gcloud dataproc jobs submit pyspark \
        --cluster=CLUSTER_NAME \
        --region=region \
        JOB_FILE \
        -- JOB_ARGS
    

### Sample PySpark job

The following PySpark file creates, reads, and writes a Hudi table.
    
    
    #!/usr/bin/env python
    """Pyspark Hudi test."""
    
    import sys
    from pyspark.sql import SparkSession
    
    
    def create_hudi_table(spark, table_name, table_uri):
      """Creates Hudi table."""
      create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
          uuid string,
          begin_lat double,
          begin_lon double,
          end_lat double,
          end_lon double,
          driver string,
          rider string,
          fare double,
          partitionpath string,
          ts long
        ) USING hudi
        LOCATION '{table_uri}'
        TBLPROPERTIES (
          type = 'cow',
          primaryKey = 'uuid',
          preCombineField = 'ts'
        )
        PARTITIONED BY (partitionpath)
      """
      spark.sql(create_table_sql)
    
    
    def generate_test_dataframe(spark, n_rows):
      """Generates test dataframe with Hudi's built-in data generator."""
      sc = spark.sparkContext
      utils = sc._jvm.org.apache.hudi.QuickstartUtils
      data_generator = utils.DataGenerator()
      inserts = utils.convertToStringList(data_generator.generateInserts(n_rows))
      return spark.read.json(sc.parallelize(inserts, 2))
    
    
    def write_hudi_table(table_name, table_uri, df):
      """Writes Hudi table."""
      hudi_options = {
          'hoodie.table.name': table_name,
          'hoodie.datasource.write.recordkey.field': 'uuid',
          'hoodie.datasource.write.partitionpath.field': 'partitionpath',
          'hoodie.datasource.write.table.name': table_name,
          'hoodie.datasource.write.operation': 'upsert',
          'hoodie.datasource.write.precombine.field': 'ts',
          'hoodie.upsert.shuffle.parallelism': 2,
          'hoodie.insert.shuffle.parallelism': 2,
      }
      df.write.format('hudi').options(**hudi_options).mode('append').save(table_uri)
    
    
    def query_commit_history(spark, table_name, table_uri):
      tmp_table = f'{table_name}_commit_history'
      spark.read.format('hudi').load(table_uri).createOrReplaceTempView(tmp_table)
      query = f"""
        SELECT DISTINCT(_hoodie_commit_time)
        FROM {tmp_table}
        ORDER BY _hoodie_commit_time
        DESC
      """
      return spark.sql(query)
    
    
    def read_hudi_table(spark, table_name, table_uri, commit_ts=''):
      """Reads Hudi table at the given commit timestamp."""
      if commit_ts:
        options = {'as.of.instant': commit_ts}
      else:
        options = {}
      tmp_table = f'{table_name}_snapshot'
      spark.read.format('hudi').options(**options).load(
          table_uri
      ).createOrReplaceTempView(tmp_table)
      query = f"""
        SELECT _hoodie_commit_time, begin_lat, begin_lon,
            driver, end_lat, end_lon, fare, partitionpath,
            rider, ts, uuid
        FROM {tmp_table}
      """
      return spark.sql(query)
    
    
    def main():
      """Test create write and read Hudi table."""
      if len(sys.argv) != 3:
        raise Exception('Expected arguments: <table_name> <table_uri>')
    
      table_name = sys.argv[1]
      table_uri = sys.argv[2]
    
      app_name = f'pyspark-hudi-test_{table_name}'
      print(f'Creating Spark session {app_name} ...')
      spark = SparkSession.builder.appName(app_name).getOrCreate()
      spark.sparkContext.setLogLevel('WARN')
    
      print(f'Creating Hudi table {table_name} at {table_uri} ...')
      create_hudi_table(spark, table_name, table_uri)
    
      print('Generating test data batch 1...')
      n_rows1 = 10
      input_df1 = generate_test_dataframe(spark, n_rows1)
      input_df1.show(truncate=False)
    
      print('Writing Hudi table, batch 1 ...')
      write_hudi_table(table_name, table_uri, input_df1)
    
      print('Generating test data batch 2...')
      n_rows2 = 10
      input_df2 = generate_test_dataframe(spark, n_rows2)
      input_df2.show(truncate=False)
    
      print('Writing Hudi table, batch 2 ...')
      write_hudi_table(table_name, table_uri, input_df2)
    
      print('Querying commit history ...')
      commits_df = query_commit_history(spark, table_name, table_uri)
      commits_df.show(truncate=False)
      previous_commit_ts = commits_df.collect()[1]._hoodie_commit_time
    
      print('Reading the Hudi table snapshot at the latest commit ...')
      output_df1 = read_hudi_table(spark, table_name, table_uri)
      output_df1.show(truncate=False)
    
      print(f'Reading the Hudi table snapshot at {previous_commit_ts} ...')
      output_df2 = read_hudi_table(spark, table_name, table_uri, previous_commit_ts)
      output_df2.show(truncate=False)
    
      print('Stopping Spark session ...')
      spark.stop()
    
      print('All done')
    
    
    main()
    

The following gcloud CLI command submits the sample PySpark file to Managed Service for Apache Spark.
    
    
    gcloud dataproc jobs submit pyspark \
        --cluster=CLUSTER_NAME \
        gs://BUCKET_NAME/pyspark_hudi_example.py \
        -- TABLE_NAME gs://BUCKET_NAME/TABLE_NAME
    

## Use the Hudi CLI

The Hudi CLI is located at `/usr/lib/hudi/cli/hudi-cli.sh` on the Managed Service for Apache Spark cluster master node. You can use the Hudi CLI to view Hudi table schemas, commits, and statistics, and to manually perform administrative operations, such as schedule compactions (see [Using hudi-cli](https://hudi.apache.org/docs/cli/#using-hudi-cli)).

To start the Hudi CLI and connect to a Hudi table:

  1. [SSH into the master node](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh).
  2. Run `/usr/lib/hudi/cli/hudi-cli.sh`. The command prompt changes to `hudi->`.
  3. Run `connect --path gs://my-bucket/my-hudi-table`.
  4. Run commands, such as `desc`, which describes the table schema, or `commits show`, which shows the commit history.
  5. To stop the CLI session, run `exit`.



## What's next

  * See the [Hudi Quick Start guide](https://hudi.apache.org/docs/quick-start-guide/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
