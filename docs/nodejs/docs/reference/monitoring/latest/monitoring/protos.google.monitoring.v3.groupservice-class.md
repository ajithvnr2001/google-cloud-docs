---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.groupservice-class
title: Class protos.google.monitoring.v3.GroupService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:58.275078+00:00
---

# Class protos.google.monitoring.v3.GroupService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.groupservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.GroupService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a GroupService

## Inheritance

$protobuf.rpc.Service > protos.google.monitoring.v3.GroupService

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new GroupService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): GroupService;

Creates new GroupService service using the specified rpc implementation.

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
`[GroupService](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.groupservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createGroup(request, callback)
    
    
    public createGroup(request: google.monitoring.v3.ICreateGroupRequest, callback: google.monitoring.v3.GroupService.CreateGroupCallback): void;

Calls CreateGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreategrouprequest)`   
CreateGroupRequest message or plain object  
`callback` |  `[CreateGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and Group  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGroup(request)
    
    
    public createGroup(request: google.monitoring.v3.ICreateGroupRequest): Promise<google.monitoring.v3.Group>;

Calls CreateGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreategrouprequest)`   
CreateGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.Group](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.group)>` | Promise  
  
### deleteGroup(request, callback)
    
    
    public deleteGroup(request: google.monitoring.v3.IDeleteGroupRequest, callback: google.monitoring.v3.GroupService.DeleteGroupCallback): void;

Calls DeleteGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ideletegrouprequest)`   
DeleteGroupRequest message or plain object  
`callback` |  `[DeleteGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGroup(request)
    
    
    public deleteGroup(request: google.monitoring.v3.IDeleteGroupRequest): Promise<google.protobuf.Empty>;

Calls DeleteGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ideletegrouprequest)`   
DeleteGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.protobuf.empty)>` | Promise  
  
### getGroup(request, callback)
    
    
    public getGroup(request: google.monitoring.v3.IGetGroupRequest, callback: google.monitoring.v3.GroupService.GetGroupCallback): void;

Calls GetGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetgrouprequest)`   
GetGroupRequest message or plain object  
`callback` |  `[GetGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and Group  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGroup(request)
    
    
    public getGroup(request: google.monitoring.v3.IGetGroupRequest): Promise<google.monitoring.v3.Group>;

Calls GetGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetgrouprequest)`   
GetGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.Group](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.group)>` | Promise  
  
### listGroupMembers(request, callback)
    
    
    public listGroupMembers(request: google.monitoring.v3.IListGroupMembersRequest, callback: google.monitoring.v3.GroupService.ListGroupMembersCallback): void;

Calls ListGroupMembers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ilistgroupmembersrequest)`   
ListGroupMembersRequest message or plain object  
`callback` |  `[ListGroupMembersCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGroupMembersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGroupMembers(request)
    
    
    public listGroupMembers(request: google.monitoring.v3.IListGroupMembersRequest): Promise<google.monitoring.v3.ListGroupMembersResponse>;

Calls ListGroupMembers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ilistgroupmembersrequest)`   
ListGroupMembersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.ListGroupMembersResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.listgroupmembersresponse)>` | Promise  
  
### listGroups(request, callback)
    
    
    public listGroups(request: google.monitoring.v3.IListGroupsRequest, callback: google.monitoring.v3.GroupService.ListGroupsCallback): void;

Calls ListGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ilistgroupsrequest)`   
ListGroupsRequest message or plain object  
`callback` |  `[ListGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGroups(request)
    
    
    public listGroups(request: google.monitoring.v3.IListGroupsRequest): Promise<google.monitoring.v3.ListGroupsResponse>;

Calls ListGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ilistgroupsrequest)`   
ListGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.ListGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.listgroupsresponse)>` | Promise  
  
### updateGroup(request, callback)
    
    
    public updateGroup(request: google.monitoring.v3.IUpdateGroupRequest, callback: google.monitoring.v3.GroupService.UpdateGroupCallback): void;

Calls UpdateGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.iupdategrouprequest)`   
UpdateGroupRequest message or plain object  
`callback` |  `[UpdateGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and Group  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGroup(request)
    
    
    public updateGroup(request: google.monitoring.v3.IUpdateGroupRequest): Promise<google.monitoring.v3.Group>;

Calls UpdateGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.iupdategrouprequest)`   
UpdateGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.Group](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.group)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
