---
url: https://docs.cloud.google.com/logging/docs/region-support/
title: Locations \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:39.882092+00:00
---

# Locations  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/region-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Resources ](https://docs.cloud.google.com/logging/quotas)



Send feedback 

#  Locations Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how regionality applies to Cloud Logging and lists the different geographical locations where you can store your log data.

**Tip:** If you want to automatically apply a particular storage region to the new `_Default` and `_Required` buckets created in your organization, then configure a [default resource location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region).

## Overview

In Logging, [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries#about_log_buckets) are regional resources: the infrastructure that stores, indexes, and searches your logs is located in a specific geographical location. With the exception of log buckets in the `global`, `eu`, or `us` regions, Google Cloud manages the infrastructure so that your applications are available redundantly across the zones within the region of the log bucket.

Your organization might be required to store its logs data in specific regions. The primary factors in selecting the region where your logs are stored include meeting your organization's latency, availability, or compliance requirements. When selecting a region for logs storage, consider the locations of the other Google Cloud products and services that your application uses.

If you have data residency requirements, then don't enable services that can query log data and then store the query result in a `global` location. An example of such a service is [Gemini Cloud Assist](https://docs.cloud.google.com/gemini/docs/discover/certifications#cloud-assist-security).

## Key concepts

The following key concepts apply to data regionality for Logging.

### Log Router locations

The [Log Router](https://docs.cloud.google.com/logging/docs/routing/overview) processes all log entries written to the Cloud Logging API. It checks each log entry against existing rules to determine which log entries to store in Logging buckets and which log entries to route to supported destinations using [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks). To reliably route logs, the Log Router also stores the logs temporarily, which buffers against temporary disruptions on any sink.

The Log Router processes logs in the region in which they are received. The Log Router might send logs to a different region based on a sink's definition or if you've opted to share log data with another Google Cloud service such as the [Security Command Center Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-event-threat-detection). Sinks apply to logs equally and regardless of region. 

### Log bucket locations

[Log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries) are the containers in your Google Cloud project, billing account, folder, and organization that store and organize your logs data.

For each Google Cloud project, billing account, folder, and organization, Logging automatically creates two log buckets: `_Required` and `_Default`, which are in the `global` location. You can't change the location of existing buckets. However, your organization can create a policy that sets a different default location for these buckets. For more information, see [Configure default settings for organizations and folders](https://docs.cloud.google.com/logging/docs/default-settings).

You can also [create user-defined log buckets](https://docs.cloud.google.com/logging/docs/buckets) for any Google Cloud project. When you create a user-defined log bucket, you can specify the location of the log bucket. After you create the log bucket, the location can't be changed, but you can create a new bucket and then direct log entries to the new log bucket by using sinks. To learn how to set the location for your buckets, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).

**Note:** Log buckets in the `global` region or in multi-regions don't offer added resiliency compared to log buckets created in single regions like `us-west1`.

Logging supports querying logs from multiple regions together, in which case queries are processed in the same locations as the buckets being queried and then aggregated in the region the query was received from to return the results.

The region of a log bucket is shown on the **Logs Storage** page and on some dialogs. For example, when you to the Logs Explorer page and use the **Refine scope** selector to list log views, region information is also displayed. For this selector, when the region is `global`, both the region and the current storage location are displayed in a format similar to `GLOBAL (US-WEST4)`.

## Supported regions

The following [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) are supported by Cloud Logging:

#### Global

**Note:** If you want to choose the storage location for your log data or choose where your log data is analyzed with Observability Analytics, then don't create log buckets in the `global` location. Instead, either use a regional log bucket or, if you have data in a BigQuery multi-region and want to colocate your log data, then set the location of your log buckets to the appropriate multi-region location.Region name | Region description  
---|---  
`global` | Logs stored in any data centers in the world. Logs might be moved to different data centers. Unlike [ other global resources in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#global-resources), global log buckets in Cloud Logging don't provide additional redundancy guarantees compared to a regional log bucket.  
  
#### Multi-regions: EU and US

**Note:** If you have data in a [BigQuery multi-region](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) and want to colocate your log data with that other business data then set the location of your log buckets to the appropriate multi-region. Alternatively, to control the storage location for your log data or where your log data is analyzed with Observability Analytics, specify that location when you create the log bucket. Don't use the `global` location.Region name | Region description  
---|---  
`eu` | Logs stored in any data centers within the European Union. Logs might be moved to different data centers. No additional redundancy guarantees.  
`us` | Logs stored in any data centers within the United States. Logs might be moved to different data centers. No additional redundancy guarantees.  
  
#### Africa

Region name | Region description  
---|---  
`africa-south1` | Johannesburg  
  
#### Americas

Region name | Region description  
---|---  
`northamerica-northeast1` | Montréal  
`northamerica-northeast2` | Toronto  
`northamerica-south1` | Mexico  
`southamerica-east1` | São Paulo  
`southamerica-west1` | Santiago  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | North Virginia  
`us-east5` | Columbus  
`us-south1` | Dallas  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
#### Asia Pacific

Region name | Region description  
---|---  
`asia-east1` | Taiwan  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo  
`asia-northeast2` | Osaka  
`asia-northeast3` | Seoul  
`asia-south1` | Mumbai  
`asia-south2` | Delhi  
`asia-southeast1` | Singapore  
`asia-southeast2` | Jakarta  
`asia-southeast3` | Bangkok  
`australia-southeast1` | Sydney  
`australia-southeast2` | Melbourne  
  
#### Europe

Region name | Region description  
---|---  
`europe-central2` | Warsaw  
`europe-north1` | Finland  
`europe-north2` | Stockholm  
`europe-southwest1` | Madrid  
`europe-west1` | Belgium  
`europe-west2` | London  
`europe-west3` | Frankfurt  
`europe-west4` | Netherlands  
`europe-west6` | Zurich  
`europe-west8` | Milan  
`europe-west9` | Paris  
`europe-west10` | Berlin  
`europe-west12` | Turin  
  
#### Middle East

Region name | Region description  
---|---  
`me-central1` | Doha  
`me-central2` | Dammam  
`me-west1` | Tel Aviv  
  
## Limitations

Following are known limitations of data regionality for Cloud Logging:

  * You can't get advisory notifications about sensitive actions when you configure your Admin Activity Logs to be located in a specific region. For more information, see [Overview of Sensitive Actions notifications](https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-overview).


  * You can't use customer-managed encryption keys (CMEK) on a log bucket when the log bucket is in the `global` region. For more information, see [Configure CMEK for log buckets](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).


  * Cloud Monitoring is a [global product](https://docs.cloud.google.com/about/locations#global-products), and its services are available with no dependence on location. [Log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) let you define rules for aggregating logs into time series by processing logs at the Log Router. The storage location of these time series is unspecified.


  * Gemini Cloud Assist can store data in any Google Cloud data center globally. Don't enable the [Gemini Cloud Assist API](https://docs.cloud.google.com/gemini/docs/discover/certifications#cloud-assist-security) for projects that have data residency or [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/cmek) requirements.



## Next steps

  * Learn how to [configure the default location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region) for the `_Default` and `_Required` buckets created in your organization.

  * Learn how to [regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).



  * [View all the Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations#region).

  * [Explore additional location-based concepts](https://docs.cloud.google.com/docs/geography-and-regions), such as zones, that apply to other Google Cloud services.

  * Read the following whitepapers that provide best practices for data governance:

    * [Logs data: A step by step guide for overcoming common compliance challenges](https://services.google.com/fh/files/misc/whitepaper_data_governance_logs_how_to.pdf)

    * [Data governance: Principles for securing and managing logs](https://docs.cloud.google.com/resources/data-governance-logs-best-practices-whitepaper)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
