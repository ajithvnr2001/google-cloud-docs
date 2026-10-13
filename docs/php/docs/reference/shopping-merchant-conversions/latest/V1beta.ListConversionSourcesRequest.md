---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.ListConversionSourcesRequest
title: Google Shopping Merchant Conversions V1beta Client - Class ListConversionSourcesRequest (1.2.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:10.659471+00:00
---

# Google Shopping Merchant Conversions V1beta Client - Class ListConversionSourcesRequest (1.2.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.ListConversionSourcesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Conversions V1beta Client - Class ListConversionSourcesRequest (1.2.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.4 (latest)  1.2.0  1.1.3  1.0.0  0.3.0  0.2.1  0.1.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Conversions V1beta Client class ListConversionSourcesRequest.

Request message for the ListConversionSources method.

Generated from protobuf message `google.shopping.merchant.conversions.v1beta.ListConversionSourcesRequest`

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
`↳ parent` |  `string`   
Required. The merchant account who owns the collection of conversion sources. Format: accounts/{account}  
`↳ page_size` |  `int`   
Optional. The maximum number of conversion sources to return in a page. If no `page_size` is specified, `100` is used as the default value. The maximum value is `200`. Values above `200` will be coerced to `200`. Regardless of pagination, at most `200` conversion sources are returned in total.  
`↳ page_token` |  `string`   
Optional. Page token.  
`↳ show_deleted` |  `bool`   
Optional. Show deleted (archived) option.  
  
### getParent

Required. The merchant account who owns the collection of conversion sources. Format: accounts/{account}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The merchant account who owns the collection of conversion sources. Format: accounts/{account}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. The maximum number of conversion sources to return in a page.

If no `page_size` is specified, `100` is used as the default value. The maximum value is `200`. Values above `200` will be coerced to `200`. Regardless of pagination, at most `200` conversion sources are returned in total.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. The maximum number of conversion sources to return in a page.

If no `page_size` is specified, `100` is used as the default value. The maximum value is `200`. Values above `200` will be coerced to `200`. Regardless of pagination, at most `200` conversion sources are returned in total.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. Page token.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. Page token.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getShowDeleted

Optional. Show deleted (archived) option.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setShowDeleted

Optional. Show deleted (archived) option.

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
`parent` |  `string`   
Required. The merchant account who owns the collection of conversion sources. Format: accounts/{account} Please see ConversionSourcesServiceClient::accountName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListConversionSourcesRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-conversions/latest/V1beta.ListConversionSourcesRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
