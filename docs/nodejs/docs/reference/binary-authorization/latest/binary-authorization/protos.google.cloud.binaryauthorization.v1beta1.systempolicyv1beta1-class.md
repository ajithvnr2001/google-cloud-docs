---
url: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.systempolicyv1beta1-class
title: Class protos.google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1 (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:12.540276+00:00
---

# Class protos.google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1 (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.systempolicyv1beta1-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1 (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.5.0  4.4.0  4.2.0  3.7.0  2.5.0  2.2.1  2.1.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.6 

Represents a SystemPolicyV1Beta1

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1

## Package

[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SystemPolicyV1Beta1 service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SystemPolicyV1Beta1;

Creates new SystemPolicyV1Beta1 service using the specified rpc implementation.

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
`[SystemPolicyV1Beta1](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.systempolicyv1beta1-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getSystemPolicy(request, callback)
    
    
    public getSystemPolicy(request: google.cloud.binaryauthorization.v1beta1.IGetSystemPolicyRequest, callback: google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1.GetSystemPolicyCallback): void;

Calls GetSystemPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSystemPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetsystempolicyrequest)`   
GetSystemPolicyRequest message or plain object  
`callback` |  `[GetSystemPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSystemPolicy(request)
    
    
    public getSystemPolicy(request: google.cloud.binaryauthorization.v1beta1.IGetSystemPolicyRequest): Promise<google.cloud.binaryauthorization.v1beta1.Policy>;

Calls GetSystemPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSystemPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetsystempolicyrequest)`   
GetSystemPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1beta1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.policy-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
