---
url: https://docs.cloud.google.com/php/docs/reference/cloud-configdelivery/latest/V1beta.ListFleetPackagesRequest
title: Google Cloud Config Delivery V1beta Client - Class ListFleetPackagesRequest (0.4.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:54.363569+00:00
---

# Google Cloud Config Delivery V1beta Client - Class ListFleetPackagesRequest (0.4.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-configdelivery/latest/V1beta.ListFleetPackagesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Config Delivery V1beta Client - Class ListFleetPackagesRequest (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.3.3  0.2.1  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Config Delivery V1beta Client class ListFleetPackagesRequest.

Message for requesting list of FleetPackage.

Generated from protobuf message `google.cloud.configdelivery.v1beta.ListFleetPackagesRequest`

## Namespace

Google \ Cloud \ ConfigDelivery \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Parent value for ListFleetPackagesRequest.  
`↳ page_size` |  `int`   
Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`↳ page_token` |  `string`   
Optional. A token identifying a page of results the server should return.  
`↳ filter` |  `string`   
Optional. Filtering results  
`↳ order_by` |  `string`   
Optional. Hint for how to order the results  
  
### getParent

Required. Parent value for ListFleetPackagesRequest.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Parent value for ListFleetPackagesRequest.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. A token identifying a page of results the server should return.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. A token identifying a page of results the server should return.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. Filtering results

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. Filtering results

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. Hint for how to order the results

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. Hint for how to order the results

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
Required. Parent value for ListFleetPackagesRequest. Please see ConfigDeliveryClient::locationName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListFleetPackagesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-configdelivery/latest/V1beta.ListFleetPackagesRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
