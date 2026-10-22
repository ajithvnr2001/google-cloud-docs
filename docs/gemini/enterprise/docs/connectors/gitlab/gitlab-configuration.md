---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab/gitlab-configuration/
title: GitLab configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:32.545020+00:00
---

# GitLab configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab/gitlab-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  GitLab configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party configuration before creating the GitLab data store.

## Set permissions and obtain client ID and client secret

To register a GitLab app and obtain the client ID and client secret, do the following:

  1. Sign in to your GitLab account and navigate to the group for which you want to create an application.

  2. Go to the selected group.

  3. Select **Settings** > **Applications**.

  4. In the **Name** field, enter a name for your application.

  5. In the **Redirect URI** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.

  6. In the **Scopes** section, select the appropriate scope based on your needs:

     * For search-only access, select **read_api**.
     * For search and actions (write) access, select **api**.
  7. Select **Save application**. GitLab provides:

     * The OAuth2 Client ID in the **Application ID** field.
     * The OAuth2 Client Secret, accessible by selecting **Copy** in the **Secret** field.
     * The **Renew secret** function. Use this function to generate and copy a new secret for this application. Renewing a secret prevents the existing application from functioning until the credentials are updated.
  8. Copy the **Application ID** and **Secret** values that are generated, and store them securely for later use.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
