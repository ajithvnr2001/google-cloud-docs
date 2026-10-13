---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.MerchantCenterDestination
title: Google Shopping Merchant Conversions V1beta Client - Class MerchantCenterDestination (1.2.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:12.499727+00:00
---

# Google Shopping Merchant Conversions V1beta Client - Class MerchantCenterDestination (1.2.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.MerchantCenterDestination

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Conversions V1beta Client - Class MerchantCenterDestination (1.2.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.4 (latest)  1.2.0  1.1.3  1.0.0  0.3.0  0.2.1  0.1.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Conversions V1beta Client class MerchantCenterDestination.

"Merchant Center Destination" sources can be used to send conversion events from an online store using a Google tag directly to a Merchant Center account where the source is created.

Generated from protobuf message `google.shopping.merchant.conversions.v1beta.MerchantCenterDestination`

## Namespace

Google \ Shopping \ Merchant \ Conversions \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ destination` |  `string`   
Output only. Merchant Center Destination ID.  
`↳ attribution_settings` |  `[AttributionSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.AttributionSettings)`   
Required. Attribution settings being used for the Merchant Center Destination.  
`↳ display_name` |  `string`   
Required. Merchant-specified display name for the destination. This is the name that identifies the conversion source within the Merchant Center UI. Limited to 64 characters.  
`↳ currency_code` |  `string`   
Required. Three-letter currency code (ISO 4217). The currency code defines in which currency the conversions sent to this destination will be reported in Merchant Center.  
  
### getDestination

Output only. Merchant Center Destination ID.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDestination

Output only. Merchant Center Destination ID.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAttributionSettings

Required. Attribution settings being used for the Merchant Center Destination.

**Returns**  
---  
**Type** | **Description**  
`[AttributionSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.AttributionSettings)|null` |   
  
### hasAttributionSettings

### clearAttributionSettings

### setAttributionSettings

Required. Attribution settings being used for the Merchant Center Destination.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AttributionSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.AttributionSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. Merchant-specified display name for the destination. This is the name that identifies the conversion source within the Merchant Center UI.

Limited to 64 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. Merchant-specified display name for the destination. This is the name that identifies the conversion source within the Merchant Center UI.

Limited to 64 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCurrencyCode

Required. Three-letter currency code (ISO 4217). The currency code defines in which currency the conversions sent to this destination will be reported in Merchant Center.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCurrencyCode

Required. Three-letter currency code (ISO 4217). The currency code defines in which currency the conversions sent to this destination will be reported in Merchant Center.

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

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
