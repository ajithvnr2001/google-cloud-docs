---
url: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.ListTokenAuthUsersRequest
title: Google Cloud Memorystore V1beta Client - Class ListTokenAuthUsersRequest (0.13.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:03.681539+00:00
---

# Google Cloud Memorystore V1beta Client - Class ListTokenAuthUsersRequest (0.13.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.ListTokenAuthUsersRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Memorystore V1beta Client - Class ListTokenAuthUsersRequest (0.13.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.3 (latest)  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Memorystore V1beta Client class ListTokenAuthUsersRequest.

Request message for `ListTokenAuthUsers`.

Generated from protobuf message `google.cloud.memorystore.v1beta.ListTokenAuthUsersRequest`

## Namespace

Google \ Cloud \ Memorystore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The parent to list token auth users from. Format: projects/{project}/locations/{location}/instances/{instance}  
`↳ page_size` |  `int`   
Optional. The maximum number of items to return. The maximum value is 1000; values above 1000 will be coerced to 1000. If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more token auth users left to be queried.  
`↳ page_token` |  `string`   
Optional. The `next_page_token` value returned from a previous `ListTokenAuthUsers` request, if any.  
`↳ filter` |  `string`   
Optional. Expression for filtering results.  
`↳ order_by` |  `string`   
Optional. Sort results by a defined order.  
  
### getParent

Required. The parent to list token auth users from.

Format: projects/{project}/locations/{location}/instances/{instance}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The parent to list token auth users from.

Format: projects/{project}/locations/{location}/instances/{instance}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. The maximum number of items to return. The maximum value is 1000; values above 1000 will be coerced to 1000. If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more token auth users left to be queried.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. The maximum number of items to return. The maximum value is 1000; values above 1000 will be coerced to 1000. If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more token auth users left to be queried.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. The `next_page_token` value returned from a previous `ListTokenAuthUsers` request, if any.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. The `next_page_token` value returned from a previous `ListTokenAuthUsers` request, if any.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. Expression for filtering results.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. Expression for filtering results.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. Sort results by a defined order.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. Sort results by a defined order.

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
Required. The parent to list token auth users from. Format: projects/{project}/locations/{location}/instances/{instance} Please see MemorystoreClient::instanceName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListTokenAuthUsersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.ListTokenAuthUsersRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
