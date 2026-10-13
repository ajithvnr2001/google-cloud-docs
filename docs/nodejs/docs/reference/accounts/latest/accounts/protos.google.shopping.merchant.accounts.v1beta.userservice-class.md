---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.userservice-class
title: Class protos.google.shopping.merchant.accounts.v1beta.UserService (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:59.844290+00:00
---

# Class protos.google.shopping.merchant.accounts.v1beta.UserService (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.userservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.accounts.v1beta.UserService (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Represents a UserService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.accounts.v1beta.UserService

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new UserService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): UserService;

Creates new UserService service using the specified rpc implementation.

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
`[UserService](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.userservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createUser(request, callback)
    
    
    public createUser(request: google.shopping.merchant.accounts.v1beta.ICreateUserRequest, callback: google.shopping.merchant.accounts.v1beta.UserService.CreateUserCallback): void;

Calls CreateUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.icreateuserrequest)`   
CreateUserRequest message or plain object  
`callback` |  `[CreateUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and User  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUser(request)
    
    
    public createUser(request: google.shopping.merchant.accounts.v1beta.ICreateUserRequest): Promise<google.shopping.merchant.accounts.v1beta.User>;

Calls CreateUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.icreateuserrequest)`   
CreateUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.User](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.user-class)>` | Promise  
  
### deleteUser(request, callback)
    
    
    public deleteUser(request: google.shopping.merchant.accounts.v1beta.IDeleteUserRequest, callback: google.shopping.merchant.accounts.v1beta.UserService.DeleteUserCallback): void;

Calls DeleteUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.ideleteuserrequest)`   
DeleteUserRequest message or plain object  
`callback` |  `[DeleteUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUser(request)
    
    
    public deleteUser(request: google.shopping.merchant.accounts.v1beta.IDeleteUserRequest): Promise<google.protobuf.Empty>;

Calls DeleteUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.ideleteuserrequest)`   
DeleteUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.protobuf.empty)>` | Promise  
  
### getUser(request, callback)
    
    
    public getUser(request: google.shopping.merchant.accounts.v1beta.IGetUserRequest, callback: google.shopping.merchant.accounts.v1beta.UserService.GetUserCallback): void;

Calls GetUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetuserrequest)`   
GetUserRequest message or plain object  
`callback` |  `[GetUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and User  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUser(request)
    
    
    public getUser(request: google.shopping.merchant.accounts.v1beta.IGetUserRequest): Promise<google.shopping.merchant.accounts.v1beta.User>;

Calls GetUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetuserrequest)`   
GetUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.User](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.user-class)>` | Promise  
  
### listUsers(request, callback)
    
    
    public listUsers(request: google.shopping.merchant.accounts.v1beta.IListUsersRequest, callback: google.shopping.merchant.accounts.v1beta.UserService.ListUsersCallback): void;

Calls ListUsers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.ilistusersrequest)`   
ListUsersRequest message or plain object  
`callback` |  `[ListUsersCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUsersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUsers(request)
    
    
    public listUsers(request: google.shopping.merchant.accounts.v1beta.IListUsersRequest): Promise<google.shopping.merchant.accounts.v1beta.ListUsersResponse>;

Calls ListUsers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.ilistusersrequest)`   
ListUsersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.ListUsersResponse](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.listusersresponse)>` | Promise  
  
### updateUser(request, callback)
    
    
    public updateUser(request: google.shopping.merchant.accounts.v1beta.IUpdateUserRequest, callback: google.shopping.merchant.accounts.v1beta.UserService.UpdateUserCallback): void;

Calls UpdateUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateuserrequest)`   
UpdateUserRequest message or plain object  
`callback` |  `[UpdateUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and User  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUser(request)
    
    
    public updateUser(request: google.shopping.merchant.accounts.v1beta.IUpdateUserRequest): Promise<google.shopping.merchant.accounts.v1beta.User>;

Calls UpdateUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateuserrequest)`   
UpdateUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.User](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.user-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
