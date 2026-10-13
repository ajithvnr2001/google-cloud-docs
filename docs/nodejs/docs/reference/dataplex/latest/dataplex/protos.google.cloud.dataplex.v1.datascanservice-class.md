---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanservice-class
title: Class protos.google.cloud.dataplex.v1.DataScanService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:41.810232+00:00
---

# Class protos.google.cloud.dataplex.v1.DataScanService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.DataScanService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a DataScanService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataplex.v1.DataScanService

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataScanService service.

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

### cancelDataScanJob(request, callback)
    
    
    public cancelDataScanJob(request: google.cloud.dataplex.v1.ICancelDataScanJobRequest, callback: google.cloud.dataplex.v1.DataScanService.CancelDataScanJobCallback): void;

Calls CancelDataScanJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelDataScanJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icanceldatascanjobrequest)`   
CancelDataScanJobRequest message or plain object  
`callback` |  `[CancelDataScanJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and CancelDataScanJobResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelDataScanJob(request)
    
    
    public cancelDataScanJob(request: google.cloud.dataplex.v1.ICancelDataScanJobRequest): Promise<google.cloud.dataplex.v1.CancelDataScanJobResponse>;

Calls CancelDataScanJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelDataScanJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icanceldatascanjobrequest)`   
CancelDataScanJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.CancelDataScanJobResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.canceldatascanjobresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataScanService;

Creates new DataScanService service using the specified rpc implementation.

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
`[DataScanService](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataScan(request, callback)
    
    
    public createDataScan(request: google.cloud.dataplex.v1.ICreateDataScanRequest, callback: google.cloud.dataplex.v1.DataScanService.CreateDataScanCallback): void;

Calls CreateDataScan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedatascanrequest)`   
CreateDataScanRequest message or plain object  
`callback` |  `[CreateDataScanCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataScan(request)
    
    
    public createDataScan(request: google.cloud.dataplex.v1.ICreateDataScanRequest): Promise<google.longrunning.Operation>;

Calls CreateDataScan.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedatascanrequest)`   
CreateDataScanRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataScan(request, callback)
    
    
    public deleteDataScan(request: google.cloud.dataplex.v1.IDeleteDataScanRequest, callback: google.cloud.dataplex.v1.DataScanService.DeleteDataScanCallback): void;

Calls DeleteDataScan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedatascanrequest)`   
DeleteDataScanRequest message or plain object  
`callback` |  `[DeleteDataScanCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataScan(request)
    
    
    public deleteDataScan(request: google.cloud.dataplex.v1.IDeleteDataScanRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataScan.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedatascanrequest)`   
DeleteDataScanRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### generateDataQualityRules(request, callback)
    
    
    public generateDataQualityRules(request: google.cloud.dataplex.v1.IGenerateDataQualityRulesRequest, callback: google.cloud.dataplex.v1.DataScanService.GenerateDataQualityRulesCallback): void;

Calls GenerateDataQualityRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateDataQualityRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igeneratedataqualityrulesrequest)`   
GenerateDataQualityRulesRequest message or plain object  
`callback` |  `[GenerateDataQualityRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateDataQualityRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateDataQualityRules(request)
    
    
    public generateDataQualityRules(request: google.cloud.dataplex.v1.IGenerateDataQualityRulesRequest): Promise<google.cloud.dataplex.v1.GenerateDataQualityRulesResponse>;

Calls GenerateDataQualityRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateDataQualityRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igeneratedataqualityrulesrequest)`   
GenerateDataQualityRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.GenerateDataQualityRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.generatedataqualityrulesresponse)>` | Promise  
  
### getDataScan(request, callback)
    
    
    public getDataScan(request: google.cloud.dataplex.v1.IGetDataScanRequest, callback: google.cloud.dataplex.v1.DataScanService.GetDataScanCallback): void;

Calls GetDataScan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdatascanrequest)`   
GetDataScanRequest message or plain object  
`callback` |  `[GetDataScanCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and DataScan  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataScan(request)
    
    
    public getDataScan(request: google.cloud.dataplex.v1.IGetDataScanRequest): Promise<google.cloud.dataplex.v1.DataScan>;

Calls GetDataScan.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdatascanrequest)`   
GetDataScanRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.DataScan](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascan-class)>` | Promise  
  
### getDataScanJob(request, callback)
    
    
    public getDataScanJob(request: google.cloud.dataplex.v1.IGetDataScanJobRequest, callback: google.cloud.dataplex.v1.DataScanService.GetDataScanJobCallback): void;

Calls GetDataScanJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataScanJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdatascanjobrequest)`   
GetDataScanJobRequest message or plain object  
`callback` |  `[GetDataScanJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and DataScanJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataScanJob(request)
    
    
    public getDataScanJob(request: google.cloud.dataplex.v1.IGetDataScanJobRequest): Promise<google.cloud.dataplex.v1.DataScanJob>;

Calls GetDataScanJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataScanJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdatascanjobrequest)`   
GetDataScanJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.DataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class)>` | Promise  
  
### listDataScanJobs(request, callback)
    
    
    public listDataScanJobs(request: google.cloud.dataplex.v1.IListDataScanJobsRequest, callback: google.cloud.dataplex.v1.DataScanService.ListDataScanJobsCallback): void;

Calls ListDataScanJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataScanJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdatascanjobsrequest)`   
ListDataScanJobsRequest message or plain object  
`callback` |  `[ListDataScanJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataScanJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataScanJobs(request)
    
    
    public listDataScanJobs(request: google.cloud.dataplex.v1.IListDataScanJobsRequest): Promise<google.cloud.dataplex.v1.ListDataScanJobsResponse>;

Calls ListDataScanJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataScanJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdatascanjobsrequest)`   
ListDataScanJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListDataScanJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listdatascanjobsresponse)>` | Promise  
  
### listDataScans(request, callback)
    
    
    public listDataScans(request: google.cloud.dataplex.v1.IListDataScansRequest, callback: google.cloud.dataplex.v1.DataScanService.ListDataScansCallback): void;

Calls ListDataScans.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataScansRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdatascansrequest)`   
ListDataScansRequest message or plain object  
`callback` |  `[ListDataScansCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataScansResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataScans(request)
    
    
    public listDataScans(request: google.cloud.dataplex.v1.IListDataScansRequest): Promise<google.cloud.dataplex.v1.ListDataScansResponse>;

Calls ListDataScans.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataScansRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdatascansrequest)`   
ListDataScansRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListDataScansResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listdatascansresponse)>` | Promise  
  
### runDataScan(request, callback)
    
    
    public runDataScan(request: google.cloud.dataplex.v1.IRunDataScanRequest, callback: google.cloud.dataplex.v1.DataScanService.RunDataScanCallback): void;

Calls RunDataScan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.irundatascanrequest)`   
RunDataScanRequest message or plain object  
`callback` |  `[RunDataScanCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and RunDataScanResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runDataScan(request)
    
    
    public runDataScan(request: google.cloud.dataplex.v1.IRunDataScanRequest): Promise<google.cloud.dataplex.v1.RunDataScanResponse>;

Calls RunDataScan.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.irundatascanrequest)`   
RunDataScanRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.RunDataScanResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.rundatascanresponse)>` | Promise  
  
### updateDataScan(request, callback)
    
    
    public updateDataScan(request: google.cloud.dataplex.v1.IUpdateDataScanRequest, callback: google.cloud.dataplex.v1.DataScanService.UpdateDataScanCallback): void;

Calls UpdateDataScan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedatascanrequest)`   
UpdateDataScanRequest message or plain object  
`callback` |  `[UpdateDataScanCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataScan(request)
    
    
    public updateDataScan(request: google.cloud.dataplex.v1.IUpdateDataScanRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataScan.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataScanRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedatascanrequest)`   
UpdateDataScanRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
