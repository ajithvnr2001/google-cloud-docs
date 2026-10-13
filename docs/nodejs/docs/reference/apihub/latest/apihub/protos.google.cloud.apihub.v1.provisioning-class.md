---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.provisioning-class
title: Class protos.google.cloud.apihub.v1.Provisioning (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:14.330375+00:00
---

# Class protos.google.cloud.apihub.v1.Provisioning (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.provisioning-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.Provisioning (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Provisioning

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.Provisioning

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Provisioning service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Provisioning;

Creates new Provisioning service using the specified rpc implementation.

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
`[Provisioning](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.provisioning-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createApiHubInstance(request, callback)
    
    
    public createApiHubInstance(request: google.cloud.apihub.v1.ICreateApiHubInstanceRequest, callback: google.cloud.apihub.v1.Provisioning.CreateApiHubInstanceCallback): void;

Calls CreateApiHubInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateapihubinstancerequest)`   
CreateApiHubInstanceRequest message or plain object  
`callback` |  `[CreateApiHubInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createApiHubInstance(request)
    
    
    public createApiHubInstance(request: google.cloud.apihub.v1.ICreateApiHubInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateApiHubInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateapihubinstancerequest)`   
CreateApiHubInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### deleteApiHubInstance(request, callback)
    
    
    public deleteApiHubInstance(request: google.cloud.apihub.v1.IDeleteApiHubInstanceRequest, callback: google.cloud.apihub.v1.Provisioning.DeleteApiHubInstanceCallback): void;

Calls DeleteApiHubInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteapihubinstancerequest)`   
DeleteApiHubInstanceRequest message or plain object  
`callback` |  `[DeleteApiHubInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteApiHubInstance(request)
    
    
    public deleteApiHubInstance(request: google.cloud.apihub.v1.IDeleteApiHubInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteApiHubInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteapihubinstancerequest)`   
DeleteApiHubInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### getApiHubInstance(request, callback)
    
    
    public getApiHubInstance(request: google.cloud.apihub.v1.IGetApiHubInstanceRequest, callback: google.cloud.apihub.v1.Provisioning.GetApiHubInstanceCallback): void;

Calls GetApiHubInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetapihubinstancerequest)`   
GetApiHubInstanceRequest message or plain object  
`callback` |  `[GetApiHubInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ApiHubInstance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getApiHubInstance(request)
    
    
    public getApiHubInstance(request: google.cloud.apihub.v1.IGetApiHubInstanceRequest): Promise<google.cloud.apihub.v1.ApiHubInstance>;

Calls GetApiHubInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetapihubinstancerequest)`   
GetApiHubInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ApiHubInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubinstance-class)>` | Promise  
  
### lookupApiHubInstance(request, callback)
    
    
    public lookupApiHubInstance(request: google.cloud.apihub.v1.ILookupApiHubInstanceRequest, callback: google.cloud.apihub.v1.Provisioning.LookupApiHubInstanceCallback): void;

Calls LookupApiHubInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilookupapihubinstancerequest)`   
LookupApiHubInstanceRequest message or plain object  
`callback` |  `[LookupApiHubInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and LookupApiHubInstanceResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupApiHubInstance(request)
    
    
    public lookupApiHubInstance(request: google.cloud.apihub.v1.ILookupApiHubInstanceRequest): Promise<google.cloud.apihub.v1.LookupApiHubInstanceResponse>;

Calls LookupApiHubInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupApiHubInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilookupapihubinstancerequest)`   
LookupApiHubInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.LookupApiHubInstanceResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.lookupapihubinstanceresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
