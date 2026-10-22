---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/quotas/
title: Quotas and limits \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:13.860292+00:00
---

# Quotas and limits  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about quotas and limits for AI Commerce Search.

**Important:** These quotas only apply to recommendations within AI Commerce Search.

## Default quotas

By default, your project has the following quotas for AI Commerce Search.

To increase or otherwise edit these quotas, see Edit your quotas.

Quota | Value  
---|---  
User event writes per minute | 60,000  
User event imports per minute | 100  
User event writes per user per minute | 240  
User event reads per minute | 300  
Product writes per minute | 12,000  
Product imports per minute | 100  
Product reads per minute | 300  
Predictions per minute | 60,000  
Predictions per minute for a specific user | 60,000  
Searches per minute | 300  
Completion read per minute | 1200  
Total user events | 40,000,000,000  
Total products (search not enabled) | 40,000,000  
Total products (search enabled) | 4,000,000  
Total tags   
(sum of per-product tag counts, not unique tags) | 100,000,000  
Pending Cloud Storage import long running operations | 300  
Pending BigQuery import long running operations | 100  
Pending Merchant Center import long running operations | 10  
Concurrent active models | 10  
Total models (active and paused) | 20  
Total placements | 100  
Total Controls | 100  
  
## Check your quotas

To check the current quotas for AI Commerce Search resources in your project, go to the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console and select **AI Commerce Search API** in the **Services** drop-down list.

You can see recent quota usage by going to the [API Dashboard](https://console.cloud.google.com/apis/api), selecting **AI Commerce Search API** , and opening the **Quotas** tab.

## Edit your quotas

As your use of Google Cloud expands over time, you might want to increase your quotas accordingly. Or you might need to limit certain quotas. If you expect a notable upcoming increase in usage, make your request to increase your quotas a few days in advance to ensure that your quotas are adequately sized.

**Note:** To request additional quotas, your user account must have the `serviceusage.quotas.update` permission. This permission is included by default for the following [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles): Owner, Editor, and Quota Administrator.

  1. In the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, select **AI Commerce Search API** in the **Services** drop-down list.

  2. Select the quotas you want to change.

  3. Click **Edit quotas**.

  4. Fill out your name, email, and phone number and click **Next**.

  5. Fill in your quota request and click **Submit request**.




You will receive a response from the AI Commerce Search team within 48 hours of your request.

## Limits

The following limits are enforced:

  * You can start up to five model operations per minute. Limited model operations include creation, deletion, pause, and resume. 

  * Your site can have up to 250,000 user event writes per visitor ID or user ID per week.

  * Your site can have up to 10,000 product writes per product ID per week and one product write per product ID per second. Too frequent updates on the same product are unexpected, and the additional updates might be rejected with a `RESOURCE_EXHAUSTED` error.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
