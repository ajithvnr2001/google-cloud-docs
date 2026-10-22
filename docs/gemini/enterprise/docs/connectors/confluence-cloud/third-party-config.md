---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config/
title: Confluence Cloud configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:43.181721+00:00
---

# Confluence Cloud configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Confluence Cloud configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure your Confluence Cloud instance before creating the Confluence Cloud data store.

## Set up authentication and permissions

You need to set up authentication and permissions in the Atlassian administrator account center. This is crucial for allowing the connector to access and synchronize data. The Confluence Cloud connector supports various authentication methods, such as OAuth client credentials or API tokens.

### Create an OAuth 2.0 app

To create an OAuth 2.0 app for authentication, follow these steps to set up the application in your Atlassian Developer Console and obtain the necessary client ID and client secret.

#### Verify Confluence organization administrator access

To verify Confluence organization administrator access, do the following:

  1. Sign-in to [Atlassian](https://id.atlassian.com/login) with your user credentials.

  2. Select the **Confluence** app.

  3. Click **Settings**.

If you see the **System** option under **Confluence settings** , you have Confluence _organization administrator_ access. Otherwise, request your Confluence organization administrator to provide access.




#### Create OAuth 2.0 app

To create an OAuth 2.0 app, do the following:

  1. Sign in to the [Atlassian Developer Console](https://developer.atlassian.com).

  2. Click the profile icon and select **Developer console**.

  3. In the **Console** page, click **Create** and select **OAuth 2.0 Integration**.

  4. In the app creation page, do the following: 

     1. Enter a name for the app.

     2. Select the checkbox to agree to Atlassian's developer terms.

     3. Click **Create**.

  5. In the app page, do the following:

     1. From the navigation menu, click **Authorization**.

     2. In the **Authorization type** table, select **Add** for **OAuth 2.0 (3LO)**.

  6. In the **Callback URL** field, enter the URL as per the connection mode of your data store.

     * Data ingestion and actions: `https://vertexaisearch.cloud.google.com/console/oauth/confluence_oauth.html`

     * Federated search and actions: `https://vertexaisearch.cloud.google.com/oauth-redirect`

  7. Click **Save changes**.




### Obtain client ID and client secret

To obtain the client ID and client secret, do the following:

  1. In the app page, from the navigation menu click **Distribution**.
  2. In the **Distribution** page, do the following: 

     1. In the **Distribution controls** section, select **Edit**.
     2. In the **Distribution status** section, select **Sharing** to enable editing other fields.
     3. Enter information in the following mandatory fields: 
        1. For **Vendor** , enter `Google`.
        2. For **Privacy policy** , enter `https://policies.google.com`.
        3. For **Does your app store personal data?** , select **Yes**.
        4. Select **I confirm that I've implemented the personal data reporting API** checkbox.
     4. Click **Save changes**.
  3. In the app page, do the following:

     1. From the navigation menu, click **Settings**.
     2. From the settings page, copy your **Client ID** and **Client secret**.



### Obtain an instance ID and instance URL

  1. Obtain the instance ID:

     1. Open a new tab, copy the instance URL, and append `/_edge/tenant_info` to the instance URL. For example, `https://YOUR_INSTANCE.atlassian.net/_edge/tenant_info`.
     2. Navigate to the link to find the `cloudId` value. The `cloudId` is your instance ID.
  2. Obtain the instance URL:

     1. Go to [atlassian.net](https://atlassian.net) and sign in with your _administrator_ account.
     2. Select the app you want to sync. For example, sync the first app.
     3. Find the instance URL (the subdomain in the address bar).



### Grant administrator roles

To grant the Confluence _administrator_ the Discovery Engine Editor role in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.
  2. Navigate to **IAM**.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  3. Locate the user account that has _administrator_ access in Confluence and click the **Edit** icon edit.

  4. Grant the Discovery Engine Editor role to the _administrator_.




To grant a user an _administrator_ role in Atlassian, do the following:

  1. Sign in to [Atlassian](https://atlassian.com) using an _organization administrator_ account.

  2. Click the menu icon and select your organization. Alternatively, you can go to [admin.atlassian.com](https://admin.atlassian.com).

  3. On the **Admin** page, click the product and select the **Manage users** button.

  4. Click **Groups** under **User management**.

  5. On the **Groups** page:

     1. Click **Create group**.
     2. Enter a name for the group.



This group receives permissions required by the connector. Users added to this group inherit these permissions. The connector uses this group to authenticate and fetch documents.

  1. On the **Group page** , click **Add product**.

  2. Select **User access admin** as the role for **Confluence**.

  3. Select **Product admin** as the role for **Confluence administration**.

  4. Click **Grant Access**.

  5. Click **Add group members** to add a user account or group members that the connector uses to authenticate and access the required resources.




### Configure minimum application scopes

To configure OAuth 2.0 and retrieve the required credentials for your Confluence connector setup, do the following:

  1. To configure scopes, do the following:

     1. Click **Permissions**.
     2. Add the necessary Confluence API scopes:

        1. Go to **Confluence API**.
        2. Click **Add > Configure**.
        3. Go to the **Granular scopes** tab and click **Edit scopes**. For federated search, some scopes might be listed under **Classic Scopes**.

        4. Select the required scopes according to your connection mode.

**Note:** The following table outlines the permissions required for each connection mode. If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the permissions listed in the **Actions** row. 

Usage reason | Permission | Description  
---|---|---  
**Data ingestion** | `read:content-details:confluence` | Allows the data store to read content details in Confluence.  
`read:attachment:confluence` | Allows the data store to download and read attachments.  
`read:comment:confluence` | Allows the data store to read comments.  
`read:page:confluence` | Allows the data store to read pages.  
`read:whiteboard:confluence` | Allows the data store to read whiteboards.  
`read:space:confluence` | Allows the data store to read spaces.  
`read:group:confluence` | Allows the data store to read groups.  
`read:user:confluence` | Allows the data store to read users.  
`read:content.metadata:confluence` | Allows the data store to read content metadata.  
`read:configuration:confluence` | Allows the data store to read configurations.  
**Federated search** | `search:confluence` | Allows the data store to perform search queries in Confluence.  
**Actions** | `write:page:confluence` | Allows the data store to create and update pages in Confluence.  
`write:attachment:confluence` | Allows the data store to upload attachments to Confluence pages.  
`write:blogpost:confluence` | Allows the data store to create and update Confluence blog posts.  
`write:space:confluence` | Allows the data store to create and update Confluence spaces.  
`write:confluence-space` | Allows the data store to manage Confluence space information, including create, update, and delete operations.  
`write:confluence-content` | Allows the data store to write content in Confluence.  
`write:confluence-file` | Allows the data store to upload attachments to Confluence.  
`read:attachment:confluence` | Allows the data store to download and read attachments.  
`read:blogpost:confluence` | Allows the data store to read blog posts.  
`read:comment:confluence` | Allows the data store to read comments.  
`read:configuration:confluence` | Allows the data store to read configurations.  
`read:confluence-content.all` | Allows the data store to read all Confluence content.  
`read:confluence-space.summary` | Allows the data store to read space summaries.  
`read:content-details:confluence` | Allows the data store to read content details in Confluence.  
`read:content.metadata:confluence` | Allows the data store to read content metadata.  
`read:group:confluence` | Allows the data store to read groups.  
`read:page:confluence` | Allows the data store to read pages.  
`read:space:confluence` | Allows the data store to read spaces.  
`read:space-details:confluence` | Allows the data store to read space details.  
`read:task:confluence` | Allows the data store to read tasks.  
`read:user:confluence` | Allows the data store to read users.  
`read:whiteboard:confluence` | Allows the data store to read whiteboards.  
`search:confluence` | Allows the data store to perform search queries in Confluence.  
     3. Add User Identity API scopes. The `read:me` scope is required when Actions are enabled for the data store:

        1. Go to **User Identity API**.
        2. Click **Add > Configure**.
        3. Go to the **Granular scopes** tab and click **Edit scopes**.
        4. Select the `read:me` scope.
Usage reason | Permission | Description  
---|---|---  
**Actions** | `read:me` | Allows the data store to read current user information.  
     4. Confirm that all the scopes are selected and save your changes.




### Set up an API token in Confluence

If you plan to use an API token for authentication, you must create an API token without scopes. This data store doesn't support API tokens with scopes.

  1. Sign in to [Atlassian Console](https://id.atlassian.com/manage-profile/security/api-tokens).
  2. Click **Create API token**.
  3. Enter a name for the API token.
  4. Select an expiration date for the API token. The token expiration period ranges from 1 to 365 days.
  5. Click **Create**.
  6. Save the token for later use.



### Manage user visibility

To make the user's email visible to anyone in the Atlassian account, follow these steps:

  1. Sign in to the [Atlassian Developer Console](https://developer.atlassian.com).

  2. Click the profile icon and select **Developer console**.

  3. Click the user profile icon and select **Manage account**.

  4. Navigate to **Profile and visibility**.

  5. Go to **Contact** and set the **Who can see this** as **Anyone**.




To make the user's email visible to anyone in Confluence, follow these steps:

  1. Sign in to [Atlassian](https://id.atlassian.com/login) with your user credentials.

  2. Select a Confluence app.

  3. Click **Settings** > **System**.

  4. Select **General Configuration** in the left pane.

  5. Click **Edit Settings**.

  6. For **User email visibility** , select **Public**.

  7. Click **Update**.




## Install and configure User Identity Accessor for Confluence Cloud

If user email addresses aren't publicly accessible by default due to privacy settings in Confluence Cloud, you must install the **User Identity Accessor for Confluence Cloud** app to securely retrieve user email addresses. If user email addresses are already publicly visible, you might not need to install the app. For more information about restricted email visibility, see [Manage user visibility and grant roles](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#manage-users).

### Roles and permissions

To install and configure the **User Identity Accessor for Confluence Cloud** app, you must have the appropriate administrative role and grant the required app-level permissions.

  * **Required role** : You must be a `Confluence Site administrator` to install and configure the app.
  * **App-level permissions** : You must grant the following permissions during the app installation: 
    * `Read Email Address`: Allows the app to securely retrieve user email addresses, even when profile visibility is restricted.
    * `App Storage scope`: Enables the app to read and write to its storage device.



### Install User Identity Accessor for Confluence Cloud

To install the **User Identity Accessor for Confluence Cloud** app on your Confluence site, follow these steps:

  1. Navigate to [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1238254/user-identity-accessor-for-confluence-cloud).
  2. Click **Get it now**.

![configure-uia-button-conf](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/user-identity-accessor-conf.png)Get it now 
  3. From the **Select a site** list, select the Confluence site where you want to install the app.

**Note:** You must have administrator privileges for the selected Confluence site to install the app.
  4. Click **Review** to authorize the required permissions and agree to the terms and conditions.

  5. Click **Get it now** to complete the app installation.

Upon successful installation, a confirmation message appears: "Your app has been added to your instance and is ready for use."




### Configure User Identity Accessor for Confluence Cloud

After you've installed the **User Identity Accessor for Confluence Cloud** app, configure an API key that your external system (for example, your Confluence Cloud data store) uses to securely call the app's webtrigger to fetch emails.

#### Access the configuration page

To access the **User Identity Accessor for Confluence Cloud** app's configuration page in Confluence Cloud, follow these steps:

  1. In your Confluence Cloud instance, click the **Settings** ⚙️ icon in the navigation menu.
  2. Select **Apps** from the menu.
  3. On the **Apps administration** page, locate your app, **User Identity Accessor for Confluence Cloud** , in the **Manage apps** list.
  4. Click **Configure** or the link associated with your app. The app's dedicated configuration page opens within Confluence.



#### Set up the API key

To set up the API key on the configuration page, follow these steps:

  1. In the **API Key Configuration** section, specify the secret key for authenticating requests to the app's webtrigger. You can authenticate requests using _either_ of the following methods:

     * **Enter your own key** : Type or paste your own strong, unique API key into the API Key field. Use a key of at least 20–30 characters with a mix of uppercase letters, lowercase letters, numbers, and symbols.

     * **Generate a key** : Click the **Generate New Key** button. The system generates and displays a strong, random key in the field.

**Important** : Immediately copy the API key displayed in the field. For security reasons, you might be unable to view the full key again after saving or navigating away. If lost, you need to set or generate a new one.

  2. Click **Save API Key**. A success message confirms that the key is securely saved.




> **Note:** The API key generated or created in this section serves as the value for the **Confluence Identity Sync Forge Client Secret** field in the **Advanced Options** section during [data store setup](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store#create-data-store).

#### Test the app configuration

Verify that the User Identity Accessor for Confluence Cloud app is configured correctly by sending a request from your external system and confirming that user email addresses are returned successfully.

##### Get the webtrigger URL

  1. On the **Apps administration** page, locate the **Webtrigger URL** section, which displays the unique URL specific to your Confluence site and this app installation: 
     * Your external system must call this URL to request user emails. For example, `https://YOUR_INSTANCE_ID.hello.atlassian-dev.net/x1/WEBTRIGGER_ID`, where `YOUR_INSTANCE_ID` is your Confluence Cloud instance identifier and `WEBTRIGGER_ID` is the unique identifier for the webtrigger endpoint generated for your app.
  2. Click the **Copy URL** button or copy the entire URL.



##### Configure your external system

  * Configure your external system that needs to fetch Confluence user emails with the API key and webtrigger URL obtained in the previous steps.

    * **Endpoint URL** : The webtrigger URL you copied.
    * **HTTP Method** : `POST`
    * **Required Headers** :

      * **Content-Type** : `application/json`
      * **X-Api-Key** : `YOUR_API_KEY`

Replace `YOUR_API_KEY` with the API key you set or generated in the [Set up the API key](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#set-up-api-key) section.




##### Example curl command

This example demonstrates calling the **User Identity Accessor for Confluence Cloud** webtrigger, which accepts an array of account IDs and returns the email addresses.
    
    
    curl --location --request POST 'https://YOUR_INSTANCE_ID.hello.atlassian-dev.net/x1/ENDPOINT_PATH' \
    --header 'X-Api-Key: YOUR-API-KEY' \
    --header 'Content-Type: application/json' \
    --data-raw '{
       "accountIds": [
           "ACCOUNT_ID_1",
           "ACCOUNT_ID_2"
       ]
    }'
    

Replace:

  * `YOUR_INSTANCE_ID` with your Confluence Cloud instance ID
  * `ENDPOINT_PATH` with the API endpoint path
  * `YOUR_API_KEY` with the API key you set or generated in the [Set up the API key](https://docs.cloud.google.com/gemini/enterprise/docs/confluence-cloud/third-party-config#set-up-api-key) section
  * `ACCOUNT_ID` with Atlassian account IDs you want to target



##### Expected response
    
    
    [{"accountId":"ACCOUNT_ID_1","emailAddress":"EMAIL_ADDRESS_1"},
     {"accountId":"ACCOUNT_ID_2","emailAddress":"EMAIL_ADDRESS_2"}]
    

Replace:

  * `ACCOUNT_ID_X` with actual Atlassian account IDs
  * `USER_EMAIL_X` with user email addresses returned from your API call



#### Implement security best practices

To confirm the security of your API key, follow these recommendations:

  * Store the API key securely within your Confluence Cloud data store's configuration.
  * Verify that all communication with the webhook URL occurs over HTTPS. This is the default for **User Identity Accessor for Confluence Cloud** webtriggers.



### Support for User Identity Accessor for Confluence Cloud

Support offerings are available from Google for the **User Identity Accessor for Confluence Cloud** app that can include maintenance and regular updates to keep the app up to date. If you encounter any issues or have questions specific to the app functionality, contact [Google Cloud Support](https://support.cloud.google.com/portal/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
