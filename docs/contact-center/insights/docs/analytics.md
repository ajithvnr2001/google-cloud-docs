---
url: https://docs.cloud.google.com/contact-center/insights/docs/analytics/
title: Explore conversation analytics \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:37.773548+00:00
---

# Explore conversation analytics  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Explore conversation analytics Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A centralized view of conversation and analysis data can help you research and track CX Insights data. The analytics dashboard features charts and graphs that help you visualize your data and identify trends. Begin with a big-picture view of your organization, and drill down into specific metrics and sample conversation transcripts.

You can also use the analytics dashboard to create custom reports and share them with your team.

## Before you begin

To view CX Insights analytics, follow these steps:

  1. Navigate to the [CX Insights console](https://ccai.cloud.google.com/insights).
  2. If prompted, sign in using your Google Account.
  3. Enter your project ID.
  4. From the navigation menu on the left, select **Analytics**.



## View and filter data

After conversations have been ingested and analyzed in CX Insights, data analytics will be displayed in the dashboard.

### Defaults

By default, the last month of data appears, and the latest deployed topic model is selected. As analytics data in the dashboard is refreshed, the last updated date syncs periodically, depending on the preset interval.

### Filtering

  * To filter data in the dashboard view, select a time period.
  * Select a particular topic model in the dashboard to filter topic results by it.



### Sorting

You can sort across all metrics by clicking column headers.

### Metrics

Along with the topic name, the following metrics are displayed, bound by the select time filter.

  * **Volume** : Total number of conversations with the related topic.
  * **Percent (%) of total** : Volume, divided by the total number of conversations across all topics.
  * **Volume trend** : Volume of conversations over a previous period of time, equal to the current.
  * **AHT (min)** : Average handling time in minutes, across conversations. This time is the difference between the timestamps of the first and the last word of the conversation.
  * **Percent (%) silence** : Average silence time percentage in a conversation, across conversations.
  * **Turns** : Average turn count, across conversations. A turn consists of the speaker changing from one party of the conversation to another.
  * **Sentiment** : Average customer sentiment from 0 to 1 in a conversation, across conversations.



### Topic details

To see more about a topic, including related metrics over the selected time period, click a topic row. Sample snippets, which represent random utterances from conversations across the expanded topic appear alongside time series data.

  * Navigate to the selected Topic Model configuration screen by clicking **Manage this topic**.
  * Locate specific conversations that contain the topic selected by clicking **View conversations**. You might notice fewer conversations appear in the Conversation Hub due to the fact that if there are multiple assigned topics, Conversation Hub filters by primary topic while conversations in the analytics view are counted for all assigned topics.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
