---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-bigquery/
title: Using Sensitive Data Protection with BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:00.267680+00:00
---

# Using Sensitive Data Protection with BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-bigquery/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Using Sensitive Data Protection with BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page contains references to pages that provide information on how to use Sensitive Data Protection with [BigQuery](https://docs.cloud.google.com/bigquery).

## Quickstart guides

[Quickstart: Scheduling a Sensitive Data Protection inspection scan](https://docs.cloud.google.com/sensitive-data-protection/docs/schedule-inspection-scan)
    Schedule periodic inspection of a Cloud Storage bucket, a BigQuery table, or a Datastore kind. For detailed instructions, see [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers).

## How-to guides

This section provides a categorized list of task-based guides that demonstrate how to use Sensitive Data Protection with BigQuery.

### Inspection

[Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage)
    Create a one-time job that searches for sensitive data in a Cloud Storage bucket, a BigQuery table, or a Datastore kind.
[Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)
    Create and schedule a job trigger that searches for sensitive data in a Cloud Storage bucket, a BigQuery table, or a Datastore kind. A job trigger automates the creation of Sensitive Data Protection jobs on a periodic basis.

### Working with scan results

[Adding Knowledge Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects)
    Automatically add Knowledge Catalog aspects to your data after Sensitive Data Protection profiles your resources
[Sending Sensitive Data Protection scan results to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-scc)
    Scan a Cloud Storage bucket, a BigQuery table, or a Datastore kind, and then send the findings to Security Command Center.
[Analyzing and reporting on Sensitive Data Protection findings](https://docs.cloud.google.com/sensitive-data-protection/docs/analyzing-and-reporting)
    Use BigQuery to run analytics on Sensitive Data Protection findings.
[Querying Sensitive Data Protection findings in BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/querying-findings)
    Look through sample queries that you can use in BigQuery to analyze findings that Sensitive Data Protection identified.

### Re-identification risk analysis

[Measuring re-identification and disclosure risk](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis)
    

Analyze structured data stored in a BigQuery table and compute the following re-identification risk metrics:

  * [_k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity)
  * [_l_ -diversity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-l-diversity)
  * [_k_ -map](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-map)
  * [_δ_ -presence](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-d-presence)


[Computing numerical and categorical statistics](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-stats)
    

Determine minimum, maximum, and quantile values for an individual BigQuery column.

[Visualizing re-identification risk using Data Studio](https://docs.cloud.google.com/sensitive-data-protection/docs/visualizing_re-id_risk)
    

Measure the _k_ -anonymity of a dataset, and then visualize it in Data Studio.

## Tutorials

[De-identify BigQuery data at query time](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-bq-tutorial)
    Follow a step-by-step tutorial that uses BigQuery remote functions to de-identify and re-identify data in real-time query results.
[De-identification and re-identification of PII in large-scale datasets using Sensitive Data Protection](https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp)
    Review a reference architecture for creating an automated data transformation pipeline that de-identifies sensitive data like personally identifiable information (PII).

## Best practices

[Secure a BigQuery data warehouse that stores confidential data](https://docs.cloud.google.com/architecture/confidential-data-warehouse-blueprint)
    Architectural overview and best practices for data governance when creating, deploying, and operating a data warehouse in Google Cloud, including data de-identification, differential handling of confidential data, and column-level access controls.

## Community contributions

The following are owned and managed by community members, and not by the Sensitive Data Protection team. For questions on these items, contact their respective owners.

[Event-driven serverless scheduling architecture with Sensitive Data Protection](https://github.com/GoogleCloudPlatform/community/blob/master/archived/event-driven-serverless-scheduling-framework-dlp/index.md)
    Set up an event-driven, serverless scheduling application that uses the Cloud Data Loss Prevention API to inspect BigQuery data.
[Real-time anomaly detection using Google Cloud stream analytics and AI services](https://github.com/GoogleCloudPlatform/df-ml-anomaly-detection)
    Walk through a real-time artificial intelligence (AI) pattern for detecting anomalies in log files. This proof-of-concept uses Pub/Sub, Dataflow, BigQuery ML, and Sensitive Data Protection.
[Relational database import to BigQuery with Dataflow and Sensitive Data Protection](https://github.com/GoogleCloudPlatform/dlp-rdb-bq-import)
    Use Dataflow and Sensitive Data Protection to securely tokenize and import data from a relational database to BigQuery. This example describes how to tokenize PII data before it's made persistent.

## Pricing

When you inspect a BigQuery table, you incur Sensitive Data Protection costs, according to the [storage inspection job pricing](https://cloud.google.com/sensitive-data-protection/pricing#storage-pricing).

In addition, when you save inspection findings to a BigQuery table, [BigQuery charges](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing) apply.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
