---
url: https://docs.cloud.google.com/gemini/enterprise/docs/dropbox/data-store/
title: Set up a Dropbox data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:45.091649+00:00
---

# Set up a Dropbox data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/dropbox/data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Set up a Dropbox data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store, and connect Dropbox to Gemini Enterprise.

**Note:** To enforce data source access control and secure data in Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

## Before you begin

Before you set up your Dropbox data store, do the following:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. Create an app in the Dropbox App Console, obtain the authentication credentials, and set the required scopes. For more information, see [Dropbox configuration](https://docs.cloud.google.com/gemini/enterprise/docs/dropbox/config).




## Create the Dropbox data store

To create a Dropbox data store, do the following:

  1. In the Google Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add **Create data store**.

  5. On the **Select a data source** page, enter _Dropbox_ into the search field. The Dropbox card displays.

  6. Click Select.

![Select the Dropbox data source](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/select-source.png)

  7. In the **Data** section, fill in the following fields:

     1. For the **Connector mode** field, select **Federated search** and click **Continue**.

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

     2. Under **Authentication settings** , enter the values you copied when you created an app in the Dropbox App Console:

        * For **Client ID** , enter the Dropbox app's **App key**.

        * For **Client Secret** , enter the Dropbox app's **App secret**.

For more information about creating an app in the Dropbox App Console, see [Dropbox configuration](https://docs.cloud.google.com/gemini/enterprise/docs/dropbox/config).

![Provide your client ID and client secret](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/authentication-settings.png)

Click **Login**.

     3. Click **Continue**.

     4. In the **Entities to search** section, select the entity types that you want Gemini Enterprise to search.

![Select entities to include in search](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/entities.png)

Click **Continue**.

  8. In the **Actions** section, select the actions that you want users to be able to perform in their Dropbox accounts using the Gemini Enterprise assistant.

**Note:** If you skip adding actions in this step, you must create a new data store to add actions.

To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

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

![Select a location and enter a name for the data store](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/configuration.png)

Click **Continue**.

  10. In the **Billing** section, select **General pricing** or **Configurable pricing**. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and [Licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses). 

![Select a pricing model](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/dropbox-images/billing.png)




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Dropbox data store is ready to be used.

After creating the data store, do the following before running any queries:

  1. [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  2. [Connect the app](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store) to the Dropbox data store.

  3. [Authorize](https://docs.cloud.google.com/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to connect to Dropbox.




For information about the permissions required to perform a search, see [Minimum permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox#minimum-permissions-actions).

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Dropbox and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Dropbox API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Dropbox API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Dropbox. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Dropbox API.

## What's next

  * To provide a user interface for querying your data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Dropbox data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).

  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).

  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
