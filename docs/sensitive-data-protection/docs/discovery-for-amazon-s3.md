---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-amazon-s3/
title: Sensitive data discovery for Amazon S3 \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:45.363962+00:00
---

# Sensitive data discovery for Amazon S3  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-amazon-s3/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Sensitive data discovery for Amazon S3 Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Sensitive Data Protection discovery for use with Amazon S3. This feature is available only to customers who have [activated Security Command Center at the Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).

Sensitive Data Protection discovery helps you learn about the types of data that you're storing in S3 and the sensitivity levels of your data. When you profile your S3 data, you generate _file store data profiles_ , which provide insights and metadata about your S3 buckets. For each S3 bucket, a file store data profile includes the following information:

  * The types of files that you're storing in the bucket, categorized into [file clusters](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#file_clusters)
  * The sensitivity level of the data in the bucket
  * A summary about each detected file cluster, including the types of sensitive information found



For a full list of insights and metadata in each file store data profile, see [File store data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#file-store-data-profile).

For more information about the discovery service, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## Workflow

The high-level workflow for profiling Amazon S3 data is as follows:

  1. In Security Command Center, [create a connector for Amazon Web Services (AWS)](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws). Make sure that you select the **Grant permissions for Sensitive Data Protection discovery** checkbox and follow the instructions to configure the connector with sensitive data discovery permissions.

If you already have a connector that doesn't have **Grant permissions for Sensitive Data Protection discovery** selected, see [Grant sensitive data discovery permissions to an existing AWS connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws#grant-sdp-permissions-existing-connector).

  2. [Create an inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect#create_a_new_inspection_template) in the `global` region or the region where you plan to store the discovery scan configuration and all generated data profiles.

  3. [Create a discovery scan configuration for Amazon S3](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-amazon-s3).

Sensitive Data Protection profiles your data according to the schedule that you specify.




## Pricing

When you profile Amazon S3 data, AWS charges you for requests that Sensitive Data Protection makes and for data transfers from S3 to the internet.

When the discovery service profiles your data, it scans a sample of the data in your S3 bucket. Discovery uses heuristic methods to determine how much data to sample in each bucket and within specific files. In this process, some data is transferred to Google Cloud and inspected using the [content inspection service](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types#content-methods) of Sensitive Data Protection. In most cases, if there are no intermittent errors, the data transferred and scanned for each bucket does not exceed 30 GB. The data sampled for each bucket can be less than 30 GB.

### Requests from Sensitive Data Protection

Sensitive Data Protection performs the following operations in the process of profiling your S3 buckets:

  * Around 50 `LIST` requests per day per profiled S3 bucket.
  * Around 4 `GET` requests per file for up to 7,000 files in a profiled bucket. Sensitive Data Protection generally makes under 100,000 `GET` calls. Don't rely on this value when optimizing for cost; this value might change in the future.



The price that AWS charges per 1,000 requests differs based on the region of the S3 bucket. For more information, see _Requests & data retrievals_ in the [Amazon S3 pricing documentation](https://aws.amazon.com/s3/pricing/).

### Data transfers from S3 to the internet

When Sensitive Data Protection profiles S3 data, the data is considered to be transferred from S3 to the internet. AWS charges may apply. For more information, see _Data Transfer OUT From Amazon S3 To Internet_ in the [Amazon S3 pricing documentation](https://aws.amazon.com/s3/pricing/).

### Example calculations

Suppose that you want to profile 10 S3 Standard buckets in the US East (N. Virginia) region. You can estimate the Amazon costs that are directly related to the discovery operation as follows.

**Important:** These rates are provided for illustration purposes only. You are responsible for calculating your Amazon costs using the latest rates and pricing policies in the Amazon pricing documentation.

#### Example: Requests and data retrievals

| **Estimated number of requests per bucket** | **Estimated number of requests for 10 buckets** | **Amazon rate** | **Subtotal**  
---|---|---|---|---  
`LIST` | 50 | 500 | $0.005 per 1,000 calls | 0.005  
`GET` | 28,000 | 280,000 | $0.0004 per 1,000 calls | 0.112  
**Total** |  |  |  | **0.117**  
  
#### Example: Data transfer out from Amazon S3 to the internet

**Data sampled  
per bucket** | **Amazon rate** | **Price per bucket**  
---|---|---  
Up to of 30 GB | $0.09 per GB | **Up to $2.70**  
  
## Data residency considerations

Consider the following when you plan to profile data from other cloud providers:

  * The data profiles are stored alongside the discovery scan configuration. In contrast, when you profile Google Cloud data, the profiles are stored in the same region as the data to be profiled.
  * If you store your inspection template in the `global` region, an in-memory copy of that template is read in the region where you store the discovery scan configuration.
  * Your data is not modified. An in-memory copy of your data is read in the region where you store the discovery scan configuration. However, Sensitive Data Protection makes no guarantees about where the data passes through after it reaches the public internet. The data is encrypted with SSL.



## What's next

  * [Profile Amazon S3 data](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-amazon-s3)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
