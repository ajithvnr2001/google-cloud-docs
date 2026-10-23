---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/quotas/
title: Quotas and system limits \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:17.199381+00:00
---

# Quotas and system limits  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Resources ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/resources)



#  Quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Network Insights.

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

Allocation quotas restrict the amount of a specific resource that Cloud Network Insights lets you use at a given time. When you create a resource, your available quota for that resource decreases. When you delete the resource, the quota is restored.

If you run Connectivity Tests, the [Connectivity Tests quotas](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/resources/quotas) also apply to the tests that you run in Cloud Network Insights

## Rate quotas

Rate quotas restrict the rate at which you can consume a resource. Per-minute rate quotas reset every minute. Per-day rate quotas reset at midnight Pacific Time. The following table lists the rate quotas that apply to Cloud Network Insights and the default value for each quota.

Quota | Value | Notes  
---|---|---  
API requests per minute | [1,250](https://console.cloud.google.com/iam-admin/quotas?service=networkmanagement.googleapis.com&metric=API%20requests%20per%20minute) | This is the quota for all requests to the `networkmanagement.googleapis.com` API.  
  
## System limits

The following table lists the system limits that apply to Cloud Network Insights and the value for each system limit.

System limit | Value  
---|---  
Network Monitoring Providers | 1  
Monitored Paths | 10,000  
Monitoring Points | 1,000  
Network Paths | 10,000  
Web Paths | 10,000  
  
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

To get the metric names for a Google Cloud service by using the gcloud CLI, run the [`gcloud quotas info list` command](https://docs.cloud.google.com/sdk/gcloud/reference/quotas/info/list). To skip lines that don't list metric names, pass the output to a command such as `grep` with `metric:` as the search term, or use the gcloud CLI [`--format`](https://docs.cloud.google.com/sdk/gcloud/reference#--format) flag:
    
    
    gcloud quotas info list --project=PROJECT_ID_OR_NUMBER \
        --service=networkmanagement.googleapis.com --format="value(metric)"
    

Replace `PROJECT_ID_OR_NUMBER` with the project ID or project number.

## Request a quota adjustment

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
