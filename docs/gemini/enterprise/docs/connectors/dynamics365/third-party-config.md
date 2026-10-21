---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365/third-party-config/
title: Dynamics 365 configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:30.879517+00:00
---

# Dynamics 365 configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Dynamics 365 configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up and configure a third-party application before creating the Dynamics 365 data store.

## Register Microsoft Entra app for Dynamics 365 connector

You must set up an Entra application registration to enable secure access to Dynamics 365 before you can create the connector in Gemini Enterprise.

To register Gemini Enterprise as an OAuth 2.0 application in Entra, do the following:

  1. Navigate to [Microsoft Entra admin center](https://entra.microsoft.com).

  2. In the navigation menu, expand **Identity** and select **App registrations**.

  3. On the **App registrations** page, click add**New registration**.

  4. On the **Register an application** page, do the following:

     1. In the **Name** field, enter a name for your app.
     2. In the **Supported account types** section, select **Accounts in this organizational directory only**.
     3. In the **Redirect URI** section, do the following: 
        1. In the platform list, select `Web`.
        2. In the redirect URI field, enter `https://vertexaisearch.cloud.google.com/console/oauth/default_oauth.html`.
     4. Click **Register**. Microsoft Entra creates your app and displays the overview page of your app.
  5. In the app navigation menu, click **Authentication**.

  6. Click add**Add redirect URI**.

  7. In the platform selection pane, do the following:

     1. Select **Web**.
     2. In the **Redirect URI** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.
     3. Click **Configure**.



## Add federated credential

To enable access to your Dynamics 365 instance using federated credentials, do the following:

  1. In the app navigation menu, click **Certificates & secrets**.

  2. Select the **Federated credentials** tab.

  3. Click add**Add credential**.

  4. Select **Other issuer** from the **Federated credential scenario** list.

  5. In the **Issuer** field, enter `https://accounts.google.com`.

  6. In the **Subject identifier** field, enter the value that you get from the Google Cloud console. This value is generated during the [Dynamics 365 datastore creation](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365/set-up-data-store#create-data-store) in the data section.

  7. In the **Name** field, enter a unique label for the federated credential.

  8. Click **Add** to grant access.




## Obtain client credentials

To connect the Dynamics 365 data store, obtain the application's Client ID and your Tenant ID:

### Obtain client ID

  1. In the app navigation menu, select **Overview**.
  2. Copy the **Application (client) ID**.



### Obtain Tenant ID

Your tenant ID can be found in the **Tenant ID** box on the [overview page](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center.

## Configure Microsoft API permissions

To configure the required API permissions for the app, do the following:

  1. Navigate to the app page.

  2. In the app navigation menu, select **API permissions**.

  3. Click add**Add permissions**.

  4. In the **Request API permissions** pane, select **Dynamics CRM**.

  5. Search for and select the following delegated permission:

     * **user_impersonation** (Access Dynamics 365 as organization users)
  6. Click **Add Permissions**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
