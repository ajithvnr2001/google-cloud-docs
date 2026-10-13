---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistdirectlicenseservice-class
title: Class protos.google.ads.datamanager.v1.UserListDirectLicenseService (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:29.247279+00:00
---

# Class protos.google.ads.datamanager.v1.UserListDirectLicenseService (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistdirectlicenseservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.UserListDirectLicenseService (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a UserListDirectLicenseService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.datamanager.v1.UserListDirectLicenseService

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new UserListDirectLicenseService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): UserListDirectLicenseService;

Creates new UserListDirectLicenseService service using the specified rpc implementation.

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
`[UserListDirectLicenseService](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistdirectlicenseservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createUserListDirectLicense(request, callback)
    
    
    public createUserListDirectLicense(request: google.ads.datamanager.v1.ICreateUserListDirectLicenseRequest, callback: google.ads.datamanager.v1.UserListDirectLicenseService.CreateUserListDirectLicenseCallback): void;

Calls CreateUserListDirectLicense.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserListDirectLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreateuserlistdirectlicenserequest)`   
CreateUserListDirectLicenseRequest message or plain object  
`callback` |  `[CreateUserListDirectLicenseCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserListDirectLicense  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserListDirectLicense(request)
    
    
    public createUserListDirectLicense(request: google.ads.datamanager.v1.ICreateUserListDirectLicenseRequest): Promise<google.ads.datamanager.v1.UserListDirectLicense>;

Calls CreateUserListDirectLicense.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserListDirectLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreateuserlistdirectlicenserequest)`   
CreateUserListDirectLicenseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserListDirectLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistdirectlicense)>` | Promise  
  
### getUserListDirectLicense(request, callback)
    
    
    public getUserListDirectLicense(request: google.ads.datamanager.v1.IGetUserListDirectLicenseRequest, callback: google.ads.datamanager.v1.UserListDirectLicenseService.GetUserListDirectLicenseCallback): void;

Calls GetUserListDirectLicense.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserListDirectLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.igetuserlistdirectlicenserequest)`   
GetUserListDirectLicenseRequest message or plain object  
`callback` |  `[GetUserListDirectLicenseCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserListDirectLicense  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserListDirectLicense(request)
    
    
    public getUserListDirectLicense(request: google.ads.datamanager.v1.IGetUserListDirectLicenseRequest): Promise<google.ads.datamanager.v1.UserListDirectLicense>;

Calls GetUserListDirectLicense.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUserListDirectLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.igetuserlistdirectlicenserequest)`   
GetUserListDirectLicenseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserListDirectLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistdirectlicense)>` | Promise  
  
### listUserListDirectLicenses(request, callback)
    
    
    public listUserListDirectLicenses(request: google.ads.datamanager.v1.IListUserListDirectLicensesRequest, callback: google.ads.datamanager.v1.UserListDirectLicenseService.ListUserListDirectLicensesCallback): void;

Calls ListUserListDirectLicenses.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserListDirectLicensesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistdirectlicensesrequest)`   
ListUserListDirectLicensesRequest message or plain object  
`callback` |  `[ListUserListDirectLicensesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUserListDirectLicensesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserListDirectLicenses(request)
    
    
    public listUserListDirectLicenses(request: google.ads.datamanager.v1.IListUserListDirectLicensesRequest): Promise<google.ads.datamanager.v1.ListUserListDirectLicensesResponse>;

Calls ListUserListDirectLicenses.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUserListDirectLicensesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistdirectlicensesrequest)`   
ListUserListDirectLicensesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.ListUserListDirectLicensesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.listuserlistdirectlicensesresponse)>` | Promise  
  
### updateUserListDirectLicense(request, callback)
    
    
    public updateUserListDirectLicense(request: google.ads.datamanager.v1.IUpdateUserListDirectLicenseRequest, callback: google.ads.datamanager.v1.UserListDirectLicenseService.UpdateUserListDirectLicenseCallback): void;

Calls UpdateUserListDirectLicense.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserListDirectLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iupdateuserlistdirectlicenserequest)`   
UpdateUserListDirectLicenseRequest message or plain object  
`callback` |  `[UpdateUserListDirectLicenseCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserListDirectLicense  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUserListDirectLicense(request)
    
    
    public updateUserListDirectLicense(request: google.ads.datamanager.v1.IUpdateUserListDirectLicenseRequest): Promise<google.ads.datamanager.v1.UserListDirectLicense>;

Calls UpdateUserListDirectLicense.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserListDirectLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iupdateuserlistdirectlicenserequest)`   
UpdateUserListDirectLicenseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserListDirectLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistdirectlicense)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
