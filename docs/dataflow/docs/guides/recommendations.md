---
url: https://docs.cloud.google.com/dataflow/docs/guides/recommendations/
title: Dataflow recommendations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:12.234811+00:00
---

# Dataflow recommendations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow recommendations Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow provides recommendations for improving job performance, reducing cost, and troubleshooting errors. This section explains how to review and interpret the recommendations. Keep in mind that some recommendations might not be relevant to your use case.

## View recommendations

To view recommendations, perform the following steps:

  1. In the Google Cloud console, go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Select a job.

  3. Click the **Recommendations** tab.




The **Recommendations** tab displays insights from Dataflow regarding the pipeline. The goal of these insights is to identify situations in which improvements in cost and performance might be made.

![The Recommendations tab for a Dataflow job with sample recommendations.](https://docs.cloud.google.com/static/dataflow/images/recommendations.png)

The **Update date** column indicates the last time that an insight was observed. Recommendations are stored for 30 days from the **Update date**.

### Programmatic access to recommendations

For programmatic access to recommendations, use the [Recommender API](https://docs.cloud.google.com/recommender/docs/using-api).

## Dismiss a recommendation

You can dismiss a recommendation at the Active Assist for your project.

To dismiss a recommendation, follow these steps:

  1. In the Google Cloud console, open the navigation menu.
  2. Select **Home** , and then **Recommendations**.
  3. On the **Dataflow Diagnostics** card, click **View all**.
  4. Select the recommendation that you want to dismiss, and then click **Dismiss**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
