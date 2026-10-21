---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/create-salesforce-app-for-plugin/
title: Create a Salesforce Connected App for Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:27.127393+00:00
---

# Create a Salesforce Connected App for Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/create-salesforce-app-for-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create a Salesforce Connected App for Cloud Data Fusion Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect to Salesforce APIs when you use Salesforce plugins in Cloud Data Fusion. You create a Salesforce Connected App, which is an entry point to access Salesforce APIs. Creating the app is required to integrate a Cloud Data Fusion instance with a Salesforce instance. After you create the app in Salesforce, you call its APIs by adding its credentials, such as Consumer and Consumer Secret Keys, to the [plugin properties](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#properties).

## Create a Connected Salesforce App for Cloud Data Fusion

To create a Connected Salesforce App, follow these steps. For more information, see the Salesforce documentation: [Configure basic Connected App settings](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5).

  1. Sign into Salesforce with your developer account.
  2. In the Salesforce web interface, go to the **Account** menu and click **Setup**.
  3. In the **Apps** list, select **App Manager**.
  4. Click **New Connected App**.
  5. On the **Manage Connected App** page, enter a name, API name, and contact email. The examples in this guide use the name `DATA_FUSION_APP`.
  6. Enable the OAuth settings. For more information, see [Enable OAuth Settings for API Integration](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_api_integration.htm&type=5).

![Enter Data Fusion information in Salesforce.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/create-salesforce-app-for-plugin/create-sf-connected-app.png)

When you configure Salesforce in Cloud Data Fusion, enter the following values:

     1. In the **Callback URL** field, enter the following: 
        * For a production environment, enter `https://login.salesforce.com/services/oauth2/token`.
        * For a sandbox, enter `https://test.salesforce.com/services/oauth2/token`.
        * If you have a custom domain enabled for your organization, use the custom URL, which is formatted as `https://CUSTOM_DOMAIN1.my.salesforce.com/services/oauth2/token`.
     2. In the Selected **OAuth Scopes** field, select **Manage user data via APIs (api)** and click **Add**.

![Enter Callback URL and OAuth Scopes in Salesforce.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/create-salesforce-app-for-plugin/callback-url.png)

     3. Click **Save**.




## Manage the Connected Salesforce App for Cloud Data Fusion

  1. In the Salesforce web interface, on the new **Connected App** page that opens, click **Manage > Edit Policies**.

  2. On the **Connected App Edit** page that opens, select the following:

     * In the **Permitted Users** field, select **All users may self-authorize**.
     * In the **IP Relaxation** field, select **Relax IP Restrictions**.
  3. Click **Save**.




## Get properties from Salesforce

The following sections describe how to find configuration information in Salesforce.

### Get the consumer keys for the plugin configurations

When you configure a Salesforce batch source properties in Cloud Data Fusion, you must enter a consumer key and a consumer secret key from Salesforce. To get them, follow these steps:

  1. Go to the Salesforce web interface.
  2. Go to the **API (Enable OAuth Settings)** section. Note the **Consumer Key** and **Consumer Secret**. Enter these credentials when you configure the plugin in Cloud Data Fusion.



### Get the security token for the plugin configurations

The plugin requires a security token for authentication with Salesforce. To get the security token, follow the steps in the Salesforce documentation: [Reset your security token](https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm&type=5).

## What's next

  * Configure the [Salesforce batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) in Cloud Data Fusion. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
