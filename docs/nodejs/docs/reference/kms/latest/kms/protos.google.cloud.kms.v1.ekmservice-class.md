---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmservice-class
title: Class protos.google.cloud.kms.v1.EkmService (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:49.207449+00:00
---

# Class protos.google.cloud.kms.v1.EkmService (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.EkmService (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents an EkmService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.kms.v1.EkmService

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new EkmService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): EkmService;

Creates new EkmService service using the specified rpc implementation.

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
`[EkmService](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createEkmConnection(request, callback)
    
    
    public createEkmConnection(request: google.cloud.kms.v1.ICreateEkmConnectionRequest, callback: google.cloud.kms.v1.EkmService.CreateEkmConnectionCallback): void;

Calls CreateEkmConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEkmConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreateekmconnectionrequest)`   
CreateEkmConnectionRequest message or plain object  
`callback` |  `[CreateEkmConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and EkmConnection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEkmConnection(request)
    
    
    public createEkmConnection(request: google.cloud.kms.v1.ICreateEkmConnectionRequest): Promise<google.cloud.kms.v1.EkmConnection>;

Calls CreateEkmConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEkmConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreateekmconnectionrequest)`   
CreateEkmConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.EkmConnection](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmconnection-class)>` | Promise  
  
### getEkmConfig(request, callback)
    
    
    public getEkmConfig(request: google.cloud.kms.v1.IGetEkmConfigRequest, callback: google.cloud.kms.v1.EkmService.GetEkmConfigCallback): void;

Calls GetEkmConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEkmConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetekmconfigrequest)`   
GetEkmConfigRequest message or plain object  
`callback` |  `[GetEkmConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and EkmConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEkmConfig(request)
    
    
    public getEkmConfig(request: google.cloud.kms.v1.IGetEkmConfigRequest): Promise<google.cloud.kms.v1.EkmConfig>;

Calls GetEkmConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEkmConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetekmconfigrequest)`   
GetEkmConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.EkmConfig](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmconfig)>` | Promise  
  
### getEkmConnection(request, callback)
    
    
    public getEkmConnection(request: google.cloud.kms.v1.IGetEkmConnectionRequest, callback: google.cloud.kms.v1.EkmService.GetEkmConnectionCallback): void;

Calls GetEkmConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEkmConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetekmconnectionrequest)`   
GetEkmConnectionRequest message or plain object  
`callback` |  `[GetEkmConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and EkmConnection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEkmConnection(request)
    
    
    public getEkmConnection(request: google.cloud.kms.v1.IGetEkmConnectionRequest): Promise<google.cloud.kms.v1.EkmConnection>;

Calls GetEkmConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEkmConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetekmconnectionrequest)`   
GetEkmConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.EkmConnection](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmconnection-class)>` | Promise  
  
### listEkmConnections(request, callback)
    
    
    public listEkmConnections(request: google.cloud.kms.v1.IListEkmConnectionsRequest, callback: google.cloud.kms.v1.EkmService.ListEkmConnectionsCallback): void;

Calls ListEkmConnections.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEkmConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistekmconnectionsrequest)`   
ListEkmConnectionsRequest message or plain object  
`callback` |  `[ListEkmConnectionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEkmConnectionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEkmConnections(request)
    
    
    public listEkmConnections(request: google.cloud.kms.v1.IListEkmConnectionsRequest): Promise<google.cloud.kms.v1.ListEkmConnectionsResponse>;

Calls ListEkmConnections.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEkmConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistekmconnectionsrequest)`   
ListEkmConnectionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListEkmConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listekmconnectionsresponse)>` | Promise  
  
### updateEkmConfig(request, callback)
    
    
    public updateEkmConfig(request: google.cloud.kms.v1.IUpdateEkmConfigRequest, callback: google.cloud.kms.v1.EkmService.UpdateEkmConfigCallback): void;

Calls UpdateEkmConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEkmConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdateekmconfigrequest)`   
UpdateEkmConfigRequest message or plain object  
`callback` |  `[UpdateEkmConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and EkmConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEkmConfig(request)
    
    
    public updateEkmConfig(request: google.cloud.kms.v1.IUpdateEkmConfigRequest): Promise<google.cloud.kms.v1.EkmConfig>;

Calls UpdateEkmConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEkmConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdateekmconfigrequest)`   
UpdateEkmConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.EkmConfig](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmconfig)>` | Promise  
  
### updateEkmConnection(request, callback)
    
    
    public updateEkmConnection(request: google.cloud.kms.v1.IUpdateEkmConnectionRequest, callback: google.cloud.kms.v1.EkmService.UpdateEkmConnectionCallback): void;

Calls UpdateEkmConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEkmConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdateekmconnectionrequest)`   
UpdateEkmConnectionRequest message or plain object  
`callback` |  `[UpdateEkmConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and EkmConnection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEkmConnection(request)
    
    
    public updateEkmConnection(request: google.cloud.kms.v1.IUpdateEkmConnectionRequest): Promise<google.cloud.kms.v1.EkmConnection>;

Calls UpdateEkmConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEkmConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdateekmconnectionrequest)`   
UpdateEkmConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.EkmConnection](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ekmconnection-class)>` | Promise  
  
### verifyConnectivity(request, callback)
    
    
    public verifyConnectivity(request: google.cloud.kms.v1.IVerifyConnectivityRequest, callback: google.cloud.kms.v1.EkmService.VerifyConnectivityCallback): void;

Calls VerifyConnectivity.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IVerifyConnectivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iverifyconnectivityrequest)`   
VerifyConnectivityRequest message or plain object  
`callback` |  `[VerifyConnectivityCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and VerifyConnectivityResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### verifyConnectivity(request)
    
    
    public verifyConnectivity(request: google.cloud.kms.v1.IVerifyConnectivityRequest): Promise<google.cloud.kms.v1.VerifyConnectivityResponse>;

Calls VerifyConnectivity.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IVerifyConnectivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iverifyconnectivityrequest)`   
VerifyConnectivityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.VerifyConnectivityResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.verifyconnectivityresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
