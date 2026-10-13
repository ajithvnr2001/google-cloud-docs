---
url: https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.CreateSubscriptionRequest
title: Google Apps Events Subscriptions V1beta Client - Class CreateSubscriptionRequest (0.5.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:35.733729+00:00
---

# Google Apps Events Subscriptions V1beta Client - Class CreateSubscriptionRequest (0.5.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.CreateSubscriptionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Events Subscriptions V1beta Client - Class CreateSubscriptionRequest (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.4.4  0.3.1  0.2.1  0.1.6 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Apps Events Subscriptions V1beta Client class CreateSubscriptionRequest.

The request message for [SubscriptionsService.CreateSubscription](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Client.SubscriptionsServiceClient#_Google_Apps_Events_Subscriptions_V1beta_Client_SubscriptionsServiceClient__createSubscription__).

Generated from protobuf message `google.apps.events.subscriptions.v1beta.CreateSubscriptionRequest`

## Namespace

Google \ Apps \ Events \ Subscriptions \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ subscription` |  `[Subscription](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription)`   
Required. The subscription resource to create.  
`↳ validate_only` |  `bool`   
Optional. If set to `true`, validates and previews the request, but doesn't create the subscription.  
  
### getSubscription

Required. The subscription resource to create.

**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription)|null` |   
  
### hasSubscription

### clearSubscription

### setSubscription

Required. The subscription resource to create.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Subscription](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getValidateOnly

Optional. If set to `true`, validates and previews the request, but doesn't create the subscription.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setValidateOnly

Optional. If set to `true`, validates and previews the request, but doesn't create the subscription.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`subscription` |  `[Subscription](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription)`   
Required. The subscription resource to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreateSubscriptionRequest](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.CreateSubscriptionRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
