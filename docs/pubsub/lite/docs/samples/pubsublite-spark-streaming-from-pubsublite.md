---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-spark-streaming-from-pubsublite/
title: Read from Pub/Sub Lite from Spark (streaming) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:07.467153+00:00
---

# Read from Pub/Sub Lite from Spark (streaming)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-spark-streaming-from-pubsublite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Read from Pub/Sub Lite from Spark (streaming) Stay organized with collections  Save and categorize content based on your preferences. 

Read messages from a Pub/Sub Lite subscription from a Spark cluster in the streaming mode.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Write Pub/Sub Lite messages by using Apache Spark](https://docs.cloud.google.com/pubsub/lite/docs/write-messages-apache-spark)



## Code sample

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
