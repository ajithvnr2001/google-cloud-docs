---
url: https://docs.cloud.google.com/dataproc-serverless/docs/guides/data-lineage/
title: Use data lineage with Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:48.379897+00:00
---

# Use data lineage with Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-serverless/docs/guides/data-lineage/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use data lineage with Managed Service for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable [data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage) on Managed Service for Apache Spark batch workloads and interactive sessions at the project, batch workload, or interactive session level.

## Overview

Data lineage is a [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) feature that lets you track how data moves through your systems: where it comes from, where it is passed to, and what transformations are applied to it.

Managed Service for Apache Spark workloads and sessions capture lineage events and publish them to the Knowledge Catalog [Data Lineage API](https://docs.cloud.google.com/dataplex/docs/reference/data-lineage/rest). Managed Service for Apache Spark integrates with the Data Lineage API through [OpenLineage](https://docs.cloud.google.com/dataplex/docs/open-lineage), using the [OpenLineage Spark plugin](https://github.com/OpenLineage/OpenLineage).

You can access lineage information through Knowledge Catalog, using [lineage graphs](https://docs.cloud.google.com/dataplex/docs/about-data-lineage#lineage-feature-graph) and the [Data Lineage API](https://docs.cloud.google.com/dataplex/docs/reference/data-lineage/rest). For more information, see View lineage graphs in Knowledge Catalog.

## Availability

Data lineage, which supports BigQuery and Cloud Storage data sources, is available for workloads and sessions that run with [supported Managed Service for Apache Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions) with the following exceptions and limitations:

  * Data lineage is not available for SparkR or Spark streaming workloads or sessions.



## Before you begin

  1. On the project selector page in the Google Cloud console, select the project to use for your Managed Service for Apache Spark workloads or sessions.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Data Lineage API.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datalineage.googleapis.com)

**Upcoming Spark data lineage changes** See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for the announcement of a change that will automatically make Spark data lineage available to your projects, batch workloads, and interactive sessions when you enable the Data Lineage API (see [Control lineage ingestion for a service](https://docs.cloud.google.com/dataplex/docs/use-lineage#control-ingestion)) without requiring additional project, batch workload, or interactive session settings.




## Required roles

If your batch workload uses the default [Managed Service for Apache Spark service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account), it has the [`Managed Service for Apache Spark Worker`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) role, which contains the permissions required by data lineage.

However, if your batch workload uses a custom service account to enable data lineage, you must grant **one** of the roles listed in the following paragraph, which contain the permissions required by data lineage, to the custom service account. 

To get the permissions that you need to use data lineage with Managed Service for Apache Spark , ask your administrator to grant you the following IAM roles on your batch workload custom service account: 

  * Grant **one** of the following roles: 
    * [Managed Service for Apache Spark Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)
    * [Data Lineage Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)
    * [Data Lineage Producer ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)
    * [Data Lineage Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable Spark data lineage

You can enable Spark data lineage for your project, batch workload, or interactive session.

### Enable data lineage at the project level

After you enable Spark data lineage at the project level, subsequent Spark jobs that run in a batch workload or interactive session will have Spark data lineage enabled.

**Note:** Setting data lineage on a project does not enable data lineage for batch workloads and interactive sessions that use the [Managed Service for Apache Spark 3.0 runtime](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions). You must separately enable data lineage on the 3.0 batch workload, interactive session or session template. 

To enable Spark data lineage on your project, [set the following custom project metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata):

Key | Value  
---|---  
`DATAPROC_LINEAGE_ENABLED` | `true`  
  
You can disable Spark data lineage for a project by setting the `DATAPROC_LINEAGE_ENABLED` metadata to `false`.

**Note:** You can also disable Spark data lineage for a project by [disabling lineage ingestion for Managed Service for Apache Spark](https://docs.cloud.google.com/dataplex/docs/use-lineage#disable-lineage-ingestion). This setting overrides all other data lineage settings.

### Enable data lineage on a Spark batch workload

To enable data lineage on a batch workload, set the `spark.dataproc.lineage.enabled` property to `true` when you submit the workload. This setting overrides any Spark data lineage setting at the project level: if Spark data lineage is disabled at the project level but enabled for the batch workload, the batch workload setting takes precedence.

You can disable Spark data lineage on a Spark batch workload by setting the `spark.dataproc.lineage.enabled` property to `false` when you submit the workload.

**Note:** You can also disable Spark data lineage by [disabling lineage ingestion for Managed Service for Apache Spark](https://docs.cloud.google.com/dataplex/docs/use-lineage#disable-lineage-ingestion). This setting overrides all other data lineage settings.

This example uses the gcloud CLI to submit a batch `lineage-example.py` workload with Spark lineage enabled.
    
    
    gcloud dataproc batches submit pyspark lineage-example.py \
        --region=REGION \
        --deps-bucket=gs://BUCKET \
        --properties=spark.dataproc.lineage.enabled=true
    

The following `lineage-example.py` code reads data from a public BigQuery table, and then writes the output a new table in an existing BigQuery dataset. It uses a Cloud Storage bucket for temporary storage.
    
    
    #!/usr/bin/env python
    
    from pyspark.sql import SparkSession
    import sys
    
    spark = SparkSession \
      .builder \
      .appName('LINEAGE_BQ_TO_BQ') \
      .getOrCreate()
    
    source = 'bigquery-public-data:samples.shakespeare'
    words = spark.read.format('bigquery') \
      .option('table', source) \
      .load()
    words.createOrReplaceTempView('words')
    
    word_count = spark.sql('SELECT word, SUM(word_count) AS word_count FROM words GROUP BY word')
    
    destination_table = 'PROJECT_ID:DATASET.TABLE'
    word_count.write.format('bigquery') \
      .option('table', destination_table) \
      .option('writeMethod', 'direct') \
      .save()
    

Replace the following:

  * REGION: The [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) to run the workload
  * BUCKET: The name of an existing Cloud Storage bucket to store dependencies
  * PROJECT_ID, DATASET, and TABLE: The project ID, the name of an existing BigQuery dataset, and the name of a new table to create in the dataset (the table must not exist)



You can view the lineage graph in the Knowledge Catalog UI.

![Spark lineage graph](https://docs.cloud.google.com/static/managed-spark/images/lineage-example.png)

### Enable data lineage on a Spark interactive session or session template

To enable data lineage on a Spark interactive session or session template, set the `spark.dataproc.lineage.enabled` property to `true` when you [create the session or session template](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates). This setting overrides any Spark data lineage setting at the project level: if Spark data lineage is disabled at the project level but enabled for the interactive session, the interactive session setting takes precedence.

You can disable Spark data lineage on a Spark interactive session or session template by setting the `spark.dataproc.lineage.enabled` property to `false` when you create the interactive session or session template.

**Note:** You can also disable Spark data lineage by [disabling lineage ingestion for Managed Service for Apache Spark](https://docs.cloud.google.com/dataplex/docs/use-lineage#disable-lineage-ingestion). This setting overrides all other data lineage settings.

The following PySpark notebook code configures a Managed Service for Apache Spark interactive session with Spark data lineage enabled. It then creates a [Spark Connect](https://spark.apache.org/spark-connect/) session that runs a word count query on a public BigQuery Shakespeare dataset, and then writes the output to a new table in an existing BigQuery dataset (see [Create a Spark session in a BigQuery Studio notebook](https://docs.cloud.google.com/bigquery/docs/use-spark#create-a-single-spark-session-in-a-bigquery-studio-notebook)) .
    
    
    # Configure the Dataproc Serverless interactive session
    # to enable Spark data lineage.
    from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
    
    session = Session()
    session.runtime_config.properties["spark.dataproc.lineage.enabled"] = "true"
    
    # Create the Spark Connect session.
    from google.cloud.dataproc_spark_connect import DataprocSparkSession
    
    spark = DataprocSparkSession.builder.dataprocSessionConfig(session).getOrCreate()
    
    # Run a wordcount query on the public BigQuery Shakespeare dataset.
    source = "bigquery-public-data:samples.shakespeare"
    words = spark.read.format("bigquery").option("table", source).load()
    words.createOrReplaceTempView('words')
    word_count = spark.sql(
               'SELECT word, SUM(word_count) AS word_count FROM words GROUP BY word')
    
    # Output the results to a BigQuery destination table.
    destination_table = 'PROJECT_ID:DATASET.TABLE'
    word_count.write.format('bigquery') \
      .option('table', destination_table) \
      .save()
    

Replace the following:

  * PROJECT_ID, DATASET, and TABLE: The project ID, the name of an existing BigQuery dataset, and the name of a new table to create in the dataset (the table must not exist)



You can view the data lineage graph by clicking the destination table name listed in the navigation pane on BigQuery **Explorer** page, then selecting the lineage tab on the table details pane.

![Spark lineage graph](https://docs.cloud.google.com/static/managed-spark/docs/images/shakespeare-lineage-graph.png)

## View lineage in Knowledge Catalog

A lineage graph displays relationships between your project resources and the processes that created them. You can [view data lineage information](https://docs.cloud.google.com/dataplex/docs/use-lineage) in the Google Cloud console or retrieve the information from the [Data Lineage API](https://docs.cloud.google.com/dataplex/docs/reference/data-lineage/rest) as JSON data.

## What's next

  * Learn more about [data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage).
  * Try data lineage in an interactive lab: [Capture and Explore Data Updates With Data Lineage and OpenLineage in Dataplex](https://www.skills.google/focuses/133556?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=70803730).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
