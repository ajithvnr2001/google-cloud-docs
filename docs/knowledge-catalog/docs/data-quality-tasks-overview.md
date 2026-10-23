---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-quality-tasks-overview/
title: Data quality tasks overview \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:58.368722+00:00
---

# Data quality tasks overview  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-quality-tasks-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Data quality tasks overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Knowledge Catalog (formerly Dataplex Universal Catalog) data quality tasks is a legacy offering based on open source software. We recommend that you start using the latest built-in [Automatic data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview) offering.

Knowledge Catalog data quality tasks let you define and run data quality checks across tables in BigQuery and Cloud Storage. Knowledge Catalog data quality tasks also let you apply regular data controls in BigQuery environments.

## When to create Knowledge Catalog data quality tasks

Knowledge Catalog data quality tasks can help you with the following:

  * Validate data as part of a data production pipeline.
  * Routinely monitor the quality of datasets against your expectations.
  * Build data quality reports for regulatory requirements.



## Benefits

  * **Customizable specifications.** You can use the highly flexible YAML syntax to declare your data quality rules.
  * **Serverless implementation.** Knowledge Catalog does not need any infrastructure setup.
  * **Zero-copy and automatic pushdown.** YAML checks are converted to SQL and pushed down to BigQuery, resulting in no data copy.
  * **Schedulable data quality checks.** You can schedule data quality checks through the serverless scheduler in Knowledge Catalog, or use the Dataplex API through external schedulers like Managed Airflow for pipeline integration.
  * **Managed experience.** Knowledge Catalog uses an open source data quality engine, [CloudDQ](https://github.com/GoogleCloudPlatform/cloud-data-quality), to run data quality checks. However, Knowledge Catalog provides a seamless managed experience for performing your data quality checks.



## How data quality tasks work

The following diagram shows how Knowledge Catalog data quality tasks work:

![image](https://docs.cloud.google.com/static/knowledge-catalog/images/data-quality.png)

  * **Input from users**
    * **YAML specification** : A set of one or more YAML files that define data quality rules based on the specification syntax. You store the YAML files in a Cloud Storage bucket in your project. Users can run multiple rules simultaneously, and those rules can be applied to different BigQuery tables, including tables across different datasets or Google Cloud projects. The specification supports incremental runs for only validating new data. To create a YAML specification, see [Create a specification file](https://docs.cloud.google.com/knowledge-catalog/docs/check-data-quality#create-a-specification-file).
    * **BigQuery result table** : A user-specified table where the data quality validation results are stored. The Google Cloud project in which this table resides can be a different project than the one in which the Knowledge Catalog data quality task is used.
  * **Tables to validate**
    * Within the YAML specification, you need to specify which tables you want to validate for which rules, also known as a _rule binding_. The tables can be BigQuery native tables or BigQuery external tables in Cloud Storage. The YAML specification lets you specify tables inside or outside a Knowledge Catalog zone.
    * BigQuery and Cloud Storage tables that are validated in a single run can belong to different projects.
  * **Knowledge Catalog data quality task** : A Knowledge Catalog data quality task is configured with a prebuilt, maintained CloudDQ PySpark binary and takes the YAML specification and BigQuery result table as the input. Similar to other [Knowledge Catalog tasks](https://docs.cloud.google.com/knowledge-catalog/docs/schedule-custom-spark-tasks), the Knowledge Catalog data quality task runs on a serverless Spark environment, converts the YAML specification to BigQuery queries, and then runs those queries on the tables that are defined in the specification file.



## Pricing

When you run Knowledge Catalog data quality tasks, you are charged for BigQuery and Managed Service for Apache Spark (Batches) usage.

  * The Knowledge Catalog data quality task converts the specification file to BigQuery queries and runs them in the user project. See [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

  * Knowledge Catalog uses Spark to run the prebuilt, Google-maintained [open source CloudDQ](https://github.com/GoogleCloudPlatform/cloud-data-quality) driver program to convert user specification to BigQuery queries. See [Managed Service for Apache Spark pricing](https://docs.cloud.google.com/dataproc-serverless/pricing).




There are no charges for using Knowledge Catalog to organize data or using the serverless scheduler in Knowledge Catalog to schedule data quality checks. See [Knowledge Catalog pricing](https://docs.cloud.google.com/dataplex/pricing).

## What's next

  * [Create Knowledge Catalog data quality checks](https://docs.cloud.google.com/knowledge-catalog/docs/check-data-quality).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
