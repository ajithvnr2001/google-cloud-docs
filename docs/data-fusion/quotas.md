---
url: https://docs.cloud.google.com/data-fusion/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:23:28.578756+00:00
---

# Quotas and limits  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion)
  * [ Resources ](https://docs.cloud.google.com/data-fusion/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains current content limits and rate quotas for the Cloud Data Fusion API.

## Rate quotas

The following [Cloud Data Fusion API](https://docs.cloud.google.com/data-fusion/docs/reference/rest) rate quotas apply to Cloud Data Fusion control plane API requests, such as requests to create, update, or delete Cloud Data Fusion instances. They do not apply to requests for other Google Cloud resources, such as Compute Engine or Cloud Storage resources, to run data processing pipelines on Cloud Data Fusion instances (other [quota limits](https://console.cloud.google.com/iam-admin/quotas) may apply to requests for pipeline resources).

Quotas are subject to change.

Quota | Value  
---|---  
Requests per minute from a single user in a single region | 600  
  
These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

## Other Google Cloud quotas

Your Cloud Data Fusion instances can use other Google Cloud products to run pipelines. These products have project-level quotas, which include quotas that apply to Cloud Data Fusion use.

### Managed Service for Apache Spark

Cloud Data Fusion uses Managed Service for Apache Spark as the execution environment for pipelines. [Managed Service for Apache Spark quota](https://docs.cloud.google.com/dataproc/quotas "Cloud Dataproc quota") applies to all pipelines that you execute.

### Cloud Logging

Cloud Data Fusion saves logs in [Logging](https://docs.cloud.google.com/logging "Stackdriver Logging"). The [Logging quota](https://docs.cloud.google.com/logging/quota-policy "Stackdriver Logging quota") applies to your Cloud Data Fusion instances.

### Additional quotas

Depending on the Google Cloud services your pipelines use, additional quotas might apply, for example:

  * BigQuery—When reading or writing data into BigQuery, the [BigQuery quota](https://docs.cloud.google.com/bigquery/quota-policy) applies.
  * Bigtable—When reading or writing data into Bigtable, the [Bigtable quota](https://docs.cloud.google.com/bigtable/quotas) applies.
  * Cloud Storage—When reading or writing data into Cloud Storage, the [Cloud Storage quota](https://docs.cloud.google.com/storage/quotas) applies.
  * Compute Engine—When reading or writing data into Compute Engine, the [Compute Engine quota](https://docs.cloud.google.com/compute/quotas) applies.
  * Spanner—When reading or writing data into Spanner, the [Spanner quota](https://docs.cloud.google.com/spanner/quotas) applies.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
