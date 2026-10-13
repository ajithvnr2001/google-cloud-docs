---
url: https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.cloudmemcache-class
title: Class protos.google.cloud.memcache.v1beta2.CloudMemcache (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:38.584525+00:00
---

# Class protos.google.cloud.memcache.v1beta2.CloudMemcache (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.cloudmemcache-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.memcache.v1beta2.CloudMemcache (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  2.3.2  2.1.4  1.5.1  1.4.7 

Represents a CloudMemcache

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.memcache.v1beta2.CloudMemcache

## Package

[@google-cloud/memcache](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CloudMemcache service.

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

### applyParameters(request, callback)
    
    
    public applyParameters(request: google.cloud.memcache.v1beta2.IApplyParametersRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.ApplyParametersCallback): void;

Calls ApplyParameters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApplyParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iapplyparametersrequest)`   
ApplyParametersRequest message or plain object  
`callback` |  `[ApplyParametersCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### applyParameters(request)
    
    
    public applyParameters(request: google.cloud.memcache.v1beta2.IApplyParametersRequest): Promise<google.longrunning.Operation>;

Calls ApplyParameters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApplyParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iapplyparametersrequest)`   
ApplyParametersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### applySoftwareUpdate(request, callback)
    
    
    public applySoftwareUpdate(request: google.cloud.memcache.v1beta2.IApplySoftwareUpdateRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.ApplySoftwareUpdateCallback): void;

Calls ApplySoftwareUpdate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApplySoftwareUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iapplysoftwareupdaterequest)`   
ApplySoftwareUpdateRequest message or plain object  
`callback` |  `[ApplySoftwareUpdateCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### applySoftwareUpdate(request)
    
    
    public applySoftwareUpdate(request: google.cloud.memcache.v1beta2.IApplySoftwareUpdateRequest): Promise<google.longrunning.Operation>;

Calls ApplySoftwareUpdate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApplySoftwareUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iapplysoftwareupdaterequest)`   
ApplySoftwareUpdateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CloudMemcache;

Creates new CloudMemcache service using the specified rpc implementation.

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
`[CloudMemcache](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.cloudmemcache-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createInstance(request, callback)
    
    
    public createInstance(request: google.cloud.memcache.v1beta2.ICreateInstanceRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.CreateInstanceCallback): void;

Calls CreateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
`callback` |  `[CreateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstance(request)
    
    
    public createInstance(request: google.cloud.memcache.v1beta2.ICreateInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### deleteInstance(request, callback)
    
    
    public deleteInstance(request: google.cloud.memcache.v1beta2.IDeleteInstanceRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.DeleteInstanceCallback): void;

Calls DeleteInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
`callback` |  `[DeleteInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstance(request)
    
    
    public deleteInstance(request: google.cloud.memcache.v1beta2.IDeleteInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.memcache.v1beta2.IGetInstanceRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.memcache.v1beta2.IGetInstanceRequest): Promise<google.cloud.memcache.v1beta2.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memcache.v1beta2.Instance](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.instance-class)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.memcache.v1beta2.IListInstancesRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.memcache.v1beta2.IListInstancesRequest): Promise<google.cloud.memcache.v1beta2.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memcache.v1beta2.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.listinstancesresponse)>` | Promise  
  
### rescheduleMaintenance(request, callback)
    
    
    public rescheduleMaintenance(request: google.cloud.memcache.v1beta2.IRescheduleMaintenanceRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.RescheduleMaintenanceCallback): void;

Calls RescheduleMaintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
`callback` |  `[RescheduleMaintenanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rescheduleMaintenance(request)
    
    
    public rescheduleMaintenance(request: google.cloud.memcache.v1beta2.IRescheduleMaintenanceRequest): Promise<google.longrunning.Operation>;

Calls RescheduleMaintenance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### updateInstance(request, callback)
    
    
    public updateInstance(request: google.cloud.memcache.v1beta2.IUpdateInstanceRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.UpdateInstanceCallback): void;

Calls UpdateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
`callback` |  `[UpdateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInstance(request)
    
    
    public updateInstance(request: google.cloud.memcache.v1beta2.IUpdateInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpdateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### updateParameters(request, callback)
    
    
    public updateParameters(request: google.cloud.memcache.v1beta2.IUpdateParametersRequest, callback: google.cloud.memcache.v1beta2.CloudMemcache.UpdateParametersCallback): void;

Calls UpdateParameters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iupdateparametersrequest)`   
UpdateParametersRequest message or plain object  
`callback` |  `[UpdateParametersCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateParameters(request)
    
    
    public updateParameters(request: google.cloud.memcache.v1beta2.IUpdateParametersRequest): Promise<google.longrunning.Operation>;

Calls UpdateParameters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1beta2.iupdateparametersrequest)`   
UpdateParametersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
