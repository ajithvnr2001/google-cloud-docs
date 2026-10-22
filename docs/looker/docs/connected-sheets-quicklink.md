---
url: https://docs.cloud.google.com/looker/docs/connected-sheets-quicklink/
title: Connected Sheets quick link \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:47.298613+00:00
---

# Connected Sheets quick link  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/connected-sheets-quicklink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Connected Sheets quick link Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of the Connected Sheets **Explore actions** gear menu option, report it to [looker-connected-sheets-external@google.com](mailto:looker-connected-sheets-external@google.com).

This page describes how to enable and use the **Connected Sheets** quick link option from the **Explore actions** gear menu in Looker. The **Connected Sheets** option opens Google Sheets and initiates a connection from Google Sheets to the Looker Explore. You can then build reports, pivot tables, or charts within the newly-created Google Sheet using the fields from the selected Looker Explore.

## Before you begin

To use the **Connected Sheets** quick link, you need the following:

  * A Looker instance that has been enabled and configured for the feature by an admin as described in the Enabling and configuring the Connected Sheets quick link section on this page
  * A Looker user account with the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission for the LookML models that you want to connect to Sheets
  * A Google Account with the same email address that's associated with your Looker account

**Note:** This feature isn't available for Looker embed users.

## Using the Connected Sheets quick link from an Explore

If your Looker admin has enabled the feature, you can initiate a connection between Google Sheets and any Explore that you have access to:

  1. Log into Looker with the email address that's associated with your Google Account.

  2. In Looker, navigate to the Explore that you want to use as a data source. 

**Tip:** You don't have to create a query in the Explore; you can leave the Explore blank.
  3. Click the settings **Explore actions** gear icon and select **Connected Sheets**.

  4. The first time that you use this feature, you'll be prompted to authorize Looker to access your Google Account. Choose the Google Account that you want to use. The email address for the Google Account _must_ match the email address that's associated with your Looker user account.

  5. Review the permissions that are requested on the consent screen and click **Allow**.

  6. A new browser tab opens to Google Sheets and presents a dialog that asks if you want to link your Google Account with your Looker account. Click **Link Account**.




The Google Sheet is now connected to the Looker Explore from which you started. Within the Google Sheet, you can add fields from the Explore, create pivot tables, build charts, and apply formulas to analyze the data from your Looker Explore. 

See the [Using Connected Sheets for Looker](https://docs.cloud.google.com/looker/docs/connected-sheets#building-looker-queries-using-google-sheets) documentation page for more information on building queries in Connected Sheets.

## Enabling and Configuring the Connected Sheets quick link

To enable the **Connected Sheets** quick link in the **Explore actions** gear menu, your Looker instance must meet the following requirements:

  * Your instance must be running Looker 25.20 or later.
  * For Looker (Google Cloud core) instances, the **Connected Sheets** quick link is supported only for [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#both_public_and_private_ip_connections) network connections. Looker (Google Cloud core) [private connections (private services access)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) instances aren't supported.
  * For Looker (original) instances, the **Connected Sheets** quick link is supported only for Looker-hosted instances. [Customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted) aren't supported.



To enable the **Connected Sheets** option in the **Explore actions** gear menu on a Looker instance, an admin must perform these general tasks, which are described in the following sections:

  * Enable the Google Sheets API in the Google Cloud console.
  * Create an OAuth client in the Google Cloud console in the same Google Cloud console project where the Google Sheets API was enabled.
  * Enable and configure the **Enable Connected Sheets quick link** option on the Looker BI Connectors page.



### Enabling the Google Sheets API in the Google Cloud console

The **Connected Sheets** quick link uses the Google Sheets API, so this API must be turned on in the same project that you will use to create the OAuth client. The Google Sheets API can be enabled by an IAM user with the IAM [`roles/serviceusage.serviceUsageAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.services.enable) permission.

Perform the following steps to enable the Google Sheets API:

  1. In the Google Cloud console navigation menu, go to **APIs & Services > Library** and open the Google Sheets API.

[Go to Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com)

  2. From the Google Cloud console **Open project picker** , select the project that you want to use for connecting to Google Sheets from your Looker Explores. You must use the same Google Cloud console project throughout the Connected Sheets quick link setup procedure so that the Google Sheets API is enabled on the same project where you configure OAuth.

  3. On the Google Sheets API page, click **Enable** if the API isn't already enabled.




### Create the OAuth client

An IAM user with the [required roles](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#required-roles) must create an OAuth client. 

You can set up the OAuth client in any Google Cloud project that you want. However, the Google Sheets API **must be enabled** in this same project.

**Note:** Before you can generate your OAuth credentials, Google requires that you configure an OAuth consent screen, which lets your users choose how to grant access to their private data. If you haven't yet configured an OAuth consent screen for your selected Google Cloud console project, the Google Cloud console will display a notice with a **Configure consent screen** button. Click the button and follow the procedure on the [Configure the OAuth consent screen and choose scopes](https://developers.google.com/workspace/guides/configure-oauth-consent#configure_oauth_consent) Workspace documentation page, and then return to this procedure.

To create the client and its credentials, follow these steps:

  1. In Google Cloud console, use the Google Cloud console **Open project picker** to open the same project where you enabled the Google Sheets API.

[ Go to Google Cloud console](https://console.cloud.google.com/)

  2. Use the Google Cloud console main menu to navigate to **APIs & Services > Credentials**.

  3. From the **Credentials** page, click the **Create Credentials** drop-down menu, and then select **OAuth client ID**.

  4. In the **Application type** drop-down, select **Web application**.

  5. In the **Name** field, enter a name for your OAuth client, such as `Looker to Connected Sheets`.

  6. In the **Authorized redirect URIs** section, click the **Add URI** button. Add the following URI:
         
         https://LOOKER_INSTANCE_URL/oauth2callback
         

  7. Click the **Add URI** button to also add the following URI:
         
         https://LOOKER_INSTANCE_URL/external_oauth/redirect
         

  8. Click **Create**.

  9. After you click **Create** , an **OAuth client created** window appears. This window displays the client ID and client secret that the Google Cloud console created for your OAuth client. Copy and make note of these values, as they will be required when you configure the Enable Connected Sheets quick link option.




### Configuring the Enable Connected Sheets quick link option

After you have enabled the Google Sheets API in the Google Cloud console and created the OAuth client in the Google Cloud console, you can enable the **Connected Sheets** quick link on your Looker instance by performing these steps: 

  1. In your Looker instance, select **BI Connectors** from the **Platform** section of the **Admin** panel.
  2. Enable the **Google Sheets** toggle if it isn't already enabled. 
  3. Enable the nested toggle **Enable Connected Sheets quick link**.
  4. In the **Client ID** and **Client Secret** fields, paste the values that you copied from the Google Cloud console when you created the OAuth client in the Google Cloud console.
  5. Click **Save**.



The **Connected Sheets** option in the **Explore actions** gear menu is now set up for your Looker instance.

## Migrating from the pilot program

If your organization participated in the earlier pilot program for the **Open in Sheets** feature, your Looker instance used a centrally managed OAuth client that was provided by Looker. This setup is being deprecated in favor of the more secure and scalable method where each Looker admin configures their own OAuth client for their Looker instance. Existing pilot customers should transition to this new configuration to ensure continued functionality.

To migrate to the new version, an admin must set up your organization's own OAuth client in the Google Cloud console and then configure the credentials in the Looker BI Connectors admin page. The steps are the same as the first-time setup, which are described in these sections of this page:

  * Enable the Google Sheets API in the Google Cloud console
  * Create an OAuth client in the Google Cloud console in the same Google Cloud console project where the Google Sheets API was enabled
  * Enable and configure the **Enable Connected Sheets quick link** option on the Looker BI Connectors page



After an admin completes these steps, your instance will automatically use the new customer-managed OAuth flow. The previous pilot functionality and its reliance on the Looker-managed OAuth client will no longer be active.

## Troubleshooting

  * **Email mismatch error:** If you encounter an error during the Google authentication step, ensure that the Google Account that you're selecting has the exact same email address as your Looker user account.
  * **"Connected Sheets" option not visible:** This option will appear in the **Explore actions** gear menu only if your Looker admin has enabled the feature in the BI Connectors settings. Contact your Looker admin for assistance.
  * **Google Cloud console permissions:** The admin who configures the OAuth client and consent screen needs to have the `roles/oauthconfig.editor` and `roles/serviceusage.serviceUsageAdmin` permissions in the Google Cloud project.
  * For other issues or feedback during the Public Preview period, email [looker-connected-sheets-external@google.com](mailto:looker-connected-sheets-external@google.com).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
