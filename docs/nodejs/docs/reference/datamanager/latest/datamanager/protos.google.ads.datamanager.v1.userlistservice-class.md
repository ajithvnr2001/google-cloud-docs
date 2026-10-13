---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistservice-class
title: Class protos.google.ads.datamanager.v1.UserListService (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:42.605697+00:00
---

# Class protos.google.ads.datamanager.v1.UserListService (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.UserListService (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a UserListService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.datamanager.v1.UserListService

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new UserListService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): UserListService;

Creates new UserListService service using the specified rpc implementation.

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
`[UserListService](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createUserList(request, callback)
    
    
    public createUserList(request: google.ads.datamanager.v1.ICreateUserListRequest, callback: google.ads.datamanager.v1.UserListService.CreateUserListCallback): void;

Calls CreateUserList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreateuserlistrequest)`   
CreateUserListRequest message or plain object  
`callback` |  `[CreateUserListCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserList(request)
    
    
    public createUserList(request: google.ads.datamanager.v1.ICreateUserListRequest): Promise<google.ads.datamanager.v1.UserList>;

Calls CreateUserList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreateuserlistrequest)`   
CreateUserListRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)>` | Promise  
  
### deleteUserList(request, callback)
    
    
    public deleteUserList(request: google.ads.datamanager.v1.IDeleteUserListRequest, callback: google.ads.datamanager.v1.UserListService.DeleteUserListCallback): void;

Calls DeleteUserList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ideleteuserlistrequest)`   
DeleteUserListRequest message or plain object  
`callback` |  `[DeleteUserListCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUserList(request)
    
    
    public deleteUserList(request: google.ads.datamanager.v1.IDeleteUserListRequest): Promise<google.protobuf.Empty>;

Calls DeleteUserList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ideleteuserlistrequest)`   
DeleteUserListRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.protobuf.empty)>` | Promise  
  
### getUserList(request, callback)
    
    
    public getUserList(request: google.ads.datamanager.v1.IGetUserListRequest, callback: google.ads.datamanager.v1.UserListService.GetUserListCallback): void;

Calls GetUserList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.igetuserlistrequest)`   
GetUserListRequest message or plain object  
`callback` |  `[GetUserListCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserList(request)
    
    
    public getUserList(request: google.ads.datamanager.v1.IGetUserListRequest): Promise<google.ads.datamanager.v1.UserList>;

Calls GetUserList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.igetuserlistrequest)`   
GetUserListRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)>` | Promise  
  
### listUserLists(request, callback)
    
    
    public listUserLists(request: google.ads.datamanager.v1.IListUserListsRequest, callback: google.ads.datamanager.v1.UserListService.ListUserListsCallback): void;

Calls ListUserLists.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistsrequest)`   
ListUserListsRequest message or plain object  
`callback` |  `[ListUserListsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUserListsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserLists(request)
    
    
    public listUserLists(request: google.ads.datamanager.v1.IListUserListsRequest): Promise<google.ads.datamanager.v1.ListUserListsResponse>;

Calls ListUserLists.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUserListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistsrequest)`   
ListUserListsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.ListUserListsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.listuserlistsresponse)>` | Promise  
  
### updateUserList(request, callback)
    
    
    public updateUserList(request: google.ads.datamanager.v1.IUpdateUserListRequest, callback: google.ads.datamanager.v1.UserListService.UpdateUserListCallback): void;

Calls UpdateUserList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iupdateuserlistrequest)`   
UpdateUserListRequest message or plain object  
`callback` |  `[UpdateUserListCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUserList(request)
    
    
    public updateUserList(request: google.ads.datamanager.v1.IUpdateUserListRequest): Promise<google.ads.datamanager.v1.UserList>;

Calls UpdateUserList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserListRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iupdateuserlistrequest)`   
UpdateUserListRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
