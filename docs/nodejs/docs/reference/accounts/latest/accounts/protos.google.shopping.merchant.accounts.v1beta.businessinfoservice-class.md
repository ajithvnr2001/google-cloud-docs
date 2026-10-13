---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.businessinfoservice-class
title: Class protos.google.shopping.merchant.accounts.v1beta.BusinessInfoService (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:52.901644+00:00
---

# Class protos.google.shopping.merchant.accounts.v1beta.BusinessInfoService (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.businessinfoservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.accounts.v1beta.BusinessInfoService (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Represents a BusinessInfoService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.accounts.v1beta.BusinessInfoService

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BusinessInfoService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BusinessInfoService;

Creates new BusinessInfoService service using the specified rpc implementation.

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
`[BusinessInfoService](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.businessinfoservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getBusinessInfo(request, callback)
    
    
    public getBusinessInfo(request: google.shopping.merchant.accounts.v1beta.IGetBusinessInfoRequest, callback: google.shopping.merchant.accounts.v1beta.BusinessInfoService.GetBusinessInfoCallback): void;

Calls GetBusinessInfo.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBusinessInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetbusinessinforequest)`   
GetBusinessInfoRequest message or plain object  
`callback` |  `[GetBusinessInfoCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and BusinessInfo  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBusinessInfo(request)
    
    
    public getBusinessInfo(request: google.shopping.merchant.accounts.v1beta.IGetBusinessInfoRequest): Promise<google.shopping.merchant.accounts.v1beta.BusinessInfo>;

Calls GetBusinessInfo.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBusinessInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetbusinessinforequest)`   
GetBusinessInfoRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.BusinessInfo](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.businessinfo)>` | Promise  
  
### updateBusinessInfo(request, callback)
    
    
    public updateBusinessInfo(request: google.shopping.merchant.accounts.v1beta.IUpdateBusinessInfoRequest, callback: google.shopping.merchant.accounts.v1beta.BusinessInfoService.UpdateBusinessInfoCallback): void;

Calls UpdateBusinessInfo.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBusinessInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdatebusinessinforequest)`   
UpdateBusinessInfoRequest message or plain object  
`callback` |  `[UpdateBusinessInfoCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and BusinessInfo  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBusinessInfo(request)
    
    
    public updateBusinessInfo(request: google.shopping.merchant.accounts.v1beta.IUpdateBusinessInfoRequest): Promise<google.shopping.merchant.accounts.v1beta.BusinessInfo>;

Calls UpdateBusinessInfo.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBusinessInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdatebusinessinforequest)`   
UpdateBusinessInfoRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.BusinessInfo](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.businessinfo)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
