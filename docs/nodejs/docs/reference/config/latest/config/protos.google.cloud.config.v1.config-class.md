---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.config-class
title: Class protos.google.cloud.config.v1.Config (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:50.961714+00:00
---

# Class protos.google.cloud.config.v1.Config (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.config-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.config.v1.Config (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Represents a Config

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.config.v1.Config

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Config service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Config;

Creates new Config service using the specified rpc implementation.

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
`[Config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.config-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDeployment(request, callback)
    
    
    public createDeployment(request: google.cloud.config.v1.ICreateDeploymentRequest, callback: google.cloud.config.v1.Config.CreateDeploymentCallback): void;

Calls CreateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.icreatedeploymentrequest)`   
CreateDeploymentRequest message or plain object  
`callback` |  `[CreateDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDeployment(request)
    
    
    public createDeployment(request: google.cloud.config.v1.ICreateDeploymentRequest): Promise<google.longrunning.Operation>;

Calls CreateDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.icreatedeploymentrequest)`   
CreateDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### createDeploymentGroup(request, callback)
    
    
    public createDeploymentGroup(request: google.cloud.config.v1.ICreateDeploymentGroupRequest, callback: google.cloud.config.v1.Config.CreateDeploymentGroupCallback): void;

Calls CreateDeploymentGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.icreatedeploymentgrouprequest)`   
CreateDeploymentGroupRequest message or plain object  
`callback` |  `[CreateDeploymentGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDeploymentGroup(request)
    
    
    public createDeploymentGroup(request: google.cloud.config.v1.ICreateDeploymentGroupRequest): Promise<google.longrunning.Operation>;

Calls CreateDeploymentGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.icreatedeploymentgrouprequest)`   
CreateDeploymentGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### createPreview(request, callback)
    
    
    public createPreview(request: google.cloud.config.v1.ICreatePreviewRequest, callback: google.cloud.config.v1.Config.CreatePreviewCallback): void;

Calls CreatePreview.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePreviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.icreatepreviewrequest)`   
CreatePreviewRequest message or plain object  
`callback` |  `[CreatePreviewCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPreview(request)
    
    
    public createPreview(request: google.cloud.config.v1.ICreatePreviewRequest): Promise<google.longrunning.Operation>;

Calls CreatePreview.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePreviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.icreatepreviewrequest)`   
CreatePreviewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### deleteDeployment(request, callback)
    
    
    public deleteDeployment(request: google.cloud.config.v1.IDeleteDeploymentRequest, callback: google.cloud.config.v1.Config.DeleteDeploymentCallback): void;

Calls DeleteDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletedeploymentrequest)`   
DeleteDeploymentRequest message or plain object  
`callback` |  `[DeleteDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDeployment(request)
    
    
    public deleteDeployment(request: google.cloud.config.v1.IDeleteDeploymentRequest): Promise<google.longrunning.Operation>;

Calls DeleteDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletedeploymentrequest)`   
DeleteDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### deleteDeploymentGroup(request, callback)
    
    
    public deleteDeploymentGroup(request: google.cloud.config.v1.IDeleteDeploymentGroupRequest, callback: google.cloud.config.v1.Config.DeleteDeploymentGroupCallback): void;

Calls DeleteDeploymentGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletedeploymentgrouprequest)`   
DeleteDeploymentGroupRequest message or plain object  
`callback` |  `[DeleteDeploymentGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDeploymentGroup(request)
    
    
    public deleteDeploymentGroup(request: google.cloud.config.v1.IDeleteDeploymentGroupRequest): Promise<google.longrunning.Operation>;

Calls DeleteDeploymentGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletedeploymentgrouprequest)`   
DeleteDeploymentGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### deletePreview(request, callback)
    
    
    public deletePreview(request: google.cloud.config.v1.IDeletePreviewRequest, callback: google.cloud.config.v1.Config.DeletePreviewCallback): void;

Calls DeletePreview.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePreviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletepreviewrequest)`   
DeletePreviewRequest message or plain object  
`callback` |  `[DeletePreviewCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePreview(request)
    
    
    public deletePreview(request: google.cloud.config.v1.IDeletePreviewRequest): Promise<google.longrunning.Operation>;

Calls DeletePreview.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePreviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletepreviewrequest)`   
DeletePreviewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### deleteStatefile(request, callback)
    
    
    public deleteStatefile(request: google.cloud.config.v1.IDeleteStatefileRequest, callback: google.cloud.config.v1.Config.DeleteStatefileCallback): void;

Calls DeleteStatefile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletestatefilerequest)`   
DeleteStatefileRequest message or plain object  
`callback` |  `[DeleteStatefileCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteStatefile(request)
    
    
    public deleteStatefile(request: google.cloud.config.v1.IDeleteStatefileRequest): Promise<google.protobuf.Empty>;

Calls DeleteStatefile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideletestatefilerequest)`   
DeleteStatefileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.empty)>` | Promise  
  
### deprovisionDeploymentGroup(request, callback)
    
    
    public deprovisionDeploymentGroup(request: google.cloud.config.v1.IDeprovisionDeploymentGroupRequest, callback: google.cloud.config.v1.Config.DeprovisionDeploymentGroupCallback): void;

Calls DeprovisionDeploymentGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideprovisiondeploymentgrouprequest)`   
DeprovisionDeploymentGroupRequest message or plain object  
`callback` |  `[DeprovisionDeploymentGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deprovisionDeploymentGroup(request)
    
    
    public deprovisionDeploymentGroup(request: google.cloud.config.v1.IDeprovisionDeploymentGroupRequest): Promise<google.longrunning.Operation>;

Calls DeprovisionDeploymentGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideprovisiondeploymentgrouprequest)`   
DeprovisionDeploymentGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### exportDeploymentStatefile(request, callback)
    
    
    public exportDeploymentStatefile(request: google.cloud.config.v1.IExportDeploymentStatefileRequest, callback: google.cloud.config.v1.Config.ExportDeploymentStatefileCallback): void;

Calls ExportDeploymentStatefile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDeploymentStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportdeploymentstatefilerequest)`   
ExportDeploymentStatefileRequest message or plain object  
`callback` |  `[ExportDeploymentStatefileCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Statefile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportDeploymentStatefile(request)
    
    
    public exportDeploymentStatefile(request: google.cloud.config.v1.IExportDeploymentStatefileRequest): Promise<google.cloud.config.v1.Statefile>;

Calls ExportDeploymentStatefile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportDeploymentStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportdeploymentstatefilerequest)`   
ExportDeploymentStatefileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.Statefile](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.statefile)>` | Promise  
  
### exportLockInfo(request, callback)
    
    
    public exportLockInfo(request: google.cloud.config.v1.IExportLockInfoRequest, callback: google.cloud.config.v1.Config.ExportLockInfoCallback): void;

Calls ExportLockInfo.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportLockInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportlockinforequest)`   
ExportLockInfoRequest message or plain object  
`callback` |  `[ExportLockInfoCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and LockInfo  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportLockInfo(request)
    
    
    public exportLockInfo(request: google.cloud.config.v1.IExportLockInfoRequest): Promise<google.cloud.config.v1.LockInfo>;

Calls ExportLockInfo.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportLockInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportlockinforequest)`   
ExportLockInfoRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.LockInfo](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.lockinfo)>` | Promise  
  
### exportPreviewResult(request, callback)
    
    
    public exportPreviewResult(request: google.cloud.config.v1.IExportPreviewResultRequest, callback: google.cloud.config.v1.Config.ExportPreviewResultCallback): void;

Calls ExportPreviewResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportPreviewResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportpreviewresultrequest)`   
ExportPreviewResultRequest message or plain object  
`callback` |  `[ExportPreviewResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ExportPreviewResultResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportPreviewResult(request)
    
    
    public exportPreviewResult(request: google.cloud.config.v1.IExportPreviewResultRequest): Promise<google.cloud.config.v1.ExportPreviewResultResponse>;

Calls ExportPreviewResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportPreviewResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportpreviewresultrequest)`   
ExportPreviewResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse)>` | Promise  
  
### exportRevisionStatefile(request, callback)
    
    
    public exportRevisionStatefile(request: google.cloud.config.v1.IExportRevisionStatefileRequest, callback: google.cloud.config.v1.Config.ExportRevisionStatefileCallback): void;

Calls ExportRevisionStatefile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportRevisionStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportrevisionstatefilerequest)`   
ExportRevisionStatefileRequest message or plain object  
`callback` |  `[ExportRevisionStatefileCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Statefile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportRevisionStatefile(request)
    
    
    public exportRevisionStatefile(request: google.cloud.config.v1.IExportRevisionStatefileRequest): Promise<google.cloud.config.v1.Statefile>;

Calls ExportRevisionStatefile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportRevisionStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportrevisionstatefilerequest)`   
ExportRevisionStatefileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.Statefile](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.statefile)>` | Promise  
  
### getAutoMigrationConfig(request, callback)
    
    
    public getAutoMigrationConfig(request: google.cloud.config.v1.IGetAutoMigrationConfigRequest, callback: google.cloud.config.v1.Config.GetAutoMigrationConfigCallback): void;

Calls GetAutoMigrationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoMigrationConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetautomigrationconfigrequest)`   
GetAutoMigrationConfigRequest message or plain object  
`callback` |  `[GetAutoMigrationConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and AutoMigrationConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAutoMigrationConfig(request)
    
    
    public getAutoMigrationConfig(request: google.cloud.config.v1.IGetAutoMigrationConfigRequest): Promise<google.cloud.config.v1.AutoMigrationConfig>;

Calls GetAutoMigrationConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoMigrationConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetautomigrationconfigrequest)`   
GetAutoMigrationConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.AutoMigrationConfig](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.automigrationconfig)>` | Promise  
  
### getDeployment(request, callback)
    
    
    public getDeployment(request: google.cloud.config.v1.IGetDeploymentRequest, callback: google.cloud.config.v1.Config.GetDeploymentCallback): void;

Calls GetDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
`callback` |  `[GetDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeployment(request)
    
    
    public getDeployment(request: google.cloud.config.v1.IGetDeploymentRequest): Promise<google.cloud.config.v1.Deployment>;

Calls GetDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class)>` | Promise  
  
### getDeploymentGroup(request, callback)
    
    
    public getDeploymentGroup(request: google.cloud.config.v1.IGetDeploymentGroupRequest, callback: google.cloud.config.v1.Config.GetDeploymentGroupCallback): void;

Calls GetDeploymentGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetdeploymentgrouprequest)`   
GetDeploymentGroupRequest message or plain object  
`callback` |  `[GetDeploymentGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and DeploymentGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeploymentGroup(request)
    
    
    public getDeploymentGroup(request: google.cloud.config.v1.IGetDeploymentGroupRequest): Promise<google.cloud.config.v1.DeploymentGroup>;

Calls GetDeploymentGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetdeploymentgrouprequest)`   
GetDeploymentGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.DeploymentGroup](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentgroup-class)>` | Promise  
  
### getDeploymentGroupRevision(request, callback)
    
    
    public getDeploymentGroupRevision(request: google.cloud.config.v1.IGetDeploymentGroupRevisionRequest, callback: google.cloud.config.v1.Config.GetDeploymentGroupRevisionCallback): void;

Calls GetDeploymentGroupRevision.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetdeploymentgrouprevisionrequest)`   
GetDeploymentGroupRevisionRequest message or plain object  
`callback` |  `[GetDeploymentGroupRevisionCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and DeploymentGroupRevision  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeploymentGroupRevision(request)
    
    
    public getDeploymentGroupRevision(request: google.cloud.config.v1.IGetDeploymentGroupRevisionRequest): Promise<google.cloud.config.v1.DeploymentGroupRevision>;

Calls GetDeploymentGroupRevision.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetdeploymentgrouprevisionrequest)`   
GetDeploymentGroupRevisionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.DeploymentGroupRevision](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentgrouprevision)>` | Promise  
  
### getPreview(request, callback)
    
    
    public getPreview(request: google.cloud.config.v1.IGetPreviewRequest, callback: google.cloud.config.v1.Config.GetPreviewCallback): void;

Calls GetPreview.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPreviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetpreviewrequest)`   
GetPreviewRequest message or plain object  
`callback` |  `[GetPreviewCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Preview  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPreview(request)
    
    
    public getPreview(request: google.cloud.config.v1.IGetPreviewRequest): Promise<google.cloud.config.v1.Preview>;

Calls GetPreview.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPreviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetpreviewrequest)`   
GetPreviewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.Preview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class)>` | Promise  
  
### getResource(request, callback)
    
    
    public getResource(request: google.cloud.config.v1.IGetResourceRequest, callback: google.cloud.config.v1.Config.GetResourceCallback): void;

Calls GetResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetresourcerequest)`   
GetResourceRequest message or plain object  
`callback` |  `[GetResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Resource  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getResource(request)
    
    
    public getResource(request: google.cloud.config.v1.IGetResourceRequest): Promise<google.cloud.config.v1.Resource>;

Calls GetResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetresourcerequest)`   
GetResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.Resource](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.resource-class)>` | Promise  
  
### getResourceChange(request, callback)
    
    
    public getResourceChange(request: google.cloud.config.v1.IGetResourceChangeRequest, callback: google.cloud.config.v1.Config.GetResourceChangeCallback): void;

Calls GetResourceChange.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetresourcechangerequest)`   
GetResourceChangeRequest message or plain object  
`callback` |  `[GetResourceChangeCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ResourceChange  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getResourceChange(request)
    
    
    public getResourceChange(request: google.cloud.config.v1.IGetResourceChangeRequest): Promise<google.cloud.config.v1.ResourceChange>;

Calls GetResourceChange.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetresourcechangerequest)`   
GetResourceChangeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ResourceChange](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.resourcechange-class)>` | Promise  
  
### getResourceDrift(request, callback)
    
    
    public getResourceDrift(request: google.cloud.config.v1.IGetResourceDriftRequest, callback: google.cloud.config.v1.Config.GetResourceDriftCallback): void;

Calls GetResourceDrift.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceDriftRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetresourcedriftrequest)`   
GetResourceDriftRequest message or plain object  
`callback` |  `[GetResourceDriftCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ResourceDrift  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getResourceDrift(request)
    
    
    public getResourceDrift(request: google.cloud.config.v1.IGetResourceDriftRequest): Promise<google.cloud.config.v1.ResourceDrift>;

Calls GetResourceDrift.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceDriftRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetresourcedriftrequest)`   
GetResourceDriftRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ResourceDrift](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.resourcedrift)>` | Promise  
  
### getRevision(request, callback)
    
    
    public getRevision(request: google.cloud.config.v1.IGetRevisionRequest, callback: google.cloud.config.v1.Config.GetRevisionCallback): void;

Calls GetRevision.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetrevisionrequest)`   
GetRevisionRequest message or plain object  
`callback` |  `[GetRevisionCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Revision  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRevision(request)
    
    
    public getRevision(request: google.cloud.config.v1.IGetRevisionRequest): Promise<google.cloud.config.v1.Revision>;

Calls GetRevision.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetrevisionrequest)`   
GetRevisionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.Revision](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.revision-class)>` | Promise  
  
### getTerraformVersion(request, callback)
    
    
    public getTerraformVersion(request: google.cloud.config.v1.IGetTerraformVersionRequest, callback: google.cloud.config.v1.Config.GetTerraformVersionCallback): void;

Calls GetTerraformVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTerraformVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetterraformversionrequest)`   
GetTerraformVersionRequest message or plain object  
`callback` |  `[GetTerraformVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and TerraformVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTerraformVersion(request)
    
    
    public getTerraformVersion(request: google.cloud.config.v1.IGetTerraformVersionRequest): Promise<google.cloud.config.v1.TerraformVersion>;

Calls GetTerraformVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTerraformVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.igetterraformversionrequest)`   
GetTerraformVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.TerraformVersion](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.terraformversion-class)>` | Promise  
  
### importStatefile(request, callback)
    
    
    public importStatefile(request: google.cloud.config.v1.IImportStatefileRequest, callback: google.cloud.config.v1.Config.ImportStatefileCallback): void;

Calls ImportStatefile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iimportstatefilerequest)`   
ImportStatefileRequest message or plain object  
`callback` |  `[ImportStatefileCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Statefile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importStatefile(request)
    
    
    public importStatefile(request: google.cloud.config.v1.IImportStatefileRequest): Promise<google.cloud.config.v1.Statefile>;

Calls ImportStatefile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportStatefileRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iimportstatefilerequest)`   
ImportStatefileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.Statefile](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.statefile)>` | Promise  
  
### listDeploymentGroupRevisions(request, callback)
    
    
    public listDeploymentGroupRevisions(request: google.cloud.config.v1.IListDeploymentGroupRevisionsRequest, callback: google.cloud.config.v1.Config.ListDeploymentGroupRevisionsCallback): void;

Calls ListDeploymentGroupRevisions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistdeploymentgrouprevisionsrequest)`   
ListDeploymentGroupRevisionsRequest message or plain object  
`callback` |  `[ListDeploymentGroupRevisionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeploymentGroupRevisionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeploymentGroupRevisions(request)
    
    
    public listDeploymentGroupRevisions(request: google.cloud.config.v1.IListDeploymentGroupRevisionsRequest): Promise<google.cloud.config.v1.ListDeploymentGroupRevisionsResponse>;

Calls ListDeploymentGroupRevisions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistdeploymentgrouprevisionsrequest)`   
ListDeploymentGroupRevisionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listdeploymentgrouprevisionsresponse)>` | Promise  
  
### listDeploymentGroups(request, callback)
    
    
    public listDeploymentGroups(request: google.cloud.config.v1.IListDeploymentGroupsRequest, callback: google.cloud.config.v1.Config.ListDeploymentGroupsCallback): void;

Calls ListDeploymentGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistdeploymentgroupsrequest)`   
ListDeploymentGroupsRequest message or plain object  
`callback` |  `[ListDeploymentGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeploymentGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeploymentGroups(request)
    
    
    public listDeploymentGroups(request: google.cloud.config.v1.IListDeploymentGroupsRequest): Promise<google.cloud.config.v1.ListDeploymentGroupsResponse>;

Calls ListDeploymentGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistdeploymentgroupsrequest)`   
ListDeploymentGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListDeploymentGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listdeploymentgroupsresponse)>` | Promise  
  
### listDeployments(request, callback)
    
    
    public listDeployments(request: google.cloud.config.v1.IListDeploymentsRequest, callback: google.cloud.config.v1.Config.ListDeploymentsCallback): void;

Calls ListDeployments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
`callback` |  `[ListDeploymentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeploymentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeployments(request)
    
    
    public listDeployments(request: google.cloud.config.v1.IListDeploymentsRequest): Promise<google.cloud.config.v1.ListDeploymentsResponse>;

Calls ListDeployments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listdeploymentsresponse)>` | Promise  
  
### listPreviews(request, callback)
    
    
    public listPreviews(request: google.cloud.config.v1.IListPreviewsRequest, callback: google.cloud.config.v1.Config.ListPreviewsCallback): void;

Calls ListPreviews.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPreviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistpreviewsrequest)`   
ListPreviewsRequest message or plain object  
`callback` |  `[ListPreviewsCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPreviewsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPreviews(request)
    
    
    public listPreviews(request: google.cloud.config.v1.IListPreviewsRequest): Promise<google.cloud.config.v1.ListPreviewsResponse>;

Calls ListPreviews.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPreviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistpreviewsrequest)`   
ListPreviewsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListPreviewsResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listpreviewsresponse)>` | Promise  
  
### listResourceChanges(request, callback)
    
    
    public listResourceChanges(request: google.cloud.config.v1.IListResourceChangesRequest, callback: google.cloud.config.v1.Config.ListResourceChangesCallback): void;

Calls ListResourceChanges.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListResourceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistresourcechangesrequest)`   
ListResourceChangesRequest message or plain object  
`callback` |  `[ListResourceChangesCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListResourceChangesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listResourceChanges(request)
    
    
    public listResourceChanges(request: google.cloud.config.v1.IListResourceChangesRequest): Promise<google.cloud.config.v1.ListResourceChangesResponse>;

Calls ListResourceChanges.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListResourceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistresourcechangesrequest)`   
ListResourceChangesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListResourceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listresourcechangesresponse)>` | Promise  
  
### listResourceDrifts(request, callback)
    
    
    public listResourceDrifts(request: google.cloud.config.v1.IListResourceDriftsRequest, callback: google.cloud.config.v1.Config.ListResourceDriftsCallback): void;

Calls ListResourceDrifts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListResourceDriftsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistresourcedriftsrequest)`   
ListResourceDriftsRequest message or plain object  
`callback` |  `[ListResourceDriftsCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListResourceDriftsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listResourceDrifts(request)
    
    
    public listResourceDrifts(request: google.cloud.config.v1.IListResourceDriftsRequest): Promise<google.cloud.config.v1.ListResourceDriftsResponse>;

Calls ListResourceDrifts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListResourceDriftsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistresourcedriftsrequest)`   
ListResourceDriftsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListResourceDriftsResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listresourcedriftsresponse)>` | Promise  
  
### listResources(request, callback)
    
    
    public listResources(request: google.cloud.config.v1.IListResourcesRequest, callback: google.cloud.config.v1.Config.ListResourcesCallback): void;

Calls ListResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistresourcesrequest)`   
ListResourcesRequest message or plain object  
`callback` |  `[ListResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListResourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listResources(request)
    
    
    public listResources(request: google.cloud.config.v1.IListResourcesRequest): Promise<google.cloud.config.v1.ListResourcesResponse>;

Calls ListResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistresourcesrequest)`   
ListResourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listresourcesresponse)>` | Promise  
  
### listRevisions(request, callback)
    
    
    public listRevisions(request: google.cloud.config.v1.IListRevisionsRequest, callback: google.cloud.config.v1.Config.ListRevisionsCallback): void;

Calls ListRevisions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistrevisionsrequest)`   
ListRevisionsRequest message or plain object  
`callback` |  `[ListRevisionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRevisionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRevisions(request)
    
    
    public listRevisions(request: google.cloud.config.v1.IListRevisionsRequest): Promise<google.cloud.config.v1.ListRevisionsResponse>;

Calls ListRevisions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistrevisionsrequest)`   
ListRevisionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listrevisionsresponse)>` | Promise  
  
### listTerraformVersions(request, callback)
    
    
    public listTerraformVersions(request: google.cloud.config.v1.IListTerraformVersionsRequest, callback: google.cloud.config.v1.Config.ListTerraformVersionsCallback): void;

Calls ListTerraformVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTerraformVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistterraformversionsrequest)`   
ListTerraformVersionsRequest message or plain object  
`callback` |  `[ListTerraformVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTerraformVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTerraformVersions(request)
    
    
    public listTerraformVersions(request: google.cloud.config.v1.IListTerraformVersionsRequest): Promise<google.cloud.config.v1.ListTerraformVersionsResponse>;

Calls ListTerraformVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTerraformVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilistterraformversionsrequest)`   
ListTerraformVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.config.v1.ListTerraformVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.listterraformversionsresponse)>` | Promise  
  
### lockDeployment(request, callback)
    
    
    public lockDeployment(request: google.cloud.config.v1.ILockDeploymentRequest, callback: google.cloud.config.v1.Config.LockDeploymentCallback): void;

Calls LockDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILockDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilockdeploymentrequest)`   
LockDeploymentRequest message or plain object  
`callback` |  `[LockDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lockDeployment(request)
    
    
    public lockDeployment(request: google.cloud.config.v1.ILockDeploymentRequest): Promise<google.longrunning.Operation>;

Calls LockDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILockDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ilockdeploymentrequest)`   
LockDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### provisionDeploymentGroup(request, callback)
    
    
    public provisionDeploymentGroup(request: google.cloud.config.v1.IProvisionDeploymentGroupRequest, callback: google.cloud.config.v1.Config.ProvisionDeploymentGroupCallback): void;

Calls ProvisionDeploymentGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iprovisiondeploymentgrouprequest)`   
ProvisionDeploymentGroupRequest message or plain object  
`callback` |  `[ProvisionDeploymentGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### provisionDeploymentGroup(request)
    
    
    public provisionDeploymentGroup(request: google.cloud.config.v1.IProvisionDeploymentGroupRequest): Promise<google.longrunning.Operation>;

Calls ProvisionDeploymentGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IProvisionDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iprovisiondeploymentgrouprequest)`   
ProvisionDeploymentGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### unlockDeployment(request, callback)
    
    
    public unlockDeployment(request: google.cloud.config.v1.IUnlockDeploymentRequest, callback: google.cloud.config.v1.Config.UnlockDeploymentCallback): void;

Calls UnlockDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUnlockDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iunlockdeploymentrequest)`   
UnlockDeploymentRequest message or plain object  
`callback` |  `[UnlockDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### unlockDeployment(request)
    
    
    public unlockDeployment(request: google.cloud.config.v1.IUnlockDeploymentRequest): Promise<google.longrunning.Operation>;

Calls UnlockDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUnlockDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iunlockdeploymentrequest)`   
UnlockDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### updateAutoMigrationConfig(request, callback)
    
    
    public updateAutoMigrationConfig(request: google.cloud.config.v1.IUpdateAutoMigrationConfigRequest, callback: google.cloud.config.v1.Config.UpdateAutoMigrationConfigCallback): void;

Calls UpdateAutoMigrationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iupdateautomigrationconfigrequest)`   
UpdateAutoMigrationConfigRequest message or plain object  
`callback` |  `[UpdateAutoMigrationConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAutoMigrationConfig(request)
    
    
    public updateAutoMigrationConfig(request: google.cloud.config.v1.IUpdateAutoMigrationConfigRequest): Promise<google.longrunning.Operation>;

Calls UpdateAutoMigrationConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iupdateautomigrationconfigrequest)`   
UpdateAutoMigrationConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### updateDeployment(request, callback)
    
    
    public updateDeployment(request: google.cloud.config.v1.IUpdateDeploymentRequest, callback: google.cloud.config.v1.Config.UpdateDeploymentCallback): void;

Calls UpdateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iupdatedeploymentrequest)`   
UpdateDeploymentRequest message or plain object  
`callback` |  `[UpdateDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDeployment(request)
    
    
    public updateDeployment(request: google.cloud.config.v1.IUpdateDeploymentRequest): Promise<google.longrunning.Operation>;

Calls UpdateDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iupdatedeploymentrequest)`   
UpdateDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
### updateDeploymentGroup(request, callback)
    
    
    public updateDeploymentGroup(request: google.cloud.config.v1.IUpdateDeploymentGroupRequest, callback: google.cloud.config.v1.Config.UpdateDeploymentGroupCallback): void;

Calls UpdateDeploymentGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iupdatedeploymentgrouprequest)`   
UpdateDeploymentGroupRequest message or plain object  
`callback` |  `[UpdateDeploymentGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDeploymentGroup(request)
    
    
    public updateDeploymentGroup(request: google.cloud.config.v1.IUpdateDeploymentGroupRequest): Promise<google.longrunning.Operation>;

Calls UpdateDeploymentGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iupdatedeploymentgrouprequest)`   
UpdateDeploymentGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
