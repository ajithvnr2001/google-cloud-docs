---
url: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.binauthzmanagementservicev1-class
title: Class protos.google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1 (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:05.270121+00:00
---

# Class protos.google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1 (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.binauthzmanagementservicev1-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1 (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.5.0  4.4.0  4.2.0  3.7.0  2.5.0  2.2.1  2.1.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.6 

Represents a BinauthzManagementServiceV1

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1

## Package

[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BinauthzManagementServiceV1 service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BinauthzManagementServiceV1;

Creates new BinauthzManagementServiceV1 service using the specified rpc implementation.

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
`[BinauthzManagementServiceV1](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.binauthzmanagementservicev1-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAttestor(request, callback)
    
    
    public createAttestor(request: google.cloud.binaryauthorization.v1.ICreateAttestorRequest, callback: google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.CreateAttestorCallback): void;

Calls CreateAttestor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.icreateattestorrequest)`   
CreateAttestorRequest message or plain object  
`callback` |  `[CreateAttestorCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and Attestor  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAttestor(request)
    
    
    public createAttestor(request: google.cloud.binaryauthorization.v1.ICreateAttestorRequest): Promise<google.cloud.binaryauthorization.v1.Attestor>;

Calls CreateAttestor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.icreateattestorrequest)`   
CreateAttestorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1.Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.attestor)>` | Promise  
  
### deleteAttestor(request, callback)
    
    
    public deleteAttestor(request: google.cloud.binaryauthorization.v1.IDeleteAttestorRequest, callback: google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.DeleteAttestorCallback): void;

Calls DeleteAttestor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ideleteattestorrequest)`   
DeleteAttestorRequest message or plain object  
`callback` |  `[DeleteAttestorCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAttestor(request)
    
    
    public deleteAttestor(request: google.cloud.binaryauthorization.v1.IDeleteAttestorRequest): Promise<google.protobuf.Empty>;

Calls DeleteAttestor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ideleteattestorrequest)`   
DeleteAttestorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.protobuf.empty)>` | Promise  
  
### getAttestor(request, callback)
    
    
    public getAttestor(request: google.cloud.binaryauthorization.v1.IGetAttestorRequest, callback: google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetAttestorCallback): void;

Calls GetAttestor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.igetattestorrequest)`   
GetAttestorRequest message or plain object  
`callback` |  `[GetAttestorCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and Attestor  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAttestor(request)
    
    
    public getAttestor(request: google.cloud.binaryauthorization.v1.IGetAttestorRequest): Promise<google.cloud.binaryauthorization.v1.Attestor>;

Calls GetAttestor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.igetattestorrequest)`   
GetAttestorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1.Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.attestor)>` | Promise  
  
### getPolicy(request, callback)
    
    
    public getPolicy(request: google.cloud.binaryauthorization.v1.IGetPolicyRequest, callback: google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetPolicyCallback): void;

Calls GetPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.igetpolicyrequest)`   
GetPolicyRequest message or plain object  
`callback` |  `[GetPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPolicy(request)
    
    
    public getPolicy(request: google.cloud.binaryauthorization.v1.IGetPolicyRequest): Promise<google.cloud.binaryauthorization.v1.Policy>;

Calls GetPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.igetpolicyrequest)`   
GetPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.policy-class)>` | Promise  
  
### listAttestors(request, callback)
    
    
    public listAttestors(request: google.cloud.binaryauthorization.v1.IListAttestorsRequest, callback: google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestorsCallback): void;

Calls ListAttestors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ilistattestorsrequest)`   
ListAttestorsRequest message or plain object  
`callback` |  `[ListAttestorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAttestorsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAttestors(request)
    
    
    public listAttestors(request: google.cloud.binaryauthorization.v1.IListAttestorsRequest): Promise<google.cloud.binaryauthorization.v1.ListAttestorsResponse>;

Calls ListAttestors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ilistattestorsrequest)`   
ListAttestorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1.ListAttestorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.listattestorsresponse)>` | Promise  
  
### updateAttestor(request, callback)
    
    
    public updateAttestor(request: google.cloud.binaryauthorization.v1.IUpdateAttestorRequest, callback: google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdateAttestorCallback): void;

Calls UpdateAttestor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.iupdateattestorrequest)`   
UpdateAttestorRequest message or plain object  
`callback` |  `[UpdateAttestorCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and Attestor  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAttestor(request)
    
    
    public updateAttestor(request: google.cloud.binaryauthorization.v1.IUpdateAttestorRequest): Promise<google.cloud.binaryauthorization.v1.Attestor>;

Calls UpdateAttestor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.iupdateattestorrequest)`   
UpdateAttestorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1.Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.attestor)>` | Promise  
  
### updatePolicy(request, callback)
    
    
    public updatePolicy(request: google.cloud.binaryauthorization.v1.IUpdatePolicyRequest, callback: google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdatePolicyCallback): void;

Calls UpdatePolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.iupdatepolicyrequest)`   
UpdatePolicyRequest message or plain object  
`callback` |  `[UpdatePolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePolicy(request)
    
    
    public updatePolicy(request: google.cloud.binaryauthorization.v1.IUpdatePolicyRequest): Promise<google.cloud.binaryauthorization.v1.Policy>;

Calls UpdatePolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.iupdatepolicyrequest)`   
UpdatePolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.policy-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
