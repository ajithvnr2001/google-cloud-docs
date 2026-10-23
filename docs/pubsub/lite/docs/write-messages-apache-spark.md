---
url: https://docs.cloud.google.com/pubsub/lite/docs/write-messages-apache-spark/
title: Quickstart: Write Pub/Sub Lite messages by using Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:14.292329+00:00
---

# Quickstart: Write Pub/Sub Lite messages by using Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/write-messages-apache-spark/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write Pub/Sub Lite messages by using Apache Spark

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

The [Pub/Sub Lite Spark Connector](https://github.com/googleapis/java-pubsublite-spark) is an open-source Java client library that supports the use of Pub/Sub Lite as an input and output source for [Apache Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) . The connector works in all Apache Spark distributions, including Managed Service for Apache Spark.

This quickstart shows you how to:

  * read messages from Pub/Sub Lite
  * write messages to Pub/Sub Lite



using [PySpark](https://spark.apache.org/docs/3.1.2/api/python/index.html) from a Managed Service for Apache Spark Spark cluster.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Pub/Sub Lite, Managed Service for Apache Spark, Cloud Storage, Logging APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsublite.googleapis.com,dataproc,storage_api,logging)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Pub/Sub Lite, Managed Service for Apache Spark, Cloud Storage, Logging APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsublite.googleapis.com,dataproc,storage_api,logging)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Set up

  1. Create variables for your project.
         
         export PROJECT_ID=$(gcloud config get-value project)
         export PROJECT_NUMBER=$(gcloud projects list \
             --filter="projectId:$PROJECT_ID" \
             --format="value(PROJECT_NUMBER)")

  2. Create a Cloud Storage bucket. Cloud Storage bucket names must be globally unique.
         
         export BUCKET=your-bucket-name
         gcloud storage buckets create gs://$BUCKET
         

  3. Create a Pub/Sub Lite topic and subscription in a supported [location](https://docs.cloud.google.com/pubsub/lite/docs/locations). See [Create a topic](https://docs.cloud.google.com/pubsub/lite/docs/topics#create_a_lite_topic) if you use a Pub/Sub Lite [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations).
         
         export TOPIC=your-lite-topic-id
         export SUBSCRIPTION=your-lite-subscription-id
         export PUBSUBLITE_LOCATION=your-lite-location
         gcloud pubsub lite-topics create $TOPIC \
             --location=$PUBSUBLITE_LOCATION \
             --partitions=2 \
             --per-partition-bytes=30GiB
         gcloud pubsub lite-subscriptions create $SUBSCRIPTION \
             --location=$PUBSUBLITE_LOCATION \
             --topic=$TOPIC

  4. Create a Managed Service for Apache Spark cluster.
         
         export DATAPROC_REGION=your-dataproc-region
         export CLUSTER_ID=your-dataproc-cluster-id
         gcloud dataproc clusters create $CLUSTER_ID \
            --region $DATAPROC_REGION \
            --image-version 2.1 \
            --scopes 'https://www.googleapis.com/auth/cloud-platform' \
            --enable-component-gateway \
            --bucket $BUCKET

     * `--region`: a supported Managed Service for Apache Spark [region](https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints) where your Pub/Sub Lite topic and subscription reside.
     * `--image-version`: the [cluster's image version](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) , which determines the Apache Spark version installed on the cluster. Choose [2.x.x image release versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.0) because the Pub/Sub Lite Spark Connector currently supports Apache Spark 3.x.x.
     * `--scopes`: enable API access to Google Cloud services in the same project.
     * `--enable-component-gateway`: enable access to the Apache Spark web UI.
     * `--bucket`: a staging Cloud Storage bucket used to store cluster job dependencies, driver output, and cluster config files.
  5. Clone the quickstart repository and navigate to the sample code directory:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         cd python-docs-samples/pubsublite/spark-connector/
         




## Writing to Pub/Sub Lite

The following example will:

  * create a [rate source](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#creating-streaming-dataframes-and-streaming-datasets) that generates consecutive numbers and timestamps formatted as [`spark.sql.Row`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Row.html)
  * transform the data to match the required [table schema](https://github.com/googleapis/java-pubsublite-spark#data-schema) by the Pub/Sub Lite Spark Connector's [`writeStream`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.writeStream.html) API
  * write the data to an existing Pub/Sub Lite topic


    
    
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import array, create_map, col, lit, when
    from pyspark.sql.types import BinaryType, StringType
    import uuid
    
    # TODO(developer):
    # project_number = 11223344556677
    # location = "us-central1-a"
    # topic_id = "your-topic-id"
    
    spark = SparkSession.builder.appName("write-app").getOrCreate()
    
    # Create a RateStreamSource that generates consecutive numbers with timestamps:
    # |-- timestamp: timestamp (nullable = true)
    # |-- value: long (nullable = true)
    sdf = spark.readStream.format("rate").option("rowsPerSecond", 1).load()
    
    # Transform the dataframe to match the required data fields and data types:
    # https://github.com/googleapis/java-pubsublite-spark#data-schema
    sdf = (
        sdf.withColumn("key", lit("example").cast(BinaryType()))
        .withColumn("data", col("value").cast(StringType()).cast(BinaryType()))
        .withColumnRenamed("timestamp", "event_timestamp")
        # Populate the attributes field. For example, an even value will
        # have {"key1", [b"even"]}.
        .withColumn(
            "attributes",
            create_map(
                lit("key1"),
                array(when(col("value") % 2 == 0, b"even").otherwise(b"odd")),
            ),
        )
        .drop("value")
    )
    
    # After the transformation, the schema of the dataframe should look like:
    # |-- key: binary (nullable = false)
    # |-- data: binary (nullable = true)
    # |-- event_timestamp: timestamp (nullable = true)
    # |-- attributes: map (nullable = false)
    # |    |-- key: string
    # |    |-- value: array (valueContainsNull = false)
    # |    |    |-- element: binary (containsNull = false)
    sdf.printSchema()
    
    query = (
        sdf.writeStream.format("pubsublite")
        .option(
            "pubsublite.topic",
            f"projects/{project_number}/locations/{location}/topics/{topic_id}",
        )
        # Required. Use a unique checkpoint location for each job.
        .option("checkpointLocation", "/tmp/app" + uuid.uuid4().hex)
        .outputMode("append")
        .trigger(processingTime="1 second")
        .start()
    )
    
    # Wait 60 seconds to terminate the query.
    query.awaitTermination(60)
    query.stop()

To submit the write job to Managed Service for Apache Spark:

### Console

  1. Upload the PySpark script to your Cloud Storage bucket. 
     1. Go to the [Cloud Storage console](https://console.cloud.google.com/storage?project=).
     2. Select your bucket.
     3. Use **Upload files** to upload the PySpark script that you intend to use.
  2. Submit the job to your Managed Service for Apache Spark cluster: 
     1. Go to the [Managed Service for Apache Spark console](https://console.cloud.google.com/dataproc?project=).
     2. Navigate to jobs.
     3. Click **Submit job**.
     4. Fill in the job details.
     5. Under **Cluster** , choose your cluster.
     6. Under **Job** , give a name to the job ID.
     7. For **Job type** , choose PySpark.
     8. For **Main python file** , provide the gcloud storage URI of the uploaded PySpark script that starts with `gs://`.
     9. For **Jar files** , choose the latest Spark connector version from [Maven](https://mvnrepository.com/artifact/com.google.cloud/pubsublite-spark-sql-streaming) , look for the jar with dependencies in the download options, and copy its link.
     10. For **Arguments** , if you use the full PySpark script from GitHub, enter `--project_number=`PROJECT_NUMBER, `--location=`PUBSUBLITE_LOCATION, `--topic_id=`TOPIC_ID ; if you copy the PySpark script above with the to-do's completed, leave it blank.
     11. Under **Properties** , enter key `spark.master` and value `yarn`.
     12. Click **Submit**.



### gcloud

Use the [gcloud dataproc jobs submit pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pyspark) command to submit the job to Managed Service for Apache Spark:
    
    
    gcloud dataproc jobs submit pyspark spark_streaming_to_pubsublite_example.py \
        --region=$DATAPROC_REGION \
        --cluster=$CLUSTER_ID \
        --jars=gs://spark-lib/pubsublite/pubsublite-spark-sql-streaming-LATEST-with-dependencies.jar \
        --driver-log-levels=root=INFO \
        --properties=spark.master=yarn \
        -- --project_number=$PROJECT_NUMBER --location=$PUBSUBLITE_LOCATION --topic_id=$TOPIC
    

  * `--region`: the pre-selected Managed Service for Apache Spark [region](https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints).
  * `--cluster`: the Managed Service for Apache Spark cluster name.
  * `--jars`: the Pub/Sub Lite Spark Connector's uber jar with dependencies in a public Cloud Storage bucket. You can also visit this [link](https://search.maven.org/search?q=g:com.google.cloud%20a:pubsublite-spark-sql-streaming) to download the uber jar with dependencies from Maven.
  * `--driver-log-levels`: set logging level to INFO at the root level.
  * `--properties`: use YARN resource manager for the Spark master.
  * `--`: provide the arguments required by the script.



If the `writeStream` operation succeeds, you should see log messages like the following locally as well as in the job details page in the Google Cloud console:
    
    
    INFO com.google.cloud.pubsublite.spark.PslStreamWriter: Committed 1 messages for epochId ..
    

## Reading from Pub/Sub Lite

The following example will read messages from an existing Pub/Sub Lite subscription using the [`readStream`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.readStream.html) API. The connector will output messages that conforms to the fixed [table schema](https://github.com/googleapis/java-pubsublite-spark#data-schema) formatted as [`spark.sql.Row`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Row.html) .
    
    
    from pyspark.sql import SparkSession
    from pyspark.sql.types import StringType
    
    # TODO(developer):
    # project_number = 11223344556677
    # location = "us-central1-a"
    # subscription_id = "your-subscription-id"
    
    spark = SparkSession.builder.appName("read-app").master("yarn").getOrCreate()
    
    sdf = (
        spark.readStream.format("pubsublite")
        .option(
            "pubsublite.subscription",
            f"projects/{project_number}/locations/{location}/subscriptions/{subscription_id}",
        )
        .load()
    )
    
    sdf = sdf.withColumn("data", sdf.data.cast(StringType()))
    
    query = (
        sdf.writeStream.format("console")
        .outputMode("append")
        .trigger(processingTime="1 second")
        .start()
    )
    
    # Wait 120 seconds (must be >= 60 seconds) to start receiving messages.
    query.awaitTermination(120)
    query.stop()

To submit the read job to Managed Service for Apache Spark:

### Console

  1. Upload the PySpark script to your Cloud Storage bucket. 
     1. Go to the [Cloud Storage console](https://console.cloud.google.com/storage?project=).
     2. Select your bucket.
     3. Use **Upload files** to upload the PySpark script that you intend to use.
  2. Submit the job to your Managed Service for Apache Spark cluster: 
     1. Go to the [Managed Service for Apache Spark console](https://console.cloud.google.com/dataproc?project=).
     2. Navigate to jobs.
     3. Click **Submit job**.
     4. Fill in the job details.
     5. Under **Cluster** , choose your cluster.
     6. Under **Job** , give a name to the job ID.
     7. For **Job type** , choose PySpark.
     8. For **Main python file** , provide the gcloud storage URI of the uploaded PySpark script that starts with `gs://`.
     9. For **Jar files** , choose the latest Spark connector version from [Maven](https://mvnrepository.com/artifact/com.google.cloud/pubsublite-spark-sql-streaming) , look for the jar with dependencies in the download options, and copy its link.
     10. For **Arguments** , if you use the full PySpark script from GitHub, enter `--project_number=`PROJECT_NUMBER, `--location=`PUBSUBLITE_LOCATION, `--subscription_id=`SUBSCRIPTION_ID ; if you copy the PySpark script above with the to-do's completed, leave it blank.
     11. Under **Properties** , enter key `spark.master` and value `yarn`.
     12. Click **Submit**.



### gcloud

Use the [gcloud dataproc jobs submit pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pyspark) command again to submit the job to Managed Service for Apache Spark:
    
    
    gcloud dataproc jobs submit pyspark spark_streaming_to_pubsublite_example.py \
        --region=$DATAPROC_REGION \
        --cluster=$CLUSTER_ID \
        --jars=gs://spark-lib/pubsublite/pubsublite-spark-sql-streaming-LATEST-with-dependencies.jar \
        --driver-log-levels=root=INFO \
        --properties=spark.master=yarn \
        -- --project_number=$PROJECT_NUMBER --location=$PUBSUBLITE_LOCATION --subscription_id=$SUBSCRIPTION
    

  * `--region`: the pre-selected Managed Service for Apache Spark [region](https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints).
  * `--cluster`: the Managed Service for Apache Spark cluster name.
  * `--jars`: the Pub/Sub Lite Spark Connector's uber jar with dependencies in a public Cloud Storage bucket. You can also visit this [link](https://search.maven.org/search?q=g:com.google.cloud%20a:pubsublite-spark-sql-streaming) to download the uber jar with dependencies from Maven.
  * `--driver-log-levels`: set logging level to INFO at the root level.
  * `--properties`: use YARN resource manager for the Spark master.
  * `--`: provide required arguments for the script.



If the `readStream` operation succeeds, you should see log messages like the following locally as well as in the job details page in the Google Cloud console:
    
    
    +--------------------+---------+------+---+----+--------------------+--------------------+----------+
    |        subscription|partition|offset|key|data|   publish_timestamp|     event_timestamp|attributes|
    +--------------------+---------+------+---+----+--------------------+--------------------+----------+
    |projects/50200928...|        0| 89523|  0|   .|2021-09-03 23:01:...|2021-09-03 22:56:...|        []|
    |projects/50200928...|        0| 89524|  1|   .|2021-09-03 23:01:...|2021-09-03 22:56:...|        []|
    |projects/50200928...|        0| 89525|  2|   .|2021-09-03 23:01:...|2021-09-03 22:56:...|        []|
    

## Replay and purge messages from Pub/Sub Lite

[Seek operations](https://docs.cloud.google.com/pubsub/lite/docs/seek) don't work when reading from Pub/Sub Lite using the Pub/Sub Lite Spark Connector because [Apache Spark](https://spark.apache.org/) systems perform their own tracking of offsets within partitions. The workaround is to drain, seek and restart the workflows.

**Note:** Due to [limitations](https://issues.apache.org/jira/browse/SPARK-41942) in [Apache Spark](https://spark.apache.org/)'s processing model, don't attempt to seek to or create a subscription at the beginning of backlog if using the Pub/Sub Lite Spark Connector to read from Pub/Sub Lite. Instead, seek to the publish timestamp of the unix epoch to replay all messages from backlog.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the topic and subscription.
         
         gcloud pubsub lite-topics delete $TOPIC
         gcloud pubsub lite-subscriptions delete $SUBSCRIPTION
         

  2. Delete the Managed Service for Apache Spark cluster.
         
         gcloud dataproc clusters delete $CLUSTER_ID --region=$DATAPROC_REGION
         

  3. Remove the Cloud Storage bucket.
         
         gcloud storage rm gs://$BUCKET
         




## What's next

  * Check out the [word count example in Java](https://github.com/googleapis/java-pubsublite-spark/tree/master/samples) for the Pub/Sub Lite Spark Connector.

  * Learn how to [access the Managed Service for Apache Spark job driver output](https://docs.cloud.google.com/dataproc/docs/guides/dataproc-job-output).

  * Other Spark connectors by Google Cloud products: [BigQuery connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/bigquery), [Bigtable connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-bigtable), [Cloud Storage connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
