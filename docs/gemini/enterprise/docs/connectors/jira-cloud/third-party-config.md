---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config/
title: Jira Cloud configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:38.964507+00:00
---

# Jira Cloud configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Jira Cloud configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party configuration before creating the Jira Cloud data store.

## Set up authentication and permissions

You need to set up authentication and permissions in the Atlassian administrator account center. This is crucial for allowing the connector to access and synchronize data. The Jira Cloud connector supports various authentication methods, such as OAuth client credentials or API tokens.

### Create an OAuth 2.0 app

To create an OAuth 2.0 app for authentication, follow these steps to set up the application in your Atlassian Developer Console and obtain the necessary client ID and client secret.

#### Verify Jira organization administrator access

To verify Jira organization administrator access, do the following:

  1. Sign-in to [Atlassian](https://id.atlassian.com/login) with your user credentials.

  2. Select the **Jira** app.

  3. Click **Settings**.

If you see the **System** option under **Jira settings** , you have Jira _organization administrator_ access. Otherwise, request your Jira organization administrator to provide access.




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

     3. In the **Callback URL** field, enter the URL as per the connection mode of your data store.

        * Federated search and actions: `https://vertexaisearch.cloud.google.com/oauth-redirect`.

        * Data ingestion: `https://vertexaisearch.cloud.google.com/console/oauth/jira_oauth.html`.

**Note:** Actions always use `https://vertexaisearch.cloud.google.com/oauth-redirect`. If you use the same OAuth 2.0 app for both data ingestion and actions, you must register both callback URLs in this app. If a required URL is missing, you'll see a `redirect_uri is not registered for client` error when authorizing.
  6. Click **Save changes**.




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
        4. Select **I confirm that I've implemented the personal data reporting API** checkbox. For more information, see [Personal data reporting API](https://developer.atlassian.com/cloud/jira/platform/user-privacy-developer-guide/).
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



### Obtain project key

To obtain the project key, do the following:

  1. Sign in to your [Jira Cloud account](https://www.atlassian.com/software/jira).

  2. From the navigation menu, select **Spaces**.

  3. Select the project for which you need the project ID.

  4. Open any issue within that project and click  more_horiz **Actions**.

  5. Click **Export XML** and download the file.

  6. Open the downloaded XML file and search for the tag containing `project id`. Copy the value associated with this tag for later use.




### Grant administrator roles

To grant the Jira _administrator_ the Discovery Engine Editor role in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.
  2. Navigate to **IAM**.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  3. Locate the user account which has _administrator_ access in Jira and click edit **Edit**.

  4. Grant the Discovery Engine Editor role to the _administrator_.




To grant a user an _administrator_ role in Atlassian, do the following:

  1. Sign in to [Atlassian](https://atlassian.com) using an _organization administrator_ account.

  2. Click the menu icon and select your organization. Alternatively, you can go to [admin.atlassian.com](https://admin.atlassian.com).

  3. On the **Admin** page, click the product and select the **Manage users** button.

![manage-users](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/manage-users.png)Manage users 
  4. Click **Groups** under **User management**.

  5. On the **Groups** page:

     1. Click **Create group**.
     2. Enter a name for the group.
![create-group](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/create-group.png)Create group 



This group receives permissions required by the connector. Users added to this group inherit these permissions. The connector uses this group to authenticate and fetch documents.

  1. On the **Group page** , click **Add product**.

  2. Select **User access admin** as the role for **Jira**.

  3. Select **Product admin** as the role for **Jira administration**.

![jira-user-access-admin](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/jira-user-access-admin.png)Jira user access administrator 
  4. Click **Grant Access**.

  5. Click **Add group members** to add a user account or group members that the connector uses to authenticate and access the required resources.

![add-group-members](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/add-group-members.png)Add group members 



### Manage user visibility

To make the user's email visible to anyone in the Atlassian account, do the following:

  1. Sign in to the [Atlassian Developer Console](https://developer.atlassian.com).

  2. Click the profile icon and select **Developer console**.

  3. Click the user profile icon and select **Manage account**.

![manage-account](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/manage-account.png)Manage account 
  4. Navigate to the **Profile and visibility**.

![profile-visibility](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/profile-visibility.png)Profile and visibility 
  5. Go to **Contact** and set the **Who can see this** as **Anyone**.

![contact](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/contact.png)Contact 



To make the user's email visible to anyone in Jira, do the following:

  1. Sign in to [Atlassian](https://id.atlassian.com/login) with your user credentials.

  2. Select a Jira app.

  3. Click **Settings** > **System**.

  4. Select **General Configuration** in the left pane.

  5. Click **Edit Settings**.

  6. For **User email visibility** , select **Public**.

![select email visibility](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/select-email-visibility.png)Select email visibility 
  7. Click **Update**.




## Configure minimum application scopes

To perform the defined [actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud#supported-actions), you need to set up the following permissions for the Jira Cloud connector in the Atlassian platform.

  1. On the application page, click **Permissions**.

  2. Go to **Jira API** and click **Add**.

**Note:** After adding the Jira API, the **Configure** button might take a moment to appear. If it doesn't show up immediately, try refreshing the page or waiting a few seconds.
  3. Click **Configure**.

  4. Go to the **Classic scopes** tab.

  5. Click **Edit scopes** and select the classic scopes as per your requirement from the following table:

Connection mode | Permission | Purpose  
---|---|---  
**Federated search and actions** | `read:jira-user`, `read:jira-work` | Allows the assistant to fetch and display search results and user details in real-time.  
`write:jira-work` | Allows the assistant to modify work items (for example, updating issue fields), manage comments or issues, and upload attachments.  
`manage:jira-project` | Allows the assistant to manage Jira project settings and create new project-level objects such as versions and components. Required for the create and update project actions.  
**Federated search only** | `read:jira-user`, `read:jira-work` | Allows the assistant to search for and view issues, projects, and user profiles.  
**Data ingestion and actions** | `read:jira-work` | Allows the assistant to perform broad data crawling and indexing of work items.  
`write:jira-work` | Allows the assistant to perform write actions (creation, updates, comments, and attachments) on work items within the ingested environment.  
**Data ingestion** | `read:jira-work` | Allows the assistant to crawl and index Jira content for search availability.  
  6. Confirm all the scopes are selected, and click **Save**.

  7. Go to the **Granular scopes** tab.

  8. Click **Edit scopes** and select the granular scopes as per your requirement from the following table:


Connection mode | Permission | Purpose  
---|---|---  
**Federated search and actions** | `write:comment:jira` | Allows the data store to post new comments or replies directly from the Gemini Enterprise interface.  
`write:issue:jira` | Allows the data store to create new issues or perform major edits to existing ones.  
`write:attachment:jira` | Allows the data store to upload attachments to Jira issues.  
`write:project:jira` | Allows the data store to create and update Jira projects.  
`write:issue-worklog:jira` | Allows the data store to create and update issue worklogs.  
`write:issue-link:jira` | Allows the data store to create and update links between issues.  
`read:issue:jira` | Allows the data store to read issues.  
`read:issue-type:jira` | Allows the data store to read issue types.  
`read:comment:jira` | Allows the data store to read comments.  
`read:comment.property:jira` | Allows the data store to read issue comment properties.  
`read:project:jira` | Allows the data store to read projects.  
`read:priority:jira` | Allows the data store to read priorities.  
`read:issue.transition:jira` | Allows the data store to read issue transitions.  
`read:issue-meta:jira` | Allows the data store to read issue metadata.  
`read:board-scope.admin:jira-software` | Allows the data store to read the configuration, project features, filters, properties, and quick filters for a board.  
`read:board-scope:jira-software` | Allows the data store to read boards, issues on a board, issues from a backlog, reports, and versions.  
`read:issue-details:jira` | Allows the data store to read issue details.  
`read:jql:jira` | Allows the data store to read Jira Query Language (JQL) queries.  
**Federated search only** | `read:issue:jira` | Allows the data store to read issues.  
`read:issue-type:jira` | Allows the data store to read issue types.  
`read:comment:jira` | Allows the data store to read comments.  
`read:comment.property:jira` | Allows the data store to read issue comment properties.  
`read:project:jira` | Allows the data store to read projects.  
`read:priority:jira` | Allows the data store to read priorities.  
`read:issue.transition:jira` | Allows the data store to read issue transitions.  
`read:issue-meta:jira` | Allows the data store to read issue metadata.  
`read:board-scope.admin:jira-software` | Allows the data store to read the configuration, project features, filters, properties, and quick filters for a board.  
`read:board-scope:jira-software` | Allows the data store to read boards, issues on a board, issues from a backlog, reports, and versions.  
`read:sprint:jira-software` | Allows the data store to read sprint details.  
`read:issue-details:jira` | Allows the data store to read issue details.  
`read:jql:jira` | Allows the data store to read Jira Query Language (JQL) queries.  
**Data ingestion and actions** | `read:user:jira`, `read:group:jira`, `read:avatar:jira` | Allows syncing user/group metadata and displaying user profiles.  
`read:issue-security-level:jira`, `read:issue-security-scheme:jira` | Allows for access control, ensuring the ingested data respects Jira's security boundaries.  
`read:audit-log:jira` | Allows tracking changes and performing incremental syncs to keep ingested data up to date.  
`write:comment:jira` | Allows adding comments to issues using the data store.  
`write:issue:jira` | Allows the assistant to create or modify issues.  
**Data ingestion** | `read:user:jira`, `read:group:jira`, `read:avatar:jira` | Allows crawling and indexing Jira content and user relationships.  
`read:issue-security-level:jira`, `read:issue-security-scheme:jira` | Allows mapping permissions so only authorized users can search the ingested data.  
`read:audit-log:jira` | Allows the sync engine to identify which items have been updated or deleted.  
`read:sprint:jira-software` | Allows the data store to read sprint details.  
  
9\. Confirm all the scopes are selected, and click **Save**.

**Note:** If you want to skip actions and use the data store for search, you can limit the permissions to just `read` permissions. `write` permissions are required only to perform the actions mentioned in [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud#supported-actions).

## Install User Identity Accessor

To install the **User Identity Accessor for Jira Cloud** app on your Jira Cloud site, follow these steps:

  1. Navigate to [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1238248/user-identity-accessor-for-jira-cloud).
  2. Click **Get it now**.

![configure-uia-button-jira](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/user-identity-accessor-jira.png)Get it now 
  3. From the **Select a site** list, select the Jira site where you want to install the app.

**Note:** You must have administrator privileges for the selected Jira site to install the app.
  4. Click **Review** to authorize the required permissions and agree to the terms and conditions.

  5. Click **Get it now** to complete the app installation.

Upon successful installation, a confirmation message appears: "Your app has been added to your instance and is ready for use."




## Configure User Identity Accessor

After you've installed the **User Identity Accessor for Jira Cloud** app, configure an API key that your external system (for example, your Jira Cloud Connector) uses to securely call the app's web trigger to fetch emails.

### Access the configuration page

To access the **User Identity Accessor for Jira Cloud** app's configuration page, do the following:

  1. In your Jira Cloud instance, click the **Settings** ⚙️ icon in the navigation menu.
  2. Select **Apps** from the menu.
  3. On the **Apps administration** page, locate your app, **User Identity Accessor for Jira Cloud** , in the **Manage apps** list.
  4. Click **Configure** or the link associated with your app. The app's dedicated configuration page opens within Jira Cloud.

![configure-uia-button-jira](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/configure-uia-button-jira.png)Configure the User Identity Accessor for Jira Cloud app 



### Set up the API key

To set up the API key on the configuration page, do the following:

  1. In the **API Key Configuration** section, specify the secret key for authenticating requests to the app's web trigger. You can authenticate requests using _either_ of the following methods:

     * **Enter your own key** : Type or paste your own strong, unique API key into the **API Key** field. Use a key of at least 20–30 characters with a mix of uppercase letters, lowercase letters, numbers, and symbols.

![save-key](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/save-key.png)Enter your own key 
     * **Generate a key** : Click the **Generate New Key** button. The system generates and displays a strong, random key in the field. ![generate-key](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/jira-confluence-connector-images/generate-key.png)Generate a key 

**Important** : Immediately copy the API key displayed in the field. For security reasons, you might be unable to view the full key again after saving or navigating away. If lost, you need to set or generate a new one.

  2. Click **Save API Key**. A success message confirms that the key is securely saved.




> **Note:** The API key generated or created in this section serves as the value for the **Jira Identity Sync Forge Client Secret** field in the **Advanced Options** section during [Connector setup](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store#create-data-store).

### Test the app configuration

Verify if the **User Identity Accessor for Jira Cloud** app is configured correctly by sending a request from your external system and confirming that user email addresses are returned successfully.

#### Get the web trigger URL

  1. On the **Apps administration** page, locate the **Webtrigger URL** section, which displays the unique URL specific to your Jira site and this app installation: 
     * Your external system must call this URL to request user emails.
     * URL example: `https://YOUR_INSTANCE_ID.hello.atlassian-dev.net/x1/WEBTRIGGER_ID`, where `YOUR_INSTANCE_ID` is your Jira Cloud instance identifier and `WEBTRIGGER_ID` is the unique identifier for the web trigger endpoint generated for your app.
  2. Click the **Copy URL** button or copy the entire URL.



#### Configure your external system

  * Configure your external system that needs to fetch Jira user emails with the API key and web trigger URL obtained in the previous steps.

  * **Endpoint URL** : The web trigger URL you copied.

  * **HTTP Method** : `POST`

  * **Required Headers** :

    * **Content-Type** : `application/json`
    * **X-Api-Key** : `YOUR_API_KEY`

Replace `YOUR_API_KEY` with the API key you set or generated in the Set up the API key section.




#### Example curl command

This example demonstrates calling the **User Identity Accessor for Jira Cloud** web trigger, which accepts an array of account IDs and returns the email addresses.
    
    
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

  * `YOUR_INSTANCE_ID` with your Jira Cloud instance ID
  * `ENDPOINT_PATH` with the API endpoint path
  * `YOUR_API_KEY` with the API key you set or generated in the Set up the API key section
  * `ACCOUNT_ID` with Atlassian account IDs that you want to target



##### Expected response
    
    
    [{"accountId":"ACCOUNT_ID_1","emailAddress":"EMAIL_ADDRESS_1"},
     {"accountId":"ACCOUNT_ID_2","emailAddress":"EMAIL_ADDRESS_2"}]
    

Replace:

  * `ACCOUNT_ID_X` with actual Atlassian account IDs
  * `USER_EMAIL_X` with user email addresses returned from your API call



#### Implement security best practices

To confirm the security of your API key, follow these recommendations:

  * Store the API key securely within your Jira Cloud Connector's configuration.
  * Verify that all communication with the webhook URL occurs over HTTPS. This is the default for **User Identity Accessor for Jira Cloud** web triggers.



### Support for User Identity Accessor for Jira Cloud

Support offerings are available from Google for the **User Identity Accessor for Jira Cloud** app that can include maintenance and regular updates to keep the app up-to-date. If you encounter any issues or have questions specific to the app functionality, contact [Google Cloud Support](https://support.cloud.google.com/portal/). For more information, see [Getting Cloud Customer Care](https://docs.cloud.google.com/support/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
