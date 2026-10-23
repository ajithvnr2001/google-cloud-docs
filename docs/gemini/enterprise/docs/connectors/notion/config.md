---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/config/
title: Notion configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:29.555313+00:00
---

# Notion configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Notion configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up authentication and permissions before creating a Notion data store for use with Gemini Enterprise.

## Set up authentication and permissions

To connect Notion to Gemini Enterprise, you must create a Notion OAuth integration. Notion integrations can be either _public_ or _internal_. To connect Gemini Enterprise, you must create a public integration.

**Note:** A public Notion integration isn't visible or accessible outside your organization unless you submit it for publishing. You don't need to publish your integration in order to connect Notion to Gemini Enterprise.

### Create a Notion integration

  1. Navigate to the [Notion Integrations dashboard](https://www.notion.so/profile/integrations).

  2. Click **New integration**. Fill in the following fields:

     1. For **Associated workspace** , select your Notion workspace.

     2. In the **Type** list, select **Public**.

  3. Fill in required organizational fields such as **Company name** , **Website** , and **Privacy policy**.

  4. In the **OAuth domain & URIs** section, enter the OAuth redirect URIs for Gemini Enterprise:

     1. In the **Redirect URIs** field, enter `https://vertexaisearch.cloud.google.com/console/oauth/default_oauth.html`, and press `Enter`.

     2. Again, in the **Redirect URIs** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`, and press `Enter`.

  5. Click **Save**.




### Configure permissions and get credentials

  1. In the settings page for your new integration, under **Configuration** , copy the **OAuth Client ID** and **OAuth Client Secret** values.

  2. In the **Capabilities** section, under **Content Requests** , select the **Read content** capability.

  3. Click **Save changes**.




You can now create a data store to connect Notion to Gemini Enterprise. For more information, see [Set up a Notion data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/data-store).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
