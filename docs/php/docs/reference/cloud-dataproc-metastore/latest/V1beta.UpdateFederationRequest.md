---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.UpdateFederationRequest
title: Google Cloud Dataproc Metastore V1beta Client - Class UpdateFederationRequest (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:00.930638+00:00
---

# Google Cloud Dataproc Metastore V1beta Client - Class UpdateFederationRequest (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.UpdateFederationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1beta Client - Class UpdateFederationRequest (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1beta Client class UpdateFederationRequest.

Request message for UpdateFederation.

Generated from protobuf message `google.cloud.metastore.v1beta.UpdateFederationRequest`

## Namespace

Google \ Cloud \ Metastore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`↳ federation` |  `[Federation](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Federation)`   
Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore federation's `name` field is used to identify the metastore service to be updated.  
`↳ request_id` |  `string`   
Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request. For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments. The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.  
  
### getUpdateMask

Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update.

Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update.

Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFederation

Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`.

The metastore federation's `name` field is used to identify the metastore service to be updated.

**Returns**  
---  
**Type** | **Description**  
`[Federation](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Federation)|null` |   
  
### hasFederation

### clearFederation

### setFederation

Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`.

The metastore federation's `name` field is used to identify the metastore service to be updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Federation](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Federation)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRequestId

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments. The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRequestId

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments. The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`federation` |  `[Federation](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Federation)`   
Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore federation's `name` field is used to identify the metastore service to be updated.  
`updateMask` |  `Google\Protobuf\FieldMask`   
Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateFederationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.UpdateFederationRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
