---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubdependencies-class
title: Class protos.google.cloud.apihub.v1.ApiHubDependencies (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:42.157931+00:00
---

# Class protos.google.cloud.apihub.v1.ApiHubDependencies (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubdependencies-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.ApiHubDependencies (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ApiHubDependencies

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.ApiHubDependencies

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ApiHubDependencies service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ApiHubDependencies;

Creates new ApiHubDependencies service using the specified rpc implementation.

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
`[ApiHubDependencies](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubdependencies-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDependency(request, callback)
    
    
    public createDependency(request: google.cloud.apihub.v1.ICreateDependencyRequest, callback: google.cloud.apihub.v1.ApiHubDependencies.CreateDependencyCallback): void;

Calls CreateDependency.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatedependencyrequest)`   
CreateDependencyRequest message or plain object  
`callback` |  `[CreateDependencyCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Dependency  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDependency(request)
    
    
    public createDependency(request: google.cloud.apihub.v1.ICreateDependencyRequest): Promise<google.cloud.apihub.v1.Dependency>;

Calls CreateDependency.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatedependencyrequest)`   
CreateDependencyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Dependency](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.dependency-class)>` | Promise  
  
### deleteDependency(request, callback)
    
    
    public deleteDependency(request: google.cloud.apihub.v1.IDeleteDependencyRequest, callback: google.cloud.apihub.v1.ApiHubDependencies.DeleteDependencyCallback): void;

Calls DeleteDependency.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletedependencyrequest)`   
DeleteDependencyRequest message or plain object  
`callback` |  `[DeleteDependencyCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDependency(request)
    
    
    public deleteDependency(request: google.cloud.apihub.v1.IDeleteDependencyRequest): Promise<google.protobuf.Empty>;

Calls DeleteDependency.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletedependencyrequest)`   
DeleteDependencyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### getDependency(request, callback)
    
    
    public getDependency(request: google.cloud.apihub.v1.IGetDependencyRequest, callback: google.cloud.apihub.v1.ApiHubDependencies.GetDependencyCallback): void;

Calls GetDependency.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdependencyrequest)`   
GetDependencyRequest message or plain object  
`callback` |  `[GetDependencyCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Dependency  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDependency(request)
    
    
    public getDependency(request: google.cloud.apihub.v1.IGetDependencyRequest): Promise<google.cloud.apihub.v1.Dependency>;

Calls GetDependency.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdependencyrequest)`   
GetDependencyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Dependency](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.dependency-class)>` | Promise  
  
### listDependencies(request, callback)
    
    
    public listDependencies(request: google.cloud.apihub.v1.IListDependenciesRequest, callback: google.cloud.apihub.v1.ApiHubDependencies.ListDependenciesCallback): void;

Calls ListDependencies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDependenciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdependenciesrequest)`   
ListDependenciesRequest message or plain object  
`callback` |  `[ListDependenciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDependenciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDependencies(request)
    
    
    public listDependencies(request: google.cloud.apihub.v1.IListDependenciesRequest): Promise<google.cloud.apihub.v1.ListDependenciesResponse>;

Calls ListDependencies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDependenciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdependenciesrequest)`   
ListDependenciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListDependenciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listdependenciesresponse)>` | Promise  
  
### updateDependency(request, callback)
    
    
    public updateDependency(request: google.cloud.apihub.v1.IUpdateDependencyRequest, callback: google.cloud.apihub.v1.ApiHubDependencies.UpdateDependencyCallback): void;

Calls UpdateDependency.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatedependencyrequest)`   
UpdateDependencyRequest message or plain object  
`callback` |  `[UpdateDependencyCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Dependency  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDependency(request)
    
    
    public updateDependency(request: google.cloud.apihub.v1.IUpdateDependencyRequest): Promise<google.cloud.apihub.v1.Dependency>;

Calls UpdateDependency.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDependencyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatedependencyrequest)`   
UpdateDependencyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Dependency](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.dependency-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
