---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.dataprocmetastorefederation-class
title: Class protos.google.cloud.metastore.v1alpha.DataprocMetastoreFederation (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:14.017801+00:00
---

# Class protos.google.cloud.metastore.v1alpha.DataprocMetastoreFederation (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.dataprocmetastorefederation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.metastore.v1alpha.DataprocMetastoreFederation (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  4.1.0  3.5.0  3.4.1  3.1.2  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.6 

Represents a DataprocMetastoreFederation

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.metastore.v1alpha.DataprocMetastoreFederation

## Package

[@google-cloud/dataproc-metastore](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataprocMetastoreFederation service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataprocMetastoreFederation;

Creates new DataprocMetastoreFederation service using the specified rpc implementation.

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
`[DataprocMetastoreFederation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.dataprocmetastorefederation-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createFederation(request, callback)
    
    
    public createFederation(request: google.cloud.metastore.v1alpha.ICreateFederationRequest, callback: google.cloud.metastore.v1alpha.DataprocMetastoreFederation.CreateFederationCallback): void;

Calls CreateFederation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.icreatefederationrequest)`   
CreateFederationRequest message or plain object  
`callback` |  `[CreateFederationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFederation(request)
    
    
    public createFederation(request: google.cloud.metastore.v1alpha.ICreateFederationRequest): Promise<google.longrunning.Operation>;

Calls CreateFederation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.icreatefederationrequest)`   
CreateFederationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.longrunning.operation)>` | Promise  
  
### deleteFederation(request, callback)
    
    
    public deleteFederation(request: google.cloud.metastore.v1alpha.IDeleteFederationRequest, callback: google.cloud.metastore.v1alpha.DataprocMetastoreFederation.DeleteFederationCallback): void;

Calls DeleteFederation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.ideletefederationrequest)`   
DeleteFederationRequest message or plain object  
`callback` |  `[DeleteFederationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFederation(request)
    
    
    public deleteFederation(request: google.cloud.metastore.v1alpha.IDeleteFederationRequest): Promise<google.longrunning.Operation>;

Calls DeleteFederation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.ideletefederationrequest)`   
DeleteFederationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.longrunning.operation)>` | Promise  
  
### getFederation(request, callback)
    
    
    public getFederation(request: google.cloud.metastore.v1alpha.IGetFederationRequest, callback: google.cloud.metastore.v1alpha.DataprocMetastoreFederation.GetFederationCallback): void;

Calls GetFederation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.igetfederationrequest)`   
GetFederationRequest message or plain object  
`callback` |  `[GetFederationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)`   
Node-style callback called with the error, if any, and Federation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFederation(request)
    
    
    public getFederation(request: google.cloud.metastore.v1alpha.IGetFederationRequest): Promise<google.cloud.metastore.v1alpha.Federation>;

Calls GetFederation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.igetfederationrequest)`   
GetFederationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.metastore.v1alpha.Federation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.federation-class)>` | Promise  
  
### listFederations(request, callback)
    
    
    public listFederations(request: google.cloud.metastore.v1alpha.IListFederationsRequest, callback: google.cloud.metastore.v1alpha.DataprocMetastoreFederation.ListFederationsCallback): void;

Calls ListFederations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFederationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.ilistfederationsrequest)`   
ListFederationsRequest message or plain object  
`callback` |  `[ListFederationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFederationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFederations(request)
    
    
    public listFederations(request: google.cloud.metastore.v1alpha.IListFederationsRequest): Promise<google.cloud.metastore.v1alpha.ListFederationsResponse>;

Calls ListFederations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFederationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.ilistfederationsrequest)`   
ListFederationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.metastore.v1alpha.ListFederationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.listfederationsresponse)>` | Promise  
  
### updateFederation(request, callback)
    
    
    public updateFederation(request: google.cloud.metastore.v1alpha.IUpdateFederationRequest, callback: google.cloud.metastore.v1alpha.DataprocMetastoreFederation.UpdateFederationCallback): void;

Calls UpdateFederation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.iupdatefederationrequest)`   
UpdateFederationRequest message or plain object  
`callback` |  `[UpdateFederationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFederation(request)
    
    
    public updateFederation(request: google.cloud.metastore.v1alpha.IUpdateFederationRequest): Promise<google.longrunning.Operation>;

Calls UpdateFederation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFederationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1alpha.iupdatefederationrequest)`   
UpdateFederationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
