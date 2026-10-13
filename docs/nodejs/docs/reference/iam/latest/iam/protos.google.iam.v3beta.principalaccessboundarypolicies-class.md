---
url: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.principalaccessboundarypolicies-class
title: Class protos.google.iam.v3beta.PrincipalAccessBoundaryPolicies (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:12.521219+00:00
---

# Class protos.google.iam.v3beta.PrincipalAccessBoundaryPolicies (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.principalaccessboundarypolicies-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.iam.v3beta.PrincipalAccessBoundaryPolicies (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.2.0  0.3.2  0.2.2 

Represents a PrincipalAccessBoundaryPolicies

## Inheritance

$protobuf.rpc.Service > protos.google.iam.v3beta.PrincipalAccessBoundaryPolicies

## Package

[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PrincipalAccessBoundaryPolicies service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PrincipalAccessBoundaryPolicies;

Creates new PrincipalAccessBoundaryPolicies service using the specified rpc implementation.

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
`[PrincipalAccessBoundaryPolicies](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.principalaccessboundarypolicies-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createPrincipalAccessBoundaryPolicy(request, callback)
    
    
    public createPrincipalAccessBoundaryPolicy(request: google.iam.v3beta.ICreatePrincipalAccessBoundaryPolicyRequest, callback: google.iam.v3beta.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicyCallback): void;

Calls CreatePrincipalAccessBoundaryPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.icreateprincipalaccessboundarypolicyrequest)`   
CreatePrincipalAccessBoundaryPolicyRequest message or plain object  
`callback` |  `[CreatePrincipalAccessBoundaryPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPrincipalAccessBoundaryPolicy(request)
    
    
    public createPrincipalAccessBoundaryPolicy(request: google.iam.v3beta.ICreatePrincipalAccessBoundaryPolicyRequest): Promise<google.longrunning.Operation>;

Calls CreatePrincipalAccessBoundaryPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.icreateprincipalaccessboundarypolicyrequest)`   
CreatePrincipalAccessBoundaryPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.operation)>` | Promise  
  
### deletePrincipalAccessBoundaryPolicy(request, callback)
    
    
    public deletePrincipalAccessBoundaryPolicy(request: google.iam.v3beta.IDeletePrincipalAccessBoundaryPolicyRequest, callback: google.iam.v3beta.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicyCallback): void;

Calls DeletePrincipalAccessBoundaryPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.ideleteprincipalaccessboundarypolicyrequest)`   
DeletePrincipalAccessBoundaryPolicyRequest message or plain object  
`callback` |  `[DeletePrincipalAccessBoundaryPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrincipalAccessBoundaryPolicy(request)
    
    
    public deletePrincipalAccessBoundaryPolicy(request: google.iam.v3beta.IDeletePrincipalAccessBoundaryPolicyRequest): Promise<google.longrunning.Operation>;

Calls DeletePrincipalAccessBoundaryPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.ideleteprincipalaccessboundarypolicyrequest)`   
DeletePrincipalAccessBoundaryPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.operation)>` | Promise  
  
### getPrincipalAccessBoundaryPolicy(request, callback)
    
    
    public getPrincipalAccessBoundaryPolicy(request: google.iam.v3beta.IGetPrincipalAccessBoundaryPolicyRequest, callback: google.iam.v3beta.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicyCallback): void;

Calls GetPrincipalAccessBoundaryPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.igetprincipalaccessboundarypolicyrequest)`   
GetPrincipalAccessBoundaryPolicyRequest message or plain object  
`callback` |  `[GetPrincipalAccessBoundaryPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)`   
Node-style callback called with the error, if any, and PrincipalAccessBoundaryPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPrincipalAccessBoundaryPolicy(request)
    
    
    public getPrincipalAccessBoundaryPolicy(request: google.iam.v3beta.IGetPrincipalAccessBoundaryPolicyRequest): Promise<google.iam.v3beta.PrincipalAccessBoundaryPolicy>;

Calls GetPrincipalAccessBoundaryPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.igetprincipalaccessboundarypolicyrequest)`   
GetPrincipalAccessBoundaryPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v3beta.PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.principalaccessboundarypolicy)>` | Promise  
  
### listPrincipalAccessBoundaryPolicies(request, callback)
    
    
    public listPrincipalAccessBoundaryPolicies(request: google.iam.v3beta.IListPrincipalAccessBoundaryPoliciesRequest, callback: google.iam.v3beta.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPoliciesCallback): void;

Calls ListPrincipalAccessBoundaryPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.ilistprincipalaccessboundarypoliciesrequest)`   
ListPrincipalAccessBoundaryPoliciesRequest message or plain object  
`callback` |  `[ListPrincipalAccessBoundaryPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPrincipalAccessBoundaryPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrincipalAccessBoundaryPolicies(request)
    
    
    public listPrincipalAccessBoundaryPolicies(request: google.iam.v3beta.IListPrincipalAccessBoundaryPoliciesRequest): Promise<google.iam.v3beta.ListPrincipalAccessBoundaryPoliciesResponse>;

Calls ListPrincipalAccessBoundaryPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.ilistprincipalaccessboundarypoliciesrequest)`   
ListPrincipalAccessBoundaryPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v3beta.ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.listprincipalaccessboundarypoliciesresponse)>` | Promise  
  
### searchPrincipalAccessBoundaryPolicyBindings(request, callback)
    
    
    public searchPrincipalAccessBoundaryPolicyBindings(request: google.iam.v3beta.ISearchPrincipalAccessBoundaryPolicyBindingsRequest, callback: google.iam.v3beta.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindingsCallback): void;

Calls SearchPrincipalAccessBoundaryPolicyBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.isearchprincipalaccessboundarypolicybindingsrequest)`   
SearchPrincipalAccessBoundaryPolicyBindingsRequest message or plain object  
`callback` |  `[SearchPrincipalAccessBoundaryPolicyBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchPrincipalAccessBoundaryPolicyBindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchPrincipalAccessBoundaryPolicyBindings(request)
    
    
    public searchPrincipalAccessBoundaryPolicyBindings(request: google.iam.v3beta.ISearchPrincipalAccessBoundaryPolicyBindingsRequest): Promise<google.iam.v3beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse>;

Calls SearchPrincipalAccessBoundaryPolicyBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.isearchprincipalaccessboundarypolicybindingsrequest)`   
SearchPrincipalAccessBoundaryPolicyBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v3beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.searchprincipalaccessboundarypolicybindingsresponse)>` | Promise  
  
### updatePrincipalAccessBoundaryPolicy(request, callback)
    
    
    public updatePrincipalAccessBoundaryPolicy(request: google.iam.v3beta.IUpdatePrincipalAccessBoundaryPolicyRequest, callback: google.iam.v3beta.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicyCallback): void;

Calls UpdatePrincipalAccessBoundaryPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.iupdateprincipalaccessboundarypolicyrequest)`   
UpdatePrincipalAccessBoundaryPolicyRequest message or plain object  
`callback` |  `[UpdatePrincipalAccessBoundaryPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePrincipalAccessBoundaryPolicy(request)
    
    
    public updatePrincipalAccessBoundaryPolicy(request: google.iam.v3beta.IUpdatePrincipalAccessBoundaryPolicyRequest): Promise<google.longrunning.Operation>;

Calls UpdatePrincipalAccessBoundaryPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3beta.iupdateprincipalaccessboundarypolicyrequest)`   
UpdatePrincipalAccessBoundaryPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
