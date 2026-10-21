---
url: https://docs.cloud.google.com/sensitive-data-protection/limits/
title: Quotas and limits \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:02.267793+00:00
---

# Quotas and limits  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection)
  * [ Resources ](https://docs.cloud.google.com/sensitive-data-protection/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains current restrictions and usage limits when using Sensitive Data Protection. For billing information, see the [pricing page](https://docs.cloud.google.com/sensitive-data-protection/pricing).

These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

You can set lower quotas in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Service_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22Sensitive%2520Data%2520Protection%2520%2528DLP%2529_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceTitle_22%257D%255D%22\)\)).

**Note:** Quotas and limits specified in this document are subject to change.

## Rate quotas

This table highlights important quotas for Sensitive Data Protection requests in each project. For other quotas, see the [**Quotas & System Limits** page in the Google Cloud console](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Service_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22Sensitive%2520Data%2520Protection%2520%2528DLP%2529_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceTitle_22%257D%255D%22\)\)).

Quota | Value | Description  
---|---|---  
Number of requests per minute | 10,000 | Total number of requests to all [global and regional endpoints](https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints) for Sensitive Data Protection across all locations  
Number of requests to a regional endpoint per minute per region | 600 | Requests made to the global endpoint (`dlp.googleapis.com`) [where a location is specified](https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints#location-specified)  
Number of requests to a regional endpoint per minute per region | 100 | Requests made to a [regional endpoint](https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints#regional) (`dlp.REGION.rep.googleapis.com`)  
  
## Resource limits

Sensitive Data Protection enforces the following limits on stored resources per project.

Resource | Limit  
---|---  
Maximum number of [templates](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates) | 1000  
Maximum number of [job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers) | 1000  
Maximum number of running jobs | 1000  
Maximum number of [stored infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes) | 30  
Maximum number of [discovery configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-configuration) | 100  
  
## Content inspection and de-identification limits

Sensitive Data Protection enforces the following usage limits for [inspecting](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text) and [de-identifying](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data) content sent directly to the DLP API as text or images:

Type of limit | Usage limit  
---|---  
Maximum number of [regular custom dictionaries](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary) per request | 10  
Maximum size of each [quote](https://docs.cloud.google.com/sensitive-data-protection/docs/quote "Quote Concept Page") (a contextual snippet, returned with findings, of the text that triggered a match) | 4 KB  
Maximum number of table values | 50,000  
Maximum number of transformations per request | 100  
Maximum number of [inspection rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules) per [set](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InspectionRuleSet) | 10  
Maximum number of inspection rule sets per [inspection configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) | 10  
Maximum number of findings per request | 3,000  
Maximum size of each request, except `projects.image.redact` | 0.5 MB  
Maximum size of each `projects.image.redact` request | 4 MB  
  
If you need to inspect files that are larger than these limits, store those files on Cloud Storage and run an [inspection job](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#inspecting-gcs).

## Content policy limits

Sensitive Data Protection enforces the following limits when evaluating [content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy):

Type of limit | Usage limit  
---|---  
Maximum size of a single PDF | 50 MB  
Maximum size of a single Microsoft Word file | 30 MB  
Maximum size of a single Microsoft PowerPoint file | 30 MB  
Maximum size of a single Microsoft Excel file | 30 MB  
Maximum size of a single plain text or image file | 10 MB  
  
In your [content policy configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies#create-content-policy), you can specify the verdict that Sensitive Data Protection assigns to files that are too large.

## Storage inspection limits

Sensitive Data Protection enforces the following usage limits for [inspecting Google Cloud storage repositories](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage):

Type of limit | Usage limit  
---|---  
Maximum total scan size | 2 TB  
Maximum size of each [quote](https://docs.cloud.google.com/sensitive-data-protection/docs/quote "Quote Concept Page") (a contextual snippet, returned with findings, of the text that triggered a match) | 4 KB  
  
## Storage de-identification limits

Sensitive Data Protection enforces the following usage limit when you [de-identify data in storage](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage):

Type of limit | Usage limit  
---|---  
Maximum file size | 60,000 KB  
  
## Data profiling limits

Sensitive Data Protection enforces the following usage limits for [profiling data](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

These limits apply globally for all data configurations at both organization and project levels.

Type of limit | Usage limit  
---|---  
Maximum number of schedules per discovery scan configuration | 100  
Maximum number of filters per schedule | 100  
Subscription capacity used for profiling | See Subscription capacity used for profiling on this page.  
  
### Subscription capacity used for profiling

This value depends on the number of subscription units that you purchased. For example, if you purchased 5 subscription units, you get 50,000 tokens for the whole month. Therefore, you can consume around 1,667 tokens per day (that is, 50,000 tokens divided by 30 days).

To review your subscription capacity usage, go to the **[Subscriptions](https://console.cloud.google.com/security/sensitive-data-protection/landing/billing;source=7)** page and click **Review capacity usage**.

For information about how to calculate how many profiles can be generated by your tokens, see [Data resources profiled per subscription unit](https://docs.cloud.google.com/sensitive-data-protection/pricing#profiles-per-unit).

### BigQuery profiling limits

Type of limit | Usage limit  
---|---  
Maximum number of BigQuery tables | 200,000  
Maximum sum of columns in all BigQuery tables to be profiled | 20,000,000  
  
#### Example: Organization-level limits

Suppose you have an organization that has two folders, and you [create a scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder) for each folder. The total number of tables to be profiled from both of the configurations must not exceed 200,000. The total number of columns in all those tables must not exceed 20,000,000.

#### Example: Project-level limits

If you configure data profiling at the project level, then the total number of tables in that project must not exceed 200,000. The total number of columns in all those tables must not exceed 20,000,000.

### Cloud SQL profiling limits

Type of limit | Usage limit  
---|---  
Maximum number of databases per instance | 1,000  
Maximum number of tables per database | 20,000  
  
## Custom infoType limits

Sensitive Data Protection enforces the following limits for [custom infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes).

Type of limit | Usage limit  
---|---  
Maximum size of word list passed directly in the request message per regular custom dictionary | 128 KB  
Maximum size of word list specified as a file in Cloud Storage per regular custom dictionary | 512 KB  
Maximum number of components (continuous sequences containing only letters, only digits, only non-letter characters, or only non-digit characters) per regular custom dictionary phrase | 40  
Maximum combined size of all [stored custom dictionaries](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes) per request | 5 MB  
Maximum number of built-in and [custom infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) per request | 150  
Maximum number of [detection rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes#api-overview) per custom infoType | 5  
Maximum number of [custom infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) per request | 30  
Maximum number of [regular custom dictionaries](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary) per request | 10  
Maximum length of regular expressions | 1000  
  
## Stored infoType limits

Sensitive Data Protection enforces the following limits for [creating stored infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes).

Type of limit | Usage limit  
---|---  
Maximum size of a single [input file](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes#create_a_phrase_list) stored in Cloud Storage | 200 MB  
Maximum combined size of all input files stored in Cloud Storage | 1 GB  
Maximum number of input files stored in Cloud Storage | 100  
Maximum size of an input column in BigQuery | 1 GB  
Maximum number of input table rows in BigQuery | 5,000,000  
Maximum size of [output files](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes#create_the_dictionary) | 500 MB  
  
## Avro scanning limits

Generally, Avro files have the same limitations for Sensitive Data Protection and BigQuery. If these limits are hit, binary scanning is used as a fallback. The following limits apply to inspect content requests and inspect storage jobs for Avro files:

Type of limit | Usage limit  
---|---  
Maximum size for a single Avro block | 100 MB  
Maximum size for a single Avro file | 1 TB  
Maximum number of columns in an Avro file | 10,000  
Maximum level of nested fields | 15  
  
## Scanning limits for PDFs and Microsoft products

These limits apply when scanning the following types of files:

  * PDF
  * Microsoft Word
  * Microsoft Excel
  * Microsoft Powerpoint



If these limits are hit, binary scanning is used as a fallback.

Type of Limit | Usage Limit  
---|---  
Maximum size of a single PDF in Cloud Storage. Files exceeding this limit are binary scanned. | 150 MB, up to 10,000 pages  
Maximum size of a single Word file in Cloud Storage. Files exceeding this limit are binary scanned. | 30 MB  
Maximum size of a single Excel file in Cloud Storage. Files exceeding this limit are binary scanned. | 30 MB  
Maximum size of a single Powerpoint file in Cloud Storage. Files exceeding this limit are binary scanned. | 30 MB  
  
These limits apply on these file types even if you set a [maximum byte size per file](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file).

## Quota increases

You can edit your quotas up to their maximum values on the [**Quotas & System Limits**](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Service_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22Sensitive%2520Data%2520Protection%2520%2528DLP%2529_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceTitle_22%257D%255D%22\)\)) page for your project. To request an increase in quota, edit your quota with your requested increase and justification and submit your update. You are notified when your request is received. You might be contacted for more information regarding your request. After your request is reviewed, you are notified whether it has been approved or denied.

## Quota dependencies

Depending on which features you are using, you may also need additional quota.

  * **Pub/Sub** : If you are using Pub/Sub, you may need additional [quota](https://docs.cloud.google.com/pubsub/quotas).
  * **BigQuery** : 
    * Streaming API is used for persisting findings for inspect jobs, where [quota values and other restrictions apply](https://docs.cloud.google.com/bigquery/quotas#streaming_inserts).
    * [`google.cloud.bigquery.storage.v1beta1.BigQueryStorage`](https://docs.cloud.google.com/bigquery/docs/reference/storage/rpc/google.cloud.bigquery.storage.v1beta1), which lists the contents of rows in a table, is [subject to quota limits](https://docs.cloud.google.com/bigquery/quotas#storage-limits).



## Learn about service disruptions

Sensitive Data Protection has features that depend on other Google Cloud services. Because of these dependencies, you can expect Sensitive Data Protection to have comparable reliability as those products.

We make a best effort to retry until any recurring errors have subsided, but degraded experiences may occur if those services experience disruptions.

Check the [Google Cloud Status Dashboard](https://status.cloud.google.com/) for all known service disruptions. You can also subscribe to the Google Cloud Status Dashboard updates [JSON feed](https://status.cloud.google.com/incidents.json) or [RSS feed](https://status.cloud.google.com/feed.atom) for push updates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
