---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.autokey-class
title: Class protos.google.cloud.kms.v1.Autokey (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:43.092207+00:00
---

# Class protos.google.cloud.kms.v1.Autokey (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.autokey-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.Autokey (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents an Autokey

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.kms.v1.Autokey

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Autokey service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Autokey;

Creates new Autokey service using the specified rpc implementation.

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
`[Autokey](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.autokey-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createKeyHandle(request, callback)
    
    
    public createKeyHandle(request: google.cloud.kms.v1.ICreateKeyHandleRequest, callback: google.cloud.kms.v1.Autokey.CreateKeyHandleCallback): void;

Calls CreateKeyHandle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyHandleRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatekeyhandlerequest)`   
CreateKeyHandleRequest message or plain object  
`callback` |  `[CreateKeyHandleCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createKeyHandle(request)
    
    
    public createKeyHandle(request: google.cloud.kms.v1.ICreateKeyHandleRequest): Promise<google.longrunning.Operation>;

Calls CreateKeyHandle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyHandleRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatekeyhandlerequest)`   
CreateKeyHandleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.longrunning.operation)>` | Promise  
  
### getKeyHandle(request, callback)
    
    
    public getKeyHandle(request: google.cloud.kms.v1.IGetKeyHandleRequest, callback: google.cloud.kms.v1.Autokey.GetKeyHandleCallback): void;

Calls GetKeyHandle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyHandleRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetkeyhandlerequest)`   
GetKeyHandleRequest message or plain object  
`callback` |  `[GetKeyHandleCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyHandle  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getKeyHandle(request)
    
    
    public getKeyHandle(request: google.cloud.kms.v1.IGetKeyHandleRequest): Promise<google.cloud.kms.v1.KeyHandle>;

Calls GetKeyHandle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyHandleRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetkeyhandlerequest)`   
GetKeyHandleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.KeyHandle](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.keyhandle)>` | Promise  
  
### listKeyHandles(request, callback)
    
    
    public listKeyHandles(request: google.cloud.kms.v1.IListKeyHandlesRequest, callback: google.cloud.kms.v1.Autokey.ListKeyHandlesCallback): void;

Calls ListKeyHandles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyHandlesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistkeyhandlesrequest)`   
ListKeyHandlesRequest message or plain object  
`callback` |  `[ListKeyHandlesCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListKeyHandlesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKeyHandles(request)
    
    
    public listKeyHandles(request: google.cloud.kms.v1.IListKeyHandlesRequest): Promise<google.cloud.kms.v1.ListKeyHandlesResponse>;

Calls ListKeyHandles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListKeyHandlesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistkeyhandlesrequest)`   
ListKeyHandlesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListKeyHandlesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listkeyhandlesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
