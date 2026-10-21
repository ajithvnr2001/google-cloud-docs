---
url: https://docs.cloud.google.com/dataflow/docs/guides/job-builder/
title: Job builder UI overview \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:37.482904+00:00
---

# Job builder UI overview  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/job-builder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Job builder UI overview Stay organized with collections  Save and categorize content based on your preferences. 

The job builder is a visual UI for building and running Dataflow pipelines in the Google Cloud console, without writing code.

The following image shows a detail from the job builder UI. In this image, the user is creating a pipeline to read from Pub/Sub to BigQuery:

![A screenshot of the job builder UI](https://docs.cloud.google.com/static/dataflow/images/job-builder.png)

## Overview

The job builder supports reading and writing the following types of data:

  * Pub/Sub messages
  * BigQuery table data
  * CSV files, JSON files, and text files in Cloud Storage
  * PostgreSQL, MySQL, Oracle, and SQL Server table data
  * Apache Iceberg table data
  * Delta Lake table data



It supports pipeline transforms including filter, map, SQL, group-by, join, and explode (array flatten).

With the job builder you can:

  * Stream from Pub/Sub to BigQuery with transforms and windowed aggregation
  * Write data from Cloud Storage to BigQuery
  * Use error handling to filter erroneous data (dead-letter queue)
  * Manipulate or aggregate data using SQL with the SQL transform
  * Add, modify, or drop fields from data with mapping transforms
  * Schedule recurring batch jobs



The job builder can also save pipelines as [Apache Beam YAML](https://beam.apache.org/documentation/sdks/yaml/) files and load pipeline definitions from Beam YAML files. By using this feature, you can design your pipeline in the job builder and then store the YAML file in Cloud Storage or a source control repository for reuse. YAML job definitions can also be used to launch jobs using the gcloud CLI.

Consider the job builder for the following use cases:

  * You want to build a pipeline quickly without writing code.
  * You want to save a pipeline to YAML for re-use.
  * Your pipeline can be expressed using the supported sources, sinks, and transforms.
  * There is no [Google-provided template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) that matches your use case.



## Run a sample job

The Word Count example is a batch pipeline that reads text from Cloud Storage, tokenizes the text lines into individual words, and performs a frequency count on each of the words.

If the Cloud Storage bucket is outside of your [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview), create an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) that allows access to the bucket.

To run the Word Count pipeline, follow these steps:

  1. Go to the **Jobs** page in the Google Cloud console.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. Click add_box**Create job from template**.

  3. In the side pane, click edit **Job builder**.

  4. Click **Load blueprints** expand_more.

  5. Click **Word Count**. The job builder is populated with a graphical representation of the pipeline.

For each pipeline step, the job builder displays a card that specifies the configuration parameters for that step. For example, the first step reads text files from Cloud Storage. The location of the source data is pre-populated in the **Text location** box.




![A screenshot of the job builder](https://docs.cloud.google.com/static/dataflow/images/job-builder-quickstart.png)

  1. Locate the card titled **New sink**. You might need to scroll.

  2. In the **Text location** box, enter the Cloud Storage location path prefix for the output text files.

  3. Click **Run job**. The job builder creates a Dataflow job and then navigates to the [job graph](https://docs.cloud.google.com/dataflow/docs/guides/job-graph). When the job starts, the job graph shows a graphical representation of the pipeline. This graph representation is similar to the one shown in the job builder. As each step of the pipeline runs, the status is updated in the job graph.




The **Job info** panel shows the overall status of the job. If the job completes successfully, the **Job status** field updates to `Succeeded`.

## What's next

  * [Use the Dataflow job monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).
  * [Create a custom job](https://docs.cloud.google.com/dataflow/docs/guides/job-builder-custom-job) in the job builder.
  * [Save and load](https://docs.cloud.google.com/dataflow/docs/guides/job-builder-save-load-yaml) YAML job definitions in the job builder.
  * Learn more about [Beam YAML](https://beam.apache.org/documentation/sdks/yaml/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
