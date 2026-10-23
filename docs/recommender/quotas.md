---
url: https://docs.cloud.google.com/recommender/quotas/
title: Quotas and limits \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:56.707658+00:00
---

# Quotas and limits  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Resources ](https://docs.cloud.google.com/recommender/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

## Charged quota

Recommender API pricing controls how much read and write quota is provided to individual resources. To support different pricing options, the read and write quota is broken down per recommender.

Depending on the [resource](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) from which the call is made, the following quotas apply:

Resource | Charged quota  
---|---  
Project | Resource project's organization  
Organization | Resource organization  
Folder | Resource organization  
Billing Account | Client project's organization  
  
## API request quota types

Calls to the Recommender API are charged according to the following quota types:

Method | Quota type  
---|---  
`ListInsights` | Read  
`GetInsight` | Read  
`MarkInsightAccepted` | Write  
`ListRecommendations` | Read  
`GetRecommendation` | Read  
`MarkRecommendationClaimed` | Write  
`MarkRecommendationSucceeded` | Write  
`MarkRecommendationFailed` | Write  
  
When the Recommender API is called, you are eligible for the following quotas: 

  * Free tier quota if you have not purchased a support package, or have only a basic role-based support.
  * Full quota if you have purchased a support package other than a basic role-based support.

Quota level | Reads per minute | Reads per day | Writes per minute | Writes per day  
---|---|---|---|---  
Free tier quota | 100 per organization | 100 per organization | 100 per organization | 100 per organization  
Full quota | 6,000 per organization | 1,000,000 per organization | 3,000 per organization | 100,000 per organization  
  
When the quota above is exceeded, you get the HTTP status code `429 RESOURCE_EXHAUSTED`.

**Note:** For projects outside an organization, quotas are applied _per project_ and not per organization. 

## Viewing quotas and limits

View the quotas and limits for an organization using the following steps.

### Console

  1. In the Google Cloud console, go to the **IAM** page for your organization.
[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)
  2. To view all quotas, click **Quotas**.
  3. To view the quotas and limits for a service, click **All Quotas**.



### gcloud

To view the quotas and limits for an organization, use the [`services quota list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/quota/list): 
    
    
        gcloud alpha services quota list --consumer=CONSUMER --service=SERVICE
       

Replace the following: 

  * `CONSUMER`: the organization/_< your organization ID>_ in which you want to view the quotas and limits for.
  * `SERVICE`: specify the ID of the service, `recommender.googleapis.com`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
