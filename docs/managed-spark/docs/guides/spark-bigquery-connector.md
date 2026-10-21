---
url: https://docs.cloud.google.com/managed-spark/docs/guides/spark-bigquery-connector/
title: Use the Spark BigQuery connector \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:27.704041+00:00
---

# Use the Spark BigQuery connector  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/spark-bigquery-connector/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use the Spark BigQuery connector Stay organized with collections  Save and categorize content based on your preferences. 

You can use the [spark-bigquery-connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector) with Managed Service for Apache Spark to read and write data from and to [BigQuery](https://docs.cloud.google.com/bigquery "BigQuery"). This tutorial demonstrates a PySpark application that uses the `spark-bigquery-connector`.

The spark-bigquery-connector takes advantage of the [BigQuery Storage API](https://docs.cloud.google.com/bigquery/docs/reference/storage) when reading data from BigQuery. 

## Confirm the connector version

See [Managed Service for Apache Spark runtime releases](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions) to determine the BigQuery connector version that is installed in your batch workload or interactive session runtime version. If the connector is not listed, see Make the connector available to applications.

**Note:** You can update the installed BigQuery connector version using the `dataproc.sparkBqConnector.version` property (see [Other Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#other_properties)).

### Make the connector available to applications (if needed)

The BigQuery connector is installed in all [supported Managed Service for Apache Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions). If you are using an [unsupported runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#unsupported-dataproc-serverless-for-spark-runtime-versions) that does not install the connector (`Spark runtime 1.0`), you can make the connector available to an application in **either** of the following two ways:

  * Use the `jars` parameter to point to a connector jar file when you submit a Managed Service for Apache Spark batch workload or run an interactive session. The following batch workload example specifies a connector jar file (see the [GoogleCloudDataproc/spark-bigquery-connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) repository on GitHub for a list of available connector jar files). 
    * Google Cloud CLI example: 
          
          gcloud dataproc batches submit pyspark \
              --region=REGION \
              --jars=spark-3.5-bigquery-version.jar \
              ... other args
          


**Note:** If the connector is not available to your application at runtime, a `ClassNotFoundException` is thrown.

## Calculate costs

This tutorial uses billable components of Google Cloud, including:

  * Managed Service for Apache Spark
  * BigQuery
  * Cloud Storage



Use the [Pricing Calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

New Cloud Platform users may be eligible for a [free trial](https://cloud.google.com/free). 

## Configure billing

By default, the project associated with the credentials or service account is billed for API usage. To bill a different project, set the following configuration property: `spark.conf.set("parentProject", "<BILLED-GCP-PROJECT>")`.

You can also add this property to a read or write operation, as follows: `.option("parentProject", "<BILLED-GCP-PROJECT>")`.

## Submit a PySpark wordcount batch workload

This example reads data from [BigQuery](https://console.cloud.google.com/bigquery) into a Spark DataFrame to perform a word count using the [standard data source API](https://spark.apache.org/docs/latest/sql-data-sources.html "Data Sources").

The connector writes the wordcount output to BigQuery in the following sequence of operations:

  1. Buffers the data into temporary files in your Cloud Storage bucket

  2. Copies the data in one operation from your Cloud Storage bucket into BigQuery

  3. Deletes the temporary files in Cloud Storage after the BigQuery load operation completes (temporary files are also deleted after the Spark application terminates). If deletion fails, you will need to delete any unwanted temporary Cloud Storage files, which typically are placed in `gs://BUCKET_NAME/.spark-bigquery-JOB_ID-UUID`.




### Steps to run the wordcount workload

  1. Open a local terminal or [Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 
  2. Create the `wordcount_dataset` with the [bq](https://docs.cloud.google.com/bigquery/bq-command-line-tool) command-line tool in a local terminal or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 
         
         bq mk wordcount_dataset
         

  3. Create a Cloud Storage bucket with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage). 
         
         gcloud storage buckets create gs://BUCKET_NAME
         

Replace `BUCKET_NAME` with the name of the Cloud Storage bucket you created. 
  4. Create the file `wordcount.py` locally in a text editor by copying the following PySpark code. 
         
         #!/usr/bin/python
         """BigQuery I/O PySpark example."""
         from pyspark.sql import SparkSession
         
         spark = SparkSession \
           .builder \
           .appName('spark-bigquery-demo') \
           .getOrCreate()
         
         # Cloud Storage bucket used by the connector for temporary BigQuery
         # export data.
         bucket = "BUCKET_NAME"
         spark.conf.set('temporaryGcsBucket', bucket)
         # Enable reading from BigQuery views and materializing query results.
         spark.conf.set('viewsEnabled', 'true')
         spark.conf.set('materializationDataset', 'wordcount_dataset')
         
         # Load data from BigQuery.
         words = spark.read.format('bigquery') \
           .load('bigquery-public-data.samples.shakespeare')
         words.createOrReplaceTempView('words')
         
         # Perform word count.
         word_count = spark.sql(
             'SELECT word, SUM(word_count) AS word_count FROM words GROUP BY word')
         word_count.show()
         word_count.printSchema()
         
         # Save the data to BigQuery
         word_count.write.format('bigquery') \
           .save('wordcount_dataset.wordcount_output')

  5. Submit the PySpark batch workload: 
         
         gcloud dataproc batches submit pyspark wordcount.py \
             --region=REGION \
             --deps-bucket=BUCKET_NAME
         

**Sample terminal output:**
         
         ...
         +---------+----------+
         |     word|word_count|
         +---------+----------+
         |     XVII|         2|
         |    spoil|        28|
         |    Drink|         7|
         |forgetful|         5|
         |   Cannot|        46|
         |    cures|        10|
         |   harder|        13|
         |  tresses|         3|
         |      few|        62|
         |  steel'd|         5|
         | tripping|         7|
         |   travel|        35|
         |   ransom|        55|
         |     hope|       366|
         |       By|       816|
         |     some|      1169|
         |    those|       508|
         |    still|       567|
         |      art|       893|
         |    feign|        10|
         +---------+----------+
         only showing top 20 rows
         
         root
          |-- word: string (nullable = false)
          |-- word_count: long (nullable = true)
         

  
To preview the output table in the Google Cloud console, open the [BigQuery](https://console.cloud.google.com/bigquery) page, select the `wordcount_output` table, and then click **Preview**. ![BigQuery table preview rendering](https://docs.cloud.google.com/static/dataproc/images/table-preview.png)**Figure 1:** Preview the output table in BigQuery



## For more information

  * [BigQuery Storage & Spark SQL - Python](https://github.com/tfayyaz/cloud-dataproc/blob/master/notebooks/python/1.2.%20BigQuery%20Storage%20%26%20Spark%20SQL%20-%20Python.ipynb)
  * [Creating a table definition file for an external data source](https://docs.cloud.google.com/bigquery/external-table-definition)
  * [Use externally partitioned data](https://docs.cloud.google.com/bigquery/docs/hive-partitioned-queries-gcs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
