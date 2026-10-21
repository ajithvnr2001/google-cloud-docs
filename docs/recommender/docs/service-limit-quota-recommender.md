---
url: https://docs.cloud.google.com/recommender/docs/service-limit-quota-recommender/
title: Service limit (quota) recommender \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:15.165219+00:00
---

# Service limit (quota) recommender  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/service-limit-quota-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service limit (quota) recommender

The service limit recommender analyzes usage of service quotas by projects in your organization and provides recommendations that help you identify resources that may be getting close to their quota limits.

## Overview

[Quotas](https://docs.cloud.google.com/docs/quotas/overview) are in place to help you manage resources and protect you from unforeseen spikes in usage, but they can be complicated to track and manage. Service limit recommender analyzes your quota utilization and provides you with the following features to help you catch potential bottlenecks before they become an issue:

  * Recommendations to review quotas with high utilization
  * Usage insights for each quota with high utilization



Proactively monitoring and taking action on quota recommendations can help reduce the risk of [running out of quota](https://docs.cloud.google.com/docs/quotas/overview#manage_quota_values). In addition to recommendations that are updated once per day, you can [set up quota alerts and monitoring](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts) for any quotas that may require real-time monitoring.

## How it works

The service limit recommender analyzes usage over [rate, allocation, and concurrent quotas](https://docs.cloud.google.com/docs/quotas/overview#types_of_quota) over the last 30 days. If at any point during those 30 days your utilization has hit 80% of your current limit, a recommendation will be generated.

**Note:** The service limit recommender generates insights and recommendations for all quotas except the following: 

  * Quotas that are specified on dimensions other than project, location, or time (e.g. "per organization", "per folder", "per user", "per resource", or "per VPC" quotas)
  * [Google Search Indexing](https://developers.google.com/search/apis/indexing-api/v3/quota-pricing) and [YouTube](https://developers.google.com/youtube/v3/determine_quota_cost) quotas
  * The IAM quota `ServiceAccountsPerProject`, in cases where a project is newly created or has not been used extensively



## Pricing

Please refer to [recommender pricing](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view the insights and recommendations, you must do the following:

  * You must [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling). You only need to enable the API on a single project. You can then use this same project to examine recommendations and insights for other projects by using the [\--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project) functionality of gcloud/API.
  * Make sure that you have one of these required roles assigned:

Description | Roles  
---|---  
View recommendations |  `recommender.serviceLimitViewer`  
  
View and update recommendations |  `recommender.serviceLimitAdmin`  
  
  
These roles provide a set of [permissions](https://docs.cloud.google.com/recommender/docs/service-limit-quota-recommender#required_iam_permissions) that enable you to access the insights and recommendations. For more information about roles, refer to [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You may also opt out of all service limit insights and recommendations in Transparency and Control Center. In order to change opt-out settings you must have the `dataprocessing.admin` IAM role. For more information about opting out, refer to [opting out of insights and recommendations](https://docs.cloud.google.com/recommender/docs/opting-out).

### Recommender ID

Here are the service limit (quota) recommender ID and insight type:

  * `google.resourcemanager.serviceLimit.Recommender`
  * `google.resourcemanager.serviceLimit.Insight`



### Required IAM permissions

To access the list of service limit recommendations and insights, the following permissions are required:

  * `recommender.resourcemanagerServiceLimitRecommendations.get`
  * `recommender.resourcemanagerServiceLimitRecommendations.list`
  * `recommender.resourcemanagerServiceLimitInsights.get`
  * `recommender.resourcemanagerServiceLimitInsights.list`



To update recommendations and insights (for example, to dismiss a recommendation), the following permissions are required:

  * `recommender.resourcemanagerServiceLimitRecommendations.update`
  * `recommender.resourcemanagerServiceLimitInsights.update`



## Viewing service limit (quota) recommendations

Insights and recommendations can be accessed through the Cloud Console, `gcloud`, or the Recommender API for all customers.

Exporting recommendations via BigQuery is also available for customers with a Standard, Enhanced, or Premium support package.

###  Console 

  1. Go to **Active Assist**.

[Go to Active Assist](https://console.cloud.google.com/active-assist)

  2. In the **Review and manage quota utilization** card, click **View all**.

**Note:** You must have the have the correct IAM permissions (listed above) in order to see recommendations. If you have the correct permissions and the page does not show any recommendations then the project does not have any quota utilization meeting the criteria for a recommendation.



###  gcloud 

To view recommendations and insights using `gcloud`, follow the steps below. For more information, see [Using the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api) and [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api).

#### Recommendations

  1. To list recommendations for the project where you've enabled the Recommender API, run the following command:
         
         gcloud recommender recommendations list \
           --project=PROJECT_ID \
           --location=LOCATION \
           --recommender=google.resourcemanager.serviceLimit.Recommender
         

Replace the following:

     * `PROJECT_ID`: The project ID.
     * `LOCATION`: The Cloud region or zone. If a quota type is not defined on a regional or zonal basis then it will fall under the "global" location.
**Note:** If the command does not return any recommendations then the project does not have any quota utilization meeting the criteria for a recommendation.
  2. To list recommendations in a different project while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         gcloud recommender recommendations list \
           --billing-project=BILLING_PROJECT_ID \
           --project=PROJECT_ID \
           --location=LOCATION \
           --recommender=google.resourcemanager.serviceLimit.Recommender
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `PROJECT_ID`: The ID of a different project for which you'd like to view the recommendations.
     * `LOCATION`: The Cloud region or zone. If a quota type is not defined on a regional or zonal basis then it will fall under the "global" location.

**Note:** You can expand the details of the Recommendations from the list command by appending a --format=yaml flag towards the end.

#### Insights

A similar set of commands may be used to list insights. Simply make two modifications to each of the above commands:

  * Instead of running `gcloud recommender recommendations list` run `gcloud recommender insights list`.
  * Instead of passing `--recommender=google.resourcemanager.serviceLimit.Recommender` pass `--insight-type=google.resourcemanager.serviceLimit.Insight`



For example, to list insights for a given project run the following command:
    
    
        gcloud recommender insights list   
    
        --project=PROJECT_ID   
    
        --location=LOCATION   
    
        --insight-type=google.resourcemanager.serviceLimit.Insight
      

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The Cloud region or zone. If a quota type is not defined on a regional or zonal basis then it will fall under the "global" location.



###  API 

To view recommendations and insights, you can use `curl` to send a request to the recommender APIs. To authorize requests from the command line, you use OAuth access tokens. An OAuth access token is a string that grants temporary access to an API.

**Note:** If you aren't already familiar with the authentication prerequisites for calling Google Cloud APIs, see the [Authentication overview](https://docs.cloud.google.com/docs/authentication#service-account-keys).

#### Recommendations

  1. To list recommendations for the project where you've enabled the Recommender API, run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/\
         recommenders/google.resourcemanager.serviceLimit.Recommender/recommendations"
         

Replace the following:

     * `PROJECT_ID`: The project ID.
     * `LOCATION`: The Cloud region or zone. If a quota type is not defined on a regional or zonal basis then it will fall under the "global" location.
**Note:** If the API call does not return any recommendations then the project does not have any quota utilization meeting the criteria for a recommendation.
  2. To list recommendations in a different project while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
         -H "x-goog-user-project: BILLING_PROJECT_ID" \
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/\
         recommenders/google.resourcemanager.serviceLimit.Recommender/recommendations"
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `PROJECT_ID`: The ID of a different project for which you'd like to view the recommendations.
     * `LOCATION`: The Cloud region or zone. If a quota type is not defined on a regional or zonal basis then it will fall under the "global" location.



#### Insights

A similar set of commands may be used to list insights. Simply replace `recommenders/google.resourcemanager.serviceLimit.Recommender/recommendations` with `insightTypes/google.resourcemanager.serviceLimit.Insight/insights` in the url.

For example, to list insights for a given project run the following command:
    
    
      curl   
    
     -H "Authorization: Bearer $(gcloud auth print-access-token)"   
    
     "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/  
    
     insightTypes/google.resourcemanager.serviceLimit.Insight/insights"
      

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The Cloud region or zone. If a quota type is not defined on a regional or zonal basis then it will fall under the "global" location.



###  BigQuery export 

Recommendations and insights can also be exported in bulk to a BigQuery table. For details please refer to the [BigQuery export documentation](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
