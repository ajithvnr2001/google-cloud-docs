---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-vertex-ai/
title: Sensitive data discovery for Vertex AI \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:33.178811+00:00
---

# Sensitive data discovery for Vertex AI  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-vertex-ai/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Sensitive data discovery for Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Sensitive Data Protection discovery for use with Vertex AI.

Sensitive Data Protection discovery helps you learn about the data included in your Vertex AI training datasets and tuning jobs. Discovery generates [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) that provide insights like the information types ([_infoTypes_](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference)) detected and the sensitivity level of the data that you use for training and tuning models.

## Benefits

This feature offers the following benefits:

  * You can monitor your Vertex AI datasets and tuning jobs—at the organization, folder, or project level—for sensitive data, and [report on the results](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles).
  * If discovery detects sensitive training or tuning data, you can use the data profiles to identify which resources need to be further investigated. You can [perform a deep inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles#create-inspection-job) and find all sensitive instances in a resource.
  * You can [send discovery results to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc) so that your AI-related workloads with potentially sensitive data are taken into account when you evaluate your organization's security posture.



## Supported data source

This feature can profile the following types of data referenced in your Vertex AI datasets and tuning jobs:

  * Training and tuning data in Cloud Storage buckets. For information about the supported file types, see [File clusters](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#file_clusters).
  * Training data in BigQuery tables.



## How it works

When you profile a Vertex AI dataset, Sensitive Data Protection generates a _file store data profile_ or _table data profile_ , depending on where the training data is stored: a Cloud Storage bucket or a BigQuery table.

When you profile a Vertex AI tuning job, Sensitive Data Protection generates a _file store data profile_.

A data profile provides insights and metadata about the resource that you profiled. For each Vertex AI dataset or tuning job, the generated data profile includes the following information.

**Note:** Sensitive Data Protection uses the term _file store_ to refer to a file storage bucket or container.

  * The sensitivity and data risk levels of the training or tuning data
  * The types of sensitive information found in the training or tuning data—for example, driver's license IDs and email addresses



For a full list of insights and metadata in each file store data profile, see [File store data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#file-store-data-profile).

For a full list of insights and metadata in each table data profile, see [Table data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#table-data-profile).

For more information about the discovery service, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## Pricing

When you profile data, you incur Sensitive Data Protection charges according to your chosen [discovery pricing mode](https://docs.cloud.google.com/sensitive-data-protection/pricing#data_profiling_pricing).

In addition, if your training or tuning data is in a Cloud Storage bucket, then Cloud Storage charges you for requests that Sensitive Data Protection makes to profile the data. The following sections describe the associated Cloud Storage charges that you incur.

### Class B operations

You are charged for the Class B (`storage.buckets.get`) operations that Sensitive Data Protection performs in the process of profiling data in your Cloud Storage buckets.

For information about how much Cloud Storage charges for Class B operations, see [Operation charges](https://cloud.google.com/storage/pricing#operations-pricing) in the Cloud Storage documentation.

### Retrieval fees

For objects that have a non-Standard storage class, you are charged for retrieval fees. For information about how much Cloud Storage charges for data retrieval, see [Retrieval fees](https://cloud.google.com/storage/pricing#retrieval-pricing) in the Cloud Storage documentation.

## What's next

  * [Profile Vertex AI data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-vertex-ai)
  * [Profile Vertex AI data in an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-vertex-ai)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
