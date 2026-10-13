---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.applicationservice-class
title: Class protos.google.ads.admanager.v1.ApplicationService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:47.284101+00:00
---

# Class protos.google.ads.admanager.v1.ApplicationService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.applicationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.ApplicationService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an ApplicationService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.ApplicationService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ApplicationService service.

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

### batchArchiveApplications(request, callback)
    
    
    public batchArchiveApplications(request: google.ads.admanager.v1.IBatchArchiveApplicationsRequest, callback: google.ads.admanager.v1.ApplicationService.BatchArchiveApplicationsCallback): void;

Calls BatchArchiveApplications.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchArchiveApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatcharchiveapplicationsrequest)`   
BatchArchiveApplicationsRequest message or plain object  
`callback` |  `[BatchArchiveApplicationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchArchiveApplicationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchArchiveApplications(request)
    
    
    public batchArchiveApplications(request: google.ads.admanager.v1.IBatchArchiveApplicationsRequest): Promise<google.ads.admanager.v1.BatchArchiveApplicationsResponse>;

Calls BatchArchiveApplications.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchArchiveApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatcharchiveapplicationsrequest)`   
BatchArchiveApplicationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchArchiveApplicationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batcharchiveapplicationsresponse)>` | Promise  
  
### batchCreateApplications(request, callback)
    
    
    public batchCreateApplications(request: google.ads.admanager.v1.IBatchCreateApplicationsRequest, callback: google.ads.admanager.v1.ApplicationService.BatchCreateApplicationsCallback): void;

Calls BatchCreateApplications.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateapplicationsrequest)`   
BatchCreateApplicationsRequest message or plain object  
`callback` |  `[BatchCreateApplicationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateApplicationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateApplications(request)
    
    
    public batchCreateApplications(request: google.ads.admanager.v1.IBatchCreateApplicationsRequest): Promise<google.ads.admanager.v1.BatchCreateApplicationsResponse>;

Calls BatchCreateApplications.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateapplicationsrequest)`   
BatchCreateApplicationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateApplicationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreateapplicationsresponse)>` | Promise  
  
### batchUnarchiveApplications(request, callback)
    
    
    public batchUnarchiveApplications(request: google.ads.admanager.v1.IBatchUnarchiveApplicationsRequest, callback: google.ads.admanager.v1.ApplicationService.BatchUnarchiveApplicationsCallback): void;

Calls BatchUnarchiveApplications.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUnarchiveApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchunarchiveapplicationsrequest)`   
BatchUnarchiveApplicationsRequest message or plain object  
`callback` |  `[BatchUnarchiveApplicationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUnarchiveApplicationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUnarchiveApplications(request)
    
    
    public batchUnarchiveApplications(request: google.ads.admanager.v1.IBatchUnarchiveApplicationsRequest): Promise<google.ads.admanager.v1.BatchUnarchiveApplicationsResponse>;

Calls BatchUnarchiveApplications.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUnarchiveApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchunarchiveapplicationsrequest)`   
BatchUnarchiveApplicationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUnarchiveApplicationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchunarchiveapplicationsresponse)>` | Promise  
  
### batchUpdateApplications(request, callback)
    
    
    public batchUpdateApplications(request: google.ads.admanager.v1.IBatchUpdateApplicationsRequest, callback: google.ads.admanager.v1.ApplicationService.BatchUpdateApplicationsCallback): void;

Calls BatchUpdateApplications.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateapplicationsrequest)`   
BatchUpdateApplicationsRequest message or plain object  
`callback` |  `[BatchUpdateApplicationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateApplicationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateApplications(request)
    
    
    public batchUpdateApplications(request: google.ads.admanager.v1.IBatchUpdateApplicationsRequest): Promise<google.ads.admanager.v1.BatchUpdateApplicationsResponse>;

Calls BatchUpdateApplications.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateapplicationsrequest)`   
BatchUpdateApplicationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUpdateApplicationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchupdateapplicationsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ApplicationService;

Creates new ApplicationService service using the specified rpc implementation.

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
`[ApplicationService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.applicationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createApplication(request, callback)
    
    
    public createApplication(request: google.ads.admanager.v1.ICreateApplicationRequest, callback: google.ads.admanager.v1.ApplicationService.CreateApplicationCallback): void;

Calls CreateApplication.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateapplicationrequest)`   
CreateApplicationRequest message or plain object  
`callback` |  `[CreateApplicationCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Application  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createApplication(request)
    
    
    public createApplication(request: google.ads.admanager.v1.ICreateApplicationRequest): Promise<google.ads.admanager.v1.Application>;

Calls CreateApplication.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateapplicationrequest)`   
CreateApplicationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)>` | Promise  
  
### getApplication(request, callback)
    
    
    public getApplication(request: google.ads.admanager.v1.IGetApplicationRequest, callback: google.ads.admanager.v1.ApplicationService.GetApplicationCallback): void;

Calls GetApplication.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetapplicationrequest)`   
GetApplicationRequest message or plain object  
`callback` |  `[GetApplicationCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Application  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getApplication(request)
    
    
    public getApplication(request: google.ads.admanager.v1.IGetApplicationRequest): Promise<google.ads.admanager.v1.Application>;

Calls GetApplication.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetapplicationrequest)`   
GetApplicationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)>` | Promise  
  
### listApplications(request, callback)
    
    
    public listApplications(request: google.ads.admanager.v1.IListApplicationsRequest, callback: google.ads.admanager.v1.ApplicationService.ListApplicationsCallback): void;

Calls ListApplications.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistapplicationsrequest)`   
ListApplicationsRequest message or plain object  
`callback` |  `[ListApplicationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListApplicationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listApplications(request)
    
    
    public listApplications(request: google.ads.admanager.v1.IListApplicationsRequest): Promise<google.ads.admanager.v1.ListApplicationsResponse>;

Calls ListApplications.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListApplicationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistapplicationsrequest)`   
ListApplicationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListApplicationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listapplicationsresponse)>` | Promise  
  
### updateApplication(request, callback)
    
    
    public updateApplication(request: google.ads.admanager.v1.IUpdateApplicationRequest, callback: google.ads.admanager.v1.ApplicationService.UpdateApplicationCallback): void;

Calls UpdateApplication.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateapplicationrequest)`   
UpdateApplicationRequest message or plain object  
`callback` |  `[UpdateApplicationCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Application  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateApplication(request)
    
    
    public updateApplication(request: google.ads.admanager.v1.IUpdateApplicationRequest): Promise<google.ads.admanager.v1.Application>;

Calls UpdateApplication.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateapplicationrequest)`   
UpdateApplicationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
