---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-test-mode/
title: Profile a single data resource \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:54.945599+00:00
---

# Profile a single data resource  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-test-mode/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Profile a single data resource Stay organized with collections  Save and categorize content based on your preferences. 

If you only want to profile a single data resource, you can do so by creating a project-level scan configuration. 

## Supported resources

The following resource types are supported:

  * BigQuery table
  * Cloud SQL table
  * Cloud Storage bucket
  * Vertex AI dataset
  * Vertex AI tuning job
  * Amazon S3 bucket
  * Azure Blob Storage container



## Differences between profiling a single data resource and standard profiling

Single-resource profiling differs from standard profiling in the following ways:

  * Single-resource profiling is available only in project view.
  * A single-resource discovery configuration lets you profile only one data resource. You can't add schedules to the configuration, but you can edit the catch-all schedule. You can't add filters to the schedule.
  * You can create many single-resource discovery configurations for different data resources in a project. For each data resource, you can have only one single-resource discovery configuration.



## Create a single-resource discovery configuration

To create a single-resource discovery configuration, see the instructions for the data that you want to profile:

  * [Profile BigQuery data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project)
  * [Profile Cloud SQL data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-sql)
  * [Profile Cloud Storage data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-storage)
  * [Profile Vertex AI data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-vertex-ai)
  * [Discovery for Amazon S3 data](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-amazon-s3)



When you're prompted to select the scope of the scan, select the single-resource option, and then enter the details of the resource.

## Profile regeneration

Sensitive Data Protection reprofiles data as described in [Frequency of data profile generation](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-frequency). You can customize the profiling frequency in your scan configuration by [creating a schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder#manage-schedules). To force the discovery service to reprofile your data, see [Force a reprofile operation](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles#force-reprofile). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
