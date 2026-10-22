---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/set-up-data-store/
title: Set up a Microsoft Teams data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:20.763048+00:00
---

# Set up a Microsoft Teams data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Microsoft Teams data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Microsoft Teams to Gemini Enterprise.

## Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

Before you set up your Microsoft Teams data store, ensure the following:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. Register Gemini Enterprise as an [OAuth 2.0 application in Microsoft Entra ID](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#entra-app-registration) and [obtain the following credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#obtain-client-id-and-client-secret):

     * Client ID

     * Client secret

     * Tenant ID

  3. Configure the [Microsoft Graph application permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#microsoft-graph-minimum-permissions) with the consent of a Microsoft Teams administrator.

  4. Add the following URL as web callback URL:

     * https://vertexaisearch.cloud.google.com/oauth-redirect



### Create the Microsoft Teams data store

To create the Microsoft Teams data store, perform the following steps:

  1. In the Google Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add **Create data store**.

  5. In the **Source** , search for **Microsoft Teams** , and click **Select**.

  6. In the **Data** section: 

     1. In the connection mode section, choose **Federated search**.
     2. In the **Authentication settings** section, configure authentication:

        1. Provide the following authentication details:

           * **Client ID:** The unique identifier of the application registered in Microsoft Entra ID.
           * **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID.
           * **Tenant ID:** The unique identifier for your Microsoft 365 or Azure environment.

For information on how to obtain the client ID, client secret, and tenant ID, see [Obtain client ID and client secret](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#obtain-client-id-and-client-secret) and [Obtain tenant ID](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#obtain-tenant-id). For the permissions required to perform search and actions, see [Required permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams#set-up-permissions).

        2. Click **Login** and complete the Microsoft sign-in.

        3. Click **Continue**.

     3. In the **Advanced options** section:

        1. **Azure Tenant** : Enter the tenant ID. This is a required field and must match the **Tenant ID** provided in the **Authentication settings** section.
        2. **Include All Groups** : Optional: Enable this checkbox to list all the groups in your organizations or only groups the logged in user is a member of.
        3. **Include All Users** : Optional: Enable this checkbox to list all the users in your organizations or only the logged in users.
        4. Click **Continue**.
     4. In the **Entities to search** section, select all the entities to search from the list. You must select at least one entity.

  7. Click **Continue**.

  8. In the **Actions** section, for **Select Microsoft Teams actions to enable** , choose the actions from the category to enable them for the data store.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

  9. Click **Continue**.

  10. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

  11. In the **Configuration** section: 

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Your data connector name** field, enter a name for your connector.
     3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
        * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  12. Click **Continue**.

  13. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Microsoft Teams connector is ready to be used.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the Microsoft Teams data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to Microsoft Teams before executing any queries.

For information on permissions required to perform search, see [Configure the Microsoft Graph permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#microsoft-graph-minimum-permissions).

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Microsoft Teams and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Microsoft API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Microsoft API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Microsoft Teams. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Microsoft API.

## What's next

  * To provide a user interface for querying your data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Microsoft Teams data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
