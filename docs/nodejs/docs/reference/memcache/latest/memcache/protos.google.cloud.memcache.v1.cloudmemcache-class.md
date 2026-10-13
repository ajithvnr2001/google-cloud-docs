---
url: https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.cloudmemcache-class
title: Class protos.google.cloud.memcache.v1.CloudMemcache (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:34.674758+00:00
---

# Class protos.google.cloud.memcache.v1.CloudMemcache (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.cloudmemcache-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.memcache.v1.CloudMemcache (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  2.3.2  2.1.4  1.5.1  1.4.7 

Represents a CloudMemcache

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.memcache.v1.CloudMemcache

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
    
    
    public applyParameters(request: google.cloud.memcache.v1.IApplyParametersRequest, callback: google.cloud.memcache.v1.CloudMemcache.ApplyParametersCallback): void;

Calls ApplyParameters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApplyParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.iapplyparametersrequest)`   
ApplyParametersRequest message or plain object  
`callback` |  `[ApplyParametersCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### applyParameters(request)
    
    
    public applyParameters(request: google.cloud.memcache.v1.IApplyParametersRequest): Promise<google.longrunning.Operation>;

Calls ApplyParameters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApplyParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.iapplyparametersrequest)`   
ApplyParametersRequest message or plain object  
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
`[CloudMemcache](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.cloudmemcache-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createInstance(request, callback)
    
    
    public createInstance(request: google.cloud.memcache.v1.ICreateInstanceRequest, callback: google.cloud.memcache.v1.CloudMemcache.CreateInstanceCallback): void;

Calls CreateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
`callback` |  `[CreateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstance(request)
    
    
    public createInstance(request: google.cloud.memcache.v1.ICreateInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### deleteInstance(request, callback)
    
    
    public deleteInstance(request: google.cloud.memcache.v1.IDeleteInstanceRequest, callback: google.cloud.memcache.v1.CloudMemcache.DeleteInstanceCallback): void;

Calls DeleteInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
`callback` |  `[DeleteInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstance(request)
    
    
    public deleteInstance(request: google.cloud.memcache.v1.IDeleteInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.memcache.v1.IGetInstanceRequest, callback: google.cloud.memcache.v1.CloudMemcache.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.memcache.v1.IGetInstanceRequest): Promise<google.cloud.memcache.v1.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memcache.v1.Instance](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.instance-class)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.memcache.v1.IListInstancesRequest, callback: google.cloud.memcache.v1.CloudMemcache.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.memcache.v1.IListInstancesRequest): Promise<google.cloud.memcache.v1.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memcache.v1.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.listinstancesresponse)>` | Promise  
  
### rescheduleMaintenance(request, callback)
    
    
    public rescheduleMaintenance(request: google.cloud.memcache.v1.IRescheduleMaintenanceRequest, callback: google.cloud.memcache.v1.CloudMemcache.RescheduleMaintenanceCallback): void;

Calls RescheduleMaintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
`callback` |  `[RescheduleMaintenanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rescheduleMaintenance(request)
    
    
    public rescheduleMaintenance(request: google.cloud.memcache.v1.IRescheduleMaintenanceRequest): Promise<google.longrunning.Operation>;

Calls RescheduleMaintenance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### updateInstance(request, callback)
    
    
    public updateInstance(request: google.cloud.memcache.v1.IUpdateInstanceRequest, callback: google.cloud.memcache.v1.CloudMemcache.UpdateInstanceCallback): void;

Calls UpdateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
`callback` |  `[UpdateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInstance(request)
    
    
    public updateInstance(request: google.cloud.memcache.v1.IUpdateInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpdateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### updateParameters(request, callback)
    
    
    public updateParameters(request: google.cloud.memcache.v1.IUpdateParametersRequest, callback: google.cloud.memcache.v1.CloudMemcache.UpdateParametersCallback): void;

Calls UpdateParameters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.iupdateparametersrequest)`   
UpdateParametersRequest message or plain object  
`callback` |  `[UpdateParametersCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateParameters(request)
    
    
    public updateParameters(request: google.cloud.memcache.v1.IUpdateParametersRequest): Promise<google.longrunning.Operation>;

Calls UpdateParameters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.cloud.memcache.v1.iupdateparametersrequest)`   
UpdateParametersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
