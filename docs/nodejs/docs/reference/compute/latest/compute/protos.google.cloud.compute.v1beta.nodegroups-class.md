---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.nodegroups-class
title: Class protos.google.cloud.compute.v1beta.NodeGroups (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:36.799760+00:00
---

# Class protos.google.cloud.compute.v1beta.NodeGroups (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.nodegroups-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.NodeGroups (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a NodeGroups

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1beta.NodeGroups

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new NodeGroups service.

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

### addNodes(request, callback)
    
    
    public addNodes(request: google.cloud.compute.v1beta.IAddNodesNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.AddNodesCallback): void;

Calls AddNodes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddnodesnodegrouprequest)`   
AddNodesNodeGroupRequest message or plain object  
`callback` |  `[AddNodesCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addNodes(request)
    
    
    public addNodes(request: google.cloud.compute.v1beta.IAddNodesNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls AddNodes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddnodesnodegrouprequest)`   
AddNodesNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### aggregatedList(request, callback)
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListNodeGroupsRequest, callback: google.cloud.compute.v1beta.NodeGroups.AggregatedListCallback): void;

Calls AggregatedList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListNodeGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlistnodegroupsrequest)`   
AggregatedListNodeGroupsRequest message or plain object  
`callback` |  `[AggregatedListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and NodeGroupAggregatedList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### aggregatedList(request)
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListNodeGroupsRequest): Promise<google.cloud.compute.v1beta.NodeGroupAggregatedList>;

Calls AggregatedList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListNodeGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlistnodegroupsrequest)`   
AggregatedListNodeGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.NodeGroupAggregatedList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.nodegroupaggregatedlist)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): NodeGroups;

Creates new NodeGroups service using the specified rpc implementation.

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
`[NodeGroups](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.nodegroups-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletenodegrouprequest)`   
DeleteNodeGroupRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletenodegrouprequest)`   
DeleteNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### deleteNodes(request, callback)
    
    
    public deleteNodes(request: google.cloud.compute.v1beta.IDeleteNodesNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.DeleteNodesCallback): void;

Calls DeleteNodes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletenodesnodegrouprequest)`   
DeleteNodesNodeGroupRequest message or plain object  
`callback` |  `[DeleteNodesCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteNodes(request)
    
    
    public deleteNodes(request: google.cloud.compute.v1beta.IDeleteNodesNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls DeleteNodes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletenodesnodegrouprequest)`   
DeleteNodesNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1beta.IGetNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetnodegrouprequest)`   
GetNodeGroupRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and NodeGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1beta.IGetNodeGroupRequest): Promise<google.cloud.compute.v1beta.NodeGroup>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetnodegrouprequest)`   
GetNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.NodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.nodegroup-class)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.cloud.compute.v1beta.IGetIamPolicyNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicynodegrouprequest)`   
GetIamPolicyNodeGroupRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.cloud.compute.v1beta.IGetIamPolicyNodeGroupRequest): Promise<google.cloud.compute.v1beta.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicynodegrouprequest)`   
GetIamPolicyNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertnodegrouprequest)`   
InsertNodeGroupRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertnodegrouprequest)`   
InsertNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1beta.IListNodeGroupsRequest, callback: google.cloud.compute.v1beta.NodeGroups.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodeGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistnodegroupsrequest)`   
ListNodeGroupsRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and NodeGroupList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1beta.IListNodeGroupsRequest): Promise<google.cloud.compute.v1beta.NodeGroupList>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListNodeGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistnodegroupsrequest)`   
ListNodeGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.NodeGroupList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.nodegrouplist)>` | Promise  
  
### listNodes(request, callback)
    
    
    public listNodes(request: google.cloud.compute.v1beta.IListNodesNodeGroupsRequest, callback: google.cloud.compute.v1beta.NodeGroups.ListNodesCallback): void;

Calls ListNodes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodesNodeGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistnodesnodegroupsrequest)`   
ListNodesNodeGroupsRequest message or plain object  
`callback` |  `[ListNodesCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and NodeGroupsListNodes  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNodes(request)
    
    
    public listNodes(request: google.cloud.compute.v1beta.IListNodesNodeGroupsRequest): Promise<google.cloud.compute.v1beta.NodeGroupsListNodes>;

Calls ListNodes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListNodesNodeGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistnodesnodegroupsrequest)`   
ListNodesNodeGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.NodeGroupsListNodes](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.nodegroupslistnodes)>` | Promise  
  
### patch(request, callback)
    
    
    public patch(request: google.cloud.compute.v1beta.IPatchNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.PatchCallback): void;

Calls Patch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchnodegrouprequest)`   
PatchNodeGroupRequest message or plain object  
`callback` |  `[PatchCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patch(request)
    
    
    public patch(request: google.cloud.compute.v1beta.IPatchNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Patch.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPatchNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchnodegrouprequest)`   
PatchNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### performMaintenance(request, callback)
    
    
    public performMaintenance(request: google.cloud.compute.v1beta.IPerformMaintenanceNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.PerformMaintenanceCallback): void;

Calls PerformMaintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPerformMaintenanceNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iperformmaintenancenodegrouprequest)`   
PerformMaintenanceNodeGroupRequest message or plain object  
`callback` |  `[PerformMaintenanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### performMaintenance(request)
    
    
    public performMaintenance(request: google.cloud.compute.v1beta.IPerformMaintenanceNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls PerformMaintenance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPerformMaintenanceNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iperformmaintenancenodegrouprequest)`   
PerformMaintenanceNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.cloud.compute.v1beta.ISetIamPolicyNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicynodegrouprequest)`   
SetIamPolicyNodeGroupRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.cloud.compute.v1beta.ISetIamPolicyNodeGroupRequest): Promise<google.cloud.compute.v1beta.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicynodegrouprequest)`   
SetIamPolicyNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy)>` | Promise  
  
### setNodeTemplate(request, callback)
    
    
    public setNodeTemplate(request: google.cloud.compute.v1beta.ISetNodeTemplateNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.SetNodeTemplateCallback): void;

Calls SetNodeTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodeTemplateNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetnodetemplatenodegrouprequest)`   
SetNodeTemplateNodeGroupRequest message or plain object  
`callback` |  `[SetNodeTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodeTemplate(request)
    
    
    public setNodeTemplate(request: google.cloud.compute.v1beta.ISetNodeTemplateNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetNodeTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetNodeTemplateNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetnodetemplatenodegrouprequest)`   
SetNodeTemplateNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### simulateMaintenanceEvent(request, callback)
    
    
    public simulateMaintenanceEvent(request: google.cloud.compute.v1beta.ISimulateMaintenanceEventNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.SimulateMaintenanceEventCallback): void;

Calls SimulateMaintenanceEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISimulateMaintenanceEventNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isimulatemaintenanceeventnodegrouprequest)`   
SimulateMaintenanceEventNodeGroupRequest message or plain object  
`callback` |  `[SimulateMaintenanceEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### simulateMaintenanceEvent(request)
    
    
    public simulateMaintenanceEvent(request: google.cloud.compute.v1beta.ISimulateMaintenanceEventNodeGroupRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SimulateMaintenanceEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISimulateMaintenanceEventNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isimulatemaintenanceeventnodegrouprequest)`   
SimulateMaintenanceEventNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsNodeGroupRequest, callback: google.cloud.compute.v1beta.NodeGroups.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsnodegrouprequest)`   
TestIamPermissionsNodeGroupRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TestPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsNodeGroupRequest): Promise<google.cloud.compute.v1beta.TestPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsnodegrouprequest)`   
TestIamPermissionsNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
