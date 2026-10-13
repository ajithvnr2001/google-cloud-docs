---
url: https://docs.cloud.google.com/saas-runtime/docs/quotas/
title: Quotas and system limits \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:19.075144+00:00
---

# Quotas and system limits  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/quotas/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Resources ](https://docs.cloud.google.com/app-lifecycle-manager/resources)



Send feedback 

#  Quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document lists the quotas and system limits that apply to App Lifecycle Manager.

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

## Allocation quotas

Allocation quotas restrict the amount of a specific resource that App Lifecycle Manager lets you use at a given time. When you create a resource, your available quota for that resource decreases. When you delete the resource, the quota is restored.

The following table lists the allocation quotas that apply to App Lifecycle Manager and the default value for each quota.

Quota | Value  
---|---  
`UnitKindsUsedPerProjectPerRegion` (`regional-unitkinds-used-by-project`) | 10  
`UnitsUsedPerProjectPerRegion` (`regional-units-used-by-project`) | 5000  
  
## Rate quotas

Rate quotas restrict the rate at which you can consume a resource. Per-minute rate quotas reset every minute. Per-day rate quotas reset at midnight Pacific Time. The following table lists the rate quotas that apply to App Lifecycle Manager and the default value for each quota.

Quota | Value  
---|---  
Unit APIs: `api-unit-read-requests` | 1000 QPS  
Unit APIs: `api-unit-write-requests` | 200 QPS  
Unit APIs: `regional-api-unit-read-requests` | 1000 QPS  
Unit APIs: `regional-api-unit-write-requests` | 200 QPS  
UnitOperation APIs: `api-unitops-read-requests` | 1000 QPS  
UnitOperation APIs: `api-unitops-write-requests` | 200 QPS  
UnitOperation APIs: `regional-api-unitops-read-requests` | 1000 QPS  
UnitOperation APIs: `regional-api-unitops-write-requests` | 200 QPS  
Other APIs: `api-read-requests` | 200 QPS  
Other APIs: `api-write-requests` | 10 QPS  
Other APIs: `regional-api-read-requests` | 200 QPS  
Other APIs: `regional-api-write-requests` | 10 QPS  
  
## Concurrent quota

Concurrent quotas tracks the number of items going in parallel. App Lifecycle Manager enforces the following concurrent quota limits:

Concurrent limit | Value  
---|---  
Unit operations per project, per region | 1500  
  
## Get quota and system limit metric names

Quotas and system limits have two types of names: display names and metric names. Display names have spaces and capitalization that make them easier for humans to read. Metric names are more likely to be lowercase and delimited by underscores instead of spaces; the exact format depends on the service.

The following instructions show how to get metric names for quotas and system limits by using either the Google Cloud console or the gcloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **IAM & Admin > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

The table on this page displays quotas and system limits that have usage or have adjusted values, and a reference entry for other quotas. The reference entry has the word "default" in parentheses at the end of the listing in the **Name** column. For example, `SetIAMPolicy requests per minute per region (default)` is the reference entry for the quota `SetIamPolicyRequestsPerMinutePerProject`.

  2. If you don't see the **Metric** column, take the following steps.

     1. Click view_column **Column display options**.
     2. Select **Metric**.
     3. Click **OK**. The **Metric** column appears in the table.



The **Metric** column shows the metric names. To filter the results, enter a property name or value in the field next to filter_list **Filter**.

###  gcloud 

To get the metric names for a Google Cloud service by using the gcloud CLI, run the `quotas info list` command. To skip lines that don't list metric names, pass the output to a command such as `grep` with `metric:` as the search term, or use the gcloud CLI [`--format`](https://docs.cloud.google.com/sdk/gcloud/reference#--format) flag:
    
    
    gcloud beta quotas info list --project=PROJECT_ID_OR_NUMBER \
        --service=SERVICE_NAME --format="value(metric)"
    

Replace the following:

  * `PROJECT_ID_OR_NUMBER`: the project ID or project number.
  * `SERVICE_NAME`: the name of the service whose quota metrics you want to see—for example, the service name for Compute Engine is `compute.googleapis.com`. Include the `googleapis.com` portion of the service name.



## Request a quota adjustment

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
