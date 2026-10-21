---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/best-practices-costs/
title: Keeping costs under control \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:00.599991+00:00
---

# Keeping costs under control  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/best-practices-costs/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Resources ](https://docs.cloud.google.com/sensitive-data-protection/docs/resources)



Send feedback 

#  Keeping costs under control Stay organized with collections  Save and categorize content based on your preferences. 

Sensitive Data Protection has many powerful capabilities, but depending on the quantity of information that you instruct Sensitive Data Protection to scan, it is possible for costs to become prohibitively high. This topic describes several methods that you can use to keep costs down while also ensuring that you're using Sensitive Data Protection to scan the exact data that you intend to.

## Inspection

Google recommends the following practices to help you control your inspection costs.

### Use sampling to restrict the number of bytes inspected

If you are scanning BigQuery tables or Cloud Storage buckets, Sensitive Data Protection can scan a small subset of the dataset. This can provide a sampling of scan results without incurring the potential costs of scanning an entire dataset.

Once you find a sample with sensitive data, you can schedule a second, more exhaustive scan of that dataset to discover the entire list of findings.

For more information, see [Limiting the amount of content inspected](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#sampling) in [Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage).

### Scan only data that has changed

You can instruct Sensitive Data Protection to avoid scanning data that hasn't been modified since the last inspection. Setting a [timespan](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#timespanconfig) lets you control what data to scan based on when the data was last modified.

If you're using [job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers), you can set the flag `enable_auto_population_of_timespan_config` in `TimespanConfig` to automatically skip content that was scanned during the last scheduled job.

For more information, see [Limit scans to only new content](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#limit_scans_to_only_new_content) in [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers).

### Limit scans of files in Cloud Storage to only relevant files

By specifying the [`CloudStorageRegexFileSet`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#cloudstorageregexfileset) message, you can use regular expression filters for finer control over which files or folders in buckets to include or exclude.

This is useful in situations where you want to skip scanning files that you know have no sensitive data, such as backups, TMP files, static Web content, and so on.

## Discovery

We recommend the following practices to help you control your [data profiling](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) costs.

### Run an estimation

Before you start a data profiling operation, consider running an estimation first. Running an estimation lets you understand the size and shape of the BigQuery data to be profiled. Each estimate provides the approximate table count, data size, and profiling cost. It also shows a projection of the monthly growth of your BigQuery data.

For more information on running an estimation, see the following:

  * [Estimate data profiling cost for an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/estimate-org-folder)
  * [Estimate data profiling cost for a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/estimate-project)



### Add schedules in your scan configurations

To help control the cost of data profiling, consider [creating a schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder#manage-schedules) where you set filters and conditions. The following are examples of things you can do:

  * If you don't need to profile certain tables, you can specify that tables that match your filters must never be profiled.
  * If you want to profile only certain tables, you can turn off profiling for all tables, except for those that match your filter.
  * If you want certain tables to be profiled only once and never again, you can specify that those tables must never be reprofiled.
  * If you don't need to profile old tables, you can set a condition to profile only the tables that were created after a certain date.
  * If you don't need to profile tables that are new, you can set a condition to profile tables only when they reach a certain age or a minimum row count.



## View costs using a dashboard and query your audit logs

Create a dashboard to view your billing data so you can make adjustments to your Sensitive Data Protection usage. Also consider streaming your audit logs to Sensitive Data Protection so you can analyze usage patterns.

You can [export your billing data](https://support.google.com/cloud/answer/7233314) to BigQuery and visualize it in a tool such as Data Studio. For a tutorial on creating a billing dashboard, see [Visualize Google Cloud Billing using BigQuery and Data Studio](https://medium.com/google-cloud/visualize-gcp-billing-using-bigquery-and-data-studio-d3e695f90c08).

You can also stream your [audit logs](https://docs.cloud.google.com/sensitive-data-protection/docs/audit-logging) to BigQuery and analyze the logs for usage patterns such as query costs by user.

## Set budget alerts

[Set a budget alert](https://docs.cloud.google.com/billing/docs/how-to/budgets) to track how your spend is growing toward a particular amount. Setting a budget does not cap API usage; it only alerts you when your spend amount gets near the specified amount.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
