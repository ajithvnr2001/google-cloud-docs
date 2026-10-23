---
url: https://docs.cloud.google.com/recommender/docs/error-reporting/notification-recommender/
title: Error Reporting notification recommender and insights \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:57.699861+00:00
---

# Error Reporting notification recommender and insights  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/error-reporting/notification-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Error Reporting notification recommender and insights

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [Error Reporting](https://docs.cloud.google.com/error-reporting/docs) recommender looks for recent crashes in your Google Cloud project and provides recommendations if you have not configured [Error Reporting notifications](https://docs.cloud.google.com/error-reporting/docs/notifications). When you have notifications configured, no recommendations are made.

This document describes how to enable and view your recommendations and insights.

## Before you begin

Before you can view Error Reporting recommendations and insights, you must do the following:

  1. Enable the Recommender API as described in [Enable the API](https://docs.cloud.google.com/recommender/docs/enabling).

  2. Ensure that you have sufficient permission. You must have one of the following roles, which provide the necessary permissions:

Task description | Role  
---|---  
View recommendations/insights | `roles/recommender.errorReportingViewer`  
View and update (dismiss) recommendations/insights | `roles/recommender.errorReportingAdmin`  
Opt out of recommendations/insights in Transparency and Control Center. For more information, see [Opting out](https://docs.cloud.google.com/recommender/docs/opting-out). | `roles/dataprocessing.admin`  
  
These Recommender roles provide the following API permissions:

Role | Included permissions  
---|---  
`roles/recommender.errorReportingViewer` | `recommender.errorReportingInsights.get`  
`recommender.errorReportingInsights.list`  
`recommender.errorReportingRecommendations.get`  
`recommender.errorReportingRecommendations.list`  
`roles/recommender.errorReportingAdmin` | `roles/recommender.errorReportingViewer` permissions, plus  
`recommender.errorReportingInsights.update`  
`recommender.errorReportingRecommendations.update`  
  
For more information about roles and about granting access, see the following:

     * [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
     * [Managing access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



## View recommendations

Recommender displays recommendations in the Google Cloud console. You can also list recommendations by using the Google Cloud CLI or the Recommender API.

###  Google Cloud console 

To view your recommendations, do the following:

  1. Go to the Google Cloud console, or use the following button:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select the **Recommendations** tab.




###  gcloud CLI 

To list your Error Reporting recommendations by using the gcloud CLI, run the following command:
    
    
    gcloud recommender recommendations list \
        --recommender=google.clouderrorreporting.Recommender \
        --project=PROJECT_ID \
        --location=global
    

Replace PROJECT_ID with the identifier for your Google Cloud project.

For more information about this command, including options for the output format, see [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list).

###  Recommender API 

To list your Error Reporting recommendations by using the Recommender API, run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
    "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/recommenders/google.clouderrorreporting.Recommender/recommendations"
    

Replace PROJECT_ID with the identifier for your Google Cloud project.

For more information, see [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api).

## View insights

The Error Reporting recommender generates recommendations based on [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights). You can retrieve these insights by using the Google Cloud CLI or the Recommender API.

###  gcloud CLI 

To list your Error Reporting insights by using the gcloud CLI, run the following command:
    
    
    gcloud recommender insights list \
        --insight-type=google.clouderrorreporting.Insight \
        --project=PROJECT_ID \
        --location=global
    

Replace PROJECT_ID with the identifier for your Google Cloud project.

For more information about this command, including options for the output format, see [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list). 

###  Recommender API 

To list your Error Reporting insights by using the Recommender API, run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
    "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/recommenders/google.clouderrorreporting.Insight/insights"
    

Replace PROJECT_ID with the identifier for your Google Cloud project.

For more information, see [Using the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api).

## Pricing

Error Reporting recommendations and insights are available free of charge. For information about other pricing tiers, see [Recommender pricing](https://docs.cloud.google.com/recommender/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
