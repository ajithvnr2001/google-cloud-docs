---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.cloudredis-class
title: Class protos.google.cloud.redis.v1.CloudRedis (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:16.719151+00:00
---

# Class protos.google.cloud.redis.v1.CloudRedis (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.cloudredis-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.redis.v1.CloudRedis (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.3.0  5.1.0  5.0.1  3.3.0  3.2.2  3.1.5  2.4.0  2.3.1  2.2.6 

Represents a CloudRedis

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.redis.v1.CloudRedis

## Package

[@google-cloud/redis](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CloudRedis service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CloudRedis;

Creates new CloudRedis service using the specified rpc implementation.

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
`[CloudRedis](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.cloudredis-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createInstance(request, callback)
    
    
    public createInstance(request: google.cloud.redis.v1.ICreateInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.CreateInstanceCallback): void;

Calls CreateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
`callback` |  `[CreateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstance(request)
    
    
    public createInstance(request: google.cloud.redis.v1.ICreateInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
### deleteInstance(request, callback)
    
    
    public deleteInstance(request: google.cloud.redis.v1.IDeleteInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.DeleteInstanceCallback): void;

Calls DeleteInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
`callback` |  `[DeleteInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstance(request)
    
    
    public deleteInstance(request: google.cloud.redis.v1.IDeleteInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
### exportInstance(request, callback)
    
    
    public exportInstance(request: google.cloud.redis.v1.IExportInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.ExportInstanceCallback): void;

Calls ExportInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iexportinstancerequest)`   
ExportInstanceRequest message or plain object  
`callback` |  `[ExportInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportInstance(request)
    
    
    public exportInstance(request: google.cloud.redis.v1.IExportInstanceRequest): Promise<google.longrunning.Operation>;

Calls ExportInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iexportinstancerequest)`   
ExportInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
### failoverInstance(request, callback)
    
    
    public failoverInstance(request: google.cloud.redis.v1.IFailoverInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.FailoverInstanceCallback): void;

Calls FailoverInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFailoverInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ifailoverinstancerequest)`   
FailoverInstanceRequest message or plain object  
`callback` |  `[FailoverInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### failoverInstance(request)
    
    
    public failoverInstance(request: google.cloud.redis.v1.IFailoverInstanceRequest): Promise<google.longrunning.Operation>;

Calls FailoverInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFailoverInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ifailoverinstancerequest)`   
FailoverInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.redis.v1.IGetInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.redis.v1.IGetInstanceRequest): Promise<google.cloud.redis.v1.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.redis.v1.Instance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class)>` | Promise  
  
### getInstanceAuthString(request, callback)
    
    
    public getInstanceAuthString(request: google.cloud.redis.v1.IGetInstanceAuthStringRequest, callback: google.cloud.redis.v1.CloudRedis.GetInstanceAuthStringCallback): void;

Calls GetInstanceAuthString.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceAuthStringRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.igetinstanceauthstringrequest)`   
GetInstanceAuthStringRequest message or plain object  
`callback` |  `[GetInstanceAuthStringCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and InstanceAuthString  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstanceAuthString(request)
    
    
    public getInstanceAuthString(request: google.cloud.redis.v1.IGetInstanceAuthStringRequest): Promise<google.cloud.redis.v1.InstanceAuthString>;

Calls GetInstanceAuthString.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceAuthStringRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.igetinstanceauthstringrequest)`   
GetInstanceAuthStringRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.redis.v1.InstanceAuthString](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instanceauthstring)>` | Promise  
  
### importInstance(request, callback)
    
    
    public importInstance(request: google.cloud.redis.v1.IImportInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.ImportInstanceCallback): void;

Calls ImportInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iimportinstancerequest)`   
ImportInstanceRequest message or plain object  
`callback` |  `[ImportInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importInstance(request)
    
    
    public importInstance(request: google.cloud.redis.v1.IImportInstanceRequest): Promise<google.longrunning.Operation>;

Calls ImportInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iimportinstancerequest)`   
ImportInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.redis.v1.IListInstancesRequest, callback: google.cloud.redis.v1.CloudRedis.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.redis.v1.IListInstancesRequest): Promise<google.cloud.redis.v1.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.redis.v1.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.listinstancesresponse)>` | Promise  
  
### rescheduleMaintenance(request, callback)
    
    
    public rescheduleMaintenance(request: google.cloud.redis.v1.IRescheduleMaintenanceRequest, callback: google.cloud.redis.v1.CloudRedis.RescheduleMaintenanceCallback): void;

Calls RescheduleMaintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
`callback` |  `[RescheduleMaintenanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rescheduleMaintenance(request)
    
    
    public rescheduleMaintenance(request: google.cloud.redis.v1.IRescheduleMaintenanceRequest): Promise<google.longrunning.Operation>;

Calls RescheduleMaintenance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
### updateInstance(request, callback)
    
    
    public updateInstance(request: google.cloud.redis.v1.IUpdateInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.UpdateInstanceCallback): void;

Calls UpdateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
`callback` |  `[UpdateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInstance(request)
    
    
    public updateInstance(request: google.cloud.redis.v1.IUpdateInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpdateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
### upgradeInstance(request, callback)
    
    
    public upgradeInstance(request: google.cloud.redis.v1.IUpgradeInstanceRequest, callback: google.cloud.redis.v1.CloudRedis.UpgradeInstanceCallback): void;

Calls UpgradeInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpgradeInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iupgradeinstancerequest)`   
UpgradeInstanceRequest message or plain object  
`callback` |  `[UpgradeInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### upgradeInstance(request)
    
    
    public upgradeInstance(request: google.cloud.redis.v1.IUpgradeInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpgradeInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpgradeInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iupgradeinstancerequest)`   
UpgradeInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
