---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store/
title: Set up a Jira Cloud data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:13.515244+00:00
---

# Set up a Jira Cloud data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Jira Cloud data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Jira Cloud to Gemini Enterprise. 

## Before you begin

Ensure the following before you set up your Jira Cloud federated connection:

  * Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

    2. Locate the user account and click edit **Edit**.
    3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  * To enforce data source access control and secure data in Google Gemini Enterprise, [configure your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

  * To set up the Jira Cloud data store, you must use the new centralized Atlassian user management model. If you are using the original model, you need to migrate your user management before proceeding. For more information, see [Site administrator role](https://support.atlassian.com/atlassian-cloud/kb/site-administrator-role-in-the-centralized-user-management-and-original-user-management-experiences/).

  * Create an [OAuth 2.0 app](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#create-an-oauth-configuration), [obtain the client ID and secret](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#obtain-client-id-and-client-secret), and configure the [minimum application permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#configure-minimum-application-permissions) with the consent of a Jira Cloud administrator. [Verify that you have Jira _organization administrator_ access](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#verify-jira-org-admin-access) to the Jira instance and project. With the _organization administrator_ access, you can set up minimum permissions and provide access privileges to user groups.

  * Optional: To retrieve user email addresses from Jira Cloud, even when settings restrict email visibility, install the [User Identity Accessor for Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#install-identity-accessor-app) app with Jira _Site administrator_ privileges to [install](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#install-identity-accessor-app) and [configure](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#configure-identity-accessor-app) it to securely retrieve user email addresses. You might not need to install this app if email addresses are already publicly accessible.

**Note:** Atlassian is updating user interface elements, and some elements mentioned in this documentation are being renamed (for example, **Products** is being renamed to **Apps**). For more information, see [Atlassian Administration terminology change from "products" to "apps"](https://community.atlassian.com/forums/Atlassian-Platform-articles/Atlassian-Administration-terminology-change-from-products-to/ba-p/2967398).



## Create Jira Cloud data store

To create a Jira Cloud data store, perform the following steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **Jira Cloud** , and click **Select**.

  6. In the **Data** section:

     1. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode.

     2. Click **Continue**.

     3. In the **Authentication settings** section, configure authentication based on your chosen connection mode.

        1. Provide the following authentication details:

           * **Client ID** : The identifier for your OAuth 2.0 app.
           * **Client secret** : The secret key associated with your OAuth 2.0 app.
           * **Instance URI** : The base URL of your Jira Cloud instance (For example, `https://your-domain.atlassian.net`).
           * **Instance ID** : A unique identifier for your Jira Cloud instance.

For more information about how to obtain these credentials, see [Jira Cloud configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config).

        2. If you selected **Federated search** , click **Login** and complete the Atlassian sign-in.

        3. Click **Continue**.

     4. In the **Destinations** section, enter the URL to your Jira Cloud endpoint.

     5. Click **Continue**.

     6. In the **Advanced options** section:

        * Optional: To allow a set of static IP addresses in your system, select the **Enable Static IP Addresses** checkbox. After creating the data store, you must view the registered static IP addresses on the data store details page and add them to your Jira Cloud IP allowlist rule. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).
        * If you selected **Federated search** and if you have custom fields, select **Include Custom Fields** to make them searchable. Jira custom fields are user-defined data fields that store specialized information not available in default system fields.
        * If you selected **Data ingestion** : 
          1. Optional: In the **Max QPS** field, enter the maximum queries per second to apply a rate limit on the queries that the connector sends to the Jira Cloud instance. If not set, default is 12.
          2. Optional: If you have set up **User Identity Accessor for Jira Cloud** : 
             1. In the **Jira Identity Sync Forge URL** field, enter the target URL of the Forge app generated within your instance.
             2. In the **Jira Identity Sync Forge Client Secret** field, enter the API key or token generated within the Jira application's configuration. For more information about how to set up the User Identity Accessor for Jira Cloud, see [Install User Identity Accessor](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#configure-identity-accessor-app).
     7. In the **Entities to search** (if you selected **Federated search**) or **Entities to sync** (if you selected **Data ingestion**) section:

        1. Select all the required entities.
        2. If you selected **Federated search** , proceed to the next step.
        3. If you selected **Data ingestion** , continue with the following steps: 
           1. Optional: To sync specific projects, do the following: 
              1. Click **Filter**.
              2. To filter entities out of the index, select **Exclude from the index** , or to ensure that they are included in the index, select **Include to the index**.
              3. Enter the project key. Press **Enter** after each project key. For more information about obtaining the project key, see [Obtain project key](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#obtain-project-id).
              4. Enter the keys. Press enter after each key.
              5. Click **Save**.
           2. To configure the sync schedule, do the following: 
              1. In the **Sync frequency** list, select the sync frequency. 
                 * To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options**.
              2. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see [Sync schedules](https://cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#sync-schedules).
  7. Click **Continue**.

  8. In the **Actions** section:

     * If you selected **Federated search** , in the **Select Jira Cloud actions to enable** section, select the actions to enable for the data store.
     * If you selected **Data ingestion** :

       1. In the **Authentication settings** section:

          1. Provide the following authentication details: 
             * **Client ID** : The identifier for your OAuth 2.0 app.
             * **Client Secret** : The secret key associated with your OAuth 2.0 app.
             * **Instance URI** : The base URL of your Jira Cloud instance (For example, `https://your-domain.atlassian.net`).
             * **Instance ID** : A unique identifier for your Jira Cloud instance.

For more information about credentials, see [Jira Cloud configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config).

          1. Click **Login** and sign-in to Jira Cloud to verify your account.
       2. Click **Continue**.

       3. From **Select Jira Cloud actions to enable** , select the actions from the category to enable them for the data store.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To view and manage the list of actions, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

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




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Jira Cloud data store is ready to be used.

For an ingestion data store created with Jira Cloud, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the Jira Cloud data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to access Jira Cloud before executing any queries.

## Enable real-time sync for data ingestion

**Preview — Real-time sync**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Real-time sync only syncs document entities and doesn't sync data related to identity entities. The following table shows which document events are supported with real-time sync.

Jira entities | Create | Update | Delete | Permission changes  
---|---|---|---|---  
Issues | check | check | check | close  
Worklogs | check | check | check | close  
Projects | check | check | check | close  
Comments | check | check | check | check  
Attachments | check | close | check | close  
  
To enable real-time sync for a Jira Cloud data store, follow these steps:

### Generate a webhook URL

  1. Navigate to the Gemini Enterprise page, and in the navigation menu, click **Data Stores**.
  2. Select a Jira Cloud data store.
  3. Click **View/Edit** in the **Realtime sync** row.

  4. In the **View and edit realtime sync parameters** dialog, do the following:

     1. To turn on real-time sync, click the **Enable realtime sync** toggle.
     2. Enter a value in the **Client secret** field and copy it. You need this value again when creating a webhook in the Jira administration console.
     3. Click **Save**.
  5. After the status of **Realtime sync** changes to `Running`, click **View/Edit**.

  6. In the **View and edit realtime sync parameters** dialog, do the following:

     1. Copy the **Webhook URL**.
     2. Click **Close**.



### Create a webhook

  1. Sign in to the Jira administration console.
  2. Click **Settings** and select **System**.
  3. In the **System settings** pane, select **Webhooks**.
  4. Click **Create a webhook**. For information about webhooks, see [Webhooks](https://developer.atlassian.com/server/jira/platform/webhooks/).
  5. Enter a name for the webhook.
  6. Select the **Status** as `Enabled`.
  7. In the **URL** field, paste the URL copied from Gemini Enterprise and append `/{issue.id}`.
  8. In the **Secret** field, enter the same value you entered when generating a webhook URL in Gemini Enterprise.

**Note:** To verify data consistency and prevent errors when configuring webhooks in Jira, only select entities that are enabled for sync in your data store.
  9. In the **Issue related events** section, select the following options: 

Entities | Created | Updated | Deleted  
---|---|---|---  
Issue | Yes | Yes | Yes  
Worklog | Yes | Yes | Yes  
Comment | Yes | Yes | Yes  
Attachment | Yes | No | Yes  
  10. In the **Project related events** section, select the **created** , **updated** , and **deleted** checkboxes for the **Project** entity.

  11. Click **Create**.




## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Jira Cloud and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Atlassian API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Atlassian API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Jira Cloud. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Atlassian API.

## What's next

  * To provide a user interface for querying your Jira Cloud data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Jira Cloud data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To view and manage the list of actions, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
