---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihub-class
title: Class protos.google.cloud.apihub.v1.ApiHub (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:41.580656+00:00
---

# Class protos.google.cloud.apihub.v1.ApiHub (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihub-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.ApiHub (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ApiHub

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.ApiHub

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ApiHub service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ApiHub;

Creates new ApiHub service using the specified rpc implementation.

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
`[ApiHub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihub-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createApi(request, callback)
    
    
    public createApi(request: google.cloud.apihub.v1.ICreateApiRequest, callback: google.cloud.apihub.v1.ApiHub.CreateApiCallback): void;

Calls CreateApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateapirequest)`   
CreateApiRequest message or plain object  
`callback` |  `[CreateApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Api  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createApi(request)
    
    
    public createApi(request: google.cloud.apihub.v1.ICreateApiRequest): Promise<google.cloud.apihub.v1.Api>;

Calls CreateApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateapirequest)`   
CreateApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)>` | Promise  
  
### createApiOperation(request, callback)
    
    
    public createApiOperation(request: google.cloud.apihub.v1.ICreateApiOperationRequest, callback: google.cloud.apihub.v1.ApiHub.CreateApiOperationCallback): void;

Calls CreateApiOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateapioperationrequest)`   
CreateApiOperationRequest message or plain object  
`callback` |  `[CreateApiOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ApiOperation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createApiOperation(request)
    
    
    public createApiOperation(request: google.cloud.apihub.v1.ICreateApiOperationRequest): Promise<google.cloud.apihub.v1.ApiOperation>;

Calls CreateApiOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateapioperationrequest)`   
CreateApiOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ApiOperation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apioperation)>` | Promise  
  
### createAttribute(request, callback)
    
    
    public createAttribute(request: google.cloud.apihub.v1.ICreateAttributeRequest, callback: google.cloud.apihub.v1.ApiHub.CreateAttributeCallback): void;

Calls CreateAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateattributerequest)`   
CreateAttributeRequest message or plain object  
`callback` |  `[CreateAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Attribute  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAttribute(request)
    
    
    public createAttribute(request: google.cloud.apihub.v1.ICreateAttributeRequest): Promise<google.cloud.apihub.v1.Attribute>;

Calls CreateAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateattributerequest)`   
CreateAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Attribute](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.attribute-class)>` | Promise  
  
### createDeployment(request, callback)
    
    
    public createDeployment(request: google.cloud.apihub.v1.ICreateDeploymentRequest, callback: google.cloud.apihub.v1.ApiHub.CreateDeploymentCallback): void;

Calls CreateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatedeploymentrequest)`   
CreateDeploymentRequest message or plain object  
`callback` |  `[CreateDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDeployment(request)
    
    
    public createDeployment(request: google.cloud.apihub.v1.ICreateDeploymentRequest): Promise<google.cloud.apihub.v1.Deployment>;

Calls CreateDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatedeploymentrequest)`   
CreateDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)>` | Promise  
  
### createExternalApi(request, callback)
    
    
    public createExternalApi(request: google.cloud.apihub.v1.ICreateExternalApiRequest, callback: google.cloud.apihub.v1.ApiHub.CreateExternalApiCallback): void;

Calls CreateExternalApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateexternalapirequest)`   
CreateExternalApiRequest message or plain object  
`callback` |  `[CreateExternalApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ExternalApi  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createExternalApi(request)
    
    
    public createExternalApi(request: google.cloud.apihub.v1.ICreateExternalApiRequest): Promise<google.cloud.apihub.v1.ExternalApi>;

Calls CreateExternalApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateexternalapirequest)`   
CreateExternalApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ExternalApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.externalapi)>` | Promise  
  
### createSpec(request, callback)
    
    
    public createSpec(request: google.cloud.apihub.v1.ICreateSpecRequest, callback: google.cloud.apihub.v1.ApiHub.CreateSpecCallback): void;

Calls CreateSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatespecrequest)`   
CreateSpecRequest message or plain object  
`callback` |  `[CreateSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Spec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSpec(request)
    
    
    public createSpec(request: google.cloud.apihub.v1.ICreateSpecRequest): Promise<google.cloud.apihub.v1.Spec>;

Calls CreateSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatespecrequest)`   
CreateSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Spec](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.spec-class)>` | Promise  
  
### createVersion(request, callback)
    
    
    public createVersion(request: google.cloud.apihub.v1.ICreateVersionRequest, callback: google.cloud.apihub.v1.ApiHub.CreateVersionCallback): void;

Calls CreateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateversionrequest)`   
CreateVersionRequest message or plain object  
`callback` |  `[CreateVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Version  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createVersion(request)
    
    
    public createVersion(request: google.cloud.apihub.v1.ICreateVersionRequest): Promise<google.cloud.apihub.v1.Version>;

Calls CreateVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateversionrequest)`   
CreateVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)>` | Promise  
  
### deleteApi(request, callback)
    
    
    public deleteApi(request: google.cloud.apihub.v1.IDeleteApiRequest, callback: google.cloud.apihub.v1.ApiHub.DeleteApiCallback): void;

Calls DeleteApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteapirequest)`   
DeleteApiRequest message or plain object  
`callback` |  `[DeleteApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteApi(request)
    
    
    public deleteApi(request: google.cloud.apihub.v1.IDeleteApiRequest): Promise<google.protobuf.Empty>;

Calls DeleteApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteapirequest)`   
DeleteApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### deleteApiOperation(request, callback)
    
    
    public deleteApiOperation(request: google.cloud.apihub.v1.IDeleteApiOperationRequest, callback: google.cloud.apihub.v1.ApiHub.DeleteApiOperationCallback): void;

Calls DeleteApiOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteapioperationrequest)`   
DeleteApiOperationRequest message or plain object  
`callback` |  `[DeleteApiOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteApiOperation(request)
    
    
    public deleteApiOperation(request: google.cloud.apihub.v1.IDeleteApiOperationRequest): Promise<google.protobuf.Empty>;

Calls DeleteApiOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteapioperationrequest)`   
DeleteApiOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### deleteAttribute(request, callback)
    
    
    public deleteAttribute(request: google.cloud.apihub.v1.IDeleteAttributeRequest, callback: google.cloud.apihub.v1.ApiHub.DeleteAttributeCallback): void;

Calls DeleteAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteattributerequest)`   
DeleteAttributeRequest message or plain object  
`callback` |  `[DeleteAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAttribute(request)
    
    
    public deleteAttribute(request: google.cloud.apihub.v1.IDeleteAttributeRequest): Promise<google.protobuf.Empty>;

Calls DeleteAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteattributerequest)`   
DeleteAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### deleteDeployment(request, callback)
    
    
    public deleteDeployment(request: google.cloud.apihub.v1.IDeleteDeploymentRequest, callback: google.cloud.apihub.v1.ApiHub.DeleteDeploymentCallback): void;

Calls DeleteDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletedeploymentrequest)`   
DeleteDeploymentRequest message or plain object  
`callback` |  `[DeleteDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDeployment(request)
    
    
    public deleteDeployment(request: google.cloud.apihub.v1.IDeleteDeploymentRequest): Promise<google.protobuf.Empty>;

Calls DeleteDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletedeploymentrequest)`   
DeleteDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### deleteExternalApi(request, callback)
    
    
    public deleteExternalApi(request: google.cloud.apihub.v1.IDeleteExternalApiRequest, callback: google.cloud.apihub.v1.ApiHub.DeleteExternalApiCallback): void;

Calls DeleteExternalApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteexternalapirequest)`   
DeleteExternalApiRequest message or plain object  
`callback` |  `[DeleteExternalApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteExternalApi(request)
    
    
    public deleteExternalApi(request: google.cloud.apihub.v1.IDeleteExternalApiRequest): Promise<google.protobuf.Empty>;

Calls DeleteExternalApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteexternalapirequest)`   
DeleteExternalApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### deleteSpec(request, callback)
    
    
    public deleteSpec(request: google.cloud.apihub.v1.IDeleteSpecRequest, callback: google.cloud.apihub.v1.ApiHub.DeleteSpecCallback): void;

Calls DeleteSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletespecrequest)`   
DeleteSpecRequest message or plain object  
`callback` |  `[DeleteSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSpec(request)
    
    
    public deleteSpec(request: google.cloud.apihub.v1.IDeleteSpecRequest): Promise<google.protobuf.Empty>;

Calls DeleteSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletespecrequest)`   
DeleteSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### deleteVersion(request, callback)
    
    
    public deleteVersion(request: google.cloud.apihub.v1.IDeleteVersionRequest, callback: google.cloud.apihub.v1.ApiHub.DeleteVersionCallback): void;

Calls DeleteVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
`callback` |  `[DeleteVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteVersion(request)
    
    
    public deleteVersion(request: google.cloud.apihub.v1.IDeleteVersionRequest): Promise<google.protobuf.Empty>;

Calls DeleteVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### getApi(request, callback)
    
    
    public getApi(request: google.cloud.apihub.v1.IGetApiRequest, callback: google.cloud.apihub.v1.ApiHub.GetApiCallback): void;

Calls GetApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetapirequest)`   
GetApiRequest message or plain object  
`callback` |  `[GetApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Api  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getApi(request)
    
    
    public getApi(request: google.cloud.apihub.v1.IGetApiRequest): Promise<google.cloud.apihub.v1.Api>;

Calls GetApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetapirequest)`   
GetApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)>` | Promise  
  
### getApiOperation(request, callback)
    
    
    public getApiOperation(request: google.cloud.apihub.v1.IGetApiOperationRequest, callback: google.cloud.apihub.v1.ApiHub.GetApiOperationCallback): void;

Calls GetApiOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetapioperationrequest)`   
GetApiOperationRequest message or plain object  
`callback` |  `[GetApiOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ApiOperation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getApiOperation(request)
    
    
    public getApiOperation(request: google.cloud.apihub.v1.IGetApiOperationRequest): Promise<google.cloud.apihub.v1.ApiOperation>;

Calls GetApiOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetapioperationrequest)`   
GetApiOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ApiOperation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apioperation)>` | Promise  
  
### getAttribute(request, callback)
    
    
    public getAttribute(request: google.cloud.apihub.v1.IGetAttributeRequest, callback: google.cloud.apihub.v1.ApiHub.GetAttributeCallback): void;

Calls GetAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetattributerequest)`   
GetAttributeRequest message or plain object  
`callback` |  `[GetAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Attribute  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAttribute(request)
    
    
    public getAttribute(request: google.cloud.apihub.v1.IGetAttributeRequest): Promise<google.cloud.apihub.v1.Attribute>;

Calls GetAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetattributerequest)`   
GetAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Attribute](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.attribute-class)>` | Promise  
  
### getDefinition(request, callback)
    
    
    public getDefinition(request: google.cloud.apihub.v1.IGetDefinitionRequest, callback: google.cloud.apihub.v1.ApiHub.GetDefinitionCallback): void;

Calls GetDefinition.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDefinitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdefinitionrequest)`   
GetDefinitionRequest message or plain object  
`callback` |  `[GetDefinitionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Definition  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDefinition(request)
    
    
    public getDefinition(request: google.cloud.apihub.v1.IGetDefinitionRequest): Promise<google.cloud.apihub.v1.Definition>;

Calls GetDefinition.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDefinitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdefinitionrequest)`   
GetDefinitionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Definition](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.definition-class)>` | Promise  
  
### getDeployment(request, callback)
    
    
    public getDeployment(request: google.cloud.apihub.v1.IGetDeploymentRequest, callback: google.cloud.apihub.v1.ApiHub.GetDeploymentCallback): void;

Calls GetDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
`callback` |  `[GetDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeployment(request)
    
    
    public getDeployment(request: google.cloud.apihub.v1.IGetDeploymentRequest): Promise<google.cloud.apihub.v1.Deployment>;

Calls GetDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)>` | Promise  
  
### getExternalApi(request, callback)
    
    
    public getExternalApi(request: google.cloud.apihub.v1.IGetExternalApiRequest, callback: google.cloud.apihub.v1.ApiHub.GetExternalApiCallback): void;

Calls GetExternalApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetexternalapirequest)`   
GetExternalApiRequest message or plain object  
`callback` |  `[GetExternalApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ExternalApi  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExternalApi(request)
    
    
    public getExternalApi(request: google.cloud.apihub.v1.IGetExternalApiRequest): Promise<google.cloud.apihub.v1.ExternalApi>;

Calls GetExternalApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetexternalapirequest)`   
GetExternalApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ExternalApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.externalapi)>` | Promise  
  
### getSpec(request, callback)
    
    
    public getSpec(request: google.cloud.apihub.v1.IGetSpecRequest, callback: google.cloud.apihub.v1.ApiHub.GetSpecCallback): void;

Calls GetSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetspecrequest)`   
GetSpecRequest message or plain object  
`callback` |  `[GetSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Spec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSpec(request)
    
    
    public getSpec(request: google.cloud.apihub.v1.IGetSpecRequest): Promise<google.cloud.apihub.v1.Spec>;

Calls GetSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetspecrequest)`   
GetSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Spec](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.spec-class)>` | Promise  
  
### getSpecContents(request, callback)
    
    
    public getSpecContents(request: google.cloud.apihub.v1.IGetSpecContentsRequest, callback: google.cloud.apihub.v1.ApiHub.GetSpecContentsCallback): void;

Calls GetSpecContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSpecContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetspeccontentsrequest)`   
GetSpecContentsRequest message or plain object  
`callback` |  `[GetSpecContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and SpecContents  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSpecContents(request)
    
    
    public getSpecContents(request: google.cloud.apihub.v1.IGetSpecContentsRequest): Promise<google.cloud.apihub.v1.SpecContents>;

Calls GetSpecContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSpecContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetspeccontentsrequest)`   
GetSpecContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.SpecContents](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.speccontents)>` | Promise  
  
### getVersion(request, callback)
    
    
    public getVersion(request: google.cloud.apihub.v1.IGetVersionRequest, callback: google.cloud.apihub.v1.ApiHub.GetVersionCallback): void;

Calls GetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
`callback` |  `[GetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Version  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getVersion(request)
    
    
    public getVersion(request: google.cloud.apihub.v1.IGetVersionRequest): Promise<google.cloud.apihub.v1.Version>;

Calls GetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)>` | Promise  
  
### listApiOperations(request, callback)
    
    
    public listApiOperations(request: google.cloud.apihub.v1.IListApiOperationsRequest, callback: google.cloud.apihub.v1.ApiHub.ListApiOperationsCallback): void;

Calls ListApiOperations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListApiOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistapioperationsrequest)`   
ListApiOperationsRequest message or plain object  
`callback` |  `[ListApiOperationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListApiOperationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listApiOperations(request)
    
    
    public listApiOperations(request: google.cloud.apihub.v1.IListApiOperationsRequest): Promise<google.cloud.apihub.v1.ListApiOperationsResponse>;

Calls ListApiOperations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListApiOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistapioperationsrequest)`   
ListApiOperationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListApiOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listapioperationsresponse)>` | Promise  
  
### listApis(request, callback)
    
    
    public listApis(request: google.cloud.apihub.v1.IListApisRequest, callback: google.cloud.apihub.v1.ApiHub.ListApisCallback): void;

Calls ListApis.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListApisRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistapisrequest)`   
ListApisRequest message or plain object  
`callback` |  `[ListApisCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListApisResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listApis(request)
    
    
    public listApis(request: google.cloud.apihub.v1.IListApisRequest): Promise<google.cloud.apihub.v1.ListApisResponse>;

Calls ListApis.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListApisRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistapisrequest)`   
ListApisRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListApisResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listapisresponse)>` | Promise  
  
### listAttributes(request, callback)
    
    
    public listAttributes(request: google.cloud.apihub.v1.IListAttributesRequest, callback: google.cloud.apihub.v1.ApiHub.ListAttributesCallback): void;

Calls ListAttributes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistattributesrequest)`   
ListAttributesRequest message or plain object  
`callback` |  `[ListAttributesCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAttributesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAttributes(request)
    
    
    public listAttributes(request: google.cloud.apihub.v1.IListAttributesRequest): Promise<google.cloud.apihub.v1.ListAttributesResponse>;

Calls ListAttributes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistattributesrequest)`   
ListAttributesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListAttributesResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listattributesresponse)>` | Promise  
  
### listDeployments(request, callback)
    
    
    public listDeployments(request: google.cloud.apihub.v1.IListDeploymentsRequest, callback: google.cloud.apihub.v1.ApiHub.ListDeploymentsCallback): void;

Calls ListDeployments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
`callback` |  `[ListDeploymentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeploymentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeployments(request)
    
    
    public listDeployments(request: google.cloud.apihub.v1.IListDeploymentsRequest): Promise<google.cloud.apihub.v1.ListDeploymentsResponse>;

Calls ListDeployments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listdeploymentsresponse)>` | Promise  
  
### listExternalApis(request, callback)
    
    
    public listExternalApis(request: google.cloud.apihub.v1.IListExternalApisRequest, callback: google.cloud.apihub.v1.ApiHub.ListExternalApisCallback): void;

Calls ListExternalApis.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExternalApisRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistexternalapisrequest)`   
ListExternalApisRequest message or plain object  
`callback` |  `[ListExternalApisCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListExternalApisResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExternalApis(request)
    
    
    public listExternalApis(request: google.cloud.apihub.v1.IListExternalApisRequest): Promise<google.cloud.apihub.v1.ListExternalApisResponse>;

Calls ListExternalApis.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListExternalApisRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistexternalapisrequest)`   
ListExternalApisRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListExternalApisResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listexternalapisresponse)>` | Promise  
  
### listSpecs(request, callback)
    
    
    public listSpecs(request: google.cloud.apihub.v1.IListSpecsRequest, callback: google.cloud.apihub.v1.ApiHub.ListSpecsCallback): void;

Calls ListSpecs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistspecsrequest)`   
ListSpecsRequest message or plain object  
`callback` |  `[ListSpecsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSpecsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSpecs(request)
    
    
    public listSpecs(request: google.cloud.apihub.v1.IListSpecsRequest): Promise<google.cloud.apihub.v1.ListSpecsResponse>;

Calls ListSpecs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistspecsrequest)`   
ListSpecsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listspecsresponse)>` | Promise  
  
### listVersions(request, callback)
    
    
    public listVersions(request: google.cloud.apihub.v1.IListVersionsRequest, callback: google.cloud.apihub.v1.ApiHub.ListVersionsCallback): void;

Calls ListVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
`callback` |  `[ListVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVersions(request)
    
    
    public listVersions(request: google.cloud.apihub.v1.IListVersionsRequest): Promise<google.cloud.apihub.v1.ListVersionsResponse>;

Calls ListVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listversionsresponse)>` | Promise  
  
### searchResources(request, callback)
    
    
    public searchResources(request: google.cloud.apihub.v1.ISearchResourcesRequest, callback: google.cloud.apihub.v1.ApiHub.SearchResourcesCallback): void;

Calls SearchResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.isearchresourcesrequest)`   
SearchResourcesRequest message or plain object  
`callback` |  `[SearchResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchResourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchResources(request)
    
    
    public searchResources(request: google.cloud.apihub.v1.ISearchResourcesRequest): Promise<google.cloud.apihub.v1.SearchResourcesResponse>;

Calls SearchResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.isearchresourcesrequest)`   
SearchResourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.SearchResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.searchresourcesresponse)>` | Promise  
  
### updateApi(request, callback)
    
    
    public updateApi(request: google.cloud.apihub.v1.IUpdateApiRequest, callback: google.cloud.apihub.v1.ApiHub.UpdateApiCallback): void;

Calls UpdateApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateapirequest)`   
UpdateApiRequest message or plain object  
`callback` |  `[UpdateApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Api  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateApi(request)
    
    
    public updateApi(request: google.cloud.apihub.v1.IUpdateApiRequest): Promise<google.cloud.apihub.v1.Api>;

Calls UpdateApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateapirequest)`   
UpdateApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)>` | Promise  
  
### updateApiOperation(request, callback)
    
    
    public updateApiOperation(request: google.cloud.apihub.v1.IUpdateApiOperationRequest, callback: google.cloud.apihub.v1.ApiHub.UpdateApiOperationCallback): void;

Calls UpdateApiOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateapioperationrequest)`   
UpdateApiOperationRequest message or plain object  
`callback` |  `[UpdateApiOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ApiOperation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateApiOperation(request)
    
    
    public updateApiOperation(request: google.cloud.apihub.v1.IUpdateApiOperationRequest): Promise<google.cloud.apihub.v1.ApiOperation>;

Calls UpdateApiOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateapioperationrequest)`   
UpdateApiOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ApiOperation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apioperation)>` | Promise  
  
### updateAttribute(request, callback)
    
    
    public updateAttribute(request: google.cloud.apihub.v1.IUpdateAttributeRequest, callback: google.cloud.apihub.v1.ApiHub.UpdateAttributeCallback): void;

Calls UpdateAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateattributerequest)`   
UpdateAttributeRequest message or plain object  
`callback` |  `[UpdateAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Attribute  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAttribute(request)
    
    
    public updateAttribute(request: google.cloud.apihub.v1.IUpdateAttributeRequest): Promise<google.cloud.apihub.v1.Attribute>;

Calls UpdateAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateattributerequest)`   
UpdateAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Attribute](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.attribute-class)>` | Promise  
  
### updateDeployment(request, callback)
    
    
    public updateDeployment(request: google.cloud.apihub.v1.IUpdateDeploymentRequest, callback: google.cloud.apihub.v1.ApiHub.UpdateDeploymentCallback): void;

Calls UpdateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatedeploymentrequest)`   
UpdateDeploymentRequest message or plain object  
`callback` |  `[UpdateDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDeployment(request)
    
    
    public updateDeployment(request: google.cloud.apihub.v1.IUpdateDeploymentRequest): Promise<google.cloud.apihub.v1.Deployment>;

Calls UpdateDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatedeploymentrequest)`   
UpdateDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)>` | Promise  
  
### updateExternalApi(request, callback)
    
    
    public updateExternalApi(request: google.cloud.apihub.v1.IUpdateExternalApiRequest, callback: google.cloud.apihub.v1.ApiHub.UpdateExternalApiCallback): void;

Calls UpdateExternalApi.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateexternalapirequest)`   
UpdateExternalApiRequest message or plain object  
`callback` |  `[UpdateExternalApiCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ExternalApi  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateExternalApi(request)
    
    
    public updateExternalApi(request: google.cloud.apihub.v1.IUpdateExternalApiRequest): Promise<google.cloud.apihub.v1.ExternalApi>;

Calls UpdateExternalApi.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExternalApiRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateexternalapirequest)`   
UpdateExternalApiRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ExternalApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.externalapi)>` | Promise  
  
### updateSpec(request, callback)
    
    
    public updateSpec(request: google.cloud.apihub.v1.IUpdateSpecRequest, callback: google.cloud.apihub.v1.ApiHub.UpdateSpecCallback): void;

Calls UpdateSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatespecrequest)`   
UpdateSpecRequest message or plain object  
`callback` |  `[UpdateSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Spec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSpec(request)
    
    
    public updateSpec(request: google.cloud.apihub.v1.IUpdateSpecRequest): Promise<google.cloud.apihub.v1.Spec>;

Calls UpdateSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatespecrequest)`   
UpdateSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Spec](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.spec-class)>` | Promise  
  
### updateVersion(request, callback)
    
    
    public updateVersion(request: google.cloud.apihub.v1.IUpdateVersionRequest, callback: google.cloud.apihub.v1.ApiHub.UpdateVersionCallback): void;

Calls UpdateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateversionrequest)`   
UpdateVersionRequest message or plain object  
`callback` |  `[UpdateVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Version  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateVersion(request)
    
    
    public updateVersion(request: google.cloud.apihub.v1.IUpdateVersionRequest): Promise<google.cloud.apihub.v1.Version>;

Calls UpdateVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateversionrequest)`   
UpdateVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
