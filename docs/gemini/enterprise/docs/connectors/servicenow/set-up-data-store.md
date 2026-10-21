---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/set-up-data-store/
title: Set up a ServiceNow data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:30:34.563081+00:00
---

# Set up a ServiceNow data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a ServiceNow data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect ServiceNow to Gemini Enterprise. 

## Before you begin

Before setting up your ServiceNow connection, ensure you have the following in place:

  * Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

    2. Locate the user account and click edit **Edit**.
    3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  * [ServiceNow OAuth registration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-cred): Register Gemini Enterprise as an OAuth 2.0 application in ServiceNow with **Broadly scoped** scope restriction.

  * [Set up ServiceNow account](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config#create-account) and [obtain authentication credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-cred).

  * [Set up administrator role](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config#admin-roles) and use administrator account to [set the required user roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/servicenow/third-party-config#user-roles-permissions).

  * [Set up a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) with an administrator account capable of managing organization-level configurations, ensuring the organization can set up a workforce pool. Make sure your organization is set up to manage a workforce pool.

  * To enable keyword search capabilities, ensure that "table indexing" is enabled on your ServiceNow instance. For information, see [Configure table for indexing and searching](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/search-administration/task/configure-single-table-for-indexing.html).




## Create ServiceNow data store

To create a ServiceNow data store, perform the following steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **ServiceNow** , and click **Select**.

  6. In the **Data** section:

     1. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode.

     2. Click **Continue**.

     3. In the **Authentication settings** section, configure authentication based on your chosen connection mode.

        * If you selected **Federated search** , enter the following details:

          * **Instance URL** : The base URL of your ServiceNow instance.
          * **Client ID** : The OAuth client ID for your application.
          * **Client Secret** : The OAuth client secret for your application.
          * **Auth URI** : The authorization endpoint URL provided by ServiceNow.
          * **Token URI** : The token endpoint URL provided by ServiceNow.
          * **User ID** : The ServiceNow user ID.
          * **Password** : The password for the ServiceNow user.
        * If you selected **Data ingestion** , enter the following details:

          * **Instance URL** : The base URL of your ServiceNow instance.
          * **Client ID** : The OAuth client ID for your application.
          * **Client Secret** : The OAuth client secret for your application.
          * **User ID** : The ServiceNow user ID.
          * **Password** : The password for the ServiceNow user.

For more information about credentials, see [ServiceNow configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config).

        * If you selected **Federated Search** , click **Login** and complete the ServiceNow sign-in.

     4. Click **Continue**.

     5. If you selected **Federated search** , do the following:

        1. In the **Destinations** section: 
           1. Enter **Instance URL** of your ServiceNow site.
           2. Enter **Base URL** of your ServiceNow site.
        2. Click **Continue**.

        3. Optional: In the **Advanced options** section, to expose or hide ServiceNow system tables, select the **Include system tables** checkbox.

        4. Click **Continue**.

     6. If you selected **Data ingestion** , in the **Advanced options** section do the following:

        1. Optional: In the **URL suffix** field, enter the URL suffix from the knowledge or catalog portal link.
        2. Optional: To allow a set of static IP addresses in your system, select the **Enable Static IP Addresses** checkbox. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).
        3. Optional: In the **Max QPS** field, enter the maximum queries per second to apply a rate limit on the queries that the connector sends to the ServiceNow instance.
        4. Click **Continue**.
     7. In the **Entities to search** (if you selected **Federated search**) or **Entities to sync** (if you selected **Data ingestion**) section select all the required entities.

        * If you selected **Federated search** , proceed to the next step.
        * If you selected **Data ingestion** , continue with the following steps: 
          1. **Optional:** To sync specific projects, do the following: 
             1. Click **Filter**.
             2. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include to the index** checkbox.
             3. Enter the keys. Press enter after each key.
             4. Click **Save**.
          2. To configure the sync schedule, do the following: 
             1. In the **Sync frequency** list, select the sync frequency. 
                * To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options**.
             2. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see [Sync schedules](https://cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#sync-schedules).
  7. Click **Continue**.

  8. In the **Actions** section:

     * If you selected **Federated search** , from **Select ServiceNow actions to enable** , select the actions from the category to enable them for the connector.
     * If you selected **Data ingestion** :

       1. In the **Authentication settings** section, configure authentication based on your chosen connection mode.
       2. Provide the following authentication details as necessary:

          * **Instance URL** : The base URL of your ServiceNow instance.
          * **Client ID** : The OAuth client ID for your application.
          * **Client Secret** : The OAuth client secret for your application.
          * **Auth URI** : The authorization endpoint URL provided by ServiceNow.
          * **Token URI** : The token endpoint URL provided by ServiceNow.
          * **User ID** : The ServiceNow user ID.
          * **Password** : The password for the ServiceNow user.

For more information about credentials, see [ServiceNow configuration](https://docs.cloud.google.com/gemini/enterprise/docs/servicenow/third-party-config).

       3. Click **Login** and sign-in to ServiceNow to verify your account.

       4. Click **Continue**.

       5. Optional: In the **Advanced options** section, to expose or hide ServiceNow system tables, select the **Include system tables** checkbox.

       6. Click **Continue**.

       7. In the **Destinations** section:

          1. Optional: Enter **Instance URL** of your ServiceNow site.
          2. Optional: Enter **Base URL** of your ServiceNow site.
       8. Click **Continue**.

       9. From **Select ServiceNow actions to enable** , select the actions from the category to enable them for the connector.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

  9. Click **Continue**.

  10. In the **Configuration** section: 

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Your data connector name** field, enter a name for your connector.
     3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
        * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  11. Click **Continue**.

  12. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 

  13. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the ServiceNow connector is ready to be used.

For an ingestion connector created with ServiceNow, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the ServiceNow data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access ServiceNow before executing any queries.

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize ServiceNow and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the ServiceNow API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (ServiceNow API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to ServiceNow. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the ServiceNow API.

## What's next

  * To provide a user interface for querying your ServiceNow data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the ServiceNow data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
