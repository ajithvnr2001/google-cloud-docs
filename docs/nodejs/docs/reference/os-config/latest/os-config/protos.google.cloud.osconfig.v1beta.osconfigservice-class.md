---
url: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.osconfigservice-class
title: Class protos.google.cloud.osconfig.v1beta.OsConfigService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:17.030796+00:00
---

# Class protos.google.cloud.osconfig.v1beta.OsConfigService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.osconfigservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.osconfig.v1beta.OsConfigService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.2.2  2.1.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.6 

Represents an OsConfigService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.osconfig.v1beta.OsConfigService

## Package

[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new OsConfigService service.

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

### cancelPatchJob(request, callback)
    
    
    public cancelPatchJob(request: google.cloud.osconfig.v1beta.ICancelPatchJobRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.CancelPatchJobCallback): void;

Calls CancelPatchJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest)`   
CancelPatchJobRequest message or plain object  
`callback` |  `[CancelPatchJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelPatchJob(request)
    
    
    public cancelPatchJob(request: google.cloud.osconfig.v1beta.ICancelPatchJobRequest): Promise<google.cloud.osconfig.v1beta.PatchJob>;

Calls CancelPatchJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest)`   
CancelPatchJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchjob-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): OsConfigService;

Creates new OsConfigService service using the specified rpc implementation.

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
`[OsConfigService](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.osconfigservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createGuestPolicy(request, callback)
    
    
    public createGuestPolicy(request: google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.CreateGuestPolicyCallback): void;

Calls CreateGuestPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest)`   
CreateGuestPolicyRequest message or plain object  
`callback` |  `[CreateGuestPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and GuestPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGuestPolicy(request)
    
    
    public createGuestPolicy(request: google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest): Promise<google.cloud.osconfig.v1beta.GuestPolicy>;

Calls CreateGuestPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest)`   
CreateGuestPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy)>` | Promise  
  
### createPatchDeployment(request, callback)
    
    
    public createPatchDeployment(request: google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.CreatePatchDeploymentCallback): void;

Calls CreatePatchDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest)`   
CreatePatchDeploymentRequest message or plain object  
`callback` |  `[CreatePatchDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchDeployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPatchDeployment(request)
    
    
    public createPatchDeployment(request: google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest): Promise<google.cloud.osconfig.v1beta.PatchDeployment>;

Calls CreatePatchDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest)`   
CreatePatchDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchdeployment-class)>` | Promise  
  
### deleteGuestPolicy(request, callback)
    
    
    public deleteGuestPolicy(request: google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.DeleteGuestPolicyCallback): void;

Calls DeleteGuestPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest)`   
DeleteGuestPolicyRequest message or plain object  
`callback` |  `[DeleteGuestPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGuestPolicy(request)
    
    
    public deleteGuestPolicy(request: google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest): Promise<google.protobuf.Empty>;

Calls DeleteGuestPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest)`   
DeleteGuestPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.empty)>` | Promise  
  
### deletePatchDeployment(request, callback)
    
    
    public deletePatchDeployment(request: google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.DeletePatchDeploymentCallback): void;

Calls DeletePatchDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest)`   
DeletePatchDeploymentRequest message or plain object  
`callback` |  `[DeletePatchDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePatchDeployment(request)
    
    
    public deletePatchDeployment(request: google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest): Promise<google.protobuf.Empty>;

Calls DeletePatchDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest)`   
DeletePatchDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.empty)>` | Promise  
  
### executePatchJob(request, callback)
    
    
    public executePatchJob(request: google.cloud.osconfig.v1beta.IExecutePatchJobRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.ExecutePatchJobCallback): void;

Calls ExecutePatchJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest)`   
ExecutePatchJobRequest message or plain object  
`callback` |  `[ExecutePatchJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### executePatchJob(request)
    
    
    public executePatchJob(request: google.cloud.osconfig.v1beta.IExecutePatchJobRequest): Promise<google.cloud.osconfig.v1beta.PatchJob>;

Calls ExecutePatchJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest)`   
ExecutePatchJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchjob-class)>` | Promise  
  
### getGuestPolicy(request, callback)
    
    
    public getGuestPolicy(request: google.cloud.osconfig.v1beta.IGetGuestPolicyRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.GetGuestPolicyCallback): void;

Calls GetGuestPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest)`   
GetGuestPolicyRequest message or plain object  
`callback` |  `[GetGuestPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and GuestPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGuestPolicy(request)
    
    
    public getGuestPolicy(request: google.cloud.osconfig.v1beta.IGetGuestPolicyRequest): Promise<google.cloud.osconfig.v1beta.GuestPolicy>;

Calls GetGuestPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest)`   
GetGuestPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy)>` | Promise  
  
### getPatchDeployment(request, callback)
    
    
    public getPatchDeployment(request: google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.GetPatchDeploymentCallback): void;

Calls GetPatchDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest)`   
GetPatchDeploymentRequest message or plain object  
`callback` |  `[GetPatchDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchDeployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPatchDeployment(request)
    
    
    public getPatchDeployment(request: google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest): Promise<google.cloud.osconfig.v1beta.PatchDeployment>;

Calls GetPatchDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest)`   
GetPatchDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchdeployment-class)>` | Promise  
  
### getPatchJob(request, callback)
    
    
    public getPatchJob(request: google.cloud.osconfig.v1beta.IGetPatchJobRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.GetPatchJobCallback): void;

Calls GetPatchJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest)`   
GetPatchJobRequest message or plain object  
`callback` |  `[GetPatchJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPatchJob(request)
    
    
    public getPatchJob(request: google.cloud.osconfig.v1beta.IGetPatchJobRequest): Promise<google.cloud.osconfig.v1beta.PatchJob>;

Calls GetPatchJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest)`   
GetPatchJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchjob-class)>` | Promise  
  
### listGuestPolicies(request, callback)
    
    
    public listGuestPolicies(request: google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.ListGuestPoliciesCallback): void;

Calls ListGuestPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest)`   
ListGuestPoliciesRequest message or plain object  
`callback` |  `[ListGuestPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGuestPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGuestPolicies(request)
    
    
    public listGuestPolicies(request: google.cloud.osconfig.v1beta.IListGuestPoliciesRequest): Promise<google.cloud.osconfig.v1beta.ListGuestPoliciesResponse>;

Calls ListGuestPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest)`   
ListGuestPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.ListGuestPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.listguestpoliciesresponse)>` | Promise  
  
### listPatchDeployments(request, callback)
    
    
    public listPatchDeployments(request: google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.ListPatchDeploymentsCallback): void;

Calls ListPatchDeployments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest)`   
ListPatchDeploymentsRequest message or plain object  
`callback` |  `[ListPatchDeploymentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPatchDeploymentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchDeployments(request)
    
    
    public listPatchDeployments(request: google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest): Promise<google.cloud.osconfig.v1beta.ListPatchDeploymentsResponse>;

Calls ListPatchDeployments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest)`   
ListPatchDeploymentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.ListPatchDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.listpatchdeploymentsresponse)>` | Promise  
  
### listPatchJobInstanceDetails(request, callback)
    
    
    public listPatchJobInstanceDetails(request: google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobInstanceDetailsCallback): void;

Calls ListPatchJobInstanceDetails.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest)`   
ListPatchJobInstanceDetailsRequest message or plain object  
`callback` |  `[ListPatchJobInstanceDetailsCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPatchJobInstanceDetailsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchJobInstanceDetails(request)
    
    
    public listPatchJobInstanceDetails(request: google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest): Promise<google.cloud.osconfig.v1beta.ListPatchJobInstanceDetailsResponse>;

Calls ListPatchJobInstanceDetails.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest)`   
ListPatchJobInstanceDetailsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.ListPatchJobInstanceDetailsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.listpatchjobinstancedetailsresponse)>` | Promise  
  
### listPatchJobs(request, callback)
    
    
    public listPatchJobs(request: google.cloud.osconfig.v1beta.IListPatchJobsRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobsCallback): void;

Calls ListPatchJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest)`   
ListPatchJobsRequest message or plain object  
`callback` |  `[ListPatchJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPatchJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchJobs(request)
    
    
    public listPatchJobs(request: google.cloud.osconfig.v1beta.IListPatchJobsRequest): Promise<google.cloud.osconfig.v1beta.ListPatchJobsResponse>;

Calls ListPatchJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest)`   
ListPatchJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.ListPatchJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.listpatchjobsresponse)>` | Promise  
  
### lookupEffectiveGuestPolicy(request, callback)
    
    
    public lookupEffectiveGuestPolicy(request: google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.LookupEffectiveGuestPolicyCallback): void;

Calls LookupEffectiveGuestPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest)`   
LookupEffectiveGuestPolicyRequest message or plain object  
`callback` |  `[LookupEffectiveGuestPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and EffectiveGuestPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupEffectiveGuestPolicy(request)
    
    
    public lookupEffectiveGuestPolicy(request: google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest): Promise<google.cloud.osconfig.v1beta.EffectiveGuestPolicy>;

Calls LookupEffectiveGuestPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest)`   
LookupEffectiveGuestPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.EffectiveGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.effectiveguestpolicy-class)>` | Promise  
  
### pausePatchDeployment(request, callback)
    
    
    public pausePatchDeployment(request: google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.PausePatchDeploymentCallback): void;

Calls PausePatchDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest)`   
PausePatchDeploymentRequest message or plain object  
`callback` |  `[PausePatchDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchDeployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pausePatchDeployment(request)
    
    
    public pausePatchDeployment(request: google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest): Promise<google.cloud.osconfig.v1beta.PatchDeployment>;

Calls PausePatchDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest)`   
PausePatchDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchdeployment-class)>` | Promise  
  
### resumePatchDeployment(request, callback)
    
    
    public resumePatchDeployment(request: google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.ResumePatchDeploymentCallback): void;

Calls ResumePatchDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest)`   
ResumePatchDeploymentRequest message or plain object  
`callback` |  `[ResumePatchDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchDeployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumePatchDeployment(request)
    
    
    public resumePatchDeployment(request: google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest): Promise<google.cloud.osconfig.v1beta.PatchDeployment>;

Calls ResumePatchDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest)`   
ResumePatchDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchdeployment-class)>` | Promise  
  
### updateGuestPolicy(request, callback)
    
    
    public updateGuestPolicy(request: google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.UpdateGuestPolicyCallback): void;

Calls UpdateGuestPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest)`   
UpdateGuestPolicyRequest message or plain object  
`callback` |  `[UpdateGuestPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and GuestPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGuestPolicy(request)
    
    
    public updateGuestPolicy(request: google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest): Promise<google.cloud.osconfig.v1beta.GuestPolicy>;

Calls UpdateGuestPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest)`   
UpdateGuestPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy)>` | Promise  
  
### updatePatchDeployment(request, callback)
    
    
    public updatePatchDeployment(request: google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest, callback: google.cloud.osconfig.v1beta.OsConfigService.UpdatePatchDeploymentCallback): void;

Calls UpdatePatchDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest)`   
UpdatePatchDeploymentRequest message or plain object  
`callback` |  `[UpdatePatchDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)`   
Node-style callback called with the error, if any, and PatchDeployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePatchDeployment(request)
    
    
    public updatePatchDeployment(request: google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest): Promise<google.cloud.osconfig.v1beta.PatchDeployment>;

Calls UpdatePatchDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest)`   
UpdatePatchDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.osconfig.v1beta.PatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchdeployment-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
