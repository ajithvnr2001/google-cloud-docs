---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension
title: Google Analytics Admin V1alpha Client - Class CustomDimension (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:00.287200+00:00
---

# Google Analytics Admin V1alpha Client - Class CustomDimension (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class CustomDimension (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class CustomDimension.

A definition for a CustomDimension.

Generated from protobuf message `google.analytics.admin.v1alpha.CustomDimension`

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
Identifier. Resource name for this CustomDimension resource. Format: properties/{property}/customDimensions/{customDimension}  
`↳ parameter_name` |  `string`   
Required. Immutable. Tagging parameter name for this custom dimension. If this is a user-scoped dimension, then this is the user property name. If this is an event-scoped dimension, then this is the event parameter name. If this is an item-scoped dimension, then this is the parameter name found in the eCommerce items array. May only contain alphanumeric and underscore characters, starting with a letter. Max length of 24 characters for user-scoped dimensions, 40 characters for event-scoped dimensions.  
`↳ display_name` |  `string`   
Required. Display name for this custom dimension as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display names may contain square brackets, but updates to this field will never permit square brackets.  
`↳ description` |  `string`   
Optional. Description for this custom dimension. Max length of 150 characters.  
`↳ scope` |  `int`   
Required. Immutable. The scope of this dimension.  
`↳ disallow_ads_personalization` |  `bool`   
Optional. If set to true, sets this dimension as NPA and excludes it from ads personalization. This is currently only supported by user-scoped custom dimensions.  
  
### getName

Identifier. Resource name for this CustomDimension resource.

Format: properties/{property}/customDimensions/{customDimension}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Resource name for this CustomDimension resource.

Format: properties/{property}/customDimensions/{customDimension}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getParameterName

Required. Immutable. Tagging parameter name for this custom dimension.

If this is a user-scoped dimension, then this is the user property name. If this is an event-scoped dimension, then this is the event parameter name. If this is an item-scoped dimension, then this is the parameter name found in the eCommerce items array. May only contain alphanumeric and underscore characters, starting with a letter. Max length of 24 characters for user-scoped dimensions, 40 characters for event-scoped dimensions.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParameterName

Required. Immutable. Tagging parameter name for this custom dimension.

If this is a user-scoped dimension, then this is the user property name. If this is an event-scoped dimension, then this is the event parameter name. If this is an item-scoped dimension, then this is the parameter name found in the eCommerce items array. May only contain alphanumeric and underscore characters, starting with a letter. Max length of 24 characters for user-scoped dimensions, 40 characters for event-scoped dimensions.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. Display name for this custom dimension as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display names may contain square brackets, but updates to this field will never permit square brackets.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. Display name for this custom dimension as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display names may contain square brackets, but updates to this field will never permit square brackets.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. Description for this custom dimension. Max length of 150 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. Description for this custom dimension. Max length of 150 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getScope

Required. Immutable. The scope of this dimension.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [DimensionScope](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension.DimensionScope).  
  
### setScope

Required. Immutable. The scope of this dimension.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [DimensionScope](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension.DimensionScope).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisallowAdsPersonalization

Optional. If set to true, sets this dimension as NPA and excludes it from ads personalization.

This is currently only supported by user-scoped custom dimensions.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDisallowAdsPersonalization

Optional. If set to true, sets this dimension as NPA and excludes it from ads personalization.

This is currently only supported by user-scoped custom dimensions.

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
