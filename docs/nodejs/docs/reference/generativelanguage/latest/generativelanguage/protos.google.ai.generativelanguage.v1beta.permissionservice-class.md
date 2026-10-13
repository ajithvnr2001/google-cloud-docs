---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.permissionservice-class
title: Class protos.google.ai.generativelanguage.v1beta.PermissionService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:45.046796+00:00
---

# Class protos.google.ai.generativelanguage.v1beta.PermissionService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.permissionservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1beta.PermissionService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a PermissionService

## Inheritance

$protobuf.rpc.Service > protos.google.ai.generativelanguage.v1beta.PermissionService

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PermissionService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PermissionService;

Creates new PermissionService service using the specified rpc implementation.

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
`[PermissionService](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.permissionservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createPermission(request, callback)
    
    
    public createPermission(request: google.ai.generativelanguage.v1beta.ICreatePermissionRequest, callback: google.ai.generativelanguage.v1beta.PermissionService.CreatePermissionCallback): void;

Calls CreatePermission.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatepermissionrequest)`   
CreatePermissionRequest message or plain object  
`callback` |  `[CreatePermissionCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Permission  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPermission(request)
    
    
    public createPermission(request: google.ai.generativelanguage.v1beta.ICreatePermissionRequest): Promise<google.ai.generativelanguage.v1beta.Permission>;

Calls CreatePermission.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatepermissionrequest)`   
CreatePermissionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta.Permission](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.permission-class)>` | Promise  
  
### deletePermission(request, callback)
    
    
    public deletePermission(request: google.ai.generativelanguage.v1beta.IDeletePermissionRequest, callback: google.ai.generativelanguage.v1beta.PermissionService.DeletePermissionCallback): void;

Calls DeletePermission.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletepermissionrequest)`   
DeletePermissionRequest message or plain object  
`callback` |  `[DeletePermissionCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePermission(request)
    
    
    public deletePermission(request: google.ai.generativelanguage.v1beta.IDeletePermissionRequest): Promise<google.protobuf.Empty>;

Calls DeletePermission.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletepermissionrequest)`   
DeletePermissionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` | Promise  
  
### getPermission(request, callback)
    
    
    public getPermission(request: google.ai.generativelanguage.v1beta.IGetPermissionRequest, callback: google.ai.generativelanguage.v1beta.PermissionService.GetPermissionCallback): void;

Calls GetPermission.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetpermissionrequest)`   
GetPermissionRequest message or plain object  
`callback` |  `[GetPermissionCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Permission  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPermission(request)
    
    
    public getPermission(request: google.ai.generativelanguage.v1beta.IGetPermissionRequest): Promise<google.ai.generativelanguage.v1beta.Permission>;

Calls GetPermission.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetpermissionrequest)`   
GetPermissionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta.Permission](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.permission-class)>` | Promise  
  
### listPermissions(request, callback)
    
    
    public listPermissions(request: google.ai.generativelanguage.v1beta.IListPermissionsRequest, callback: google.ai.generativelanguage.v1beta.PermissionService.ListPermissionsCallback): void;

Calls ListPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistpermissionsrequest)`   
ListPermissionsRequest message or plain object  
`callback` |  `[ListPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPermissions(request)
    
    
    public listPermissions(request: google.ai.generativelanguage.v1beta.IListPermissionsRequest): Promise<google.ai.generativelanguage.v1beta.ListPermissionsResponse>;

Calls ListPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistpermissionsrequest)`   
ListPermissionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta.ListPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.listpermissionsresponse)>` | Promise  
  
### transferOwnership(request, callback)
    
    
    public transferOwnership(request: google.ai.generativelanguage.v1beta.ITransferOwnershipRequest, callback: google.ai.generativelanguage.v1beta.PermissionService.TransferOwnershipCallback): void;

Calls TransferOwnership.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITransferOwnershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.itransferownershiprequest)`   
TransferOwnershipRequest message or plain object  
`callback` |  `[TransferOwnershipCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and TransferOwnershipResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### transferOwnership(request)
    
    
    public transferOwnership(request: google.ai.generativelanguage.v1beta.ITransferOwnershipRequest): Promise<google.ai.generativelanguage.v1beta.TransferOwnershipResponse>;

Calls TransferOwnership.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITransferOwnershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.itransferownershiprequest)`   
TransferOwnershipRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta.TransferOwnershipResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.transferownershipresponse)>` | Promise  
  
### updatePermission(request, callback)
    
    
    public updatePermission(request: google.ai.generativelanguage.v1beta.IUpdatePermissionRequest, callback: google.ai.generativelanguage.v1beta.PermissionService.UpdatePermissionCallback): void;

Calls UpdatePermission.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatepermissionrequest)`   
UpdatePermissionRequest message or plain object  
`callback` |  `[UpdatePermissionCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Permission  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePermission(request)
    
    
    public updatePermission(request: google.ai.generativelanguage.v1beta.IUpdatePermissionRequest): Promise<google.ai.generativelanguage.v1beta.Permission>;

Calls UpdatePermission.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePermissionRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatepermissionrequest)`   
UpdatePermissionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta.Permission](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.permission-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
