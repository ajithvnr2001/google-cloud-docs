---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/pubsub-lite/
title: Pub/Sub Lite with Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:34.419829+00:00
---

# Pub/Sub Lite with Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/pubsub-lite/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Pub/Sub Lite with Managed Service for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

[Pub/Sub Lite](https://docs.cloud.google.com/pubsub/lite/docs "Pub/Sub Lite") is a real-time messaging service built for low cost and offers lower reliability compared to Pub/Sub. Pub/Sub Lite offers zonal and regional topics for storage.

The [Pub/Sub Lite Spark Connector](https://github.com/googleapis/java-pubsublite-spark) supports Pub/Sub Lite as an input source to Apache Spark Structured Streaming in the default micro-batch processing and experimental continuous processing modes.

## Use Pub/Sub Lite with Managed Service for Apache Spark

###  Java 

The `samples` directory in the [`java-pubsublite-spark` repository on GitHub](https://github.com/googleapis/java-pubsublite-spark) contains a Spark example in Java that uses Pub/Sub Lite with Managed Service for Apache Spark. To run the example, follow the [directions in the Spark example](https://github.com/googleapis/java-pubsublite-spark/tree/master/samples).

  1. To get started, clone the `java-pubsublite-spark` GitHub repository: 
         
         git clone https://github.com/googleapis/java-pubsublite-spark
         cd java-pubsublite-spark/samples
         




###  Python / Scala 

The connector is available from the [Maven Central repository](https://search.maven.org/artifact/com.google.cloud/pubsublite-spark-sql-streaming). You can download and provide it using the `--packages` option when using the spark-submit command or set it using the `spark.jars.packages` [configuration property](https://spark.apache.org/docs/latest/configuration.html#available-properties).

## What's next

  * See [Using Pub/Sub Lite with Apache Spark](https://docs.cloud.google.com/pubsub/lite/docs/write-messages-apache-spark), a quickstart that runs a Python script on a Managed Service for Apache Spark cluster to read and write data from and to Pub/Sub Lite.
  * [Select the version of the Pub/Sub Lite Spark Connector](https://search.maven.org/artifact/com.google.cloud/pubsublite-spark-sql-streaming), and then download its JAR on the linked page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
