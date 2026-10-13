---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.ListWorkflowConfigsRequest
title: Google Cloud Dataform V1beta1 Client - Class ListWorkflowConfigsRequest (0.17.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:46.083607+00:00
---

# Google Cloud Dataform V1beta1 Client - Class ListWorkflowConfigsRequest (0.17.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.ListWorkflowConfigsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataform V1beta1 Client - Class ListWorkflowConfigsRequest (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.3  0.12.0  0.11.0  0.10.1  0.9.2  0.8.1  0.7.0  0.6.0  0.5.1  0.4.7  0.3.0  0.2.3  0.1.6 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataform V1beta1 Client class ListWorkflowConfigsRequest.

`ListWorkflowConfigs` request message.

Generated from protobuf message `google.cloud.dataform.v1beta1.ListWorkflowConfigsRequest`

## Namespace

Google \ Cloud \ Dataform \ V1beta1

## Methods 

### __construct

Constructor.

**Parameter**  
---  
**Name** | **Description**  
`data` |  `mixed`   
  
  
### getParent

Required. The repository in which to list workflow configs. Must be in the format `projects/*/locations/*/repositories/*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The repository in which to list workflow configs. Must be in the format `projects/*/locations/*/repositories/*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. Maximum number of workflow configs to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. Maximum number of workflow configs to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. Page token received from a previous `ListWorkflowConfigs` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListWorkflowConfigs`, with the exception of `page_size`, must match the call that provided the page token.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. Page token received from a previous `ListWorkflowConfigs` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListWorkflowConfigs`, with the exception of `page_size`, must match the call that provided the page token.

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
Required. The repository in which to list workflow configs. Must be in the format `projects/*/locations/*/repositories/*`. Please see DataformClient::repositoryName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkflowConfigsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.ListWorkflowConfigsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
