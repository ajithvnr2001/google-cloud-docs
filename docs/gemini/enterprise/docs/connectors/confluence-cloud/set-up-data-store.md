---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store/
title: Set up a Confluence Cloud data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:50.454725+00:00
---

# Set up a Confluence Cloud data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Confluence Cloud data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Confluence Cloud to Gemini Enterprise. 

## Before you begin

Ensure the following before you set up your Confluence Cloud federated connection:

  * Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

    2. Locate the user account and click edit **Edit**.
    3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  * To enforce data source access control and secure data in Google Gemini Enterprise, [configure your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

  * To set up the Confluence Cloud data store, you must use the new centralized Atlassian user management model. If you are using the original model, you need to migrate your user management before proceeding. For more information, see [Site administrator role](https://support.atlassian.com/atlassian-cloud/kb/site-administrator-role-in-the-centralized-user-management-and-original-user-management-experiences/).

  * Create an [OAuth 2.0 app](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#create-an-oauth-configuration), [obtain the client ID and secret](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#obtain-client-id-and-client-secret), and configure the [minimum application permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#configure-minimum-application-permissions) with the consent of a Confluence Cloud administrator.

  * Optional: To retrieve user email addresses from Confluence Cloud, even when settings restrict email visibility, [install the User Identity Accessor for Confluence Cloud app](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#install-identity-accessor-app) with Confluence _Site administrator_ privileges, and then [configure it](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#configure-identity-accessor-app) to securely retrieve user email addresses. You might not need to install this app if email addresses are already publicly accessible.

**Note:** Atlassian is updating user interface elements, and some elements mentioned in this documentation are being renamed (for example, **Products** is being renamed to **Apps**). For more information, see [Atlassian Administration terminology change from "products" to "apps"](https://community.atlassian.com/forums/Atlassian-Platform-articles/Atlassian-Administration-terminology-change-from-products-to/ba-p/2967398).



## Create Confluence Cloud data store

To create a Confluence Cloud data store, perform the following steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **Confluence Cloud** , and click **Select**.

  6. In the **Data** section:

     1. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode.
     2. Click **Continue**.

     3. In the **Authentication settings** section, configure authentication based on your chosen connection mode.

        * If you selected **Data ingestion** :

          1. Select **OAuth 2.0 client credentials** or **API token** as the authentication method.
          * If you select **OAuth 2.0 client credentials** , enter the following details:

            * **Client ID** : The identifier for your OAuth 2.0 app.
            * **Client secret** : The secret key associated with your OAuth 2.0 app.
            * **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://your-domain.atlassian.net`).
            * **Instance ID** : A unique identifier for your Confluence Cloud instance.
          * If you select **API token** , enter the following details:

            * **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://your-domain.atlassian.net`).
            * **User account** : The Atlassian username associated with the API token.
            * **API token** : The API token generated from your Atlassian account.
        * If you selected **Federated search** :

          1. Enter the following details:

             * **Client ID** : The identifier for your OAuth 2.0 app.
             * **Client secret** : The secret key associated with your OAuth 2.0 app.
             * **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://your-domain.atlassian.net`).
          2. Click **Login** and complete the Atlassian sign-in.

For more information about credentials, see [Confluence Cloud configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config).

     4. Click **Continue**.

     5. In the **Destinations** section, enter the URL for your Confluence Cloud endpoint.

     6. Click **Continue**.

     7. In the **Entities to sync** (if you selected **Data ingestion**) or **Entities to search** (if you selected **Federated search**) section:

        1. Select all the required entities.
        * If you selected **Federated search** , proceed to the next step.
        * If you selected **Data ingestion** , do the following:

          1. Optional: To sync specific projects, do the following:

             1. Click **Filter**.
             2. To filter entities out of the index, select **Exclude from the index** , or to ensure that they are included in the index, select **Include in the index**.
             3. Enter the space keys. Press **Enter** after each space key. The space key is the unique code in a Confluence space URL, found after `/spaces/`. (For example, in `https://company.atlassian.net/wiki/spaces/ABC/overview`, the space key is `ABC`.)
             4. Click **Save**.
          2. To configure the sync schedule, do the following:

             1. In the **Sync frequency** list, select the sync frequency.

                * To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options**.
             2. In the **Incremental sync frequency** list, select the incremental sync frequency.

For more information, see [Sync schedules](https://cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#sync-schedules).

  7. Click **Continue**.

  8. In the **Actions** section:

     * If you selected **Federated search** : 
       1. From **Select Confluence Cloud actions to enable** , select the actions from the category to enable them for the data store.
     * If you selected **Data ingestion** :

       1. In the **Authentication settings** section, configure authentication based on your chosen connection mode.
       2. Enter the following authentication details:

          * **Client ID** : The identifier for your OAuth 2.0 app.
          * **Client secret** : The secret key associated with your OAuth 2.0 app.
          * **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://your-domain.atlassian.net`).
          * **Instance ID** : A unique identifier for your Confluence Cloud instance.

For more information about credentials, see [Confluence Cloud configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config).

       3. Click **Login** and sign-in to Confluence Cloud to verify your account.

       4. Click **Continue**.

       5. In the **Destinations** section, enter the URL for your Confluence Cloud endpoint.

       6. From **Select Confluence Cloud actions to enable** , select the actions from the category to enable them for the data store.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To view and manage the list of actions, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

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

  14. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Confluence Cloud data store is ready to be used.

For an ingestion data store created with Confluence Cloud, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the Confluence Cloud data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to access Confluence Cloud before executing any queries.

## Enable real-time sync for data ingestion

**Preview — Real-time sync**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Real-time sync only syncs document entities and doesn't sync data related to identity entities. The following table shows which document events are supported with real-time sync.

Confluence entities | Create | Update | Delete | Permission changes  
---|---|---|---|---  
Spaces | check | check | close | close  
Pages | check | check | close | close  
Blogs | check | check | close | close  
Attachments | check | check | close | close  
Comments | check | check | close | close  
Whiteboards | close | close | close | close  
  
Enable real-time sync 20 minutes after creating the Confluence Cloud data store.

To enable real-time sync for a Confluence data store, follow these steps:

### Generate a webhook URL

  1. Navigate to the Gemini Enterprise page, and in the navigation menu, click **Data Stores**.
  2. Select a Confluence data store.
  3. Click **View/Edit** in the **Realtime sync** row.
  4. In the **View and edit realtime sync parameters** dialog, do the following: 
     1. To turn on real-time sync, click the **Enable realtime sync** toggle.
     2. In the **Client secret** field, enter a placeholder value, such as `clientsecret`.
     3. Click **Save**.
  5. After the status of **Realtime sync** changes to `Running`, click **View/Edit**.
  6. In the **View and edit realtime sync parameters** dialog, do the following: 
     1. Copy the **Webhook URL**.
     2. Click **Close**.



### Subscribe to events using the API

To receive real-time updates from Confluence, you must subscribe to specific events using a POST request. To make API calls, use the same administrator account used for setting up authentication and permissions in Confluence to create the data store.
    
    
          curl -X POST \
            INSTANCE_URL/wiki/rest/webhooks/1.0/webhook \
            -H "Content-Type: application/json" \
            -u "USERNAME:API_TOKEN" \
            -d '{
              "name": "SUBSCRIPTION_NAME",
              "url": "LISTENER_URL",
              "events": [
                "EVENT_TYPE_1",
                "EVENT_TYPE_2"
              ],
              "active": true
            }'
    

  * INSTANCE_URL: The base web address for your Atlassian Cloud site.

  * USERNAME: The Atlassian Cloud username.

  * API_TOKEN: The API token generated from your Atlassian account. For more information, see [Set up an API token in Confluence](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#api-token)

  * SUBSCRIPTION_NAME: A unique name for your event subscription.

  * LISTENER_URL: The webhook URL copied from the Google Cloud console once Real-Time Sync (RTS) is enabled on your data store.

  * EVENT_TYPE: The event types that you want to subscribe to. You can subscribe to create, update, and delete events for attachments, blog posts, pages, spaces, and comments.

The user can subscribe to the following events:

    * `space_created`
    * `space_updated`
    * `page_created`
    * `page_updated`
    * `attachment_created`
    * `attachment_updated`
    * `comment_created`
    * `comment_updated`
    * `blog_created`
    * `blog_updated`
**Note:** `Whiteboard` and `trashed` events are not supported. Create subscriptions only for entities already added to your data store to avoid ingesting unwanted data.

#### Example command and result
    
    curl -X POST \
        https://cymbalgroup.atlassian.net/wiki/rest/webhooks/1.0/webhook \
        -H "Content-Type: application/json" \
        -u "admin1:######" \
        -d '{
          "name": "Cymbal_DCT",
          "events": [
            "attachment_created",
            "attachment_updated"
          ],
          "url": "https://rt-server-a-jx3m2-uw.a.run.app/webhook",
          "active": true
        }'
    
    
    * * *
    
    
    {
    "name": "Cymbal_DCT",
    "url": "https://cymbalgroup.atlassian.net/wiki/rest/webhooks/1.0/webhook",
    "description": " Webhook for Cymbal DCT group to fetch attachments.",
    "excludeBody": false,
    "filters": {},
    "events": [
        "attachment_created",
        "attachment_updated",
    ],
    "enabled": true,
    "self": https://rt-server-a-jx3m2-uw.a.run.app/webhook,
    "lastUpdatedUser": "Cymb_389",
    "lastUpdatedDisplayName": "Ariel",
    "lastUpdated": 1752095647212
    }
    




#### API error codes

This table lists common API error codes users encounter when creating webhooks. 

Error class | Error code | Error message | Troubleshooting  
---|---|---|---  
`403` | `FORBIDDEN` | Current user not permitted to use Confluence. | Ensure a valid token from an administrator account and correct API endpoint.  
  
## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Confluence Cloud and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Atlassian API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Atlassian API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Confluence Cloud. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Atlassian API.

## What's next

  * To provide a user interface for querying your Confluence Cloud data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Confluence Cloud data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To view and manage the list of actions, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
