---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.siptrunks-class
title: Class protos.google.cloud.dialogflow.v2beta1.SipTrunks (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:45.826689+00:00
---

# Class protos.google.cloud.dialogflow.v2beta1.SipTrunks (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.siptrunks-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2beta1.SipTrunks (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a SipTrunks

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2beta1.SipTrunks

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SipTrunks service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SipTrunks;

Creates new SipTrunks service using the specified rpc implementation.

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
`[SipTrunks](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.siptrunks-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSipTrunk(request, callback)
    
    
    public createSipTrunk(request: google.cloud.dialogflow.v2beta1.ICreateSipTrunkRequest, callback: google.cloud.dialogflow.v2beta1.SipTrunks.CreateSipTrunkCallback): void;

Calls CreateSipTrunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreatesiptrunkrequest)`   
CreateSipTrunkRequest message or plain object  
`callback` |  `[CreateSipTrunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SipTrunk  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSipTrunk(request)
    
    
    public createSipTrunk(request: google.cloud.dialogflow.v2beta1.ICreateSipTrunkRequest): Promise<google.cloud.dialogflow.v2beta1.SipTrunk>;

Calls CreateSipTrunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreatesiptrunkrequest)`   
CreateSipTrunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2beta1.SipTrunk](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.siptrunk-class)>` | Promise  
  
### deleteSipTrunk(request, callback)
    
    
    public deleteSipTrunk(request: google.cloud.dialogflow.v2beta1.IDeleteSipTrunkRequest, callback: google.cloud.dialogflow.v2beta1.SipTrunks.DeleteSipTrunkCallback): void;

Calls DeleteSipTrunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideletesiptrunkrequest)`   
DeleteSipTrunkRequest message or plain object  
`callback` |  `[DeleteSipTrunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSipTrunk(request)
    
    
    public deleteSipTrunk(request: google.cloud.dialogflow.v2beta1.IDeleteSipTrunkRequest): Promise<google.protobuf.Empty>;

Calls DeleteSipTrunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideletesiptrunkrequest)`   
DeleteSipTrunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### getSipTrunk(request, callback)
    
    
    public getSipTrunk(request: google.cloud.dialogflow.v2beta1.IGetSipTrunkRequest, callback: google.cloud.dialogflow.v2beta1.SipTrunks.GetSipTrunkCallback): void;

Calls GetSipTrunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetsiptrunkrequest)`   
GetSipTrunkRequest message or plain object  
`callback` |  `[GetSipTrunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SipTrunk  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSipTrunk(request)
    
    
    public getSipTrunk(request: google.cloud.dialogflow.v2beta1.IGetSipTrunkRequest): Promise<google.cloud.dialogflow.v2beta1.SipTrunk>;

Calls GetSipTrunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetsiptrunkrequest)`   
GetSipTrunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2beta1.SipTrunk](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.siptrunk-class)>` | Promise  
  
### listSipTrunks(request, callback)
    
    
    public listSipTrunks(request: google.cloud.dialogflow.v2beta1.IListSipTrunksRequest, callback: google.cloud.dialogflow.v2beta1.SipTrunks.ListSipTrunksCallback): void;

Calls ListSipTrunks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSipTrunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistsiptrunksrequest)`   
ListSipTrunksRequest message or plain object  
`callback` |  `[ListSipTrunksCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSipTrunksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSipTrunks(request)
    
    
    public listSipTrunks(request: google.cloud.dialogflow.v2beta1.IListSipTrunksRequest): Promise<google.cloud.dialogflow.v2beta1.ListSipTrunksResponse>;

Calls ListSipTrunks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSipTrunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistsiptrunksrequest)`   
ListSipTrunksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2beta1.ListSipTrunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.listsiptrunksresponse)>` | Promise  
  
### updateSipTrunk(request, callback)
    
    
    public updateSipTrunk(request: google.cloud.dialogflow.v2beta1.IUpdateSipTrunkRequest, callback: google.cloud.dialogflow.v2beta1.SipTrunks.UpdateSipTrunkCallback): void;

Calls UpdateSipTrunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdatesiptrunkrequest)`   
UpdateSipTrunkRequest message or plain object  
`callback` |  `[UpdateSipTrunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SipTrunk  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSipTrunk(request)
    
    
    public updateSipTrunk(request: google.cloud.dialogflow.v2beta1.IUpdateSipTrunkRequest): Promise<google.cloud.dialogflow.v2beta1.SipTrunk>;

Calls UpdateSipTrunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSipTrunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdatesiptrunkrequest)`   
UpdateSipTrunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2beta1.SipTrunk](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.siptrunk-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
