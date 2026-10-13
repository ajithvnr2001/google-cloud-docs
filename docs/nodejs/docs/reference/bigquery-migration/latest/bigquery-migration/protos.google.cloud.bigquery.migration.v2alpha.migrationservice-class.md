---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.migrationservice-class
title: Class protos.google.cloud.bigquery.migration.v2alpha.MigrationService (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:24.644637+00:00
---

# Class protos.google.cloud.bigquery.migration.v2alpha.MigrationService (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.migrationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.migration.v2alpha.MigrationService (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.2.0  1.0.1  0.2.0  0.1.0 

Represents a MigrationService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.bigquery.migration.v2alpha.MigrationService

## Package

[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MigrationService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MigrationService;

Creates new MigrationService service using the specified rpc implementation.

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
`[MigrationService](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.migrationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createMigrationWorkflow(request, callback)
    
    
    public createMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest, callback: google.cloud.bigquery.migration.v2alpha.MigrationService.CreateMigrationWorkflowCallback): void;

Calls CreateMigrationWorkflow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest)`   
CreateMigrationWorkflowRequest message or plain object  
`callback` |  `[CreateMigrationWorkflowCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)`   
Node-style callback called with the error, if any, and MigrationWorkflow  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMigrationWorkflow(request)
    
    
    public createMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest): Promise<google.cloud.bigquery.migration.v2alpha.MigrationWorkflow>;

Calls CreateMigrationWorkflow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest)`   
CreateMigrationWorkflowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.migration.v2alpha.MigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.migrationworkflow-class)>` | Promise  
  
### deleteMigrationWorkflow(request, callback)
    
    
    public deleteMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest, callback: google.cloud.bigquery.migration.v2alpha.MigrationService.DeleteMigrationWorkflowCallback): void;

Calls DeleteMigrationWorkflow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest)`   
DeleteMigrationWorkflowRequest message or plain object  
`callback` |  `[DeleteMigrationWorkflowCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMigrationWorkflow(request)
    
    
    public deleteMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest): Promise<google.protobuf.Empty>;

Calls DeleteMigrationWorkflow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest)`   
DeleteMigrationWorkflowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.empty)>` | Promise  
  
### getMigrationSubtask(request, callback)
    
    
    public getMigrationSubtask(request: google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest, callback: google.cloud.bigquery.migration.v2alpha.MigrationService.GetMigrationSubtaskCallback): void;

Calls GetMigrationSubtask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest)`   
GetMigrationSubtaskRequest message or plain object  
`callback` |  `[GetMigrationSubtaskCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)`   
Node-style callback called with the error, if any, and MigrationSubtask  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMigrationSubtask(request)
    
    
    public getMigrationSubtask(request: google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest): Promise<google.cloud.bigquery.migration.v2alpha.MigrationSubtask>;

Calls GetMigrationSubtask.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest)`   
GetMigrationSubtaskRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.migration.v2alpha.MigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.migrationsubtask-class)>` | Promise  
  
### getMigrationWorkflow(request, callback)
    
    
    public getMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest, callback: google.cloud.bigquery.migration.v2alpha.MigrationService.GetMigrationWorkflowCallback): void;

Calls GetMigrationWorkflow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest)`   
GetMigrationWorkflowRequest message or plain object  
`callback` |  `[GetMigrationWorkflowCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)`   
Node-style callback called with the error, if any, and MigrationWorkflow  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMigrationWorkflow(request)
    
    
    public getMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest): Promise<google.cloud.bigquery.migration.v2alpha.MigrationWorkflow>;

Calls GetMigrationWorkflow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest)`   
GetMigrationWorkflowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.migration.v2alpha.MigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.migrationworkflow-class)>` | Promise  
  
### listMigrationSubtasks(request, callback)
    
    
    public listMigrationSubtasks(request: google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, callback: google.cloud.bigquery.migration.v2alpha.MigrationService.ListMigrationSubtasksCallback): void;

Calls ListMigrationSubtasks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest)`   
ListMigrationSubtasksRequest message or plain object  
`callback` |  `[ListMigrationSubtasksCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMigrationSubtasksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMigrationSubtasks(request)
    
    
    public listMigrationSubtasks(request: google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest): Promise<google.cloud.bigquery.migration.v2alpha.ListMigrationSubtasksResponse>;

Calls ListMigrationSubtasks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest)`   
ListMigrationSubtasksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.migration.v2alpha.ListMigrationSubtasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.listmigrationsubtasksresponse)>` | Promise  
  
### listMigrationWorkflows(request, callback)
    
    
    public listMigrationWorkflows(request: google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, callback: google.cloud.bigquery.migration.v2alpha.MigrationService.ListMigrationWorkflowsCallback): void;

Calls ListMigrationWorkflows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest)`   
ListMigrationWorkflowsRequest message or plain object  
`callback` |  `[ListMigrationWorkflowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMigrationWorkflowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMigrationWorkflows(request)
    
    
    public listMigrationWorkflows(request: google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest): Promise<google.cloud.bigquery.migration.v2alpha.ListMigrationWorkflowsResponse>;

Calls ListMigrationWorkflows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest)`   
ListMigrationWorkflowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.migration.v2alpha.ListMigrationWorkflowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.listmigrationworkflowsresponse)>` | Promise  
  
### startMigrationWorkflow(request, callback)
    
    
    public startMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest, callback: google.cloud.bigquery.migration.v2alpha.MigrationService.StartMigrationWorkflowCallback): void;

Calls StartMigrationWorkflow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest)`   
StartMigrationWorkflowRequest message or plain object  
`callback` |  `[StartMigrationWorkflowCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startMigrationWorkflow(request)
    
    
    public startMigrationWorkflow(request: google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest): Promise<google.protobuf.Empty>;

Calls StartMigrationWorkflow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest)`   
StartMigrationWorkflowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.empty)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
