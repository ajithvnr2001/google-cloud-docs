---
url: https://docs.cloud.google.com/php/docs/reference/cloud-networkservices/latest/V1beta1.ListEndpointPoliciesRequest
title: Google Cloud Network Services V1beta1 Client - Class ListEndpointPoliciesRequest (0.13.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:09.228383+00:00
---

# Google Cloud Network Services V1beta1 Client - Class ListEndpointPoliciesRequest (0.13.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-networkservices/latest/V1beta1.ListEndpointPoliciesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Network Services V1beta1 Client - Class ListEndpointPoliciesRequest (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.10.0  0.8.2  0.7.1  0.6.1  0.5.0  0.4.0  0.3.0  0.2.3  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Network Services V1beta1 Client class ListEndpointPoliciesRequest.

Request used with the ListEndpointPolicies method.

Generated from protobuf message `google.cloud.networkservices.v1beta1.ListEndpointPoliciesRequest`

## Namespace

Google \ Cloud \ NetworkServices \ V1beta1

## Methods 

### __construct

Constructor.

**Parameter**  
---  
**Name** | **Description**  
`data` |  `mixed`   
  
  
### getParent

Required. The project and location from which the EndpointPolicies should be listed, specified in the format `projects/*/locations/global`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The project and location from which the EndpointPolicies should be listed, specified in the format `projects/*/locations/global`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Maximum number of EndpointPolicies to return per call.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Maximum number of EndpointPolicies to return per call.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

The value returned by the last `ListEndpointPoliciesResponse` Indicates that this is a continuation of a prior `ListEndpointPolicies` call, and that the system should return the next page of data.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

The value returned by the last `ListEndpointPoliciesResponse` Indicates that this is a continuation of a prior `ListEndpointPolicies` call, and that the system should return the next page of data.

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
Required. The project and location from which the EndpointPolicies should be listed, specified in the format `projects/*/locations/global`. Please see NetworkServicesClient::locationName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListEndpointPoliciesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-networkservices/latest/V1beta1.ListEndpointPoliciesRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
