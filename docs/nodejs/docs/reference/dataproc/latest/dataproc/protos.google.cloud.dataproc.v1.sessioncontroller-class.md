---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessioncontroller-class
title: Class protos.google.cloud.dataproc.v1.SessionController (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:59.836442+00:00
---

# Class protos.google.cloud.dataproc.v1.SessionController (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessioncontroller-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.SessionController (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a SessionController

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataproc.v1.SessionController

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SessionController service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SessionController;

Creates new SessionController service using the specified rpc implementation.

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
`[SessionController](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessioncontroller-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSession(request, callback)
    
    
    public createSession(request: google.cloud.dataproc.v1.ICreateSessionRequest, callback: google.cloud.dataproc.v1.SessionController.CreateSessionCallback): void;

Calls CreateSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatesessionrequest)`   
CreateSessionRequest message or plain object  
`callback` |  `[CreateSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSession(request)
    
    
    public createSession(request: google.cloud.dataproc.v1.ICreateSessionRequest): Promise<google.longrunning.Operation>;

Calls CreateSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatesessionrequest)`   
CreateSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### deleteSession(request, callback)
    
    
    public deleteSession(request: google.cloud.dataproc.v1.IDeleteSessionRequest, callback: google.cloud.dataproc.v1.SessionController.DeleteSessionCallback): void;

Calls DeleteSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletesessionrequest)`   
DeleteSessionRequest message or plain object  
`callback` |  `[DeleteSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSession(request)
    
    
    public deleteSession(request: google.cloud.dataproc.v1.IDeleteSessionRequest): Promise<google.longrunning.Operation>;

Calls DeleteSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletesessionrequest)`   
DeleteSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### getSession(request, callback)
    
    
    public getSession(request: google.cloud.dataproc.v1.IGetSessionRequest, callback: google.cloud.dataproc.v1.SessionController.GetSessionCallback): void;

Calls GetSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetsessionrequest)`   
GetSessionRequest message or plain object  
`callback` |  `[GetSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Session  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSession(request)
    
    
    public getSession(request: google.cloud.dataproc.v1.IGetSessionRequest): Promise<google.cloud.dataproc.v1.Session>;

Calls GetSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetsessionrequest)`   
GetSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.Session](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class)>` | Promise  
  
### listSessions(request, callback)
    
    
    public listSessions(request: google.cloud.dataproc.v1.IListSessionsRequest, callback: google.cloud.dataproc.v1.SessionController.ListSessionsCallback): void;

Calls ListSessions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistsessionsrequest)`   
ListSessionsRequest message or plain object  
`callback` |  `[ListSessionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSessionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSessions(request)
    
    
    public listSessions(request: google.cloud.dataproc.v1.IListSessionsRequest): Promise<google.cloud.dataproc.v1.ListSessionsResponse>;

Calls ListSessions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistsessionsrequest)`   
ListSessionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.ListSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.listsessionsresponse)>` | Promise  
  
### terminateSession(request, callback)
    
    
    public terminateSession(request: google.cloud.dataproc.v1.ITerminateSessionRequest, callback: google.cloud.dataproc.v1.SessionController.TerminateSessionCallback): void;

Calls TerminateSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITerminateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iterminatesessionrequest)`   
TerminateSessionRequest message or plain object  
`callback` |  `[TerminateSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### terminateSession(request)
    
    
    public terminateSession(request: google.cloud.dataproc.v1.ITerminateSessionRequest): Promise<google.longrunning.Operation>;

Calls TerminateSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITerminateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iterminatesessionrequest)`   
TerminateSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
