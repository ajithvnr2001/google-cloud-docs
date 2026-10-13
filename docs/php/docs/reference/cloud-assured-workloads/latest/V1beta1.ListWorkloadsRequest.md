---
url: https://docs.cloud.google.com/php/docs/reference/cloud-assured-workloads/latest/V1beta1.ListWorkloadsRequest
title: Google Cloud Assured Workloads V1beta1 Client - Class ListWorkloadsRequest (1.2.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:01.134734+00:00
---

# Google Cloud Assured Workloads V1beta1 Client - Class ListWorkloadsRequest (1.2.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-assured-workloads/latest/V1beta1.ListWorkloadsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Assured Workloads V1beta1 Client - Class ListWorkloadsRequest (1.2.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.3 (latest)  1.1.3  1.0.5  0.11.5  0.10.2  0.9.1  0.8.3  0.7.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Assured Workloads V1beta1 Client class ListWorkloadsRequest.

Request for fetching workloads in an organization.

Generated from protobuf message `google.cloud.assuredworkloads.v1beta1.ListWorkloadsRequest`

## Namespace

Google \ Cloud \ AssuredWorkloads \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`.  
`↳ page_size` |  `int`   
Page size.  
`↳ page_token` |  `string`   
Page token returned from previous request. Page token contains context from previous request. Page token needs to be passed in the second and following requests.  
`↳ filter` |  `string`   
A custom filter for filtering by properties of a workload. At this time, only filtering by labels is supported.  
  
### getParent

Required. Parent Resource to list workloads from.

Must be of the form `organizations/{org_id}/locations/{location}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Parent Resource to list workloads from.

Must be of the form `organizations/{org_id}/locations/{location}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Page size.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Page size.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Page token returned from previous request. Page token contains context from previous request. Page token needs to be passed in the second and following requests.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Page token returned from previous request. Page token contains context from previous request. Page token needs to be passed in the second and following requests.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

A custom filter for filtering by properties of a workload. At this time, only filtering by labels is supported.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

A custom filter for filtering by properties of a workload. At this time, only filtering by labels is supported.

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
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`. Please see AssuredWorkloadsServiceClient::locationName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkloadsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-assured-workloads/latest/V1beta1.ListWorkloadsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
