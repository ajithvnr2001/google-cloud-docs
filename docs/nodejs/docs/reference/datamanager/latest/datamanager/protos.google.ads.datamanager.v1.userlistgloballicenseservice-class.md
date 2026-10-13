---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicenseservice-class
title: Class protos.google.ads.datamanager.v1.UserListGlobalLicenseService (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:41.682337+00:00
---

# Class protos.google.ads.datamanager.v1.UserListGlobalLicenseService (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicenseservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.UserListGlobalLicenseService (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a UserListGlobalLicenseService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.datamanager.v1.UserListGlobalLicenseService

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new UserListGlobalLicenseService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): UserListGlobalLicenseService;

Creates new UserListGlobalLicenseService service using the specified rpc implementation.

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
`[UserListGlobalLicenseService](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicenseservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createUserListGlobalLicense(request, callback)
    
    
    public createUserListGlobalLicense(request: google.ads.datamanager.v1.ICreateUserListGlobalLicenseRequest, callback: google.ads.datamanager.v1.UserListGlobalLicenseService.CreateUserListGlobalLicenseCallback): void;

Calls CreateUserListGlobalLicense.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserListGlobalLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreateuserlistgloballicenserequest)`   
CreateUserListGlobalLicenseRequest message or plain object  
`callback` |  `[CreateUserListGlobalLicenseCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserListGlobalLicense  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserListGlobalLicense(request)
    
    
    public createUserListGlobalLicense(request: google.ads.datamanager.v1.ICreateUserListGlobalLicenseRequest): Promise<google.ads.datamanager.v1.UserListGlobalLicense>;

Calls CreateUserListGlobalLicense.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserListGlobalLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreateuserlistgloballicenserequest)`   
CreateUserListGlobalLicenseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)>` | Promise  
  
### getUserListGlobalLicense(request, callback)
    
    
    public getUserListGlobalLicense(request: google.ads.datamanager.v1.IGetUserListGlobalLicenseRequest, callback: google.ads.datamanager.v1.UserListGlobalLicenseService.GetUserListGlobalLicenseCallback): void;

Calls GetUserListGlobalLicense.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserListGlobalLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.igetuserlistgloballicenserequest)`   
GetUserListGlobalLicenseRequest message or plain object  
`callback` |  `[GetUserListGlobalLicenseCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserListGlobalLicense  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserListGlobalLicense(request)
    
    
    public getUserListGlobalLicense(request: google.ads.datamanager.v1.IGetUserListGlobalLicenseRequest): Promise<google.ads.datamanager.v1.UserListGlobalLicense>;

Calls GetUserListGlobalLicense.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUserListGlobalLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.igetuserlistgloballicenserequest)`   
GetUserListGlobalLicenseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)>` | Promise  
  
### listUserListGlobalLicenseCustomerInfos(request, callback)
    
    
    public listUserListGlobalLicenseCustomerInfos(request: google.ads.datamanager.v1.IListUserListGlobalLicenseCustomerInfosRequest, callback: google.ads.datamanager.v1.UserListGlobalLicenseService.ListUserListGlobalLicenseCustomerInfosCallback): void;

Calls ListUserListGlobalLicenseCustomerInfos.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserListGlobalLicenseCustomerInfosRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistgloballicensecustomerinfosrequest)`   
ListUserListGlobalLicenseCustomerInfosRequest message or plain object  
`callback` |  `[ListUserListGlobalLicenseCustomerInfosCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUserListGlobalLicenseCustomerInfosResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserListGlobalLicenseCustomerInfos(request)
    
    
    public listUserListGlobalLicenseCustomerInfos(request: google.ads.datamanager.v1.IListUserListGlobalLicenseCustomerInfosRequest): Promise<google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosResponse>;

Calls ListUserListGlobalLicenseCustomerInfos.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUserListGlobalLicenseCustomerInfosRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistgloballicensecustomerinfosrequest)`   
ListUserListGlobalLicenseCustomerInfosRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.listuserlistgloballicensecustomerinfosresponse)>` | Promise  
  
### listUserListGlobalLicenses(request, callback)
    
    
    public listUserListGlobalLicenses(request: google.ads.datamanager.v1.IListUserListGlobalLicensesRequest, callback: google.ads.datamanager.v1.UserListGlobalLicenseService.ListUserListGlobalLicensesCallback): void;

Calls ListUserListGlobalLicenses.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserListGlobalLicensesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistgloballicensesrequest)`   
ListUserListGlobalLicensesRequest message or plain object  
`callback` |  `[ListUserListGlobalLicensesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUserListGlobalLicensesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserListGlobalLicenses(request)
    
    
    public listUserListGlobalLicenses(request: google.ads.datamanager.v1.IListUserListGlobalLicensesRequest): Promise<google.ads.datamanager.v1.ListUserListGlobalLicensesResponse>;

Calls ListUserListGlobalLicenses.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUserListGlobalLicensesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ilistuserlistgloballicensesrequest)`   
ListUserListGlobalLicensesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.ListUserListGlobalLicensesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.listuserlistgloballicensesresponse)>` | Promise  
  
### updateUserListGlobalLicense(request, callback)
    
    
    public updateUserListGlobalLicense(request: google.ads.datamanager.v1.IUpdateUserListGlobalLicenseRequest, callback: google.ads.datamanager.v1.UserListGlobalLicenseService.UpdateUserListGlobalLicenseCallback): void;

Calls UpdateUserListGlobalLicense.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserListGlobalLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iupdateuserlistgloballicenserequest)`   
UpdateUserListGlobalLicenseRequest message or plain object  
`callback` |  `[UpdateUserListGlobalLicenseCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and UserListGlobalLicense  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUserListGlobalLicense(request)
    
    
    public updateUserListGlobalLicense(request: google.ads.datamanager.v1.IUpdateUserListGlobalLicenseRequest): Promise<google.ads.datamanager.v1.UserListGlobalLicense>;

Calls UpdateUserListGlobalLicense.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserListGlobalLicenseRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iupdateuserlistgloballicenserequest)`   
UpdateUserListGlobalLicenseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
