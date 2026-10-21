---
url: https://docs.cloud.google.com/recaptcha/docs/monitor-keys/
title: Monitor reCAPTCHA keys \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:32.131551+00:00
---

# Monitor reCAPTCHA keys  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/monitor-keys/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Monitor reCAPTCHA keys Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to monitor reCAPTCHA key details for your web pages or mobile applications to gain insights into score trends and CAPTCHA challenge outcomes.

## Before you begin

To get the permissions that you need to monitor reCAPTCHA keys, ask your administrator to grant you the following IAM roles on your project: 

  * To view settings: reCAPTCHA Enterprise Viewer (`roles/recaptchaenterprise.viewer`). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Monitor reCAPTCHA keys

  1. In the Google Cloud console, go to the **reCAPTCHA** page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha)

  2. Select the **Keys** tab.

  3. In the **reCAPTCHA keys** section, find your key and click the key.

  4. In the **Key details** page, click the **Bots** tab.

  5. Set the required action in the filter.

Multiple charts appear for the action value that you set.

  6. To view score trends, set a threshold in **Risky definition** , and go to the **Score overview** chart.

The **Score overview** and action charts display request volume, score distribution across your traffic, and top actions so that you can identify abusive traffic patterns and tune your score thresholds for each action.

  7. To view challenge outcomes, go to the **Challenges** chart.

For keys that use CAPTCHA challenges, the **Challenges** chart shows the breakdown of requests that passed without a visual challenge (no CAPTCHA), requests where users passed or failed a challenge, and overall traffic trends.




## What's next

  * [Learn how to manage reCAPTCHA keys](https://docs.cloud.google.com/recaptcha/docs/manage-keys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
