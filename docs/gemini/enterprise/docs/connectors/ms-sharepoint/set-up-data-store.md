---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store/
title: Set up a Microsoft SharePoint data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:38:02.702232+00:00
---

# Set up a Microsoft SharePoint data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Microsoft SharePoint data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Microsoft SharePoint to Gemini Enterprise.

## Before you begin

**Note:** To enforce data source access control and secure data in Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

Ensure the following before you set up your Microsoft SharePoint federated connection:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. Register Gemini Enterprise as an [OAuth 2.0 application in Microsoft Entra ID](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config) and [obtain the following credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#obtain-client-id-and-client-secret):

     * Client ID

     * Client secret

     * Tenant ID

     * Instance URI

  3. Configure the [Microsoft API permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#configure-api-permissions) with the consent of a Microsoft SharePoint admin.




## Create Microsoft SharePoint data store

To create a Microsoft SharePoint data store, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **Microsoft SharePoint** , and click **Select**.

  6. In the **Data** section:

     1. In the **Connector mode** section, select **Federated search** or **Data ingestion** as the connection mode.

     2. Click **Continue**.

     3. In the **Authentication settings** section, configure authentication based on your chosen connection mode.

        1. Provide the following authentication details as necessary: 
           * **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID.
           * **Client secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID.
           * **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center.
           * **Instance URI** : The base URL for your Microsoft SharePoint instance (e.g., `https://{your-domain}.sharepoint.com`).
           * **Microsoft SharePoint Environment Type:** Select the environment that hosts your Microsoft 365 tenant: 
             * Select **Standard** (the default) if you connect to standard commercial Microsoft 365 or Government Community Cloud (GCC).
             * Select **US Government** if you connect to a Microsoft 365 US Government sovereign cloud (GCC High or DoD).

For more information, see [Obtain client credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#obtain-client-id-and-client-secret).

**Note:** These settings apply only to Microsoft 365 US Government (sovereign cloud) customers. If you connect to a US Government cloud, use the matching combination; otherwise keep the defaults (**Standard** and **Global**): 
           * **GCC** : Environment Type **Standard** , Cloud Environment **GCC**.
           * **GCC High** : Environment Type **US Government** , Cloud Environment **GCC High**.
           * **DoD** : Environment Type **US Government** , Cloud Environment **DoD**.
        * If you selected **Data ingestion** with **Federated credentials** authentication method, copy the **Subject identifier** and use it to [add federated credential for data ingestion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#add-fed-credentials).

          * **Subject identifier:** The unique ID of the service account you plan to use.
        * If you selected **Federated search** , click **Login** and complete the third-party sign-in.

     4. Click **Continue**.

     5. If you selected **Federated search** , the **Destinations** section appears. Enter the base URL for the site.

     6. Click **Continue**.

     7. In the **Advanced options** section, select your **Microsoft 365 Cloud Environment** :

        * If you connect to a Microsoft 365 US Government instance, select the option that matches it: **GCC** , **GCC High** , or **DoD**.
        * Otherwise, keep the default, **Global**.
     8. If you selected **Federated search** , in the **Advanced options** section, you can refine the scope of your searches and actions by specifying which Microsoft SharePoint sites or specific paths to include or exclude. You can only mutate or retrieve data within the included paths. Requests for out-of-scope data either fail or return no results.

You can add filters to the data store using the Google Cloud console or API:

### Console

Note: When entering multiple sites, separate each URL with a comma. You can also copy and paste a list of URLs directly from a CSV file.

        1. In the Site filter section: 
           * Choose the filter type: **Include in search** or **Exclude from search**.
           * In the **Site URL filter** field, enter the exact Microsoft SharePoint site URLs to filter, in the format `https://{your-tenant}.sharepoint.com/sites/{your-site-name}`. 

**Note:** Enter the exact site URLs. Subpaths, folders, or document libraries are not supported in this specific field.

        2. In the Path filter section: 
           * Choose the filter type: **Include in search** or **Exclude from search**.
           * In the **Path filter** field, enter the full SharePoint paths. 

**Note:** This field supports subpaths, folders, and document libraries, in the format, `https://{your-tenant}.sharepoint.com/sites/{your-site-name}/{your-folder-name}/`. Any content under the specified path will be filtered.

### REST

To add filters when creating a data store, call the [`setUpDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setUpDataConnector) method.
    
    curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION:setUpDataConnector" \
            -d '{
            "collectionId": "COLLECTION_ID",
            "collectionDisplayName": "COLLECTION_DISPLAY_NAME",
            "dataConnector": {
                "dataSource": "sharepoint_federated_search",
                "params": {
                "client_id": "CLIENT_ID",
                "client_secret": "CLIENT_SECRET",
                "instance_uri": "INSTANCE_URI",
                "tenant_id": "TENANT_ID",
                "FILTER_TYPE": {
                    "FILTER_KEY": [
                    "FILTER_VALUE1",
                    "FILTER_VALUE2"
                    ]
                }
                },
                "entities": [
                {
                    "entityName": "file"
                }
                ],
                "refreshInterval": "7200s",
                "connectorType": "THIRD_PARTY_FEDERATED",
                "connectorModes": [
                "FEDERATED"
                ]
            }
            }'
            

Replace the following:

        * `PROJECT_ID`: the ID of your project. 
        * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
          * `us` for the US multi-region
          * `eu` for the EU multi-region
          * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
        * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
        * `COLLECTION_ID`: the unique ID of the data store. 
        * `COLLECTION_DISPLAY_NAME`: the display name of the data store. 
        * `CLIENT_ID`: the client ID for SharePoint authentication. 
        * `CLIENT_SECRET`: the client secret for SharePoint authentication. 
        * `INSTANCE_URI`: the instance URI for SharePoint. 
        * `TENANT_ID`: the tenant ID for SharePoint. 
        * `FILTER_TYPE`: the type of filter added to your Microsoft SharePoint data stores. For more information, see [Filter types](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store#filter-types). 
        * `FILTER_KEY`: the key for the filter, corresponding to a field in your data. For more information, see [Filter keys](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store#filter-keys). 
        * `FILTER_VALUES`: the value or values to filter on for the specified `FILTER_KEY`. 

For more details on filter types and adding filters, see [Add filters to Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store).

  7. Click **Continue**.

     1. In the **Entities to search** (if you selected **Federated search**) or **Entities to sync** (if you selected **Data ingestion**) section: 
        1. Select all the required entities.
        2. If you selected **Federated search** , proceed to the next step.
        3. If you selected **Data ingestion** , continue with the following steps: 
           1. Optional: To sync specific projects, do the following: 
              1. Click **Filter**.
              2. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include to the index** checkbox.
              3. Enter the keys. Press enter after each key.
              4. Click **Save**.
           2. To configure the sync schedule, do the following: 
              1. In the **Sync frequency** list, select the sync frequency. 
                 * To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options**.
              2. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see [Sync schedules](https://cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#sync-schedules).
  8. Click **Continue**.

  9. In the **Actions** section:

     1. If you selected **Federated search** : 
        1. From **Select Microsoft SharePoint actions to enable** , select the actions from the category to enable them for the connector.
     2. If you selected **Data ingestion** :

        1. In the **Authentication settings** section, configure authentication based on your chosen connection mode.

           1. Provide the following authentication details as necessary:

              * **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID.
              * **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID.
              * **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center.
              * **Instance URI** : The base URL for your Microsoft SharePoint instance (e.g., `https://{your-domain}.sharepoint.com`).

For more information, see [Obtain client credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#obtain-client-id-and-client-secret).

        2. Click **Continue**.

        3. In the **Destinations** section, enter the base URL for the site.

        4. Click **Continue**.

        5. From **Select Microsoft SharePoint actions to enable** , select the actions from the category to enable them for the connector.

  10. Click **Continue**.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

**Warning:**

     * **Default write actions:** When creating and configuring the data store, ensure that any default _write_ actions are explicitly disabled if you only intend to grant read access. Leaving write actions enabled without the corresponding write scopes in Microsoft Entra ID results in authentication and sync errors.

  11. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

  12. In the **Configuration** section: 

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Your data connector name** field, enter a name for your connector.
     3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
        * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  13. Click **Continue**.

  14. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 

  15. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Microsoft SharePoint connector is ready to be used.

For an ingestion connector created with Microsoft SharePoint, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Microsoft SharePoint before executing any queries.

## Enable real-time sync for data ingestion

**Preview — Real-time sync**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Real-time sync is only available for the **Data ingestion** connection mode.

Real-time sync only syncs document entities and doesn't sync data related to identity entities. The following table shows which document events are supported with real-time sync.

Microsoft SharePoint entities | Create | Update | Delete | Permission changes  
---|---|---|---|---  
Attachments | close | close | close | close  
Comments | close | close | close | close  
Events | check | check | check | close  
Files | check | check | check | close  
Pages | check | check | check | close  
  
To enable real-time sync for your data store, follow these steps.

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data Stores**.

  3. Click the name of the Microsoft SharePoint data store for which you want to enable real-time sync.

  4. On the data store **Data** page, wait until the **Connector state** changes to **Active**.

  5. In the **Real-time sync** field, click **View/edit**.

  6. To enable real-time sync, click the **Enable real-time sync** toggle.

  7. In the **Client secret** field, enter a value. This value is used to verify Microsoft SharePoint webhook events. We recommend using a string of 20 characters.

  8. Click **Save**.

Wait for the **Real-time sync** field to change to **Running**.




## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Microsoft SharePoint and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Microsoft API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Microsoft API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Microsoft SharePoint. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Microsoft API.

## What's next

  * To provide a user interface for querying your Microsoft SharePoint data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 
  * To add filters to the data store, see [Add filters to Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
