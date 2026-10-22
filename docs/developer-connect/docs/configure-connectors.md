---
url: https://docs.cloud.google.com/developer-connect/docs/configure-connectors/
title: Configure account connectors \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:55.002438+00:00
---

# Configure account connectors  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/configure-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Configure account connectors Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the advanced configuration options for Developer Connect account connectors.

An account connector is a Developer Connect feature that helps you connect your Google Cloud account with your individual account on an non-Google Developer Tools provider. Users can specify the type of data to be accessed by the account connector by selecting the appropriate scopes for that connector. Once an account connector connection is created for an organization, users within that organization can use that connection to authorize their individual accounts to be used with that connection.

You can configure an account connector using either a Developer Connect pre-configured OAuth client (for example, GitHub or GitLab), or you can use your own custom OAuth client (for example, an on-premises GitHub Enterprise instance).

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Developer Connect API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Developer Connect API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com)

Enabling Developer Connect also enables the [Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/overview).

  8. Optional: Create a [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/create-key) (CMEK) for encrypting the authentication secrets that Developer Connect creates.



### Required roles

To get the permissions that you need to Create an account connector, ask your administrator to grant you the [Developer Connect OAuth Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.oauthAdmin) (`roles/developerconnect.oauthAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an account connector using available providers

The following steps describe how to create an account connector for the built-in providers. If you want create an account connector and specify your custom OAuth client, see Create an account connector using a custom OAuth client.

###  Google Cloud console 

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

  2. Select **Account connectors**.

  3. Click **Create connector**.

  4. Select the **Region** in which to create this account connector.

  5. Give the account connector a **Name**.

  6. For **Configuration type** choose **Pre-configured OAuth clients**.

  7. Select the OAuth provider.

  8. Choose whether or not to enable **Developer Connect proxy**.

With proxy enabled, Developer Connect sends Git commands or makes HTTP calls (or both) to the provider on your behalf. [Learn more](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy).

  9. Select the scopes to be granted to Developer Connect for this account connector.

Scopes determine what actions Developer Connect can perform in the selected provider's service. Scopes differ according to each provider. You must select at least one scope unless the provider has no scopes.

Depending on the provider, it's possible that no scopes are available to select. You might be able to add them manually. It's also possible that scopes are required.

  10. Click **Create** to finish creating this account connector.




###  Google Cloud CLI 

To create an account connector, run the following command:
    
    
       gcloud alpha developer-connect account-connectors create my-ac \
           --location=LOCATION \
           --provider-oauth-config-system-id=PROVIDER \
           --provider-oauth-config-scopes=SCOPES \
           --project=PROJECT_ID
    

In this command, replace the following:

  * `LOCATION` with the region in which you're creating this account connector.

  * `PROVIDER` with the SCM provider you're connecting to:

`GITHUB`, `GITLAB`, or `BITBUCKET_CLOUD`.

  * `PROJECT_ID` with the project ID (not the project number) of the project in which you're creating this account connector.




## Create an account connector using a custom OAuth client

The following steps describe how to configure an account connector to use an OAuth client you specify. If you want create an account connector with the built-in providers, see Create an account connector using available providers.

###  Google Cloud console 

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

  2. Select **Account connectors**.

  3. Click **Create connector**.

  4. Select the **Region** in which to create this account connector.

  5. Give the account connector a **Name**.

  6. For **Configuration type** choose **Custom OAuth client**.

The **Create account connector** screen displays a Redirect URI.

  7. Copy the **Redirect URI**.

The URI will have the following format:

`https://developerconnect.google.com/redirect/custom/projects/<project_number>/locations/<location>/accountConnectors/<account_connector_id>`

In this URI, `<project_number>` is the project number, NOT the project ID.

  8. Create your custom app for your chosen SCM, using the copied redirect URI, then return to this form to provide the details of your OAuth client:

     1. Select the provider.

     2. In the **Host URI** field, provide the URI for your source code management system.

     3. Enter the address for the authorization server in the **Authorization URI** field. This address takes the following form:

For GitHub Enterprise: `https://<host_name>/login/oauth/authorize` For GitLab Enterprise: `https://<host_name>/oauth/authorize` For BitBucket Data Center: `https://<host_name>/rest/oauth2/latest/authorize`

     4. In the **Token URI** field, provide the URI to use to exchange an authorization code for an access token. This address takes the following form:

For GitHub Enterprise: `https://<host_name>/login/oauth/access_token` For GitLab Enterprise: `https://<host_name>/oauth/token` For BitBucket Data Center: `https://<host_name>/rest/oauth2/latest/token`

     5. For **Client ID** , provide the client ID of your OAuth app.

     6. Provide the **Client secret** to authenticate your app with the authorization server.

     7. If your account connector will use Developer Connect proxy for issuing Git commands, select **Enable Developer Connect proxy**.

     8. For **Scopes** , select from the list of available scopes.

     9. Optionally. configure networking and security:

        1. Select whether this account connector will use the public internet or a private network.

If a private network, provide the following:

           * The CA certificate to use

           * The information for your Service Directory service:

You can identify the project for your Service Directory service, or specify the region, namespace, and service name.

        2. Enable or disable PKCE for this app.

Your OAuth service must support PKCE.

     10. Click **Create** to finish creating this account connector.




###  Google Cloud CLI 
    
    
      ```sh
      gcloud alpha developer-connect account-connectors create my-ac \
        --location=LOCATION \
        --project=PROJECT_ID \
        --custom-provider-oauth-config-system-id=PROVIDER \
        --custom-oauth-config-host-uri= HOST_URI \
        --custom-oauth-config-auth-uri=AUTH_URI \
        --custom-provider-oauth-config-scopes=SCOPES \
        --custom-oauth-config-token-uri=TOKEN_URI \
        --custom-oauth-config-client-id=CLIENT_ID \
        --custom-oauth-config-client-secret=SECRET
    
      ```
    

In this command, replace the following:

  * `LOCATION` with the region in which you're creating this account connector.

  * `PROJECT_ID` with the project ID (not the project number) of the project in which you're creating this account connector.

  * `PROVIDER` with the SCM provider you're connecting to:

`GITHUB_ENTERPRISE`, `GITLAB_ENTERPRISE`, or `BITBUCKET_DATA_CENTER`.

  * `HOST_URI` with the URL for your source code management system.

  * `AUTH_URI` with the URL used to authenticate to your chosen SCM provider.

For example:

    * GitHub Enterprise: `https://<host_name>/login/oauth/authorize`

    * GitLab Self Hosted: `https://<host_name>/oauth/authorize`

    * BitBucket Data Center: `https://<host_name>/rest/oauth2/latest/authorize`

  * `SCOPES` with a comma-separated list of all the provider OAuth scopes you want to include for this account connector. 

  * `TOKEN_URI` with the URI to use to exchange an authorization code for an access token.

  * `CLIENT_ID` with the client ID of your OAth app.

  * `SECRET` with the secret provided by the SCMS your connecting to.




## Connect your account

After you've created an account connector, you still need to connect Developer Connect to your account with the provider before you can use the account connector.

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

  2. Select **Account connectors**.

The **Account connectors** page lists all the account connectors you have in your project.

  3. Click the name of the account connector for which you want to connect your provider account.

The **Connector details** page is displayed.

  4. Click **Connect your account**.

An OAuth authentication dialog is shown.

  5. Provide the information in the dialog to authenticate to your provider.

  6. Click **Authorize**.




## Update an account connector

You can update an existing account connector, but you can only update the scopes for that connector, toggle the proxy setting on or off, or both. If you update scopes for a given account connector, all existing users of that connector are removed.

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

Developer Connect displays the **Git repositories** page.

  2. Select **Account connectors**.

The **Account connectors** page lists all the account connectors you have in your project.

  3. Click the name of the account connector you want to update.

The **Connector details** page is displayed.

  4. Click **Edit**.

  5. From the **Scopes** list, select the scopes you want to allow for this account connector.

  6. Click **Save**.




## Delete an account connector

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

Developer Connect displays the **Git repositories** page.

  2. Select **Account connectors**.

The **Account connectors** page lists all the account connectors you have in your project.

  3. From the **More** menu, select **Delete**.

The **Connector details** page is displayed.

  4. Click **Edit**.




## What's next

  * [Learn about account connectors](https://docs.cloud.google.com/developer-connect/docs/account-connectors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
