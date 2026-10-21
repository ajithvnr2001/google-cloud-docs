---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/relativity/third-party-config/
title: Relativity configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:32:29.686070+00:00
---

# Relativity configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/relativity/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Relativity configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party configuration before creating the Relativity data store.

## Set up authentication and permissions

You need to set up authentication and permissions in your Relativity instance.

### Create an OAuth 2.0 app

To connect Gemini Enterprise to Relativity, you must create an OAuth 2.0 application in your Relativity environment to obtain a **Client ID**.

  1. Sign in to your Relativity instance.
  2. Navigate to the **OAuth2 Clients** tab (typically under **Instance Details** or **Setup**).
  3. Click **New OAuth2 Client**.
  4. Enter a name for the client (for example, `Gemini Enterprise Connector`).
  5. Set the **Flow** to **Authorization Code**.
  6. In the **Redirect URL** or **Callback URL** field, enter: `https://vertexaisearch.cloud.google.com/oauth-redirect`
  7. Save the configuration.
  8. Copy the generated **Client ID**.

**Note:** Relativity does not use a Client Secret for this flow as it relies on PKCE.

### Obtain Instance URI

Identify your Relativity instance URL (for example, `https://<tenant>.r1.kcura.com`). Ensure it does not include a trailing slash.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
