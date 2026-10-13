---
url: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapmanagement-class
title: Class protos.google.maps.mapmanagement.v2beta.MapManagement (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:18.961800+00:00
---

# Class protos.google.maps.mapmanagement.v2beta.MapManagement (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapmanagement-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.mapmanagement.v2beta.MapManagement (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a MapManagement

## Inheritance

$protobuf.rpc.Service > protos.google.maps.mapmanagement.v2beta.MapManagement

## Package

[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MapManagement service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MapManagement;

Creates new MapManagement service using the specified rpc implementation.

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
`[MapManagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapmanagement-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createMapConfig(request, callback)
    
    
    public createMapConfig(request: google.maps.mapmanagement.v2beta.ICreateMapConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.CreateMapConfigCallback): void;

Calls CreateMapConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest)`   
CreateMapConfigRequest message or plain object  
`callback` |  `[CreateMapConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and MapConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMapConfig(request)
    
    
    public createMapConfig(request: google.maps.mapmanagement.v2beta.ICreateMapConfigRequest): Promise<google.maps.mapmanagement.v2beta.MapConfig>;

Calls CreateMapConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest)`   
CreateMapConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig)>` | Promise  
  
### createMapContextConfig(request, callback)
    
    
    public createMapContextConfig(request: google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.CreateMapContextConfigCallback): void;

Calls CreateMapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest)`   
CreateMapContextConfigRequest message or plain object  
`callback` |  `[CreateMapContextConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and MapContextConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMapContextConfig(request)
    
    
    public createMapContextConfig(request: google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest): Promise<google.maps.mapmanagement.v2beta.MapContextConfig>;

Calls CreateMapContextConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest)`   
CreateMapContextConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.MapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapcontextconfig-class)>` | Promise  
  
### createStyleConfig(request, callback)
    
    
    public createStyleConfig(request: google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.CreateStyleConfigCallback): void;

Calls CreateStyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest)`   
CreateStyleConfigRequest message or plain object  
`callback` |  `[CreateStyleConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and StyleConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createStyleConfig(request)
    
    
    public createStyleConfig(request: google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest): Promise<google.maps.mapmanagement.v2beta.StyleConfig>;

Calls CreateStyleConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest)`   
CreateStyleConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig)>` | Promise  
  
### deleteMapConfig(request, callback)
    
    
    public deleteMapConfig(request: google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.DeleteMapConfigCallback): void;

Calls DeleteMapConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
DeleteMapConfigRequest message or plain object  
`callback` |  `[DeleteMapConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMapConfig(request)
    
    
    public deleteMapConfig(request: google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteMapConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
DeleteMapConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.empty)>` | Promise  
  
### deleteMapContextConfig(request, callback)
    
    
    public deleteMapContextConfig(request: google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.DeleteMapContextConfigCallback): void;

Calls DeleteMapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest)`   
DeleteMapContextConfigRequest message or plain object  
`callback` |  `[DeleteMapContextConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMapContextConfig(request)
    
    
    public deleteMapContextConfig(request: google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteMapContextConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest)`   
DeleteMapContextConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.empty)>` | Promise  
  
### deleteStyleConfig(request, callback)
    
    
    public deleteStyleConfig(request: google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.DeleteStyleConfigCallback): void;

Calls DeleteStyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest)`   
DeleteStyleConfigRequest message or plain object  
`callback` |  `[DeleteStyleConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteStyleConfig(request)
    
    
    public deleteStyleConfig(request: google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteStyleConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest)`   
DeleteStyleConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.empty)>` | Promise  
  
### getMapConfig(request, callback)
    
    
    public getMapConfig(request: google.maps.mapmanagement.v2beta.IGetMapConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.GetMapConfigCallback): void;

Calls GetMapConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest)`   
GetMapConfigRequest message or plain object  
`callback` |  `[GetMapConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and MapConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMapConfig(request)
    
    
    public getMapConfig(request: google.maps.mapmanagement.v2beta.IGetMapConfigRequest): Promise<google.maps.mapmanagement.v2beta.MapConfig>;

Calls GetMapConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest)`   
GetMapConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig)>` | Promise  
  
### getMapContextConfig(request, callback)
    
    
    public getMapContextConfig(request: google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.GetMapContextConfigCallback): void;

Calls GetMapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest)`   
GetMapContextConfigRequest message or plain object  
`callback` |  `[GetMapContextConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and MapContextConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMapContextConfig(request)
    
    
    public getMapContextConfig(request: google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest): Promise<google.maps.mapmanagement.v2beta.MapContextConfig>;

Calls GetMapContextConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest)`   
GetMapContextConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.MapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapcontextconfig-class)>` | Promise  
  
### getStyleConfig(request, callback)
    
    
    public getStyleConfig(request: google.maps.mapmanagement.v2beta.IGetStyleConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.GetStyleConfigCallback): void;

Calls GetStyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest)`   
GetStyleConfigRequest message or plain object  
`callback` |  `[GetStyleConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and StyleConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStyleConfig(request)
    
    
    public getStyleConfig(request: google.maps.mapmanagement.v2beta.IGetStyleConfigRequest): Promise<google.maps.mapmanagement.v2beta.StyleConfig>;

Calls GetStyleConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest)`   
GetStyleConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig)>` | Promise  
  
### listMapConfigs(request, callback)
    
    
    public listMapConfigs(request: google.maps.mapmanagement.v2beta.IListMapConfigsRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.ListMapConfigsCallback): void;

Calls ListMapConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest)`   
ListMapConfigsRequest message or plain object  
`callback` |  `[ListMapConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMapConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMapConfigs(request)
    
    
    public listMapConfigs(request: google.maps.mapmanagement.v2beta.IListMapConfigsRequest): Promise<google.maps.mapmanagement.v2beta.ListMapConfigsResponse>;

Calls ListMapConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest)`   
ListMapConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.ListMapConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.listmapconfigsresponse)>` | Promise  
  
### listMapContextConfigs(request, callback)
    
    
    public listMapContextConfigs(request: google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.ListMapContextConfigsCallback): void;

Calls ListMapContextConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest)`   
ListMapContextConfigsRequest message or plain object  
`callback` |  `[ListMapContextConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMapContextConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMapContextConfigs(request)
    
    
    public listMapContextConfigs(request: google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest): Promise<google.maps.mapmanagement.v2beta.ListMapContextConfigsResponse>;

Calls ListMapContextConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest)`   
ListMapContextConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.ListMapContextConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.listmapcontextconfigsresponse)>` | Promise  
  
### listStyleConfigs(request, callback)
    
    
    public listStyleConfigs(request: google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.ListStyleConfigsCallback): void;

Calls ListStyleConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest)`   
ListStyleConfigsRequest message or plain object  
`callback` |  `[ListStyleConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and ListStyleConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStyleConfigs(request)
    
    
    public listStyleConfigs(request: google.maps.mapmanagement.v2beta.IListStyleConfigsRequest): Promise<google.maps.mapmanagement.v2beta.ListStyleConfigsResponse>;

Calls ListStyleConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest)`   
ListStyleConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.ListStyleConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.liststyleconfigsresponse)>` | Promise  
  
### updateMapConfig(request, callback)
    
    
    public updateMapConfig(request: google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.UpdateMapConfigCallback): void;

Calls UpdateMapConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
UpdateMapConfigRequest message or plain object  
`callback` |  `[UpdateMapConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and MapConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMapConfig(request)
    
    
    public updateMapConfig(request: google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest): Promise<google.maps.mapmanagement.v2beta.MapConfig>;

Calls UpdateMapConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
UpdateMapConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig)>` | Promise  
  
### updateMapContextConfig(request, callback)
    
    
    public updateMapContextConfig(request: google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.UpdateMapContextConfigCallback): void;

Calls UpdateMapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
UpdateMapContextConfigRequest message or plain object  
`callback` |  `[UpdateMapContextConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and MapContextConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMapContextConfig(request)
    
    
    public updateMapContextConfig(request: google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest): Promise<google.maps.mapmanagement.v2beta.MapContextConfig>;

Calls UpdateMapContextConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
UpdateMapContextConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.MapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapcontextconfig-class)>` | Promise  
  
### updateStyleConfig(request, callback)
    
    
    public updateStyleConfig(request: google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest, callback: google.maps.mapmanagement.v2beta.MapManagement.UpdateStyleConfigCallback): void;

Calls UpdateStyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest)`   
UpdateStyleConfigRequest message or plain object  
`callback` |  `[UpdateStyleConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)`   
Node-style callback called with the error, if any, and StyleConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateStyleConfig(request)
    
    
    public updateStyleConfig(request: google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest): Promise<google.maps.mapmanagement.v2beta.StyleConfig>;

Calls UpdateStyleConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest)`   
UpdateStyleConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.mapmanagement.v2beta.StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-25 UTC."],[],[]] 
