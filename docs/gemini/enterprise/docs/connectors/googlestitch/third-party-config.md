---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch/third-party-config/
title: Google Stitch configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:26.091735+00:00
---

# Google Stitch configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Google Stitch configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up and configure a Google Cloud project with the necessary OAuth credentials before creating the Google Stitch data store.

## Create OAuth app and client credentials

To set up OAuth credentials for Google Stitch, a Google Cloud administrator must perform the following steps in the Google Cloud console.

### Enable the Google Stitch API

In the Google Cloud console, enable the Google Stitch API.

  1. Go to the **API Library** page. 

[Go to API Library](https://console.cloud.google.com/apis/library)

  2. In the search box, enter `Google Stitch API` or `Stitch API` and click the result.
  3. Click **Enable**.



### Create an OAuth consent screen

If you don't have an OAuth consent screen configured for your project, follow these steps:

  1. Go to the **OAuth consent screen** page. 

[Go to OAuth consent screen](https://console.cloud.google.com/auth/overview)

  2. Enter the required information, such as the **App name** , **User support email** , and **Developer contact information**.
  3. Under **Scopes** , click **Add or remove scopes** and add the following scope: 
     * `https://www.googleapis.com/auth/aida`
  4. Under **Audience** , select the user type for your app: 
     * **Internal** : If the app is restricted to members of your organization.
     * **External** : If you want to make it available to any Google user. If you select **External** , you must add test users under **Test users**.
  5. Save your changes.



### Create OAuth client credentials

To create a new OAuth client ID and client secret:

  1. Go to the **Credentials** page. 

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create Credentials** and select **OAuth client ID**.
  3. For **Application type** , select **Web application**.
  4. In the **Name** field, enter a name for the credentials.
  5. In the **Authorized redirect URIs** section, click **Add URI** and enter the following URI: `https://vertexaisearch.cloud.google.com/oauth-redirect`
  6. Click **Create**.
  7. In the dialog that appears, copy the **Client ID** and **Client Secret** , and save them securely.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
