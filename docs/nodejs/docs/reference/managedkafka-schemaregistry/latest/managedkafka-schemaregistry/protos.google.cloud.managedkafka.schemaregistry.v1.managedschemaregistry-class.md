---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.managedschemaregistry-class
title: Class protos.google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:06.764856+00:00
---

# Class protos.google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.managedschemaregistry-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a ManagedSchemaRegistry

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry

## Package

[@google-cloud/managedkafka-schemaregistry](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ManagedSchemaRegistry service.

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

### checkCompatibility(request, callback)
    
    
    public checkCompatibility(request: google.cloud.managedkafka.schemaregistry.v1.ICheckCompatibilityRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CheckCompatibilityCallback): void;

Calls CheckCompatibility.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.icheckcompatibilityrequest)`   
CheckCompatibilityRequest message or plain object  
`callback` |  `[CheckCompatibilityCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and CheckCompatibilityResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkCompatibility(request)
    
    
    public checkCompatibility(request: google.cloud.managedkafka.schemaregistry.v1.ICheckCompatibilityRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.CheckCompatibilityResponse>;

Calls CheckCompatibility.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICheckCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.icheckcompatibilityrequest)`   
CheckCompatibilityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.CheckCompatibilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.checkcompatibilityresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ManagedSchemaRegistry;

Creates new ManagedSchemaRegistry service using the specified rpc implementation.

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
`[ManagedSchemaRegistry](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.managedschemaregistry-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSchemaRegistry(request, callback)
    
    
    public createSchemaRegistry(request: google.cloud.managedkafka.schemaregistry.v1.ICreateSchemaRegistryRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateSchemaRegistryCallback): void;

Calls CreateSchemaRegistry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSchemaRegistryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.icreateschemaregistryrequest)`   
CreateSchemaRegistryRequest message or plain object  
`callback` |  `[CreateSchemaRegistryCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaRegistry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSchemaRegistry(request)
    
    
    public createSchemaRegistry(request: google.cloud.managedkafka.schemaregistry.v1.ICreateSchemaRegistryRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaRegistry>;

Calls CreateSchemaRegistry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSchemaRegistryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.icreateschemaregistryrequest)`   
CreateSchemaRegistryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaRegistry](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaregistry)>` | Promise  
  
### createVersion(request, callback)
    
    
    public createVersion(request: google.cloud.managedkafka.schemaregistry.v1.ICreateVersionRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateVersionCallback): void;

Calls CreateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.icreateversionrequest)`   
CreateVersionRequest message or plain object  
`callback` |  `[CreateVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and CreateVersionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createVersion(request)
    
    
    public createVersion(request: google.cloud.managedkafka.schemaregistry.v1.ICreateVersionRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.CreateVersionResponse>;

Calls CreateVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.icreateversionrequest)`   
CreateVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.CreateVersionResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.createversionresponse)>` | Promise  
  
### deleteSchemaConfig(request, callback)
    
    
    public deleteSchemaConfig(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSchemaConfigRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaConfigCallback): void;

Calls DeleteSchemaConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSchemaConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteschemaconfigrequest)`   
DeleteSchemaConfigRequest message or plain object  
`callback` |  `[DeleteSchemaConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSchemaConfig(request)
    
    
    public deleteSchemaConfig(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSchemaConfigRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaConfig>;

Calls DeleteSchemaConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSchemaConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteschemaconfigrequest)`   
DeleteSchemaConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)>` | Promise  
  
### deleteSchemaMode(request, callback)
    
    
    public deleteSchemaMode(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSchemaModeRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaModeCallback): void;

Calls DeleteSchemaMode.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSchemaModeRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteschemamoderequest)`   
DeleteSchemaModeRequest message or plain object  
`callback` |  `[DeleteSchemaModeCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaMode  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSchemaMode(request)
    
    
    public deleteSchemaMode(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSchemaModeRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaMode>;

Calls DeleteSchemaMode.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSchemaModeRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteschemamoderequest)`   
DeleteSchemaModeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaMode](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemamode-class)>` | Promise  
  
### deleteSchemaRegistry(request, callback)
    
    
    public deleteSchemaRegistry(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSchemaRegistryRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaRegistryCallback): void;

Calls DeleteSchemaRegistry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSchemaRegistryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteschemaregistryrequest)`   
DeleteSchemaRegistryRequest message or plain object  
`callback` |  `[DeleteSchemaRegistryCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSchemaRegistry(request)
    
    
    public deleteSchemaRegistry(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSchemaRegistryRequest): Promise<google.protobuf.Empty>;

Calls DeleteSchemaRegistry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSchemaRegistryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteschemaregistryrequest)`   
DeleteSchemaRegistryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.empty)>` | Promise  
  
### deleteSubject(request, callback)
    
    
    public deleteSubject(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSubjectRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSubjectCallback): void;

Calls DeleteSubject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideletesubjectrequest)`   
DeleteSubjectRequest message or plain object  
`callback` |  `[DeleteSubjectCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSubject(request)
    
    
    public deleteSubject(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteSubjectRequest): Promise<google.api.HttpBody>;

Calls DeleteSubject.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideletesubjectrequest)`   
DeleteSubjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### deleteVersion(request, callback)
    
    
    public deleteVersion(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteVersionRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteVersionCallback): void;

Calls DeleteVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
`callback` |  `[DeleteVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteVersion(request)
    
    
    public deleteVersion(request: google.cloud.managedkafka.schemaregistry.v1.IDeleteVersionRequest): Promise<google.api.HttpBody>;

Calls DeleteVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### getContext(request, callback)
    
    
    public getContext(request: google.cloud.managedkafka.schemaregistry.v1.IGetContextRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetContextCallback): void;

Calls GetContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetcontextrequest)`   
GetContextRequest message or plain object  
`callback` |  `[GetContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and Context  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getContext(request)
    
    
    public getContext(request: google.cloud.managedkafka.schemaregistry.v1.IGetContextRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.Context>;

Calls GetContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetcontextrequest)`   
GetContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.Context](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.context)>` | Promise  
  
### getRawSchema(request, callback)
    
    
    public getRawSchema(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchemaCallback): void;

Calls GetRawSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemarequest)`   
GetSchemaRequest message or plain object  
`callback` |  `[GetRawSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRawSchema(request)
    
    
    public getRawSchema(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaRequest): Promise<google.api.HttpBody>;

Calls GetRawSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemarequest)`   
GetSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### getRawSchemaVersion(request, callback)
    
    
    public getRawSchemaVersion(request: google.cloud.managedkafka.schemaregistry.v1.IGetVersionRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchemaVersionCallback): void;

Calls GetRawSchemaVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
`callback` |  `[GetRawSchemaVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRawSchemaVersion(request)
    
    
    public getRawSchemaVersion(request: google.cloud.managedkafka.schemaregistry.v1.IGetVersionRequest): Promise<google.api.HttpBody>;

Calls GetRawSchemaVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### getSchema(request, callback)
    
    
    public getSchema(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaCallback): void;

Calls GetSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemarequest)`   
GetSchemaRequest message or plain object  
`callback` |  `[GetSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and Schema  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSchema(request)
    
    
    public getSchema(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.Schema>;

Calls GetSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemarequest)`   
GetSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.Schema](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schema-class)>` | Promise  
  
### getSchemaConfig(request, callback)
    
    
    public getSchemaConfig(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaConfigRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaConfigCallback): void;

Calls GetSchemaConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemaconfigrequest)`   
GetSchemaConfigRequest message or plain object  
`callback` |  `[GetSchemaConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSchemaConfig(request)
    
    
    public getSchemaConfig(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaConfigRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaConfig>;

Calls GetSchemaConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemaconfigrequest)`   
GetSchemaConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)>` | Promise  
  
### getSchemaMode(request, callback)
    
    
    public getSchemaMode(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaModeRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaModeCallback): void;

Calls GetSchemaMode.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaModeRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemamoderequest)`   
GetSchemaModeRequest message or plain object  
`callback` |  `[GetSchemaModeCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaMode  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSchemaMode(request)
    
    
    public getSchemaMode(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaModeRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaMode>;

Calls GetSchemaMode.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaModeRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemamoderequest)`   
GetSchemaModeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaMode](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemamode-class)>` | Promise  
  
### getSchemaRegistry(request, callback)
    
    
    public getSchemaRegistry(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaRegistryRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaRegistryCallback): void;

Calls GetSchemaRegistry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRegistryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemaregistryrequest)`   
GetSchemaRegistryRequest message or plain object  
`callback` |  `[GetSchemaRegistryCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaRegistry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSchemaRegistry(request)
    
    
    public getSchemaRegistry(request: google.cloud.managedkafka.schemaregistry.v1.IGetSchemaRegistryRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaRegistry>;

Calls GetSchemaRegistry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRegistryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetschemaregistryrequest)`   
GetSchemaRegistryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaRegistry](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaregistry)>` | Promise  
  
### getVersion(request, callback)
    
    
    public getVersion(request: google.cloud.managedkafka.schemaregistry.v1.IGetVersionRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetVersionCallback): void;

Calls GetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
`callback` |  `[GetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getVersion(request)
    
    
    public getVersion(request: google.cloud.managedkafka.schemaregistry.v1.IGetVersionRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaVersion>;

Calls GetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaVersion](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaversion)>` | Promise  
  
### listContexts(request, callback)
    
    
    public listContexts(request: google.cloud.managedkafka.schemaregistry.v1.IListContextsRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListContextsCallback): void;

Calls ListContexts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistcontextsrequest)`   
ListContextsRequest message or plain object  
`callback` |  `[ListContextsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listContexts(request)
    
    
    public listContexts(request: google.cloud.managedkafka.schemaregistry.v1.IListContextsRequest): Promise<google.api.HttpBody>;

Calls ListContexts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistcontextsrequest)`   
ListContextsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### listReferencedSchemas(request, callback)
    
    
    public listReferencedSchemas(request: google.cloud.managedkafka.schemaregistry.v1.IListReferencedSchemasRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListReferencedSchemasCallback): void;

Calls ListReferencedSchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReferencedSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistreferencedschemasrequest)`   
ListReferencedSchemasRequest message or plain object  
`callback` |  `[ListReferencedSchemasCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReferencedSchemas(request)
    
    
    public listReferencedSchemas(request: google.cloud.managedkafka.schemaregistry.v1.IListReferencedSchemasRequest): Promise<google.api.HttpBody>;

Calls ListReferencedSchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReferencedSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistreferencedschemasrequest)`   
ListReferencedSchemasRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### listSchemaRegistries(request, callback)
    
    
    public listSchemaRegistries(request: google.cloud.managedkafka.schemaregistry.v1.IListSchemaRegistriesRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaRegistriesCallback): void;

Calls ListSchemaRegistries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSchemaRegistriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistschemaregistriesrequest)`   
ListSchemaRegistriesRequest message or plain object  
`callback` |  `[ListSchemaRegistriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSchemaRegistriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSchemaRegistries(request)
    
    
    public listSchemaRegistries(request: google.cloud.managedkafka.schemaregistry.v1.IListSchemaRegistriesRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.ListSchemaRegistriesResponse>;

Calls ListSchemaRegistries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSchemaRegistriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistschemaregistriesrequest)`   
ListSchemaRegistriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.ListSchemaRegistriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.listschemaregistriesresponse)>` | Promise  
  
### listSchemaTypes(request, callback)
    
    
    public listSchemaTypes(request: google.cloud.managedkafka.schemaregistry.v1.IListSchemaTypesRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaTypesCallback): void;

Calls ListSchemaTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSchemaTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistschematypesrequest)`   
ListSchemaTypesRequest message or plain object  
`callback` |  `[ListSchemaTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSchemaTypes(request)
    
    
    public listSchemaTypes(request: google.cloud.managedkafka.schemaregistry.v1.IListSchemaTypesRequest): Promise<google.api.HttpBody>;

Calls ListSchemaTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSchemaTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistschematypesrequest)`   
ListSchemaTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### listSchemaVersions(request, callback)
    
    
    public listSchemaVersions(request: google.cloud.managedkafka.schemaregistry.v1.IListSchemaVersionsRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaVersionsCallback): void;

Calls ListSchemaVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSchemaVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistschemaversionsrequest)`   
ListSchemaVersionsRequest message or plain object  
`callback` |  `[ListSchemaVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSchemaVersions(request)
    
    
    public listSchemaVersions(request: google.cloud.managedkafka.schemaregistry.v1.IListSchemaVersionsRequest): Promise<google.api.HttpBody>;

Calls ListSchemaVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSchemaVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistschemaversionsrequest)`   
ListSchemaVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### listSubjects(request, callback)
    
    
    public listSubjects(request: google.cloud.managedkafka.schemaregistry.v1.IListSubjectsRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjectsCallback): void;

Calls ListSubjects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistsubjectsrequest)`   
ListSubjectsRequest message or plain object  
`callback` |  `[ListSubjectsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubjects(request)
    
    
    public listSubjects(request: google.cloud.managedkafka.schemaregistry.v1.IListSubjectsRequest): Promise<google.api.HttpBody>;

Calls ListSubjects.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistsubjectsrequest)`   
ListSubjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### listSubjectsBySchemaId(request, callback)
    
    
    public listSubjectsBySchemaId(request: google.cloud.managedkafka.schemaregistry.v1.IListSubjectsBySchemaIdRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjectsBySchemaIdCallback): void;

Calls ListSubjectsBySchemaId.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubjectsBySchemaIdRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistsubjectsbyschemaidrequest)`   
ListSubjectsBySchemaIdRequest message or plain object  
`callback` |  `[ListSubjectsBySchemaIdCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubjectsBySchemaId(request)
    
    
    public listSubjectsBySchemaId(request: google.cloud.managedkafka.schemaregistry.v1.IListSubjectsBySchemaIdRequest): Promise<google.api.HttpBody>;

Calls ListSubjectsBySchemaId.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubjectsBySchemaIdRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistsubjectsbyschemaidrequest)`   
ListSubjectsBySchemaIdRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### listVersions(request, callback)
    
    
    public listVersions(request: google.cloud.managedkafka.schemaregistry.v1.IListVersionsRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListVersionsCallback): void;

Calls ListVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
`callback` |  `[ListVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVersions(request)
    
    
    public listVersions(request: google.cloud.managedkafka.schemaregistry.v1.IListVersionsRequest): Promise<google.api.HttpBody>;

Calls ListVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.api.httpbody)>` | Promise  
  
### lookupVersion(request, callback)
    
    
    public lookupVersion(request: google.cloud.managedkafka.schemaregistry.v1.ILookupVersionRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.LookupVersionCallback): void;

Calls LookupVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilookupversionrequest)`   
LookupVersionRequest message or plain object  
`callback` |  `[LookupVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupVersion(request)
    
    
    public lookupVersion(request: google.cloud.managedkafka.schemaregistry.v1.ILookupVersionRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaVersion>;

Calls LookupVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilookupversionrequest)`   
LookupVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaVersion](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaversion)>` | Promise  
  
### updateSchemaConfig(request, callback)
    
    
    public updateSchemaConfig(request: google.cloud.managedkafka.schemaregistry.v1.IUpdateSchemaConfigRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaConfigCallback): void;

Calls UpdateSchemaConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSchemaConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.iupdateschemaconfigrequest)`   
UpdateSchemaConfigRequest message or plain object  
`callback` |  `[UpdateSchemaConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSchemaConfig(request)
    
    
    public updateSchemaConfig(request: google.cloud.managedkafka.schemaregistry.v1.IUpdateSchemaConfigRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaConfig>;

Calls UpdateSchemaConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSchemaConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.iupdateschemaconfigrequest)`   
UpdateSchemaConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)>` | Promise  
  
### updateSchemaMode(request, callback)
    
    
    public updateSchemaMode(request: google.cloud.managedkafka.schemaregistry.v1.IUpdateSchemaModeRequest, callback: google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaModeCallback): void;

Calls UpdateSchemaMode.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSchemaModeRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.iupdateschemamoderequest)`   
UpdateSchemaModeRequest message or plain object  
`callback` |  `[UpdateSchemaModeCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and SchemaMode  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSchemaMode(request)
    
    
    public updateSchemaMode(request: google.cloud.managedkafka.schemaregistry.v1.IUpdateSchemaModeRequest): Promise<google.cloud.managedkafka.schemaregistry.v1.SchemaMode>;

Calls UpdateSchemaMode.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSchemaModeRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.iupdateschemamoderequest)`   
UpdateSchemaModeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.schemaregistry.v1.SchemaMode](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemamode-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
