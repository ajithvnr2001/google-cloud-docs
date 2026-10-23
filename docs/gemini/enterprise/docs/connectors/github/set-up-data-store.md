---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/set-up-data-store/
title: Set up a GitHub data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:11.325541+00:00
---

# Set up a GitHub data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a GitHub data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect GitHub to Gemini Enterprise. 

## Before you begin

Before setting up your GitHub connection, ensure you have the following in place:

  * Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

    2. Locate the user account and click edit **Edit**.
    3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  * Sign in to your GitHub account and [obtain authentication credentials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/github-configuration#set-permissions-and-get-credentials%7D).

  * Create a GitHub app to use this connector. For more information, see [Creating GitHub apps](https://docs.github.com/en/apps/creating-github-apps).




## Create GitHub data store

To create a GitHub data store, perform the following steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **GitHub** , then select it.

  6. In the **Data** > **Authentication settings** section:

     1. Enter the client credential details:

        * **Client ID** : The OAuth client ID for your application.
        * **Client Secret** : The OAuth client secret for your application.

For more information about credentials, see [GitHub configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/github-configuration#set-permissions-and-get-credentials%7D).

     2. If your users sign in through an identity provider (IdP), such as with [GitHub Enterprise Managed Users (EMU)](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users), then enter the GitHub SSO sign-in details. Otherwise, leave these fields blank.

        * **GitHub SSO Scope** : The GitHub namespace that gates sign-in. If your IdP is configured at the enterprise level, select **enterprises**. If your IdP is configured at the organization level, select **orgs**.

        * **GitHub SSO Slug** : The slug of your GitHub enterprise or organization, for example `octocorp` for the enterprise URL `https://github.com/enterprises/octocorp`. Enter the slug only, not a full URL.

     3. Click **Verify Auth** and complete verifying the GitHub authorization.

  7. In the **Data** > **Advanced options** section:

     1. Enter your GitHub organization name in the **Organization Name** field. This is required to scope search and actions.

     2. Click **Continue**.

  8. In the **Data** > **Entities to search** section:

     1. Select the required entities.

     2. Click **Continue**.

  9. In the **Actions** section:

     1. For **Select GitHub actions to enable** , choose the actions from the category to enable them for the data store.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

     2. Click **Continue**.

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




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the GitHub connector is ready to be used.

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize GitHub and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the GitHub API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (GitHub API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to GitHub. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the GitHub API.

## What's next

  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
