---
url: https://docs.cloud.google.com/recommender/docs/change-risk-recommendations/
title: Change risk recommendations \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:17.423286+00:00
---

# Change risk recommendations  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/change-risk-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change risk recommendations

**Preview — Change risk recommendations**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Change risk recommendations help you reduce the risk of cloud infrastructure misconfigurations by intelligently flagging common risky changes to your most important resources and providing recommendations to prevent and mitigate issues.

## Introduction

Misconfigurations are a common cause of cloud incidents. They can happen due to human errors or unexpected workload changes, and can lead to a variety of problems, including performance issues, reliability issues, and even outages. Many misconfigurations can go unnoticed initially, making them difficult to track down and resolve.

**Change risk recommendations** is a new family of Active Assist recommendations and insights within the [Recommender](https://cloud.google.com/recommender/docs/recommenders) service. Change risk recommendations automatically flag risky changes to cloud resources identified as _important_ based on their usage and other signals, to help prevent, detect, and mitigate issues (for example, service outages) caused by misconfigurations of those important cloud resources. For example, if you try to delete a highly used project, or modify an IAM policy that could be an essential dependency based on its recent usage activity, **change risk recommendations** can help prevent unintended issues by proactively warning you about the risks associated with a given change.

## Change risk recommendations scope

The change risk recommendations are currently only supported for the resources and actions listed in the table below.

Resource | Action | Surfaces | Criteria used to determine resource importance  
---|---|---|---  
**Project** | Deletion | 

  * Google Cloud console
  * gcloud CLI
  * Recommender API

| 

  * Project usage (API calls, networking traffic, and Google Cloud services usage)
  * Billing
  * Usage within the last 30 days

  
**Service account** | Deletion | 

  * Google Cloud console
  * gcloud CLI
  * Recommender API

| 

  * Number of authentications
  * Usage within the last 90 days

  
**IAM policy** | Change | 

  * Google Cloud console
  * gcloud CLI
  * Recommender API

| 

  * Number of exercised permissions
  * Usage within the last 90 days
  * Belong to an important project

  
**Caution:** Change risk recommendations won't recognize resources as important if they had sudden changes in their activity within less than 24 hours.

## Before you begin

Before you begin using this feature, you must first set up the service:

  1. [Enable the Recommender API](https://cloud.google.com/recommender/docs/enabling) on a single billing project. You can then use this same billing project to retrieve recommendations and insights for other projects, the entire organization or the billing account, using the billing-project functionality of gcloud/API.
  2. Grant permissions on the user or service account that you will be used for accessing this feature.



## Permissions

To view the recommendations for Change risk recommendations, you must have the specific permissions for the specific resource.

  * Project

    * `recommender.resourcemanagerProjectChangeRiskRecommendations.get`
    * `recommender.resourcemanagerProjectChangeRiskRecommendations.list`
    * `recommender.resourcemanagerProjectChangeRiskInsights.get`
    * `recommender.resourcemanagerProjectChangeRiskInsights.list`
  * Service Account

    * `recommender.iamServiceAccountChangeRiskRecommendations.get`
    * `recommender.iamServiceAccountChangeRiskRecommendations.list`
    * `recommender.iamServiceAccountChangeRiskInsights.get`
    * `recommender.iamServiceAccountChangeRiskInsights.list`
  * IAM Policy

    * `recommender.iamPolicyChangeRiskRecommendations.get`
    * `recommender.iamPolicyChangeRiskRecommendations.list`
    * `recommender.iamPolicyChangeRiskInsights.get`
    * `recommender.iamPolicyChangeRiskInsights.list`



You can also grant [roles/recommender.viewer](https://cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer) role to cover these permissions.

## Understanding the response for change risk recommenders/insights

The following table provides a description of the presented fields in the recommendation and insight object:

### Recommendation

Field name | Type | Description  
---|---|---  
` associatedInsights ` |  ` string ` |  Insight that is associated with this recommendation. ` projects/[project_number]/locations/global/ insightTypes/google.resourcemanager.project. ChangeRiskInsight/insights/[fingerprint] `  
` asset ` |  ` object ` |  Contains the asset name and asset type of the associated resource.   
` etag ` |  ` string ` |  Fingerprint of the RecommenderConfig. Provides optimistic locking when updating.   
` updateTime ` |  ` string ` |  Timestamp of the last time when the recommendation was updated. A timestamp in RFC 3339 UTC **Zulu** format, accurate to nanoseconds. Example: `2022-01-10T22:47:38.421626Z`.   
  
### Insight

Field name | Type | Description  
---|---|---  
` associatedRecommendations ` |  ` string ` |  Recommendation that is associated with this recommendation. ` projects/[project_number]/locations/global/ recommenders/google.resourcemanager.project. ChangeRiskRecommender/recommendations/ [recommendation_id] `  
` constraint ` |  ` object ` |  Contains the change risk recommendations constraint that the user is advised against doing. ` This project should not be deleted. `  
` importance ` |  ` object ` |  Contains the list of reasons why we determined this resource is important. For example, high usage.   
` risk ` |  ` object ` |  Contains risk assessment details. For example,resource usage activity values are used to determine importance.   
` updateTime ` |  ` string ` |  Timestamp of the last time when the recommendation was updated. A timestamp in RFC 3339 UTC **Zulu** format, accurate to nanoseconds. Example: `2022-01-10T22:47:38.421626Z`.   
  
## Viewing the change risk recommendations

In addition to the usage model discussed above, you can use the standard approach for Recommender service to view the change risk recommendations and insights for a Project, Service account or an IAM Policy:

  * Google Cloud console
  * API
  * gcloud



### Google Cloud console

You can view change risk recommendations and insights on the product pages themselves. The recommendations will automatically be active as long as you have the permissions listed above.

Active Assist warns you of the dangers of deleting an important resource, and indicates what to do when that warning appears in the following situations:

  * [Deleting a project](https://console.cloud.google.com/cloud-resource-manager)
  * [Deleting a service account](https://console.cloud.google.com/iam-admin/serviceaccounts)
  * [Deleting a policy binding](https://console.cloud.google.com/iam-admin/iam)



### gcloud and API

The following sections present the commands to request change risk recommendations and insights trough `gcloud` and the API for a Project, Service account or an IAM Policy.

#### Project

Insights and recommendations can be accessed through the Google Cloud console, `gcloud`, or the Recommender API for all customers.

###  gcloud 

To view recommendations and insights using `gcloud`, follow the steps below. For more information, see [Using the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api) and [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api).

##### Recommendations:

To list recommendations for the project where you've enabled the Recommender API, run the following command:
    
    
    gcloud recommender recommendations list
    --recommender=google.resourcemanager.project.ChangeRiskRecommender
    --project=PROJECT_ID  --location=global --format=yaml
    

Replace the following:

  * `PROJECT_ID `: The project ID.



##### Insights:

A similar set of commands may be used to list insights:
    
    
    gcloud recommender insights list
    --insight-type=google.resourcemanager.project.ChangeRiskInsight
    --project=PROJECT_ID  --location=global --format=yaml
    

Replace the following:

  * `PROJECT_ID `: The project ID.



###  API 

To view recommendations and insights, you can use `curl` to send a request to the recommender APIs.

##### Recommendations

To list recommendations for the project where you've enabled the Recommender API, run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "x-goog-user-project: BILLING_PROJECT_ID " "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/
    recommenders/google.resourcemanager.project.ChangeRiskRecommender/recommendations"
    

Replace the following:

  * `BILLING_PROJECT_ID `: The billing project ID.



##### Insights:

A similar set of commands may be used to list insights:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "x-goog-user-project: BILLING_PROJECT_ID " "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/insightTypes/google.resourcemanager.project.ChangeRiskInsight/insights"
    

Replace the following: * `BILLING_PROJECT_ID `: The billing project ID.

#### Service account

Insights and recommendations about a Service Account can be accessed through the Google Cloud console, `gcloud`, or the Recommender API for all customers.

###  gcloud 

To view recommendations and insights using `gcloud`, follow the steps below. For more information, see [Using the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api) and [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api).

##### Recommendations:

To list recommendations for a Service Account where you've enabled the Recommender API, run the following command:
    
    
    gcloud recommender recommendations list
    --recommender=google.iam.serviceAccount.ChangeRiskRecommender
    --project=PROJECT_ID  --location=global --format=yaml
    

Replace the following:

  * `PROJECT_ID `: The project ID.



##### Insights:

A similar set of commands may be used to list insights:
    
    
    gcloud recommender insights list
    --insight-type=google.iam.serviceAccount.ChangeRiskInsight
    --project=PROJECT_ID  --location=global --format=yaml
    

Replace the following: * `PROJECT_ID `: The project ID.

###  API 

To view recommendations and insights, you can use `curl` to send a request to the recommender APIs.

##### Recommendations:

To list recommendations for a Service Account where you've enabled the Recommender API, run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "x-goog-user-project: BILLING_PROJECT_ID " "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/
    recommenders/google.iam.serviceAccount.ChangeRiskRecommender/recommendations"
    

Replace the following:

  * `PROJECT_ID `: The project ID.
  * `BILLING_PROJECT_ID `: The billing project ID.



##### Insights:

A similar set of commands may be used to list insights:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "x-goog-user-project: BILLING_PROJECT_ID " "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/insightTypes/google.iam.serviceAccount.ChangeRiskInsight/insights"
    

Replace the following: * `PROJECT_ID `: The project ID. * `BILLING_PROJECT_ID `: The billing project ID.

#### IAM Policy

Insights and recommendations about an IAM Policy can be accessed through the Google Cloud console, `gcloud`, or the Recommender API for all customers.

###  gcloud 

To view recommendations and insights using `gcloud`, follow the steps below. For more information, see [Using the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api) and [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api).

##### Recommendations:

To list recommendations for an IAM Policy where you've enabled the Recommender API, run the following command:
    
    
    gcloud recommender recommendations list --recommender=google.iam.policy.ChangeRiskRecommender --project=PROJECT_ID  --location=global --format=yaml
    

Replace the following:

  * `PROJECT_ID `: The project ID.



##### Insights:

A similar set of commands may be used to list insights:
    
    
    gcloud recommender insights list --insight-type=google.iam.policy.ChangeRiskInsight --project=PROJECT_ID  --location=global --format=yaml
    

Replace the following: * `PROJECT_ID `: The project ID.

###  API 

To view recommendations and insights, you can use `curl` to send a request to the recommender APIs.

##### Recommendations:

To list recommendations for an IAM Policy where you've enabled the Recommender API, run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/\recommenders/google.iam.policy.ChangeRiskRecommender/recommendations"
    

Replace the following:

  * `PROJECT_ID `: The project ID.



##### Insights:

A similar set of commands may be used to list insights:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "x-goog-user-project: BILLING_PROJECT_ID " "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/insightTypes/google.iam.policy.ChangeRiskInsight/insights"
    

Replace the following: * `PROJECT_ID `: The project ID. * `BILLING_PROJECT_ID `: The billing project ID.

## Feedback and support

Email [active-assist-feedback@google.com](https://docs.cloud.google.com/recommender/docs/active-assist-feedback@google.com) in case of technical issues, questions or feedback.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
