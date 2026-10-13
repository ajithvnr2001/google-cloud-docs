---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient
title: Discovery Engine v1beta API - Class AclConfigServiceClient (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:29.332495+00:00
---

# Discovery Engine v1beta API - Class AclConfigServiceClient (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class AclConfigServiceClient (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public abstract class AclConfigServiceClient

Reference documentation and code samples for the Discovery Engine v1beta API class AclConfigServiceClient.

AclConfigService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AclConfigServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AclConfigServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClientImpl)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Remarks

Service for managing Acl Configuration.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AclConfigService service, which is a host of "discoveryengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AclConfigService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AclConfigService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/discoveryengine.readwrite>
  * <https://www.googleapis.com/auth/discoveryengine.serving.readwrite>



### GrpcClient
    
    
    public virtual AclConfigService.AclConfigServiceClient GrpcClient { get; }

The underlying gRPC AclConfigService client

**Property Value**  
---  
**Type** | **Description**  
`[AclConfigService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigService)[AclConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigService.AclConfigServiceClient)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static AclConfigServiceClient Create()

Synchronously creates a [AclConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AclConfigServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AclConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient)` | The created [AclConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AclConfigServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AclConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AclConfigServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient)` | The task representing the created [AclConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient).  
  
### GetAclConfig(AclConfigName, CallSettings)
    
    
    public virtual AclConfig GetAclConfig(AclConfigName name, CallSettings callSettings = null)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigName)`  
Required. Resource name of [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], such as `projects/*/locations/*/aclConfig`. If the caller does not have permission to access the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = AclConfigServiceClient.Create();
    // Initialize request argument(s)
    AclConfigName name = AclConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    AclConfig response = aclConfigServiceClient.GetAclConfig(name);
    

### GetAclConfig(GetAclConfigRequest, CallSettings)
    
    
    public virtual AclConfig GetAclConfig(GetAclConfigRequest request, CallSettings callSettings = null)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetAclConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = AclConfigServiceClient.Create();
    // Initialize request argument(s)
    GetAclConfigRequest request = new GetAclConfigRequest
    {
        AclConfigName = AclConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    AclConfig response = aclConfigServiceClient.GetAclConfig(request);
    

### GetAclConfig(string, CallSettings)
    
    
    public virtual AclConfig GetAclConfig(string name, CallSettings callSettings = null)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], such as `projects/*/locations/*/aclConfig`. If the caller does not have permission to access the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = AclConfigServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/aclConfig";
    // Make the request
    AclConfig response = aclConfigServiceClient.GetAclConfig(name);
    

### GetAclConfigAsync(AclConfigName, CallSettings)
    
    
    public virtual Task<AclConfig> GetAclConfigAsync(AclConfigName name, CallSettings callSettings = null)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigName)`  
Required. Resource name of [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], such as `projects/*/locations/*/aclConfig`. If the caller does not have permission to access the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    AclConfigName name = AclConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    AclConfig response = await aclConfigServiceClient.GetAclConfigAsync(name);
    

### GetAclConfigAsync(AclConfigName, CancellationToken)
    
    
    public virtual Task<AclConfig> GetAclConfigAsync(AclConfigName name, CancellationToken cancellationToken)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigName)`  
Required. Resource name of [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], such as `projects/*/locations/*/aclConfig`. If the caller does not have permission to access the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    AclConfigName name = AclConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    AclConfig response = await aclConfigServiceClient.GetAclConfigAsync(name);
    

### GetAclConfigAsync(GetAclConfigRequest, CallSettings)
    
    
    public virtual Task<AclConfig> GetAclConfigAsync(GetAclConfigRequest request, CallSettings callSettings = null)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetAclConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAclConfigRequest request = new GetAclConfigRequest
    {
        AclConfigName = AclConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    AclConfig response = await aclConfigServiceClient.GetAclConfigAsync(request);
    

### GetAclConfigAsync(GetAclConfigRequest, CancellationToken)
    
    
    public virtual Task<AclConfig> GetAclConfigAsync(GetAclConfigRequest request, CancellationToken cancellationToken)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetAclConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAclConfigRequest request = new GetAclConfigRequest
    {
        AclConfigName = AclConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    AclConfig response = await aclConfigServiceClient.GetAclConfigAsync(request);
    

### GetAclConfigAsync(string, CallSettings)
    
    
    public virtual Task<AclConfig> GetAclConfigAsync(string name, CallSettings callSettings = null)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], such as `projects/*/locations/*/aclConfig`. If the caller does not have permission to access the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/aclConfig";
    // Make the request
    AclConfig response = await aclConfigServiceClient.GetAclConfigAsync(name);
    

### GetAclConfigAsync(string, CancellationToken)
    
    
    public virtual Task<AclConfig> GetAclConfigAsync(string name, CancellationToken cancellationToken)

Gets the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], such as `projects/*/locations/*/aclConfig`. If the caller does not have permission to access the [AclConfig][google.cloud.discoveryengine.v1beta.AclConfig], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/aclConfig";
    // Make the request
    AclConfig response = await aclConfigServiceClient.GetAclConfigAsync(name);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AclConfigServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AclConfigServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AclConfigServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfigServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AclConfigServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateAclConfig(UpdateAclConfigRequest, CallSettings)
    
    
    public virtual AclConfig UpdateAclConfig(UpdateAclConfigRequest request, CallSettings callSettings = null)

Default ACL configuration for use in a location of a customer's project. Updates will only reflect to new data stores. Existing data stores will still use the old value.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateAclConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = AclConfigServiceClient.Create();
    // Initialize request argument(s)
    UpdateAclConfigRequest request = new UpdateAclConfigRequest
    {
        AclConfig = new AclConfig(),
    };
    // Make the request
    AclConfig response = aclConfigServiceClient.UpdateAclConfig(request);
    

### UpdateAclConfigAsync(UpdateAclConfigRequest, CallSettings)
    
    
    public virtual Task<AclConfig> UpdateAclConfigAsync(UpdateAclConfigRequest request, CallSettings callSettings = null)

Default ACL configuration for use in a location of a customer's project. Updates will only reflect to new data stores. Existing data stores will still use the old value.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateAclConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAclConfigRequest request = new UpdateAclConfigRequest
    {
        AclConfig = new AclConfig(),
    };
    // Make the request
    AclConfig response = await aclConfigServiceClient.UpdateAclConfigAsync(request);
    

### UpdateAclConfigAsync(UpdateAclConfigRequest, CancellationToken)
    
    
    public virtual Task<AclConfig> UpdateAclConfigAsync(UpdateAclConfigRequest request, CancellationToken cancellationToken)

Default ACL configuration for use in a location of a customer's project. Updates will only reflect to new data stores. Existing data stores will still use the old value.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateAclConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AclConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AclConfigServiceClient aclConfigServiceClient = await AclConfigServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAclConfigRequest request = new UpdateAclConfigRequest
    {
        AclConfig = new AclConfig(),
    };
    // Make the request
    AclConfig response = await aclConfigServiceClient.UpdateAclConfigAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
