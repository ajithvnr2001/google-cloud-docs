---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/set-up-data-store/
title: Set up a Zendesk data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:46.619553+00:00
---

# Set up a Zendesk data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Zendesk data store Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to create a data store and connect Zendesk to Gemini Enterprise.

## Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

Before you set up your Zendesk data store, ensure the following:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. [Create an OAuth client](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config#create-oauth-client) and obtain the following credentials:

     * Client ID

     * Client secret

  3. Configure the [necessary permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config#set-up-permissions) within Zendesk for the OAuth application.

  4. Ensure that [token access is enabled](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config#enable-token-access) in the Zendesk API settings.




### Create the Zendesk data store

To create the Zendesk data store, perform the following steps:

  1. In the Google Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add **Create data store**.

  5. In the **Source** , search for **Zendesk** , and click **Select**.

  6. In the **Data** section: 

     1. In the **Authentication settings** section, provide the following details: * **Instance URI:** Enter the Zendesk instance URI (for example, `https://[subdomain].zendesk.com`). * **Client ID:** The unique identifier of the application registered in Zendesk. * **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Zendesk.

For information on how to obtain the client ID and client secret, see [Obtain client ID and client secret](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config#create-oauth-client). For the permissions required to perform search, see [Required permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk#set-up-permissions).

     2. Click **Login** and complete the Zendesk sign-in.

     3. Click **Continue**.

     4. In the **Destinations** section:

        1. **Proxy Server** : Enter the hostname or IP address of a proxy to route HTTP traffic through, including the **Host** and **Port**.
        2. **Zendesk Support URL** : Enter the instance URL, including `https://`, which is your Zendesk Support URL.
        3. Click **Continue**.
     5. Optional: In the **Advanced options** section:

        1. **Enable Static IP Addresses** : Registers a narrow set of static IP addresses to be added to your system's allowlist. Sync runs will fail until these IP addresses are in the allowlist. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).
        2. **Max API Requests Per Minute** : The maximum number of API requests per minute to send to your Zendesk instance for each connector run.
        3. Click **Continue**.
     6. In the **Entities to search** section, select all the entities to search from the list. You must select at least one entity.

**Note:** To avoid 404 errors for `search articles` and `search community posts` entities, ensure the Zendesk help center is enabled. For more information, see [Enabling and activating your help center](https://support.zendesk.com/hc/en-us/articles/5702269234330-Enabling-and-activating-your-help-center).
  7. Click **Continue**.

  8. In the **Actions** section, for **Select Zendesk actions to enable** , choose the actions from the category to enable them for the data store.

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




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Zendesk connector is ready to be used.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the Zendesk data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to Zendesk before executing any queries.

For information on permissions required to perform search, see [Required permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk#set-up-permissions).

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Zendesk and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Zendesk API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Zendesk API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Zendesk. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Zendesk API.

## What's next

  * To provide a user interface for querying your data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Zendesk data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
