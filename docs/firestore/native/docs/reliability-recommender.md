---
url: https://docs.cloud.google.com/firestore/native/docs/reliability-recommender/
title: Reliability recommender \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:50.715694+00:00
---

# Reliability recommender  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/reliability-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reliability recommender

The Reliability recommender supports the following recommendation subtypes: 

  * [Enable scheduled backups](https://docs.cloud.google.com/firestore/docs/backups)
  * [Enable PITR](https://docs.cloud.google.com/firestore/docs/pitr)



which are a part of [Disaster Recovery Plan](https://docs.cloud.google.com/firestore/docs/disaster-recovery) to protect your data against data disasters such as accidental deletion or modification of data.

This document describes how to enable and view your recommendations and insights to improve the reliability of your databases.

## Before you begin

Before you can view Firestore reliability recommendations and insights, do the following:

  1. Enable the Recommender API as described in [Enable the API](https://docs.cloud.google.com/recommender/docs/enabling).

  2. Ensure that you have sufficient permissions. You must have one of the following roles, which provide the necessary permissions:

Task description | Role  
---|---  
View recommendations/insights | `roles/recommender.firestoredatabasereliabilityViewer`  
View and update (dismiss) recommendations/insights | `roles/recommender.firestoredatabasereliabilityAdmin`  
Opt out of recommendations/insights in Transparency and Control Center. For more information, see [Opting out](https://docs.cloud.google.com/recommender/docs/opting-out). | `roles/dataprocessing.admin`  
  
These Recommender roles provide the following API permissions:

Role | Included permissions  
---|---  
`roles/recommender.firestoredatabasereliabilityViewer` | `recommender.firestoreDatabaseReliabilityRecommendations.get`  
`recommender.firestoreDatabaseReliabilityRecommendations.list`  
`recommender.firestoreDatabaseReliabilityInsights.get`  
`recommender.firestoreDatabaseReliabilityInsights.list`  
`roles/recommender.firestoredatabasereliabilityAdmin` | `roles/recommender.firestoredatabasereliabilityViewer` permissions, plus  
`recommender.firestoreDatabaseReliabilityRecommendations.update`  
`recommender.firestoreDatabaseReliabilityInsights.update`  
  
For more information about roles and about granting access, see the following:

     * [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
     * [Managing access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



## View recommendations

You can list Reliability recommendations in different ways.

You can view reliability recommendations only if you have non-empty, in-use databases that don't have scheduled backups or PITR enabled. 

###  Google Cloud console 

You can view your recommendations by doing following:

  1. Go to the Google Cloud console, or use the following button:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select the **Recommendations** tab.




###  gcloud CLI 

To list reliability recommendations by using `gcloud`, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
      gcloud recommender recommendations list \
      --project=PROJECT_ID \
      --location=LOCATION \
      --recommender=google.firestore.database.<var>RECOMMENDER</var>
    

Replace the following:

  * `PROJECT_ID`: Your project ID
  * `LOCATION`: A region, such as `us-central1`
  * `RECOMMENDER`: The ID of the recommender as `ReliabilityRecommender`.



###  Recommender API 

To list your reliability recommendations by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
      -H "x-goog-user-project: PROJECT_ID" \
      "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.firestore.database.RECOMMENDER/recommendations"
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `RECOMMENDER`: The ID of the recommender as `ReliabilityRecommender`.



For more information, see [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api). 

## View insights

You can view insights and detailed recommendations about disaster recovery plan in different ways.

###  Console 

To view insights and detailed recommendations by using the Google Cloud console, click the recommendation button in the list of databases.

###  gcloud CLI 

To view insights by using `gcloud`, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
      gcloud recommender insights list \
      --project=PROJECT_ID \
      --location=LOCATION \
      --insight-type=google.firestore.database.INSIGHT_TYPE
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type as `ReliabilityInsight`. 



###  Recommender API 

To list your insights by using the Recommender API, run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
    
    "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.firestore.database.INSIGHT_TYPE/insights"
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type as `ReliabilityInsight`.



For more information, see [Using the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api).

## Apply recommendations

For more information about how to improve your disaster recovery plan, see [Plan disaster recovery](https://docs.cloud.google.com/firestore/native/docs/disaster-recovery).

## Pricing

Reliability recommendations and insights are available free of charge. For information about other pricing tiers, see [Recommender pricing](https://docs.cloud.google.com/recommender/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
