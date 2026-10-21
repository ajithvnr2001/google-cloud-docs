---
url: https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems/
title: Find recommendations with Active Assist \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:10.287188+00:00
---

# Find recommendations with Active Assist  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Find recommendations with Active Assist

This page shows you how to use Active Assist to find and apply [recommendations](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations) from recommenders that support Active Assist. For details about recommenders and supported clients, see [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders).

## Before you begin

For this quickstart, you need a Google Cloud project.

  1. Go to the Google Cloud console.

  2. Select a Google Cloud project, folder, or organization.

You can only see recommendations at an organization or folder level if you have permissions for that organization or folder, regardless of your permissions for folders or projects within it.

  3. Ensure you have sufficient Identity and Access Management (IAM) permissions to view the project's recommendations. If you don't have sufficient permission, you might not be able to view some recommendations, and Active Assist might appear empty. To see recommendations for all Google Cloud products and services, grant or request the [**Recommender Viewer** Role](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer). Alternatively, you can grant viewer roles for individual recommenders, such as the [**IAM Recommender Viewer** role](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer). See [recommenders](https://docs.cloud.google.com/recommender/docs/recommenders) for links to information about individual recommenders.


**Note:** If you are starting with a new project, you won't see any recommendations.

## Find recommendations

  1. Navigate to Active Assist.

[Go to Active Assist](https://console.cloud.google.com/active-assist)

This page displays an overview of all recommendations categorized by value pillar (Cost, Security, Performance, Reliability, Management, and Sustainability).

**Note:** If you have sufficient permissions and your Active Assist is still empty, you may have no active services that have recommenders that support Active Assist or your services may not have been in use long enough to generate recommendations.
  2. Select the **All recommendations** tab.

This page displays a table of every recommendation that you can filter, sort, and share. You can explore recommendations in detail, see what resources are affected, and what impact applying a recommendation might have.




## Apply and dismiss recommendations

  1. In the Recommendation column, click the recommendation you want to learn more about. A details panel opens that shows the observation that led to the recommendation, as well as relevant data that might help you decide whether to apply or dismiss it.

  2. Apply or dismiss recommendations that you have permission to using the apply or dismiss buttons.

Note that some recommendations might not be directly applicable in the details panel. Follow the instructions listed in the details panel to apply them.


**Warning:**

Before applying recommendations in the Google Cloud console or using the API, ensure that impacts are assessed by a reviewer within your organization. The reviewer should have the knowledge to assess impacts identified in recommendations, as well as impacts specific to your infrastructure and business. Applying recommendations without proper assessment could result in unexpected changes, such as issues with system performance, poor reliability, or loss of required permissions. If you choose to apply recommendations without human review, ensure that you have set up a rollback process before making any changes.

### Restore dismissed recommendations

The [**Applied and dismissed page**](https://console.cloud.google.com/active-assist/applied-dismissed) contains a record of all of the recommendations you have applied or dismissed.

You can only restore a recommendation that has the status Dismissed. To restore a dismissed recommendation, click **RESTORE** in the restore column.

## Recommendations that you can't find

Not every recommendation can be found in Active Assist. You can also [find and apply recommendations in service pages](https://docs.cloud.google.com/recommender/docs/quickstart-incontext) or [using the API](https://docs.cloud.google.com/recommender/docs/using-api). For details about recommenders and supported clients, see [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders).

## What's next

  * [Finding and applying recommendations in context](https://docs.cloud.google.com/recommender/docs/quickstart-incontext)
  * [Enabling the API](https://docs.cloud.google.com/recommender/docs/enabling)
  * [Using the API](https://docs.cloud.google.com/recommender/docs/using-api)
  * [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
