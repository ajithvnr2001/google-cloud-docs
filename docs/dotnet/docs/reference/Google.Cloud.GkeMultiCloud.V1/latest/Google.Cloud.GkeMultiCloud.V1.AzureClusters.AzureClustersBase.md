---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureClusters.AzureClustersBase
title: Anthos Multi-Cloud v1 API - Class AzureClusters.AzureClustersBase (2.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:27.977795+00:00
---

# Anthos Multi-Cloud v1 API - Class AzureClusters.AzureClustersBase (2.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureClusters.AzureClustersBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Anthos Multi-Cloud v1 API - Class AzureClusters.AzureClustersBase (2.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.0 (latest)  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0-beta01 
    
    
    [Obsolete]
    [BindServiceMethod(typeof(AzureClusters), "BindService")]
    public abstract class AzureClusters.AzureClustersBase

Reference documentation and code samples for the Anthos Multi-Cloud v1 API class AzureClusters.AzureClustersBase.

Base class for server-side implementations of AzureClusters

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AzureClusters.AzureClustersBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeMultiCloud.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1)

## Assembly

Google.Cloud.GkeMultiCloud.V1.dll

## Methods 

### CreateAzureClient(CreateAzureClientRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> CreateAzureClient(CreateAzureClientRequest request, ServerCallContext context)

Creates a new [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] resource on a given Google Cloud project and region.

`AzureClient` resources hold client authentication information needed by the Anthos Multicloud API to manage Azure resources on your Azure subscription on your behalf.

If successful, the response contains a newly created [Operation][google.longrunning.Operation] resource that can be described to track the status of the operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAzureClientRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.CreateAzureClientRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateAzureCluster(CreateAzureClusterRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> CreateAzureCluster(CreateAzureClusterRequest request, ServerCallContext context)

Creates a new [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster] resource on a given Google Cloud Platform project and region.

If successful, the response contains a newly created [Operation][google.longrunning.Operation] resource that can be described to track the status of the operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAzureClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.CreateAzureClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateAzureNodePool(CreateAzureNodePoolRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> CreateAzureNodePool(CreateAzureNodePoolRequest request, ServerCallContext context)

Creates a new [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool], attached to a given [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

If successful, the response contains a newly created [Operation][google.longrunning.Operation] resource that can be described to track the status of the operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAzureNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.CreateAzureNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAzureClient(DeleteAzureClientRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> DeleteAzureClient(DeleteAzureClientRequest request, ServerCallContext context)

Deletes a specific [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] resource.

If the client is used by one or more clusters, deletion will fail and a `FAILED_PRECONDITION` error will be returned.

If successful, the response contains a newly created [Operation][google.longrunning.Operation] resource that can be described to track the status of the operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAzureClientRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAzureClientRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAzureCluster(DeleteAzureClusterRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> DeleteAzureCluster(DeleteAzureClusterRequest request, ServerCallContext context)

Deletes a specific [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster] resource.

Fails if the cluster has one or more associated [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool] resources.

If successful, the response contains a newly created [Operation][google.longrunning.Operation] resource that can be described to track the status of the operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAzureClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAzureClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAzureNodePool(DeleteAzureNodePoolRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> DeleteAzureNodePool(DeleteAzureNodePoolRequest request, ServerCallContext context)

Deletes a specific [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool] resource.

If successful, the response contains a newly created [Operation][google.longrunning.Operation] resource that can be described to track the status of the operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAzureNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAzureNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GenerateAzureAccessToken(GenerateAzureAccessTokenRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<GenerateAzureAccessTokenResponse> GenerateAzureAccessToken(GenerateAzureAccessTokenRequest request, ServerCallContext context)

Generates a short-lived access token to authenticate to a given [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster] resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAzureAccessTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GenerateAzureAccessTokenRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateAzureAccessTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GenerateAzureAccessTokenResponse)` | The response to send back to the client (wrapped by a task).  
  
### GenerateAzureClusterAgentToken(GenerateAzureClusterAgentTokenRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<GenerateAzureClusterAgentTokenResponse> GenerateAzureClusterAgentToken(GenerateAzureClusterAgentTokenRequest request, ServerCallContext context)

Generates an access token for a cluster agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAzureClusterAgentTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GenerateAzureClusterAgentTokenRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateAzureClusterAgentTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GenerateAzureClusterAgentTokenResponse)` | The response to send back to the client (wrapped by a task).  
  
### GetAzureClient(GetAzureClientRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<AzureClient> GetAzureClient(GetAzureClientRequest request, ServerCallContext context)

Describes a specific [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAzureClientRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GetAzureClientRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AzureClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureClient)` | The response to send back to the client (wrapped by a task).  
  
### GetAzureCluster(GetAzureClusterRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<AzureCluster> GetAzureCluster(GetAzureClusterRequest request, ServerCallContext context)

Describes a specific [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster] resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAzureClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GetAzureClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AzureCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureCluster)` | The response to send back to the client (wrapped by a task).  
  
### GetAzureJsonWebKeys(GetAzureJsonWebKeysRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<AzureJsonWebKeys> GetAzureJsonWebKeys(GetAzureJsonWebKeysRequest request, ServerCallContext context)

Gets the public component of the cluster signing keys in JSON Web Key format.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAzureJsonWebKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GetAzureJsonWebKeysRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AzureJsonWebKeys](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureJsonWebKeys)` | The response to send back to the client (wrapped by a task).  
  
### GetAzureNodePool(GetAzureNodePoolRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<AzureNodePool> GetAzureNodePool(GetAzureNodePoolRequest request, ServerCallContext context)

Describes a specific [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool] resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAzureNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GetAzureNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AzureNodePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureNodePool)` | The response to send back to the client (wrapped by a task).  
  
### GetAzureOpenIdConfig(GetAzureOpenIdConfigRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<AzureOpenIdConfig> GetAzureOpenIdConfig(GetAzureOpenIdConfigRequest request, ServerCallContext context)

Gets the OIDC discovery document for the cluster. See the [OpenID Connect Discovery 1.0 specification](https://openid.net/specs/openid-connect-discovery-1_0.html) for details.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAzureOpenIdConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GetAzureOpenIdConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AzureOpenIdConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureOpenIdConfig)` | The response to send back to the client (wrapped by a task).  
  
### GetAzureServerConfig(GetAzureServerConfigRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<AzureServerConfig> GetAzureServerConfig(GetAzureServerConfigRequest request, ServerCallContext context)

Returns information, such as supported Azure regions and Kubernetes versions, on a given Google Cloud location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAzureServerConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.GetAzureServerConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AzureServerConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureServerConfig)` | The response to send back to the client (wrapped by a task).  
  
### ListAzureClients(ListAzureClientsRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<ListAzureClientsResponse> ListAzureClients(ListAzureClientsRequest request, ServerCallContext context)

Lists all [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] resources on a given Google Cloud project and region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAzureClientsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ListAzureClientsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAzureClientsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ListAzureClientsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListAzureClusters(ListAzureClustersRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<ListAzureClustersResponse> ListAzureClusters(ListAzureClustersRequest request, ServerCallContext context)

Lists all [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster] resources on a given Google Cloud project and region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAzureClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ListAzureClustersRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAzureClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ListAzureClustersResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListAzureNodePools(ListAzureNodePoolsRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<ListAzureNodePoolsResponse> ListAzureNodePools(ListAzureNodePoolsRequest request, ServerCallContext context)

Lists all [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool] resources on a given [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAzureNodePoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ListAzureNodePoolsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAzureNodePoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ListAzureNodePoolsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateAzureCluster(UpdateAzureClusterRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> UpdateAzureCluster(UpdateAzureClusterRequest request, ServerCallContext context)

Updates an [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAzureClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAzureClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateAzureNodePool(UpdateAzureNodePoolRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> UpdateAzureNodePool(UpdateAzureNodePoolRequest request, ServerCallContext context)

Updates an [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAzureNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAzureNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-26 UTC."],[],[]] 
