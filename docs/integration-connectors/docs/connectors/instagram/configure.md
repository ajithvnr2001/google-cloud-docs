---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/instagram/configure/
title: Instagram \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:22.517785+00:00
---

# Instagram  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/instagram/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Instagram

The Instagram connector lets you perform insert, delete, update, and read operations on Instagram.

## Before you begin

Before using the Instagram connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




### Instagram configuration

To create an app that integrates with Instagram, complete the following tasks:

  * Set up an Instagram business account
  * Create a Facebook developer account
  * Set up OAuth2.0 client authentication
  * Set up scope details
  * Set up redirect URL details



#### Set up an Instagram business account

  1. Login to the [Instagram account](https://www.instagram.com/).
  2. If you are a new user, open the app and follow the prompts to create a new account. You can sign up with an email address, phone number, or through the Facebook application.
  3. If you are an existing user, sign in to your existing account.

For information about creating a new Instagram business account, see [Instagram account](https://help.instagram.com/502981923235522).

  4. Connect to a Facebook page.

During the setup, Instagram offers you the option to connect to a Facebook page. This is optional but is recommended for access to all features.

You can create a new Facebook page directly through the setup or link to an existing one.




#### Create a Facebook developer account for app creation and configuration

Log in using the Facebook account that you have created earlier.

  1. Login to the [Facebook developer account](https://developers.facebook.com/?.).
  2. Click on **My Apps** and select **Create App**.
  3. Choose the platform for your app from the list of options, such as iOS, Android, Web, etc.
  4. Enter basic information in your app, such as name, email address, and category.
  5. Click **Create App ID** after entering the necessary information to generate a unique identifier for your app.
  6. Configure additional settings in your app, by adding platform-specific details such as iOS bundle ID, Android package name and setting up app domains, and privacy policy URLs.

For information about creating an app, see [Create an app](https://developers.facebook.com/docs/development/create-an-app/).

  7. Configure Instagram Graph API.
     1. Navigate to the settings of your app.
     2. Add the **Instagram Graph API** product to your app through the dashboard.
     3. On your app dashboard, click **Set Up** under Instagram 
     4. Configure the settings according to the needs of your app, including setting permissions. For information about configuring the Instagram Graph API, see [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/getting-started/).
  8. Add permissions for access.

Request the necessary permissions for the data you need. This typically includes permissions like instagram_basic, instagram_manage_comments, instagram_content_publish, instagram_manage_insights, pages_show_list etc.

Each permission defines the type of data or actions you can perform with the API. For information about permissions, see [Authorization and permissions](https://developers.facebook.com/docs/instagram-api/overview#authorization).

If your app requires additional data, you must submit your app for App review by Facebook. For this you need to describe how your app uses the data, by providing a screencast of the actual usage, to ensure that you meet the platform policy.

  9. Link your Instagram business account.
     1. Make sure your Instagram account is a Business or Creator account, as the Instagram Graph API does not work with personal account.
     2. Link this Instagram account to a Facebook Page.

#### Set up OAuth2.0 client authentication

     1. Log in to the [ Meta for Developers](https://developers.facebook.com/apps/?show_reminder=true) using your Facebook credentials.
     2. Click on Apps tab and choose the Meta App you created in the previous step.
     3. Click on App **Settings > Basic** in the menu.
     4. View the App secret which is the client secret. Click on show, it will prompt you for your account password, save the client secret for later use.
     5. Click on App **Settings > Advanced** in the menu. Find the client token, which is the client ID. You can reset it if needed.

#### Set up Scope details

Scopes can be set according to your business needs. Scopes have been set as instagram_basic, pages_show_list, pages_read_engagement.

#### Set up Redirect URL details

     1. Log in to the [Meta for Developers](https://developers.facebook.com/apps/?show_reminder=true) using your Facebook credentials.
     2. Click on Apps tab and choose the Meta App you created in the previous step.
     3. Click facebook **Login > Settings** from the menu.
     4. Paste the redirect url generated under **Valid OAuth Redirect URIs** in the required field.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

     1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

     2. Click **\+ Create new** to open the **Create Connection** page.
     3. In the **Location** section, choose the location for the connection. 
        1. **Region** : Select a location from the drop-down list. 

Supported regions for connectors include: 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

        2. Click **Next**.
     4. In the **Connection Details** section, complete the following: 
        1. **Connector** : Select **Instagram** from the drop down list of available Connectors.
        2. **Connector version** : Select the Connector version from the drop down list of available versions. 
        3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

           * Connection names can use letters, numbers, or hyphens.
           * Letters must be lower-case.
           * Connection names must begin with a letter and end with a letter or number.
           * Connection names cannot exceed 49 characters.
        4. Optionally, enter a **Description** for the connection instance.
        5. **Service Account** : Select a service account that has the required roles.
        6. Optionally, configure the **Connection node settings** : 

           * **Minimum number of nodes** : Enter the minimum number of connection nodes.
           * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
        7. **Verbosity Level** : Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates). 
        8. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
        9. Click **Next**.
     5. In the **Authentication** section, enter the authentication details. 
        1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Instagram connection:

           * OAuth 2.0 Auth Code Grant 

To understand how to configure these authentication types, see Configure authentication.

        2. Click **Next**.
     6. **Review** : Review your connection and authentication details.
     7. Click **Create**.

### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Instagram connection.

#### Instagram web connection type

Fieldname | Details  
---|---  
Location | europe-west1  
Connector | instagram  
Connector version | 1  
Connection Name | google-cloud-instagram  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Client ID | CLIENT_ID  
Scopes | instagram_basic,pages_show_list,pages_read_engagement  
Client secret | CLIENT_SECRET  
Secret version | 2  
  
### Configure authentication

Enter the details based on the authentication you want to use.

     * **OAuth 2.0 Auth Code Grant**
       * **Client ID** : The client ID used for requesting access tokens.
       * **Scopes** : A comma-separated list of desired scopes.
       * **Client secret** : The client secret used for requesting access tokens.
       * **Secret version** : The version of the secret that contains the client secret.

## Re-authorization for authorization code

If you are using `Authorization code` authentication type and have made any cofiguration changes in your Azure AD application, you must re-authorize your Azure AD connection. To re-authorize a connection, perform the following steps:

     1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

     2. Click **Edit** to edit the connection details. 
     3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

     4. Click **Save**. This takes you to the connection details page.
     5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
     6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).

### Additional steps after connection creation

If you selected `OAuth 2.0 - Authorization code` for authentication, you must do the following additional steps after creating the connection:

     1. In the [Connections page](https://console.cloud.google.com/connectors/connections), locate the newly created connection. 

Notice that the **Status** for the new connector will be **Authorization required**.

     2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

     3. Copy the **Redirect URI** value to your external application.
     4. Verify the authorization details.
     5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com/connectors/connections).

## Entities, operations, and actions

All the Integration Connectors provide a layer of abstraction for the objects of the connected application. You can access an application's objects only through this abstraction. The abstraction is exposed to you as entities, operations, and actions.

**Note:** You can view the entities, operations, and actions of a connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).
     * **Entity:** An entity can be thought of as an object, or a collection of properties, in the connected application or service. The definition of an entity differs from a connector to a connector. For example, in a database connector, tables are the entities, in a file server connector, folders are the entities, and in a messaging system connector, queues are the entities. 

However, it is possible that a connector doesn't support or have any entities, in which case the `Entities` list will be empty.

     * **Operation:** An operation is the activity that you can perform on an entity. You can perform any of the following operations on an entity: 
       * [List](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
       * [Get](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
       * [Create](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
       * [Update](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
       * [Delete](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)

Selecting an entity from the available list, generates a list of operations available for the entity. For a detailed description of the operations, see the Connectors task's [entity operations](https://docs.cloud.google.com/application-integration/docs/connectors-task#config-prop). However, if a connector doesn't support any of the entity operations, such unsupported operations aren't listed in the `Operations` list.

     * **Action:** An action is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and vary from connector to connector. Normally, an action will have some input parameters, and an output parameter. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty. 
**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. 

## System limitations

The Instagram connector can process 2 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 
     * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
     * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).

The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - List all IGMedia

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select IGMedia from the `Entity` list.
     3. Select the `List` operation, and then click **Done**.

### Example - List all AccountFollowersNonfollowers

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select AccountFollowersNonfollowers from the `Entity` list.
     3. Select the `List` operation, and then click **Done**.
     4. Set the filter clause to List single AccountFollowersNonfollowers. To set the filter clause, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `Metric='reach'` in the **Input Value** field and choose the filter clause as Local variable.

You must use the filter clause in the **Data Mapper** section of the Tasks to perform an operation with the AccountFollowersNonfollowers entity.

### Example - Get single IGMedia

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select IGMedia from the `Entity` list.
     3. Select the `Get` operation, and then click **Done**.
     4. Set the entity ID to Get single IGMedia. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `18008309540391873` in the **Input Value** field and choose the EntityId as Local variable.

### Example - Get MediaInsightReels

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select MediaInsightReels from the `Entity` list.
     3. Select the `List` operation, and then click **Done**.
     4. Set the filter clause to Get single MediaInsightReels. To set the filter clause, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `MediaId='18018014180193817'` in the **Input Value** field and choose the filter clause as Local variable. 

You must use the filter clause in the **Data Mapper** section of the Tasks to perform a Get operation for the following entities: MediaInsightReels, MediaInsights, MediaInsightsPost, AccountFollowersNonfollowers, andAccountContactButtonType.

### Example - Delete a comment

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select Comments from the `Entity` list.
     3. Select the `Delete` operation, and then click **Done**.
     4. Set the entity ID to Delete Comments. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `18435078259055638` in the **Input Value** field and choose the EntityId as Local variable.

### Example - Create a comment

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select Comments from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
            
            {
            "MediaId": "18008309540391873",
            "Text": "The Universe is with you"
            }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
            
            {
            "Id": "18351045133102133"
            }

### Example - Create a reply

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select Replies from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
            
            {
            "CommentId": "18022630739158714",
            "Text": "conquered" 
            }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
            
            {
            "Id": "18167970637306971"
            }

## Use the Instagram connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

     * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
     * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

     * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
     * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
     * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
