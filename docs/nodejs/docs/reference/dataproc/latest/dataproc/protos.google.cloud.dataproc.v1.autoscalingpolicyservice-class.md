---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.autoscalingpolicyservice-class
title: Class protos.google.cloud.dataproc.v1.AutoscalingPolicyService (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:34.775197+00:00
---

# Class protos.google.cloud.dataproc.v1.AutoscalingPolicyService (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.autoscalingpolicyservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.AutoscalingPolicyService (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents an AutoscalingPolicyService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataproc.v1.AutoscalingPolicyService

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AutoscalingPolicyService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AutoscalingPolicyService;

Creates new AutoscalingPolicyService service using the specified rpc implementation.

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
`[AutoscalingPolicyService](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.autoscalingpolicyservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAutoscalingPolicy(request, callback)
    
    
    public createAutoscalingPolicy(request: google.cloud.dataproc.v1.ICreateAutoscalingPolicyRequest, callback: google.cloud.dataproc.v1.AutoscalingPolicyService.CreateAutoscalingPolicyCallback): void;

Calls CreateAutoscalingPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreateautoscalingpolicyrequest)`   
CreateAutoscalingPolicyRequest message or plain object  
`callback` |  `[CreateAutoscalingPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and AutoscalingPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAutoscalingPolicy(request)
    
    
    public createAutoscalingPolicy(request: google.cloud.dataproc.v1.ICreateAutoscalingPolicyRequest): Promise<google.cloud.dataproc.v1.AutoscalingPolicy>;

Calls CreateAutoscalingPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreateautoscalingpolicyrequest)`   
CreateAutoscalingPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.AutoscalingPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.autoscalingpolicy-class)>` | Promise  
  
### deleteAutoscalingPolicy(request, callback)
    
    
    public deleteAutoscalingPolicy(request: google.cloud.dataproc.v1.IDeleteAutoscalingPolicyRequest, callback: google.cloud.dataproc.v1.AutoscalingPolicyService.DeleteAutoscalingPolicyCallback): void;

Calls DeleteAutoscalingPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideleteautoscalingpolicyrequest)`   
DeleteAutoscalingPolicyRequest message or plain object  
`callback` |  `[DeleteAutoscalingPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAutoscalingPolicy(request)
    
    
    public deleteAutoscalingPolicy(request: google.cloud.dataproc.v1.IDeleteAutoscalingPolicyRequest): Promise<google.protobuf.Empty>;

Calls DeleteAutoscalingPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideleteautoscalingpolicyrequest)`   
DeleteAutoscalingPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.protobuf.empty)>` | Promise  
  
### getAutoscalingPolicy(request, callback)
    
    
    public getAutoscalingPolicy(request: google.cloud.dataproc.v1.IGetAutoscalingPolicyRequest, callback: google.cloud.dataproc.v1.AutoscalingPolicyService.GetAutoscalingPolicyCallback): void;

Calls GetAutoscalingPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetautoscalingpolicyrequest)`   
GetAutoscalingPolicyRequest message or plain object  
`callback` |  `[GetAutoscalingPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and AutoscalingPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAutoscalingPolicy(request)
    
    
    public getAutoscalingPolicy(request: google.cloud.dataproc.v1.IGetAutoscalingPolicyRequest): Promise<google.cloud.dataproc.v1.AutoscalingPolicy>;

Calls GetAutoscalingPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetautoscalingpolicyrequest)`   
GetAutoscalingPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.AutoscalingPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.autoscalingpolicy-class)>` | Promise  
  
### listAutoscalingPolicies(request, callback)
    
    
    public listAutoscalingPolicies(request: google.cloud.dataproc.v1.IListAutoscalingPoliciesRequest, callback: google.cloud.dataproc.v1.AutoscalingPolicyService.ListAutoscalingPoliciesCallback): void;

Calls ListAutoscalingPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoscalingPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistautoscalingpoliciesrequest)`   
ListAutoscalingPoliciesRequest message or plain object  
`callback` |  `[ListAutoscalingPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAutoscalingPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAutoscalingPolicies(request)
    
    
    public listAutoscalingPolicies(request: google.cloud.dataproc.v1.IListAutoscalingPoliciesRequest): Promise<google.cloud.dataproc.v1.ListAutoscalingPoliciesResponse>;

Calls ListAutoscalingPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAutoscalingPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistautoscalingpoliciesrequest)`   
ListAutoscalingPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.ListAutoscalingPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.listautoscalingpoliciesresponse)>` | Promise  
  
### updateAutoscalingPolicy(request, callback)
    
    
    public updateAutoscalingPolicy(request: google.cloud.dataproc.v1.IUpdateAutoscalingPolicyRequest, callback: google.cloud.dataproc.v1.AutoscalingPolicyService.UpdateAutoscalingPolicyCallback): void;

Calls UpdateAutoscalingPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdateautoscalingpolicyrequest)`   
UpdateAutoscalingPolicyRequest message or plain object  
`callback` |  `[UpdateAutoscalingPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and AutoscalingPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAutoscalingPolicy(request)
    
    
    public updateAutoscalingPolicy(request: google.cloud.dataproc.v1.IUpdateAutoscalingPolicyRequest): Promise<google.cloud.dataproc.v1.AutoscalingPolicy>;

Calls UpdateAutoscalingPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutoscalingPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdateautoscalingpolicyrequest)`   
UpdateAutoscalingPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.AutoscalingPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.autoscalingpolicy-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
