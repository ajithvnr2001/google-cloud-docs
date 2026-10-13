---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedclusters-class
title: Class protos.google.cloud.gkemulticloud.v1.AttachedClusters (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:38.530463+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AttachedClusters (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedclusters-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AttachedClusters (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AttachedClusters

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.gkemulticloud.v1.AttachedClusters

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AttachedClusters service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AttachedClusters;

Creates new AttachedClusters service using the specified rpc implementation.

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
`[AttachedClusters](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedclusters-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAttachedCluster(request, callback)
    
    
    public createAttachedCluster(request: google.cloud.gkemulticloud.v1.ICreateAttachedClusterRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.CreateAttachedClusterCallback): void;

Calls CreateAttachedCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateattachedclusterrequest)`   
CreateAttachedClusterRequest message or plain object  
`callback` |  `[CreateAttachedClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAttachedCluster(request)
    
    
    public createAttachedCluster(request: google.cloud.gkemulticloud.v1.ICreateAttachedClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateAttachedCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.icreateattachedclusterrequest)`   
CreateAttachedClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### deleteAttachedCluster(request, callback)
    
    
    public deleteAttachedCluster(request: google.cloud.gkemulticloud.v1.IDeleteAttachedClusterRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.DeleteAttachedClusterCallback): void;

Calls DeleteAttachedCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteattachedclusterrequest)`   
DeleteAttachedClusterRequest message or plain object  
`callback` |  `[DeleteAttachedClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAttachedCluster(request)
    
    
    public deleteAttachedCluster(request: google.cloud.gkemulticloud.v1.IDeleteAttachedClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteAttachedCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ideleteattachedclusterrequest)`   
DeleteAttachedClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### generateAttachedClusterAgentToken(request, callback)
    
    
    public generateAttachedClusterAgentToken(request: google.cloud.gkemulticloud.v1.IGenerateAttachedClusterAgentTokenRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.GenerateAttachedClusterAgentTokenCallback): void;

Calls GenerateAttachedClusterAgentToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAttachedClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateattachedclusteragenttokenrequest)`   
GenerateAttachedClusterAgentTokenRequest message or plain object  
`callback` |  `[GenerateAttachedClusterAgentTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateAttachedClusterAgentTokenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAttachedClusterAgentToken(request)
    
    
    public generateAttachedClusterAgentToken(request: google.cloud.gkemulticloud.v1.IGenerateAttachedClusterAgentTokenRequest): Promise<google.cloud.gkemulticloud.v1.GenerateAttachedClusterAgentTokenResponse>;

Calls GenerateAttachedClusterAgentToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAttachedClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateattachedclusteragenttokenrequest)`   
GenerateAttachedClusterAgentTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.GenerateAttachedClusterAgentTokenResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateattachedclusteragenttokenresponse)>` | Promise  
  
### generateAttachedClusterInstallManifest(request, callback)
    
    
    public generateAttachedClusterInstallManifest(request: google.cloud.gkemulticloud.v1.IGenerateAttachedClusterInstallManifestRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.GenerateAttachedClusterInstallManifestCallback): void;

Calls GenerateAttachedClusterInstallManifest.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAttachedClusterInstallManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateattachedclusterinstallmanifestrequest)`   
GenerateAttachedClusterInstallManifestRequest message or plain object  
`callback` |  `[GenerateAttachedClusterInstallManifestCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateAttachedClusterInstallManifestResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAttachedClusterInstallManifest(request)
    
    
    public generateAttachedClusterInstallManifest(request: google.cloud.gkemulticloud.v1.IGenerateAttachedClusterInstallManifestRequest): Promise<google.cloud.gkemulticloud.v1.GenerateAttachedClusterInstallManifestResponse>;

Calls GenerateAttachedClusterInstallManifest.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAttachedClusterInstallManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateattachedclusterinstallmanifestrequest)`   
GenerateAttachedClusterInstallManifestRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.GenerateAttachedClusterInstallManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateattachedclusterinstallmanifestresponse)>` | Promise  
  
### getAttachedCluster(request, callback)
    
    
    public getAttachedCluster(request: google.cloud.gkemulticloud.v1.IGetAttachedClusterRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedClusterCallback): void;

Calls GetAttachedCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetattachedclusterrequest)`   
GetAttachedClusterRequest message or plain object  
`callback` |  `[GetAttachedClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AttachedCluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAttachedCluster(request)
    
    
    public getAttachedCluster(request: google.cloud.gkemulticloud.v1.IGetAttachedClusterRequest): Promise<google.cloud.gkemulticloud.v1.AttachedCluster>;

Calls GetAttachedCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetattachedclusterrequest)`   
GetAttachedClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class)>` | Promise  
  
### getAttachedServerConfig(request, callback)
    
    
    public getAttachedServerConfig(request: google.cloud.gkemulticloud.v1.IGetAttachedServerConfigRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedServerConfigCallback): void;

Calls GetAttachedServerConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttachedServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetattachedserverconfigrequest)`   
GetAttachedServerConfigRequest message or plain object  
`callback` |  `[GetAttachedServerConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and AttachedServerConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAttachedServerConfig(request)
    
    
    public getAttachedServerConfig(request: google.cloud.gkemulticloud.v1.IGetAttachedServerConfigRequest): Promise<google.cloud.gkemulticloud.v1.AttachedServerConfig>;

Calls GetAttachedServerConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAttachedServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igetattachedserverconfigrequest)`   
GetAttachedServerConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.AttachedServerConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedserverconfig)>` | Promise  
  
### importAttachedCluster(request, callback)
    
    
    public importAttachedCluster(request: google.cloud.gkemulticloud.v1.IImportAttachedClusterRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.ImportAttachedClusterCallback): void;

Calls ImportAttachedCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iimportattachedclusterrequest)`   
ImportAttachedClusterRequest message or plain object  
`callback` |  `[ImportAttachedClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importAttachedCluster(request)
    
    
    public importAttachedCluster(request: google.cloud.gkemulticloud.v1.IImportAttachedClusterRequest): Promise<google.longrunning.Operation>;

Calls ImportAttachedCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iimportattachedclusterrequest)`   
ImportAttachedClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
### listAttachedClusters(request, callback)
    
    
    public listAttachedClusters(request: google.cloud.gkemulticloud.v1.IListAttachedClustersRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.ListAttachedClustersCallback): void;

Calls ListAttachedClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttachedClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistattachedclustersrequest)`   
ListAttachedClustersRequest message or plain object  
`callback` |  `[ListAttachedClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAttachedClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAttachedClusters(request)
    
    
    public listAttachedClusters(request: google.cloud.gkemulticloud.v1.IListAttachedClustersRequest): Promise<google.cloud.gkemulticloud.v1.ListAttachedClustersResponse>;

Calls ListAttachedClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAttachedClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.ilistattachedclustersrequest)`   
ListAttachedClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkemulticloud.v1.ListAttachedClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.listattachedclustersresponse)>` | Promise  
  
### updateAttachedCluster(request, callback)
    
    
    public updateAttachedCluster(request: google.cloud.gkemulticloud.v1.IUpdateAttachedClusterRequest, callback: google.cloud.gkemulticloud.v1.AttachedClusters.UpdateAttachedClusterCallback): void;

Calls UpdateAttachedCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateattachedclusterrequest)`   
UpdateAttachedClusterRequest message or plain object  
`callback` |  `[UpdateAttachedClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAttachedCluster(request)
    
    
    public updateAttachedCluster(request: google.cloud.gkemulticloud.v1.IUpdateAttachedClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateAttachedCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttachedClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iupdateattachedclusterrequest)`   
UpdateAttachedClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
