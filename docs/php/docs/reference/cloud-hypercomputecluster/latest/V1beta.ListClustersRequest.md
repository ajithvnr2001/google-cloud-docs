---
url: https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.ListClustersRequest
title: Google Cloud Hypercompute Cluster V1beta Client - Class ListClustersRequest (0.4.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:17.100632+00:00
---

# Google Cloud Hypercompute Cluster V1beta Client - Class ListClustersRequest (0.4.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.ListClustersRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Hypercompute Cluster V1beta Client - Class ListClustersRequest (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.3.1  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Hypercompute Cluster V1beta Client class ListClustersRequest.

Request message for [ListClusters](https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.Client.HypercomputeClusterClient#_Google_Cloud_HypercomputeCluster_V1beta_Client_HypercomputeClusterClient__listClusters__).

Generated from protobuf message `google.cloud.hypercomputecluster.v1beta.ListClustersRequest`

## Namespace

Google \ Cloud \ HypercomputeCluster \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Parent location of the clusters to list, in the format `projects/{project}/locations/{location}`.  
`↳ page_size` |  `int`   
Optional. Maximum number of clusters to return. The service may return fewer than this value.  
`↳ page_token` |  `string`   
Optional. A page token received from a previous `ListClusters` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListClusters` must match the call that provided the page token.  
`↳ filter` |  `string`   
Optional. [Filter](https://google.aip.dev/160) to apply to the returned results.  
`↳ order_by` |  `string`   
Optional. How to order the resulting clusters. Must be one of the following strings: * * `name` * * `name desc` * * `create_time` * * `create_time desc` If not specified, clusters will be returned in an arbitrary order.  
  
### getParent

Required. Parent location of the clusters to list, in the format `projects/{project}/locations/{location}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Parent location of the clusters to list, in the format `projects/{project}/locations/{location}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. Maximum number of clusters to return. The service may return fewer than this value.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. Maximum number of clusters to return. The service may return fewer than this value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. A page token received from a previous `ListClusters` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListClusters` must match the call that provided the page token.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. A page token received from a previous `ListClusters` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListClusters` must match the call that provided the page token.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. [Filter](https://google.aip.dev/160) to apply to the returned results.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. [Filter](https://google.aip.dev/160) to apply to the returned results.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. How to order the resulting clusters. Must be one of the following strings:

  * `name`
  * `name desc`
  * `create_time`
  * `create_time desc` If not specified, clusters will be returned in an arbitrary order.



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. How to order the resulting clusters. Must be one of the following strings:

  * `name`
  * `name desc`
  * `create_time`
  * `create_time desc` If not specified, clusters will be returned in an arbitrary order.



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
Required. Parent location of the clusters to list, in the format `projects/{project}/locations/{location}`. Please see HypercomputeClusterClient::locationName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListClustersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.ListClustersRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
