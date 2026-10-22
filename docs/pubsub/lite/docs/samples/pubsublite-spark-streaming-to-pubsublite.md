---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-spark-streaming-to-pubsublite/
title: Write to Pub/Sub Lite from Spark (streaming) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:07.409282+00:00
---

# Write to Pub/Sub Lite from Spark (streaming)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-spark-streaming-to-pubsublite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Write to Pub/Sub Lite from Spark (streaming) Stay organized with collections  Save and categorize content based on your preferences. 

Write messages to a Pub/Sub Lite topic from a Spark cluster in the streaming mode.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Write Pub/Sub Lite messages by using Apache Spark](https://docs.cloud.google.com/pubsub/lite/docs/write-messages-apache-spark)



## Code sample

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
