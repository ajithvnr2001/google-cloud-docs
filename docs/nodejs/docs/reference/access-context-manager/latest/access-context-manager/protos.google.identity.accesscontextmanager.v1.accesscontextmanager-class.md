---
url: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.accesscontextmanager-class
title: Class protos.google.identity.accesscontextmanager.v1.AccessContextManager (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:54.951966+00:00
---

# Class protos.google.identity.accesscontextmanager.v1.AccessContextManager (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.accesscontextmanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.identity.accesscontextmanager.v1.AccessContextManager (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  2.3.2  2.2.0  2.1.1  1.0.0  0.2.0 

Represents an AccessContextManager

## Inheritance

$protobuf.rpc.Service > protos.google.identity.accesscontextmanager.v1.AccessContextManager

## Package

[@google-cloud/access-context-manager](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AccessContextManager service.

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

### commitServicePerimeters(request, callback)
    
    
    public commitServicePerimeters(request: google.identity.accesscontextmanager.v1.ICommitServicePerimetersRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.CommitServicePerimetersCallback): void;

Calls CommitServicePerimeters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitServicePerimetersRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icommitserviceperimetersrequest)`   
CommitServicePerimetersRequest message or plain object  
`callback` |  `[CommitServicePerimetersCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commitServicePerimeters(request)
    
    
    public commitServicePerimeters(request: google.identity.accesscontextmanager.v1.ICommitServicePerimetersRequest): Promise<google.longrunning.Operation>;

Calls CommitServicePerimeters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICommitServicePerimetersRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icommitserviceperimetersrequest)`   
CommitServicePerimetersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AccessContextManager;

Creates new AccessContextManager service using the specified rpc implementation.

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
`[AccessContextManager](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.accesscontextmanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAccessLevel(request, callback)
    
    
    public createAccessLevel(request: google.identity.accesscontextmanager.v1.ICreateAccessLevelRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessLevelCallback): void;

Calls CreateAccessLevel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icreateaccesslevelrequest)`   
CreateAccessLevelRequest message or plain object  
`callback` |  `[CreateAccessLevelCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAccessLevel(request)
    
    
    public createAccessLevel(request: google.identity.accesscontextmanager.v1.ICreateAccessLevelRequest): Promise<google.longrunning.Operation>;

Calls CreateAccessLevel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icreateaccesslevelrequest)`   
CreateAccessLevelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### createAccessPolicy(request, callback)
    
    
    public createAccessPolicy(request: google.identity.accesscontextmanager.v1.IAccessPolicy, callback: google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessPolicyCallback): void;

Calls CreateAccessPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAccessPolicy](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iaccesspolicy)`   
AccessPolicy message or plain object  
`callback` |  `[CreateAccessPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAccessPolicy(request)
    
    
    public createAccessPolicy(request: google.identity.accesscontextmanager.v1.IAccessPolicy): Promise<google.longrunning.Operation>;

Calls CreateAccessPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAccessPolicy](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iaccesspolicy)`   
AccessPolicy message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### createGcpUserAccessBinding(request, callback)
    
    
    public createGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.ICreateGcpUserAccessBindingRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.CreateGcpUserAccessBindingCallback): void;

Calls CreateGcpUserAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icreategcpuseraccessbindingrequest)`   
CreateGcpUserAccessBindingRequest message or plain object  
`callback` |  `[CreateGcpUserAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGcpUserAccessBinding(request)
    
    
    public createGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.ICreateGcpUserAccessBindingRequest): Promise<google.longrunning.Operation>;

Calls CreateGcpUserAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icreategcpuseraccessbindingrequest)`   
CreateGcpUserAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### createServicePerimeter(request, callback)
    
    
    public createServicePerimeter(request: google.identity.accesscontextmanager.v1.ICreateServicePerimeterRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.CreateServicePerimeterCallback): void;

Calls CreateServicePerimeter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icreateserviceperimeterrequest)`   
CreateServicePerimeterRequest message or plain object  
`callback` |  `[CreateServicePerimeterCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createServicePerimeter(request)
    
    
    public createServicePerimeter(request: google.identity.accesscontextmanager.v1.ICreateServicePerimeterRequest): Promise<google.longrunning.Operation>;

Calls CreateServicePerimeter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.icreateserviceperimeterrequest)`   
CreateServicePerimeterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteAccessLevel(request, callback)
    
    
    public deleteAccessLevel(request: google.identity.accesscontextmanager.v1.IDeleteAccessLevelRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessLevelCallback): void;

Calls DeleteAccessLevel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideleteaccesslevelrequest)`   
DeleteAccessLevelRequest message or plain object  
`callback` |  `[DeleteAccessLevelCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAccessLevel(request)
    
    
    public deleteAccessLevel(request: google.identity.accesscontextmanager.v1.IDeleteAccessLevelRequest): Promise<google.longrunning.Operation>;

Calls DeleteAccessLevel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideleteaccesslevelrequest)`   
DeleteAccessLevelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteAccessPolicy(request, callback)
    
    
    public deleteAccessPolicy(request: google.identity.accesscontextmanager.v1.IDeleteAccessPolicyRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessPolicyCallback): void;

Calls DeleteAccessPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideleteaccesspolicyrequest)`   
DeleteAccessPolicyRequest message or plain object  
`callback` |  `[DeleteAccessPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAccessPolicy(request)
    
    
    public deleteAccessPolicy(request: google.identity.accesscontextmanager.v1.IDeleteAccessPolicyRequest): Promise<google.longrunning.Operation>;

Calls DeleteAccessPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideleteaccesspolicyrequest)`   
DeleteAccessPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteGcpUserAccessBinding(request, callback)
    
    
    public deleteGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.IDeleteGcpUserAccessBindingRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.DeleteGcpUserAccessBindingCallback): void;

Calls DeleteGcpUserAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideletegcpuseraccessbindingrequest)`   
DeleteGcpUserAccessBindingRequest message or plain object  
`callback` |  `[DeleteGcpUserAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGcpUserAccessBinding(request)
    
    
    public deleteGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.IDeleteGcpUserAccessBindingRequest): Promise<google.longrunning.Operation>;

Calls DeleteGcpUserAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideletegcpuseraccessbindingrequest)`   
DeleteGcpUserAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteServicePerimeter(request, callback)
    
    
    public deleteServicePerimeter(request: google.identity.accesscontextmanager.v1.IDeleteServicePerimeterRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.DeleteServicePerimeterCallback): void;

Calls DeleteServicePerimeter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideleteserviceperimeterrequest)`   
DeleteServicePerimeterRequest message or plain object  
`callback` |  `[DeleteServicePerimeterCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteServicePerimeter(request)
    
    
    public deleteServicePerimeter(request: google.identity.accesscontextmanager.v1.IDeleteServicePerimeterRequest): Promise<google.longrunning.Operation>;

Calls DeleteServicePerimeter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ideleteserviceperimeterrequest)`   
DeleteServicePerimeterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### getAccessLevel(request, callback)
    
    
    public getAccessLevel(request: google.identity.accesscontextmanager.v1.IGetAccessLevelRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessLevelCallback): void;

Calls GetAccessLevel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetaccesslevelrequest)`   
GetAccessLevelRequest message or plain object  
`callback` |  `[GetAccessLevelCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessLevel  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccessLevel(request)
    
    
    public getAccessLevel(request: google.identity.accesscontextmanager.v1.IGetAccessLevelRequest): Promise<google.identity.accesscontextmanager.v1.AccessLevel>;

Calls GetAccessLevel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetaccesslevelrequest)`   
GetAccessLevelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.AccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.accesslevel)>` | Promise  
  
### getAccessPolicy(request, callback)
    
    
    public getAccessPolicy(request: google.identity.accesscontextmanager.v1.IGetAccessPolicyRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessPolicyCallback): void;

Calls GetAccessPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetaccesspolicyrequest)`   
GetAccessPolicyRequest message or plain object  
`callback` |  `[GetAccessPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccessPolicy(request)
    
    
    public getAccessPolicy(request: google.identity.accesscontextmanager.v1.IGetAccessPolicyRequest): Promise<google.identity.accesscontextmanager.v1.AccessPolicy>;

Calls GetAccessPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetaccesspolicyrequest)`   
GetAccessPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.AccessPolicy](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.accesspolicy)>` | Promise  
  
### getGcpUserAccessBinding(request, callback)
    
    
    public getGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.IGetGcpUserAccessBindingRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.GetGcpUserAccessBindingCallback): void;

Calls GetGcpUserAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetgcpuseraccessbindingrequest)`   
GetGcpUserAccessBindingRequest message or plain object  
`callback` |  `[GetGcpUserAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and GcpUserAccessBinding  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGcpUserAccessBinding(request)
    
    
    public getGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.IGetGcpUserAccessBindingRequest): Promise<google.identity.accesscontextmanager.v1.GcpUserAccessBinding>;

Calls GetGcpUserAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetgcpuseraccessbindingrequest)`   
GetGcpUserAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.GcpUserAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.gcpuseraccessbinding)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.policy)>` | Promise  
  
### getServicePerimeter(request, callback)
    
    
    public getServicePerimeter(request: google.identity.accesscontextmanager.v1.IGetServicePerimeterRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.GetServicePerimeterCallback): void;

Calls GetServicePerimeter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetserviceperimeterrequest)`   
GetServicePerimeterRequest message or plain object  
`callback` |  `[GetServicePerimeterCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ServicePerimeter  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServicePerimeter(request)
    
    
    public getServicePerimeter(request: google.identity.accesscontextmanager.v1.IGetServicePerimeterRequest): Promise<google.identity.accesscontextmanager.v1.ServicePerimeter>;

Calls GetServicePerimeter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.igetserviceperimeterrequest)`   
GetServicePerimeterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.ServicePerimeter](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.serviceperimeter-class)>` | Promise  
  
### listAccessLevels(request, callback)
    
    
    public listAccessLevels(request: google.identity.accesscontextmanager.v1.IListAccessLevelsRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessLevelsCallback): void;

Calls ListAccessLevels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessLevelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistaccesslevelsrequest)`   
ListAccessLevelsRequest message or plain object  
`callback` |  `[ListAccessLevelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccessLevelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccessLevels(request)
    
    
    public listAccessLevels(request: google.identity.accesscontextmanager.v1.IListAccessLevelsRequest): Promise<google.identity.accesscontextmanager.v1.ListAccessLevelsResponse>;

Calls ListAccessLevels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccessLevelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistaccesslevelsrequest)`   
ListAccessLevelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.ListAccessLevelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.listaccesslevelsresponse)>` | Promise  
  
### listAccessPolicies(request, callback)
    
    
    public listAccessPolicies(request: google.identity.accesscontextmanager.v1.IListAccessPoliciesRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessPoliciesCallback): void;

Calls ListAccessPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistaccesspoliciesrequest)`   
ListAccessPoliciesRequest message or plain object  
`callback` |  `[ListAccessPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccessPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccessPolicies(request)
    
    
    public listAccessPolicies(request: google.identity.accesscontextmanager.v1.IListAccessPoliciesRequest): Promise<google.identity.accesscontextmanager.v1.ListAccessPoliciesResponse>;

Calls ListAccessPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccessPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistaccesspoliciesrequest)`   
ListAccessPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.ListAccessPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.listaccesspoliciesresponse)>` | Promise  
  
### listGcpUserAccessBindings(request, callback)
    
    
    public listGcpUserAccessBindings(request: google.identity.accesscontextmanager.v1.IListGcpUserAccessBindingsRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.ListGcpUserAccessBindingsCallback): void;

Calls ListGcpUserAccessBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGcpUserAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistgcpuseraccessbindingsrequest)`   
ListGcpUserAccessBindingsRequest message or plain object  
`callback` |  `[ListGcpUserAccessBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGcpUserAccessBindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGcpUserAccessBindings(request)
    
    
    public listGcpUserAccessBindings(request: google.identity.accesscontextmanager.v1.IListGcpUserAccessBindingsRequest): Promise<google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsResponse>;

Calls ListGcpUserAccessBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGcpUserAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistgcpuseraccessbindingsrequest)`   
ListGcpUserAccessBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.listgcpuseraccessbindingsresponse)>` | Promise  
  
### listServicePerimeters(request, callback)
    
    
    public listServicePerimeters(request: google.identity.accesscontextmanager.v1.IListServicePerimetersRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.ListServicePerimetersCallback): void;

Calls ListServicePerimeters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicePerimetersRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistserviceperimetersrequest)`   
ListServicePerimetersRequest message or plain object  
`callback` |  `[ListServicePerimetersCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServicePerimetersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServicePerimeters(request)
    
    
    public listServicePerimeters(request: google.identity.accesscontextmanager.v1.IListServicePerimetersRequest): Promise<google.identity.accesscontextmanager.v1.ListServicePerimetersResponse>;

Calls ListServicePerimeters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServicePerimetersRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ilistserviceperimetersrequest)`   
ListServicePerimetersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.identity.accesscontextmanager.v1.ListServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.listserviceperimetersresponse)>` | Promise  
  
### replaceAccessLevels(request, callback)
    
    
    public replaceAccessLevels(request: google.identity.accesscontextmanager.v1.IReplaceAccessLevelsRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceAccessLevelsCallback): void;

Calls ReplaceAccessLevels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReplaceAccessLevelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceaccesslevelsrequest)`   
ReplaceAccessLevelsRequest message or plain object  
`callback` |  `[ReplaceAccessLevelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### replaceAccessLevels(request)
    
    
    public replaceAccessLevels(request: google.identity.accesscontextmanager.v1.IReplaceAccessLevelsRequest): Promise<google.longrunning.Operation>;

Calls ReplaceAccessLevels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReplaceAccessLevelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceaccesslevelsrequest)`   
ReplaceAccessLevelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### replaceServicePerimeters(request, callback)
    
    
    public replaceServicePerimeters(request: google.identity.accesscontextmanager.v1.IReplaceServicePerimetersRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceServicePerimetersCallback): void;

Calls ReplaceServicePerimeters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReplaceServicePerimetersRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceserviceperimetersrequest)`   
ReplaceServicePerimetersRequest message or plain object  
`callback` |  `[ReplaceServicePerimetersCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### replaceServicePerimeters(request)
    
    
    public replaceServicePerimeters(request: google.identity.accesscontextmanager.v1.IReplaceServicePerimetersRequest): Promise<google.longrunning.Operation>;

Calls ReplaceServicePerimeters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReplaceServicePerimetersRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceserviceperimetersrequest)`   
ReplaceServicePerimetersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.policy)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and TestIamPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest): Promise<google.iam.v1.TestIamPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.testiampermissionsresponse)>` | Promise  
  
### updateAccessLevel(request, callback)
    
    
    public updateAccessLevel(request: google.identity.accesscontextmanager.v1.IUpdateAccessLevelRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessLevelCallback): void;

Calls UpdateAccessLevel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdateaccesslevelrequest)`   
UpdateAccessLevelRequest message or plain object  
`callback` |  `[UpdateAccessLevelCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAccessLevel(request)
    
    
    public updateAccessLevel(request: google.identity.accesscontextmanager.v1.IUpdateAccessLevelRequest): Promise<google.longrunning.Operation>;

Calls UpdateAccessLevel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdateaccesslevelrequest)`   
UpdateAccessLevelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### updateAccessPolicy(request, callback)
    
    
    public updateAccessPolicy(request: google.identity.accesscontextmanager.v1.IUpdateAccessPolicyRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessPolicyCallback): void;

Calls UpdateAccessPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdateaccesspolicyrequest)`   
UpdateAccessPolicyRequest message or plain object  
`callback` |  `[UpdateAccessPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAccessPolicy(request)
    
    
    public updateAccessPolicy(request: google.identity.accesscontextmanager.v1.IUpdateAccessPolicyRequest): Promise<google.longrunning.Operation>;

Calls UpdateAccessPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdateaccesspolicyrequest)`   
UpdateAccessPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### updateGcpUserAccessBinding(request, callback)
    
    
    public updateGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.IUpdateGcpUserAccessBindingRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.UpdateGcpUserAccessBindingCallback): void;

Calls UpdateGcpUserAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdategcpuseraccessbindingrequest)`   
UpdateGcpUserAccessBindingRequest message or plain object  
`callback` |  `[UpdateGcpUserAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGcpUserAccessBinding(request)
    
    
    public updateGcpUserAccessBinding(request: google.identity.accesscontextmanager.v1.IUpdateGcpUserAccessBindingRequest): Promise<google.longrunning.Operation>;

Calls UpdateGcpUserAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdategcpuseraccessbindingrequest)`   
UpdateGcpUserAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
### updateServicePerimeter(request, callback)
    
    
    public updateServicePerimeter(request: google.identity.accesscontextmanager.v1.IUpdateServicePerimeterRequest, callback: google.identity.accesscontextmanager.v1.AccessContextManager.UpdateServicePerimeterCallback): void;

Calls UpdateServicePerimeter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdateserviceperimeterrequest)`   
UpdateServicePerimeterRequest message or plain object  
`callback` |  `[UpdateServicePerimeterCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateServicePerimeter(request)
    
    
    public updateServicePerimeter(request: google.identity.accesscontextmanager.v1.IUpdateServicePerimeterRequest): Promise<google.longrunning.Operation>;

Calls UpdateServicePerimeter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServicePerimeterRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdateserviceperimeterrequest)`   
UpdateServicePerimeterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
