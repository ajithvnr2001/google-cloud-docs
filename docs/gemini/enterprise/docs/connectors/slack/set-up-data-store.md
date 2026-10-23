---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack/set-up-data-store/
title: Set up a Slack data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:57.521709+00:00
---

# Set up a Slack data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Slack data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Slack to Gemini Enterprise.

## Before you begin

Before setting up your Slack connection, ensure you have the following in place:

  * Grant the Discovery Engine Editor role (`roles/discoveryengine.editor`). This role is required for the user to create the data store. To grant this role, do the following: 

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

    2. Locate the user account and click edit **Edit**.
    3. Grant the `Discovery Engine Editor` role to the user. For more information, see [IAM roles and permissions](https://cloud.google.com/gemini/enterprise/docs/access-control).
  * Verify you have access to the Slack workspace you need to connect to and are signed in to your Slack account.

  * Verify that you have a [Slack plan](https://app.slack.com/plans/) that includes Slack AI search.

  * Coordinate with your organization's Slack administrator to ensure that end users can authorize their accounts without disruption. Share the official [Slack Help Center: Manage app approval for your workspace](https://slack.com/intl/en-in/help/articles/222386767-Manage-app-approval-for-your-workspace) documentation for step-by-step instructions on setting up one of the following deployment options:

    * **App Pre-Approval (Recommended):** If the **Require approved apps** setting is enabled in Slack, the administrator can pre-approve the [Gemini Enterprise app](https://gerestrictedw-qhw2314.slack.com/marketplace/A099QQHCXKN-gemini-enterprise) within the Slack App Marketplace. Members can install and use pre-approved apps immediately. See [Slack Help: Pre-approve or restrict apps](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#pre-approve-or-restrict-apps).

    * **Request-on-Demand:** If the **Require approved apps** setting is enabled in Slack, the administrator can allow members to request apps that have not been pre-approved. Members can submit requests for administrative approval. See [Slack Help: Allow members to request apps](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#allow-members-to-request-apps:%7E:text=manage%20app%20requests-,Allow%20members%20to%20request%20apps,-When%20app%20approval).

    * **Direct Installation:** If the **Require approved apps** setting is disabled in Slack, members can directly install and use the app without administrator intervention. See [Slack Help: Manage app approval for your workspace](https://slack.com/intl/en-in/help/articles/222386767-Manage-app-approval-for-your-workspace).




## Create Slack data store

To create a Slack data store, perform the following steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add**Create data store**.

  5. In the **Source** section, search for **Slack** , and click **Select**.

  6. In the **Data** section:

     1. In the **Entities to search** section, select the entities you want to search from the following:

        * Conversation
        * File
        * Message
     2. Optional: In the **Slack Team ID** field, enter your Slack team ID to restrict users from connecting only to a specific Slack workspace. For more information, see Restrict the connector to a specific Slack workspace (optional).

  7. Click **Continue**.

  8. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

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

  12. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.




On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Slack connector is ready to be used.

After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [connect it to the Slack data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store), and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Slack before executing any queries.

## Restrict the connector to a specific Slack workspace (optional)

The **Slack Team ID** field is optional. Use it to restrict end users to a specific Slack workspace and prevent them from linking personal or unauthorized accounts.

  * **If you provide a Team ID** : During authorization, the connector verifies that the connecting account belongs to the specified workspace. If it doesn't, the connection is rejected.

  * **If you leave this field blank** : Users can connect to any workspace that their account has permission to access.


**Note:** The ID always begins with the letter `T` (for example, `T01234567`).

To find the Team ID corresponding to a specific workspace, do one of the following:

  * **Web browser address bar:** Sign in to Slack in a web browser using your workspace URL (for example, `https://example.slack.com`). Once the page loads, look at the address bar: the URL has the format `https://app.slack.com/client/T01234567/C01234567`, and the segment beginning with `T` is your Team ID.
  * **Admin dashboard:** Enterprise Grid administrators can locate a specific workspace's Team ID from the admin dashboard at [admin.slack.com](https://admin.slack.com) under **Workspaces**.
  * **Slack API:** Retrieve the Team ID programmatically using Slack's [`team.info`](https://api.slack.com/methods/team.info) API method.



Copy the value and paste it into the **Slack Team ID** field to enforce the restriction.

## Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

### Query execution

After you authorize Slack and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Slack API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



### Data handling

When using third-party federated search, the following data handling rules apply:

  * Your query string is sent to the third-party search backend (Slack API).
  * These third parties may associate queries with your identity.
  * If multiple federated search data sources are enabled, the query might be sent to all of them.
  * After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies.

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Slack. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Slack API.

## What's next

  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
