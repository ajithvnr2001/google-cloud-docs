---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsclusters-class
title: Class protos.google.cloud.gkemulticloud.v1.AwsClusters (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:40.780657+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AwsClusters (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsclusters-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AwsClusters (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AwsClusters

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.gkemulticloud.v1.AwsClusters

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AwsClusters service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AwsClusters;

Creates new AwsClusters service using the specified rpc implementation.

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
`[AwsClusters](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsclusters-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAwsCluster(request, callback)
    
    
    public createAwsCluster(request: google.cloud.gkemulticloud.v1.ICreateAwsClusterRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsClusterCallback): void;

Calls CreateAwsCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateawsclusterrequest)`   
CreateAwsClusterRequest message or plain object  
`callback` |  `[CreateAwsClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAwsCluster(request)
    
    
    public createAwsCluster(request: google.cloud.gkemulticloud.v1.ICreateAwsClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateAwsCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateawsclusterrequest)`   
CreateAwsClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### createAwsNodePool(request, callback)
    
    
    public createAwsNodePool(request: google.cloud.gkemulticloud.v1.ICreateAwsNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsNodePoolCallback): void;

Calls CreateAwsNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateawsnodepoolrequest)`   
CreateAwsNodePoolRequest message or plain object  
`callback` |  `[CreateAwsNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAwsNodePool(request)
    
    
    public createAwsNodePool(request: google.cloud.gkemulticloud.v1.ICreateAwsNodePoolRequest): Promise<google.longrunning.Operation>;

Calls CreateAwsNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateawsnodepoolrequest)`   
CreateAwsNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### deleteAwsCluster(request, callback)
    
    
    public deleteAwsCluster(request: google.cloud.gkemulticloud.v1.IDeleteAwsClusterRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsClusterCallback): void;

Calls DeleteAwsCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteawsclusterrequest)`   
DeleteAwsClusterRequest message or plain object  
`callback` |  `[DeleteAwsClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAwsCluster(request)
    
    
    public deleteAwsCluster(request: google.cloud.gkemulticloud.v1.IDeleteAwsClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteAwsCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteawsclusterrequest)`   
DeleteAwsClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### deleteAwsNodePool(request, callback)
    
    
    public deleteAwsNodePool(request: google.cloud.gkemulticloud.v1.IDeleteAwsNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsNodePoolCallback): void;

Calls DeleteAwsNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteawsnodepoolrequest)`   
DeleteAwsNodePoolRequest message or plain object  
`callback` |  `[DeleteAwsNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAwsNodePool(request)
    
    
    public deleteAwsNodePool(request: google.cloud.gkemulticloud.v1.IDeleteAwsNodePoolRequest): Promise<google.longrunning.Operation>;

Calls DeleteAwsNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteawsnodepoolrequest)`   
DeleteAwsNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### generateAwsAccessToken(request, callback)
    
    
    public generateAwsAccessToken(request: google.cloud.gkemulticloud.v1.IGenerateAwsAccessTokenRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.GenerateAwsAccessTokenCallback): void;

Calls GenerateAwsAccessToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAwsAccessTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsaccesstokenrequest)`   
GenerateAwsAccessTokenRequest message or plain object  
`callback` |  `[GenerateAwsAccessTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateAwsAccessTokenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAwsAccessToken(request)
    
    
    public generateAwsAccessToken(request: google.cloud.gkemulticloud.v1.IGenerateAwsAccessTokenRequest): Promise<google.cloud.gkemulticloud.v1.GenerateAwsAccessTokenResponse>;

Calls GenerateAwsAccessToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAwsAccessTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsaccesstokenrequest)`   
GenerateAwsAccessTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.GenerateAwsAccessTokenResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsaccesstokenresponse)>` | Promise  
  
### generateAwsClusterAgentToken(request, callback)
    
    
    public generateAwsClusterAgentToken(request: google.cloud.gkemulticloud.v1.IGenerateAwsClusterAgentTokenRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.GenerateAwsClusterAgentTokenCallback): void;

Calls GenerateAwsClusterAgentToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsclusteragenttokenrequest)`   
GenerateAwsClusterAgentTokenRequest message or plain object  
`callback` |  `[GenerateAwsClusterAgentTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateAwsClusterAgentTokenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAwsClusterAgentToken(request)
    
    
    public generateAwsClusterAgentToken(request: google.cloud.gkemulticloud.v1.IGenerateAwsClusterAgentTokenRequest): Promise<google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenResponse>;

Calls GenerateAwsClusterAgentToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsclusteragenttokenrequest)`   
GenerateAwsClusterAgentTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenresponse)>` | Promise  
  
### getAwsCluster(request, callback)
    
    
    public getAwsCluster(request: google.cloud.gkemulticloud.v1.IGetAwsClusterRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.GetAwsClusterCallback): void;

Calls GetAwsCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsclusterrequest)`   
GetAwsClusterRequest message or plain object  
`callback` |  `[GetAwsClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AwsCluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAwsCluster(request)
    
    
    public getAwsCluster(request: google.cloud.gkemulticloud.v1.IGetAwsClusterRequest): Promise<google.cloud.gkemulticloud.v1.AwsCluster>;

Calls GetAwsCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsclusterrequest)`   
GetAwsClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class)>` | Promise  
  
### getAwsJsonWebKeys(request, callback)
    
    
    public getAwsJsonWebKeys(request: google.cloud.gkemulticloud.v1.IGetAwsJsonWebKeysRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.GetAwsJsonWebKeysCallback): void;

Calls GetAwsJsonWebKeys.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsJsonWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsjsonwebkeysrequest)`   
GetAwsJsonWebKeysRequest message or plain object  
`callback` |  `[GetAwsJsonWebKeysCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AwsJsonWebKeys  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAwsJsonWebKeys(request)
    
    
    public getAwsJsonWebKeys(request: google.cloud.gkemulticloud.v1.IGetAwsJsonWebKeysRequest): Promise<google.cloud.gkemulticloud.v1.AwsJsonWebKeys>;

Calls GetAwsJsonWebKeys.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsJsonWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsjsonwebkeysrequest)`   
GetAwsJsonWebKeysRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AwsJsonWebKeys](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsjsonwebkeys)>` | Promise  
  
### getAwsNodePool(request, callback)
    
    
    public getAwsNodePool(request: google.cloud.gkemulticloud.v1.IGetAwsNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.GetAwsNodePoolCallback): void;

Calls GetAwsNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsnodepoolrequest)`   
GetAwsNodePoolRequest message or plain object  
`callback` |  `[GetAwsNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AwsNodePool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAwsNodePool(request)
    
    
    public getAwsNodePool(request: google.cloud.gkemulticloud.v1.IGetAwsNodePoolRequest): Promise<google.cloud.gkemulticloud.v1.AwsNodePool>;

Calls GetAwsNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsnodepoolrequest)`   
GetAwsNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AwsNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodepool-class)>` | Promise  
  
### getAwsOpenIdConfig(request, callback)
    
    
    public getAwsOpenIdConfig(request: google.cloud.gkemulticloud.v1.IGetAwsOpenIdConfigRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.GetAwsOpenIdConfigCallback): void;

Calls GetAwsOpenIdConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsOpenIdConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsopenidconfigrequest)`   
GetAwsOpenIdConfigRequest message or plain object  
`callback` |  `[GetAwsOpenIdConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AwsOpenIdConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAwsOpenIdConfig(request)
    
    
    public getAwsOpenIdConfig(request: google.cloud.gkemulticloud.v1.IGetAwsOpenIdConfigRequest): Promise<google.cloud.gkemulticloud.v1.AwsOpenIdConfig>;

Calls GetAwsOpenIdConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsOpenIdConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsopenidconfigrequest)`   
GetAwsOpenIdConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AwsOpenIdConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsopenidconfig)>` | Promise  
  
### getAwsServerConfig(request, callback)
    
    
    public getAwsServerConfig(request: google.cloud.gkemulticloud.v1.IGetAwsServerConfigRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.GetAwsServerConfigCallback): void;

Calls GetAwsServerConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsserverconfigrequest)`   
GetAwsServerConfigRequest message or plain object  
`callback` |  `[GetAwsServerConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AwsServerConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAwsServerConfig(request)
    
    
    public getAwsServerConfig(request: google.cloud.gkemulticloud.v1.IGetAwsServerConfigRequest): Promise<google.cloud.gkemulticloud.v1.AwsServerConfig>;

Calls GetAwsServerConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAwsServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetawsserverconfigrequest)`   
GetAwsServerConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AwsServerConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsserverconfig)>` | Promise  
  
### listAwsClusters(request, callback)
    
    
    public listAwsClusters(request: google.cloud.gkemulticloud.v1.IListAwsClustersRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.ListAwsClustersCallback): void;

Calls ListAwsClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAwsClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistawsclustersrequest)`   
ListAwsClustersRequest message or plain object  
`callback` |  `[ListAwsClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAwsClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAwsClusters(request)
    
    
    public listAwsClusters(request: google.cloud.gkemulticloud.v1.IListAwsClustersRequest): Promise<google.cloud.gkemulticloud.v1.ListAwsClustersResponse>;

Calls ListAwsClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAwsClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistawsclustersrequest)`   
ListAwsClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.ListAwsClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.listawsclustersresponse)>` | Promise  
  
### listAwsNodePools(request, callback)
    
    
    public listAwsNodePools(request: google.cloud.gkemulticloud.v1.IListAwsNodePoolsRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.ListAwsNodePoolsCallback): void;

Calls ListAwsNodePools.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAwsNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistawsnodepoolsrequest)`   
ListAwsNodePoolsRequest message or plain object  
`callback` |  `[ListAwsNodePoolsCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAwsNodePoolsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAwsNodePools(request)
    
    
    public listAwsNodePools(request: google.cloud.gkemulticloud.v1.IListAwsNodePoolsRequest): Promise<google.cloud.gkemulticloud.v1.ListAwsNodePoolsResponse>;

Calls ListAwsNodePools.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAwsNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistawsnodepoolsrequest)`   
ListAwsNodePoolsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.ListAwsNodePoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.listawsnodepoolsresponse)>` | Promise  
  
### rollbackAwsNodePoolUpdate(request, callback)
    
    
    public rollbackAwsNodePoolUpdate(request: google.cloud.gkemulticloud.v1.IRollbackAwsNodePoolUpdateRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.RollbackAwsNodePoolUpdateCallback): void;

Calls RollbackAwsNodePoolUpdate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackAwsNodePoolUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.irollbackawsnodepoolupdaterequest)`   
RollbackAwsNodePoolUpdateRequest message or plain object  
`callback` |  `[RollbackAwsNodePoolUpdateCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rollbackAwsNodePoolUpdate(request)
    
    
    public rollbackAwsNodePoolUpdate(request: google.cloud.gkemulticloud.v1.IRollbackAwsNodePoolUpdateRequest): Promise<google.longrunning.Operation>;

Calls RollbackAwsNodePoolUpdate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRollbackAwsNodePoolUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.irollbackawsnodepoolupdaterequest)`   
RollbackAwsNodePoolUpdateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### updateAwsCluster(request, callback)
    
    
    public updateAwsCluster(request: google.cloud.gkemulticloud.v1.IUpdateAwsClusterRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsClusterCallback): void;

Calls UpdateAwsCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateawsclusterrequest)`   
UpdateAwsClusterRequest message or plain object  
`callback` |  `[UpdateAwsClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAwsCluster(request)
    
    
    public updateAwsCluster(request: google.cloud.gkemulticloud.v1.IUpdateAwsClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateAwsCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAwsClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateawsclusterrequest)`   
UpdateAwsClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### updateAwsNodePool(request, callback)
    
    
    public updateAwsNodePool(request: google.cloud.gkemulticloud.v1.IUpdateAwsNodePoolRequest, callback: google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsNodePoolCallback): void;

Calls UpdateAwsNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateawsnodepoolrequest)`   
UpdateAwsNodePoolRequest message or plain object  
`callback` |  `[UpdateAwsNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAwsNodePool(request)
    
    
    public updateAwsNodePool(request: google.cloud.gkemulticloud.v1.IUpdateAwsNodePoolRequest): Promise<google.longrunning.Operation>;

Calls UpdateAwsNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAwsNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateawsnodepoolrequest)`   
UpdateAwsNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
