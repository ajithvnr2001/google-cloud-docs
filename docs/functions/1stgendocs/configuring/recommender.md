---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/recommender/
title: Minimize Cold Starts with Recommender \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:38.912099+00:00
---

# Minimize Cold Starts with Recommender  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/recommender/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Minimize Cold Starts with Recommender

Recommender is a service that automatically provides recommendations and insights for using resources on Google Cloud, based on heuristic methods, machine learning, and current resource usage. Each recommendation includes a link you can click to put the recommendation into effect for your function.

This topic shows how to use [Recommender](https://docs.cloud.google.com/recommender) to minimize cold starts:

  * Detect functions that could benefit from setting up the minimum instances (in other words, functions that are likely to be negatively affected by cold start issues).
  * Inform users about the opportunity to eliminate cold start issues.
  * Let users set up the minimum instances directly from the recommendation system.



## Recommendation availability after deployment

Recommender automatically provides recommendations for a function as soon as a week after it has been deployed. After this period of time, recommendations for the function are displayed with the function on the function list page in the [Cloud Run functions Overview page](https://console.cloud.google.com/functions/list) in the Google Cloud console and in the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

## Alternate ways of using recommendations

In addition to the use of recommendations covered on this page inside the Cloud Run functions UI, recommendations are also available through the following:

  * [Recommender API](https://docs.cloud.google.com/recommender/docs/using-api)
  * [BigQuery export](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq)
  * [Recommender Logs](https://docs.cloud.google.com/recommender/docs/viewing-logs)



## Viewing and accepting recommendations for Cloud Run functions

To view and accept a recommendation in the Cloud Run functions user interface:

  1. [Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list)

  2. Look for functions in the list that have a **Performance** light bulb icon in the **Recommendation** column.

  3. Click **Performance** to view details for the recommendation:

     * An overview of why this recommendation is being suggested.
     * The recommendation itself.
  4. If you decide to apply the recommendation, set the number of minimum instances and click **Apply**.

This redeploys the function with the new minimum instance value. After this, the recommendation will no longer be displayed next to the function.




## Dismissing a recommendation

Click **Dismiss** if you want to dismiss the recommendation without applying it. This prevents the recommendation for that function from appearing again for 30 days.

## Viewing recommendations in Active Assist

You can also view recommendations in the Active Assist. For more information refer to the Active Assist [Getting started](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) documentation. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
