---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.ListDataSourcesRequest
title: Google Shopping Merchant DataSources V1beta Client - Class ListDataSourcesRequest (2.0.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:08.419193+00:00
---

# Google Shopping Merchant DataSources V1beta Client - Class ListDataSourcesRequest (2.0.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.ListDataSourcesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant DataSources V1beta Client - Class ListDataSourcesRequest (2.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.3.6  1.2.1  1.1.1  1.0.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.3  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant DataSources V1beta Client class ListDataSourcesRequest.

Request message for the ListDataSources method.

Generated from protobuf message `google.shopping.merchant.datasources.v1beta.ListDataSourcesRequest`

## Namespace

Google \ Shopping \ Merchant \ DataSources \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The account to list data sources for. Format: `accounts/{account}`  
`↳ page_size` |  `int`   
Optional. The maximum number of data sources to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000. If unspecified, the maximum number of data sources will be returned.  
`↳ page_token` |  `string`   
Optional. A page token, received from a previous `ListDataSources` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataSources` must match the call that provided the page token.  
  
### getParent

Required. The account to list data sources for.

Format: `accounts/{account}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The account to list data sources for.

Format: `accounts/{account}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. The maximum number of data sources to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000. If unspecified, the maximum number of data sources will be returned.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. The maximum number of data sources to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000. If unspecified, the maximum number of data sources will be returned.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. A page token, received from a previous `ListDataSources` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataSources` must match the call that provided the page token.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. A page token, received from a previous `ListDataSources` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataSources` must match the call that provided the page token.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The account to list data sources for. Format: `accounts/{account}` Please see DataSourcesServiceClient::accountName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListDataSourcesRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.ListDataSourcesRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
