---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sqldatabasesservice-class
title: Class protos.google.cloud.sql.v1.SqlDatabasesService (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:31.887783+00:00
---

# Class protos.google.cloud.sql.v1.SqlDatabasesService (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sqldatabasesservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.sql.v1.SqlDatabasesService (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Represents a SqlDatabasesService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.sql.v1.SqlDatabasesService

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SqlDatabasesService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SqlDatabasesService;

Creates new SqlDatabasesService service using the specified rpc implementation.

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
`[SqlDatabasesService](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sqldatabasesservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.sql.v1.ISqlDatabasesDeleteRequest, callback: google.cloud.sql.v1.SqlDatabasesService.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesDeleteRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesdeleterequest)`   
SqlDatabasesDeleteRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.sql.v1.ISqlDatabasesDeleteRequest): Promise<google.cloud.sql.v1.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesDeleteRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesdeleterequest)`   
SqlDatabasesDeleteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.sql.v1.ISqlDatabasesGetRequest, callback: google.cloud.sql.v1.SqlDatabasesService.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesGetRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesgetrequest)`   
SqlDatabasesGetRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and Database  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.sql.v1.ISqlDatabasesGetRequest): Promise<google.cloud.sql.v1.Database>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesGetRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesgetrequest)`   
SqlDatabasesGetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.Database](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.database)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.sql.v1.ISqlDatabasesInsertRequest, callback: google.cloud.sql.v1.SqlDatabasesService.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesInsertRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesinsertrequest)`   
SqlDatabasesInsertRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.sql.v1.ISqlDatabasesInsertRequest): Promise<google.cloud.sql.v1.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesInsertRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesinsertrequest)`   
SqlDatabasesInsertRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.sql.v1.ISqlDatabasesListRequest, callback: google.cloud.sql.v1.SqlDatabasesService.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesListRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabaseslistrequest)`   
SqlDatabasesListRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and DatabasesListResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.sql.v1.ISqlDatabasesListRequest): Promise<google.cloud.sql.v1.DatabasesListResponse>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesListRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabaseslistrequest)`   
SqlDatabasesListRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.DatabasesListResponse](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.databaseslistresponse)>` | Promise  
  
### patch(request, callback)
    
    
    public patch(request: google.cloud.sql.v1.ISqlDatabasesUpdateRequest, callback: google.cloud.sql.v1.SqlDatabasesService.PatchCallback): void;

Calls Patch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesupdaterequest)`   
SqlDatabasesUpdateRequest message or plain object  
`callback` |  `[PatchCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patch(request)
    
    
    public patch(request: google.cloud.sql.v1.ISqlDatabasesUpdateRequest): Promise<google.cloud.sql.v1.Operation>;

Calls Patch.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesupdaterequest)`   
SqlDatabasesUpdateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.operation-class)>` | Promise  
  
### update(request, callback)
    
    
    public update(request: google.cloud.sql.v1.ISqlDatabasesUpdateRequest, callback: google.cloud.sql.v1.SqlDatabasesService.UpdateCallback): void;

Calls Update.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesupdaterequest)`   
SqlDatabasesUpdateRequest message or plain object  
`callback` |  `[UpdateCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### update(request)
    
    
    public update(request: google.cloud.sql.v1.ISqlDatabasesUpdateRequest): Promise<google.cloud.sql.v1.Operation>;

Calls Update.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlDatabasesUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqldatabasesupdaterequest)`   
SqlDatabasesUpdateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.operation-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
