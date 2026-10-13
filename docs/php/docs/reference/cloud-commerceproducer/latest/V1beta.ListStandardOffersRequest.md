---
url: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.ListStandardOffersRequest
title: Google Cloud Commerce Producer V1beta Client - Class ListStandardOffersRequest (0.2.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:16.120520+00:00
---

# Google Cloud Commerce Producer V1beta Client - Class ListStandardOffersRequest (0.2.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.ListStandardOffersRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Commerce Producer V1beta Client - Class ListStandardOffersRequest (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Commerce Producer V1beta Client class ListStandardOffersRequest.

Message for requesting list of StandardOffers

Generated from protobuf message `google.cloud.commerceproducer.v1beta.ListStandardOffersRequest`

## Namespace

Google \ Cloud \ CommerceProducer \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Parent value for ListStandardOffersRequest  
`↳ page_size` |  `int`   
Optional. Maximum results to return. The service may return fewer than this value. The maximum value is 500; values above 500 will be coerced to 500. If unspecified, the server will default to the maximum.  
`↳ page_token` |  `string`   
Optional. A page token, received from a previous list response message. Provide this to retrieve the subsequent page. When paginating, all other parameters of the list request must match the request that returned the page token.  
`↳ filter` |  `string`   
Optional. Filter expression that matches a subset of resources to show. See <https://google.aip.dev/160> for more details. Supports filtering by: * * `effective_time`. Example: `effective_time > "2012-04-21T11:30:00-04:00"`. * * `expire_time`. Example: `expire_time < "2026-05-06T00:00:00Z"`.  
`↳ order_by` |  `string`   
Optional. Ordering expression for sorting the results. See <https://google.aip.dev/132#ordering> for more details. If no value is present the default ordering is unspecified. Supports ordering by: * * `effective_time` * * `expire_time`  
  
### getParent

Required. Parent value for ListStandardOffersRequest

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Parent value for ListStandardOffersRequest

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. Maximum results to return. The service may return fewer than this value. The maximum value is 500; values above 500 will be coerced to 500.

If unspecified, the server will default to the maximum.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. Maximum results to return. The service may return fewer than this value. The maximum value is 500; values above 500 will be coerced to 500.

If unspecified, the server will default to the maximum.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. A page token, received from a previous list response message.

Provide this to retrieve the subsequent page. When paginating, all other parameters of the list request must match the request that returned the page token.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. A page token, received from a previous list response message.

Provide this to retrieve the subsequent page. When paginating, all other parameters of the list request must match the request that returned the page token.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. Filter expression that matches a subset of resources to show.

See <https://google.aip.dev/160> for more details. Supports filtering by:

  * `effective_time`. Example: `effective_time > "2012-04-21T11:30:00-04:00"`.
  * `expire_time`. Example: `expire_time < "2026-05-06T00:00:00Z"`.



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. Filter expression that matches a subset of resources to show.

See <https://google.aip.dev/160> for more details. Supports filtering by:

  * `effective_time`. Example: `effective_time > "2012-04-21T11:30:00-04:00"`.
  * `expire_time`. Example: `expire_time < "2026-05-06T00:00:00Z"`.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. Ordering expression for sorting the results.

See <https://google.aip.dev/132#ordering> for more details. If no value is present the default ordering is unspecified. Supports ordering by:

  * `effective_time`
  * `expire_time`



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. Ordering expression for sorting the results.

See <https://google.aip.dev/132#ordering> for more details. If no value is present the default ordering is unspecified. Supports ordering by:

  * `effective_time`
  * `expire_time`



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
Required. Parent value for ListStandardOffersRequest Please see CommerceTransactionClient::serviceName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListStandardOffersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.ListStandardOffersRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
