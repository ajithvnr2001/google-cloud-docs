---
url: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connectors-class
title: Class protos.google.cloud.connectors.v1.Connectors (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:21.556660+00:00
---

# Class protos.google.cloud.connectors.v1.Connectors (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connectors-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.connectors.v1.Connectors (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Connectors

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.connectors.v1.Connectors

## Package

[@google-cloud/connectors](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Connectors service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Connectors;

Creates new Connectors service using the specified rpc implementation.

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
`[Connectors](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connectors-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConnection(request, callback)
    
    
    public createConnection(request: google.cloud.connectors.v1.ICreateConnectionRequest, callback: google.cloud.connectors.v1.Connectors.CreateConnectionCallback): void;

Calls CreateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.icreateconnectionrequest)`   
CreateConnectionRequest message or plain object  
`callback` |  `[CreateConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConnection(request)
    
    
    public createConnection(request: google.cloud.connectors.v1.ICreateConnectionRequest): Promise<google.longrunning.Operation>;

Calls CreateConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.icreateconnectionrequest)`   
CreateConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.longrunning.operation)>` | Promise  
  
### deleteConnection(request, callback)
    
    
    public deleteConnection(request: google.cloud.connectors.v1.IDeleteConnectionRequest, callback: google.cloud.connectors.v1.Connectors.DeleteConnectionCallback): void;

Calls DeleteConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ideleteconnectionrequest)`   
DeleteConnectionRequest message or plain object  
`callback` |  `[DeleteConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnection(request)
    
    
    public deleteConnection(request: google.cloud.connectors.v1.IDeleteConnectionRequest): Promise<google.longrunning.Operation>;

Calls DeleteConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ideleteconnectionrequest)`   
DeleteConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.longrunning.operation)>` | Promise  
  
### getConnection(request, callback)
    
    
    public getConnection(request: google.cloud.connectors.v1.IGetConnectionRequest, callback: google.cloud.connectors.v1.Connectors.GetConnectionCallback): void;

Calls GetConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectionrequest)`   
GetConnectionRequest message or plain object  
`callback` |  `[GetConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Connection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnection(request)
    
    
    public getConnection(request: google.cloud.connectors.v1.IGetConnectionRequest): Promise<google.cloud.connectors.v1.Connection>;

Calls GetConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectionrequest)`   
GetConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.Connection](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connection)>` | Promise  
  
### getConnectionSchemaMetadata(request, callback)
    
    
    public getConnectionSchemaMetadata(request: google.cloud.connectors.v1.IGetConnectionSchemaMetadataRequest, callback: google.cloud.connectors.v1.Connectors.GetConnectionSchemaMetadataCallback): void;

Calls GetConnectionSchemaMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionSchemaMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectionschemametadatarequest)`   
GetConnectionSchemaMetadataRequest message or plain object  
`callback` |  `[GetConnectionSchemaMetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ConnectionSchemaMetadata  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnectionSchemaMetadata(request)
    
    
    public getConnectionSchemaMetadata(request: google.cloud.connectors.v1.IGetConnectionSchemaMetadataRequest): Promise<google.cloud.connectors.v1.ConnectionSchemaMetadata>;

Calls GetConnectionSchemaMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionSchemaMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectionschemametadatarequest)`   
GetConnectionSchemaMetadataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ConnectionSchemaMetadata](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connectionschemametadata-class)>` | Promise  
  
### getConnector(request, callback)
    
    
    public getConnector(request: google.cloud.connectors.v1.IGetConnectorRequest, callback: google.cloud.connectors.v1.Connectors.GetConnectorCallback): void;

Calls GetConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectorrequest)`   
GetConnectorRequest message or plain object  
`callback` |  `[GetConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Connector  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnector(request)
    
    
    public getConnector(request: google.cloud.connectors.v1.IGetConnectorRequest): Promise<google.cloud.connectors.v1.Connector>;

Calls GetConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectorrequest)`   
GetConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.Connector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector)>` | Promise  
  
### getConnectorVersion(request, callback)
    
    
    public getConnectorVersion(request: google.cloud.connectors.v1.IGetConnectorVersionRequest, callback: google.cloud.connectors.v1.Connectors.GetConnectorVersionCallback): void;

Calls GetConnectorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectorversionrequest)`   
GetConnectorVersionRequest message or plain object  
`callback` |  `[GetConnectorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ConnectorVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnectorVersion(request)
    
    
    public getConnectorVersion(request: google.cloud.connectors.v1.IGetConnectorVersionRequest): Promise<google.cloud.connectors.v1.ConnectorVersion>;

Calls GetConnectorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetconnectorversionrequest)`   
GetConnectorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ConnectorVersion](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connectorversion)>` | Promise  
  
### getGlobalSettings(request, callback)
    
    
    public getGlobalSettings(request: google.cloud.connectors.v1.IGetGlobalSettingsRequest, callback: google.cloud.connectors.v1.Connectors.GetGlobalSettingsCallback): void;

Calls GetGlobalSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGlobalSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetglobalsettingsrequest)`   
GetGlobalSettingsRequest message or plain object  
`callback` |  `[GetGlobalSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Settings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGlobalSettings(request)
    
    
    public getGlobalSettings(request: google.cloud.connectors.v1.IGetGlobalSettingsRequest): Promise<google.cloud.connectors.v1.Settings>;

Calls GetGlobalSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGlobalSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetglobalsettingsrequest)`   
GetGlobalSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.Settings](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.settings)>` | Promise  
  
### getProvider(request, callback)
    
    
    public getProvider(request: google.cloud.connectors.v1.IGetProviderRequest, callback: google.cloud.connectors.v1.Connectors.GetProviderCallback): void;

Calls GetProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetproviderrequest)`   
GetProviderRequest message or plain object  
`callback` |  `[GetProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Provider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProvider(request)
    
    
    public getProvider(request: google.cloud.connectors.v1.IGetProviderRequest): Promise<google.cloud.connectors.v1.Provider>;

Calls GetProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetproviderrequest)`   
GetProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.Provider](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.provider)>` | Promise  
  
### getRuntimeConfig(request, callback)
    
    
    public getRuntimeConfig(request: google.cloud.connectors.v1.IGetRuntimeConfigRequest, callback: google.cloud.connectors.v1.Connectors.GetRuntimeConfigCallback): void;

Calls GetRuntimeConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuntimeConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetruntimeconfigrequest)`   
GetRuntimeConfigRequest message or plain object  
`callback` |  `[GetRuntimeConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and RuntimeConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRuntimeConfig(request)
    
    
    public getRuntimeConfig(request: google.cloud.connectors.v1.IGetRuntimeConfigRequest): Promise<google.cloud.connectors.v1.RuntimeConfig>;

Calls GetRuntimeConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRuntimeConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.igetruntimeconfigrequest)`   
GetRuntimeConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.RuntimeConfig](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.runtimeconfig-class)>` | Promise  
  
### listConnections(request, callback)
    
    
    public listConnections(request: google.cloud.connectors.v1.IListConnectionsRequest, callback: google.cloud.connectors.v1.Connectors.ListConnectionsCallback): void;

Calls ListConnections.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistconnectionsrequest)`   
ListConnectionsRequest message or plain object  
`callback` |  `[ListConnectionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConnectionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnections(request)
    
    
    public listConnections(request: google.cloud.connectors.v1.IListConnectionsRequest): Promise<google.cloud.connectors.v1.ListConnectionsResponse>;

Calls ListConnections.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistconnectionsrequest)`   
ListConnectionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ListConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.listconnectionsresponse)>` | Promise  
  
### listConnectors(request, callback)
    
    
    public listConnectors(request: google.cloud.connectors.v1.IListConnectorsRequest, callback: google.cloud.connectors.v1.Connectors.ListConnectorsCallback): void;

Calls ListConnectors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistconnectorsrequest)`   
ListConnectorsRequest message or plain object  
`callback` |  `[ListConnectorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConnectorsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnectors(request)
    
    
    public listConnectors(request: google.cloud.connectors.v1.IListConnectorsRequest): Promise<google.cloud.connectors.v1.ListConnectorsResponse>;

Calls ListConnectors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConnectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistconnectorsrequest)`   
ListConnectorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ListConnectorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.listconnectorsresponse)>` | Promise  
  
### listConnectorVersions(request, callback)
    
    
    public listConnectorVersions(request: google.cloud.connectors.v1.IListConnectorVersionsRequest, callback: google.cloud.connectors.v1.Connectors.ListConnectorVersionsCallback): void;

Calls ListConnectorVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectorVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistconnectorversionsrequest)`   
ListConnectorVersionsRequest message or plain object  
`callback` |  `[ListConnectorVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConnectorVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnectorVersions(request)
    
    
    public listConnectorVersions(request: google.cloud.connectors.v1.IListConnectorVersionsRequest): Promise<google.cloud.connectors.v1.ListConnectorVersionsResponse>;

Calls ListConnectorVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConnectorVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistconnectorversionsrequest)`   
ListConnectorVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ListConnectorVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.listconnectorversionsresponse)>` | Promise  
  
### listProviders(request, callback)
    
    
    public listProviders(request: google.cloud.connectors.v1.IListProvidersRequest, callback: google.cloud.connectors.v1.Connectors.ListProvidersCallback): void;

Calls ListProviders.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistprovidersrequest)`   
ListProvidersRequest message or plain object  
`callback` |  `[ListProvidersCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProvidersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProviders(request)
    
    
    public listProviders(request: google.cloud.connectors.v1.IListProvidersRequest): Promise<google.cloud.connectors.v1.ListProvidersResponse>;

Calls ListProviders.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistprovidersrequest)`   
ListProvidersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ListProvidersResponse](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.listprovidersresponse)>` | Promise  
  
### listRuntimeActionSchemas(request, callback)
    
    
    public listRuntimeActionSchemas(request: google.cloud.connectors.v1.IListRuntimeActionSchemasRequest, callback: google.cloud.connectors.v1.Connectors.ListRuntimeActionSchemasCallback): void;

Calls ListRuntimeActionSchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRuntimeActionSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistruntimeactionschemasrequest)`   
ListRuntimeActionSchemasRequest message or plain object  
`callback` |  `[ListRuntimeActionSchemasCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRuntimeActionSchemasResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRuntimeActionSchemas(request)
    
    
    public listRuntimeActionSchemas(request: google.cloud.connectors.v1.IListRuntimeActionSchemasRequest): Promise<google.cloud.connectors.v1.ListRuntimeActionSchemasResponse>;

Calls ListRuntimeActionSchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRuntimeActionSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistruntimeactionschemasrequest)`   
ListRuntimeActionSchemasRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ListRuntimeActionSchemasResponse](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.listruntimeactionschemasresponse)>` | Promise  
  
### listRuntimeEntitySchemas(request, callback)
    
    
    public listRuntimeEntitySchemas(request: google.cloud.connectors.v1.IListRuntimeEntitySchemasRequest, callback: google.cloud.connectors.v1.Connectors.ListRuntimeEntitySchemasCallback): void;

Calls ListRuntimeEntitySchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRuntimeEntitySchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistruntimeentityschemasrequest)`   
ListRuntimeEntitySchemasRequest message or plain object  
`callback` |  `[ListRuntimeEntitySchemasCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRuntimeEntitySchemasResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRuntimeEntitySchemas(request)
    
    
    public listRuntimeEntitySchemas(request: google.cloud.connectors.v1.IListRuntimeEntitySchemasRequest): Promise<google.cloud.connectors.v1.ListRuntimeEntitySchemasResponse>;

Calls ListRuntimeEntitySchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRuntimeEntitySchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.ilistruntimeentityschemasrequest)`   
ListRuntimeEntitySchemasRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.connectors.v1.ListRuntimeEntitySchemasResponse](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.listruntimeentityschemasresponse)>` | Promise  
  
### refreshConnectionSchemaMetadata(request, callback)
    
    
    public refreshConnectionSchemaMetadata(request: google.cloud.connectors.v1.IRefreshConnectionSchemaMetadataRequest, callback: google.cloud.connectors.v1.Connectors.RefreshConnectionSchemaMetadataCallback): void;

Calls RefreshConnectionSchemaMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRefreshConnectionSchemaMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.irefreshconnectionschemametadatarequest)`   
RefreshConnectionSchemaMetadataRequest message or plain object  
`callback` |  `[RefreshConnectionSchemaMetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### refreshConnectionSchemaMetadata(request)
    
    
    public refreshConnectionSchemaMetadata(request: google.cloud.connectors.v1.IRefreshConnectionSchemaMetadataRequest): Promise<google.longrunning.Operation>;

Calls RefreshConnectionSchemaMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRefreshConnectionSchemaMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.irefreshconnectionschemametadatarequest)`   
RefreshConnectionSchemaMetadataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.longrunning.operation)>` | Promise  
  
### updateConnection(request, callback)
    
    
    public updateConnection(request: google.cloud.connectors.v1.IUpdateConnectionRequest, callback: google.cloud.connectors.v1.Connectors.UpdateConnectionCallback): void;

Calls UpdateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iupdateconnectionrequest)`   
UpdateConnectionRequest message or plain object  
`callback` |  `[UpdateConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnection(request)
    
    
    public updateConnection(request: google.cloud.connectors.v1.IUpdateConnectionRequest): Promise<google.longrunning.Operation>;

Calls UpdateConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iupdateconnectionrequest)`   
UpdateConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
