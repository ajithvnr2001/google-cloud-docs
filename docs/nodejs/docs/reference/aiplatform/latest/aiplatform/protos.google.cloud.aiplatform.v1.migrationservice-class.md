---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.migrationservice-class
title: Class protos.google.cloud.aiplatform.v1.MigrationService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:02.134142+00:00
---

# Class protos.google.cloud.aiplatform.v1.MigrationService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.migrationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1.MigrationService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a MigrationService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1.MigrationService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

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

### batchMigrateResources(request, callback)
    
    
    public batchMigrateResources(request: google.cloud.aiplatform.v1.IBatchMigrateResourcesRequest, callback: google.cloud.aiplatform.v1.MigrationService.BatchMigrateResourcesCallback): void;

Calls BatchMigrateResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchMigrateResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ibatchmigrateresourcesrequest)`   
BatchMigrateResourcesRequest message or plain object  
`callback` |  `[BatchMigrateResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchMigrateResources(request)
    
    
    public batchMigrateResources(request: google.cloud.aiplatform.v1.IBatchMigrateResourcesRequest): Promise<google.longrunning.Operation>;

Calls BatchMigrateResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchMigrateResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ibatchmigrateresourcesrequest)`   
BatchMigrateResourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
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
`[MigrationService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.migrationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### searchMigratableResources(request, callback)
    
    
    public searchMigratableResources(request: google.cloud.aiplatform.v1.ISearchMigratableResourcesRequest, callback: google.cloud.aiplatform.v1.MigrationService.SearchMigratableResourcesCallback): void;

Calls SearchMigratableResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchMigratableResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.isearchmigratableresourcesrequest)`   
SearchMigratableResourcesRequest message or plain object  
`callback` |  `[SearchMigratableResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchMigratableResourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchMigratableResources(request)
    
    
    public searchMigratableResources(request: google.cloud.aiplatform.v1.ISearchMigratableResourcesRequest): Promise<google.cloud.aiplatform.v1.SearchMigratableResourcesResponse>;

Calls SearchMigratableResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchMigratableResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.isearchmigratableresourcesrequest)`   
SearchMigratableResourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.SearchMigratableResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.searchmigratableresourcesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
