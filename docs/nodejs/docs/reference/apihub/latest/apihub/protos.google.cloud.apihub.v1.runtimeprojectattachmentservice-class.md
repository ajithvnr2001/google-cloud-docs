---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.runtimeprojectattachmentservice-class
title: Class protos.google.cloud.apihub.v1.RuntimeProjectAttachmentService (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:38.684525+00:00
---

# Class protos.google.cloud.apihub.v1.RuntimeProjectAttachmentService (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.runtimeprojectattachmentservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.RuntimeProjectAttachmentService (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a RuntimeProjectAttachmentService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.RuntimeProjectAttachmentService

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RuntimeProjectAttachmentService service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RuntimeProjectAttachmentService;

Creates new RuntimeProjectAttachmentService service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeProjectAttachmentService](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.runtimeprojectattachmentservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createRuntimeProjectAttachment(request, callback)
    
    
    public createRuntimeProjectAttachment(request: google.cloud.apihub.v1.ICreateRuntimeProjectAttachmentRequest, callback: google.cloud.apihub.v1.RuntimeProjectAttachmentService.CreateRuntimeProjectAttachmentCallback): void;

Calls CreateRuntimeProjectAttachment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateruntimeprojectattachmentrequest)`   
CreateRuntimeProjectAttachmentRequest message or plain object  
`callback` |  `[CreateRuntimeProjectAttachmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and RuntimeProjectAttachment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRuntimeProjectAttachment(request)
    
    
    public createRuntimeProjectAttachment(request: google.cloud.apihub.v1.ICreateRuntimeProjectAttachmentRequest): Promise<google.cloud.apihub.v1.RuntimeProjectAttachment>;

Calls CreateRuntimeProjectAttachment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateruntimeprojectattachmentrequest)`   
CreateRuntimeProjectAttachmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.RuntimeProjectAttachment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.runtimeprojectattachment)>` | Promise  
  
### deleteRuntimeProjectAttachment(request, callback)
    
    
    public deleteRuntimeProjectAttachment(request: google.cloud.apihub.v1.IDeleteRuntimeProjectAttachmentRequest, callback: google.cloud.apihub.v1.RuntimeProjectAttachmentService.DeleteRuntimeProjectAttachmentCallback): void;

Calls DeleteRuntimeProjectAttachment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteruntimeprojectattachmentrequest)`   
DeleteRuntimeProjectAttachmentRequest message or plain object  
`callback` |  `[DeleteRuntimeProjectAttachmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRuntimeProjectAttachment(request)
    
    
    public deleteRuntimeProjectAttachment(request: google.cloud.apihub.v1.IDeleteRuntimeProjectAttachmentRequest): Promise<google.protobuf.Empty>;

Calls DeleteRuntimeProjectAttachment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteruntimeprojectattachmentrequest)`   
DeleteRuntimeProjectAttachmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### getRuntimeProjectAttachment(request, callback)
    
    
    public getRuntimeProjectAttachment(request: google.cloud.apihub.v1.IGetRuntimeProjectAttachmentRequest, callback: google.cloud.apihub.v1.RuntimeProjectAttachmentService.GetRuntimeProjectAttachmentCallback): void;

Calls GetRuntimeProjectAttachment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetruntimeprojectattachmentrequest)`   
GetRuntimeProjectAttachmentRequest message or plain object  
`callback` |  `[GetRuntimeProjectAttachmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and RuntimeProjectAttachment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRuntimeProjectAttachment(request)
    
    
    public getRuntimeProjectAttachment(request: google.cloud.apihub.v1.IGetRuntimeProjectAttachmentRequest): Promise<google.cloud.apihub.v1.RuntimeProjectAttachment>;

Calls GetRuntimeProjectAttachment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetruntimeprojectattachmentrequest)`   
GetRuntimeProjectAttachmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.RuntimeProjectAttachment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.runtimeprojectattachment)>` | Promise  
  
### listRuntimeProjectAttachments(request, callback)
    
    
    public listRuntimeProjectAttachments(request: google.cloud.apihub.v1.IListRuntimeProjectAttachmentsRequest, callback: google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachmentsCallback): void;

Calls ListRuntimeProjectAttachments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRuntimeProjectAttachmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistruntimeprojectattachmentsrequest)`   
ListRuntimeProjectAttachmentsRequest message or plain object  
`callback` |  `[ListRuntimeProjectAttachmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRuntimeProjectAttachmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRuntimeProjectAttachments(request)
    
    
    public listRuntimeProjectAttachments(request: google.cloud.apihub.v1.IListRuntimeProjectAttachmentsRequest): Promise<google.cloud.apihub.v1.ListRuntimeProjectAttachmentsResponse>;

Calls ListRuntimeProjectAttachments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRuntimeProjectAttachmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistruntimeprojectattachmentsrequest)`   
ListRuntimeProjectAttachmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListRuntimeProjectAttachmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listruntimeprojectattachmentsresponse)>` | Promise  
  
### lookupRuntimeProjectAttachment(request, callback)
    
    
    public lookupRuntimeProjectAttachment(request: google.cloud.apihub.v1.ILookupRuntimeProjectAttachmentRequest, callback: google.cloud.apihub.v1.RuntimeProjectAttachmentService.LookupRuntimeProjectAttachmentCallback): void;

Calls LookupRuntimeProjectAttachment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilookupruntimeprojectattachmentrequest)`   
LookupRuntimeProjectAttachmentRequest message or plain object  
`callback` |  `[LookupRuntimeProjectAttachmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and LookupRuntimeProjectAttachmentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupRuntimeProjectAttachment(request)
    
    
    public lookupRuntimeProjectAttachment(request: google.cloud.apihub.v1.ILookupRuntimeProjectAttachmentRequest): Promise<google.cloud.apihub.v1.LookupRuntimeProjectAttachmentResponse>;

Calls LookupRuntimeProjectAttachment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupRuntimeProjectAttachmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilookupruntimeprojectattachmentrequest)`   
LookupRuntimeProjectAttachmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.LookupRuntimeProjectAttachmentResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.lookupruntimeprojectattachmentresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
