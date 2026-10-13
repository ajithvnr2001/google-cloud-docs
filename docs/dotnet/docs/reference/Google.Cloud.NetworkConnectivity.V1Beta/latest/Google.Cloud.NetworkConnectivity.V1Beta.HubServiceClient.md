---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient
title: Network Connectivity v1beta API - Class HubServiceClient (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:09.642091+00:00
---

# Network Connectivity v1beta API - Class HubServiceClient (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Class HubServiceClient (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public abstract class HubServiceClient

Reference documentation and code samples for the Network Connectivity v1beta API class HubServiceClient.

HubService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > HubServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[HubServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClientImpl)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Remarks

Network Connectivity Center is a hub-and-spoke abstraction for network connectivity management in Google Cloud. It reduces operational complexity through a simple, centralized connectivity management model.

## Properties 

### AcceptHubSpokeOperationsClient
    
    
    public virtual OperationsClient AcceptHubSpokeOperationsClient { get; }

The long-running operations client for `AcceptHubSpoke`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### AcceptSpokeUpdateOperationsClient
    
    
    public virtual OperationsClient AcceptSpokeUpdateOperationsClient { get; }

The long-running operations client for `AcceptSpokeUpdate`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateGatewayAdvertisedRouteOperationsClient
    
    
    public virtual OperationsClient CreateGatewayAdvertisedRouteOperationsClient { get; }

The long-running operations client for `CreateGatewayAdvertisedRoute`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateHubOperationsClient
    
    
    public virtual OperationsClient CreateHubOperationsClient { get; }

The long-running operations client for `CreateHub`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateSpokeOperationsClient
    
    
    public virtual OperationsClient CreateSpokeOperationsClient { get; }

The long-running operations client for `CreateSpoke`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the HubService service, which is a host of "networkconnectivity.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default HubService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default HubService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteGatewayAdvertisedRouteOperationsClient
    
    
    public virtual OperationsClient DeleteGatewayAdvertisedRouteOperationsClient { get; }

The long-running operations client for `DeleteGatewayAdvertisedRoute`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteHubOperationsClient
    
    
    public virtual OperationsClient DeleteHubOperationsClient { get; }

The long-running operations client for `DeleteHub`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteSpokeOperationsClient
    
    
    public virtual OperationsClient DeleteSpokeOperationsClient { get; }

The long-running operations client for `DeleteSpoke`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual HubService.HubServiceClient GrpcClient { get; }

The underlying gRPC HubService client

**Property Value**  
---  
**Type** | **Description**  
`[HubService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubService)[HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubService.HubServiceClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### RejectHubSpokeOperationsClient
    
    
    public virtual OperationsClient RejectHubSpokeOperationsClient { get; }

The long-running operations client for `RejectHubSpoke`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### RejectSpokeUpdateOperationsClient
    
    
    public virtual OperationsClient RejectSpokeUpdateOperationsClient { get; }

The long-running operations client for `RejectSpokeUpdate`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### UpdateGatewayAdvertisedRouteOperationsClient
    
    
    public virtual OperationsClient UpdateGatewayAdvertisedRouteOperationsClient { get; }

The long-running operations client for `UpdateGatewayAdvertisedRoute`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateGroupOperationsClient
    
    
    public virtual OperationsClient UpdateGroupOperationsClient { get; }

The long-running operations client for `UpdateGroup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateHubOperationsClient
    
    
    public virtual OperationsClient UpdateHubOperationsClient { get; }

The long-running operations client for `UpdateHub`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateSpokeOperationsClient
    
    
    public virtual OperationsClient UpdateSpokeOperationsClient { get; }

The long-running operations client for `UpdateSpoke`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### AcceptHubSpoke(AcceptHubSpokeRequest, CallSettings)
    
    
    public virtual Operation<AcceptHubSpokeResponse, OperationMetadata> AcceptHubSpoke(AcceptHubSpokeRequest request, CallSettings callSettings = null)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptHubSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    AcceptHubSpokeRequest request = new AcceptHubSpokeRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
    };
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = hubServiceClient.AcceptHubSpoke(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceAcceptHubSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpoke(HubName, SpokeName, CallSettings)
    
    
    public virtual Operation<AcceptHubSpokeResponse, OperationMetadata> AcceptHubSpoke(HubName name, SpokeName spokeUri, CallSettings callSettings = null)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to accept into the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = hubServiceClient.AcceptHubSpoke(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceAcceptHubSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpoke(string, string, CallSettings)
    
    
    public virtual Operation<AcceptHubSpokeResponse, OperationMetadata> AcceptHubSpoke(string name, string spokeUri, CallSettings callSettings = null)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to accept into the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = hubServiceClient.AcceptHubSpoke(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceAcceptHubSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpokeAsync(AcceptHubSpokeRequest, CallSettings)
    
    
    public virtual Task<Operation<AcceptHubSpokeResponse, OperationMetadata>> AcceptHubSpokeAsync(AcceptHubSpokeRequest request, CallSettings callSettings = null)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptHubSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcceptHubSpokeRequest request = new AcceptHubSpokeRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
    };
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = await hubServiceClient.AcceptHubSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpokeAsync(AcceptHubSpokeRequest, CancellationToken)
    
    
    public virtual Task<Operation<AcceptHubSpokeResponse, OperationMetadata>> AcceptHubSpokeAsync(AcceptHubSpokeRequest request, CancellationToken cancellationToken)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptHubSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcceptHubSpokeRequest request = new AcceptHubSpokeRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
    };
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = await hubServiceClient.AcceptHubSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpokeAsync(HubName, SpokeName, CallSettings)
    
    
    public virtual Task<Operation<AcceptHubSpokeResponse, OperationMetadata>> AcceptHubSpokeAsync(HubName name, SpokeName spokeUri, CallSettings callSettings = null)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to accept into the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = await hubServiceClient.AcceptHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpokeAsync(HubName, SpokeName, CancellationToken)
    
    
    public virtual Task<Operation<AcceptHubSpokeResponse, OperationMetadata>> AcceptHubSpokeAsync(HubName name, SpokeName spokeUri, CancellationToken cancellationToken)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to accept into the hub.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = await hubServiceClient.AcceptHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpokeAsync(string, string, CallSettings)
    
    
    public virtual Task<Operation<AcceptHubSpokeResponse, OperationMetadata>> AcceptHubSpokeAsync(string name, string spokeUri, CallSettings callSettings = null)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to accept into the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = await hubServiceClient.AcceptHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptHubSpokeAsync(string, string, CancellationToken)
    
    
    public virtual Task<Operation<AcceptHubSpokeResponse, OperationMetadata>> AcceptHubSpokeAsync(string name, string spokeUri, CancellationToken cancellationToken)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to accept into the hub.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<AcceptHubSpokeResponse, OperationMetadata> response = await hubServiceClient.AcceptHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdate(AcceptSpokeUpdateRequest, CallSettings)
    
    
    public virtual Operation<AcceptSpokeUpdateResponse, OperationMetadata> AcceptSpokeUpdate(AcceptSpokeUpdateRequest request, CallSettings callSettings = null)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    AcceptSpokeUpdateRequest request = new AcceptSpokeUpdateRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        SpokeEtag = "",
        RequestId = "",
    };
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = hubServiceClient.AcceptSpokeUpdate(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceAcceptSpokeUpdate(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdate(HubName, SpokeName, string, CallSettings)
    
    
    public virtual Operation<AcceptSpokeUpdateResponse, OperationMetadata> AcceptSpokeUpdate(HubName name, SpokeName spokeUri, string spokeEtag, CallSettings callSettings = null)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to accept update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    string spokeEtag = "";
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = hubServiceClient.AcceptSpokeUpdate(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceAcceptSpokeUpdate(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdate(string, string, string, CallSettings)
    
    
    public virtual Operation<AcceptSpokeUpdateResponse, OperationMetadata> AcceptSpokeUpdate(string name, string spokeUri, string spokeEtag, CallSettings callSettings = null)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to accept update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    string spokeEtag = "";
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = hubServiceClient.AcceptSpokeUpdate(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceAcceptSpokeUpdate(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdateAsync(AcceptSpokeUpdateRequest, CallSettings)
    
    
    public virtual Task<Operation<AcceptSpokeUpdateResponse, OperationMetadata>> AcceptSpokeUpdateAsync(AcceptSpokeUpdateRequest request, CallSettings callSettings = null)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcceptSpokeUpdateRequest request = new AcceptSpokeUpdateRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        SpokeEtag = "",
        RequestId = "",
    };
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.AcceptSpokeUpdateAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdateAsync(AcceptSpokeUpdateRequest, CancellationToken)
    
    
    public virtual Task<Operation<AcceptSpokeUpdateResponse, OperationMetadata>> AcceptSpokeUpdateAsync(AcceptSpokeUpdateRequest request, CancellationToken cancellationToken)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcceptSpokeUpdateRequest request = new AcceptSpokeUpdateRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        SpokeEtag = "",
        RequestId = "",
    };
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.AcceptSpokeUpdateAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdateAsync(HubName, SpokeName, string, CallSettings)
    
    
    public virtual Task<Operation<AcceptSpokeUpdateResponse, OperationMetadata>> AcceptSpokeUpdateAsync(HubName name, SpokeName spokeUri, string spokeEtag, CallSettings callSettings = null)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to accept update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    string spokeEtag = "";
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.AcceptSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdateAsync(HubName, SpokeName, string, CancellationToken)
    
    
    public virtual Task<Operation<AcceptSpokeUpdateResponse, OperationMetadata>> AcceptSpokeUpdateAsync(HubName name, SpokeName spokeUri, string spokeEtag, CancellationToken cancellationToken)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to accept update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    string spokeEtag = "";
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.AcceptSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdateAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Operation<AcceptSpokeUpdateResponse, OperationMetadata>> AcceptSpokeUpdateAsync(string name, string spokeUri, string spokeEtag, CallSettings callSettings = null)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to accept update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    string spokeEtag = "";
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.AcceptSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### AcceptSpokeUpdateAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<AcceptSpokeUpdateResponse, OperationMetadata>> AcceptSpokeUpdateAsync(string name, string spokeUri, string spokeEtag, CancellationToken cancellationToken)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to accept update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    string spokeEtag = "";
    // Make the request
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.AcceptSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AcceptSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AcceptSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceAcceptSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AcceptSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static HubServiceClient Create()

Synchronously creates a [HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [HubServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient)` | The created [HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<HubServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [HubServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient)` | The task representing the created [HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient).  
  
### CreateGatewayAdvertisedRoute(CreateGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual Operation<GatewayAdvertisedRoute, OperationMetadata> CreateGatewayAdvertisedRoute(CreateGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    CreateGatewayAdvertisedRouteRequest request = new CreateGatewayAdvertisedRouteRequest
    {
        ParentAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        GatewayAdvertisedRouteId = "",
        GatewayAdvertisedRoute = new GatewayAdvertisedRoute(),
        RequestId = "",
    };
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = hubServiceClient.CreateGatewayAdvertisedRoute(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRoute(SpokeName, GatewayAdvertisedRoute, string, CallSettings)
    
    
    public virtual Operation<GatewayAdvertisedRoute, OperationMetadata> CreateGatewayAdvertisedRoute(SpokeName parent, GatewayAdvertisedRoute gatewayAdvertisedRoute, string gatewayAdvertisedRouteId, CallSettings callSettings = null)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The parent resource.  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. Initial values for the new gateway advertised route.  
`gatewayAdvertisedRouteId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the route to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    SpokeName parent = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    string gatewayAdvertisedRouteId = "";
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = hubServiceClient.CreateGatewayAdvertisedRoute(parent, gatewayAdvertisedRoute, gatewayAdvertisedRouteId);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRoute(string, GatewayAdvertisedRoute, string, CallSettings)
    
    
    public virtual Operation<GatewayAdvertisedRoute, OperationMetadata> CreateGatewayAdvertisedRoute(string parent, GatewayAdvertisedRoute gatewayAdvertisedRoute, string gatewayAdvertisedRouteId, CallSettings callSettings = null)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. Initial values for the new gateway advertised route.  
`gatewayAdvertisedRouteId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the route to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    string gatewayAdvertisedRouteId = "";
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = hubServiceClient.CreateGatewayAdvertisedRoute(parent, gatewayAdvertisedRoute, gatewayAdvertisedRouteId);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRouteAsync(CreateGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> CreateGatewayAdvertisedRouteAsync(CreateGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateGatewayAdvertisedRouteRequest request = new CreateGatewayAdvertisedRouteRequest
    {
        ParentAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        GatewayAdvertisedRouteId = "",
        GatewayAdvertisedRoute = new GatewayAdvertisedRoute(),
        RequestId = "",
    };
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.CreateGatewayAdvertisedRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRouteAsync(CreateGatewayAdvertisedRouteRequest, CancellationToken)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> CreateGatewayAdvertisedRouteAsync(CreateGatewayAdvertisedRouteRequest request, CancellationToken cancellationToken)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateGatewayAdvertisedRouteRequest request = new CreateGatewayAdvertisedRouteRequest
    {
        ParentAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        GatewayAdvertisedRouteId = "",
        GatewayAdvertisedRoute = new GatewayAdvertisedRoute(),
        RequestId = "",
    };
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.CreateGatewayAdvertisedRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRouteAsync(SpokeName, GatewayAdvertisedRoute, string, CallSettings)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> CreateGatewayAdvertisedRouteAsync(SpokeName parent, GatewayAdvertisedRoute gatewayAdvertisedRoute, string gatewayAdvertisedRouteId, CallSettings callSettings = null)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The parent resource.  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. Initial values for the new gateway advertised route.  
`gatewayAdvertisedRouteId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the route to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpokeName parent = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    string gatewayAdvertisedRouteId = "";
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.CreateGatewayAdvertisedRouteAsync(parent, gatewayAdvertisedRoute, gatewayAdvertisedRouteId);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRouteAsync(SpokeName, GatewayAdvertisedRoute, string, CancellationToken)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> CreateGatewayAdvertisedRouteAsync(SpokeName parent, GatewayAdvertisedRoute gatewayAdvertisedRoute, string gatewayAdvertisedRouteId, CancellationToken cancellationToken)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The parent resource.  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. Initial values for the new gateway advertised route.  
`gatewayAdvertisedRouteId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the route to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpokeName parent = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    string gatewayAdvertisedRouteId = "";
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.CreateGatewayAdvertisedRouteAsync(parent, gatewayAdvertisedRoute, gatewayAdvertisedRouteId);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRouteAsync(string, GatewayAdvertisedRoute, string, CallSettings)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> CreateGatewayAdvertisedRouteAsync(string parent, GatewayAdvertisedRoute gatewayAdvertisedRoute, string gatewayAdvertisedRouteId, CallSettings callSettings = null)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. Initial values for the new gateway advertised route.  
`gatewayAdvertisedRouteId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the route to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    string gatewayAdvertisedRouteId = "";
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.CreateGatewayAdvertisedRouteAsync(parent, gatewayAdvertisedRoute, gatewayAdvertisedRouteId);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateGatewayAdvertisedRouteAsync(string, GatewayAdvertisedRoute, string, CancellationToken)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> CreateGatewayAdvertisedRouteAsync(string parent, GatewayAdvertisedRoute gatewayAdvertisedRoute, string gatewayAdvertisedRouteId, CancellationToken cancellationToken)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. Initial values for the new gateway advertised route.  
`gatewayAdvertisedRouteId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the route to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    string gatewayAdvertisedRouteId = "";
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.CreateGatewayAdvertisedRouteAsync(parent, gatewayAdvertisedRoute, gatewayAdvertisedRouteId);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### CreateHub(LocationName, Hub, string, CallSettings)
    
    
    public virtual Operation<Hub, OperationMetadata> CreateHub(LocationName parent, Hub hub, string hubId, CallSettings callSettings = null)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. A unique identifier for the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Hub hub = new Hub();
    string hubId = "";
    // Make the request
    Operation<Hub, OperationMetadata> response = hubServiceClient.CreateHub(parent, hub, hubId);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHub(CreateHubRequest, CallSettings)
    
    
    public virtual Operation<Hub, OperationMetadata> CreateHub(CreateHubRequest request, CallSettings callSettings = null)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    CreateHubRequest request = new CreateHubRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        HubId = "",
        Hub = new Hub(),
        RequestId = "",
    };
    // Make the request
    Operation<Hub, OperationMetadata> response = hubServiceClient.CreateHub(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHub(string, Hub, string, CallSettings)
    
    
    public virtual Operation<Hub, OperationMetadata> CreateHub(string parent, Hub hub, string hubId, CallSettings callSettings = null)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. A unique identifier for the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Hub hub = new Hub();
    string hubId = "";
    // Make the request
    Operation<Hub, OperationMetadata> response = hubServiceClient.CreateHub(parent, hub, hubId);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHubAsync(LocationName, Hub, string, CallSettings)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> CreateHubAsync(LocationName parent, Hub hub, string hubId, CallSettings callSettings = null)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. A unique identifier for the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Hub hub = new Hub();
    string hubId = "";
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.CreateHubAsync(parent, hub, hubId);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHubAsync(LocationName, Hub, string, CancellationToken)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> CreateHubAsync(LocationName parent, Hub hub, string hubId, CancellationToken cancellationToken)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. A unique identifier for the hub.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Hub hub = new Hub();
    string hubId = "";
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.CreateHubAsync(parent, hub, hubId);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHubAsync(CreateHubRequest, CallSettings)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> CreateHubAsync(CreateHubRequest request, CallSettings callSettings = null)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateHubRequest request = new CreateHubRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        HubId = "",
        Hub = new Hub(),
        RequestId = "",
    };
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.CreateHubAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHubAsync(CreateHubRequest, CancellationToken)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> CreateHubAsync(CreateHubRequest request, CancellationToken cancellationToken)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateHubRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateHubRequest request = new CreateHubRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        HubId = "",
        Hub = new Hub(),
        RequestId = "",
    };
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.CreateHubAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHubAsync(string, Hub, string, CallSettings)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> CreateHubAsync(string parent, Hub hub, string hubId, CallSettings callSettings = null)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. A unique identifier for the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Hub hub = new Hub();
    string hubId = "";
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.CreateHubAsync(parent, hub, hubId);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateHubAsync(string, Hub, string, CancellationToken)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> CreateHubAsync(string parent, Hub hub, string hubId, CancellationToken cancellationToken)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. A unique identifier for the hub.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Hub hub = new Hub();
    string hubId = "";
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.CreateHubAsync(parent, hub, hubId);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpoke(LocationName, Spoke, string, CallSettings)
    
    
    public virtual Operation<Spoke, OperationMetadata> CreateSpoke(LocationName parent, Spoke spoke, string spokeId, CallSettings callSettings = null)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the spoke to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Spoke spoke = new Spoke();
    string spokeId = "";
    // Make the request
    Operation<Spoke, OperationMetadata> response = hubServiceClient.CreateSpoke(parent, spoke, spokeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpoke(CreateSpokeRequest, CallSettings)
    
    
    public virtual Operation<Spoke, OperationMetadata> CreateSpoke(CreateSpokeRequest request, CallSettings callSettings = null)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    CreateSpokeRequest request = new CreateSpokeRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SpokeId = "",
        Spoke = new Spoke(),
        RequestId = "",
    };
    // Make the request
    Operation<Spoke, OperationMetadata> response = hubServiceClient.CreateSpoke(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpoke(string, Spoke, string, CallSettings)
    
    
    public virtual Operation<Spoke, OperationMetadata> CreateSpoke(string parent, Spoke spoke, string spokeId, CallSettings callSettings = null)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the spoke to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Spoke spoke = new Spoke();
    string spokeId = "";
    // Make the request
    Operation<Spoke, OperationMetadata> response = hubServiceClient.CreateSpoke(parent, spoke, spokeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceCreateSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpokeAsync(LocationName, Spoke, string, CallSettings)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> CreateSpokeAsync(LocationName parent, Spoke spoke, string spokeId, CallSettings callSettings = null)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the spoke to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Spoke spoke = new Spoke();
    string spokeId = "";
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.CreateSpokeAsync(parent, spoke, spokeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpokeAsync(LocationName, Spoke, string, CancellationToken)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> CreateSpokeAsync(LocationName parent, Spoke spoke, string spokeId, CancellationToken cancellationToken)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the spoke to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Spoke spoke = new Spoke();
    string spokeId = "";
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.CreateSpokeAsync(parent, spoke, spokeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpokeAsync(CreateSpokeRequest, CallSettings)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> CreateSpokeAsync(CreateSpokeRequest request, CallSettings callSettings = null)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateSpokeRequest request = new CreateSpokeRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SpokeId = "",
        Spoke = new Spoke(),
        RequestId = "",
    };
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.CreateSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpokeAsync(CreateSpokeRequest, CancellationToken)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> CreateSpokeAsync(CreateSpokeRequest request, CancellationToken cancellationToken)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.CreateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateSpokeRequest request = new CreateSpokeRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SpokeId = "",
        Spoke = new Spoke(),
        RequestId = "",
    };
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.CreateSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpokeAsync(string, Spoke, string, CallSettings)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> CreateSpokeAsync(string parent, Spoke spoke, string spokeId, CallSettings callSettings = null)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the spoke to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Spoke spoke = new Spoke();
    string spokeId = "";
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.CreateSpokeAsync(parent, spoke, spokeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpokeAsync(string, Spoke, string, CancellationToken)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> CreateSpokeAsync(string parent, Spoke spoke, string spokeId, CancellationToken cancellationToken)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Unique id for the spoke to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Spoke spoke = new Spoke();
    string spokeId = "";
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.CreateSpokeAsync(parent, spoke, spokeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceCreateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRoute(DeleteGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteGatewayAdvertisedRoute(DeleteGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    DeleteGatewayAdvertisedRouteRequest request = new DeleteGatewayAdvertisedRouteRequest
    {
        GatewayAdvertisedRouteName = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteGatewayAdvertisedRoute(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRoute(GatewayAdvertisedRouteName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteGatewayAdvertisedRoute(GatewayAdvertisedRouteName name, CallSettings callSettings = null)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GatewayAdvertisedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRouteName)`  
Required. The name of the gateway advertised route to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GatewayAdvertisedRouteName name = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteGatewayAdvertisedRoute(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRoute(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteGatewayAdvertisedRoute(string name, CallSettings callSettings = null)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the gateway advertised route to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]/gatewayAdvertisedRoutes/[GATEWAY_ADVERTISED_ROUTE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteGatewayAdvertisedRoute(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRouteAsync(DeleteGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteGatewayAdvertisedRouteAsync(DeleteGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteGatewayAdvertisedRouteRequest request = new DeleteGatewayAdvertisedRouteRequest
    {
        GatewayAdvertisedRouteName = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteGatewayAdvertisedRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRouteAsync(DeleteGatewayAdvertisedRouteRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteGatewayAdvertisedRouteAsync(DeleteGatewayAdvertisedRouteRequest request, CancellationToken cancellationToken)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteGatewayAdvertisedRouteRequest request = new DeleteGatewayAdvertisedRouteRequest
    {
        GatewayAdvertisedRouteName = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteGatewayAdvertisedRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName name, CallSettings callSettings = null)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GatewayAdvertisedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRouteName)`  
Required. The name of the gateway advertised route to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GatewayAdvertisedRouteName name = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteGatewayAdvertisedRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName name, CancellationToken cancellationToken)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GatewayAdvertisedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRouteName)`  
Required. The name of the gateway advertised route to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GatewayAdvertisedRouteName name = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteGatewayAdvertisedRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRouteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteGatewayAdvertisedRouteAsync(string name, CallSettings callSettings = null)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the gateway advertised route to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]/gatewayAdvertisedRoutes/[GATEWAY_ADVERTISED_ROUTE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteGatewayAdvertisedRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteGatewayAdvertisedRouteAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteGatewayAdvertisedRouteAsync(string name, CancellationToken cancellationToken)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the gateway advertised route to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]/gatewayAdvertisedRoutes/[GATEWAY_ADVERTISED_ROUTE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteGatewayAdvertisedRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHub(DeleteHubRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteHub(DeleteHubRequest request, CallSettings callSettings = null)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    DeleteHubRequest request = new DeleteHubRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteHub(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHub(HubName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteHub(HubName name, CallSettings callSettings = null)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteHub(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHub(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteHub(string name, CallSettings callSettings = null)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteHub(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHubAsync(DeleteHubRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteHubAsync(DeleteHubRequest request, CallSettings callSettings = null)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteHubRequest request = new DeleteHubRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteHubAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHubAsync(DeleteHubRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteHubAsync(DeleteHubRequest request, CancellationToken cancellationToken)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteHubRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteHubRequest request = new DeleteHubRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteHubAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHubAsync(HubName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteHubAsync(HubName name, CallSettings callSettings = null)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteHubAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHubAsync(HubName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteHubAsync(HubName name, CancellationToken cancellationToken)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteHubAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHubAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteHubAsync(string name, CallSettings callSettings = null)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteHubAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteHubAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteHubAsync(string name, CancellationToken cancellationToken)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteHubAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpoke(DeleteSpokeRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteSpoke(DeleteSpokeRequest request, CallSettings callSettings = null)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    DeleteSpokeRequest request = new DeleteSpokeRequest
    {
        SpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteSpoke(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpoke(SpokeName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteSpoke(SpokeName name, CallSettings callSettings = null)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The name of the spoke to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    SpokeName name = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteSpoke(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpoke(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteSpoke(string name, CallSettings callSettings = null)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the spoke to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = hubServiceClient.DeleteSpoke(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceDeleteSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpokeAsync(DeleteSpokeRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteSpokeAsync(DeleteSpokeRequest request, CallSettings callSettings = null)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteSpokeRequest request = new DeleteSpokeRequest
    {
        SpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpokeAsync(DeleteSpokeRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteSpokeAsync(DeleteSpokeRequest request, CancellationToken cancellationToken)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteSpokeRequest request = new DeleteSpokeRequest
    {
        SpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpokeAsync(SpokeName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteSpokeAsync(SpokeName name, CallSettings callSettings = null)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The name of the spoke to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpokeName name = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteSpokeAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpokeAsync(SpokeName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteSpokeAsync(SpokeName name, CancellationToken cancellationToken)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The name of the spoke to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpokeName name = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteSpokeAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpokeAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteSpokeAsync(string name, CallSettings callSettings = null)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the spoke to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteSpokeAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpokeAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteSpokeAsync(string name, CancellationToken cancellationToken)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the spoke to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await hubServiceClient.DeleteSpokeAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceDeleteSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetGatewayAdvertisedRoute(GatewayAdvertisedRouteName, CallSettings)
    
    
    public virtual GatewayAdvertisedRoute GetGatewayAdvertisedRoute(GatewayAdvertisedRouteName name, CallSettings callSettings = null)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GatewayAdvertisedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRouteName)`  
Required. The name of the gateway advertised route to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GatewayAdvertisedRouteName name = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]");
    // Make the request
    GatewayAdvertisedRoute response = hubServiceClient.GetGatewayAdvertisedRoute(name);
    

### GetGatewayAdvertisedRoute(GetGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual GatewayAdvertisedRoute GetGatewayAdvertisedRoute(GetGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GetGatewayAdvertisedRouteRequest request = new GetGatewayAdvertisedRouteRequest
    {
        GatewayAdvertisedRouteName = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]"),
    };
    // Make the request
    GatewayAdvertisedRoute response = hubServiceClient.GetGatewayAdvertisedRoute(request);
    

### GetGatewayAdvertisedRoute(string, CallSettings)
    
    
    public virtual GatewayAdvertisedRoute GetGatewayAdvertisedRoute(string name, CallSettings callSettings = null)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the gateway advertised route to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]/gatewayAdvertisedRoutes/[GATEWAY_ADVERTISED_ROUTE]";
    // Make the request
    GatewayAdvertisedRoute response = hubServiceClient.GetGatewayAdvertisedRoute(name);
    

### GetGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName, CallSettings)
    
    
    public virtual Task<GatewayAdvertisedRoute> GetGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName name, CallSettings callSettings = null)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GatewayAdvertisedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRouteName)`  
Required. The name of the gateway advertised route to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GatewayAdvertisedRouteName name = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]");
    // Make the request
    GatewayAdvertisedRoute response = await hubServiceClient.GetGatewayAdvertisedRouteAsync(name);
    

### GetGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName, CancellationToken)
    
    
    public virtual Task<GatewayAdvertisedRoute> GetGatewayAdvertisedRouteAsync(GatewayAdvertisedRouteName name, CancellationToken cancellationToken)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GatewayAdvertisedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRouteName)`  
Required. The name of the gateway advertised route to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GatewayAdvertisedRouteName name = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]");
    // Make the request
    GatewayAdvertisedRoute response = await hubServiceClient.GetGatewayAdvertisedRouteAsync(name);
    

### GetGatewayAdvertisedRouteAsync(GetGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual Task<GatewayAdvertisedRoute> GetGatewayAdvertisedRouteAsync(GetGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetGatewayAdvertisedRouteRequest request = new GetGatewayAdvertisedRouteRequest
    {
        GatewayAdvertisedRouteName = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]"),
    };
    // Make the request
    GatewayAdvertisedRoute response = await hubServiceClient.GetGatewayAdvertisedRouteAsync(request);
    

### GetGatewayAdvertisedRouteAsync(GetGatewayAdvertisedRouteRequest, CancellationToken)
    
    
    public virtual Task<GatewayAdvertisedRoute> GetGatewayAdvertisedRouteAsync(GetGatewayAdvertisedRouteRequest request, CancellationToken cancellationToken)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetGatewayAdvertisedRouteRequest request = new GetGatewayAdvertisedRouteRequest
    {
        GatewayAdvertisedRouteName = GatewayAdvertisedRouteName.FromProjectLocationSpokeGatewayAdvertisedRoute("[PROJECT]", "[LOCATION]", "[SPOKE]", "[GATEWAY_ADVERTISED_ROUTE]"),
    };
    // Make the request
    GatewayAdvertisedRoute response = await hubServiceClient.GetGatewayAdvertisedRouteAsync(request);
    

### GetGatewayAdvertisedRouteAsync(string, CallSettings)
    
    
    public virtual Task<GatewayAdvertisedRoute> GetGatewayAdvertisedRouteAsync(string name, CallSettings callSettings = null)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the gateway advertised route to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]/gatewayAdvertisedRoutes/[GATEWAY_ADVERTISED_ROUTE]";
    // Make the request
    GatewayAdvertisedRoute response = await hubServiceClient.GetGatewayAdvertisedRouteAsync(name);
    

### GetGatewayAdvertisedRouteAsync(string, CancellationToken)
    
    
    public virtual Task<GatewayAdvertisedRoute> GetGatewayAdvertisedRouteAsync(string name, CancellationToken cancellationToken)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the gateway advertised route to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]/gatewayAdvertisedRoutes/[GATEWAY_ADVERTISED_ROUTE]";
    // Make the request
    GatewayAdvertisedRoute response = await hubServiceClient.GetGatewayAdvertisedRouteAsync(name);
    

### GetGroup(GetGroupRequest, CallSettings)
    
    
    public virtual Group GetGroup(GetGroupRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GetGroupRequest request = new GetGroupRequest
    {
        GroupName = GroupName.FromProjectHubGroup("[PROJECT]", "[HUB]", "[GROUP]"),
    };
    // Make the request
    Group response = hubServiceClient.GetGroup(request);
    

### GetGroup(GroupName, CallSettings)
    
    
    public virtual Group GetGroup(GroupName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GroupName)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GroupName name = GroupName.FromProjectHubGroup("[PROJECT]", "[HUB]", "[GROUP]");
    // Make the request
    Group response = hubServiceClient.GetGroup(name);
    

### GetGroup(string, CallSettings)
    
    
    public virtual Group GetGroup(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/groups/[GROUP]";
    // Make the request
    Group response = hubServiceClient.GetGroup(name);
    

### GetGroupAsync(GetGroupRequest, CallSettings)
    
    
    public virtual Task<Group> GetGroupAsync(GetGroupRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetGroupRequest request = new GetGroupRequest
    {
        GroupName = GroupName.FromProjectHubGroup("[PROJECT]", "[HUB]", "[GROUP]"),
    };
    // Make the request
    Group response = await hubServiceClient.GetGroupAsync(request);
    

### GetGroupAsync(GetGroupRequest, CancellationToken)
    
    
    public virtual Task<Group> GetGroupAsync(GetGroupRequest request, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetGroupRequest request = new GetGroupRequest
    {
        GroupName = GroupName.FromProjectHubGroup("[PROJECT]", "[HUB]", "[GROUP]"),
    };
    // Make the request
    Group response = await hubServiceClient.GetGroupAsync(request);
    

### GetGroupAsync(GroupName, CallSettings)
    
    
    public virtual Task<Group> GetGroupAsync(GroupName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GroupName)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GroupName name = GroupName.FromProjectHubGroup("[PROJECT]", "[HUB]", "[GROUP]");
    // Make the request
    Group response = await hubServiceClient.GetGroupAsync(name);
    

### GetGroupAsync(GroupName, CancellationToken)
    
    
    public virtual Task<Group> GetGroupAsync(GroupName name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GroupName)`  
Required. The name of the route table resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GroupName name = GroupName.FromProjectHubGroup("[PROJECT]", "[HUB]", "[GROUP]");
    // Make the request
    Group response = await hubServiceClient.GetGroupAsync(name);
    

### GetGroupAsync(string, CallSettings)
    
    
    public virtual Task<Group> GetGroupAsync(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/groups/[GROUP]";
    // Make the request
    Group response = await hubServiceClient.GetGroupAsync(name);
    

### GetGroupAsync(string, CancellationToken)
    
    
    public virtual Task<Group> GetGroupAsync(string name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route table resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/groups/[GROUP]";
    // Make the request
    Group response = await hubServiceClient.GetGroupAsync(name);
    

### GetHub(GetHubRequest, CallSettings)
    
    
    public virtual Hub GetHub(GetHubRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GetHubRequest request = new GetHubRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
    };
    // Make the request
    Hub response = hubServiceClient.GetHub(request);
    

### GetHub(HubName, CallSettings)
    
    
    public virtual Hub GetHub(HubName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    Hub response = hubServiceClient.GetHub(name);
    

### GetHub(string, CallSettings)
    
    
    public virtual Hub GetHub(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    Hub response = hubServiceClient.GetHub(name);
    

### GetHubAsync(GetHubRequest, CallSettings)
    
    
    public virtual Task<Hub> GetHubAsync(GetHubRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetHubRequest request = new GetHubRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
    };
    // Make the request
    Hub response = await hubServiceClient.GetHubAsync(request);
    

### GetHubAsync(GetHubRequest, CancellationToken)
    
    
    public virtual Task<Hub> GetHubAsync(GetHubRequest request, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetHubRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetHubRequest request = new GetHubRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
    };
    // Make the request
    Hub response = await hubServiceClient.GetHubAsync(request);
    

### GetHubAsync(HubName, CallSettings)
    
    
    public virtual Task<Hub> GetHubAsync(HubName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    Hub response = await hubServiceClient.GetHubAsync(name);
    

### GetHubAsync(HubName, CancellationToken)
    
    
    public virtual Task<Hub> GetHubAsync(HubName name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    Hub response = await hubServiceClient.GetHubAsync(name);
    

### GetHubAsync(string, CallSettings)
    
    
    public virtual Task<Hub> GetHubAsync(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    Hub response = await hubServiceClient.GetHubAsync(name);
    

### GetHubAsync(string, CancellationToken)
    
    
    public virtual Task<Hub> GetHubAsync(string name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    Hub response = await hubServiceClient.GetHubAsync(name);
    

### GetRoute(GetRouteRequest, CallSettings)
    
    
    public virtual Route GetRoute(GetRouteRequest request, CallSettings callSettings = null)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GetRouteRequest request = new GetRouteRequest
    {
        HubRouteName = HubRouteName.FromProjectHubRouteTableRoute("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]"),
    };
    // Make the request
    Route response = hubServiceClient.GetRoute(request);
    

### GetRoute(HubRouteName, CallSettings)
    
    
    public virtual Route GetRoute(HubRouteName name, CallSettings callSettings = null)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubRouteName)`  
Required. The name of the route resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubRouteName name = HubRouteName.FromProjectHubRouteTableRoute("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]");
    // Make the request
    Route response = hubServiceClient.GetRoute(name);
    

### GetRoute(string, CallSettings)
    
    
    public virtual Route GetRoute(string name, CallSettings callSettings = null)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]/routes/[ROUTE]";
    // Make the request
    Route response = hubServiceClient.GetRoute(name);
    

### GetRouteAsync(GetRouteRequest, CallSettings)
    
    
    public virtual Task<Route> GetRouteAsync(GetRouteRequest request, CallSettings callSettings = null)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetRouteRequest request = new GetRouteRequest
    {
        HubRouteName = HubRouteName.FromProjectHubRouteTableRoute("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]"),
    };
    // Make the request
    Route response = await hubServiceClient.GetRouteAsync(request);
    

### GetRouteAsync(GetRouteRequest, CancellationToken)
    
    
    public virtual Task<Route> GetRouteAsync(GetRouteRequest request, CancellationToken cancellationToken)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetRouteRequest request = new GetRouteRequest
    {
        HubRouteName = HubRouteName.FromProjectHubRouteTableRoute("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]"),
    };
    // Make the request
    Route response = await hubServiceClient.GetRouteAsync(request);
    

### GetRouteAsync(HubRouteName, CallSettings)
    
    
    public virtual Task<Route> GetRouteAsync(HubRouteName name, CallSettings callSettings = null)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubRouteName)`  
Required. The name of the route resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubRouteName name = HubRouteName.FromProjectHubRouteTableRoute("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]");
    // Make the request
    Route response = await hubServiceClient.GetRouteAsync(name);
    

### GetRouteAsync(HubRouteName, CancellationToken)
    
    
    public virtual Task<Route> GetRouteAsync(HubRouteName name, CancellationToken cancellationToken)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubRouteName)`  
Required. The name of the route resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubRouteName name = HubRouteName.FromProjectHubRouteTableRoute("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]");
    // Make the request
    Route response = await hubServiceClient.GetRouteAsync(name);
    

### GetRouteAsync(string, CallSettings)
    
    
    public virtual Task<Route> GetRouteAsync(string name, CallSettings callSettings = null)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]/routes/[ROUTE]";
    // Make the request
    Route response = await hubServiceClient.GetRouteAsync(name);
    

### GetRouteAsync(string, CancellationToken)
    
    
    public virtual Task<Route> GetRouteAsync(string name, CancellationToken cancellationToken)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]/routes/[ROUTE]";
    // Make the request
    Route response = await hubServiceClient.GetRouteAsync(name);
    

### GetRouteTable(GetRouteTableRequest, CallSettings)
    
    
    public virtual RouteTable GetRouteTable(GetRouteTableRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetRouteTableRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GetRouteTableRequest request = new GetRouteTableRequest
    {
        RouteTableName = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]"),
    };
    // Make the request
    RouteTable response = hubServiceClient.GetRouteTable(request);
    

### GetRouteTable(RouteTableName, CallSettings)
    
    
    public virtual RouteTable GetRouteTable(RouteTableName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteTableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTableName)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    RouteTableName name = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]");
    // Make the request
    RouteTable response = hubServiceClient.GetRouteTable(name);
    

### GetRouteTable(string, CallSettings)
    
    
    public virtual RouteTable GetRouteTable(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]";
    // Make the request
    RouteTable response = hubServiceClient.GetRouteTable(name);
    

### GetRouteTableAsync(GetRouteTableRequest, CallSettings)
    
    
    public virtual Task<RouteTable> GetRouteTableAsync(GetRouteTableRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetRouteTableRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetRouteTableRequest request = new GetRouteTableRequest
    {
        RouteTableName = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]"),
    };
    // Make the request
    RouteTable response = await hubServiceClient.GetRouteTableAsync(request);
    

### GetRouteTableAsync(GetRouteTableRequest, CancellationToken)
    
    
    public virtual Task<RouteTable> GetRouteTableAsync(GetRouteTableRequest request, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetRouteTableRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetRouteTableRequest request = new GetRouteTableRequest
    {
        RouteTableName = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]"),
    };
    // Make the request
    RouteTable response = await hubServiceClient.GetRouteTableAsync(request);
    

### GetRouteTableAsync(RouteTableName, CallSettings)
    
    
    public virtual Task<RouteTable> GetRouteTableAsync(RouteTableName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteTableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTableName)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    RouteTableName name = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]");
    // Make the request
    RouteTable response = await hubServiceClient.GetRouteTableAsync(name);
    

### GetRouteTableAsync(RouteTableName, CancellationToken)
    
    
    public virtual Task<RouteTable> GetRouteTableAsync(RouteTableName name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteTableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTableName)`  
Required. The name of the route table resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    RouteTableName name = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]");
    // Make the request
    RouteTable response = await hubServiceClient.GetRouteTableAsync(name);
    

### GetRouteTableAsync(string, CallSettings)
    
    
    public virtual Task<RouteTable> GetRouteTableAsync(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route table resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]";
    // Make the request
    RouteTable response = await hubServiceClient.GetRouteTableAsync(name);
    

### GetRouteTableAsync(string, CancellationToken)
    
    
    public virtual Task<RouteTable> GetRouteTableAsync(string name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the route table resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]";
    // Make the request
    RouteTable response = await hubServiceClient.GetRouteTableAsync(name);
    

### GetSpoke(GetSpokeRequest, CallSettings)
    
    
    public virtual Spoke GetSpoke(GetSpokeRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GetSpokeRequest request = new GetSpokeRequest
    {
        SpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
    };
    // Make the request
    Spoke response = hubServiceClient.GetSpoke(request);
    

### GetSpoke(SpokeName, CallSettings)
    
    
    public virtual Spoke GetSpoke(SpokeName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The name of the spoke resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    SpokeName name = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Spoke response = hubServiceClient.GetSpoke(name);
    

### GetSpoke(string, CallSettings)
    
    
    public virtual Spoke GetSpoke(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the spoke resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Spoke response = hubServiceClient.GetSpoke(name);
    

### GetSpokeAsync(GetSpokeRequest, CallSettings)
    
    
    public virtual Task<Spoke> GetSpokeAsync(GetSpokeRequest request, CallSettings callSettings = null)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetSpokeRequest request = new GetSpokeRequest
    {
        SpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
    };
    // Make the request
    Spoke response = await hubServiceClient.GetSpokeAsync(request);
    

### GetSpokeAsync(GetSpokeRequest, CancellationToken)
    
    
    public virtual Task<Spoke> GetSpokeAsync(GetSpokeRequest request, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GetSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetSpokeRequest request = new GetSpokeRequest
    {
        SpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
    };
    // Make the request
    Spoke response = await hubServiceClient.GetSpokeAsync(request);
    

### GetSpokeAsync(SpokeName, CallSettings)
    
    
    public virtual Task<Spoke> GetSpokeAsync(SpokeName name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The name of the spoke resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpokeName name = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Spoke response = await hubServiceClient.GetSpokeAsync(name);
    

### GetSpokeAsync(SpokeName, CancellationToken)
    
    
    public virtual Task<Spoke> GetSpokeAsync(SpokeName name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The name of the spoke resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpokeName name = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Spoke response = await hubServiceClient.GetSpokeAsync(name);
    

### GetSpokeAsync(string, CallSettings)
    
    
    public virtual Task<Spoke> GetSpokeAsync(string name, CallSettings callSettings = null)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the spoke resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Spoke response = await hubServiceClient.GetSpokeAsync(name);
    

### GetSpokeAsync(string, CancellationToken)
    
    
    public virtual Task<Spoke> GetSpokeAsync(string name, CancellationToken cancellationToken)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the spoke resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Spoke response = await hubServiceClient.GetSpokeAsync(name);
    

### ListGatewayAdvertisedRoutes(ListGatewayAdvertisedRoutesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> ListGatewayAdvertisedRoutes(ListGatewayAdvertisedRoutesRequest request, CallSettings callSettings = null)

List GatewayAdvertisedRoutes

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewayAdvertisedRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesResponse)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A pageable sequence of [GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    ListGatewayAdvertisedRoutesRequest request = new ListGatewayAdvertisedRoutesRequest
    {
        ParentAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> response = hubServiceClient.ListGatewayAdvertisedRoutes(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (GatewayAdvertisedRoute item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGatewayAdvertisedRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (GatewayAdvertisedRoute item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<GatewayAdvertisedRoute> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (GatewayAdvertisedRoute item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGatewayAdvertisedRoutes(SpokeName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> ListGatewayAdvertisedRoutes(SpokeName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List GatewayAdvertisedRoutes

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesResponse)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A pageable sequence of [GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    SpokeName parent = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    PagedEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> response = hubServiceClient.ListGatewayAdvertisedRoutes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (GatewayAdvertisedRoute item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGatewayAdvertisedRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (GatewayAdvertisedRoute item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<GatewayAdvertisedRoute> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (GatewayAdvertisedRoute item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGatewayAdvertisedRoutes(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> ListGatewayAdvertisedRoutes(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List GatewayAdvertisedRoutes

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesResponse)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A pageable sequence of [GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    PagedEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> response = hubServiceClient.ListGatewayAdvertisedRoutes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (GatewayAdvertisedRoute item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGatewayAdvertisedRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (GatewayAdvertisedRoute item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<GatewayAdvertisedRoute> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (GatewayAdvertisedRoute item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGatewayAdvertisedRoutesAsync(ListGatewayAdvertisedRoutesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> ListGatewayAdvertisedRoutesAsync(ListGatewayAdvertisedRoutesRequest request, CallSettings callSettings = null)

List GatewayAdvertisedRoutes

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewayAdvertisedRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesResponse)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A pageable asynchronous sequence of [GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListGatewayAdvertisedRoutesRequest request = new ListGatewayAdvertisedRoutesRequest
    {
        ParentAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> response = hubServiceClient.ListGatewayAdvertisedRoutesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (GatewayAdvertisedRoute item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGatewayAdvertisedRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (GatewayAdvertisedRoute item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<GatewayAdvertisedRoute> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (GatewayAdvertisedRoute item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGatewayAdvertisedRoutesAsync(SpokeName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> ListGatewayAdvertisedRoutesAsync(SpokeName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List GatewayAdvertisedRoutes

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesResponse)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A pageable asynchronous sequence of [GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpokeName parent = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    PagedAsyncEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> response = hubServiceClient.ListGatewayAdvertisedRoutesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (GatewayAdvertisedRoute item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGatewayAdvertisedRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (GatewayAdvertisedRoute item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<GatewayAdvertisedRoute> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (GatewayAdvertisedRoute item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGatewayAdvertisedRoutesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> ListGatewayAdvertisedRoutesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List GatewayAdvertisedRoutes

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGatewayAdvertisedRoutesResponse)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)` | A pageable asynchronous sequence of [GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    PagedAsyncEnumerable<ListGatewayAdvertisedRoutesResponse, GatewayAdvertisedRoute> response = hubServiceClient.ListGatewayAdvertisedRoutesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (GatewayAdvertisedRoute item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGatewayAdvertisedRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (GatewayAdvertisedRoute item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<GatewayAdvertisedRoute> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (GatewayAdvertisedRoute item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGroups(HubName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGroupsResponse, Group> ListGroups(HubName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists groups in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsResponse)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A pageable sequence of [Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName parent = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedEnumerable<ListGroupsResponse, Group> response = hubServiceClient.ListGroups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Group item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Group item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Group> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Group item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGroups(ListGroupsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListGroupsResponse, Group> ListGroups(ListGroupsRequest request, CallSettings callSettings = null)

Lists groups in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsResponse)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A pageable sequence of [Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    ListGroupsRequest request = new ListGroupsRequest
    {
        ParentAsHubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListGroupsResponse, Group> response = hubServiceClient.ListGroups(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Group item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Group item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Group> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Group item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGroups(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGroupsResponse, Group> ListGroups(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists groups in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsResponse)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A pageable sequence of [Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedEnumerable<ListGroupsResponse, Group> response = hubServiceClient.ListGroups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Group item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Group item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Group> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Group item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGroupsAsync(HubName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGroupsResponse, Group> ListGroupsAsync(HubName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists groups in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsResponse)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A pageable asynchronous sequence of [Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName parent = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedAsyncEnumerable<ListGroupsResponse, Group> response = hubServiceClient.ListGroupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Group item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Group item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Group> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Group item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGroupsAsync(ListGroupsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGroupsResponse, Group> ListGroupsAsync(ListGroupsRequest request, CallSettings callSettings = null)

Lists groups in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsResponse)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A pageable asynchronous sequence of [Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListGroupsRequest request = new ListGroupsRequest
    {
        ParentAsHubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListGroupsResponse, Group> response = hubServiceClient.ListGroupsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Group item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Group item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Group> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Group item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGroupsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGroupsResponse, Group> ListGroupsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists groups in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListGroupsResponse)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)` | A pageable asynchronous sequence of [Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedAsyncEnumerable<ListGroupsResponse, Group> response = hubServiceClient.ListGroupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Group item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Group item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Group> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Group item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubSpokes(HubName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListHubSpokesResponse, Spoke> ListHubSpokes(HubName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListHubSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedEnumerable<ListHubSpokesResponse, Spoke> response = hubServiceClient.ListHubSpokes(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListHubSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubSpokes(ListHubSpokesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListHubSpokesResponse, Spoke> ListHubSpokes(ListHubSpokesRequest request, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHubSpokesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListHubSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    ListHubSpokesRequest request = new ListHubSpokesRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeLocations = { "", },
        Filter = "",
        OrderBy = "",
        View = ListHubSpokesRequest.Types.SpokeView.Unspecified,
    };
    // Make the request
    PagedEnumerable<ListHubSpokesResponse, Spoke> response = hubServiceClient.ListHubSpokes(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListHubSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubSpokes(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListHubSpokesResponse, Spoke> ListHubSpokes(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListHubSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedEnumerable<ListHubSpokesResponse, Spoke> response = hubServiceClient.ListHubSpokes(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListHubSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubSpokesAsync(HubName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListHubSpokesResponse, Spoke> ListHubSpokesAsync(HubName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListHubSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable asynchronous sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedAsyncEnumerable<ListHubSpokesResponse, Spoke> response = hubServiceClient.ListHubSpokesAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListHubSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubSpokesAsync(ListHubSpokesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListHubSpokesResponse, Spoke> ListHubSpokesAsync(ListHubSpokesRequest request, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHubSpokesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListHubSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable asynchronous sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListHubSpokesRequest request = new ListHubSpokesRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeLocations = { "", },
        Filter = "",
        OrderBy = "",
        View = ListHubSpokesRequest.Types.SpokeView.Unspecified,
    };
    // Make the request
    PagedAsyncEnumerable<ListHubSpokesResponse, Spoke> response = hubServiceClient.ListHubSpokesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListHubSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubSpokesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListHubSpokesResponse, Spoke> ListHubSpokesAsync(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListHubSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable asynchronous sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedAsyncEnumerable<ListHubSpokesResponse, Spoke> response = hubServiceClient.ListHubSpokesAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListHubSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubs(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListHubsResponse, Hub> ListHubs(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center hubs associated with a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListHubsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsResponse)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A pageable sequence of [Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListHubsResponse, Hub> response = hubServiceClient.ListHubs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Hub item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListHubsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Hub item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Hub> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Hub item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubs(ListHubsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListHubsResponse, Hub> ListHubs(ListHubsRequest request, CallSettings callSettings = null)

Lists the Network Connectivity Center hubs associated with a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHubsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListHubsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsResponse)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A pageable sequence of [Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    ListHubsRequest request = new ListHubsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListHubsResponse, Hub> response = hubServiceClient.ListHubs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Hub item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListHubsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Hub item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Hub> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Hub item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListHubsResponse, Hub> ListHubs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center hubs associated with a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListHubsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsResponse)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A pageable sequence of [Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListHubsResponse, Hub> response = hubServiceClient.ListHubs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Hub item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListHubsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Hub item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Hub> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Hub item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListHubsResponse, Hub> ListHubsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center hubs associated with a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListHubsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsResponse)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A pageable asynchronous sequence of [Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListHubsResponse, Hub> response = hubServiceClient.ListHubsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Hub item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListHubsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Hub item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Hub> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Hub item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubsAsync(ListHubsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListHubsResponse, Hub> ListHubsAsync(ListHubsRequest request, CallSettings callSettings = null)

Lists the Network Connectivity Center hubs associated with a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHubsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListHubsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsResponse)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A pageable asynchronous sequence of [Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListHubsRequest request = new ListHubsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListHubsResponse, Hub> response = hubServiceClient.ListHubsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Hub item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListHubsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Hub item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Hub> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Hub item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListHubsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListHubsResponse, Hub> ListHubsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center hubs associated with a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListHubsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListHubsResponse)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)` | A pageable asynchronous sequence of [Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListHubsResponse, Hub> response = hubServiceClient.ListHubsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Hub item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListHubsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Hub item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Hub> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Hub item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRouteTables(HubName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRouteTablesResponse, RouteTable> ListRouteTables(HubName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists route tables in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRouteTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesResponse)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A pageable sequence of [RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName parent = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedEnumerable<ListRouteTablesResponse, RouteTable> response = hubServiceClient.ListRouteTables(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (RouteTable item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRouteTablesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (RouteTable item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<RouteTable> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (RouteTable item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRouteTables(ListRouteTablesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListRouteTablesResponse, RouteTable> ListRouteTables(ListRouteTablesRequest request, CallSettings callSettings = null)

Lists route tables in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRouteTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRouteTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesResponse)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A pageable sequence of [RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    ListRouteTablesRequest request = new ListRouteTablesRequest
    {
        ParentAsHubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListRouteTablesResponse, RouteTable> response = hubServiceClient.ListRouteTables(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (RouteTable item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRouteTablesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (RouteTable item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<RouteTable> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (RouteTable item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRouteTables(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRouteTablesResponse, RouteTable> ListRouteTables(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists route tables in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRouteTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesResponse)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A pageable sequence of [RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedEnumerable<ListRouteTablesResponse, RouteTable> response = hubServiceClient.ListRouteTables(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (RouteTable item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRouteTablesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (RouteTable item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<RouteTable> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (RouteTable item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRouteTablesAsync(HubName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRouteTablesResponse, RouteTable> ListRouteTablesAsync(HubName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists route tables in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRouteTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesResponse)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A pageable asynchronous sequence of [RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName parent = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedAsyncEnumerable<ListRouteTablesResponse, RouteTable> response = hubServiceClient.ListRouteTablesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (RouteTable item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRouteTablesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (RouteTable item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<RouteTable> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (RouteTable item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRouteTablesAsync(ListRouteTablesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRouteTablesResponse, RouteTable> ListRouteTablesAsync(ListRouteTablesRequest request, CallSettings callSettings = null)

Lists route tables in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRouteTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRouteTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesResponse)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A pageable asynchronous sequence of [RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListRouteTablesRequest request = new ListRouteTablesRequest
    {
        ParentAsHubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListRouteTablesResponse, RouteTable> response = hubServiceClient.ListRouteTablesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (RouteTable item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRouteTablesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (RouteTable item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<RouteTable> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (RouteTable item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRouteTablesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRouteTablesResponse, RouteTable> ListRouteTablesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists route tables in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRouteTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRouteTablesResponse)[RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable)` | A pageable asynchronous sequence of [RouteTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTable) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedAsyncEnumerable<ListRouteTablesResponse, RouteTable> response = hubServiceClient.ListRouteTablesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (RouteTable item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRouteTablesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (RouteTable item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<RouteTable> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (RouteTable item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutes(ListRoutesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListRoutesResponse, Route> ListRoutes(ListRoutesRequest request, CallSettings callSettings = null)

Lists routes in a given route table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A pageable sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    ListRoutesRequest request = new ListRoutesRequest
    {
        ParentAsRouteTableName = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListRoutesResponse, Route> response = hubServiceClient.ListRoutes(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutes(RouteTableName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRoutesResponse, Route> ListRoutes(RouteTableName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists routes in a given route table.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[RouteTableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTableName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A pageable sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    RouteTableName parent = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]");
    // Make the request
    PagedEnumerable<ListRoutesResponse, Route> response = hubServiceClient.ListRoutes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutes(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRoutesResponse, Route> ListRoutes(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists routes in a given route table.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A pageable sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]";
    // Make the request
    PagedEnumerable<ListRoutesResponse, Route> response = hubServiceClient.ListRoutes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutesAsync(ListRoutesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRoutesResponse, Route> ListRoutesAsync(ListRoutesRequest request, CallSettings callSettings = null)

Lists routes in a given route table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A pageable asynchronous sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListRoutesRequest request = new ListRoutesRequest
    {
        ParentAsRouteTableName = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListRoutesResponse, Route> response = hubServiceClient.ListRoutesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutesAsync(RouteTableName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRoutesResponse, Route> ListRoutesAsync(RouteTableName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists routes in a given route table.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[RouteTableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteTableName)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A pageable asynchronous sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    RouteTableName parent = RouteTableName.FromProjectHubRouteTable("[PROJECT]", "[HUB]", "[ROUTE_TABLE]");
    // Make the request
    PagedAsyncEnumerable<ListRoutesResponse, Route> response = hubServiceClient.ListRoutesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRoutesResponse, Route> ListRoutesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists routes in a given route table.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource's name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)` | A pageable asynchronous sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/global/hubs/[HUB]/routeTables/[ROUTE_TABLE]";
    // Make the request
    PagedAsyncEnumerable<ListRoutesResponse, Route> response = hubServiceClient.ListRoutesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpokes(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSpokesResponse, Spoke> ListSpokes(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListSpokesResponse, Spoke> response = hubServiceClient.ListSpokes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpokes(ListSpokesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListSpokesResponse, Spoke> ListSpokes(ListSpokesRequest request, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSpokesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    ListSpokesRequest request = new ListSpokesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListSpokesResponse, Spoke> response = hubServiceClient.ListSpokes(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpokes(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSpokesResponse, Spoke> ListSpokes(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListSpokesResponse, Spoke> response = hubServiceClient.ListSpokes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpokesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSpokesResponse, Spoke> ListSpokesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable asynchronous sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListSpokesResponse, Spoke> response = hubServiceClient.ListSpokesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpokesAsync(ListSpokesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSpokesResponse, Spoke> ListSpokesAsync(ListSpokesRequest request, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSpokesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable asynchronous sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListSpokesRequest request = new ListSpokesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListSpokesResponse, Spoke> response = hubServiceClient.ListSpokesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpokesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSpokesResponse, Spoke> ListSpokesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Network Connectivity Center spokes in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSpokesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.ListSpokesResponse)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)` | A pageable asynchronous sequence of [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListSpokesResponse, Spoke> response = hubServiceClient.ListSpokesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Spoke item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSpokesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Spoke item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Spoke> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Spoke item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceAcceptHubSpoke(string, CallSettings)
    
    
    public virtual Operation<AcceptHubSpokeResponse, OperationMetadata> PollOnceAcceptHubSpoke(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `AcceptHubSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceAcceptHubSpokeAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AcceptHubSpokeResponse, OperationMetadata>> PollOnceAcceptHubSpokeAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `AcceptHubSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceAcceptSpokeUpdate(string, CallSettings)
    
    
    public virtual Operation<AcceptSpokeUpdateResponse, OperationMetadata> PollOnceAcceptSpokeUpdate(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `AcceptSpokeUpdate` .

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceAcceptSpokeUpdateAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AcceptSpokeUpdateResponse, OperationMetadata>> PollOnceAcceptSpokeUpdateAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `AcceptSpokeUpdate`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.AcceptSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateGatewayAdvertisedRoute(string, CallSettings)
    
    
    public virtual Operation<GatewayAdvertisedRoute, OperationMetadata> PollOnceCreateGatewayAdvertisedRoute(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateGatewayAdvertisedRoute`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateGatewayAdvertisedRouteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> PollOnceCreateGatewayAdvertisedRouteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateGatewayAdvertisedRoute`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateHub(string, CallSettings)
    
    
    public virtual Operation<Hub, OperationMetadata> PollOnceCreateHub(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateHub`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateHubAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> PollOnceCreateHubAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateHub`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateSpoke(string, CallSettings)
    
    
    public virtual Operation<Spoke, OperationMetadata> PollOnceCreateSpoke(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateSpokeAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> PollOnceCreateSpokeAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteGatewayAdvertisedRoute(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteGatewayAdvertisedRoute(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteGatewayAdvertisedRoute`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteGatewayAdvertisedRouteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteGatewayAdvertisedRouteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteGatewayAdvertisedRoute`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteHub(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteHub(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteHub`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteHubAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteHubAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteHub`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteSpoke(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteSpoke(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteSpokeAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteSpokeAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRejectHubSpoke(string, CallSettings)
    
    
    public virtual Operation<RejectHubSpokeResponse, OperationMetadata> PollOnceRejectHubSpoke(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RejectHubSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRejectHubSpokeAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RejectHubSpokeResponse, OperationMetadata>> PollOnceRejectHubSpokeAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RejectHubSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRejectSpokeUpdate(string, CallSettings)
    
    
    public virtual Operation<RejectSpokeUpdateResponse, OperationMetadata> PollOnceRejectSpokeUpdate(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RejectSpokeUpdate` .

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRejectSpokeUpdateAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RejectSpokeUpdateResponse, OperationMetadata>> PollOnceRejectSpokeUpdateAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RejectSpokeUpdate`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateGatewayAdvertisedRoute(string, CallSettings)
    
    
    public virtual Operation<GatewayAdvertisedRoute, OperationMetadata> PollOnceUpdateGatewayAdvertisedRoute(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateGatewayAdvertisedRoute`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateGatewayAdvertisedRouteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> PollOnceUpdateGatewayAdvertisedRouteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateGatewayAdvertisedRoute`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateGroup(string, CallSettings)
    
    
    public virtual Operation<Group, OperationMetadata> PollOnceUpdateGroup(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateGroup`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateGroupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Group, OperationMetadata>> PollOnceUpdateGroupAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateGroup`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateHub(string, CallSettings)
    
    
    public virtual Operation<Hub, OperationMetadata> PollOnceUpdateHub(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateHub`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateHubAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> PollOnceUpdateHubAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateHub`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateSpoke(string, CallSettings)
    
    
    public virtual Operation<Spoke, OperationMetadata> PollOnceUpdateSpoke(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateSpokeAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> PollOnceUpdateSpokeAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateSpoke`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### QueryHubStatus(HubName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<QueryHubStatusResponse, HubStatusEntry> QueryHubStatus(HubName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryHubStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusResponse)[HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry)` | A pageable sequence of [HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedEnumerable<QueryHubStatusResponse, HubStatusEntry> response = hubServiceClient.QueryHubStatus(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (HubStatusEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (QueryHubStatusResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (HubStatusEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<HubStatusEntry> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (HubStatusEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryHubStatus(QueryHubStatusRequest, CallSettings)
    
    
    public virtual PagedEnumerable<QueryHubStatusResponse, HubStatusEntry> QueryHubStatus(QueryHubStatusRequest request, CallSettings callSettings = null)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryHubStatusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryHubStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusResponse)[HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry)` | A pageable sequence of [HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    QueryHubStatusRequest request = new QueryHubStatusRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        Filter = "",
        OrderBy = "",
        GroupBy = "",
    };
    // Make the request
    PagedEnumerable<QueryHubStatusResponse, HubStatusEntry> response = hubServiceClient.QueryHubStatus(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (HubStatusEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (QueryHubStatusResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (HubStatusEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<HubStatusEntry> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (HubStatusEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryHubStatus(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<QueryHubStatusResponse, HubStatusEntry> QueryHubStatus(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryHubStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusResponse)[HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry)` | A pageable sequence of [HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedEnumerable<QueryHubStatusResponse, HubStatusEntry> response = hubServiceClient.QueryHubStatus(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (HubStatusEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (QueryHubStatusResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (HubStatusEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<HubStatusEntry> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (HubStatusEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryHubStatusAsync(HubName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<QueryHubStatusResponse, HubStatusEntry> QueryHubStatusAsync(HubName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryHubStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusResponse)[HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry)` | A pageable asynchronous sequence of [HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    // Make the request
    PagedAsyncEnumerable<QueryHubStatusResponse, HubStatusEntry> response = hubServiceClient.QueryHubStatusAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (HubStatusEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (QueryHubStatusResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (HubStatusEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<HubStatusEntry> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (HubStatusEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryHubStatusAsync(QueryHubStatusRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<QueryHubStatusResponse, HubStatusEntry> QueryHubStatusAsync(QueryHubStatusRequest request, CallSettings callSettings = null)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryHubStatusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryHubStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusResponse)[HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry)` | A pageable asynchronous sequence of [HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    QueryHubStatusRequest request = new QueryHubStatusRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        Filter = "",
        OrderBy = "",
        GroupBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<QueryHubStatusResponse, HubStatusEntry> response = hubServiceClient.QueryHubStatusAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (HubStatusEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (QueryHubStatusResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (HubStatusEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<HubStatusEntry> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (HubStatusEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryHubStatusAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<QueryHubStatusResponse, HubStatusEntry> QueryHubStatusAsync(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryHubStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.QueryHubStatusResponse)[HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry)` | A pageable asynchronous sequence of [HubStatusEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubStatusEntry) resources.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    // Make the request
    PagedAsyncEnumerable<QueryHubStatusResponse, HubStatusEntry> response = hubServiceClient.QueryHubStatusAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (HubStatusEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (QueryHubStatusResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (HubStatusEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<HubStatusEntry> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (HubStatusEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### RejectHubSpoke(HubName, SpokeName, CallSettings)
    
    
    public virtual Operation<RejectHubSpokeResponse, OperationMetadata> RejectHubSpoke(HubName name, SpokeName spokeUri, CallSettings callSettings = null)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to reject from the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = hubServiceClient.RejectHubSpoke(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceRejectHubSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpoke(RejectHubSpokeRequest, CallSettings)
    
    
    public virtual Operation<RejectHubSpokeResponse, OperationMetadata> RejectHubSpoke(RejectHubSpokeRequest request, CallSettings callSettings = null)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectHubSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    RejectHubSpokeRequest request = new RejectHubSpokeRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
        Details = "",
    };
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = hubServiceClient.RejectHubSpoke(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceRejectHubSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpoke(string, string, CallSettings)
    
    
    public virtual Operation<RejectHubSpokeResponse, OperationMetadata> RejectHubSpoke(string name, string spokeUri, CallSettings callSettings = null)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to reject from the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = hubServiceClient.RejectHubSpoke(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceRejectHubSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpokeAsync(HubName, SpokeName, CallSettings)
    
    
    public virtual Task<Operation<RejectHubSpokeResponse, OperationMetadata>> RejectHubSpokeAsync(HubName name, SpokeName spokeUri, CallSettings callSettings = null)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to reject from the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = await hubServiceClient.RejectHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpokeAsync(HubName, SpokeName, CancellationToken)
    
    
    public virtual Task<Operation<RejectHubSpokeResponse, OperationMetadata>> RejectHubSpokeAsync(HubName name, SpokeName spokeUri, CancellationToken cancellationToken)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to reject from the hub.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = await hubServiceClient.RejectHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpokeAsync(RejectHubSpokeRequest, CallSettings)
    
    
    public virtual Task<Operation<RejectHubSpokeResponse, OperationMetadata>> RejectHubSpokeAsync(RejectHubSpokeRequest request, CallSettings callSettings = null)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectHubSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    RejectHubSpokeRequest request = new RejectHubSpokeRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
        Details = "",
    };
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = await hubServiceClient.RejectHubSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpokeAsync(RejectHubSpokeRequest, CancellationToken)
    
    
    public virtual Task<Operation<RejectHubSpokeResponse, OperationMetadata>> RejectHubSpokeAsync(RejectHubSpokeRequest request, CancellationToken cancellationToken)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectHubSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    RejectHubSpokeRequest request = new RejectHubSpokeRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        RequestId = "",
        Details = "",
    };
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = await hubServiceClient.RejectHubSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpokeAsync(string, string, CallSettings)
    
    
    public virtual Task<Operation<RejectHubSpokeResponse, OperationMetadata>> RejectHubSpokeAsync(string name, string spokeUri, CallSettings callSettings = null)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to reject from the hub.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = await hubServiceClient.RejectHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectHubSpokeAsync(string, string, CancellationToken)
    
    
    public virtual Task<Operation<RejectHubSpokeResponse, OperationMetadata>> RejectHubSpokeAsync(string name, string spokeUri, CancellationToken cancellationToken)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to reject from the hub.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectHubSpokeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectHubSpokeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    // Make the request
    Operation<RejectHubSpokeResponse, OperationMetadata> response = await hubServiceClient.RejectHubSpokeAsync(name, spokeUri);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectHubSpokeResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectHubSpokeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectHubSpokeResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectHubSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectHubSpokeResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdate(HubName, SpokeName, string, CallSettings)
    
    
    public virtual Operation<RejectSpokeUpdateResponse, OperationMetadata> RejectSpokeUpdate(HubName name, SpokeName spokeUri, string spokeEtag, CallSettings callSettings = null)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to reject update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    string spokeEtag = "";
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = hubServiceClient.RejectSpokeUpdate(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceRejectSpokeUpdate(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdate(RejectSpokeUpdateRequest, CallSettings)
    
    
    public virtual Operation<RejectSpokeUpdateResponse, OperationMetadata> RejectSpokeUpdate(RejectSpokeUpdateRequest request, CallSettings callSettings = null)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectSpokeUpdateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    RejectSpokeUpdateRequest request = new RejectSpokeUpdateRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        SpokeEtag = "",
        Details = "",
        RequestId = "",
    };
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = hubServiceClient.RejectSpokeUpdate(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceRejectSpokeUpdate(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdate(string, string, string, CallSettings)
    
    
    public virtual Operation<RejectSpokeUpdateResponse, OperationMetadata> RejectSpokeUpdate(string name, string spokeUri, string spokeEtag, CallSettings callSettings = null)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to reject update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    string spokeEtag = "";
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = hubServiceClient.RejectSpokeUpdate(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceRejectSpokeUpdate(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdateAsync(HubName, SpokeName, string, CallSettings)
    
    
    public virtual Task<Operation<RejectSpokeUpdateResponse, OperationMetadata>> RejectSpokeUpdateAsync(HubName name, SpokeName spokeUri, string spokeEtag, CallSettings callSettings = null)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to reject update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    string spokeEtag = "";
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.RejectSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdateAsync(HubName, SpokeName, string, CancellationToken)
    
    
    public virtual Task<Operation<RejectSpokeUpdateResponse, OperationMetadata>> RejectSpokeUpdateAsync(HubName name, SpokeName spokeUri, string spokeEtag, CancellationToken cancellationToken)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[HubName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubName)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to reject update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    HubName name = HubName.FromProjectHub("[PROJECT]", "[HUB]");
    SpokeName spokeUri = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]");
    string spokeEtag = "";
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.RejectSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdateAsync(RejectSpokeUpdateRequest, CallSettings)
    
    
    public virtual Task<Operation<RejectSpokeUpdateResponse, OperationMetadata>> RejectSpokeUpdateAsync(RejectSpokeUpdateRequest request, CallSettings callSettings = null)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectSpokeUpdateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    RejectSpokeUpdateRequest request = new RejectSpokeUpdateRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        SpokeEtag = "",
        Details = "",
        RequestId = "",
    };
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.RejectSpokeUpdateAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdateAsync(RejectSpokeUpdateRequest, CancellationToken)
    
    
    public virtual Task<Operation<RejectSpokeUpdateResponse, OperationMetadata>> RejectSpokeUpdateAsync(RejectSpokeUpdateRequest request, CancellationToken cancellationToken)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectSpokeUpdateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    RejectSpokeUpdateRequest request = new RejectSpokeUpdateRequest
    {
        HubName = HubName.FromProjectHub("[PROJECT]", "[HUB]"),
        SpokeUriAsSpokeName = SpokeName.FromProjectLocationSpoke("[PROJECT]", "[LOCATION]", "[SPOKE]"),
        SpokeEtag = "",
        Details = "",
        RequestId = "",
    };
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.RejectSpokeUpdateAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdateAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Operation<RejectSpokeUpdateResponse, OperationMetadata>> RejectSpokeUpdateAsync(string name, string spokeUri, string spokeEtag, CallSettings callSettings = null)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to reject update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    string spokeEtag = "";
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.RejectSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### RejectSpokeUpdateAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<RejectSpokeUpdateResponse, OperationMetadata>> RejectSpokeUpdateAsync(string name, string spokeUri, string spokeEtag, CancellationToken cancellationToken)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The etag of the spoke to reject update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RejectSpokeUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RejectSpokeUpdateResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/global/hubs/[HUB]";
    string spokeUri = "projects/[PROJECT]/locations/[LOCATION]/spokes/[SPOKE]";
    string spokeEtag = "";
    // Make the request
    Operation<RejectSpokeUpdateResponse, OperationMetadata> response = await hubServiceClient.RejectSpokeUpdateAsync(name, spokeUri, spokeEtag);
    
    // Poll until the returned long-running operation is complete
    Operation<RejectSpokeUpdateResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RejectSpokeUpdateResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RejectSpokeUpdateResponse, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceRejectSpokeUpdateAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RejectSpokeUpdateResponse retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient#Google_Cloud_NetworkConnectivity_V1Beta_HubServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient#Google_Cloud_NetworkConnectivity_V1Beta_HubServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient#Google_Cloud_NetworkConnectivity_V1Beta_HubServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubServiceClient#Google_Cloud_NetworkConnectivity_V1Beta_HubServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateGatewayAdvertisedRoute(GatewayAdvertisedRoute, FieldMask, CallSettings)
    
    
    public virtual Operation<GatewayAdvertisedRoute, OperationMetadata> UpdateGatewayAdvertisedRoute(GatewayAdvertisedRoute gatewayAdvertisedRoute, FieldMask updateMask, CallSettings callSettings = null)

Update a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. The gateway advertised route to update. The gateway advertised route's `name` field is used to identify the gateway advertised route to update. Format: `projects/{project}/locations/{location}/spokes/{spoke}/gatewayAdvertisedRoutes/{gatewayAdvertisedRoute}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = hubServiceClient.UpdateGatewayAdvertisedRoute(gatewayAdvertisedRoute, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGatewayAdvertisedRoute(UpdateGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual Operation<GatewayAdvertisedRoute, OperationMetadata> UpdateGatewayAdvertisedRoute(UpdateGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Update a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    UpdateGatewayAdvertisedRouteRequest request = new UpdateGatewayAdvertisedRouteRequest
    {
        UpdateMask = new FieldMask(),
        GatewayAdvertisedRoute = new GatewayAdvertisedRoute(),
        RequestId = "",
    };
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = hubServiceClient.UpdateGatewayAdvertisedRoute(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateGatewayAdvertisedRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGatewayAdvertisedRouteAsync(GatewayAdvertisedRoute, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> UpdateGatewayAdvertisedRouteAsync(GatewayAdvertisedRoute gatewayAdvertisedRoute, FieldMask updateMask, CallSettings callSettings = null)

Update a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. The gateway advertised route to update. The gateway advertised route's `name` field is used to identify the gateway advertised route to update. Format: `projects/{project}/locations/{location}/spokes/{spoke}/gatewayAdvertisedRoutes/{gatewayAdvertisedRoute}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.UpdateGatewayAdvertisedRouteAsync(gatewayAdvertisedRoute, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGatewayAdvertisedRouteAsync(GatewayAdvertisedRoute, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> UpdateGatewayAdvertisedRouteAsync(GatewayAdvertisedRoute gatewayAdvertisedRoute, FieldMask updateMask, CancellationToken cancellationToken)

Update a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`gatewayAdvertisedRoute` | `[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)`  
Required. The gateway advertised route to update. The gateway advertised route's `name` field is used to identify the gateway advertised route to update. Format: `projects/{project}/locations/{location}/spokes/{spoke}/gatewayAdvertisedRoutes/{gatewayAdvertisedRoute}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    GatewayAdvertisedRoute gatewayAdvertisedRoute = new GatewayAdvertisedRoute();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.UpdateGatewayAdvertisedRouteAsync(gatewayAdvertisedRoute, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGatewayAdvertisedRouteAsync(UpdateGatewayAdvertisedRouteRequest, CallSettings)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> UpdateGatewayAdvertisedRouteAsync(UpdateGatewayAdvertisedRouteRequest request, CallSettings callSettings = null)

Update a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGatewayAdvertisedRouteRequest request = new UpdateGatewayAdvertisedRouteRequest
    {
        UpdateMask = new FieldMask(),
        GatewayAdvertisedRoute = new GatewayAdvertisedRoute(),
        RequestId = "",
    };
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.UpdateGatewayAdvertisedRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGatewayAdvertisedRouteAsync(UpdateGatewayAdvertisedRouteRequest, CancellationToken)
    
    
    public virtual Task<Operation<GatewayAdvertisedRoute, OperationMetadata>> UpdateGatewayAdvertisedRouteAsync(UpdateGatewayAdvertisedRouteRequest request, CancellationToken cancellationToken)

Update a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateGatewayAdvertisedRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GatewayAdvertisedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.GatewayAdvertisedRoute)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGatewayAdvertisedRouteRequest request = new UpdateGatewayAdvertisedRouteRequest
    {
        UpdateMask = new FieldMask(),
        GatewayAdvertisedRoute = new GatewayAdvertisedRoute(),
        RequestId = "",
    };
    // Make the request
    Operation<GatewayAdvertisedRoute, OperationMetadata> response = await hubServiceClient.UpdateGatewayAdvertisedRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GatewayAdvertisedRoute, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GatewayAdvertisedRoute result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GatewayAdvertisedRoute, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGatewayAdvertisedRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GatewayAdvertisedRoute retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGroup(Group, FieldMask, CallSettings)
    
    
    public virtual Operation<Group, OperationMetadata> UpdateGroup(Group group, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`group` | `[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)`  
Required. The state that the group should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    Group group = new Group();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Group, OperationMetadata> response = hubServiceClient.UpdateGroup(group, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Group, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Group result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Group, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Group retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGroup(UpdateGroupRequest, CallSettings)
    
    
    public virtual Operation<Group, OperationMetadata> UpdateGroup(UpdateGroupRequest request, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    UpdateGroupRequest request = new UpdateGroupRequest
    {
        UpdateMask = new FieldMask(),
        Group = new Group(),
        RequestId = "",
    };
    // Make the request
    Operation<Group, OperationMetadata> response = hubServiceClient.UpdateGroup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Group, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Group result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Group, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Group retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGroupAsync(Group, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Group, OperationMetadata>> UpdateGroupAsync(Group group, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`group` | `[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)`  
Required. The state that the group should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    Group group = new Group();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Group, OperationMetadata> response = await hubServiceClient.UpdateGroupAsync(group, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Group, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Group result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Group, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Group retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGroupAsync(Group, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Group, OperationMetadata>> UpdateGroupAsync(Group group, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`group` | `[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)`  
Required. The state that the group should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    Group group = new Group();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Group, OperationMetadata> response = await hubServiceClient.UpdateGroupAsync(group, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Group, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Group result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Group, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Group retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGroupAsync(UpdateGroupRequest, CallSettings)
    
    
    public virtual Task<Operation<Group, OperationMetadata>> UpdateGroupAsync(UpdateGroupRequest request, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGroupRequest request = new UpdateGroupRequest
    {
        UpdateMask = new FieldMask(),
        Group = new Group(),
        RequestId = "",
    };
    // Make the request
    Operation<Group, OperationMetadata> response = await hubServiceClient.UpdateGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Group, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Group result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Group, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Group retrievedResult = retrievedResponse.Result;
    }
    

### UpdateGroupAsync(UpdateGroupRequest, CancellationToken)
    
    
    public virtual Task<Operation<Group, OperationMetadata>> UpdateGroupAsync(UpdateGroupRequest request, CancellationToken cancellationToken)

Updates the parameters of a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Group](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Group)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGroupRequest request = new UpdateGroupRequest
    {
        UpdateMask = new FieldMask(),
        Group = new Group(),
        RequestId = "",
    };
    // Make the request
    Operation<Group, OperationMetadata> response = await hubServiceClient.UpdateGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Group, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Group result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Group, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Group retrievedResult = retrievedResponse.Result;
    }
    

### UpdateHub(Hub, FieldMask, CallSettings)
    
    
    public virtual Operation<Hub, OperationMetadata> UpdateHub(Hub hub, FieldMask updateMask, CallSettings callSettings = null)

Updates the description and/or labels of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The state that the hub should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing hub, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    Hub hub = new Hub();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Hub, OperationMetadata> response = hubServiceClient.UpdateHub(hub, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### UpdateHub(UpdateHubRequest, CallSettings)
    
    
    public virtual Operation<Hub, OperationMetadata> UpdateHub(UpdateHubRequest request, CallSettings callSettings = null)

Updates the description and/or labels of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    UpdateHubRequest request = new UpdateHubRequest
    {
        UpdateMask = new FieldMask(),
        Hub = new Hub(),
        RequestId = "",
    };
    // Make the request
    Operation<Hub, OperationMetadata> response = hubServiceClient.UpdateHub(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateHub(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### UpdateHubAsync(Hub, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> UpdateHubAsync(Hub hub, FieldMask updateMask, CallSettings callSettings = null)

Updates the description and/or labels of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The state that the hub should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing hub, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    Hub hub = new Hub();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.UpdateHubAsync(hub, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### UpdateHubAsync(Hub, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> UpdateHubAsync(Hub hub, FieldMask updateMask, CancellationToken cancellationToken)

Updates the description and/or labels of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`hub` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)`  
Required. The state that the hub should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing hub, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    Hub hub = new Hub();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.UpdateHubAsync(hub, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### UpdateHubAsync(UpdateHubRequest, CallSettings)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> UpdateHubAsync(UpdateHubRequest request, CallSettings callSettings = null)

Updates the description and/or labels of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateHubRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateHubRequest request = new UpdateHubRequest
    {
        UpdateMask = new FieldMask(),
        Hub = new Hub(),
        RequestId = "",
    };
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.UpdateHubAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### UpdateHubAsync(UpdateHubRequest, CancellationToken)
    
    
    public virtual Task<Operation<Hub, OperationMetadata>> UpdateHubAsync(UpdateHubRequest request, CancellationToken cancellationToken)

Updates the description and/or labels of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHubRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateHubRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateHubRequest request = new UpdateHubRequest
    {
        UpdateMask = new FieldMask(),
        Hub = new Hub(),
        RequestId = "",
    };
    // Make the request
    Operation<Hub, OperationMetadata> response = await hubServiceClient.UpdateHubAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Hub, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Hub result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Hub, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateHubAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Hub retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpoke(Spoke, FieldMask, CallSettings)
    
    
    public virtual Operation<Spoke, OperationMetadata> UpdateSpoke(Spoke spoke, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The state that the spoke should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing spoke, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    Spoke spoke = new Spoke();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Spoke, OperationMetadata> response = hubServiceClient.UpdateSpoke(spoke, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpoke(UpdateSpokeRequest, CallSettings)
    
    
    public virtual Operation<Spoke, OperationMetadata> UpdateSpoke(UpdateSpokeRequest request, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = HubServiceClient.Create();
    // Initialize request argument(s)
    UpdateSpokeRequest request = new UpdateSpokeRequest
    {
        UpdateMask = new FieldMask(),
        Spoke = new Spoke(),
        RequestId = "",
    };
    // Make the request
    Operation<Spoke, OperationMetadata> response = hubServiceClient.UpdateSpoke(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = hubServiceClient.PollOnceUpdateSpoke(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpokeAsync(Spoke, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> UpdateSpokeAsync(Spoke spoke, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The state that the spoke should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing spoke, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    Spoke spoke = new Spoke();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.UpdateSpokeAsync(spoke, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpokeAsync(Spoke, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> UpdateSpokeAsync(Spoke spoke, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`spoke` | `[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)`  
Required. The state that the spoke should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. In the case of an update to an existing spoke, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    Spoke spoke = new Spoke();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.UpdateSpokeAsync(spoke, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpokeAsync(UpdateSpokeRequest, CallSettings)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> UpdateSpokeAsync(UpdateSpokeRequest request, CallSettings callSettings = null)

Updates the parameters of a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSpokeRequest request = new UpdateSpokeRequest
    {
        UpdateMask = new FieldMask(),
        Spoke = new Spoke(),
        RequestId = "",
    };
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.UpdateSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpokeAsync(UpdateSpokeRequest, CancellationToken)
    
    
    public virtual Task<Operation<Spoke, OperationMetadata>> UpdateSpokeAsync(UpdateSpokeRequest request, CancellationToken cancellationToken)

Updates the parameters of a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpokeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.UpdateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Spoke)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    HubServiceClient hubServiceClient = await HubServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSpokeRequest request = new UpdateSpokeRequest
    {
        UpdateMask = new FieldMask(),
        Spoke = new Spoke(),
        RequestId = "",
    };
    // Make the request
    Operation<Spoke, OperationMetadata> response = await hubServiceClient.UpdateSpokeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Spoke, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Spoke result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Spoke, OperationMetadata> retrievedResponse = await hubServiceClient.PollOnceUpdateSpokeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Spoke retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
