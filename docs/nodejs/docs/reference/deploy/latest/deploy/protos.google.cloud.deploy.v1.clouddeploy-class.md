---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.clouddeploy-class
title: Class protos.google.cloud.deploy.v1.CloudDeploy (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:01:30.078261+00:00
---

# Class protos.google.cloud.deploy.v1.CloudDeploy (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.clouddeploy-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.CloudDeploy (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a CloudDeploy

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.deploy.v1.CloudDeploy

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CloudDeploy service.

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

### abandonRelease(request, callback)
    
    
    public abandonRelease(request: google.cloud.deploy.v1.IAbandonReleaseRequest, callback: google.cloud.deploy.v1.CloudDeploy.AbandonReleaseCallback): void;

Calls AbandonRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAbandonReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iabandonreleaserequest)`   
AbandonReleaseRequest message or plain object  
`callback` |  `[AbandonReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and AbandonReleaseResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### abandonRelease(request)
    
    
    public abandonRelease(request: google.cloud.deploy.v1.IAbandonReleaseRequest): Promise<google.cloud.deploy.v1.AbandonReleaseResponse>;

Calls AbandonRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAbandonReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iabandonreleaserequest)`   
AbandonReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.AbandonReleaseResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.abandonreleaseresponse)>` | Promise  
  
### advanceRollout(request, callback)
    
    
    public advanceRollout(request: google.cloud.deploy.v1.IAdvanceRolloutRequest, callback: google.cloud.deploy.v1.CloudDeploy.AdvanceRolloutCallback): void;

Calls AdvanceRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAdvanceRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iadvancerolloutrequest)`   
AdvanceRolloutRequest message or plain object  
`callback` |  `[AdvanceRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and AdvanceRolloutResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### advanceRollout(request)
    
    
    public advanceRollout(request: google.cloud.deploy.v1.IAdvanceRolloutRequest): Promise<google.cloud.deploy.v1.AdvanceRolloutResponse>;

Calls AdvanceRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAdvanceRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iadvancerolloutrequest)`   
AdvanceRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.AdvanceRolloutResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.advancerolloutresponse)>` | Promise  
  
### approveRollout(request, callback)
    
    
    public approveRollout(request: google.cloud.deploy.v1.IApproveRolloutRequest, callback: google.cloud.deploy.v1.CloudDeploy.ApproveRolloutCallback): void;

Calls ApproveRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApproveRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iapproverolloutrequest)`   
ApproveRolloutRequest message or plain object  
`callback` |  `[ApproveRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ApproveRolloutResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### approveRollout(request)
    
    
    public approveRollout(request: google.cloud.deploy.v1.IApproveRolloutRequest): Promise<google.cloud.deploy.v1.ApproveRolloutResponse>;

Calls ApproveRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApproveRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iapproverolloutrequest)`   
ApproveRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ApproveRolloutResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.approverolloutresponse)>` | Promise  
  
### cancelAutomationRun(request, callback)
    
    
    public cancelAutomationRun(request: google.cloud.deploy.v1.ICancelAutomationRunRequest, callback: google.cloud.deploy.v1.CloudDeploy.CancelAutomationRunCallback): void;

Calls CancelAutomationRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelAutomationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icancelautomationrunrequest)`   
CancelAutomationRunRequest message or plain object  
`callback` |  `[CancelAutomationRunCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and CancelAutomationRunResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelAutomationRun(request)
    
    
    public cancelAutomationRun(request: google.cloud.deploy.v1.ICancelAutomationRunRequest): Promise<google.cloud.deploy.v1.CancelAutomationRunResponse>;

Calls CancelAutomationRun.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelAutomationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icancelautomationrunrequest)`   
CancelAutomationRunRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.CancelAutomationRunResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.cancelautomationrunresponse)>` | Promise  
  
### cancelRollout(request, callback)
    
    
    public cancelRollout(request: google.cloud.deploy.v1.ICancelRolloutRequest, callback: google.cloud.deploy.v1.CloudDeploy.CancelRolloutCallback): void;

Calls CancelRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icancelrolloutrequest)`   
CancelRolloutRequest message or plain object  
`callback` |  `[CancelRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and CancelRolloutResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelRollout(request)
    
    
    public cancelRollout(request: google.cloud.deploy.v1.ICancelRolloutRequest): Promise<google.cloud.deploy.v1.CancelRolloutResponse>;

Calls CancelRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icancelrolloutrequest)`   
CancelRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.CancelRolloutResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.cancelrolloutresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CloudDeploy;

Creates new CloudDeploy service using the specified rpc implementation.

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
`[CloudDeploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.clouddeploy-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAutomation(request, callback)
    
    
    public createAutomation(request: google.cloud.deploy.v1.ICreateAutomationRequest, callback: google.cloud.deploy.v1.CloudDeploy.CreateAutomationCallback): void;

Calls CreateAutomation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreateautomationrequest)`   
CreateAutomationRequest message or plain object  
`callback` |  `[CreateAutomationCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAutomation(request)
    
    
    public createAutomation(request: google.cloud.deploy.v1.ICreateAutomationRequest): Promise<google.longrunning.Operation>;

Calls CreateAutomation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreateautomationrequest)`   
CreateAutomationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### createCustomTargetType(request, callback)
    
    
    public createCustomTargetType(request: google.cloud.deploy.v1.ICreateCustomTargetTypeRequest, callback: google.cloud.deploy.v1.CloudDeploy.CreateCustomTargetTypeCallback): void;

Calls CreateCustomTargetType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatecustomtargettyperequest)`   
CreateCustomTargetTypeRequest message or plain object  
`callback` |  `[CreateCustomTargetTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomTargetType(request)
    
    
    public createCustomTargetType(request: google.cloud.deploy.v1.ICreateCustomTargetTypeRequest): Promise<google.longrunning.Operation>;

Calls CreateCustomTargetType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatecustomtargettyperequest)`   
CreateCustomTargetTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### createDeliveryPipeline(request, callback)
    
    
    public createDeliveryPipeline(request: google.cloud.deploy.v1.ICreateDeliveryPipelineRequest, callback: google.cloud.deploy.v1.CloudDeploy.CreateDeliveryPipelineCallback): void;

Calls CreateDeliveryPipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatedeliverypipelinerequest)`   
CreateDeliveryPipelineRequest message or plain object  
`callback` |  `[CreateDeliveryPipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDeliveryPipeline(request)
    
    
    public createDeliveryPipeline(request: google.cloud.deploy.v1.ICreateDeliveryPipelineRequest): Promise<google.longrunning.Operation>;

Calls CreateDeliveryPipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatedeliverypipelinerequest)`   
CreateDeliveryPipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### createDeployPolicy(request, callback)
    
    
    public createDeployPolicy(request: google.cloud.deploy.v1.ICreateDeployPolicyRequest, callback: google.cloud.deploy.v1.CloudDeploy.CreateDeployPolicyCallback): void;

Calls CreateDeployPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatedeploypolicyrequest)`   
CreateDeployPolicyRequest message or plain object  
`callback` |  `[CreateDeployPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDeployPolicy(request)
    
    
    public createDeployPolicy(request: google.cloud.deploy.v1.ICreateDeployPolicyRequest): Promise<google.longrunning.Operation>;

Calls CreateDeployPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatedeploypolicyrequest)`   
CreateDeployPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### createRelease(request, callback)
    
    
    public createRelease(request: google.cloud.deploy.v1.ICreateReleaseRequest, callback: google.cloud.deploy.v1.CloudDeploy.CreateReleaseCallback): void;

Calls CreateRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatereleaserequest)`   
CreateReleaseRequest message or plain object  
`callback` |  `[CreateReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRelease(request)
    
    
    public createRelease(request: google.cloud.deploy.v1.ICreateReleaseRequest): Promise<google.longrunning.Operation>;

Calls CreateRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatereleaserequest)`   
CreateReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### createRollout(request, callback)
    
    
    public createRollout(request: google.cloud.deploy.v1.ICreateRolloutRequest, callback: google.cloud.deploy.v1.CloudDeploy.CreateRolloutCallback): void;

Calls CreateRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreaterolloutrequest)`   
CreateRolloutRequest message or plain object  
`callback` |  `[CreateRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRollout(request)
    
    
    public createRollout(request: google.cloud.deploy.v1.ICreateRolloutRequest): Promise<google.longrunning.Operation>;

Calls CreateRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreaterolloutrequest)`   
CreateRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### createTarget(request, callback)
    
    
    public createTarget(request: google.cloud.deploy.v1.ICreateTargetRequest, callback: google.cloud.deploy.v1.CloudDeploy.CreateTargetCallback): void;

Calls CreateTarget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatetargetrequest)`   
CreateTargetRequest message or plain object  
`callback` |  `[CreateTargetCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTarget(request)
    
    
    public createTarget(request: google.cloud.deploy.v1.ICreateTargetRequest): Promise<google.longrunning.Operation>;

Calls CreateTarget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.icreatetargetrequest)`   
CreateTargetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### deleteAutomation(request, callback)
    
    
    public deleteAutomation(request: google.cloud.deploy.v1.IDeleteAutomationRequest, callback: google.cloud.deploy.v1.CloudDeploy.DeleteAutomationCallback): void;

Calls DeleteAutomation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideleteautomationrequest)`   
DeleteAutomationRequest message or plain object  
`callback` |  `[DeleteAutomationCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAutomation(request)
    
    
    public deleteAutomation(request: google.cloud.deploy.v1.IDeleteAutomationRequest): Promise<google.longrunning.Operation>;

Calls DeleteAutomation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideleteautomationrequest)`   
DeleteAutomationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### deleteCustomTargetType(request, callback)
    
    
    public deleteCustomTargetType(request: google.cloud.deploy.v1.IDeleteCustomTargetTypeRequest, callback: google.cloud.deploy.v1.CloudDeploy.DeleteCustomTargetTypeCallback): void;

Calls DeleteCustomTargetType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletecustomtargettyperequest)`   
DeleteCustomTargetTypeRequest message or plain object  
`callback` |  `[DeleteCustomTargetTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCustomTargetType(request)
    
    
    public deleteCustomTargetType(request: google.cloud.deploy.v1.IDeleteCustomTargetTypeRequest): Promise<google.longrunning.Operation>;

Calls DeleteCustomTargetType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletecustomtargettyperequest)`   
DeleteCustomTargetTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### deleteDeliveryPipeline(request, callback)
    
    
    public deleteDeliveryPipeline(request: google.cloud.deploy.v1.IDeleteDeliveryPipelineRequest, callback: google.cloud.deploy.v1.CloudDeploy.DeleteDeliveryPipelineCallback): void;

Calls DeleteDeliveryPipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletedeliverypipelinerequest)`   
DeleteDeliveryPipelineRequest message or plain object  
`callback` |  `[DeleteDeliveryPipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDeliveryPipeline(request)
    
    
    public deleteDeliveryPipeline(request: google.cloud.deploy.v1.IDeleteDeliveryPipelineRequest): Promise<google.longrunning.Operation>;

Calls DeleteDeliveryPipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletedeliverypipelinerequest)`   
DeleteDeliveryPipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### deleteDeployPolicy(request, callback)
    
    
    public deleteDeployPolicy(request: google.cloud.deploy.v1.IDeleteDeployPolicyRequest, callback: google.cloud.deploy.v1.CloudDeploy.DeleteDeployPolicyCallback): void;

Calls DeleteDeployPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletedeploypolicyrequest)`   
DeleteDeployPolicyRequest message or plain object  
`callback` |  `[DeleteDeployPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDeployPolicy(request)
    
    
    public deleteDeployPolicy(request: google.cloud.deploy.v1.IDeleteDeployPolicyRequest): Promise<google.longrunning.Operation>;

Calls DeleteDeployPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletedeploypolicyrequest)`   
DeleteDeployPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### deleteTarget(request, callback)
    
    
    public deleteTarget(request: google.cloud.deploy.v1.IDeleteTargetRequest, callback: google.cloud.deploy.v1.CloudDeploy.DeleteTargetCallback): void;

Calls DeleteTarget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletetargetrequest)`   
DeleteTargetRequest message or plain object  
`callback` |  `[DeleteTargetCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTarget(request)
    
    
    public deleteTarget(request: google.cloud.deploy.v1.IDeleteTargetRequest): Promise<google.longrunning.Operation>;

Calls DeleteTarget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideletetargetrequest)`   
DeleteTargetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### getAutomation(request, callback)
    
    
    public getAutomation(request: google.cloud.deploy.v1.IGetAutomationRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetAutomationCallback): void;

Calls GetAutomation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetautomationrequest)`   
GetAutomationRequest message or plain object  
`callback` |  `[GetAutomationCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Automation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAutomation(request)
    
    
    public getAutomation(request: google.cloud.deploy.v1.IGetAutomationRequest): Promise<google.cloud.deploy.v1.Automation>;

Calls GetAutomation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetautomationrequest)`   
GetAutomationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.Automation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automation)>` | Promise  
  
### getAutomationRun(request, callback)
    
    
    public getAutomationRun(request: google.cloud.deploy.v1.IGetAutomationRunRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetAutomationRunCallback): void;

Calls GetAutomationRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutomationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetautomationrunrequest)`   
GetAutomationRunRequest message or plain object  
`callback` |  `[GetAutomationRunCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and AutomationRun  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAutomationRun(request)
    
    
    public getAutomationRun(request: google.cloud.deploy.v1.IGetAutomationRunRequest): Promise<google.cloud.deploy.v1.AutomationRun>;

Calls GetAutomationRun.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAutomationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetautomationrunrequest)`   
GetAutomationRunRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.AutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class)>` | Promise  
  
### getConfig(request, callback)
    
    
    public getConfig(request: google.cloud.deploy.v1.IGetConfigRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetConfigCallback): void;

Calls GetConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetconfigrequest)`   
GetConfigRequest message or plain object  
`callback` |  `[GetConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Config  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConfig(request)
    
    
    public getConfig(request: google.cloud.deploy.v1.IGetConfigRequest): Promise<google.cloud.deploy.v1.Config>;

Calls GetConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetconfigrequest)`   
GetConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.Config](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.config)>` | Promise  
  
### getCustomTargetType(request, callback)
    
    
    public getCustomTargetType(request: google.cloud.deploy.v1.IGetCustomTargetTypeRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetCustomTargetTypeCallback): void;

Calls GetCustomTargetType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetcustomtargettyperequest)`   
GetCustomTargetTypeRequest message or plain object  
`callback` |  `[GetCustomTargetTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomTargetType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomTargetType(request)
    
    
    public getCustomTargetType(request: google.cloud.deploy.v1.IGetCustomTargetTypeRequest): Promise<google.cloud.deploy.v1.CustomTargetType>;

Calls GetCustomTargetType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetcustomtargettyperequest)`   
GetCustomTargetTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.CustomTargetType](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.customtargettype)>` | Promise  
  
### getDeliveryPipeline(request, callback)
    
    
    public getDeliveryPipeline(request: google.cloud.deploy.v1.IGetDeliveryPipelineRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetDeliveryPipelineCallback): void;

Calls GetDeliveryPipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetdeliverypipelinerequest)`   
GetDeliveryPipelineRequest message or plain object  
`callback` |  `[GetDeliveryPipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and DeliveryPipeline  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeliveryPipeline(request)
    
    
    public getDeliveryPipeline(request: google.cloud.deploy.v1.IGetDeliveryPipelineRequest): Promise<google.cloud.deploy.v1.DeliveryPipeline>;

Calls GetDeliveryPipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetdeliverypipelinerequest)`   
GetDeliveryPipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.DeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline)>` | Promise  
  
### getDeployPolicy(request, callback)
    
    
    public getDeployPolicy(request: google.cloud.deploy.v1.IGetDeployPolicyRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetDeployPolicyCallback): void;

Calls GetDeployPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetdeploypolicyrequest)`   
GetDeployPolicyRequest message or plain object  
`callback` |  `[GetDeployPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and DeployPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeployPolicy(request)
    
    
    public getDeployPolicy(request: google.cloud.deploy.v1.IGetDeployPolicyRequest): Promise<google.cloud.deploy.v1.DeployPolicy>;

Calls GetDeployPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetdeploypolicyrequest)`   
GetDeployPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.DeployPolicy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicy-class)>` | Promise  
  
### getJobRun(request, callback)
    
    
    public getJobRun(request: google.cloud.deploy.v1.IGetJobRunRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetJobRunCallback): void;

Calls GetJobRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetjobrunrequest)`   
GetJobRunRequest message or plain object  
`callback` |  `[GetJobRunCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and JobRun  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJobRun(request)
    
    
    public getJobRun(request: google.cloud.deploy.v1.IGetJobRunRequest): Promise<google.cloud.deploy.v1.JobRun>;

Calls GetJobRun.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetjobrunrequest)`   
GetJobRunRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.JobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class)>` | Promise  
  
### getRelease(request, callback)
    
    
    public getRelease(request: google.cloud.deploy.v1.IGetReleaseRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetReleaseCallback): void;

Calls GetRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetreleaserequest)`   
GetReleaseRequest message or plain object  
`callback` |  `[GetReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Release  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRelease(request)
    
    
    public getRelease(request: google.cloud.deploy.v1.IGetReleaseRequest): Promise<google.cloud.deploy.v1.Release>;

Calls GetRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetreleaserequest)`   
GetReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.Release](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.release-class)>` | Promise  
  
### getRollout(request, callback)
    
    
    public getRollout(request: google.cloud.deploy.v1.IGetRolloutRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetRolloutCallback): void;

Calls GetRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetrolloutrequest)`   
GetRolloutRequest message or plain object  
`callback` |  `[GetRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Rollout  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRollout(request)
    
    
    public getRollout(request: google.cloud.deploy.v1.IGetRolloutRequest): Promise<google.cloud.deploy.v1.Rollout>;

Calls GetRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igetrolloutrequest)`   
GetRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.Rollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class)>` | Promise  
  
### getTarget(request, callback)
    
    
    public getTarget(request: google.cloud.deploy.v1.IGetTargetRequest, callback: google.cloud.deploy.v1.CloudDeploy.GetTargetCallback): void;

Calls GetTarget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igettargetrequest)`   
GetTargetRequest message or plain object  
`callback` |  `[GetTargetCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Target  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTarget(request)
    
    
    public getTarget(request: google.cloud.deploy.v1.IGetTargetRequest): Promise<google.cloud.deploy.v1.Target>;

Calls GetTarget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.igettargetrequest)`   
GetTargetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.Target](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.target)>` | Promise  
  
### ignoreJob(request, callback)
    
    
    public ignoreJob(request: google.cloud.deploy.v1.IIgnoreJobRequest, callback: google.cloud.deploy.v1.CloudDeploy.IgnoreJobCallback): void;

Calls IgnoreJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IIgnoreJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iignorejobrequest)`   
IgnoreJobRequest message or plain object  
`callback` |  `[IgnoreJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and IgnoreJobResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### ignoreJob(request)
    
    
    public ignoreJob(request: google.cloud.deploy.v1.IIgnoreJobRequest): Promise<google.cloud.deploy.v1.IgnoreJobResponse>;

Calls IgnoreJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IIgnoreJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iignorejobrequest)`   
IgnoreJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.IgnoreJobResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ignorejobresponse)>` | Promise  
  
### listAutomationRuns(request, callback)
    
    
    public listAutomationRuns(request: google.cloud.deploy.v1.IListAutomationRunsRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListAutomationRunsCallback): void;

Calls ListAutomationRuns.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutomationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistautomationrunsrequest)`   
ListAutomationRunsRequest message or plain object  
`callback` |  `[ListAutomationRunsCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAutomationRunsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAutomationRuns(request)
    
    
    public listAutomationRuns(request: google.cloud.deploy.v1.IListAutomationRunsRequest): Promise<google.cloud.deploy.v1.ListAutomationRunsResponse>;

Calls ListAutomationRuns.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAutomationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistautomationrunsrequest)`   
ListAutomationRunsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListAutomationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listautomationrunsresponse)>` | Promise  
  
### listAutomations(request, callback)
    
    
    public listAutomations(request: google.cloud.deploy.v1.IListAutomationsRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListAutomationsCallback): void;

Calls ListAutomations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutomationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistautomationsrequest)`   
ListAutomationsRequest message or plain object  
`callback` |  `[ListAutomationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAutomationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAutomations(request)
    
    
    public listAutomations(request: google.cloud.deploy.v1.IListAutomationsRequest): Promise<google.cloud.deploy.v1.ListAutomationsResponse>;

Calls ListAutomations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAutomationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistautomationsrequest)`   
ListAutomationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListAutomationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listautomationsresponse)>` | Promise  
  
### listCustomTargetTypes(request, callback)
    
    
    public listCustomTargetTypes(request: google.cloud.deploy.v1.IListCustomTargetTypesRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListCustomTargetTypesCallback): void;

Calls ListCustomTargetTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomTargetTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistcustomtargettypesrequest)`   
ListCustomTargetTypesRequest message or plain object  
`callback` |  `[ListCustomTargetTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCustomTargetTypesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomTargetTypes(request)
    
    
    public listCustomTargetTypes(request: google.cloud.deploy.v1.IListCustomTargetTypesRequest): Promise<google.cloud.deploy.v1.ListCustomTargetTypesResponse>;

Calls ListCustomTargetTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCustomTargetTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistcustomtargettypesrequest)`   
ListCustomTargetTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListCustomTargetTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listcustomtargettypesresponse)>` | Promise  
  
### listDeliveryPipelines(request, callback)
    
    
    public listDeliveryPipelines(request: google.cloud.deploy.v1.IListDeliveryPipelinesRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListDeliveryPipelinesCallback): void;

Calls ListDeliveryPipelines.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeliveryPipelinesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistdeliverypipelinesrequest)`   
ListDeliveryPipelinesRequest message or plain object  
`callback` |  `[ListDeliveryPipelinesCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeliveryPipelinesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeliveryPipelines(request)
    
    
    public listDeliveryPipelines(request: google.cloud.deploy.v1.IListDeliveryPipelinesRequest): Promise<google.cloud.deploy.v1.ListDeliveryPipelinesResponse>;

Calls ListDeliveryPipelines.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeliveryPipelinesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistdeliverypipelinesrequest)`   
ListDeliveryPipelinesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListDeliveryPipelinesResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listdeliverypipelinesresponse)>` | Promise  
  
### listDeployPolicies(request, callback)
    
    
    public listDeployPolicies(request: google.cloud.deploy.v1.IListDeployPoliciesRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListDeployPoliciesCallback): void;

Calls ListDeployPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeployPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistdeploypoliciesrequest)`   
ListDeployPoliciesRequest message or plain object  
`callback` |  `[ListDeployPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeployPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeployPolicies(request)
    
    
    public listDeployPolicies(request: google.cloud.deploy.v1.IListDeployPoliciesRequest): Promise<google.cloud.deploy.v1.ListDeployPoliciesResponse>;

Calls ListDeployPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeployPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistdeploypoliciesrequest)`   
ListDeployPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListDeployPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listdeploypoliciesresponse)>` | Promise  
  
### listJobRuns(request, callback)
    
    
    public listJobRuns(request: google.cloud.deploy.v1.IListJobRunsRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListJobRunsCallback): void;

Calls ListJobRuns.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListJobRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistjobrunsrequest)`   
ListJobRunsRequest message or plain object  
`callback` |  `[ListJobRunsCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListJobRunsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listJobRuns(request)
    
    
    public listJobRuns(request: google.cloud.deploy.v1.IListJobRunsRequest): Promise<google.cloud.deploy.v1.ListJobRunsResponse>;

Calls ListJobRuns.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListJobRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistjobrunsrequest)`   
ListJobRunsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListJobRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listjobrunsresponse)>` | Promise  
  
### listReleases(request, callback)
    
    
    public listReleases(request: google.cloud.deploy.v1.IListReleasesRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListReleasesCallback): void;

Calls ListReleases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistreleasesrequest)`   
ListReleasesRequest message or plain object  
`callback` |  `[ListReleasesCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReleasesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleases(request)
    
    
    public listReleases(request: google.cloud.deploy.v1.IListReleasesRequest): Promise<google.cloud.deploy.v1.ListReleasesResponse>;

Calls ListReleases.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistreleasesrequest)`   
ListReleasesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListReleasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listreleasesresponse)>` | Promise  
  
### listRollouts(request, callback)
    
    
    public listRollouts(request: google.cloud.deploy.v1.IListRolloutsRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListRolloutsCallback): void;

Calls ListRollouts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistrolloutsrequest)`   
ListRolloutsRequest message or plain object  
`callback` |  `[ListRolloutsCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRolloutsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRollouts(request)
    
    
    public listRollouts(request: google.cloud.deploy.v1.IListRolloutsRequest): Promise<google.cloud.deploy.v1.ListRolloutsResponse>;

Calls ListRollouts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilistrolloutsrequest)`   
ListRolloutsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListRolloutsResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listrolloutsresponse)>` | Promise  
  
### listTargets(request, callback)
    
    
    public listTargets(request: google.cloud.deploy.v1.IListTargetsRequest, callback: google.cloud.deploy.v1.CloudDeploy.ListTargetsCallback): void;

Calls ListTargets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilisttargetsrequest)`   
ListTargetsRequest message or plain object  
`callback` |  `[ListTargetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTargetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTargets(request)
    
    
    public listTargets(request: google.cloud.deploy.v1.IListTargetsRequest): Promise<google.cloud.deploy.v1.ListTargetsResponse>;

Calls ListTargets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ilisttargetsrequest)`   
ListTargetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.ListTargetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.listtargetsresponse)>` | Promise  
  
### retryJob(request, callback)
    
    
    public retryJob(request: google.cloud.deploy.v1.IRetryJobRequest, callback: google.cloud.deploy.v1.CloudDeploy.RetryJobCallback): void;

Calls RetryJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iretryjobrequest)`   
RetryJobRequest message or plain object  
`callback` |  `[RetryJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and RetryJobResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### retryJob(request)
    
    
    public retryJob(request: google.cloud.deploy.v1.IRetryJobRequest): Promise<google.cloud.deploy.v1.RetryJobResponse>;

Calls RetryJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iretryjobrequest)`   
RetryJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.RetryJobResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobresponse)>` | Promise  
  
### rollbackTarget(request, callback)
    
    
    public rollbackTarget(request: google.cloud.deploy.v1.IRollbackTargetRequest, callback: google.cloud.deploy.v1.CloudDeploy.RollbackTargetCallback): void;

Calls RollbackTarget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irollbacktargetrequest)`   
RollbackTargetRequest message or plain object  
`callback` |  `[RollbackTargetCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and RollbackTargetResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rollbackTarget(request)
    
    
    public rollbackTarget(request: google.cloud.deploy.v1.IRollbackTargetRequest): Promise<google.cloud.deploy.v1.RollbackTargetResponse>;

Calls RollbackTarget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRollbackTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irollbacktargetrequest)`   
RollbackTargetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.RollbackTargetResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollbacktargetresponse)>` | Promise  
  
### terminateJobRun(request, callback)
    
    
    public terminateJobRun(request: google.cloud.deploy.v1.ITerminateJobRunRequest, callback: google.cloud.deploy.v1.CloudDeploy.TerminateJobRunCallback): void;

Calls TerminateJobRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITerminateJobRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iterminatejobrunrequest)`   
TerminateJobRunRequest message or plain object  
`callback` |  `[TerminateJobRunCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and TerminateJobRunResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### terminateJobRun(request)
    
    
    public terminateJobRun(request: google.cloud.deploy.v1.ITerminateJobRunRequest): Promise<google.cloud.deploy.v1.TerminateJobRunResponse>;

Calls TerminateJobRun.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITerminateJobRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iterminatejobrunrequest)`   
TerminateJobRunRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.deploy.v1.TerminateJobRunResponse](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.terminatejobrunresponse)>` | Promise  
  
### updateAutomation(request, callback)
    
    
    public updateAutomation(request: google.cloud.deploy.v1.IUpdateAutomationRequest, callback: google.cloud.deploy.v1.CloudDeploy.UpdateAutomationCallback): void;

Calls UpdateAutomation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdateautomationrequest)`   
UpdateAutomationRequest message or plain object  
`callback` |  `[UpdateAutomationCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAutomation(request)
    
    
    public updateAutomation(request: google.cloud.deploy.v1.IUpdateAutomationRequest): Promise<google.longrunning.Operation>;

Calls UpdateAutomation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutomationRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdateautomationrequest)`   
UpdateAutomationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### updateCustomTargetType(request, callback)
    
    
    public updateCustomTargetType(request: google.cloud.deploy.v1.IUpdateCustomTargetTypeRequest, callback: google.cloud.deploy.v1.CloudDeploy.UpdateCustomTargetTypeCallback): void;

Calls UpdateCustomTargetType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatecustomtargettyperequest)`   
UpdateCustomTargetTypeRequest message or plain object  
`callback` |  `[UpdateCustomTargetTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomTargetType(request)
    
    
    public updateCustomTargetType(request: google.cloud.deploy.v1.IUpdateCustomTargetTypeRequest): Promise<google.longrunning.Operation>;

Calls UpdateCustomTargetType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomTargetTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatecustomtargettyperequest)`   
UpdateCustomTargetTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### updateDeliveryPipeline(request, callback)
    
    
    public updateDeliveryPipeline(request: google.cloud.deploy.v1.IUpdateDeliveryPipelineRequest, callback: google.cloud.deploy.v1.CloudDeploy.UpdateDeliveryPipelineCallback): void;

Calls UpdateDeliveryPipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatedeliverypipelinerequest)`   
UpdateDeliveryPipelineRequest message or plain object  
`callback` |  `[UpdateDeliveryPipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDeliveryPipeline(request)
    
    
    public updateDeliveryPipeline(request: google.cloud.deploy.v1.IUpdateDeliveryPipelineRequest): Promise<google.longrunning.Operation>;

Calls UpdateDeliveryPipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeliveryPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatedeliverypipelinerequest)`   
UpdateDeliveryPipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### updateDeployPolicy(request, callback)
    
    
    public updateDeployPolicy(request: google.cloud.deploy.v1.IUpdateDeployPolicyRequest, callback: google.cloud.deploy.v1.CloudDeploy.UpdateDeployPolicyCallback): void;

Calls UpdateDeployPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatedeploypolicyrequest)`   
UpdateDeployPolicyRequest message or plain object  
`callback` |  `[UpdateDeployPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDeployPolicy(request)
    
    
    public updateDeployPolicy(request: google.cloud.deploy.v1.IUpdateDeployPolicyRequest): Promise<google.longrunning.Operation>;

Calls UpdateDeployPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeployPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatedeploypolicyrequest)`   
UpdateDeployPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
### updateTarget(request, callback)
    
    
    public updateTarget(request: google.cloud.deploy.v1.IUpdateTargetRequest, callback: google.cloud.deploy.v1.CloudDeploy.UpdateTargetCallback): void;

Calls UpdateTarget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatetargetrequest)`   
UpdateTargetRequest message or plain object  
`callback` |  `[UpdateTargetCallback](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTarget(request)
    
    
    public updateTarget(request: google.cloud.deploy.v1.IUpdateTargetRequest): Promise<google.longrunning.Operation>;

Calls UpdateTarget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iupdatetargetrequest)`   
UpdateTargetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
