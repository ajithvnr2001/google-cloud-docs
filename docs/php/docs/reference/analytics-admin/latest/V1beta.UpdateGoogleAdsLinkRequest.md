---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.UpdateGoogleAdsLinkRequest
title: Google Analytics Admin V1beta Client - Class UpdateGoogleAdsLinkRequest (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:58.791567+00:00
---

# Google Analytics Admin V1beta Client - Class UpdateGoogleAdsLinkRequest (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.UpdateGoogleAdsLinkRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1beta Client - Class UpdateGoogleAdsLinkRequest (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1beta Client class UpdateGoogleAdsLinkRequest.

Request message for UpdateGoogleAdsLink RPC

Generated from protobuf message `google.analytics.admin.v1beta.UpdateGoogleAdsLinkRequest`

## Namespace

Google \ Analytics \ Admin \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ google_ads_link` |  `[GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.GoogleAdsLink)`   
The GoogleAdsLink to update  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.  
  
### getGoogleAdsLink

The GoogleAdsLink to update

**Returns**  
---  
**Type** | **Description**  
`[GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.GoogleAdsLink)|null` |   
  
### hasGoogleAdsLink

### clearGoogleAdsLink

### setGoogleAdsLink

The GoogleAdsLink to update

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.GoogleAdsLink)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`googleAdsLink` |  `[GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.GoogleAdsLink)`   
The GoogleAdsLink to update  
`updateMask` |  `Google\Protobuf\FieldMask`   
Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.UpdateGoogleAdsLinkRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
