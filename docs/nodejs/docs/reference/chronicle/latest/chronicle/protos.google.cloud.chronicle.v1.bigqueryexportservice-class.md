---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bigqueryexportservice-class
title: Class protos.google.cloud.chronicle.v1.BigQueryExportService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:50:58.569692+00:00
---

# Class protos.google.cloud.chronicle.v1.BigQueryExportService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bigqueryexportservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.BigQueryExportService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a BigQueryExportService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.BigQueryExportService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BigQueryExportService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BigQueryExportService;

Creates new BigQueryExportService service using the specified rpc implementation.

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
`[BigQueryExportService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bigqueryexportservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getBigQueryExport(request, callback)
    
    
    public getBigQueryExport(request: google.cloud.chronicle.v1.IGetBigQueryExportRequest, callback: google.cloud.chronicle.v1.BigQueryExportService.GetBigQueryExportCallback): void;

Calls GetBigQueryExport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBigQueryExportRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetbigqueryexportrequest)`   
GetBigQueryExportRequest message or plain object  
`callback` |  `[GetBigQueryExportCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BigQueryExport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBigQueryExport(request)
    
    
    public getBigQueryExport(request: google.cloud.chronicle.v1.IGetBigQueryExportRequest): Promise<google.cloud.chronicle.v1.BigQueryExport>;

Calls GetBigQueryExport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBigQueryExportRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetbigqueryexportrequest)`   
GetBigQueryExportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BigQueryExport](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bigqueryexport)>` | Promise  
  
### provisionBigQueryExport(request, callback)
    
    
    public provisionBigQueryExport(request: google.cloud.chronicle.v1.IProvisionBigQueryExportRequest, callback: google.cloud.chronicle.v1.BigQueryExportService.ProvisionBigQueryExportCallback): void;

Calls ProvisionBigQueryExport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionBigQueryExportRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iprovisionbigqueryexportrequest)`   
ProvisionBigQueryExportRequest message or plain object  
`callback` |  `[ProvisionBigQueryExportCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BigQueryExport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### provisionBigQueryExport(request)
    
    
    public provisionBigQueryExport(request: google.cloud.chronicle.v1.IProvisionBigQueryExportRequest): Promise<google.cloud.chronicle.v1.BigQueryExport>;

Calls ProvisionBigQueryExport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IProvisionBigQueryExportRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iprovisionbigqueryexportrequest)`   
ProvisionBigQueryExportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BigQueryExport](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bigqueryexport)>` | Promise  
  
### updateBigQueryExport(request, callback)
    
    
    public updateBigQueryExport(request: google.cloud.chronicle.v1.IUpdateBigQueryExportRequest, callback: google.cloud.chronicle.v1.BigQueryExportService.UpdateBigQueryExportCallback): void;

Calls UpdateBigQueryExport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBigQueryExportRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatebigqueryexportrequest)`   
UpdateBigQueryExportRequest message or plain object  
`callback` |  `[UpdateBigQueryExportCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BigQueryExport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBigQueryExport(request)
    
    
    public updateBigQueryExport(request: google.cloud.chronicle.v1.IUpdateBigQueryExportRequest): Promise<google.cloud.chronicle.v1.BigQueryExport>;

Calls UpdateBigQueryExport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBigQueryExportRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatebigqueryexportrequest)`   
UpdateBigQueryExportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BigQueryExport](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bigqueryexport)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
