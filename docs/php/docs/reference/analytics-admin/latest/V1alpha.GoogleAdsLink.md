---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink
title: Google Analytics Admin V1alpha Client - Class GoogleAdsLink (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:13.416862+00:00
---

# Google Analytics Admin V1alpha Client - Class GoogleAdsLink (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class GoogleAdsLink (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class GoogleAdsLink.

A link between a Google Analytics property and a Google Ads account.

Generated from protobuf message `google.analytics.admin.v1alpha.GoogleAdsLink`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Format: properties/{propertyId}/googleAdsLinks/{googleAdsLinkId} Note: googleAdsLinkId is not the Google Ads customer ID.  
`↳ customer_id` |  `string`   
Immutable. Google Ads customer ID.  
`↳ can_manage_clients` |  `bool`   
Output only. If true, this link is for a Google Ads manager account.  
`↳ ads_personalization_enabled` |  `Google\Protobuf\BoolValue`   
Enable personalized advertising features with this integration. Automatically publish my Google Analytics audience lists and Google Analytics remarketing events/parameters to the linked Google Ads account. If this field is not set on create/update, it will be defaulted to true.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when this link was originally created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when this link was last updated.  
`↳ creator_email_address` |  `string`   
Output only. Email address of the user that created the link. An empty string will be returned if the email address can't be retrieved.  
  
### getName

Identifier. Format: properties/{propertyId}/googleAdsLinks/{googleAdsLinkId} Note: googleAdsLinkId is not the Google Ads customer ID.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Format: properties/{propertyId}/googleAdsLinks/{googleAdsLinkId} Note: googleAdsLinkId is not the Google Ads customer ID.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCustomerId

Immutable. Google Ads customer ID.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCustomerId

Immutable. Google Ads customer ID.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCanManageClients

Output only. If true, this link is for a Google Ads manager account.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setCanManageClients

Output only. If true, this link is for a Google Ads manager account.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdsPersonalizationEnabled

Enable personalized advertising features with this integration.

Automatically publish my Google Analytics audience lists and Google Analytics remarketing events/parameters to the linked Google Ads account. If this field is not set on create/update, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\BoolValue|null` |   
  
### hasAdsPersonalizationEnabled

### clearAdsPersonalizationEnabled

### getAdsPersonalizationEnabledUnwrapped

Returns the unboxed value from `getAdsPersonalizationEnabled()`

Enable personalized advertising features with this integration. Automatically publish my Google Analytics audience lists and Google Analytics remarketing events/parameters to the linked Google Ads account. If this field is not set on create/update, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`bool|null` |   
  
### setAdsPersonalizationEnabled

Enable personalized advertising features with this integration.

Automatically publish my Google Analytics audience lists and Google Analytics remarketing events/parameters to the linked Google Ads account. If this field is not set on create/update, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\BoolValue`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### setAdsPersonalizationEnabledUnwrapped

Sets the field by wrapping a primitive type in a Google\Protobuf\BoolValue object.

Enable personalized advertising features with this integration. Automatically publish my Google Analytics audience lists and Google Analytics remarketing events/parameters to the linked Google Ads account. If this field is not set on create/update, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool|null`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Time when this link was originally created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Time when this link was originally created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. Time when this link was last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. Time when this link was last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreatorEmailAddress

Output only. Email address of the user that created the link.

An empty string will be returned if the email address can't be retrieved.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCreatorEmailAddress

Output only. Email address of the user that created the link.

An empty string will be returned if the email address can't be retrieved.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
