---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.transitionroutegroups-class
title: Class protos.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:40.926602+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.transitionroutegroups-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a TransitionRouteGroups

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new TransitionRouteGroups service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): TransitionRouteGroups;

Creates new TransitionRouteGroups service using the specified rpc implementation.

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
`[TransitionRouteGroups](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.transitionroutegroups-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createTransitionRouteGroup(request, callback)
    
    
    public createTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.ICreateTransitionRouteGroupRequest, callback: google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.CreateTransitionRouteGroupCallback): void;

Calls CreateTransitionRouteGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreatetransitionroutegrouprequest)`   
CreateTransitionRouteGroupRequest message or plain object  
`callback` |  `[CreateTransitionRouteGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and TransitionRouteGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTransitionRouteGroup(request)
    
    
    public createTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.ICreateTransitionRouteGroupRequest): Promise<google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup>;

Calls CreateTransitionRouteGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreatetransitionroutegrouprequest)`   
CreateTransitionRouteGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.transitionroutegroup)>` | Promise  
  
### deleteTransitionRouteGroup(request, callback)
    
    
    public deleteTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.IDeleteTransitionRouteGroupRequest, callback: google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.DeleteTransitionRouteGroupCallback): void;

Calls DeleteTransitionRouteGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideletetransitionroutegrouprequest)`   
DeleteTransitionRouteGroupRequest message or plain object  
`callback` |  `[DeleteTransitionRouteGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTransitionRouteGroup(request)
    
    
    public deleteTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.IDeleteTransitionRouteGroupRequest): Promise<google.protobuf.Empty>;

Calls DeleteTransitionRouteGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideletetransitionroutegrouprequest)`   
DeleteTransitionRouteGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty)>` | Promise  
  
### getTransitionRouteGroup(request, callback)
    
    
    public getTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.IGetTransitionRouteGroupRequest, callback: google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.GetTransitionRouteGroupCallback): void;

Calls GetTransitionRouteGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igettransitionroutegrouprequest)`   
GetTransitionRouteGroupRequest message or plain object  
`callback` |  `[GetTransitionRouteGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and TransitionRouteGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTransitionRouteGroup(request)
    
    
    public getTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.IGetTransitionRouteGroupRequest): Promise<google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup>;

Calls GetTransitionRouteGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igettransitionroutegrouprequest)`   
GetTransitionRouteGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.transitionroutegroup)>` | Promise  
  
### listTransitionRouteGroups(request, callback)
    
    
    public listTransitionRouteGroups(request: google.cloud.dialogflow.cx.v3beta1.IListTransitionRouteGroupsRequest, callback: google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.ListTransitionRouteGroupsCallback): void;

Calls ListTransitionRouteGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTransitionRouteGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilisttransitionroutegroupsrequest)`   
ListTransitionRouteGroupsRequest message or plain object  
`callback` |  `[ListTransitionRouteGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTransitionRouteGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTransitionRouteGroups(request)
    
    
    public listTransitionRouteGroups(request: google.cloud.dialogflow.cx.v3beta1.IListTransitionRouteGroupsRequest): Promise<google.cloud.dialogflow.cx.v3beta1.ListTransitionRouteGroupsResponse>;

Calls ListTransitionRouteGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTransitionRouteGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilisttransitionroutegroupsrequest)`   
ListTransitionRouteGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3beta1.ListTransitionRouteGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.listtransitionroutegroupsresponse)>` | Promise  
  
### updateTransitionRouteGroup(request, callback)
    
    
    public updateTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.IUpdateTransitionRouteGroupRequest, callback: google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.UpdateTransitionRouteGroupCallback): void;

Calls UpdateTransitionRouteGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdatetransitionroutegrouprequest)`   
UpdateTransitionRouteGroupRequest message or plain object  
`callback` |  `[UpdateTransitionRouteGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and TransitionRouteGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTransitionRouteGroup(request)
    
    
    public updateTransitionRouteGroup(request: google.cloud.dialogflow.cx.v3beta1.IUpdateTransitionRouteGroupRequest): Promise<google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup>;

Calls UpdateTransitionRouteGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTransitionRouteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdatetransitionroutegrouprequest)`   
UpdateTransitionRouteGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.transitionroutegroup)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
