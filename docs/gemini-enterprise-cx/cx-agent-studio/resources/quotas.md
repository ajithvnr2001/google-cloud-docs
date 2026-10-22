---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/resources/quotas/
title: Quotas and system limits \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:08.996137+00:00
---

# Quotas and system limits  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/resources/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Customer Experience Agent Studio.

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

## Multi-region quota mapping

When using CX Agent Studio in a multi-region configuration, your quota is enforced and tracked against a designated single region. This is important to understand when checking your usage or requesting quota increases.

The multi-region identifiers map to the following single regions for quota purposes:

  * **`us`** (US multi-region) maps to **`us-central1`**
  * **`eu`** (EU multi-region) maps to **`europe-west4`**



To monitor your quota consumption for a multi-region deployment, look for the metric names under the mapped single region (for example, check `us-central1` if your app is deployed to the `us` multi-region).

## Allocation quotas

The following quotas don't reset over time. The quotas are released when you release the resource:

Quota | Value  
---|---  
Apps per project per region | 1000  
  
## Rate quotas

The following quotas specify the rate at which you use or create a resource.

Quota | Value  
---|---  
App mutation operations per minute per project per region | 200  
App read operations per minute per project per region | 600  
App generative operations per minute per project per region | 100  
`RunSession` LLM tokens per minute per project per `base_model` per region | 120000  
`Evaluation` `RunSession` LLM tokens per minute per project per `base_model` per region | 120000  
`ExecuteTool` requests per minute per project per region | 240  
`RetrieveTools` requests per minute per project per region | 120  
`RetrieveToolSchema`requests per minute per project per region | 120  
  
## Concurrent quotas

Quota | Value  
---|---  
Concurrent `BidiRunSession` Operations per 30 minutes per `base_model` per project per region | 15  
Concurrent `RunEvaluation` Operations per 10 minutes per project per region | 10  
  
## System limits

CX Agent Studio enforces the following system limits:

System limit | Value  
---|---  
Maximum number of agents per app | 100  
Maximum number of tools per app | 200  
Maximum number of tools per agent | 100  
Maximum number of toolsets per app | 100  
Maximum number of guardrails per app | 100  
Maximum number of examples per app | 1000  
Maximum number of variables per app | 100  
Maximum number of workflows per app | 100  
Maximum number of evaluations per app | 1000  
Maximum number of evaluation datasets per app | 100  
Maximum number of callbacks per agent | 50  
Maximum number of app versions per app | 200  
  
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

**Note:** To request a quota increase for a multi-region deployment, you must submit the request against the mapped single region (e.g., request the increase in `us-central1` if your app is deployed in the `us` multi-region).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
