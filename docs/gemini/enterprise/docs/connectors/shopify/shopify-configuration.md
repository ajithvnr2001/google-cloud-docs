---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify/shopify-configuration/
title: Shopify configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:30.303548+00:00
---

# Shopify configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify/shopify-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Shopify configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up and configure a third-party application before creating the Shopify data store.

## Create OAuth App

  1. Sign in to your Shopify account.

  2. Click your profile icon and select **Developer console**.

  3. In the **Developer console** page, click **Apps**.

  4. Click **Create app**.

  5. In **Create an app** page, do the following:

     1. In the **App name** field, enter a label for your app.

     2. Click **Create**.

  6. Navigate to the **Settings** tab within your app's dashboard.

  7. In the **Credentials** section, copy and store your:

     * **Client ID:** Public identifier

     * **Client Secret:** Private key




## Set redirect URL and scopes

After creating the app, configure its redirect URL and scopes:

  1. In the app page, in the navigation, click **Versions**.

     1. In the **Create a version** page, do the following:

        1. In the **Access** section, click **Select scopes**.

Scope | Purpose  
---|---  
`read_customers` | Retrieve customer profiles, contact info, and history.  
`write_customers` | Create or update customer profiles, contact info, and history.  
`read_orders` | View full order details (transactions, items, and status).  
`read_products` | View product and product variant information.  
`write_orders` | Create or update existing orders on your Shopify site.  
`read_fulfillments` | View fulfillments and fulfillment services.  
`read_assigned_fulfillment_orders` | View fulfillment orders, including their fulfillment order IDs.  
`write_assigned_fulfillment_orders` | Send a fulfillment request for an order on your Shopify site.  
        2. In the **Redirect URL** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.

        3. Click **Release**.

        4. In the confirmation dialog, enter a version label and click **Release**.

  2. In the app page, in the navigation, click **Home**.

     1. In the app home page, click **Install app**.

     2. In the confirmation page, select your store. 

     3. In the **Install app** page, review the access settings and click **Install**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
