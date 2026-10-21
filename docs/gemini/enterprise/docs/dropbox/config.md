---
url: https://docs.cloud.google.com/gemini/enterprise/docs/dropbox/config/
title: Dropbox configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:47:43.685175+00:00
---

# Dropbox configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/dropbox/config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Dropbox configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up authentication and permissions before creating a Dropbox data store for use with Gemini Enterprise.

## Set up authentication and permissions

To connect Dropbox to Gemini Enterprise, you must create an app in the Dropbox DBX Platform.

### Create and configure a Dropbox app

  1. Navigate to the [Dropbox App Console](https://www.dropbox.com/developers/apps).

  2. Click **Create app**. Fill in the following fields:

     1. For **Choose an API** , select **Scoped access**.

     2. For **Choose the type of access you need** , select **Full Dropbox**.

     3. In the **Name your app** field, enter a name for your Dropbox app.

![Enter the details of your Dropbox app](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/create-dropbox-app.png)

     4. Select the **I agree to Dropbox API Terms and Conditions** checkbox.

     5. Click **Create app**.

  3. In the details page for your new app, click the **Settings** tab. Configure the following settings:

     1. For the **Development users** status, click **Enable additional users**. A **Limit raised to 500 users** dialog opens and displays a message that your app can link to up to 500 users.

     2. Click **Okay**.

     3. Copy the **App key** and **App secret**.

     4. For the **OAuth 2** field, add `https://vertexaisearch.cloud.google.com/console/oauth/default_oauth.html` in the **Redirect URIs** field.

     5. Click **Add**.

     6. Enter `https://vertexaisearch.cloud.google.com/oauth-redirect` in the **Redirect URIs** field.

     7. Click **Add**.

        * `https://vertexaisearch.cloud.google.com/console/oauth/default_oauth.html`

        * `https://vertexaisearch.cloud.google.com/oauth-redirect`

![Configure settings for your Dropbox app](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/dropbox-app-settings.png)

  4. Click the **Permissions** tab. In the **Individual Scopes** section, select the following scopes:

     * In the **Account Info** section, select the **account_info.read** checkbox.

     * In the **Files and folders** section, select the **files.metadata.read** checkbox and the **files.content.read** checkbox.

![Select scopes for your Dropbox app](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/dropbox-app-permissions.png)

  5. Click **Submit**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
