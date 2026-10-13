---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azureclusters-class
title: Class protos.google.cloud.gkemulticloud.v1.AzureClusters (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:55.578320+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AzureClusters (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azureclusters-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AzureClusters (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AzureClusters

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.gkemulticloud.v1.AzureClusters

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AzureClusters service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AzureClusters;

Creates new AzureClusters service using the specified rpc implementation.

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
`[AzureClusters](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azureclusters-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAzureClient(request, callback)
    
    
    public createAzureClient(request: google.cloud.gkemulticloud.v1.ICreateAzureClientRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureClientCallback): void;

Calls CreateAzureClient.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAzureClientRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateazureclientrequest)`   
CreateAzureClientRequest message or plain object  
`callback` |  `[CreateAzureClientCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAzureClient(request)
    
    
    public createAzureClient(request: google.cloud.gkemulticloud.v1.ICreateAzureClientRequest): Promise<google.longrunning.Operation>;

Calls CreateAzureClient.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAzureClientRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateazureclientrequest)`   
CreateAzureClientRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### createAzureCluster(request, callback)
    
    
    public createAzureCluster(request: google.cloud.gkemulticloud.v1.ICreateAzureClusterRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureClusterCallback): void;

Calls CreateAzureCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateazureclusterrequest)`   
CreateAzureClusterRequest message or plain object  
`callback` |  `[CreateAzureClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAzureCluster(request)
    
    
    public createAzureCluster(request: google.cloud.gkemulticloud.v1.ICreateAzureClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateAzureCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateazureclusterrequest)`   
CreateAzureClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### createAzureNodePool(request, callback)
    
    
    public createAzureNodePool(request: google.cloud.gkemulticloud.v1.ICreateAzureNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureNodePoolCallback): void;

Calls CreateAzureNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateazurenodepoolrequest)`   
CreateAzureNodePoolRequest message or plain object  
`callback` |  `[CreateAzureNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAzureNodePool(request)
    
    
    public createAzureNodePool(request: google.cloud.gkemulticloud.v1.ICreateAzureNodePoolRequest): Promise<google.longrunning.Operation>;

Calls CreateAzureNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateazurenodepoolrequest)`   
CreateAzureNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### deleteAzureClient(request, callback)
    
    
    public deleteAzureClient(request: google.cloud.gkemulticloud.v1.IDeleteAzureClientRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureClientCallback): void;

Calls DeleteAzureClient.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAzureClientRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteazureclientrequest)`   
DeleteAzureClientRequest message or plain object  
`callback` |  `[DeleteAzureClientCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAzureClient(request)
    
    
    public deleteAzureClient(request: google.cloud.gkemulticloud.v1.IDeleteAzureClientRequest): Promise<google.longrunning.Operation>;

Calls DeleteAzureClient.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAzureClientRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteazureclientrequest)`   
DeleteAzureClientRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### deleteAzureCluster(request, callback)
    
    
    public deleteAzureCluster(request: google.cloud.gkemulticloud.v1.IDeleteAzureClusterRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureClusterCallback): void;

Calls DeleteAzureCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteazureclusterrequest)`   
DeleteAzureClusterRequest message or plain object  
`callback` |  `[DeleteAzureClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAzureCluster(request)
    
    
    public deleteAzureCluster(request: google.cloud.gkemulticloud.v1.IDeleteAzureClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteAzureCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteazureclusterrequest)`   
DeleteAzureClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### deleteAzureNodePool(request, callback)
    
    
    public deleteAzureNodePool(request: google.cloud.gkemulticloud.v1.IDeleteAzureNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureNodePoolCallback): void;

Calls DeleteAzureNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteazurenodepoolrequest)`   
DeleteAzureNodePoolRequest message or plain object  
`callback` |  `[DeleteAzureNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAzureNodePool(request)
    
    
    public deleteAzureNodePool(request: google.cloud.gkemulticloud.v1.IDeleteAzureNodePoolRequest): Promise<google.longrunning.Operation>;

Calls DeleteAzureNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteazurenodepoolrequest)`   
DeleteAzureNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### generateAzureAccessToken(request, callback)
    
    
    public generateAzureAccessToken(request: google.cloud.gkemulticloud.v1.IGenerateAzureAccessTokenRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GenerateAzureAccessTokenCallback): void;

Calls GenerateAzureAccessToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAzureAccessTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateazureaccesstokenrequest)`   
GenerateAzureAccessTokenRequest message or plain object  
`callback` |  `[GenerateAzureAccessTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateAzureAccessTokenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAzureAccessToken(request)
    
    
    public generateAzureAccessToken(request: google.cloud.gkemulticloud.v1.IGenerateAzureAccessTokenRequest): Promise<google.cloud.gkemulticloud.v1.GenerateAzureAccessTokenResponse>;

Calls GenerateAzureAccessToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAzureAccessTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateazureaccesstokenrequest)`   
GenerateAzureAccessTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.GenerateAzureAccessTokenResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateazureaccesstokenresponse)>` | Promise  
  
### generateAzureClusterAgentToken(request, callback)
    
    
    public generateAzureClusterAgentToken(request: google.cloud.gkemulticloud.v1.IGenerateAzureClusterAgentTokenRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GenerateAzureClusterAgentTokenCallback): void;

Calls GenerateAzureClusterAgentToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAzureClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateazureclusteragenttokenrequest)`   
GenerateAzureClusterAgentTokenRequest message or plain object  
`callback` |  `[GenerateAzureClusterAgentTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateAzureClusterAgentTokenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAzureClusterAgentToken(request)
    
    
    public generateAzureClusterAgentToken(request: google.cloud.gkemulticloud.v1.IGenerateAzureClusterAgentTokenRequest): Promise<google.cloud.gkemulticloud.v1.GenerateAzureClusterAgentTokenResponse>;

Calls GenerateAzureClusterAgentToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAzureClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateazureclusteragenttokenrequest)`   
GenerateAzureClusterAgentTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.GenerateAzureClusterAgentTokenResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateazureclusteragenttokenresponse)>` | Promise  
  
### getAzureClient(request, callback)
    
    
    public getAzureClient(request: google.cloud.gkemulticloud.v1.IGetAzureClientRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GetAzureClientCallback): void;

Calls GetAzureClient.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureClientRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureclientrequest)`   
GetAzureClientRequest message or plain object  
`callback` |  `[GetAzureClientCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AzureClient  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAzureClient(request)
    
    
    public getAzureClient(request: google.cloud.gkemulticloud.v1.IGetAzureClientRequest): Promise<google.cloud.gkemulticloud.v1.AzureClient>;

Calls GetAzureClient.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureClientRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureclientrequest)`   
GetAzureClientRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AzureClient](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azureclient)>` | Promise  
  
### getAzureCluster(request, callback)
    
    
    public getAzureCluster(request: google.cloud.gkemulticloud.v1.IGetAzureClusterRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GetAzureClusterCallback): void;

Calls GetAzureCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureclusterrequest)`   
GetAzureClusterRequest message or plain object  
`callback` |  `[GetAzureClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AzureCluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAzureCluster(request)
    
    
    public getAzureCluster(request: google.cloud.gkemulticloud.v1.IGetAzureClusterRequest): Promise<google.cloud.gkemulticloud.v1.AzureCluster>;

Calls GetAzureCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureclusterrequest)`   
GetAzureClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class)>` | Promise  
  
### getAzureJsonWebKeys(request, callback)
    
    
    public getAzureJsonWebKeys(request: google.cloud.gkemulticloud.v1.IGetAzureJsonWebKeysRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GetAzureJsonWebKeysCallback): void;

Calls GetAzureJsonWebKeys.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureJsonWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazurejsonwebkeysrequest)`   
GetAzureJsonWebKeysRequest message or plain object  
`callback` |  `[GetAzureJsonWebKeysCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AzureJsonWebKeys  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAzureJsonWebKeys(request)
    
    
    public getAzureJsonWebKeys(request: google.cloud.gkemulticloud.v1.IGetAzureJsonWebKeysRequest): Promise<google.cloud.gkemulticloud.v1.AzureJsonWebKeys>;

Calls GetAzureJsonWebKeys.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureJsonWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazurejsonwebkeysrequest)`   
GetAzureJsonWebKeysRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AzureJsonWebKeys](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurejsonwebkeys)>` | Promise  
  
### getAzureNodePool(request, callback)
    
    
    public getAzureNodePool(request: google.cloud.gkemulticloud.v1.IGetAzureNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GetAzureNodePoolCallback): void;

Calls GetAzureNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazurenodepoolrequest)`   
GetAzureNodePoolRequest message or plain object  
`callback` |  `[GetAzureNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AzureNodePool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAzureNodePool(request)
    
    
    public getAzureNodePool(request: google.cloud.gkemulticloud.v1.IGetAzureNodePoolRequest): Promise<google.cloud.gkemulticloud.v1.AzureNodePool>;

Calls GetAzureNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazurenodepoolrequest)`   
GetAzureNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class)>` | Promise  
  
### getAzureOpenIdConfig(request, callback)
    
    
    public getAzureOpenIdConfig(request: google.cloud.gkemulticloud.v1.IGetAzureOpenIdConfigRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GetAzureOpenIdConfigCallback): void;

Calls GetAzureOpenIdConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureOpenIdConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureopenidconfigrequest)`   
GetAzureOpenIdConfigRequest message or plain object  
`callback` |  `[GetAzureOpenIdConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AzureOpenIdConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAzureOpenIdConfig(request)
    
    
    public getAzureOpenIdConfig(request: google.cloud.gkemulticloud.v1.IGetAzureOpenIdConfigRequest): Promise<google.cloud.gkemulticloud.v1.AzureOpenIdConfig>;

Calls GetAzureOpenIdConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureOpenIdConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureopenidconfigrequest)`   
GetAzureOpenIdConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AzureOpenIdConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azureopenidconfig)>` | Promise  
  
### getAzureServerConfig(request, callback)
    
    
    public getAzureServerConfig(request: google.cloud.gkemulticloud.v1.IGetAzureServerConfigRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.GetAzureServerConfigCallback): void;

Calls GetAzureServerConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureserverconfigrequest)`   
GetAzureServerConfigRequest message or plain object  
`callback` |  `[GetAzureServerConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AzureServerConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAzureServerConfig(request)
    
    
    public getAzureServerConfig(request: google.cloud.gkemulticloud.v1.IGetAzureServerConfigRequest): Promise<google.cloud.gkemulticloud.v1.AzureServerConfig>;

Calls GetAzureServerConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAzureServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetazureserverconfigrequest)`   
GetAzureServerConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AzureServerConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azureserverconfig)>` | Promise  
  
### listAzureClients(request, callback)
    
    
    public listAzureClients(request: google.cloud.gkemulticloud.v1.IListAzureClientsRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClientsCallback): void;

Calls ListAzureClients.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAzureClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistazureclientsrequest)`   
ListAzureClientsRequest message or plain object  
`callback` |  `[ListAzureClientsCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAzureClientsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAzureClients(request)
    
    
    public listAzureClients(request: google.cloud.gkemulticloud.v1.IListAzureClientsRequest): Promise<google.cloud.gkemulticloud.v1.ListAzureClientsResponse>;

Calls ListAzureClients.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAzureClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistazureclientsrequest)`   
ListAzureClientsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.ListAzureClientsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.listazureclientsresponse)>` | Promise  
  
### listAzureClusters(request, callback)
    
    
    public listAzureClusters(request: google.cloud.gkemulticloud.v1.IListAzureClustersRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClustersCallback): void;

Calls ListAzureClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAzureClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistazureclustersrequest)`   
ListAzureClustersRequest message or plain object  
`callback` |  `[ListAzureClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAzureClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAzureClusters(request)
    
    
    public listAzureClusters(request: google.cloud.gkemulticloud.v1.IListAzureClustersRequest): Promise<google.cloud.gkemulticloud.v1.ListAzureClustersResponse>;

Calls ListAzureClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAzureClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistazureclustersrequest)`   
ListAzureClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.ListAzureClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.listazureclustersresponse)>` | Promise  
  
### listAzureNodePools(request, callback)
    
    
    public listAzureNodePools(request: google.cloud.gkemulticloud.v1.IListAzureNodePoolsRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.ListAzureNodePoolsCallback): void;

Calls ListAzureNodePools.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAzureNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistazurenodepoolsrequest)`   
ListAzureNodePoolsRequest message or plain object  
`callback` |  `[ListAzureNodePoolsCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAzureNodePoolsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAzureNodePools(request)
    
    
    public listAzureNodePools(request: google.cloud.gkemulticloud.v1.IListAzureNodePoolsRequest): Promise<google.cloud.gkemulticloud.v1.ListAzureNodePoolsResponse>;

Calls ListAzureNodePools.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAzureNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistazurenodepoolsrequest)`   
ListAzureNodePoolsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.ListAzureNodePoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.listazurenodepoolsresponse)>` | Promise  
  
### updateAzureCluster(request, callback)
    
    
    public updateAzureCluster(request: google.cloud.gkemulticloud.v1.IUpdateAzureClusterRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureClusterCallback): void;

Calls UpdateAzureCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateazureclusterrequest)`   
UpdateAzureClusterRequest message or plain object  
`callback` |  `[UpdateAzureClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAzureCluster(request)
    
    
    public updateAzureCluster(request: google.cloud.gkemulticloud.v1.IUpdateAzureClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateAzureCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAzureClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateazureclusterrequest)`   
UpdateAzureClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### updateAzureNodePool(request, callback)
    
    
    public updateAzureNodePool(request: google.cloud.gkemulticloud.v1.IUpdateAzureNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureNodePoolCallback): void;

Calls UpdateAzureNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateazurenodepoolrequest)`   
UpdateAzureNodePoolRequest message or plain object  
`callback` |  `[UpdateAzureNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAzureNodePool(request)
    
    
    public updateAzureNodePool(request: google.cloud.gkemulticloud.v1.IUpdateAzureNodePoolRequest): Promise<google.longrunning.Operation>;

Calls UpdateAzureNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAzureNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateazurenodepoolrequest)`   
UpdateAzureNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
