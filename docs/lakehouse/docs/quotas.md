---
url: https://docs.cloud.google.com/lakehouse/docs/quotas/
title: Quotas and system limits for borderless Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:41.452874+00:00
---

# Quotas and system limits for borderless Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/quotas/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



Send feedback 

#  Quotas and system limits for borderless Lakehouse Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Lakehouse.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Lakehouse resources. System limits can't be changed. 

## Get quota and system limit metric names

Quotas and system limits have two types of names: display names and metric names. Display names have spaces and capitalization that make them easier for humans to read. Metric names are more likely to be lowercase and delimited by underscores instead of spaces; the exact format depends on the service.

The following instructions show how to get metric names for quotas and system limits by using either the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Identity and Access Management (IAM) & Admin > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

The table on this page displays quotas and system limits that have usage or have adjusted values, and a reference entry for other quotas. The reference entry has the word "default" in parentheses at the end of the listing in the **Name** column. For example, `SetIAM Policy requests per minute per region (default)` is the reference entry for the quota `SetIamPolicyRequestsPerMinutePerProject`.

  2. If you don't see the **Metric** column, take the following steps.

     1. Click view_column **Column display options**.
     2. Select **Metric**.
     3. Click **OK**. The **Metric** column appears in the table.

The **Metric** column shows the metric names. To filter the results, enter a property name or value in the field next to filter_list **Filter**.




###  gcloud 

To get the metric names for a service by using the gcloud CLI, run the `quotas info list` command. To skip lines that don't list metric names, pass the output to a command such as `grep` with `metric:` as the search term, or use the gcloud CLI [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format):
    
    
    gcloud quotas info list --project=PROJECT_ID_OR_NUMBER \
        --service=SERVICE_NAME --format="value(metric)"
    

Replace the following:

  * `PROJECT_ID_OR_NUMBER`: the project ID or project number.
  * `SERVICE_NAME`: the name of the service whose quota metrics you want to see—for example, the service name for Compute Engine is `compute.googleapis.com`. Include the `googleapis.com` portion of the service name.



## Request a quota increase

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

## Quotas

The following quotas apply to Lakehouse:

### Lakehouse runtime catalog

The following limits apply to Lakehouse runtime catalog:

Limit | Default | Notes  
---|---|---  
Table modifications per day  |  1,500 modifications  |  Your project can make up to 1,500 table modifications per table per day. A [load job](https://docs.cloud.google.com/bigquery/quotas#load_jobs), [copy job](https://docs.cloud.google.com/bigquery/quotas#copy_jobs), or [ query job](https://docs.cloud.google.com/bigquery/quotas#query_jobs) that appends or overwrites table data counts as one modification to the table. This limit cannot be changed. DML statements are excluded and _don't_ count toward the number of table modifications per day. Streaming data is excluded and _doesn't_ count toward the number of table modifications per day.  
Maximum rate of table metadata update operations per table  |  5 operations per 10 seconds  |  Your project can make up to five table metadata update operations per 10 seconds per table. This limit applies to all table metadata update operations, performed by the following: 

  * Google Cloud console
  * The bq command-line tool
  * BigQuery client libraries
  * The following API methods: 
    * [`tables.insert`](https://docs.cloud.google.com/bigquery/docs/reference/v2/tables/insert)
    * [`tables.patch`](https://docs.cloud.google.com/bigquery/docs/reference/v2/tables/patch)
    * [`tables.update`](https://docs.cloud.google.com/bigquery/docs/reference/v2/tables/update)
  * [DDL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language) statements on tables 

This limit also includes the combined total of all load jobs, copy jobs, and query jobs that append to or overwrite a destination table or that use a [DML](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax) `DELETE`, `INSERT`, `MERGE`, `TRUNCATE TABLE`, or `UPDATE` statements to write data to a table. Note that while DML statements count toward this limit, they are not subject to it if it is reached. DML operations have [dedicated rate limits](https://docs.cloud.google.com/bigquery/quotas#data-manipulation-language-statements).  If you exceed this limit, you get an error message like `Exceeded rate limits: too many table update operations for this table`. This error is transient; you can retry with an exponential backoff.  To identify the operations that count toward this limit, you can [ Inspect your logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#bigqueryauditmetadata_format). Refer to [Troubleshoot quota errors](https://docs.cloud.google.com/bigquery/docs/troubleshoot-quotas#ts-maximum-update-table-metadata-limit) for guidance on diagnosing and resolving this error.   
Maximum number of columns per table | 10,000 columns | Each table, query result, or view definition can have up to 10,000 columns. This includes nested and repeated columns.  
  
### Cross-cloud data access

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, email [biglake-help@google.com](mailto:biglake-help@google.com).Quota | Value  
---|---  
Maximum total number of namespaces in a federated catalog | 100 namespaces  
Maximum number of tables per namespace in a federated catalog | 300 tables per namespace  
Maximum total number of tables in a federated catalog | 10,000 tables  
Maximum number of namespace filters in a federated catalog | 16 namespace filters  
  
## System limits

The following table lists the system limits that apply to _Lakehouse_ and the value for each system limit:

System limit | Value  
---|---  
Maximum number of Apache Iceberg tables managed by _Lakehouse_ per Cloud Storage bucket that a discovery scan supports | 1,000 tables per bucket  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
