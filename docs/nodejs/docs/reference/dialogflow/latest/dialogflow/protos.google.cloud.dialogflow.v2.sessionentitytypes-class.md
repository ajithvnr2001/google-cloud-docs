---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.sessionentitytypes-class
title: Class protos.google.cloud.dialogflow.v2.SessionEntityTypes (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:40.727886+00:00
---

# Class protos.google.cloud.dialogflow.v2.SessionEntityTypes (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.sessionentitytypes-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.SessionEntityTypes (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a SessionEntityTypes

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.SessionEntityTypes

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SessionEntityTypes service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SessionEntityTypes;

Creates new SessionEntityTypes service using the specified rpc implementation.

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
`[SessionEntityTypes](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.sessionentitytypes-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSessionEntityType(request, callback)
    
    
    public createSessionEntityType(request: google.cloud.dialogflow.v2.ICreateSessionEntityTypeRequest, callback: google.cloud.dialogflow.v2.SessionEntityTypes.CreateSessionEntityTypeCallback): void;

Calls CreateSessionEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreatesessionentitytyperequest)`   
CreateSessionEntityTypeRequest message or plain object  
`callback` |  `[CreateSessionEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SessionEntityType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSessionEntityType(request)
    
    
    public createSessionEntityType(request: google.cloud.dialogflow.v2.ICreateSessionEntityTypeRequest): Promise<google.cloud.dialogflow.v2.SessionEntityType>;

Calls CreateSessionEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreatesessionentitytyperequest)`   
CreateSessionEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.SessionEntityType](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.sessionentitytype-class)>` | Promise  
  
### deleteSessionEntityType(request, callback)
    
    
    public deleteSessionEntityType(request: google.cloud.dialogflow.v2.IDeleteSessionEntityTypeRequest, callback: google.cloud.dialogflow.v2.SessionEntityTypes.DeleteSessionEntityTypeCallback): void;

Calls DeleteSessionEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideletesessionentitytyperequest)`   
DeleteSessionEntityTypeRequest message or plain object  
`callback` |  `[DeleteSessionEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSessionEntityType(request)
    
    
    public deleteSessionEntityType(request: google.cloud.dialogflow.v2.IDeleteSessionEntityTypeRequest): Promise<google.protobuf.Empty>;

Calls DeleteSessionEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideletesessionentitytyperequest)`   
DeleteSessionEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### getSessionEntityType(request, callback)
    
    
    public getSessionEntityType(request: google.cloud.dialogflow.v2.IGetSessionEntityTypeRequest, callback: google.cloud.dialogflow.v2.SessionEntityTypes.GetSessionEntityTypeCallback): void;

Calls GetSessionEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetsessionentitytyperequest)`   
GetSessionEntityTypeRequest message or plain object  
`callback` |  `[GetSessionEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SessionEntityType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSessionEntityType(request)
    
    
    public getSessionEntityType(request: google.cloud.dialogflow.v2.IGetSessionEntityTypeRequest): Promise<google.cloud.dialogflow.v2.SessionEntityType>;

Calls GetSessionEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetsessionentitytyperequest)`   
GetSessionEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.SessionEntityType](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.sessionentitytype-class)>` | Promise  
  
### listSessionEntityTypes(request, callback)
    
    
    public listSessionEntityTypes(request: google.cloud.dialogflow.v2.IListSessionEntityTypesRequest, callback: google.cloud.dialogflow.v2.SessionEntityTypes.ListSessionEntityTypesCallback): void;

Calls ListSessionEntityTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionEntityTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistsessionentitytypesrequest)`   
ListSessionEntityTypesRequest message or plain object  
`callback` |  `[ListSessionEntityTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSessionEntityTypesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSessionEntityTypes(request)
    
    
    public listSessionEntityTypes(request: google.cloud.dialogflow.v2.IListSessionEntityTypesRequest): Promise<google.cloud.dialogflow.v2.ListSessionEntityTypesResponse>;

Calls ListSessionEntityTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSessionEntityTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistsessionentitytypesrequest)`   
ListSessionEntityTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListSessionEntityTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listsessionentitytypesresponse)>` | Promise  
  
### updateSessionEntityType(request, callback)
    
    
    public updateSessionEntityType(request: google.cloud.dialogflow.v2.IUpdateSessionEntityTypeRequest, callback: google.cloud.dialogflow.v2.SessionEntityTypes.UpdateSessionEntityTypeCallback): void;

Calls UpdateSessionEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdatesessionentitytyperequest)`   
UpdateSessionEntityTypeRequest message or plain object  
`callback` |  `[UpdateSessionEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SessionEntityType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSessionEntityType(request)
    
    
    public updateSessionEntityType(request: google.cloud.dialogflow.v2.IUpdateSessionEntityTypeRequest): Promise<google.cloud.dialogflow.v2.SessionEntityType>;

Calls UpdateSessionEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdatesessionentitytyperequest)`   
UpdateSessionEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.SessionEntityType](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.sessionentitytype-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
