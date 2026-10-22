---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/config/
title: Configure OAuth for Google Calendar \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:29.460948+00:00
---

# Configure OAuth for Google Calendar  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure OAuth for Google Calendar Stay organized with collections  Save and categorize content based on your preferences. 

The Google Calendar connector uses a Google-managed OAuth app to access your Google Calendar data. You don't need to enable Google Calendar APIs, create your own OAuth app, add OAuth scopes, or create OAuth client credentials.

Depending on how your organization restricts OAuth app access, a Google Workspace administrator might need to add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the connector. For instructions, see Allowlist the Google-managed OAuth app.

**Note:** Existing Google Calendar data stores that were configured with a customer-managed OAuth app continue to function. New Google Calendar data stores use the Google-managed OAuth app described on this page.

## Allowlist the Google-managed OAuth app

If your Google Workspace organization restricts OAuth app access, a Google Workspace administrator must add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the Google Calendar connector.

To add the OAuth app to the allowlist, follow these steps:

  1. Sign in to the [Google Admin console](https://admin.google.com) as a Google Workspace administrator.

  2. Go to **Security** > **Access and data control** > **API controls**.

  3. Under **App access control** , click **Manage app access**.

  4. Click **Configure new app** > **OAuth App Name Or Client ID**.

  5. In the search field, enter the following Gemini Enterprise OAuth client ID:
         
         502998392228-hpelhql0ouj9ckiu3l39lllsir24b02s.apps.googleusercontent.com

  6. Select the app from the search results and click **Select**.

  7. For the access level, select **Trusted**. For details on other access levels, see [Control which apps access Google Workspace data](https://support.google.com/a/answer/7281227).

  8. Click **Continue** and then **Finish** to save the change.




For more information about OAuth app allowlisting, see [Control which third-party & internal apps access Google Workspace data](https://support.google.com/a/answer/7281227) in the Google Workspace Admin Help.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
