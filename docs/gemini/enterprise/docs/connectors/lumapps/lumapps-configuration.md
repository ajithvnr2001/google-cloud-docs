---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lumapps/lumapps-configuration/
title: LumApps configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:01.529994+00:00
---

# LumApps configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lumapps/lumapps-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  LumApps configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party application before creating the LumApps data store.

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

## Prerequisites

Before configuring the OAuth application or creating a data store, you must request feature activation from LumApps.

Contact LumApps Support at `support@lumapps.com` and request the activation of the MCP feature flag on your LumApps platform. If the MCP feature flag is not activated, connection attempts fail with the following error:
    
    
    MCP Server is not activated for your organization. Please contact your administrator.
    

## Create OAuth app

To generate credentials for the OAuth client, perform the following steps:

  1. Sign in to your LumApps back-office platform.

  2. Go to **Provider Settings** > **LumApps applications**.

  3. Create a new application using **Authorization code** as the application type.

![Create a new LumApps application](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/lumapps-images/create-lumapps-app.png)

  4. When prompted for scopes, select `all.admin` to allow read and write access.

  5. In the **Redirect URL** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.

![Configure scopes and redirect URL for LumApps app](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/lumapps-images/lumapps-app-settings.png)

  6. Click **Save**.

  7. Copy the generated **Client ID** and **Client secret** and store them securely for later use.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
