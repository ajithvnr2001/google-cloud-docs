---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubcurate-class
title: Class protos.google.cloud.apihub.v1.ApiHubCurate (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:41.991727+00:00
---

# Class protos.google.cloud.apihub.v1.ApiHubCurate (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubcurate-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.ApiHubCurate (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ApiHubCurate

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.ApiHubCurate

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ApiHubCurate service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ApiHubCurate;

Creates new ApiHubCurate service using the specified rpc implementation.

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
`[ApiHubCurate](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubcurate-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCuration(request, callback)
    
    
    public createCuration(request: google.cloud.apihub.v1.ICreateCurationRequest, callback: google.cloud.apihub.v1.ApiHubCurate.CreateCurationCallback): void;

Calls CreateCuration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatecurationrequest)`   
CreateCurationRequest message or plain object  
`callback` |  `[CreateCurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Curation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCuration(request)
    
    
    public createCuration(request: google.cloud.apihub.v1.ICreateCurationRequest): Promise<google.cloud.apihub.v1.Curation>;

Calls CreateCuration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatecurationrequest)`   
CreateCurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Curation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.curation-class)>` | Promise  
  
### deleteCuration(request, callback)
    
    
    public deleteCuration(request: google.cloud.apihub.v1.IDeleteCurationRequest, callback: google.cloud.apihub.v1.ApiHubCurate.DeleteCurationCallback): void;

Calls DeleteCuration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletecurationrequest)`   
DeleteCurationRequest message or plain object  
`callback` |  `[DeleteCurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCuration(request)
    
    
    public deleteCuration(request: google.cloud.apihub.v1.IDeleteCurationRequest): Promise<google.protobuf.Empty>;

Calls DeleteCuration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletecurationrequest)`   
DeleteCurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### getCuration(request, callback)
    
    
    public getCuration(request: google.cloud.apihub.v1.IGetCurationRequest, callback: google.cloud.apihub.v1.ApiHubCurate.GetCurationCallback): void;

Calls GetCuration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetcurationrequest)`   
GetCurationRequest message or plain object  
`callback` |  `[GetCurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Curation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCuration(request)
    
    
    public getCuration(request: google.cloud.apihub.v1.IGetCurationRequest): Promise<google.cloud.apihub.v1.Curation>;

Calls GetCuration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetcurationrequest)`   
GetCurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Curation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.curation-class)>` | Promise  
  
### listCurations(request, callback)
    
    
    public listCurations(request: google.cloud.apihub.v1.IListCurationsRequest, callback: google.cloud.apihub.v1.ApiHubCurate.ListCurationsCallback): void;

Calls ListCurations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCurationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistcurationsrequest)`   
ListCurationsRequest message or plain object  
`callback` |  `[ListCurationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCurationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCurations(request)
    
    
    public listCurations(request: google.cloud.apihub.v1.IListCurationsRequest): Promise<google.cloud.apihub.v1.ListCurationsResponse>;

Calls ListCurations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCurationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistcurationsrequest)`   
ListCurationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListCurationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listcurationsresponse)>` | Promise  
  
### updateCuration(request, callback)
    
    
    public updateCuration(request: google.cloud.apihub.v1.IUpdateCurationRequest, callback: google.cloud.apihub.v1.ApiHubCurate.UpdateCurationCallback): void;

Calls UpdateCuration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatecurationrequest)`   
UpdateCurationRequest message or plain object  
`callback` |  `[UpdateCurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Curation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCuration(request)
    
    
    public updateCuration(request: google.cloud.apihub.v1.IUpdateCurationRequest): Promise<google.cloud.apihub.v1.Curation>;

Calls UpdateCuration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatecurationrequest)`   
UpdateCurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Curation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.curation-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
