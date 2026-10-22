---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box/set-up-data-store/
title: Set up a Box data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:36.032544+00:00
---

# Set up a Box data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Box data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Box to Gemini Enterprise.

## Before you begin

Before you set up your Box connection, do the following:

  1. Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Locate the user account and click edit **Edit**.
     3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  2. Configure the Box integration for Gemini Enterprise. For details, see [Step 1: Configure Box integration](https://docs.box.com/en/box-mcp/configuring-box-mcp-server/gemini-enterprise#step-1-configure-box-integration) in the Box documentation.




## Create the Box data store

To create the Box data store, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Go to Gemini Enterprise](https://console.cloud.google.com/gen-app-builder/engines)

  2. Click **Data stores** in the navigation menu.

  3. Click **Create data store**.

  4. In the **Third-party connectors** section, select **Box**.




**Note:** Box uses Google-managed OAuth. You don't need to create your own OAuth application or provide a client ID and client secret. You authorize the connector with your Box account when you enable connector in app.

  1. In the **Data** section:

     1. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).

     2. Click **Continue**.

     3. In the **Entities to search** section, select the entities that you want Gemini Enterprise to search. For Box, select **Box MCP**.

  2. Click **Continue**.

  3. In the **Configuration** section:

     1. From the **Multi-region** list, select the location for your data store.

     2. In the **Your data connector name** field, enter a name for your data store.

     3. Optional: In the **Tag** field, enter a stable identifier for this data store across versions. This value is immutable after you set it.

     4. If you selected `us` or `eu` as the location, configure the **Encryption settings** :

        * Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see [Register a single-region key for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
     5. Optional: In the **Sensitive Data Protection policy** section, attach an existing [Sensitive Data Protection](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step.

  4. Click **Create**.




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Box data store is ready to be used.

After creating the data store, connect the data store you just created to an existing app or [create a new app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store) it to the new app, and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Box before executing any queries.

## Enable actions

By default, all actions are turned off. When you connect Box, all of its tools are imported and displayed as actions in the Gemini Enterprise data store. To enable these actions for your users, follow these steps:

  1. Go to your Box data store.
  2. Click **Actions > Reload custom actions** to reauthenticate.

**Note:** This action performs a `tools/list` call on the MCP server to retrieve available tools, which are then displayed on the screen.
  3. Select the actions to enable.

  4. Click **Enable actions**.




## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Box and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Box API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Box API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Box. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Box API.

## What's next

  * To provide a user interface for querying your Box data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Box data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To view and manage the list of actions you enabled for the Box data store, see [View and manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
