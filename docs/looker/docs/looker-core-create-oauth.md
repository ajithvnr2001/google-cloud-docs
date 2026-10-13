---
url: https://docs.cloud.google.com/looker/docs/looker-core-create-oauth/
title: Create an OAuth client and credentials for a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:20.012171+00:00
---

# Create an OAuth client and credentials for a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-create-oauth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create an OAuth client and credentials for a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To learn how to set up OAuth for authentication, see the [Use Google OAuth for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) documentation page.

This documentation page explains how to set up your OAuth client and manually associate OAuth credentials with your instance during instance creation.

## When to create OAuth credentials

In most cases, Looker (Google Cloud core) automatically creates and assigns Looker-managed OAuth credentials by default. You need to create an OAuth client and manually associate custom OAuth credentials only in specific scenarios, depending on your instance's network connection type and authentication configuration:

  * **Private or hybrid connections with Google OAuth:** Manual OAuth setup is **required** whenever Google OAuth is used (either as primary or secondary authentication) with private or hybrid connections.
  * **Public connections with Google OAuth:** Manual OAuth setup is **not required** ; Looker (Google Cloud core) automatically assigns Looker-managed credentials by default, but you can optionally configure custom credentials.
  * **Workforce Identity Federation only:** Manual OAuth setup is **not required** across any network connection type when using Workforce Identity Federation without secondary Google OAuth.
  * **Custom domains:** If you configure a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) for an instance that uses public secure connections and Google OAuth, custom OAuth credentials are required and are configured as part of the custom domain creation process.



The following table summarizes when manual OAuth credential setup is required:

Primary authentication | Secondary authentication | Network connection type | Manual OAuth setup  
---|---|---|---  
[Google OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) | None | [Public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) | Not required. Looker (Google Cloud core) automatically assigns Looker-managed credentials.  
[Private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) | **Required.** Follow the instructions on this page.  
[Workforce Identity Federation](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity) | None | Public connections | Not required.  
[Workforce Identity Federation](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity) | [Google OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) | [Public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) | Optional. Looker (Google Cloud core) uses Looker-managed credentials by default, or you can provide custom credentials.  
  
## Required roles

To use the Google Cloud console to create and edit OAuth credentials, you need the following permissions. (To hide the list of permissions, collapse the **Required permissions** section.) 

#### Required permissions

  * clientauthconfig.*
    * clientauthconfig.brands.create
    * clientauthconfig.brands.delete
    * clientauthconfig.brands.get
    * clientauthconfig.brands.list
    * clientauthconfig.brands.update
    * clientauthconfig.clients.create
    * clientauthconfig.clients.createSecret
    * clientauthconfig.clients.delete
    * clientauthconfig.clients.get
    * clientauthconfig.clients.getWithSecret
    * clientauthconfig.clients.list
    * clientauthconfig.clients.listWithSecrets
    * clientauthconfig.clients.undelete
    * clientauthconfig.clients.update
  * oauthconfig.*
    * oauthconfig.clientpolicy.get
    * oauthconfig.testusers.get
    * oauthconfig.testusers.update
    * oauthconfig.verification.get
    * oauthconfig.verification.submit
    * oauthconfig.verification.update



You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). For more information about granting roles, see the [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) page in the Identity and Access Management (IAM) documentation.

## Before you create a Looker (Google Cloud core) instance

Before you create a Looker (Google Cloud core) instance, complete the steps that are described in these sections:

  * Generate the OAuth client ID and client secret
  * Configure the user consent screen, scopes, and test users



### Generate the OAuth client ID and client secret

First, create an OAuth client and generate the client ID and client secret for that client. These values are required during creation of the Looker (Google Cloud core) instance.

You can set up the OAuth client in any Google Cloud project you want. It doesn't need to be the same project as the Looker (Google Cloud core) instance. However, the Looker (Google Cloud core) API **must be enabled** in this project.

To create the client and its credentials, follow these steps:

  1. Navigate to the project that you want to create the OAuth client in.
  2. Navigate to **APIs & Services > Credentials**.
  3. From the **Credentials** page, click **Create Credentials**.
  4. From the drop-down menu, select **OAuth client ID**.
  5. In the **Application type** drop-down, select **Web application**.
  6. In the **Name** field, enter a name for your OAuth client.
  7. At this point, you **don't** need to add URIs in the **Authorized JavaScript origins** or **Authorized redirect URIs** sections.
  8. Click **Create**.



After you click **Create** , an **OAuth client created** window appears. This window displays the client ID and client secret created for your OAuth client. These values will be required when you [create the Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#oauth).

Optionally, click **Download JSON** to download the credential information in a JSON file. To close the window, click **OK**.

### Configure the user consent screen, scopes, and test users

Next, you may want to configure the consent screen. The consent screen is shown to a user of the Looker (Google Cloud core) instance at their first login and at any point when their authorization [expires](https://support.google.com/a/answer/7576830) or is [revoked by the user](https://developers.google.com/identity/gsi/web/guides/revoke).

Follow the instructions on the [Configure the OAuth consent screen and choose scopes](https://developers.google.com/workspace/guides/configure-oauth-consent#configure_oauth_consent) documentation page. While configuring your screen, complete the following settings as described:

  * In the **Branding** section, under **Authorized domains** , the domain must match the domain of the Looker (Google Cloud core) instance that uses the OAuth credentials. If you are going to create a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) for your Looker (Google Cloud core) instance and know the domain that you will assign to it, you can enter it now. Otherwise, you can leave this field empty; it will be automatically populated when you add the authorized redirect URI after the Looker (Google Cloud core) instance is created.

  * In the **Audience** section, under **User Type** , select one of the following:

    * **Internal** : This setting is the default. Only users within your [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) can access the instance once they are [added through IAM](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#adding-users).
    * **Make external** : Users with any kind of [Google Account](https://www.google.com/account/about/) can access the instance once they are [added through IAM](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#adding-users).
**Note:** If you want a user such as Google Support to access your instance using OAuth and IAM, **User Type** must be set to **External** , and the Support user must be [added through IAM](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication). You can edit the **User Type** setting at any point.



## During Looker (Google Cloud core) instance creation

When you are [creating the Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create), add the OAuth client ID and client secret in the [**OAuth Application Credentials** section](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#oauth). You cannot create an instance without OAuth credentials. Find the OAuth client ID and client secret by navigating to the OAuth client in the Google Cloud console.

## After you create a Looker (Google Cloud core) instance

Complete the following instructions to finish configuration. When you add an authorized redirect URI, it will be added to your OAuth consent screen as an authorized domain.

### Add the authorized redirect URI to the OAuth client

If you haven't done so already, follow these steps to enter the URL of the newly created Looker (Google Cloud core) instance into the OAuth client.

  1. After you have created a Looker (Google Cloud core) instance, find and copy the URL for the instance. You can find the URL on the [**Instances** page](https://docs.cloud.google.com/looker/docs/looker-core-view-console).

**Note:** If you are setting up a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) for your instance, be sure to complete that setup before copying the URL. Once you add the custom domain to the OAuth client, users will no longer be able to log in to the autogenerated instance URL that was granted when the instance was created, even if that domain is also in the OAuth client.
  2. In the Google Cloud console, navigate to **APIs & Services > Credentials**.

  3. Under the **OAuth 2.0 Client IDs** heading, click the name of the client you created.

  4. In the **Authorized redirect URIs** section, click **Add URI**.

  5. Paste the URL of the Looker (Google Cloud core) instance into the **URIs** field. Add `/oauth2callback` to the end of the URL. For example: `https://uuid.looker.app/oauth2callback`.

If you are going to set up [OAuth authorization for BigQuery](https://docs.cloud.google.com/looker/docs/looker-core-dialects#oauth-options), you can also add a second redirect URI that points to the URL of the Looker (Google Cloud core) instance followed by `/external_oauth/redirect` added to the end of the URL. For example: `https://uuid.looker.app/external_oauth/redirect`.

  6. Click **Save**.




It may take from five minutes to a few hours for the update to take effect.

### Manage users

Once the OAuth client is configured and the Looker (Google Cloud core) instance is [created](https://docs.cloud.google.com/looker/docs/looker-core-instance-create), you can sign in to the instance using OAuth. Then, you can [choose the authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication) for your instance.

If using OAuth as your primary authentication method, complete the steps as described on the [Use Google OAuth for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) documentation page to complete OAuth setup for user authentication.

Once your authentication method is set up, you can add or remove users through your identity provider and [manage them within Looker](https://docs.cloud.google.com/looker/docs/looker-core-user-management).

### View the type of OAuth credentials for your instance

OAuth credentials aren't listed directly on the [instance configuration page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#instance_tabs) of the Google Cloud console. Click **Edit** on the instance configuration page to see the **OAuth application credentials** section.

If the OAuth credentials are set to **Looker managed** , Looker (Google Cloud core) assigns a Looker-managed OAuth credentials for your instance during instance creation and the client ID and client secret aren't shown.

If the OAuth credentials are set to **Manual** , manual OAuth credentials were added to your instance either during or after instance creation. The client ID and client secret aren't shown; instead, the section displays `****` placeholders.

### Edit the OAuth client for a Looker (Google Cloud core) instance

If you want to, you can add, edit, or change OAuth credentials for your Looker (Google Cloud core) instance by following these steps:

  1. Set up the new client or credentials.
  2. In the Google Cloud console, from the **Instances** page, click on an instance's name to open the **DETAILS** page.
  3. From the **DETAILS** page, click **Edit**.
  4. On the **Edit Looker (Google Cloud core) instance** page, navigate to the **OAuth application credentials** section and select **Manual** , if it is not already selected.
  5. Enter the new values in the **OAuth Client ID** and **OAuth Client Secret** fields.
  6. Click **Save**.



If your OAuth application credentials are set to **Looker managed** , you can't add or edit credentials. Switch to the **Manual** setting for credentials to edit or add them.

## What's next

  * [Create a public IP Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create)
  * [Create a private connections (private services access) Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
