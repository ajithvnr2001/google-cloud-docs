---
url: https://docs.cloud.google.com/asset-inventory/docs/quota/
title: Quotas and limits \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:00.913966+00:00
---

# Quotas and limits  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Resources ](https://docs.cloud.google.com/asset-inventory/docs/quota)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

## Free analysis query limit

Policy Analyzer limits the number of queries that you can make if you don't have an [organization-level activation of the Premium or Enterprise tier of Security Command Center](https://cloud.google.com/security-command-center/pricing#organization-level-activations).

Quota | Value  
---|---  
Analysis queries per organization per day1 | 20  
  
1 This quota only applies for organizations that don't have an organization-level activation of the Premium or Enterprise tier of Security Command Center. This limit is shared among all Policy Analyzer tools.

For more details, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions) in the Policy Intelligence documentation.

## Project quota

Cloud Asset Inventory enforces the rate of incoming requests based on the consumer project. The default quotas are as follows:

Quota | Value  
---|---  
`AnalyzeIamPolicy` |  100 per minute per consumer project 1000 per day per consumer project  
`AnalyzeIamPolicyLongrunning` |  100 per minute per consumer project 1000 per day per consumer project  
`BatchGetAssetsHistory` | 100 per minute per consumer project  
`BatchGetEffectiveIamPolicies` | 100 per minute per consumer project  
`ExportAssets` |  60 per minute per consumer project 6000 per day per consumer project  
`ListAssets` | 100 per minute per consumer project  
[ Real-time feed APIs](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds) | 600 per minute per consumer project  
[ Saved Query APIs](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries) | 600 per minute per consumer project  
`SearchAllIamPolicies` | 400 per minute per consumer project  
`SearchAllResources` | 400 per minute per consumer project  
  
You can use the [APIs and services quotas dashboard](https://console.cloud.google.com/apis/api/cloudasset.googleapis.com/quotas?project=_) to view current quotas and usage for your project.

## Resource organization quota

In addition to the per-project quota, Cloud Asset Inventory also enforces rate limits on incoming requests based on resource organization. The limits are as follows:

Quota | Value  
---|---  
`BatchGetAssetsHistory` |  180 per minute per organization 195,000 per day per organization  
`ExportAssets` |  75 per minute per organization 13,000 per day per organization  
`ListAssets` |  800 per minute per organization 650,000 per day per organization  
`QueryAssets` |  20 per minute per organization for requests with a query statement  200 per minute per organization for requests with a job reference  
[ Real-time feed APIs](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds) | 30 per minute per organization  
`SearchAllIamPolicies` | 3,000 per minute per organization  
`SearchAllResources` | 1,500 per minute per organization  
  
## Policy Analyzer expansion limits

The Policy Analyzer limits group expansion in the group memberships and resource expansion in the resource hierarchy to the following values.

Limit | Value  
---|---  
`AnalyzeIamPolicy` group expansion | 1000 per group  
`AnalyzeIamPolicy` resource expansion | 1000 per resource  
`AnalyzeIamPolicyLongrunning` resource expansion | 100000 per resource   
  
## Downstream services

In addition to limits enforced by Cloud Asset Inventory, the number of incoming requests is also capped by the rate and quota of the downstream services that Cloud Asset Inventory depends on.

### BigQuery

  * **Table operations:** BigQuery has a [quota limit](https://docs.cloud.google.com/bigquery/quotas) for table operations, which defines the maximum number of `ExportAssets` API requests to the same BigQuery table that can be performed daily. `ExportAssets` issues 2 table operations per table per request.

  * **Query jobs:** BigQuery has a concurrent [rate limit](https://docs.cloud.google.com/bigquery/quotas#query_jobs) for query job, which defines the maximum number of concurrent `ExportAssets` API requests that can be issued per project.




### Pub/Sub

  * **Publisher throughput:** Pub/Sub has a [publisher throughput limit](https://docs.cloud.google.com/pubsub/quotas#quotas) per region, which affects the combined asset update size [`Real-time feed`](https://docs.cloud.google.com/asset-inventory//docs/monitor-asset-changes) can publish to your topic.

  * **Message size:** Pub/Sub has [message limits](https://docs.cloud.google.com/pubsub/quotas#resource_limits). For [`Real-time feed`](https://docs.cloud.google.com/asset-inventory//docs/monitor-asset-changes), if the payload of your asset update exceeds the limit, your asset update is discarded. 




## Optimize API usage

To help stay within existing quotas, use the following best practices to optimize your API usage:

  * Reduce your query scope to the smallest possible surface.

  * Slow down your request rate, and implement exponential backoff.

  * Batch requests where possible.

  * The [`ListAssets`](https://docs.cloud.google.com/asset-inventory/docs/list-assets) and [`SearchAllResources`](https://docs.cloud.google.com/asset-inventory/docs/search-resources) APIs are synchronous, which means that they return results in pages. This forces your application to make multiple sequential requests to retrieve a large inventory, which can exhaust your quota. Where appropriate, use the following asynchronous methods instead, so that only a single API request is made:

    * [Export to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery)

    * [Export to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery)

    * [Export to Cloud Storage](https://docs.cloud.google.com/asset-inventory/docs/export-cloud-storage)

    * [Create a Pub/Sub feed](https://docs.cloud.google.com/asset-inventory/docs/monitor-asset-changes)




## Request a quota increase

If you have access to the Security Command Center Premium or Enterprise tier at the organization level, you can contact your account representative to request a Cloud Asset Inventory quota increase. Activating Security Command Center Premium or Enterprise only at the project level might not qualify you for additional quota.

Access to the Security Command Center Premium or Enterprise tier also automatically grants an unlimited number of analysis queries per organization per day. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
