---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.hsmmanagement-class
title: Class protos.google.cloud.kms.v1.HsmManagement (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:53.328422+00:00
---

# Class protos.google.cloud.kms.v1.HsmManagement (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.hsmmanagement-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.HsmManagement (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents a HsmManagement

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.kms.v1.HsmManagement

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new HsmManagement service.

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

### approveSingleTenantHsmInstanceProposal(request, callback)
    
    
    public approveSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IApproveSingleTenantHsmInstanceProposalRequest, callback: google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposalCallback): void;

Calls ApproveSingleTenantHsmInstanceProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApproveSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iapprovesingletenanthsminstanceproposalrequest)`   
ApproveSingleTenantHsmInstanceProposalRequest message or plain object  
`callback` |  `[ApproveSingleTenantHsmInstanceProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ApproveSingleTenantHsmInstanceProposalResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### approveSingleTenantHsmInstanceProposal(request)
    
    
    public approveSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IApproveSingleTenantHsmInstanceProposalRequest): Promise<google.cloud.kms.v1.ApproveSingleTenantHsmInstanceProposalResponse>;

Calls ApproveSingleTenantHsmInstanceProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApproveSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iapprovesingletenanthsminstanceproposalrequest)`   
ApproveSingleTenantHsmInstanceProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ApproveSingleTenantHsmInstanceProposalResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.approvesingletenanthsminstanceproposalresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): HsmManagement;

Creates new HsmManagement service using the specified rpc implementation.

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
`[HsmManagement](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.hsmmanagement-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSingleTenantHsmInstance(request, callback)
    
    
    public createSingleTenantHsmInstance(request: google.cloud.kms.v1.ICreateSingleTenantHsmInstanceRequest, callback: google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceCallback): void;

Calls CreateSingleTenantHsmInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatesingletenanthsminstancerequest)`   
CreateSingleTenantHsmInstanceRequest message or plain object  
`callback` |  `[CreateSingleTenantHsmInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSingleTenantHsmInstance(request)
    
    
    public createSingleTenantHsmInstance(request: google.cloud.kms.v1.ICreateSingleTenantHsmInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateSingleTenantHsmInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatesingletenanthsminstancerequest)`   
CreateSingleTenantHsmInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.longrunning.operation)>` | Promise  
  
### createSingleTenantHsmInstanceProposal(request, callback)
    
    
    public createSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.ICreateSingleTenantHsmInstanceProposalRequest, callback: google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposalCallback): void;

Calls CreateSingleTenantHsmInstanceProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatesingletenanthsminstanceproposalrequest)`   
CreateSingleTenantHsmInstanceProposalRequest message or plain object  
`callback` |  `[CreateSingleTenantHsmInstanceProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSingleTenantHsmInstanceProposal(request)
    
    
    public createSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.ICreateSingleTenantHsmInstanceProposalRequest): Promise<google.longrunning.Operation>;

Calls CreateSingleTenantHsmInstanceProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatesingletenanthsminstanceproposalrequest)`   
CreateSingleTenantHsmInstanceProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.longrunning.operation)>` | Promise  
  
### deleteSingleTenantHsmInstanceProposal(request, callback)
    
    
    public deleteSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IDeleteSingleTenantHsmInstanceProposalRequest, callback: google.cloud.kms.v1.HsmManagement.DeleteSingleTenantHsmInstanceProposalCallback): void;

Calls DeleteSingleTenantHsmInstanceProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ideletesingletenanthsminstanceproposalrequest)`   
DeleteSingleTenantHsmInstanceProposalRequest message or plain object  
`callback` |  `[DeleteSingleTenantHsmInstanceProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSingleTenantHsmInstanceProposal(request)
    
    
    public deleteSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IDeleteSingleTenantHsmInstanceProposalRequest): Promise<google.protobuf.Empty>;

Calls DeleteSingleTenantHsmInstanceProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ideletesingletenanthsminstanceproposalrequest)`   
DeleteSingleTenantHsmInstanceProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.protobuf.empty)>` | Promise  
  
### executeSingleTenantHsmInstanceProposal(request, callback)
    
    
    public executeSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IExecuteSingleTenantHsmInstanceProposalRequest, callback: google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposalCallback): void;

Calls ExecuteSingleTenantHsmInstanceProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecuteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iexecutesingletenanthsminstanceproposalrequest)`   
ExecuteSingleTenantHsmInstanceProposalRequest message or plain object  
`callback` |  `[ExecuteSingleTenantHsmInstanceProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### executeSingleTenantHsmInstanceProposal(request)
    
    
    public executeSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IExecuteSingleTenantHsmInstanceProposalRequest): Promise<google.longrunning.Operation>;

Calls ExecuteSingleTenantHsmInstanceProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExecuteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iexecutesingletenanthsminstanceproposalrequest)`   
ExecuteSingleTenantHsmInstanceProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.longrunning.operation)>` | Promise  
  
### getSingleTenantHsmInstance(request, callback)
    
    
    public getSingleTenantHsmInstance(request: google.cloud.kms.v1.IGetSingleTenantHsmInstanceRequest, callback: google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceCallback): void;

Calls GetSingleTenantHsmInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetsingletenanthsminstancerequest)`   
GetSingleTenantHsmInstanceRequest message or plain object  
`callback` |  `[GetSingleTenantHsmInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and SingleTenantHsmInstance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSingleTenantHsmInstance(request)
    
    
    public getSingleTenantHsmInstance(request: google.cloud.kms.v1.IGetSingleTenantHsmInstanceRequest): Promise<google.cloud.kms.v1.SingleTenantHsmInstance>;

Calls GetSingleTenantHsmInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetsingletenanthsminstancerequest)`   
GetSingleTenantHsmInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.SingleTenantHsmInstance](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstance-class)>` | Promise  
  
### getSingleTenantHsmInstanceProposal(request, callback)
    
    
    public getSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IGetSingleTenantHsmInstanceProposalRequest, callback: google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceProposalCallback): void;

Calls GetSingleTenantHsmInstanceProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetsingletenanthsminstanceproposalrequest)`   
GetSingleTenantHsmInstanceProposalRequest message or plain object  
`callback` |  `[GetSingleTenantHsmInstanceProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and SingleTenantHsmInstanceProposal  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSingleTenantHsmInstanceProposal(request)
    
    
    public getSingleTenantHsmInstanceProposal(request: google.cloud.kms.v1.IGetSingleTenantHsmInstanceProposalRequest): Promise<google.cloud.kms.v1.SingleTenantHsmInstanceProposal>;

Calls GetSingleTenantHsmInstanceProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetsingletenanthsminstanceproposalrequest)`   
GetSingleTenantHsmInstanceProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class)>` | Promise  
  
### listSingleTenantHsmInstanceProposals(request, callback)
    
    
    public listSingleTenantHsmInstanceProposals(request: google.cloud.kms.v1.IListSingleTenantHsmInstanceProposalsRequest, callback: google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposalsCallback): void;

Calls ListSingleTenantHsmInstanceProposals.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSingleTenantHsmInstanceProposalsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstanceproposalsrequest)`   
ListSingleTenantHsmInstanceProposalsRequest message or plain object  
`callback` |  `[ListSingleTenantHsmInstanceProposalsCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSingleTenantHsmInstanceProposalsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSingleTenantHsmInstanceProposals(request)
    
    
    public listSingleTenantHsmInstanceProposals(request: google.cloud.kms.v1.IListSingleTenantHsmInstanceProposalsRequest): Promise<google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsResponse>;

Calls ListSingleTenantHsmInstanceProposals.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSingleTenantHsmInstanceProposalsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstanceproposalsrequest)`   
ListSingleTenantHsmInstanceProposalsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstanceproposalsresponse)>` | Promise  
  
### listSingleTenantHsmInstances(request, callback)
    
    
    public listSingleTenantHsmInstances(request: google.cloud.kms.v1.IListSingleTenantHsmInstancesRequest, callback: google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstancesCallback): void;

Calls ListSingleTenantHsmInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSingleTenantHsmInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstancesrequest)`   
ListSingleTenantHsmInstancesRequest message or plain object  
`callback` |  `[ListSingleTenantHsmInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSingleTenantHsmInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSingleTenantHsmInstances(request)
    
    
    public listSingleTenantHsmInstances(request: google.cloud.kms.v1.IListSingleTenantHsmInstancesRequest): Promise<google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse>;

Calls ListSingleTenantHsmInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSingleTenantHsmInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstancesrequest)`   
ListSingleTenantHsmInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
