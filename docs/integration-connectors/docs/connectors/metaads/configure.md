---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/metaads/configure/
title: MetaAds \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:24.139449+00:00
---

# MetaAds  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/metaads/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MetaAds

The MetaAds connector lets you connect to Meta / Facebook Ads data, and perform create, read, update, and delete operations on the data.

## Before you begin

Before using the Meta Ads connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




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
     1. **Connector** : Select **Meta Ads** from the drop down list of available Connectors.
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
     7. **Account Id** : The ID of your ad account. If none is specified, we use the first ad account id returned from Facebook Ads. 
     8. **Aggregate Format** : The format aggregate or collection columns should return in. 
     9. **Authenticate As Page** : The name or Id of a page to authenticate as when making requests to Facebook. 
     10. **Retry Level** : The most granular ad object level at which the driver will try to retrieve results on retry. 
     11. **Target** : A default target if none is specified. Used for some tables, such as Comments, where a target may be specified. 
     12. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     13. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Meta Ads connection:

        * OAuth 2.0 Auth Code Grant 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 Auth Code Grant**
    * **Access token** : The access token used for authenticating requests with auth-code-flow-based connections.
    * **Client ID** : The client id provided by connector for the app you created.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.



### Meta Ads configuration

To create an app that integrates with Meta Ads, complete the following tasks:

  * Set up and create a Meta app account
  * Set up OAuth2.0 client authentication
  * Set up scope details
  * Set up a redirect URL



#### Set up and create a Meta app account

  1. Go to [Facebook business manager](https://business.facebook.com/).
  2. Click **Create Account** and fill in your business details to create your account.
  3. Verify your identity and business information during the setup process.
  4. Go to the business settings and click **Pages** in the menu after setting up your Business manager account.
  5. Click **Add** and select **Add a Page**. Follow the other prompts to add your Facebook page to your Business manager account.
  6. Click **Add Accounts** in the menu in the business settings. Click **Add** and select **Add Ad Account**.

You can either use an existing ad account or create a new one. 

  7. Click **Payment Methods** in the business settings.
  8. Click **Add** to add a payment method such as a credit card or PayPal account. Follow the other prompts to enter your payment information.
  9. Click **Add People** and enter the email addresses of the individuals you want to grant access to your Business manager account. Assign appropriate roles and permissions to each person based on their responsibilities.
  10. Go to the **Ads Manager** , click menu icon in the Business manager and select **Ads Manager**. Click **Create** to create your ad campaign.
  11. Follow the prompts to define your campaign objective, target audience, ad format, budget, and schedule.
  12. Upload the ad that you have created, and verify the details before submitting your ad campaign for review.
  13. Monitor your ad campaign and its performance in the Ads manager after it is live. Analyze key metrics such as reach, engagement, and conversion rates. Adjust your campaigns as needed to optimize performance and achieve your advertising goals.
  14. Log in with your personal Facebook account or sign up for a new account if you do not have one already. Login to [Facebook developer](https://developers.facebook.com/?.).
  15. Click on the **My Apps** dropdown menu and select **Create App.**
  16. Select the platform for your app such as iOS, Android, Web, etc.
  17. Provide basic information about your app, such as name, email address, and category.
  18. Click on **Create App ID** to generate a unique identifier for your app after providing the necessary information.
  19. Configure additional settings for your app, such as adding platform-specific details which includes iOS bundle ID, Android package name and setting up app domains and privacy policy URLs.
  20. Choose the Facebook products you want to integrate into your app, such as Facebook Login, Analytics, or Ads.
  21. Follow the instructions provided to set up your development environment and integrate Facebook SDKs into your app code.
  22. After your app is set up and configured, start building and testing its features using the Facebook developer tools and resources.

For information about creating an app, see [Create an app](https://developers.facebook.com/docs/development/create-an-app/).




#### Set up OAuth2.0 client authentication details

  1. Go to the [Meta for developers](https://developers.facebook.com/apps/?show_reminder=true) using your facebook credentials.
  2. Click **My Apps** and select the Apps tab and choose the Meta App that you have created earlier.
  3. Click on **App Settings > Basic**.
  4. View the App secret which is the client secret. Click **show** , enter your account password, copy and save it for further usage.
  5. Click **App Settings > Advanced**. Find the client token, which is the client ID. You can reset it if needed.



#### Set up scope details

The scope fo Meta Ads connector is **ads_management**.

#### Set up redirect URL details

  1. Go to the [Meta for developers](https://developers.facebook.com/apps/?show_reminder=true) using your facebook credentials.
  2. Click on the **Apps** tab and choose the Meta App you created earlier.
  3. Click on facebook **Login > Settings**.
  4. Paste the redirect url generated under **Valid OAuth Redirect URIs** and enter the details in the other required fields.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Note:** Facebook mandates identity or business verification before allowing the creation of additional ad accounts. If this verification is not completed, you may face restrictions on creating new ad accounts. Meta requires businesses to verify their identity to run ads on the platform, helping to ensure that advertisers are legitimate and maintain the integrity of the advertising ecosystem. 

### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Meta Ads connection.

####  Meta Ads web connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | facebookads  
Connector version | 1  
Connection Name | google-cloud-meta-ads-conn  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Client ID | CLIENT_ID  
Scopes | ads_management  
Client secret | CLIENT_SECRET  
Secret version | 2  
  
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

The MetaAds connector can process 6 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### CreateAdPreview action

Creates a schema file for an app insight.

#### Input parameters of the CreateAdPreview action

Parameter Name  | Data Type | Required | Description  
---|---|---|---  
AdFormat | String | True | The format of the ad to use.The allowed values are AUDIENCE_NETWORK_INSTREAM_VIDEO, AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE, AUDIENCE_NETWORK_OUTSTREAM_VIDEO, AUDIENCE_NETWORK_REWARDED_VIDEO, DESKTOP_FEED_STANDARD, FACEBOOK_STORY_MOBILE, INSTAGRAM_STANDARD, INSTAGRAM_STORY, INSTANT_ARTICLE_STANDARD, INSTREAM_VIDEO_DESKTOP, INSTREAM_VIDEO_MOBILE, MARKETPLACE_MOBILE, MESSENGER_MOBILE_INBOX_MEDIA, MOBILE_BANNER, MOBILE_FEED_BASIC, MOBILE_FEED_STANDARD, MOBILE_FULLWIDTH, MOBILE_INTERSTITIAL, MOBILE_MEDIUM_RECTANGLE, MOBILE_NATIVE, RIGHT_COLUMN_STANDARD, SUGGESTED_VIDEO_DESKTOP, SUGGESTED_VIDEO_MOBILE, WATCH_FEED_MOBILE.  
AdCreativeId | String | True | An Id of the ad creative to use for creating the preview from.  
  
For example on how to configure the `CreateAdPreview` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Create an Ad preview

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateAdPreview` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
         "AdCreativeId": "120208552947120478",
         "AdFormat": "AUDIENCE_NETWORK_INSTREAM_VIDEO"
         }

If the action is successful, the `CreateAdPreview` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Url": "https://business.facebook.com/ads/api/preview_iframe.php?d=AQL_quk8kLm_6z2oZ14q9A0led9llzr981NPv-zUHhwZ5IXjO07s7ngrI2y0qI0VZCRH2w9hgCwy5xrbFQlWCy0g-uRpRHvFS0dS0erj2Lg4HI7ZfIRm8h3nZLhJygM",
      "@affectedrows": null
    }, {
      "Url": null,
      "@affectedrows": null
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all Ad accounts

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AdAccounts` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all campaigns

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Campaigns` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - Get an Adset

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Adsets` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `120206747969710053` in the **Default Value** field. 

Here, `120206747969710053` is a unique record ID in the `User` entity.


**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Use the MetaAds connection in an integration

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
