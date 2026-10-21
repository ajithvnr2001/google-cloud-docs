---
url: https://docs.cloud.google.com/recommender/docs/quickstart-incontext/
title: Quickstart: Find and apply recommendations in context \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:50:39.742310+00:00
---

# Quickstart: Find and apply recommendations in context  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/quickstart-incontext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Find and apply recommendations in context

Learn how to find and apply [recommendations](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations) from recommenders that support viewing and managing recommendations _in context_ (that is, using a service's user interface in the Google Cloud console). For details about recommenders and supported clients, see [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders).

## Before you begin

For this quickstart, you need a Google Cloud project with a virtual machine running on Compute Engine.

  1. Go to the Google Cloud console.

  2. Select your Google Cloud project. If you don't have a Google Cloud project, create a new project.

  3. Ensure you have sufficient Identity and Access Management (IAM) permissions to view the project's recommendations. If you don have sufficient permission, you might not be able to view some recommendations in detail. Refer to the [IAM](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy) guide for more information.


**Note:** If you're starting with a new project, you may not see any recommendations. You might use the concepts taught in this quickstart for other recommendations in the future as well.

## Find VM resource recommendations in context

In this guide, we will use Compute Engine to find recommendations to reduce VM resource costs. Use the next section to find a full list of products with recommendations available in context.

  1. Navigate to the VM Instances dashboard in Compute Engine.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. Find the recommendation column under the Recommendation header in the table.


**Note:** You might not have any recommendations in this table. If you don't see any recommendations, check the [Active Assist](https://docs.cloud.google.com/recommender/docs/reference/recommenders) documentation to see what other products you might have recommendations for or whether the recommender supports another client such as Active Assist or the Recommender API.

## Apply recommendations

This process might look different for some recommendations, which require you to visit product pages and make the changes there. However, the process is largely the same and can be applied to most recommendations.

  1. Click a recommendation in the Recommendation column in the table to open the detail panel.

  2. In the detail panel, click apply.


**Warning:**

Before applying recommendations in the Google Cloud console or using the API, ensure that impacts are assessed by a reviewer within your organization. The reviewer should have the knowledge to assess impacts identified in recommendations, as well as impacts specific to your infrastructure and business. Applying recommendations without proper assessment could result in unexpected changes, such as issues with system performance, poor reliability, or loss of required permissions. If you choose to apply recommendations without human review, ensure that you have set up a rollback process before making any changes.

## Other ways to apply recommendations

You can also use the Active Assist to find a centralized collection of recommendations available to you.

  * [Finding and applying recommendations in the Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist)



You can also batch process recommendations using the Google Cloud CLI or REST API. To learn more, refer to the following guide:

  * [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api)



## What's next

  * [Finding and applying recommendations in the Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist)
  * [Enabling the API](https://docs.cloud.google.com/recommender/docs/enabling)
  * [Using the API](https://docs.cloud.google.com/recommender/docs/using-api)
  * [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
