---
url: https://docs.cloud.google.com/knowledge-catalog/docs/faq/
title: Knowledge Catalog FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:52.750762+00:00
---

# Knowledge Catalog FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/faq/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Resources ](https://docs.cloud.google.com/knowledge-catalog/docs/resources)



Send feedback 

#  Knowledge Catalog FAQ Stay organized with collections  Save and categorize content based on your preferences. 

This document answers frequently asked questions about Google Cloud Knowledge Catalog (formerly Dataplex Universal Catalog).

For more information about Knowledge Catalog, see [Knowledge Catalog overview](https://docs.cloud.google.com/knowledge-catalog/docs/introduction).

## General concepts

Explore frequently asked questions about Knowledge Catalog features.

### What is Knowledge Catalog?

Knowledge Catalog is an intelligent governance solution for data and AI assets in Google Cloud. It provides a centralized inventory where you can discover, manage, and govern your data across Google Cloud data sources like BigQuery, Cloud Storage, Pub/Sub, and Spanner.

Knowledge Catalog uses AI to automate data discovery, metadata enrichment, and data quality. Through its governed data catalog, Knowledge Catalog provides the essential grounding that AI agents need to generate high-quality content.

### What is Knowledge Catalog used for?

Knowledge Catalog solves the "data cold start" problem—the time wasted trying to find, understand, and trust data before you can actually use it. Its primary uses include the following:

  * Accelerated data discovery: Instead of navigating complex organizational silos to locate data, you can use natural language search (for example, "Show me the most recent customer churn data") to find assets across Google Cloud resources instantly, which increases productivity for data consumers.

  * Grounding AI agents: It acts as the "source of truth" for generative AI or ADK. By linking physical data to business definitions, it ensures that AI agents (like those built on Vertex AI) use high-quality data, which significantly reduces AI hallucinations and improves trust in AI-generated insights.

  * Automated data governance: It automatically scans your data to identify sensitive information (that is, PII), tracks where data comes from (lineage), and monitors its accuracy (automatic data quality). These capabilities help improve data trust, security, and compliance with less manual effort.

  * Discovering "dark data": It can scan unstructured files (for example, PDFs or images in Cloud Storage), extract the information inside, and make it searchable and queryable in BigQuery, which helps you unlock insights from previously inaccessible data.




To get started with these scenarios, see [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).

### What types of metadata does Knowledge Catalog store?

Knowledge Catalog stores three types of metadata:

  * Technical metadata: Automatically harvested schemas, table names, and system properties.

  * Business metadata: User-defined context such as business descriptions, glossary terms, and ownership.

  * Runtime metadata: Information about data lineage, data quality scores, and data profiling statistics.




## Data insights billing

Explore frequently asked questions about token-based billing, usage metering, and administrative controls for the data insights feature in Knowledge Catalog.

**Note:** To process token billing and manage usage quotas, you must enable the Gemini Data Analytics API (`geminidataanalytics.googleapis.com`) on your Google Cloud project. If this API isn't enabled, data insights fail to execute.  
You can enable the API through the Google Cloud console when prompted, or by using the following gcloud CLI command:  
` gcloud services enable geminidataanalytics.googleapis.com `

### When will I start being billed for using data insights?

Active billing for data insights starts on October 27, 2026.

**Note:** To prevent month-end processing, the billing rollout for data insights begins on November 2, 2026, and takes up to a week to be enabled in all regions.

### How is data insights usage billed?

Usage is measured in data tokens. Data tokens represent the basic units of text and metadata processed by the Gemini model. These tokens are divided into two categories:

  * **Input tokens:** The context, instructions, and history sent to the model.
  * **Output tokens:** The generated natural language descriptions, relationships, and queries returned by the model.



For more information, see [Data Cloud Agent pricing](https://cloud.google.com/products/data-agents/pricing).

### Do service accounts receive a free quota for data insights?

No. Service accounts don't receive a free per-user quota allowance. However, their usage is metered in the same way as standard users.

### How can I prevent automatic charging for data insights?

To avoid incurring charges, verify your ongoing scans and stop triggering new scans. Administrators can also turn off the data insights capability by disabling the Dataplex API in the respective project.

### How can I find out how much I am going to be charged for data insights?

Google Cloud provides metering for data tokens. This metering lets administrators and agent owners monitor their token consumption. This metering capability is available before active billing starts in October 2026.

## Billing and cost monitoring

Explore frequently asked questions about monitoring and attributing compute costs in Knowledge Catalog.

### How do I monitor and attribute Knowledge Catalog DCU costs for Data Quality, Data Profiling, and Data Lineage?

Knowledge Catalog DataScan compute (Auto Data Quality and Data Profiling) and Data Lineage Data Compute Units (DCUs) run on serverless compute in Google-managed infrastructure and don't publish time-series metrics under `dataplex.googleapis.com/*` to Cloud Monitoring.

To monitor, alert on, and attribute Knowledge Catalog DCU costs across projects and scans, export your Cloud Billing data to BigQuery and query system labels attached to Knowledge Catalog billing records:

  * For Data Quality and Data Profiling scans, use the `goog-dataplex-datascan-*` labels (such as `goog-dataplex-datascan-id`, `goog-dataplex-datascan-data-source-project`, and `goog-dataplex-datascan-data-source-bigquery-table`).
  * For Data Lineage processing, use the `goog-dataplex-workload-type` label with value `LINEAGE`.



For detailed label definitions and example BigQuery SQL queries, see [Monitor and attribute Knowledge Catalog DCU costs with Cloud Billing export](https://docs.cloud.google.com/knowledge-catalog/docs/monitoring#monitor-dcu-costs-billing-export).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
