---
url: https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.lustre-class
title: Class protos.google.cloud.lustre.v1.Lustre (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:32.903293+00:00
---

# Class protos.google.cloud.lustre.v1.Lustre (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.lustre-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.lustre.v1.Lustre (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0 

Represents a Lustre

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.lustre.v1.Lustre

## Package

[@google-cloud/lustre](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Lustre service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Lustre;

Creates new Lustre service using the specified rpc implementation.

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
`[Lustre](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.lustre-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDirectoryPolicy(request, callback)
    
    
    public createDirectoryPolicy(request: google.cloud.lustre.v1.ICreateDirectoryPolicyRequest, callback: google.cloud.lustre.v1.Lustre.CreateDirectoryPolicyCallback): void;

Calls CreateDirectoryPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDirectoryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatedirectorypolicyrequest)`   
CreateDirectoryPolicyRequest message or plain object  
`callback` |  `[CreateDirectoryPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDirectoryPolicy(request)
    
    
    public createDirectoryPolicy(request: google.cloud.lustre.v1.ICreateDirectoryPolicyRequest): Promise<google.longrunning.Operation>;

Calls CreateDirectoryPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDirectoryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatedirectorypolicyrequest)`   
CreateDirectoryPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### createInstance(request, callback)
    
    
    public createInstance(request: google.cloud.lustre.v1.ICreateInstanceRequest, callback: google.cloud.lustre.v1.Lustre.CreateInstanceCallback): void;

Calls CreateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
`callback` |  `[CreateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstance(request)
    
    
    public createInstance(request: google.cloud.lustre.v1.ICreateInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### createMirror(request, callback)
    
    
    public createMirror(request: google.cloud.lustre.v1.ICreateMirrorRequest, callback: google.cloud.lustre.v1.Lustre.CreateMirrorCallback): void;

Calls CreateMirror.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatemirrorrequest)`   
CreateMirrorRequest message or plain object  
`callback` |  `[CreateMirrorCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMirror(request)
    
    
    public createMirror(request: google.cloud.lustre.v1.ICreateMirrorRequest): Promise<google.longrunning.Operation>;

Calls CreateMirror.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatemirrorrequest)`   
CreateMirrorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### deleteDirectoryPolicy(request, callback)
    
    
    public deleteDirectoryPolicy(request: google.cloud.lustre.v1.IDeleteDirectoryPolicyRequest, callback: google.cloud.lustre.v1.Lustre.DeleteDirectoryPolicyCallback): void;

Calls DeleteDirectoryPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDirectoryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ideletedirectorypolicyrequest)`   
DeleteDirectoryPolicyRequest message or plain object  
`callback` |  `[DeleteDirectoryPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDirectoryPolicy(request)
    
    
    public deleteDirectoryPolicy(request: google.cloud.lustre.v1.IDeleteDirectoryPolicyRequest): Promise<google.longrunning.Operation>;

Calls DeleteDirectoryPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDirectoryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ideletedirectorypolicyrequest)`   
DeleteDirectoryPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### deleteInstance(request, callback)
    
    
    public deleteInstance(request: google.cloud.lustre.v1.IDeleteInstanceRequest, callback: google.cloud.lustre.v1.Lustre.DeleteInstanceCallback): void;

Calls DeleteInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
`callback` |  `[DeleteInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstance(request)
    
    
    public deleteInstance(request: google.cloud.lustre.v1.IDeleteInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### deleteMirror(request, callback)
    
    
    public deleteMirror(request: google.cloud.lustre.v1.IDeleteMirrorRequest, callback: google.cloud.lustre.v1.Lustre.DeleteMirrorCallback): void;

Calls DeleteMirror.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ideletemirrorrequest)`   
DeleteMirrorRequest message or plain object  
`callback` |  `[DeleteMirrorCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMirror(request)
    
    
    public deleteMirror(request: google.cloud.lustre.v1.IDeleteMirrorRequest): Promise<google.longrunning.Operation>;

Calls DeleteMirror.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ideletemirrorrequest)`   
DeleteMirrorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### exportData(request, callback)
    
    
    public exportData(request: google.cloud.lustre.v1.IExportDataRequest, callback: google.cloud.lustre.v1.Lustre.ExportDataCallback): void;

Calls ExportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iexportdatarequest)`   
ExportDataRequest message or plain object  
`callback` |  `[ExportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request)
    
    
    public exportData(request: google.cloud.lustre.v1.IExportDataRequest): Promise<google.longrunning.Operation>;

Calls ExportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iexportdatarequest)`   
ExportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### getDirectoryPolicy(request, callback)
    
    
    public getDirectoryPolicy(request: google.cloud.lustre.v1.IGetDirectoryPolicyRequest, callback: google.cloud.lustre.v1.Lustre.GetDirectoryPolicyCallback): void;

Calls GetDirectoryPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDirectoryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.igetdirectorypolicyrequest)`   
GetDirectoryPolicyRequest message or plain object  
`callback` |  `[GetDirectoryPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and DirectoryPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDirectoryPolicy(request)
    
    
    public getDirectoryPolicy(request: google.cloud.lustre.v1.IGetDirectoryPolicyRequest): Promise<google.cloud.lustre.v1.DirectoryPolicy>;

Calls GetDirectoryPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDirectoryPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.igetdirectorypolicyrequest)`   
GetDirectoryPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.lustre.v1.DirectoryPolicy](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.directorypolicy-class)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.lustre.v1.IGetInstanceRequest, callback: google.cloud.lustre.v1.Lustre.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.lustre.v1.IGetInstanceRequest): Promise<google.cloud.lustre.v1.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.lustre.v1.Instance](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.instance-class)>` | Promise  
  
### getMirror(request, callback)
    
    
    public getMirror(request: google.cloud.lustre.v1.IGetMirrorRequest, callback: google.cloud.lustre.v1.Lustre.GetMirrorCallback): void;

Calls GetMirror.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.igetmirrorrequest)`   
GetMirrorRequest message or plain object  
`callback` |  `[GetMirrorCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Mirror  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMirror(request)
    
    
    public getMirror(request: google.cloud.lustre.v1.IGetMirrorRequest): Promise<google.cloud.lustre.v1.Mirror>;

Calls GetMirror.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.igetmirrorrequest)`   
GetMirrorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.lustre.v1.Mirror](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.mirror-class)>` | Promise  
  
### importData(request, callback)
    
    
    public importData(request: google.cloud.lustre.v1.IImportDataRequest, callback: google.cloud.lustre.v1.Lustre.ImportDataCallback): void;

Calls ImportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iimportdatarequest)`   
ImportDataRequest message or plain object  
`callback` |  `[ImportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request)
    
    
    public importData(request: google.cloud.lustre.v1.IImportDataRequest): Promise<google.longrunning.Operation>;

Calls ImportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iimportdatarequest)`   
ImportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### listDirectoryPolicies(request, callback)
    
    
    public listDirectoryPolicies(request: google.cloud.lustre.v1.IListDirectoryPoliciesRequest, callback: google.cloud.lustre.v1.Lustre.ListDirectoryPoliciesCallback): void;

Calls ListDirectoryPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDirectoryPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ilistdirectorypoliciesrequest)`   
ListDirectoryPoliciesRequest message or plain object  
`callback` |  `[ListDirectoryPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDirectoryPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDirectoryPolicies(request)
    
    
    public listDirectoryPolicies(request: google.cloud.lustre.v1.IListDirectoryPoliciesRequest): Promise<google.cloud.lustre.v1.ListDirectoryPoliciesResponse>;

Calls ListDirectoryPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDirectoryPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ilistdirectorypoliciesrequest)`   
ListDirectoryPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.lustre.v1.ListDirectoryPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.listdirectorypoliciesresponse)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.lustre.v1.IListInstancesRequest, callback: google.cloud.lustre.v1.Lustre.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.lustre.v1.IListInstancesRequest): Promise<google.cloud.lustre.v1.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.lustre.v1.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.listinstancesresponse)>` | Promise  
  
### listMirrors(request, callback)
    
    
    public listMirrors(request: google.cloud.lustre.v1.IListMirrorsRequest, callback: google.cloud.lustre.v1.Lustre.ListMirrorsCallback): void;

Calls ListMirrors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMirrorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ilistmirrorsrequest)`   
ListMirrorsRequest message or plain object  
`callback` |  `[ListMirrorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMirrorsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMirrors(request)
    
    
    public listMirrors(request: google.cloud.lustre.v1.IListMirrorsRequest): Promise<google.cloud.lustre.v1.ListMirrorsResponse>;

Calls ListMirrors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMirrorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ilistmirrorsrequest)`   
ListMirrorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.lustre.v1.ListMirrorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.listmirrorsresponse)>` | Promise  
  
### rescheduleMaintenance(request, callback)
    
    
    public rescheduleMaintenance(request: google.cloud.lustre.v1.IRescheduleMaintenanceRequest, callback: google.cloud.lustre.v1.Lustre.RescheduleMaintenanceCallback): void;

Calls RescheduleMaintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
`callback` |  `[RescheduleMaintenanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rescheduleMaintenance(request)
    
    
    public rescheduleMaintenance(request: google.cloud.lustre.v1.IRescheduleMaintenanceRequest): Promise<google.longrunning.Operation>;

Calls RescheduleMaintenance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### updateInstance(request, callback)
    
    
    public updateInstance(request: google.cloud.lustre.v1.IUpdateInstanceRequest, callback: google.cloud.lustre.v1.Lustre.UpdateInstanceCallback): void;

Calls UpdateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
`callback` |  `[UpdateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInstance(request)
    
    
    public updateInstance(request: google.cloud.lustre.v1.IUpdateInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpdateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
### updateMirror(request, callback)
    
    
    public updateMirror(request: google.cloud.lustre.v1.IUpdateMirrorRequest, callback: google.cloud.lustre.v1.Lustre.UpdateMirrorCallback): void;

Calls UpdateMirror.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iupdatemirrorrequest)`   
UpdateMirrorRequest message or plain object  
`callback` |  `[UpdateMirrorCallback](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMirror(request)
    
    
    public updateMirror(request: google.cloud.lustre.v1.IUpdateMirrorRequest): Promise<google.longrunning.Operation>;

Calls UpdateMirror.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMirrorRequest](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.iupdatemirrorrequest)`   
UpdateMirrorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
