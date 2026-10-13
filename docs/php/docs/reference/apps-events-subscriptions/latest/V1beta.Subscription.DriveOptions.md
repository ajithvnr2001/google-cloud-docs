---
url: https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription.DriveOptions
title: Google Apps Events Subscriptions V1beta Client - Class DriveOptions (0.5.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:54.626623+00:00
---

# Google Apps Events Subscriptions V1beta Client - Class DriveOptions (0.5.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription.DriveOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Events Subscriptions V1beta Client - Class DriveOptions (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.4.4  0.3.1  0.2.1  0.1.6 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Apps Events Subscriptions V1beta Client class DriveOptions.

Additional supported options for serving Drive events.

Generated from protobuf message `google.apps.events.subscriptions.v1beta.Subscription.DriveOptions`

## Namespace

Google \ Apps \ Events \ Subscriptions \ V1beta \ Subscription

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ include_descendants` |  `bool`   
Optional. Immutable. Whether to include all the descendant Drive files in the list of events. If false, the subscription will be created for the single file/drive that is specified as the [`target_resource`](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription#_Google_Apps_Events_Subscriptions_V1beta_Subscription__getTargetResource__). This flag can be used when the [`target_resource`](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription#_Google_Apps_Events_Subscriptions_V1beta_Subscription__getTargetResource__) is either a [Drive](https://developers.google.com/drive/api/reference/rest/v3/drives) or a [Drive file](https://developers.google.com/drive/api/reference/rest/v3/files) that has mimeType set to `application/vnd.google-apps.folder`.  
  
### getIncludeDescendants

Optional. Immutable. Whether to include all the descendant Drive files in the list of events. If false, the subscription will be created for the single file/drive that is specified as the [`target_resource`](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription#_Google_Apps_Events_Subscriptions_V1beta_Subscription__getTargetResource__).

This flag can be used when the [`target_resource`](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription#_Google_Apps_Events_Subscriptions_V1beta_Subscription__getTargetResource__) is either a [Drive](https://developers.google.com/drive/api/reference/rest/v3/drives) or a [Drive file](https://developers.google.com/drive/api/reference/rest/v3/files) that has mimeType set to `application/vnd.google-apps.folder`.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setIncludeDescendants

Optional. Immutable. Whether to include all the descendant Drive files in the list of events. If false, the subscription will be created for the single file/drive that is specified as the [`target_resource`](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription#_Google_Apps_Events_Subscriptions_V1beta_Subscription__getTargetResource__).

This flag can be used when the [`target_resource`](https://docs.cloud.google.com/php/docs/reference/apps-events-subscriptions/latest/V1beta.Subscription#_Google_Apps_Events_Subscriptions_V1beta_Subscription__getTargetResource__) is either a [Drive](https://developers.google.com/drive/api/reference/rest/v3/drives) or a [Drive file](https://developers.google.com/drive/api/reference/rest/v3/files) that has mimeType set to `application/vnd.google-apps.folder`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
