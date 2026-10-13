---
url: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.vmmigration-class
title: Class protos.google.cloud.vmmigration.v1.VmMigration (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:06.243092+00:00
---

# Class protos.google.cloud.vmmigration.v1.VmMigration (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.vmmigration-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vmmigration.v1.VmMigration (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.2  2.3.2  2.2.1  2.1.0  1.0.0  0.2.0 

Represents a VmMigration

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.vmmigration.v1.VmMigration

## Package

[@google-cloud/vmmigration](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new VmMigration service.

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

### addGroupMigration(request, callback)
    
    
    public addGroupMigration(request: google.cloud.vmmigration.v1.IAddGroupMigrationRequest, callback: google.cloud.vmmigration.v1.VmMigration.AddGroupMigrationCallback): void;

Calls AddGroupMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddGroupMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iaddgroupmigrationrequest)`   
AddGroupMigrationRequest message or plain object  
`callback` |  `[AddGroupMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addGroupMigration(request)
    
    
    public addGroupMigration(request: google.cloud.vmmigration.v1.IAddGroupMigrationRequest): Promise<google.longrunning.Operation>;

Calls AddGroupMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddGroupMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iaddgroupmigrationrequest)`   
AddGroupMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### cancelCloneJob(request, callback)
    
    
    public cancelCloneJob(request: google.cloud.vmmigration.v1.ICancelCloneJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.CancelCloneJobCallback): void;

Calls CancelCloneJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelCloneJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icancelclonejobrequest)`   
CancelCloneJobRequest message or plain object  
`callback` |  `[CancelCloneJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelCloneJob(request)
    
    
    public cancelCloneJob(request: google.cloud.vmmigration.v1.ICancelCloneJobRequest): Promise<google.longrunning.Operation>;

Calls CancelCloneJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelCloneJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icancelclonejobrequest)`   
CancelCloneJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### cancelCutoverJob(request, callback)
    
    
    public cancelCutoverJob(request: google.cloud.vmmigration.v1.ICancelCutoverJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.CancelCutoverJobCallback): void;

Calls CancelCutoverJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelCutoverJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icancelcutoverjobrequest)`   
CancelCutoverJobRequest message or plain object  
`callback` |  `[CancelCutoverJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelCutoverJob(request)
    
    
    public cancelCutoverJob(request: google.cloud.vmmigration.v1.ICancelCutoverJobRequest): Promise<google.longrunning.Operation>;

Calls CancelCutoverJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelCutoverJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icancelcutoverjobrequest)`   
CancelCutoverJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### cancelDiskMigrationJob(request, callback)
    
    
    public cancelDiskMigrationJob(request: google.cloud.vmmigration.v1.ICancelDiskMigrationJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.CancelDiskMigrationJobCallback): void;

Calls CancelDiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icanceldiskmigrationjobrequest)`   
CancelDiskMigrationJobRequest message or plain object  
`callback` |  `[CancelDiskMigrationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelDiskMigrationJob(request)
    
    
    public cancelDiskMigrationJob(request: google.cloud.vmmigration.v1.ICancelDiskMigrationJobRequest): Promise<google.longrunning.Operation>;

Calls CancelDiskMigrationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icanceldiskmigrationjobrequest)`   
CancelDiskMigrationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### cancelImageImportJob(request, callback)
    
    
    public cancelImageImportJob(request: google.cloud.vmmigration.v1.ICancelImageImportJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.CancelImageImportJobCallback): void;

Calls CancelImageImportJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelImageImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icancelimageimportjobrequest)`   
CancelImageImportJobRequest message or plain object  
`callback` |  `[CancelImageImportJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelImageImportJob(request)
    
    
    public cancelImageImportJob(request: google.cloud.vmmigration.v1.ICancelImageImportJobRequest): Promise<google.longrunning.Operation>;

Calls CancelImageImportJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelImageImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icancelimageimportjobrequest)`   
CancelImageImportJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): VmMigration;

Creates new VmMigration service using the specified rpc implementation.

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
`[VmMigration](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.vmmigration-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCloneJob(request, callback)
    
    
    public createCloneJob(request: google.cloud.vmmigration.v1.ICreateCloneJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateCloneJobCallback): void;

Calls CreateCloneJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCloneJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreateclonejobrequest)`   
CreateCloneJobRequest message or plain object  
`callback` |  `[CreateCloneJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCloneJob(request)
    
    
    public createCloneJob(request: google.cloud.vmmigration.v1.ICreateCloneJobRequest): Promise<google.longrunning.Operation>;

Calls CreateCloneJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCloneJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreateclonejobrequest)`   
CreateCloneJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createCutoverJob(request, callback)
    
    
    public createCutoverJob(request: google.cloud.vmmigration.v1.ICreateCutoverJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateCutoverJobCallback): void;

Calls CreateCutoverJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCutoverJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatecutoverjobrequest)`   
CreateCutoverJobRequest message or plain object  
`callback` |  `[CreateCutoverJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCutoverJob(request)
    
    
    public createCutoverJob(request: google.cloud.vmmigration.v1.ICreateCutoverJobRequest): Promise<google.longrunning.Operation>;

Calls CreateCutoverJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCutoverJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatecutoverjobrequest)`   
CreateCutoverJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createDatacenterConnector(request, callback)
    
    
    public createDatacenterConnector(request: google.cloud.vmmigration.v1.ICreateDatacenterConnectorRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateDatacenterConnectorCallback): void;

Calls CreateDatacenterConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatacenterConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatedatacenterconnectorrequest)`   
CreateDatacenterConnectorRequest message or plain object  
`callback` |  `[CreateDatacenterConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDatacenterConnector(request)
    
    
    public createDatacenterConnector(request: google.cloud.vmmigration.v1.ICreateDatacenterConnectorRequest): Promise<google.longrunning.Operation>;

Calls CreateDatacenterConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatacenterConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatedatacenterconnectorrequest)`   
CreateDatacenterConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createDiskMigrationJob(request, callback)
    
    
    public createDiskMigrationJob(request: google.cloud.vmmigration.v1.ICreateDiskMigrationJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateDiskMigrationJobCallback): void;

Calls CreateDiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatediskmigrationjobrequest)`   
CreateDiskMigrationJobRequest message or plain object  
`callback` |  `[CreateDiskMigrationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDiskMigrationJob(request)
    
    
    public createDiskMigrationJob(request: google.cloud.vmmigration.v1.ICreateDiskMigrationJobRequest): Promise<google.longrunning.Operation>;

Calls CreateDiskMigrationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatediskmigrationjobrequest)`   
CreateDiskMigrationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createGroup(request, callback)
    
    
    public createGroup(request: google.cloud.vmmigration.v1.ICreateGroupRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateGroupCallback): void;

Calls CreateGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreategrouprequest)`   
CreateGroupRequest message or plain object  
`callback` |  `[CreateGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGroup(request)
    
    
    public createGroup(request: google.cloud.vmmigration.v1.ICreateGroupRequest): Promise<google.longrunning.Operation>;

Calls CreateGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreategrouprequest)`   
CreateGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createImageImport(request, callback)
    
    
    public createImageImport(request: google.cloud.vmmigration.v1.ICreateImageImportRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateImageImportCallback): void;

Calls CreateImageImport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateImageImportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreateimageimportrequest)`   
CreateImageImportRequest message or plain object  
`callback` |  `[CreateImageImportCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createImageImport(request)
    
    
    public createImageImport(request: google.cloud.vmmigration.v1.ICreateImageImportRequest): Promise<google.longrunning.Operation>;

Calls CreateImageImport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateImageImportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreateimageimportrequest)`   
CreateImageImportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createMigratingVm(request, callback)
    
    
    public createMigratingVm(request: google.cloud.vmmigration.v1.ICreateMigratingVmRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateMigratingVmCallback): void;

Calls CreateMigratingVm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatemigratingvmrequest)`   
CreateMigratingVmRequest message or plain object  
`callback` |  `[CreateMigratingVmCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMigratingVm(request)
    
    
    public createMigratingVm(request: google.cloud.vmmigration.v1.ICreateMigratingVmRequest): Promise<google.longrunning.Operation>;

Calls CreateMigratingVm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatemigratingvmrequest)`   
CreateMigratingVmRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createSource(request, callback)
    
    
    public createSource(request: google.cloud.vmmigration.v1.ICreateSourceRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateSourceCallback): void;

Calls CreateSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatesourcerequest)`   
CreateSourceRequest message or plain object  
`callback` |  `[CreateSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSource(request)
    
    
    public createSource(request: google.cloud.vmmigration.v1.ICreateSourceRequest): Promise<google.longrunning.Operation>;

Calls CreateSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatesourcerequest)`   
CreateSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createTargetProject(request, callback)
    
    
    public createTargetProject(request: google.cloud.vmmigration.v1.ICreateTargetProjectRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateTargetProjectCallback): void;

Calls CreateTargetProject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatetargetprojectrequest)`   
CreateTargetProjectRequest message or plain object  
`callback` |  `[CreateTargetProjectCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTargetProject(request)
    
    
    public createTargetProject(request: google.cloud.vmmigration.v1.ICreateTargetProjectRequest): Promise<google.longrunning.Operation>;

Calls CreateTargetProject.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreatetargetprojectrequest)`   
CreateTargetProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### createUtilizationReport(request, callback)
    
    
    public createUtilizationReport(request: google.cloud.vmmigration.v1.ICreateUtilizationReportRequest, callback: google.cloud.vmmigration.v1.VmMigration.CreateUtilizationReportCallback): void;

Calls CreateUtilizationReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUtilizationReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreateutilizationreportrequest)`   
CreateUtilizationReportRequest message or plain object  
`callback` |  `[CreateUtilizationReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUtilizationReport(request)
    
    
    public createUtilizationReport(request: google.cloud.vmmigration.v1.ICreateUtilizationReportRequest): Promise<google.longrunning.Operation>;

Calls CreateUtilizationReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateUtilizationReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.icreateutilizationreportrequest)`   
CreateUtilizationReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteDatacenterConnector(request, callback)
    
    
    public deleteDatacenterConnector(request: google.cloud.vmmigration.v1.IDeleteDatacenterConnectorRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteDatacenterConnectorCallback): void;

Calls DeleteDatacenterConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatacenterConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletedatacenterconnectorrequest)`   
DeleteDatacenterConnectorRequest message or plain object  
`callback` |  `[DeleteDatacenterConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDatacenterConnector(request)
    
    
    public deleteDatacenterConnector(request: google.cloud.vmmigration.v1.IDeleteDatacenterConnectorRequest): Promise<google.longrunning.Operation>;

Calls DeleteDatacenterConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatacenterConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletedatacenterconnectorrequest)`   
DeleteDatacenterConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteDiskMigrationJob(request, callback)
    
    
    public deleteDiskMigrationJob(request: google.cloud.vmmigration.v1.IDeleteDiskMigrationJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteDiskMigrationJobCallback): void;

Calls DeleteDiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletediskmigrationjobrequest)`   
DeleteDiskMigrationJobRequest message or plain object  
`callback` |  `[DeleteDiskMigrationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDiskMigrationJob(request)
    
    
    public deleteDiskMigrationJob(request: google.cloud.vmmigration.v1.IDeleteDiskMigrationJobRequest): Promise<google.longrunning.Operation>;

Calls DeleteDiskMigrationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletediskmigrationjobrequest)`   
DeleteDiskMigrationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteGroup(request, callback)
    
    
    public deleteGroup(request: google.cloud.vmmigration.v1.IDeleteGroupRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteGroupCallback): void;

Calls DeleteGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletegrouprequest)`   
DeleteGroupRequest message or plain object  
`callback` |  `[DeleteGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGroup(request)
    
    
    public deleteGroup(request: google.cloud.vmmigration.v1.IDeleteGroupRequest): Promise<google.longrunning.Operation>;

Calls DeleteGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletegrouprequest)`   
DeleteGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteImageImport(request, callback)
    
    
    public deleteImageImport(request: google.cloud.vmmigration.v1.IDeleteImageImportRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteImageImportCallback): void;

Calls DeleteImageImport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteImageImportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideleteimageimportrequest)`   
DeleteImageImportRequest message or plain object  
`callback` |  `[DeleteImageImportCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteImageImport(request)
    
    
    public deleteImageImport(request: google.cloud.vmmigration.v1.IDeleteImageImportRequest): Promise<google.longrunning.Operation>;

Calls DeleteImageImport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteImageImportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideleteimageimportrequest)`   
DeleteImageImportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteMigratingVm(request, callback)
    
    
    public deleteMigratingVm(request: google.cloud.vmmigration.v1.IDeleteMigratingVmRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteMigratingVmCallback): void;

Calls DeleteMigratingVm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletemigratingvmrequest)`   
DeleteMigratingVmRequest message or plain object  
`callback` |  `[DeleteMigratingVmCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMigratingVm(request)
    
    
    public deleteMigratingVm(request: google.cloud.vmmigration.v1.IDeleteMigratingVmRequest): Promise<google.longrunning.Operation>;

Calls DeleteMigratingVm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletemigratingvmrequest)`   
DeleteMigratingVmRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteSource(request, callback)
    
    
    public deleteSource(request: google.cloud.vmmigration.v1.IDeleteSourceRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteSourceCallback): void;

Calls DeleteSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletesourcerequest)`   
DeleteSourceRequest message or plain object  
`callback` |  `[DeleteSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSource(request)
    
    
    public deleteSource(request: google.cloud.vmmigration.v1.IDeleteSourceRequest): Promise<google.longrunning.Operation>;

Calls DeleteSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletesourcerequest)`   
DeleteSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteTargetProject(request, callback)
    
    
    public deleteTargetProject(request: google.cloud.vmmigration.v1.IDeleteTargetProjectRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteTargetProjectCallback): void;

Calls DeleteTargetProject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletetargetprojectrequest)`   
DeleteTargetProjectRequest message or plain object  
`callback` |  `[DeleteTargetProjectCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTargetProject(request)
    
    
    public deleteTargetProject(request: google.cloud.vmmigration.v1.IDeleteTargetProjectRequest): Promise<google.longrunning.Operation>;

Calls DeleteTargetProject.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideletetargetprojectrequest)`   
DeleteTargetProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### deleteUtilizationReport(request, callback)
    
    
    public deleteUtilizationReport(request: google.cloud.vmmigration.v1.IDeleteUtilizationReportRequest, callback: google.cloud.vmmigration.v1.VmMigration.DeleteUtilizationReportCallback): void;

Calls DeleteUtilizationReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUtilizationReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideleteutilizationreportrequest)`   
DeleteUtilizationReportRequest message or plain object  
`callback` |  `[DeleteUtilizationReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUtilizationReport(request)
    
    
    public deleteUtilizationReport(request: google.cloud.vmmigration.v1.IDeleteUtilizationReportRequest): Promise<google.longrunning.Operation>;

Calls DeleteUtilizationReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUtilizationReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ideleteutilizationreportrequest)`   
DeleteUtilizationReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### extendMigration(request, callback)
    
    
    public extendMigration(request: google.cloud.vmmigration.v1.IExtendMigrationRequest, callback: google.cloud.vmmigration.v1.VmMigration.ExtendMigrationCallback): void;

Calls ExtendMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExtendMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iextendmigrationrequest)`   
ExtendMigrationRequest message or plain object  
`callback` |  `[ExtendMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### extendMigration(request)
    
    
    public extendMigration(request: google.cloud.vmmigration.v1.IExtendMigrationRequest): Promise<google.longrunning.Operation>;

Calls ExtendMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExtendMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iextendmigrationrequest)`   
ExtendMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### fetchInventory(request, callback)
    
    
    public fetchInventory(request: google.cloud.vmmigration.v1.IFetchInventoryRequest, callback: google.cloud.vmmigration.v1.VmMigration.FetchInventoryCallback): void;

Calls FetchInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ifetchinventoryrequest)`   
FetchInventoryRequest message or plain object  
`callback` |  `[FetchInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchInventoryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchInventory(request)
    
    
    public fetchInventory(request: google.cloud.vmmigration.v1.IFetchInventoryRequest): Promise<google.cloud.vmmigration.v1.FetchInventoryResponse>;

Calls FetchInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ifetchinventoryrequest)`   
FetchInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.FetchInventoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.fetchinventoryresponse)>` | Promise  
  
### fetchStorageInventory(request, callback)
    
    
    public fetchStorageInventory(request: google.cloud.vmmigration.v1.IFetchStorageInventoryRequest, callback: google.cloud.vmmigration.v1.VmMigration.FetchStorageInventoryCallback): void;

Calls FetchStorageInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchStorageInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ifetchstorageinventoryrequest)`   
FetchStorageInventoryRequest message or plain object  
`callback` |  `[FetchStorageInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchStorageInventoryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchStorageInventory(request)
    
    
    public fetchStorageInventory(request: google.cloud.vmmigration.v1.IFetchStorageInventoryRequest): Promise<google.cloud.vmmigration.v1.FetchStorageInventoryResponse>;

Calls FetchStorageInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchStorageInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ifetchstorageinventoryrequest)`   
FetchStorageInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.FetchStorageInventoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.fetchstorageinventoryresponse)>` | Promise  
  
### finalizeMigration(request, callback)
    
    
    public finalizeMigration(request: google.cloud.vmmigration.v1.IFinalizeMigrationRequest, callback: google.cloud.vmmigration.v1.VmMigration.FinalizeMigrationCallback): void;

Calls FinalizeMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFinalizeMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ifinalizemigrationrequest)`   
FinalizeMigrationRequest message or plain object  
`callback` |  `[FinalizeMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### finalizeMigration(request)
    
    
    public finalizeMigration(request: google.cloud.vmmigration.v1.IFinalizeMigrationRequest): Promise<google.longrunning.Operation>;

Calls FinalizeMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFinalizeMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ifinalizemigrationrequest)`   
FinalizeMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### getCloneJob(request, callback)
    
    
    public getCloneJob(request: google.cloud.vmmigration.v1.IGetCloneJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetCloneJobCallback): void;

Calls GetCloneJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCloneJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetclonejobrequest)`   
GetCloneJobRequest message or plain object  
`callback` |  `[GetCloneJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and CloneJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCloneJob(request)
    
    
    public getCloneJob(request: google.cloud.vmmigration.v1.IGetCloneJobRequest): Promise<google.cloud.vmmigration.v1.CloneJob>;

Calls GetCloneJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCloneJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetclonejobrequest)`   
GetCloneJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.CloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class)>` | Promise  
  
### getCutoverJob(request, callback)
    
    
    public getCutoverJob(request: google.cloud.vmmigration.v1.IGetCutoverJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetCutoverJobCallback): void;

Calls GetCutoverJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCutoverJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetcutoverjobrequest)`   
GetCutoverJobRequest message or plain object  
`callback` |  `[GetCutoverJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and CutoverJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCutoverJob(request)
    
    
    public getCutoverJob(request: google.cloud.vmmigration.v1.IGetCutoverJobRequest): Promise<google.cloud.vmmigration.v1.CutoverJob>;

Calls GetCutoverJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCutoverJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetcutoverjobrequest)`   
GetCutoverJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.CutoverJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.cutoverjob-class)>` | Promise  
  
### getDatacenterConnector(request, callback)
    
    
    public getDatacenterConnector(request: google.cloud.vmmigration.v1.IGetDatacenterConnectorRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetDatacenterConnectorCallback): void;

Calls GetDatacenterConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatacenterConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetdatacenterconnectorrequest)`   
GetDatacenterConnectorRequest message or plain object  
`callback` |  `[GetDatacenterConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and DatacenterConnector  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDatacenterConnector(request)
    
    
    public getDatacenterConnector(request: google.cloud.vmmigration.v1.IGetDatacenterConnectorRequest): Promise<google.cloud.vmmigration.v1.DatacenterConnector>;

Calls GetDatacenterConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatacenterConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetdatacenterconnectorrequest)`   
GetDatacenterConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.DatacenterConnector](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.datacenterconnector-class)>` | Promise  
  
### getDiskMigrationJob(request, callback)
    
    
    public getDiskMigrationJob(request: google.cloud.vmmigration.v1.IGetDiskMigrationJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetDiskMigrationJobCallback): void;

Calls GetDiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetdiskmigrationjobrequest)`   
GetDiskMigrationJobRequest message or plain object  
`callback` |  `[GetDiskMigrationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and DiskMigrationJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDiskMigrationJob(request)
    
    
    public getDiskMigrationJob(request: google.cloud.vmmigration.v1.IGetDiskMigrationJobRequest): Promise<google.cloud.vmmigration.v1.DiskMigrationJob>;

Calls GetDiskMigrationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetdiskmigrationjobrequest)`   
GetDiskMigrationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.DiskMigrationJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.diskmigrationjob-class)>` | Promise  
  
### getGroup(request, callback)
    
    
    public getGroup(request: google.cloud.vmmigration.v1.IGetGroupRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetGroupCallback): void;

Calls GetGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetgrouprequest)`   
GetGroupRequest message or plain object  
`callback` |  `[GetGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Group  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGroup(request)
    
    
    public getGroup(request: google.cloud.vmmigration.v1.IGetGroupRequest): Promise<google.cloud.vmmigration.v1.Group>;

Calls GetGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetgrouprequest)`   
GetGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.Group](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.group-class)>` | Promise  
  
### getImageImport(request, callback)
    
    
    public getImageImport(request: google.cloud.vmmigration.v1.IGetImageImportRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetImageImportCallback): void;

Calls GetImageImport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetImageImportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetimageimportrequest)`   
GetImageImportRequest message or plain object  
`callback` |  `[GetImageImportCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ImageImport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getImageImport(request)
    
    
    public getImageImport(request: google.cloud.vmmigration.v1.IGetImageImportRequest): Promise<google.cloud.vmmigration.v1.ImageImport>;

Calls GetImageImport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetImageImportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetimageimportrequest)`   
GetImageImportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ImageImport](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimport)>` | Promise  
  
### getImageImportJob(request, callback)
    
    
    public getImageImportJob(request: google.cloud.vmmigration.v1.IGetImageImportJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetImageImportJobCallback): void;

Calls GetImageImportJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetImageImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetimageimportjobrequest)`   
GetImageImportJobRequest message or plain object  
`callback` |  `[GetImageImportJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ImageImportJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getImageImportJob(request)
    
    
    public getImageImportJob(request: google.cloud.vmmigration.v1.IGetImageImportJobRequest): Promise<google.cloud.vmmigration.v1.ImageImportJob>;

Calls GetImageImportJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetImageImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetimageimportjobrequest)`   
GetImageImportJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class)>` | Promise  
  
### getMigratingVm(request, callback)
    
    
    public getMigratingVm(request: google.cloud.vmmigration.v1.IGetMigratingVmRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetMigratingVmCallback): void;

Calls GetMigratingVm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetmigratingvmrequest)`   
GetMigratingVmRequest message or plain object  
`callback` |  `[GetMigratingVmCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and MigratingVm  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMigratingVm(request)
    
    
    public getMigratingVm(request: google.cloud.vmmigration.v1.IGetMigratingVmRequest): Promise<google.cloud.vmmigration.v1.MigratingVm>;

Calls GetMigratingVm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetmigratingvmrequest)`   
GetMigratingVmRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.MigratingVm](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migratingvm-class)>` | Promise  
  
### getReplicationCycle(request, callback)
    
    
    public getReplicationCycle(request: google.cloud.vmmigration.v1.IGetReplicationCycleRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetReplicationCycleCallback): void;

Calls GetReplicationCycle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReplicationCycleRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetreplicationcyclerequest)`   
GetReplicationCycleRequest message or plain object  
`callback` |  `[GetReplicationCycleCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ReplicationCycle  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReplicationCycle(request)
    
    
    public getReplicationCycle(request: google.cloud.vmmigration.v1.IGetReplicationCycleRequest): Promise<google.cloud.vmmigration.v1.ReplicationCycle>;

Calls GetReplicationCycle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReplicationCycleRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetreplicationcyclerequest)`   
GetReplicationCycleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ReplicationCycle](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.replicationcycle-class)>` | Promise  
  
### getSource(request, callback)
    
    
    public getSource(request: google.cloud.vmmigration.v1.IGetSourceRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetSourceCallback): void;

Calls GetSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetsourcerequest)`   
GetSourceRequest message or plain object  
`callback` |  `[GetSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Source  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSource(request)
    
    
    public getSource(request: google.cloud.vmmigration.v1.IGetSourceRequest): Promise<google.cloud.vmmigration.v1.Source>;

Calls GetSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetsourcerequest)`   
GetSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.Source](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.source)>` | Promise  
  
### getTargetProject(request, callback)
    
    
    public getTargetProject(request: google.cloud.vmmigration.v1.IGetTargetProjectRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetTargetProjectCallback): void;

Calls GetTargetProject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igettargetprojectrequest)`   
GetTargetProjectRequest message or plain object  
`callback` |  `[GetTargetProjectCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and TargetProject  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTargetProject(request)
    
    
    public getTargetProject(request: google.cloud.vmmigration.v1.IGetTargetProjectRequest): Promise<google.cloud.vmmigration.v1.TargetProject>;

Calls GetTargetProject.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igettargetprojectrequest)`   
GetTargetProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.TargetProject](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.targetproject)>` | Promise  
  
### getUtilizationReport(request, callback)
    
    
    public getUtilizationReport(request: google.cloud.vmmigration.v1.IGetUtilizationReportRequest, callback: google.cloud.vmmigration.v1.VmMigration.GetUtilizationReportCallback): void;

Calls GetUtilizationReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUtilizationReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetutilizationreportrequest)`   
GetUtilizationReportRequest message or plain object  
`callback` |  `[GetUtilizationReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and UtilizationReport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUtilizationReport(request)
    
    
    public getUtilizationReport(request: google.cloud.vmmigration.v1.IGetUtilizationReportRequest): Promise<google.cloud.vmmigration.v1.UtilizationReport>;

Calls GetUtilizationReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUtilizationReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.igetutilizationreportrequest)`   
GetUtilizationReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.UtilizationReport](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.utilizationreport-class)>` | Promise  
  
### listCloneJobs(request, callback)
    
    
    public listCloneJobs(request: google.cloud.vmmigration.v1.IListCloneJobsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListCloneJobsCallback): void;

Calls ListCloneJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCloneJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistclonejobsrequest)`   
ListCloneJobsRequest message or plain object  
`callback` |  `[ListCloneJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCloneJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCloneJobs(request)
    
    
    public listCloneJobs(request: google.cloud.vmmigration.v1.IListCloneJobsRequest): Promise<google.cloud.vmmigration.v1.ListCloneJobsResponse>;

Calls ListCloneJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCloneJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistclonejobsrequest)`   
ListCloneJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListCloneJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listclonejobsresponse)>` | Promise  
  
### listCutoverJobs(request, callback)
    
    
    public listCutoverJobs(request: google.cloud.vmmigration.v1.IListCutoverJobsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListCutoverJobsCallback): void;

Calls ListCutoverJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCutoverJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistcutoverjobsrequest)`   
ListCutoverJobsRequest message or plain object  
`callback` |  `[ListCutoverJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCutoverJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCutoverJobs(request)
    
    
    public listCutoverJobs(request: google.cloud.vmmigration.v1.IListCutoverJobsRequest): Promise<google.cloud.vmmigration.v1.ListCutoverJobsResponse>;

Calls ListCutoverJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCutoverJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistcutoverjobsrequest)`   
ListCutoverJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListCutoverJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listcutoverjobsresponse)>` | Promise  
  
### listDatacenterConnectors(request, callback)
    
    
    public listDatacenterConnectors(request: google.cloud.vmmigration.v1.IListDatacenterConnectorsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListDatacenterConnectorsCallback): void;

Calls ListDatacenterConnectors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatacenterConnectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistdatacenterconnectorsrequest)`   
ListDatacenterConnectorsRequest message or plain object  
`callback` |  `[ListDatacenterConnectorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatacenterConnectorsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatacenterConnectors(request)
    
    
    public listDatacenterConnectors(request: google.cloud.vmmigration.v1.IListDatacenterConnectorsRequest): Promise<google.cloud.vmmigration.v1.ListDatacenterConnectorsResponse>;

Calls ListDatacenterConnectors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatacenterConnectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistdatacenterconnectorsrequest)`   
ListDatacenterConnectorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListDatacenterConnectorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listdatacenterconnectorsresponse)>` | Promise  
  
### listDiskMigrationJobs(request, callback)
    
    
    public listDiskMigrationJobs(request: google.cloud.vmmigration.v1.IListDiskMigrationJobsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListDiskMigrationJobsCallback): void;

Calls ListDiskMigrationJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDiskMigrationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistdiskmigrationjobsrequest)`   
ListDiskMigrationJobsRequest message or plain object  
`callback` |  `[ListDiskMigrationJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDiskMigrationJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDiskMigrationJobs(request)
    
    
    public listDiskMigrationJobs(request: google.cloud.vmmigration.v1.IListDiskMigrationJobsRequest): Promise<google.cloud.vmmigration.v1.ListDiskMigrationJobsResponse>;

Calls ListDiskMigrationJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDiskMigrationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistdiskmigrationjobsrequest)`   
ListDiskMigrationJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListDiskMigrationJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listdiskmigrationjobsresponse)>` | Promise  
  
### listGroups(request, callback)
    
    
    public listGroups(request: google.cloud.vmmigration.v1.IListGroupsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListGroupsCallback): void;

Calls ListGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistgroupsrequest)`   
ListGroupsRequest message or plain object  
`callback` |  `[ListGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGroups(request)
    
    
    public listGroups(request: google.cloud.vmmigration.v1.IListGroupsRequest): Promise<google.cloud.vmmigration.v1.ListGroupsResponse>;

Calls ListGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistgroupsrequest)`   
ListGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listgroupsresponse)>` | Promise  
  
### listImageImportJobs(request, callback)
    
    
    public listImageImportJobs(request: google.cloud.vmmigration.v1.IListImageImportJobsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListImageImportJobsCallback): void;

Calls ListImageImportJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListImageImportJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistimageimportjobsrequest)`   
ListImageImportJobsRequest message or plain object  
`callback` |  `[ListImageImportJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListImageImportJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listImageImportJobs(request)
    
    
    public listImageImportJobs(request: google.cloud.vmmigration.v1.IListImageImportJobsRequest): Promise<google.cloud.vmmigration.v1.ListImageImportJobsResponse>;

Calls ListImageImportJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListImageImportJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistimageimportjobsrequest)`   
ListImageImportJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListImageImportJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listimageimportjobsresponse)>` | Promise  
  
### listImageImports(request, callback)
    
    
    public listImageImports(request: google.cloud.vmmigration.v1.IListImageImportsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListImageImportsCallback): void;

Calls ListImageImports.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListImageImportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistimageimportsrequest)`   
ListImageImportsRequest message or plain object  
`callback` |  `[ListImageImportsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListImageImportsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listImageImports(request)
    
    
    public listImageImports(request: google.cloud.vmmigration.v1.IListImageImportsRequest): Promise<google.cloud.vmmigration.v1.ListImageImportsResponse>;

Calls ListImageImports.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListImageImportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistimageimportsrequest)`   
ListImageImportsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListImageImportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listimageimportsresponse)>` | Promise  
  
### listMigratingVms(request, callback)
    
    
    public listMigratingVms(request: google.cloud.vmmigration.v1.IListMigratingVmsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListMigratingVmsCallback): void;

Calls ListMigratingVms.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigratingVmsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistmigratingvmsrequest)`   
ListMigratingVmsRequest message or plain object  
`callback` |  `[ListMigratingVmsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMigratingVmsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMigratingVms(request)
    
    
    public listMigratingVms(request: google.cloud.vmmigration.v1.IListMigratingVmsRequest): Promise<google.cloud.vmmigration.v1.ListMigratingVmsResponse>;

Calls ListMigratingVms.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMigratingVmsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistmigratingvmsrequest)`   
ListMigratingVmsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListMigratingVmsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listmigratingvmsresponse)>` | Promise  
  
### listReplicationCycles(request, callback)
    
    
    public listReplicationCycles(request: google.cloud.vmmigration.v1.IListReplicationCyclesRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListReplicationCyclesCallback): void;

Calls ListReplicationCycles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReplicationCyclesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistreplicationcyclesrequest)`   
ListReplicationCyclesRequest message or plain object  
`callback` |  `[ListReplicationCyclesCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReplicationCyclesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReplicationCycles(request)
    
    
    public listReplicationCycles(request: google.cloud.vmmigration.v1.IListReplicationCyclesRequest): Promise<google.cloud.vmmigration.v1.ListReplicationCyclesResponse>;

Calls ListReplicationCycles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReplicationCyclesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistreplicationcyclesrequest)`   
ListReplicationCyclesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListReplicationCyclesResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listreplicationcyclesresponse)>` | Promise  
  
### listSources(request, callback)
    
    
    public listSources(request: google.cloud.vmmigration.v1.IListSourcesRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListSourcesCallback): void;

Calls ListSources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistsourcesrequest)`   
ListSourcesRequest message or plain object  
`callback` |  `[ListSourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSources(request)
    
    
    public listSources(request: google.cloud.vmmigration.v1.IListSourcesRequest): Promise<google.cloud.vmmigration.v1.ListSourcesResponse>;

Calls ListSources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistsourcesrequest)`   
ListSourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listsourcesresponse)>` | Promise  
  
### listTargetProjects(request, callback)
    
    
    public listTargetProjects(request: google.cloud.vmmigration.v1.IListTargetProjectsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListTargetProjectsCallback): void;

Calls ListTargetProjects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetProjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilisttargetprojectsrequest)`   
ListTargetProjectsRequest message or plain object  
`callback` |  `[ListTargetProjectsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTargetProjectsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTargetProjects(request)
    
    
    public listTargetProjects(request: google.cloud.vmmigration.v1.IListTargetProjectsRequest): Promise<google.cloud.vmmigration.v1.ListTargetProjectsResponse>;

Calls ListTargetProjects.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTargetProjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilisttargetprojectsrequest)`   
ListTargetProjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListTargetProjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listtargetprojectsresponse)>` | Promise  
  
### listUtilizationReports(request, callback)
    
    
    public listUtilizationReports(request: google.cloud.vmmigration.v1.IListUtilizationReportsRequest, callback: google.cloud.vmmigration.v1.VmMigration.ListUtilizationReportsCallback): void;

Calls ListUtilizationReports.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUtilizationReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistutilizationreportsrequest)`   
ListUtilizationReportsRequest message or plain object  
`callback` |  `[ListUtilizationReportsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUtilizationReportsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUtilizationReports(request)
    
    
    public listUtilizationReports(request: google.cloud.vmmigration.v1.IListUtilizationReportsRequest): Promise<google.cloud.vmmigration.v1.ListUtilizationReportsResponse>;

Calls ListUtilizationReports.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUtilizationReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ilistutilizationreportsrequest)`   
ListUtilizationReportsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vmmigration.v1.ListUtilizationReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.listutilizationreportsresponse)>` | Promise  
  
### pauseMigration(request, callback)
    
    
    public pauseMigration(request: google.cloud.vmmigration.v1.IPauseMigrationRequest, callback: google.cloud.vmmigration.v1.VmMigration.PauseMigrationCallback): void;

Calls PauseMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ipausemigrationrequest)`   
PauseMigrationRequest message or plain object  
`callback` |  `[PauseMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pauseMigration(request)
    
    
    public pauseMigration(request: google.cloud.vmmigration.v1.IPauseMigrationRequest): Promise<google.longrunning.Operation>;

Calls PauseMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPauseMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.ipausemigrationrequest)`   
PauseMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### removeGroupMigration(request, callback)
    
    
    public removeGroupMigration(request: google.cloud.vmmigration.v1.IRemoveGroupMigrationRequest, callback: google.cloud.vmmigration.v1.VmMigration.RemoveGroupMigrationCallback): void;

Calls RemoveGroupMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveGroupMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iremovegroupmigrationrequest)`   
RemoveGroupMigrationRequest message or plain object  
`callback` |  `[RemoveGroupMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeGroupMigration(request)
    
    
    public removeGroupMigration(request: google.cloud.vmmigration.v1.IRemoveGroupMigrationRequest): Promise<google.longrunning.Operation>;

Calls RemoveGroupMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveGroupMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iremovegroupmigrationrequest)`   
RemoveGroupMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### resumeMigration(request, callback)
    
    
    public resumeMigration(request: google.cloud.vmmigration.v1.IResumeMigrationRequest, callback: google.cloud.vmmigration.v1.VmMigration.ResumeMigrationCallback): void;

Calls ResumeMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iresumemigrationrequest)`   
ResumeMigrationRequest message or plain object  
`callback` |  `[ResumeMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeMigration(request)
    
    
    public resumeMigration(request: google.cloud.vmmigration.v1.IResumeMigrationRequest): Promise<google.longrunning.Operation>;

Calls ResumeMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumeMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iresumemigrationrequest)`   
ResumeMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### runDiskMigrationJob(request, callback)
    
    
    public runDiskMigrationJob(request: google.cloud.vmmigration.v1.IRunDiskMigrationJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.RunDiskMigrationJobCallback): void;

Calls RunDiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.irundiskmigrationjobrequest)`   
RunDiskMigrationJobRequest message or plain object  
`callback` |  `[RunDiskMigrationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runDiskMigrationJob(request)
    
    
    public runDiskMigrationJob(request: google.cloud.vmmigration.v1.IRunDiskMigrationJobRequest): Promise<google.longrunning.Operation>;

Calls RunDiskMigrationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.irundiskmigrationjobrequest)`   
RunDiskMigrationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### startMigration(request, callback)
    
    
    public startMigration(request: google.cloud.vmmigration.v1.IStartMigrationRequest, callback: google.cloud.vmmigration.v1.VmMigration.StartMigrationCallback): void;

Calls StartMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.istartmigrationrequest)`   
StartMigrationRequest message or plain object  
`callback` |  `[StartMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startMigration(request)
    
    
    public startMigration(request: google.cloud.vmmigration.v1.IStartMigrationRequest): Promise<google.longrunning.Operation>;

Calls StartMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.istartmigrationrequest)`   
StartMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### updateDiskMigrationJob(request, callback)
    
    
    public updateDiskMigrationJob(request: google.cloud.vmmigration.v1.IUpdateDiskMigrationJobRequest, callback: google.cloud.vmmigration.v1.VmMigration.UpdateDiskMigrationJobCallback): void;

Calls UpdateDiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatediskmigrationjobrequest)`   
UpdateDiskMigrationJobRequest message or plain object  
`callback` |  `[UpdateDiskMigrationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDiskMigrationJob(request)
    
    
    public updateDiskMigrationJob(request: google.cloud.vmmigration.v1.IUpdateDiskMigrationJobRequest): Promise<google.longrunning.Operation>;

Calls UpdateDiskMigrationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDiskMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatediskmigrationjobrequest)`   
UpdateDiskMigrationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### updateGroup(request, callback)
    
    
    public updateGroup(request: google.cloud.vmmigration.v1.IUpdateGroupRequest, callback: google.cloud.vmmigration.v1.VmMigration.UpdateGroupCallback): void;

Calls UpdateGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdategrouprequest)`   
UpdateGroupRequest message or plain object  
`callback` |  `[UpdateGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGroup(request)
    
    
    public updateGroup(request: google.cloud.vmmigration.v1.IUpdateGroupRequest): Promise<google.longrunning.Operation>;

Calls UpdateGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdategrouprequest)`   
UpdateGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### updateMigratingVm(request, callback)
    
    
    public updateMigratingVm(request: google.cloud.vmmigration.v1.IUpdateMigratingVmRequest, callback: google.cloud.vmmigration.v1.VmMigration.UpdateMigratingVmCallback): void;

Calls UpdateMigratingVm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatemigratingvmrequest)`   
UpdateMigratingVmRequest message or plain object  
`callback` |  `[UpdateMigratingVmCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMigratingVm(request)
    
    
    public updateMigratingVm(request: google.cloud.vmmigration.v1.IUpdateMigratingVmRequest): Promise<google.longrunning.Operation>;

Calls UpdateMigratingVm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMigratingVmRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatemigratingvmrequest)`   
UpdateMigratingVmRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### updateSource(request, callback)
    
    
    public updateSource(request: google.cloud.vmmigration.v1.IUpdateSourceRequest, callback: google.cloud.vmmigration.v1.VmMigration.UpdateSourceCallback): void;

Calls UpdateSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatesourcerequest)`   
UpdateSourceRequest message or plain object  
`callback` |  `[UpdateSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSource(request)
    
    
    public updateSource(request: google.cloud.vmmigration.v1.IUpdateSourceRequest): Promise<google.longrunning.Operation>;

Calls UpdateSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatesourcerequest)`   
UpdateSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### updateTargetProject(request, callback)
    
    
    public updateTargetProject(request: google.cloud.vmmigration.v1.IUpdateTargetProjectRequest, callback: google.cloud.vmmigration.v1.VmMigration.UpdateTargetProjectCallback): void;

Calls UpdateTargetProject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatetargetprojectrequest)`   
UpdateTargetProjectRequest message or plain object  
`callback` |  `[UpdateTargetProjectCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTargetProject(request)
    
    
    public updateTargetProject(request: google.cloud.vmmigration.v1.IUpdateTargetProjectRequest): Promise<google.longrunning.Operation>;

Calls UpdateTargetProject.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTargetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupdatetargetprojectrequest)`   
UpdateTargetProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
### upgradeAppliance(request, callback)
    
    
    public upgradeAppliance(request: google.cloud.vmmigration.v1.IUpgradeApplianceRequest, callback: google.cloud.vmmigration.v1.VmMigration.UpgradeApplianceCallback): void;

Calls UpgradeAppliance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpgradeApplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupgradeappliancerequest)`   
UpgradeApplianceRequest message or plain object  
`callback` |  `[UpgradeApplianceCallback](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### upgradeAppliance(request)
    
    
    public upgradeAppliance(request: google.cloud.vmmigration.v1.IUpgradeApplianceRequest): Promise<google.longrunning.Operation>;

Calls UpgradeAppliance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpgradeApplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iupgradeappliancerequest)`   
UpgradeApplianceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
