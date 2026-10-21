---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview/
title: Overview of Apigee monetization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:05:01.328267+00:00
---

# Overview of Apigee monetization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Overview of Apigee monetization Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section introduces you to Apigee monetization. 

##  Monetize your APIs using Apigee monetization 

As an API provider, you need an easy-to-use and flexible way to monetize your APIs so that you can generate revenue whenever your APIs are used. Using Apigee's monetization feature, you can add a rate plan to an API product. The rate plan lets you charge the developers for using your APIs. You can also configure the rate plan to share your API revenue with the developers.

![API provider creates API product that defines the API proxies
                                                                                         and rate plans that can be purchased by app developers. App developers are giving an API key when they
                                                                                         purchase a rate plan. API providers can generate usage reports for analysis and billing.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/monetization-overview.png)

As an **API provider** you monetize your APIs by [enabling Apigee monetization](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enable) in your organization and configuring the components defined in the following table. 

Component | Description  
---|---  
API proxies |  When developing API proxies for use with monetized API products, you can attach the following policies:

  * [ VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) or the [ VerifyAccessToken operation of the OAuth2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#verifyingaccesstokens) to determine if an incoming request is monetizable by checking for the active published rate plan. For more information, see [ Adding an authentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#auth). 
  * [ MonetizationLimitsCheck policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy) to validate if the developer has purchased the associated API product and has sufficient balance in the wallet. For more information, see [ Enforcing developer subscriptions to API products](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#subscriptions). 
  * [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) to use the quota configuration defined using the API product. For more information, see [ Enforcing monetization quotas](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#quotas). 
  * [ DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) to override monetization-related usage data. For more information, see [ Capture monetization data](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data). 

  
API product | Define the collection of API proxies that you want to provide to app developers as a monetized bundle. The API product configures the access limits (quotas), API key approval method, rate plan (described below), and other details for the bundled API proxies. For more information, see [What is an API product?](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product#what-is-an-api-product) and [Enforcing monetization quotas in API products](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-quotas-api-products). **Note:** If you use the API product with Apigee monetization, the product name must not contain any trailing spaces.  
Rate plan | Define the billing configuration, fees, and charges that are incurred for the use of APIs offered in a monetized API product bundle. For example, you can share the API revenue with your developers. For more information, see [Managing rate plans for API products](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-rate-plans).  **Note:** If an active rate plan is associated with an API product, the API product is considered to be monetized. An API product can have multiple rate plans associated with it but **only one** rate plan can be active at any point of time.  
  
## Manage app developer API product subscriptions

To access an API in a monetized API product, **app developers** must have a subscription to the API product and obtain API keys to send with API requests. 

App developers can obtain subscriptions through either of the following methods:

  * Directly, by obtaining a subscription to the API product. In this case, you as an **API provider** need to provide a method for app developers to purchase subscriptions to your API products. Either: 
    * [Integrate Apigee monetization with your Drupal-based developer portal](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/integrate-developer-portal)
    * Build a custom portal interface and [purchase and manage API products subscriptions using the API](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/purchase-api-products-api)
  * Through a membership in an AppGroup. For information on subscription management using AppGroups, see  Use AppGroups to manage API product subscriptions.



### Use AppGroups to manage API product subscriptions

Apigee supports using AppGroups to manage API product subscriptions and monetization for usage of those API products. If an app developer is a member of an AppGroup that has a subscription to an API product, that app developer automatically has the same subscription to the API product. 

**Note:** The email for an AppGroup must be set before purchasing a subscription for the AppGroup. See [View and manage AppGroups](https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership#viewing-and-managing-appgroup) for information on managing AppGroups. 

AppGroups in monetization support the following features: 

  * AppGroups subscribed to API products with rate plans.
  * AppGroup billing types: `PREPAID` or `POSTPAID`.
  * Prepaid AppGroup wallets debited according to the rate plan for the subscribed API product.
  * Top-ups for prepaid AppGroup account balances.
  * Admin manual adjustment of AppGroup balances.
  * Consumption and revenue sharing charges reported for AppGroups, similarly to developers.



To use AppGroups with monetization, provide one of the subscription methods listed in Enable app developers to purchase API product subscriptions and include AppGroup management in the interface. 

For information on general AppGroups management, see [ Viewing and managing AppGroups](https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership#viewing-and-managing-appgroups). 

## Understand monetization quotas

A quota defines the number of requests allowed for an API product over a given time period. Quotas can protect your backend servers from high traffic variances and differentiate your product line.

When [creating your API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products), you can configure business-level quotas to control access to your APIs. For more information about quotas defined at the API product level, see [Quotas](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product#quotas). 

Attach Quota policies to the API proxies in your monetized API product to ensure that the quota defined at the API product level is used. For more information, see [Enforcing monetization quotas](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#quotas). 

**Note:** If you add a quota after the API product has been in use, the quota calculation starts from the next monetized transaction.

## Understand billing for monetized API products

Apigee monetization supports both **postpaid** and **prepaid** billing accounts. 

  * **Postpaid billing** : In postpaid billing, your app developers do not make any upfront payment. App developers are billed after using your API products. Apigee does not provide any specific invoice generation functionality for billing. You handle the billing settlement with your developers.
  * **Prepaid billing** : In prepaid billing, app developers pay in advance before using your API products. The upfront payment made by the developer is available in the developer's wallet. Based on the usage, the per-transaction cost is deducted from the wallet. 

The setup fee (if any), per-transaction cost, and any recurring fees are deducted from the wallet. If the developer's wallet contains less than the amount of any setup fee at the time of the API product purchase attempt, the purchase will fail with an error indicating insuffient funds.




When [creating a rate plan](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-rate-plans#create), you configure the billing currency and frequency, any setup and recurring fees, and the consumption-based fees. Based on the rate plan configuration and the developer's unique API key used to access your APIs, you can collect usage data for analysis and to [generate monetization reports](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/generate-reports). Then, you can use the data collected to generate your billing invoices. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
