---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store/
title: Set up a Salesforce data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:08.997326+00:00
---

# Set up a Salesforce data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Salesforce data store Stay organized with collections  Save and categorize content based on your preferences. 

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). **Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to create a data store and connect Salesforce to Gemini Enterprise.

## Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

Before you set up your connection, do the following:

  * Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

    2. Locate the user account and click edit **Edit**.
    3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  * Set up your Salesforce account and [obtain authentication credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration#obtain-authentication-credentials).




## Create Salesforce federated data store

To create a Salesforce data store, perform the following steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add **Create data store**.

  5. In the **Source** section, search for **Salesforce** , and click **Select**.

  6. In the **Data** section:

     1. In the **Authentication settings** section, configure authentication based on your chosen connection mode. For more information about obtaining authentication credentials, see [Salesforce configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration).

        * **Instance URL** : The base URL of your Salesforce instance.
        * **Client ID** : The OAuth client ID for your application.
        * **Client Secret** : The OAuth client secret for your application.
        * Click **Login** and complete the Salesforce sign-in.
     2. Click **Continue**.

     3. In the **Advanced options** section, if you want to use the Salesforce sandbox instance, select the **Use Sandbox** checkbox.

     4. Click **Continue**.

     5. In the **Entities to search** section, select at least one entity.

**Note:** You must select at least one entity to create the Salesforce data store. However, the Salesforce data store will search across all entities in your Salesforce app regardless of your selection.
  7. Click **Continue**.

  8. If you selected **Federated search** , navigate to **Actions** and select the required actions to enable for the data store from the **Select Salesforce actions to enable** list.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To view and manage the list of actions, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

     1. Click **Continue**.
  9. In the **Configuration** section: 

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Your data connector name** field, enter a name for your connector.
     3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
        * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  10. Click **Continue**.

  11. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 

  12. Click **Continue**.

  13. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data stores** page.




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Salesforce connector is ready to be used.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) the application to access Salesforce before executing any queries.

For more information, see What's next.

## Create Salesforce data ingestion data store

If you want to create a data ingestion data store, follow these steps. Otherwise, you can skip this section.

To use the console to sync data from Salesforce to Gemini Enterprise, follow these steps:

  1. In the console, go to the **Gemini Enterprise** page. 

[Go to Console](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data Stores**.
  3. Click add **Create Data Store**.
  4. On the **Select a data source** page, scroll or search for **Salesforce V2** to connect your third-party source.
  5. In the **Authentications** section, select the authentication method and enter the authentication information. For more information about obtaining authentication credentials, see [Configure Salesforce for data ingestion data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration#expandable-1).
  6. In the **Destinations** section, select **Public** or **Private**. 
     1. For the **Public** destination type, you are not required to create the setup for service attachment. In the **Login URL** field, enter your login URL to the Salesforce server.
     2. For the **Private** destination type, enter all the required information: 
        1. **Service attachment** : Enter your service attachment.
        2. **Base domain name** : Enter your base domain.
        3. **Login URL** : Enter your login URL to the Salesforce server.
  7. Click **Continue**.
  8. In the **Entities to sync** section, do the following: 
     1. Select the entities you want to sync. 
        * Optional: **URL field name** : Enter a column name to override the default entity URL with a custom URL from the Salesforce table.
     2. Optional: To add custom entities, click **Add entities manually**. The custom entity name must be in the following format **< var>custom_object_name</var>__c**. 
     3. Select the **Sync frequency** for **Full sync** and the **Incremental sync frequency** for **Incremental data sync**. For more information, see [Sync schedules](https://docs.cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#sync-schedules). 
  9. Click **Continue**.
  10. In the **Configure your data connector** section, do the following: 
     1. Select a region for your data store.
     2. Enter a name for your data store.
     3. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 
  11. To check the status of your ingestion, go to the **Data Stores** page and click your data store name. The **Connector state** changes from **Creating** to **Running** when it starts synchronizing data.



For more information, see What's next.

## What's next

  * To provide a user interface for querying your Salesforce data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To view and manage the list of actions, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
