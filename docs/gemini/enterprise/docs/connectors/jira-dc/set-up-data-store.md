---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/set-up-data-store/
title: Set up a Jira Data Center data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:40.044192+00:00
---

# Set up a Jira Data Center data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Jira Data Center data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Jira Data Center to Gemini Enterprise.

## Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

Before you set up your connection, do the following:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. Complete the steps in [Set up authentication and obtain client credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration#create-oauth-app-link) to get the client ID and client secret, and set up OAuth scopes.

  3. If your Jira Data Center instance uses a private IP, [publish a Private Service Connect producer service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) for your Jira Data Center instance. For more information about using Private Service Connect to connect Gemini Enterprise to self-hosted data sources, see [Introduction to self-hosted data sources](https://docs.cloud.google.com/gemini/enterprise/docs/introduction-to-self-hosted).




If you are using the data ingestion connection mode, you must meet these additional requirements:

  1. Verify that you have the [Jira System Administrators permission](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration#create-jira-user) to fetch Access Control List (ACL) information.

  2. If you have [set up issue-level security](https://confluence.atlassian.com/adminjiraserver/configuring-issue-level-security-938847117.html) in Jira, [install the Permission Accessor for Jira Data Center plugin](https://marketplace.atlassian.com/apps/1237927/permission-accessor-for-jira-data-center?hosting=datacenter&tab=installation). This plugin provides REST endpoints to Gemini Enterprise. These endpoints enable Gemini Enterprise to retrieve space permission details, content restrictions, and email addresses of licensed users. This information is then used to ensure that the correct permissions are applied within the Gemini Enterprise search experience.




## Create the Jira Data Center data store

To create the Jira Data Center data store, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

**Note:** To access the unified flow, your project must be on the allowlist.
  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **Jira Data Center** , and click **Select**.

  6. In the **Data** section:

     1. In the **Connector mode** section, select **Data ingestion** or **Federated search**.

**Note:** **Data ingestion** is in Private Preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).
     2. Click **Continue**.

     3. In the **Authentication settings** section, configure authentication based on your chosen connection mode.

        1. Provide the authentication details.

           * For **Federated search** , provide the following details:

             * **Instance URI:** The base URL of your Jira Data Center instance, for example, `https://jira.yourcompany.com`.

**Note:** Ensure the URL includes the protocol (`https://`) and does not end with a trailing slash.
             * **Client ID:** The unique identifier for the OAuth application registered with Jira Data Center.

             * **Client secret:** The Secret Manager secret that contains the client secret for authenticating requests.

To obtain these credentials, see [Set up authentication and obtain client credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration#create-oauth-app-link).

           * For **Data ingestion** , select one of the following authentication methods: **Username** and **Password** , **Personal access token** , or **API token** , and then enter the required details.

        2. Click **Continue**.

     4. From the **Destination type** list, select **Public** or **Private**.

        * If you selected the **Public** destination type, for **Domain URL** , enter your public URL. This must match the instance URI.
        * If you selected the **Private** destination type, enter the following information:

          1. **Service attachment** : Enter your Private Service Connect service attachment. To obtain this, you need to [publish a Private Service Connect producer service](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer) for your Jira Data Center instance.
          2. If the region of your Private Service Connect service attachment is different from the region of your data store, select the **Enable PSC Global Access** checkbox.
          3. For an instance with a Domain URL: 
             * Optional: **Base domain name** : Enter your base domain. Specify a unique and granular base domain name (for example, `jira.example.com`) rather than a shared root domain (for example, `example.com`). If you have multiple data connectors in the same project, such as both Jira Data Center and Confluence Data Center, ensure each uses its own full instance domain as the base domain to avoid network collisions. Two data connectors using Private Connectivity with the same base domain name cannot be created in the same project.
             * **Domain URL** : Enter your domain URL. This must match the instance URI.
             * Optional: **Destination port** : Enter your destination port.
          4. For an instance without a Domain URL: 
             * **Destination port** : Enter your destination port.
**Note:** Private connectivity is required when connecting to private, on-premises authentication endpoints.
     5. Click **Continue**.

     6. Optional: Click **Advanced options**.

        * If you selected **Federated search** , do the following:

          1. If you enable the **SSL settings** checkbox, select a **Trust Model** from **Private** , **Public** , or **Insecure** , and then configure the required fields. For more information on trust models, see [Trust models](https://docs.cloud.google.com/certificate-authority-service/docs/trust-model).

             * **Public** : Use this option if your Jira Data Center instance uses certificates issued by a publicly trusted CA.
             * **Private** : Use this option if your Jira Data Center instance uses certificates signed by a private or internal CA.
             * **Insecure** : This option bypasses certificate validation. It is not recommended for production environments as it can expose your connection to security risks.

The following fields are common to all Trust Models:

             * **Keystore Client Certificate** : The client certificate in PEM format. For example, `-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----`.
             * **Keystore Client Private Key** : The private key for the client certificate in PEM format.
             * **Keystore Client Private Key Passphrase** : The passphrase for the client private key, if applicable.

The following additional detail is required for the **Private** Trust Model:

             * **Private Certificate** : The public certificate of the private CA in PEM format.
          2. You can refine the scope of your searches and actions by specifying which Jira Data Center project keys to include or exclude. You can only mutate or retrieve data within the included projects. Requests for out-of-scope data either fail or return no results.

You can add filters to the data store using the Google Cloud console or API:

### Console

Note: When entering multiple project keys, separate each key with a comma. You can also copy and paste a list directly from a CSV file.

             1. In the Project filter section: 
                * Choose the filter type: **Include in search** or **Exclude from search**.
                * In the **Project filter** field, enter the exact Jira Data Center project keys to filter (for example, `ENG, HR, SUPPORT`).

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
                "dataSource": "jira_datacenter",
                "params": {
                "client_id": "CLIENT_ID",
                "client_secret": "CLIENT_SECRET",
                "instance_uri": "INSTANCE_URI",
                "FILTER_TYPE": {
                    "FILTER_KEY": [
                    "FILTER_VALUE1",
                    "FILTER_VALUE2"
                    ]
                }
                },
                "entities": [
                {
                    "entityName": "project"
                },
                {
                    "entityName": "issue"
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
             * `CLIENT_ID`: the client ID for Jira Data Center authentication. 
             * `CLIENT_SECRET`: the client secret for Jira Data Center authentication. 
             * `INSTANCE_URI`: the instance URI for Jira Data Center. 
             * `FILTER_TYPE`: the type of filter added to your Jira Data Center data stores. For more information, see [Filter types](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store#filter-types). 
             * `FILTER_KEY`: the key for the filter (`Project`). For more information, see [Filter keys](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store#filter-keys). 
             * `FILTER_VALUES`: the value or values to filter on (`ENG`, `HR`, `SUPPORT`). 

        * If you selected **Data ingestion** , do the following:

          1. Select the **Enable Static IP Addresses** checkbox. After creating the data store, you must allowlist the registered static IPs to ensure sync runs succeed. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).
          2. In the **Max QPS** field, specify the maximum number of queries sent to the Jira Data Center data store per second.
          3. Select the **Enable Custom Fields** checkbox. If enabled, the data store fetches custom fields from the Jira Data Center.
          4. If required, select the **Proxy settings** and **SSL settings** checkboxes to enable them.
     7. Click **Continue**.

     8. In the **Entities to search** (if you selected **Federated search**) or **Entities to sync** (if you selected **Data ingestion**) section:

        1. Select all the required entities.
        2. If you selected **Federated search** , proceed to the next step.
        3. If you selected **Data ingestion** , continue with the following steps:

           1. **Optional:** To sync specific projects, do the following: 
              1. Click **Filter**.
              2. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include in the index** checkbox.
              3. Enter the keys. Press **Enter** after each key.
              4. Click **Save**.
           2. To configure the sync schedule, do the following:

              1. In the **Sync frequency** list, select a sync frequency. 
                 * To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options**.
              2. In the **Incremental sync frequency** list, select an incremental sync frequency.

For more information, see [Sync schedules](https://cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#sync-schedules).

  7. Click **Continue**.

  8. If you selected **Federated search** , in the **Actions** section, from the **Select Jira Data Center actions to enable** list, choose the actions to enable for the data store.

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

  13. Click **Continue**.

  14. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data stores** page.

  15. If you selected the **Private** destination type and [configured your Private Service Connect producer service](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer) to **Accept connections for selected projects** (explicit approval), do the following:

     1. In the Google Cloud console, search for `Private Service Connect` and go to the **Private Service Connect** page.

     2. Click the **Published services** tab.

     3. Click the name of the Private Service Connect service corresponding to your Jira Data Center data store.

     4. In the **Connected projects** section, select the checkbox next to the Gemini Enterprise tenant project for the data store, and then click **Accept project**. The Gemini Enterprise tenant project ID ends in `-tp`.

The data store status remains as **Creating** in the **Data Stores** page until you click **Accept project** on the service details page within Private Service Connect. After you click **Accept project** , the data store status changes to **Active**.




To verify the state of the data store, do the following in the **Data stores** page:

  1. Navigate to the newly created data store in the data store list and monitor its state until it changes to **Active**.
  2. When the data store state changes from **Creating** to **Active** , the Jira Data Center connector is ready to be used.



After creating the data store:

  * [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).
  * [Connect it to the Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * [Add filters to the Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store).
  * [Authorize](https://docs.cloud.google.com/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to Jira Data Center before executing any queries.



For information on permissions required to perform search, see [Required scopes](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc#set-up-permissions).

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Jira Data Center and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Jira Data Center API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Jira Data Center API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Jira Data Center. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Jira Data Center API.

## What's next

  * To provide a user interface for querying your Jira Data Center data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To add filters to the data store, see [Add filters to a Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store).
  * To manage the list of actions, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
