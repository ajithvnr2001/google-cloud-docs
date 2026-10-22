---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/oauth-email-google/
title: Configure your email channel for OAuth with Gmail \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:29.426951+00:00
---

# Configure your email channel for OAuth with Gmail  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/oauth-email-google/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure your email channel for OAuth with Gmail Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Google Cloud to create OAuth credentials for configuring your Contact Center AI Platform (CCAI Platform) email channel.

## Before you begin

Be sure that you have the following:

  * A Google Cloud account. For more information, see [Get started with Google Cloud](https://cloud.google.com/docs/get-started).

  * A Google Cloud project. For more information, see [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects).




Also, make sure that billing is enabled for your Google Cloud project. For more information, see [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled).

## Create OAuth credentials

You can use Google Cloud to create OAuth credentials—the client ID and client secret. If you haven't yet configured a consent screen, you need to do so before you can create OAuth credentials. For more information about OAuth, see [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2).

To create OAuth credentials and configure the consent screen, do the following:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that you want to use to create OAuth credentials.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Go to the **APIs and Services** page, and in the navigation menu, click **Credentials**.

[Credentials](https://console.cloud.google.com/apis/credentials)

  3. If you haven't yet configured your consent screen for this Google Cloud project, the **Configure consent screen** button appears. In that case, configure your consent screen using the following procedure. Otherwise, skip to step 4.

     1. Click **Configure consent screen**. The **OAuth consent screen** page displays.

     2. Depending on your use case, select **Internal** or **External** , and then click **Create**. The **OAuth consent screen** pane displays.

     3. Enter information on the **App information** page according to the on-screen instructions, and then click **Save and continue**. The **Scopes** pane displays.

     4. Click **Add or remove scopes**. The **Update selected scopes** pane appears.

     5. Select the scope or scopes appropriate for your use case, and then click **Update**.

     6. Click **Save and continue**. The **Test users** pane displays.

     7. If you want to add users to test access to your app, click **Add users**. The **Add users** pane displays.

     8. In the empty field, add one or more email addresses from Google accounts, and then click **Add**.

     9. Click **Save and continue**. The **Summary** pane displays.

     10. Review your OAuth consent screen information, and then click **Back to dashboard**.

     11. If you want to publish your app to production now, click **Publish app** , and then click **Confirm** in the confirmation dialog. Your consent screen is configured.

  4. On the navigation menu, click **Credentials**.

  5. Click **Create credentials** , and then click **OAuth client ID**.

  6. In the **Application type** field, click **Web application**.

  7. In the **Name** field, enter a name for your client.

  8. In the **Authorized JavaScript origins** area, click **Add IRI**.

  9. In the **URIs** field, enter `https://TENANT_NAME.ccaiplatform.com`, replacing `TENANT_NAME` with your tenant name.

  10. In the **Authorized redirect URIs** area, click **Add URI**.

  11. In the **URIs** field, enter `https://TENANT_NAME.ccaiplatform.com/v1/email_accounts/oauth_callback`, replacing `TENANT_NAME` with your tenant name.

  12. Click **Create**. The **OAuth client created** dialog displays.

  13. Click **Download JSON** to download to your computer a JSON file containing your client ID and client secret, and then click **OK**.

**Important:** Keep this JSON file in a safe place, as it contains your OAuth credentials.



## Get your client ID and client secret

After you create OAuth credentials, you can get your client ID and client secret at any time.

To get your client ID and client secret, do the following:

  1. In the Google Cloud console, go to the **APIs and Services** page. In the navigation menu, click **Credentials**.

[Credentials](https://console.cloud.google.com/apis/credentials)

  2. In the **OAuth 2.0 Client IDs** area, click the client that you want the client ID and client secret for. Your client ID and client secret are displayed in the **Additional information** area.




## Configure SSO settings for the email channel

Use the client ID and client secret that you created in Create OAuth credentials to configure single sign-on (SSO) settings for the email channel.

To configure SSO settings, do the following:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Developer settings**.

  2. Go to the **Email account management** pane, and then click **Manage email account**.

  3. On the **Email account management** page, click **Email SSO**.

  4. In the **Email SSO** pane, configure the settings as shown in the following list:

     * **Authorization URL**. Enter `https://accounts.google.com/o/oauth2/v2/auth?prompt=select_account consent`.

**Important:** Include the space before `consent`.
     * **Token URL**. Enter `https://oauth2.googleapis.com/token`.

     * **Client ID**. Enter the client ID that you created in Create OAuth credentials. If you didn't save your client ID, see Get your client ID and client Secret.

     * **Client secret**. Enter the client secret that you created in Create OAuth credentials. If you didn't save your client secret, see Get your client ID and client Secret.

     * **Scope**. Enter `https://mail.google.com/`.

     * **State**. Leave this field empty.

     * **Access type**. Enter `offline`.

     * **Grant type**. Enter `Authorization Code`.

     * Clear the **Include the Grant Type as part of the Authorization URL and Token URL** checkbox.

     * Select the **Include the Redirect URL as part of the Authorization URL and Token URL** checkbox, and then click **Save**. Your email channel is configured for OAuth.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
