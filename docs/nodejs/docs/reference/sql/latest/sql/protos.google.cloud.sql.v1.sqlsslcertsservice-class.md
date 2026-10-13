---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sqlsslcertsservice-class
title: Class protos.google.cloud.sql.v1.SqlSslCertsService (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:14.029185+00:00
---

# Class protos.google.cloud.sql.v1.SqlSslCertsService (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sqlsslcertsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.sql.v1.SqlSslCertsService (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Represents a SqlSslCertsService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.sql.v1.SqlSslCertsService

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SqlSslCertsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SqlSslCertsService;

Creates new SqlSslCertsService service using the specified rpc implementation.

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
`[SqlSslCertsService](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sqlsslcertsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.sql.v1.ISqlSslCertsDeleteRequest, callback: google.cloud.sql.v1.SqlSslCertsService.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsDeleteRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertsdeleterequest)`   
SqlSslCertsDeleteRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.sql.v1.ISqlSslCertsDeleteRequest): Promise<google.cloud.sql.v1.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsDeleteRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertsdeleterequest)`   
SqlSslCertsDeleteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.sql.v1.ISqlSslCertsGetRequest, callback: google.cloud.sql.v1.SqlSslCertsService.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsGetRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertsgetrequest)`   
SqlSslCertsGetRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and SslCert  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.sql.v1.ISqlSslCertsGetRequest): Promise<google.cloud.sql.v1.SslCert>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsGetRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertsgetrequest)`   
SqlSslCertsGetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.SslCert](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sslcert)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.sql.v1.ISqlSslCertsInsertRequest, callback: google.cloud.sql.v1.SqlSslCertsService.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsInsertRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertsinsertrequest)`   
SqlSslCertsInsertRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and SslCertsInsertResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.sql.v1.ISqlSslCertsInsertRequest): Promise<google.cloud.sql.v1.SslCertsInsertResponse>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsInsertRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertsinsertrequest)`   
SqlSslCertsInsertRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.SslCertsInsertResponse](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sslcertsinsertresponse)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.sql.v1.ISqlSslCertsListRequest, callback: google.cloud.sql.v1.SqlSslCertsService.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsListRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertslistrequest)`   
SqlSslCertsListRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)`   
Node-style callback called with the error, if any, and SslCertsListResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.sql.v1.ISqlSslCertsListRequest): Promise<google.cloud.sql.v1.SslCertsListResponse>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISqlSslCertsListRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.isqlsslcertslistrequest)`   
SqlSslCertsListRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.sql.v1.SslCertsListResponse](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.sslcertslistresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
