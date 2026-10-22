---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-connector/
title: Develop your first email connector \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:20.307027+00:00
---

# Develop your first email connector  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop your first email connector

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

_Connectors_ are the entry point for alerts into Google SecOps. Their job is to translate raw input data from multiple sources into Google SecOps format. The connectors get alerts (or equivalent data, such as alarms or correlation events) from third-party tools sent to the data processing layer and send them for ingestion as Google SecOps alerts and events. 

This document explains how to develop an email connector in the Integrated Development Environment (IDE). The process involves:

  * Ingesting raw data from an email source (Gmail).
  * Translating that data into Google Security Operations format.
  * Creating cases within the platform from the translated data.



The connector scans each email message body to extract URLs. You can then use the product integrated in [Develop your first action](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action) to check if these URLs are malicious. 

## Before you begin

Before the connector can connect to your email inbox, complete the following steps:

  1. For testing purposes, create a new Gmail account or use an existing one. 
  2. Enable two-step verification to grant Google SecOps secure access to the email inbox. 
  3. Create an App Password that grants the Google SecOps platform permission to access your account. You can only use App Passwords with accounts that have two-step verification enabled. 
  4. In your Google Account, click **App Passwords** and then fill in the required fields: 
     * In **Select app** , select **Other (Custom name)**.
     * Add the URL associated with your Google SecOps platform (DNS).
  5. Create the email connector in the IDE. For details, see [Develop the connector](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/developing-the-connector). 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
