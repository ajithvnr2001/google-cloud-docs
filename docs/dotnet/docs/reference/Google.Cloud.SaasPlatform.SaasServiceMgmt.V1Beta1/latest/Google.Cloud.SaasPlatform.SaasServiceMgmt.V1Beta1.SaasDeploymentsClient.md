---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient
title: SaaS Runtime v1beta1 API - Class SaasDeploymentsClient (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:07.977772+00:00
---

# SaaS Runtime v1beta1 API - Class SaasDeploymentsClient (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  SaaS Runtime v1beta1 API - Class SaasDeploymentsClient (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public abstract class SaasDeploymentsClient

Reference documentation and code samples for the SaaS Runtime v1beta1 API class SaasDeploymentsClient.

SaasDeployments client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SaasDeploymentsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[SaasDeploymentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClientImpl)

## Namespace

[Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1)

## Assembly

Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.dll

## Remarks

Manages the deployment of SaaS services.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the SaasDeployments service, which is a host of "saasservicemgmt.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default SaasDeployments scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default SaasDeployments scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual SaasDeployments.SaasDeploymentsClient GrpcClient { get; }

The underlying gRPC SaasDeployments client

**Property Value**  
---  
**Type** | **Description**  
`[SaasDeployments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeployments)[SaasDeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeployments.SaasDeploymentsClient)` |   
  
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
    
    
    public static SaasDeploymentsClient Create()

Synchronously creates a [SaasDeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SaasDeploymentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient)` | The created [SaasDeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<SaasDeploymentsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [SaasDeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SaasDeploymentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SaasDeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient)` | The task representing the created [SaasDeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient).  
  
### CreateRelease(LocationName, Release, string, CallSettings)
    
    
    public virtual Release CreateRelease(LocationName parent, Release release, string releaseId, CallSettings callSettings = null)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new release.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Release release = new Release();
    string releaseId = "";
    // Make the request
    Release response = saasDeploymentsClient.CreateRelease(parent, release, releaseId);
    

### CreateRelease(CreateReleaseRequest, CallSettings)
    
    
    public virtual Release CreateRelease(CreateReleaseRequest request, CallSettings callSettings = null)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    CreateReleaseRequest request = new CreateReleaseRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        ReleaseId = "",
        Release = new Release(),
    };
    // Make the request
    Release response = saasDeploymentsClient.CreateRelease(request);
    

### CreateRelease(string, Release, string, CallSettings)
    
    
    public virtual Release CreateRelease(string parent, Release release, string releaseId, CallSettings callSettings = null)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new release.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Release release = new Release();
    string releaseId = "";
    // Make the request
    Release response = saasDeploymentsClient.CreateRelease(parent, release, releaseId);
    

### CreateReleaseAsync(LocationName, Release, string, CallSettings)
    
    
    public virtual Task<Release> CreateReleaseAsync(LocationName parent, Release release, string releaseId, CallSettings callSettings = null)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new release.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Release release = new Release();
    string releaseId = "";
    // Make the request
    Release response = await saasDeploymentsClient.CreateReleaseAsync(parent, release, releaseId);
    

### CreateReleaseAsync(LocationName, Release, string, CancellationToken)
    
    
    public virtual Task<Release> CreateReleaseAsync(LocationName parent, Release release, string releaseId, CancellationToken cancellationToken)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new release.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Release release = new Release();
    string releaseId = "";
    // Make the request
    Release response = await saasDeploymentsClient.CreateReleaseAsync(parent, release, releaseId);
    

### CreateReleaseAsync(CreateReleaseRequest, CallSettings)
    
    
    public virtual Task<Release> CreateReleaseAsync(CreateReleaseRequest request, CallSettings callSettings = null)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateReleaseRequest request = new CreateReleaseRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        ReleaseId = "",
        Release = new Release(),
    };
    // Make the request
    Release response = await saasDeploymentsClient.CreateReleaseAsync(request);
    

### CreateReleaseAsync(CreateReleaseRequest, CancellationToken)
    
    
    public virtual Task<Release> CreateReleaseAsync(CreateReleaseRequest request, CancellationToken cancellationToken)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateReleaseRequest request = new CreateReleaseRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        ReleaseId = "",
        Release = new Release(),
    };
    // Make the request
    Release response = await saasDeploymentsClient.CreateReleaseAsync(request);
    

### CreateReleaseAsync(string, Release, string, CallSettings)
    
    
    public virtual Task<Release> CreateReleaseAsync(string parent, Release release, string releaseId, CallSettings callSettings = null)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new release.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Release release = new Release();
    string releaseId = "";
    // Make the request
    Release response = await saasDeploymentsClient.CreateReleaseAsync(parent, release, releaseId);
    

### CreateReleaseAsync(string, Release, string, CancellationToken)
    
    
    public virtual Task<Release> CreateReleaseAsync(string parent, Release release, string releaseId, CancellationToken cancellationToken)

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new release.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Release release = new Release();
    string releaseId = "";
    // Make the request
    Release response = await saasDeploymentsClient.CreateReleaseAsync(parent, release, releaseId);
    

### CreateSaas(LocationName, Saas, string, CallSettings)
    
    
    public virtual Saas CreateSaas(LocationName parent, Saas saas, string saasId, CallSettings callSettings = null)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new saas.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Saas saas = new Saas();
    string saasId = "";
    // Make the request
    Saas response = saasDeploymentsClient.CreateSaas(parent, saas, saasId);
    

### CreateSaas(CreateSaasRequest, CallSettings)
    
    
    public virtual Saas CreateSaas(CreateSaasRequest request, CallSettings callSettings = null)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    CreateSaasRequest request = new CreateSaasRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        SaasId = "",
        Saas = new Saas(),
    };
    // Make the request
    Saas response = saasDeploymentsClient.CreateSaas(request);
    

### CreateSaas(string, Saas, string, CallSettings)
    
    
    public virtual Saas CreateSaas(string parent, Saas saas, string saasId, CallSettings callSettings = null)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new saas.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Saas saas = new Saas();
    string saasId = "";
    // Make the request
    Saas response = saasDeploymentsClient.CreateSaas(parent, saas, saasId);
    

### CreateSaasAsync(LocationName, Saas, string, CallSettings)
    
    
    public virtual Task<Saas> CreateSaasAsync(LocationName parent, Saas saas, string saasId, CallSettings callSettings = null)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new saas.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Saas saas = new Saas();
    string saasId = "";
    // Make the request
    Saas response = await saasDeploymentsClient.CreateSaasAsync(parent, saas, saasId);
    

### CreateSaasAsync(LocationName, Saas, string, CancellationToken)
    
    
    public virtual Task<Saas> CreateSaasAsync(LocationName parent, Saas saas, string saasId, CancellationToken cancellationToken)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new saas.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Saas saas = new Saas();
    string saasId = "";
    // Make the request
    Saas response = await saasDeploymentsClient.CreateSaasAsync(parent, saas, saasId);
    

### CreateSaasAsync(CreateSaasRequest, CallSettings)
    
    
    public virtual Task<Saas> CreateSaasAsync(CreateSaasRequest request, CallSettings callSettings = null)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateSaasRequest request = new CreateSaasRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        SaasId = "",
        Saas = new Saas(),
    };
    // Make the request
    Saas response = await saasDeploymentsClient.CreateSaasAsync(request);
    

### CreateSaasAsync(CreateSaasRequest, CancellationToken)
    
    
    public virtual Task<Saas> CreateSaasAsync(CreateSaasRequest request, CancellationToken cancellationToken)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateSaasRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateSaasRequest request = new CreateSaasRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        SaasId = "",
        Saas = new Saas(),
    };
    // Make the request
    Saas response = await saasDeploymentsClient.CreateSaasAsync(request);
    

### CreateSaasAsync(string, Saas, string, CallSettings)
    
    
    public virtual Task<Saas> CreateSaasAsync(string parent, Saas saas, string saasId, CallSettings callSettings = null)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new saas.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Saas saas = new Saas();
    string saasId = "";
    // Make the request
    Saas response = await saasDeploymentsClient.CreateSaasAsync(parent, saas, saasId);
    

### CreateSaasAsync(string, Saas, string, CancellationToken)
    
    
    public virtual Task<Saas> CreateSaasAsync(string parent, Saas saas, string saasId, CancellationToken cancellationToken)

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new saas.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Saas saas = new Saas();
    string saasId = "";
    // Make the request
    Saas response = await saasDeploymentsClient.CreateSaasAsync(parent, saas, saasId);
    

### CreateTenant(LocationName, Tenant, string, CallSettings)
    
    
    public virtual Tenant CreateTenant(LocationName parent, Tenant tenant, string tenantId, CallSettings callSettings = null)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new tenant.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Tenant tenant = new Tenant();
    string tenantId = "";
    // Make the request
    Tenant response = saasDeploymentsClient.CreateTenant(parent, tenant, tenantId);
    

### CreateTenant(CreateTenantRequest, CallSettings)
    
    
    public virtual Tenant CreateTenant(CreateTenantRequest request, CallSettings callSettings = null)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    CreateTenantRequest request = new CreateTenantRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        TenantId = "",
        Tenant = new Tenant(),
    };
    // Make the request
    Tenant response = saasDeploymentsClient.CreateTenant(request);
    

### CreateTenant(string, Tenant, string, CallSettings)
    
    
    public virtual Tenant CreateTenant(string parent, Tenant tenant, string tenantId, CallSettings callSettings = null)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new tenant.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Tenant tenant = new Tenant();
    string tenantId = "";
    // Make the request
    Tenant response = saasDeploymentsClient.CreateTenant(parent, tenant, tenantId);
    

### CreateTenantAsync(LocationName, Tenant, string, CallSettings)
    
    
    public virtual Task<Tenant> CreateTenantAsync(LocationName parent, Tenant tenant, string tenantId, CallSettings callSettings = null)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new tenant.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Tenant tenant = new Tenant();
    string tenantId = "";
    // Make the request
    Tenant response = await saasDeploymentsClient.CreateTenantAsync(parent, tenant, tenantId);
    

### CreateTenantAsync(LocationName, Tenant, string, CancellationToken)
    
    
    public virtual Task<Tenant> CreateTenantAsync(LocationName parent, Tenant tenant, string tenantId, CancellationToken cancellationToken)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new tenant.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Tenant tenant = new Tenant();
    string tenantId = "";
    // Make the request
    Tenant response = await saasDeploymentsClient.CreateTenantAsync(parent, tenant, tenantId);
    

### CreateTenantAsync(CreateTenantRequest, CallSettings)
    
    
    public virtual Task<Tenant> CreateTenantAsync(CreateTenantRequest request, CallSettings callSettings = null)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateTenantRequest request = new CreateTenantRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        TenantId = "",
        Tenant = new Tenant(),
    };
    // Make the request
    Tenant response = await saasDeploymentsClient.CreateTenantAsync(request);
    

### CreateTenantAsync(CreateTenantRequest, CancellationToken)
    
    
    public virtual Task<Tenant> CreateTenantAsync(CreateTenantRequest request, CancellationToken cancellationToken)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateTenantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateTenantRequest request = new CreateTenantRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        TenantId = "",
        Tenant = new Tenant(),
    };
    // Make the request
    Tenant response = await saasDeploymentsClient.CreateTenantAsync(request);
    

### CreateTenantAsync(string, Tenant, string, CallSettings)
    
    
    public virtual Task<Tenant> CreateTenantAsync(string parent, Tenant tenant, string tenantId, CallSettings callSettings = null)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new tenant.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Tenant tenant = new Tenant();
    string tenantId = "";
    // Make the request
    Tenant response = await saasDeploymentsClient.CreateTenantAsync(parent, tenant, tenantId);
    

### CreateTenantAsync(string, Tenant, string, CancellationToken)
    
    
    public virtual Task<Tenant> CreateTenantAsync(string parent, Tenant tenant, string tenantId, CancellationToken cancellationToken)

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new tenant.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Tenant tenant = new Tenant();
    string tenantId = "";
    // Make the request
    Tenant response = await saasDeploymentsClient.CreateTenantAsync(parent, tenant, tenantId);
    

### CreateUnit(LocationName, Unit, string, CallSettings)
    
    
    public virtual Unit CreateUnit(LocationName parent, Unit unit, string unitId, CallSettings callSettings = null)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Unit unit = new Unit();
    string unitId = "";
    // Make the request
    Unit response = saasDeploymentsClient.CreateUnit(parent, unit, unitId);
    

### CreateUnit(CreateUnitRequest, CallSettings)
    
    
    public virtual Unit CreateUnit(CreateUnitRequest request, CallSettings callSettings = null)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    CreateUnitRequest request = new CreateUnitRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitId = "",
        Unit = new Unit(),
    };
    // Make the request
    Unit response = saasDeploymentsClient.CreateUnit(request);
    

### CreateUnit(string, Unit, string, CallSettings)
    
    
    public virtual Unit CreateUnit(string parent, Unit unit, string unitId, CallSettings callSettings = null)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Unit unit = new Unit();
    string unitId = "";
    // Make the request
    Unit response = saasDeploymentsClient.CreateUnit(parent, unit, unitId);
    

### CreateUnitAsync(LocationName, Unit, string, CallSettings)
    
    
    public virtual Task<Unit> CreateUnitAsync(LocationName parent, Unit unit, string unitId, CallSettings callSettings = null)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Unit unit = new Unit();
    string unitId = "";
    // Make the request
    Unit response = await saasDeploymentsClient.CreateUnitAsync(parent, unit, unitId);
    

### CreateUnitAsync(LocationName, Unit, string, CancellationToken)
    
    
    public virtual Task<Unit> CreateUnitAsync(LocationName parent, Unit unit, string unitId, CancellationToken cancellationToken)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Unit unit = new Unit();
    string unitId = "";
    // Make the request
    Unit response = await saasDeploymentsClient.CreateUnitAsync(parent, unit, unitId);
    

### CreateUnitAsync(CreateUnitRequest, CallSettings)
    
    
    public virtual Task<Unit> CreateUnitAsync(CreateUnitRequest request, CallSettings callSettings = null)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateUnitRequest request = new CreateUnitRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitId = "",
        Unit = new Unit(),
    };
    // Make the request
    Unit response = await saasDeploymentsClient.CreateUnitAsync(request);
    

### CreateUnitAsync(CreateUnitRequest, CancellationToken)
    
    
    public virtual Task<Unit> CreateUnitAsync(CreateUnitRequest request, CancellationToken cancellationToken)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateUnitRequest request = new CreateUnitRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitId = "",
        Unit = new Unit(),
    };
    // Make the request
    Unit response = await saasDeploymentsClient.CreateUnitAsync(request);
    

### CreateUnitAsync(string, Unit, string, CallSettings)
    
    
    public virtual Task<Unit> CreateUnitAsync(string parent, Unit unit, string unitId, CallSettings callSettings = null)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Unit unit = new Unit();
    string unitId = "";
    // Make the request
    Unit response = await saasDeploymentsClient.CreateUnitAsync(parent, unit, unitId);
    

### CreateUnitAsync(string, Unit, string, CancellationToken)
    
    
    public virtual Task<Unit> CreateUnitAsync(string parent, Unit unit, string unitId, CancellationToken cancellationToken)

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Unit unit = new Unit();
    string unitId = "";
    // Make the request
    Unit response = await saasDeploymentsClient.CreateUnitAsync(parent, unit, unitId);
    

### CreateUnitKind(LocationName, UnitKind, string, CallSettings)
    
    
    public virtual UnitKind CreateUnitKind(LocationName parent, UnitKind unitKind, string unitKindId, CallSettings callSettings = null)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit kind.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    UnitKind unitKind = new UnitKind();
    string unitKindId = "";
    // Make the request
    UnitKind response = saasDeploymentsClient.CreateUnitKind(parent, unitKind, unitKindId);
    

### CreateUnitKind(CreateUnitKindRequest, CallSettings)
    
    
    public virtual UnitKind CreateUnitKind(CreateUnitKindRequest request, CallSettings callSettings = null)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    CreateUnitKindRequest request = new CreateUnitKindRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitKindId = "",
        UnitKind = new UnitKind(),
    };
    // Make the request
    UnitKind response = saasDeploymentsClient.CreateUnitKind(request);
    

### CreateUnitKind(string, UnitKind, string, CallSettings)
    
    
    public virtual UnitKind CreateUnitKind(string parent, UnitKind unitKind, string unitKindId, CallSettings callSettings = null)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit kind.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    UnitKind unitKind = new UnitKind();
    string unitKindId = "";
    // Make the request
    UnitKind response = saasDeploymentsClient.CreateUnitKind(parent, unitKind, unitKindId);
    

### CreateUnitKindAsync(LocationName, UnitKind, string, CallSettings)
    
    
    public virtual Task<UnitKind> CreateUnitKindAsync(LocationName parent, UnitKind unitKind, string unitKindId, CallSettings callSettings = null)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit kind.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    UnitKind unitKind = new UnitKind();
    string unitKindId = "";
    // Make the request
    UnitKind response = await saasDeploymentsClient.CreateUnitKindAsync(parent, unitKind, unitKindId);
    

### CreateUnitKindAsync(LocationName, UnitKind, string, CancellationToken)
    
    
    public virtual Task<UnitKind> CreateUnitKindAsync(LocationName parent, UnitKind unitKind, string unitKindId, CancellationToken cancellationToken)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit kind.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    UnitKind unitKind = new UnitKind();
    string unitKindId = "";
    // Make the request
    UnitKind response = await saasDeploymentsClient.CreateUnitKindAsync(parent, unitKind, unitKindId);
    

### CreateUnitKindAsync(CreateUnitKindRequest, CallSettings)
    
    
    public virtual Task<UnitKind> CreateUnitKindAsync(CreateUnitKindRequest request, CallSettings callSettings = null)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateUnitKindRequest request = new CreateUnitKindRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitKindId = "",
        UnitKind = new UnitKind(),
    };
    // Make the request
    UnitKind response = await saasDeploymentsClient.CreateUnitKindAsync(request);
    

### CreateUnitKindAsync(CreateUnitKindRequest, CancellationToken)
    
    
    public virtual Task<UnitKind> CreateUnitKindAsync(CreateUnitKindRequest request, CancellationToken cancellationToken)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateUnitKindRequest request = new CreateUnitKindRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitKindId = "",
        UnitKind = new UnitKind(),
    };
    // Make the request
    UnitKind response = await saasDeploymentsClient.CreateUnitKindAsync(request);
    

### CreateUnitKindAsync(string, UnitKind, string, CallSettings)
    
    
    public virtual Task<UnitKind> CreateUnitKindAsync(string parent, UnitKind unitKind, string unitKindId, CallSettings callSettings = null)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit kind.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    UnitKind unitKind = new UnitKind();
    string unitKindId = "";
    // Make the request
    UnitKind response = await saasDeploymentsClient.CreateUnitKindAsync(parent, unitKind, unitKindId);
    

### CreateUnitKindAsync(string, UnitKind, string, CancellationToken)
    
    
    public virtual Task<UnitKind> CreateUnitKindAsync(string parent, UnitKind unitKind, string unitKindId, CancellationToken cancellationToken)

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit kind.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    UnitKind unitKind = new UnitKind();
    string unitKindId = "";
    // Make the request
    UnitKind response = await saasDeploymentsClient.CreateUnitKindAsync(parent, unitKind, unitKindId);
    

### CreateUnitOperation(LocationName, UnitOperation, string, CallSettings)
    
    
    public virtual UnitOperation CreateUnitOperation(LocationName parent, UnitOperation unitOperation, string unitOperationId, CallSettings callSettings = null)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit operation.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    UnitOperation unitOperation = new UnitOperation();
    string unitOperationId = "";
    // Make the request
    UnitOperation response = saasDeploymentsClient.CreateUnitOperation(parent, unitOperation, unitOperationId);
    

### CreateUnitOperation(CreateUnitOperationRequest, CallSettings)
    
    
    public virtual UnitOperation CreateUnitOperation(CreateUnitOperationRequest request, CallSettings callSettings = null)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    CreateUnitOperationRequest request = new CreateUnitOperationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitOperationId = "",
        UnitOperation = new UnitOperation(),
    };
    // Make the request
    UnitOperation response = saasDeploymentsClient.CreateUnitOperation(request);
    

### CreateUnitOperation(string, UnitOperation, string, CallSettings)
    
    
    public virtual UnitOperation CreateUnitOperation(string parent, UnitOperation unitOperation, string unitOperationId, CallSettings callSettings = null)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit operation.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    UnitOperation unitOperation = new UnitOperation();
    string unitOperationId = "";
    // Make the request
    UnitOperation response = saasDeploymentsClient.CreateUnitOperation(parent, unitOperation, unitOperationId);
    

### CreateUnitOperationAsync(LocationName, UnitOperation, string, CallSettings)
    
    
    public virtual Task<UnitOperation> CreateUnitOperationAsync(LocationName parent, UnitOperation unitOperation, string unitOperationId, CallSettings callSettings = null)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit operation.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    UnitOperation unitOperation = new UnitOperation();
    string unitOperationId = "";
    // Make the request
    UnitOperation response = await saasDeploymentsClient.CreateUnitOperationAsync(parent, unitOperation, unitOperationId);
    

### CreateUnitOperationAsync(LocationName, UnitOperation, string, CancellationToken)
    
    
    public virtual Task<UnitOperation> CreateUnitOperationAsync(LocationName parent, UnitOperation unitOperation, string unitOperationId, CancellationToken cancellationToken)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit operation.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    UnitOperation unitOperation = new UnitOperation();
    string unitOperationId = "";
    // Make the request
    UnitOperation response = await saasDeploymentsClient.CreateUnitOperationAsync(parent, unitOperation, unitOperationId);
    

### CreateUnitOperationAsync(CreateUnitOperationRequest, CallSettings)
    
    
    public virtual Task<UnitOperation> CreateUnitOperationAsync(CreateUnitOperationRequest request, CallSettings callSettings = null)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateUnitOperationRequest request = new CreateUnitOperationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitOperationId = "",
        UnitOperation = new UnitOperation(),
    };
    // Make the request
    UnitOperation response = await saasDeploymentsClient.CreateUnitOperationAsync(request);
    

### CreateUnitOperationAsync(CreateUnitOperationRequest, CancellationToken)
    
    
    public virtual Task<UnitOperation> CreateUnitOperationAsync(CreateUnitOperationRequest request, CancellationToken cancellationToken)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.CreateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateUnitOperationRequest request = new CreateUnitOperationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ValidateOnly = false,
        RequestId = "",
        UnitOperationId = "",
        UnitOperation = new UnitOperation(),
    };
    // Make the request
    UnitOperation response = await saasDeploymentsClient.CreateUnitOperationAsync(request);
    

### CreateUnitOperationAsync(string, UnitOperation, string, CallSettings)
    
    
    public virtual Task<UnitOperation> CreateUnitOperationAsync(string parent, UnitOperation unitOperation, string unitOperationId, CallSettings callSettings = null)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit operation.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    UnitOperation unitOperation = new UnitOperation();
    string unitOperationId = "";
    // Make the request
    UnitOperation response = await saasDeploymentsClient.CreateUnitOperationAsync(parent, unitOperation, unitOperationId);
    

### CreateUnitOperationAsync(string, UnitOperation, string, CancellationToken)
    
    
    public virtual Task<UnitOperation> CreateUnitOperationAsync(string parent, UnitOperation unitOperation, string unitOperationId, CancellationToken cancellationToken)

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID value for the new unit operation.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    UnitOperation unitOperation = new UnitOperation();
    string unitOperationId = "";
    // Make the request
    UnitOperation response = await saasDeploymentsClient.CreateUnitOperationAsync(parent, unitOperation, unitOperationId);
    

### DeleteRelease(DeleteReleaseRequest, CallSettings)
    
    
    public virtual void DeleteRelease(DeleteReleaseRequest request, CallSettings callSettings = null)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    DeleteReleaseRequest request = new DeleteReleaseRequest
    {
        ReleaseName = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    saasDeploymentsClient.DeleteRelease(request);
    

### DeleteRelease(ReleaseName, CallSettings)
    
    
    public virtual void DeleteRelease(ReleaseName name, CallSettings callSettings = null)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReleaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ReleaseName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ReleaseName name = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]");
    // Make the request
    saasDeploymentsClient.DeleteRelease(name);
    

### DeleteRelease(string, CallSettings)
    
    
    public virtual void DeleteRelease(string name, CallSettings callSettings = null)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/releases/[RELEASE]";
    // Make the request
    saasDeploymentsClient.DeleteRelease(name);
    

### DeleteReleaseAsync(DeleteReleaseRequest, CallSettings)
    
    
    public virtual Task DeleteReleaseAsync(DeleteReleaseRequest request, CallSettings callSettings = null)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteReleaseRequest request = new DeleteReleaseRequest
    {
        ReleaseName = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteReleaseAsync(request);
    

### DeleteReleaseAsync(DeleteReleaseRequest, CancellationToken)
    
    
    public virtual Task DeleteReleaseAsync(DeleteReleaseRequest request, CancellationToken cancellationToken)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteReleaseRequest request = new DeleteReleaseRequest
    {
        ReleaseName = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteReleaseAsync(request);
    

### DeleteReleaseAsync(ReleaseName, CallSettings)
    
    
    public virtual Task DeleteReleaseAsync(ReleaseName name, CallSettings callSettings = null)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReleaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ReleaseName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ReleaseName name = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]");
    // Make the request
    await saasDeploymentsClient.DeleteReleaseAsync(name);
    

### DeleteReleaseAsync(ReleaseName, CancellationToken)
    
    
    public virtual Task DeleteReleaseAsync(ReleaseName name, CancellationToken cancellationToken)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReleaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ReleaseName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ReleaseName name = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]");
    // Make the request
    await saasDeploymentsClient.DeleteReleaseAsync(name);
    

### DeleteReleaseAsync(string, CallSettings)
    
    
    public virtual Task DeleteReleaseAsync(string name, CallSettings callSettings = null)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/releases/[RELEASE]";
    // Make the request
    await saasDeploymentsClient.DeleteReleaseAsync(name);
    

### DeleteReleaseAsync(string, CancellationToken)
    
    
    public virtual Task DeleteReleaseAsync(string name, CancellationToken cancellationToken)

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/releases/[RELEASE]";
    // Make the request
    await saasDeploymentsClient.DeleteReleaseAsync(name);
    

### DeleteSaas(DeleteSaasRequest, CallSettings)
    
    
    public virtual void DeleteSaas(DeleteSaasRequest request, CallSettings callSettings = null)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    DeleteSaasRequest request = new DeleteSaasRequest
    {
        SaasName = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    saasDeploymentsClient.DeleteSaas(request);
    

### DeleteSaas(SaasName, CallSettings)
    
    
    public virtual void DeleteSaas(SaasName name, CallSettings callSettings = null)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SaasName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    SaasName name = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]");
    // Make the request
    saasDeploymentsClient.DeleteSaas(name);
    

### DeleteSaas(string, CallSettings)
    
    
    public virtual void DeleteSaas(string name, CallSettings callSettings = null)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/saas/[SAAS]";
    // Make the request
    saasDeploymentsClient.DeleteSaas(name);
    

### DeleteSaasAsync(DeleteSaasRequest, CallSettings)
    
    
    public virtual Task DeleteSaasAsync(DeleteSaasRequest request, CallSettings callSettings = null)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteSaasRequest request = new DeleteSaasRequest
    {
        SaasName = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteSaasAsync(request);
    

### DeleteSaasAsync(DeleteSaasRequest, CancellationToken)
    
    
    public virtual Task DeleteSaasAsync(DeleteSaasRequest request, CancellationToken cancellationToken)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteSaasRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteSaasRequest request = new DeleteSaasRequest
    {
        SaasName = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteSaasAsync(request);
    

### DeleteSaasAsync(SaasName, CallSettings)
    
    
    public virtual Task DeleteSaasAsync(SaasName name, CallSettings callSettings = null)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SaasName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    SaasName name = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]");
    // Make the request
    await saasDeploymentsClient.DeleteSaasAsync(name);
    

### DeleteSaasAsync(SaasName, CancellationToken)
    
    
    public virtual Task DeleteSaasAsync(SaasName name, CancellationToken cancellationToken)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SaasName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    SaasName name = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]");
    // Make the request
    await saasDeploymentsClient.DeleteSaasAsync(name);
    

### DeleteSaasAsync(string, CallSettings)
    
    
    public virtual Task DeleteSaasAsync(string name, CallSettings callSettings = null)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/saas/[SAAS]";
    // Make the request
    await saasDeploymentsClient.DeleteSaasAsync(name);
    

### DeleteSaasAsync(string, CancellationToken)
    
    
    public virtual Task DeleteSaasAsync(string name, CancellationToken cancellationToken)

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/saas/[SAAS]";
    // Make the request
    await saasDeploymentsClient.DeleteSaasAsync(name);
    

### DeleteTenant(DeleteTenantRequest, CallSettings)
    
    
    public virtual void DeleteTenant(DeleteTenantRequest request, CallSettings callSettings = null)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    DeleteTenantRequest request = new DeleteTenantRequest
    {
        TenantName = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    saasDeploymentsClient.DeleteTenant(request);
    

### DeleteTenant(TenantName, CallSettings)
    
    
    public virtual void DeleteTenant(TenantName name, CallSettings callSettings = null)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    TenantName name = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]");
    // Make the request
    saasDeploymentsClient.DeleteTenant(name);
    

### DeleteTenant(string, CallSettings)
    
    
    public virtual void DeleteTenant(string name, CallSettings callSettings = null)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/tenants/[TENANT]";
    // Make the request
    saasDeploymentsClient.DeleteTenant(name);
    

### DeleteTenantAsync(DeleteTenantRequest, CallSettings)
    
    
    public virtual Task DeleteTenantAsync(DeleteTenantRequest request, CallSettings callSettings = null)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteTenantRequest request = new DeleteTenantRequest
    {
        TenantName = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteTenantAsync(request);
    

### DeleteTenantAsync(DeleteTenantRequest, CancellationToken)
    
    
    public virtual Task DeleteTenantAsync(DeleteTenantRequest request, CancellationToken cancellationToken)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteTenantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteTenantRequest request = new DeleteTenantRequest
    {
        TenantName = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteTenantAsync(request);
    

### DeleteTenantAsync(TenantName, CallSettings)
    
    
    public virtual Task DeleteTenantAsync(TenantName name, CallSettings callSettings = null)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    TenantName name = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]");
    // Make the request
    await saasDeploymentsClient.DeleteTenantAsync(name);
    

### DeleteTenantAsync(TenantName, CancellationToken)
    
    
    public virtual Task DeleteTenantAsync(TenantName name, CancellationToken cancellationToken)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    TenantName name = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]");
    // Make the request
    await saasDeploymentsClient.DeleteTenantAsync(name);
    

### DeleteTenantAsync(string, CallSettings)
    
    
    public virtual Task DeleteTenantAsync(string name, CallSettings callSettings = null)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/tenants/[TENANT]";
    // Make the request
    await saasDeploymentsClient.DeleteTenantAsync(name);
    

### DeleteTenantAsync(string, CancellationToken)
    
    
    public virtual Task DeleteTenantAsync(string name, CancellationToken cancellationToken)

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/tenants/[TENANT]";
    // Make the request
    await saasDeploymentsClient.DeleteTenantAsync(name);
    

### DeleteUnit(DeleteUnitRequest, CallSettings)
    
    
    public virtual void DeleteUnit(DeleteUnitRequest request, CallSettings callSettings = null)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    DeleteUnitRequest request = new DeleteUnitRequest
    {
        UnitName = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    saasDeploymentsClient.DeleteUnit(request);
    

### DeleteUnit(UnitName, CallSettings)
    
    
    public virtual void DeleteUnit(UnitName name, CallSettings callSettings = null)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitName name = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]");
    // Make the request
    saasDeploymentsClient.DeleteUnit(name);
    

### DeleteUnit(string, CallSettings)
    
    
    public virtual void DeleteUnit(string name, CallSettings callSettings = null)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/units/[UNIT]";
    // Make the request
    saasDeploymentsClient.DeleteUnit(name);
    

### DeleteUnitAsync(DeleteUnitRequest, CallSettings)
    
    
    public virtual Task DeleteUnitAsync(DeleteUnitRequest request, CallSettings callSettings = null)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUnitRequest request = new DeleteUnitRequest
    {
        UnitName = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteUnitAsync(request);
    

### DeleteUnitAsync(DeleteUnitRequest, CancellationToken)
    
    
    public virtual Task DeleteUnitAsync(DeleteUnitRequest request, CancellationToken cancellationToken)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUnitRequest request = new DeleteUnitRequest
    {
        UnitName = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteUnitAsync(request);
    

### DeleteUnitAsync(UnitName, CallSettings)
    
    
    public virtual Task DeleteUnitAsync(UnitName name, CallSettings callSettings = null)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitName name = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]");
    // Make the request
    await saasDeploymentsClient.DeleteUnitAsync(name);
    

### DeleteUnitAsync(UnitName, CancellationToken)
    
    
    public virtual Task DeleteUnitAsync(UnitName name, CancellationToken cancellationToken)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitName name = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]");
    // Make the request
    await saasDeploymentsClient.DeleteUnitAsync(name);
    

### DeleteUnitAsync(string, CallSettings)
    
    
    public virtual Task DeleteUnitAsync(string name, CallSettings callSettings = null)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/units/[UNIT]";
    // Make the request
    await saasDeploymentsClient.DeleteUnitAsync(name);
    

### DeleteUnitAsync(string, CancellationToken)
    
    
    public virtual Task DeleteUnitAsync(string name, CancellationToken cancellationToken)

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/units/[UNIT]";
    // Make the request
    await saasDeploymentsClient.DeleteUnitAsync(name);
    

### DeleteUnitKind(DeleteUnitKindRequest, CallSettings)
    
    
    public virtual void DeleteUnitKind(DeleteUnitKindRequest request, CallSettings callSettings = null)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    DeleteUnitKindRequest request = new DeleteUnitKindRequest
    {
        UnitKindName = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    saasDeploymentsClient.DeleteUnitKind(request);
    

### DeleteUnitKind(UnitKindName, CallSettings)
    
    
    public virtual void DeleteUnitKind(UnitKindName name, CallSettings callSettings = null)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitKindName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKindName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitKindName name = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]");
    // Make the request
    saasDeploymentsClient.DeleteUnitKind(name);
    

### DeleteUnitKind(string, CallSettings)
    
    
    public virtual void DeleteUnitKind(string name, CallSettings callSettings = null)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitKinds/[UNITKIND]";
    // Make the request
    saasDeploymentsClient.DeleteUnitKind(name);
    

### DeleteUnitKindAsync(DeleteUnitKindRequest, CallSettings)
    
    
    public virtual Task DeleteUnitKindAsync(DeleteUnitKindRequest request, CallSettings callSettings = null)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUnitKindRequest request = new DeleteUnitKindRequest
    {
        UnitKindName = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteUnitKindAsync(request);
    

### DeleteUnitKindAsync(DeleteUnitKindRequest, CancellationToken)
    
    
    public virtual Task DeleteUnitKindAsync(DeleteUnitKindRequest request, CancellationToken cancellationToken)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUnitKindRequest request = new DeleteUnitKindRequest
    {
        UnitKindName = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteUnitKindAsync(request);
    

### DeleteUnitKindAsync(UnitKindName, CallSettings)
    
    
    public virtual Task DeleteUnitKindAsync(UnitKindName name, CallSettings callSettings = null)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitKindName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKindName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitKindName name = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]");
    // Make the request
    await saasDeploymentsClient.DeleteUnitKindAsync(name);
    

### DeleteUnitKindAsync(UnitKindName, CancellationToken)
    
    
    public virtual Task DeleteUnitKindAsync(UnitKindName name, CancellationToken cancellationToken)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitKindName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKindName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitKindName name = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]");
    // Make the request
    await saasDeploymentsClient.DeleteUnitKindAsync(name);
    

### DeleteUnitKindAsync(string, CallSettings)
    
    
    public virtual Task DeleteUnitKindAsync(string name, CallSettings callSettings = null)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitKinds/[UNITKIND]";
    // Make the request
    await saasDeploymentsClient.DeleteUnitKindAsync(name);
    

### DeleteUnitKindAsync(string, CancellationToken)
    
    
    public virtual Task DeleteUnitKindAsync(string name, CancellationToken cancellationToken)

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitKinds/[UNITKIND]";
    // Make the request
    await saasDeploymentsClient.DeleteUnitKindAsync(name);
    

### DeleteUnitOperation(DeleteUnitOperationRequest, CallSettings)
    
    
    public virtual void DeleteUnitOperation(DeleteUnitOperationRequest request, CallSettings callSettings = null)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    DeleteUnitOperationRequest request = new DeleteUnitOperationRequest
    {
        UnitOperationName = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    saasDeploymentsClient.DeleteUnitOperation(request);
    

### DeleteUnitOperation(UnitOperationName, CallSettings)
    
    
    public virtual void DeleteUnitOperation(UnitOperationName name, CallSettings callSettings = null)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitOperationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperationName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitOperationName name = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
    // Make the request
    saasDeploymentsClient.DeleteUnitOperation(name);
    

### DeleteUnitOperation(string, CallSettings)
    
    
    public virtual void DeleteUnitOperation(string name, CallSettings callSettings = null)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitOperations/[UNITOPERATION]";
    // Make the request
    saasDeploymentsClient.DeleteUnitOperation(name);
    

### DeleteUnitOperationAsync(DeleteUnitOperationRequest, CallSettings)
    
    
    public virtual Task DeleteUnitOperationAsync(DeleteUnitOperationRequest request, CallSettings callSettings = null)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUnitOperationRequest request = new DeleteUnitOperationRequest
    {
        UnitOperationName = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteUnitOperationAsync(request);
    

### DeleteUnitOperationAsync(DeleteUnitOperationRequest, CancellationToken)
    
    
    public virtual Task DeleteUnitOperationAsync(DeleteUnitOperationRequest request, CancellationToken cancellationToken)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.DeleteUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUnitOperationRequest request = new DeleteUnitOperationRequest
    {
        UnitOperationName = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]"),
        Etag = "",
        ValidateOnly = false,
        RequestId = "",
    };
    // Make the request
    await saasDeploymentsClient.DeleteUnitOperationAsync(request);
    

### DeleteUnitOperationAsync(UnitOperationName, CallSettings)
    
    
    public virtual Task DeleteUnitOperationAsync(UnitOperationName name, CallSettings callSettings = null)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitOperationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperationName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitOperationName name = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
    // Make the request
    await saasDeploymentsClient.DeleteUnitOperationAsync(name);
    

### DeleteUnitOperationAsync(UnitOperationName, CancellationToken)
    
    
    public virtual Task DeleteUnitOperationAsync(UnitOperationName name, CancellationToken cancellationToken)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitOperationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperationName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitOperationName name = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
    // Make the request
    await saasDeploymentsClient.DeleteUnitOperationAsync(name);
    

### DeleteUnitOperationAsync(string, CallSettings)
    
    
    public virtual Task DeleteUnitOperationAsync(string name, CallSettings callSettings = null)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitOperations/[UNITOPERATION]";
    // Make the request
    await saasDeploymentsClient.DeleteUnitOperationAsync(name);
    

### DeleteUnitOperationAsync(string, CancellationToken)
    
    
    public virtual Task DeleteUnitOperationAsync(string name, CancellationToken cancellationToken)

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitOperations/[UNITOPERATION]";
    // Make the request
    await saasDeploymentsClient.DeleteUnitOperationAsync(name);
    

### GetRelease(GetReleaseRequest, CallSettings)
    
    
    public virtual Release GetRelease(GetReleaseRequest request, CallSettings callSettings = null)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    GetReleaseRequest request = new GetReleaseRequest
    {
        ReleaseName = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]"),
    };
    // Make the request
    Release response = saasDeploymentsClient.GetRelease(request);
    

### GetRelease(ReleaseName, CallSettings)
    
    
    public virtual Release GetRelease(ReleaseName name, CallSettings callSettings = null)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReleaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ReleaseName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ReleaseName name = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]");
    // Make the request
    Release response = saasDeploymentsClient.GetRelease(name);
    

### GetRelease(string, CallSettings)
    
    
    public virtual Release GetRelease(string name, CallSettings callSettings = null)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/releases/[RELEASE]";
    // Make the request
    Release response = saasDeploymentsClient.GetRelease(name);
    

### GetReleaseAsync(GetReleaseRequest, CallSettings)
    
    
    public virtual Task<Release> GetReleaseAsync(GetReleaseRequest request, CallSettings callSettings = null)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetReleaseRequest request = new GetReleaseRequest
    {
        ReleaseName = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]"),
    };
    // Make the request
    Release response = await saasDeploymentsClient.GetReleaseAsync(request);
    

### GetReleaseAsync(GetReleaseRequest, CancellationToken)
    
    
    public virtual Task<Release> GetReleaseAsync(GetReleaseRequest request, CancellationToken cancellationToken)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetReleaseRequest request = new GetReleaseRequest
    {
        ReleaseName = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]"),
    };
    // Make the request
    Release response = await saasDeploymentsClient.GetReleaseAsync(request);
    

### GetReleaseAsync(ReleaseName, CallSettings)
    
    
    public virtual Task<Release> GetReleaseAsync(ReleaseName name, CallSettings callSettings = null)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReleaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ReleaseName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ReleaseName name = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]");
    // Make the request
    Release response = await saasDeploymentsClient.GetReleaseAsync(name);
    

### GetReleaseAsync(ReleaseName, CancellationToken)
    
    
    public virtual Task<Release> GetReleaseAsync(ReleaseName name, CancellationToken cancellationToken)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReleaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ReleaseName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ReleaseName name = ReleaseName.FromProjectLocationRelease("[PROJECT]", "[LOCATION]", "[RELEASE]");
    // Make the request
    Release response = await saasDeploymentsClient.GetReleaseAsync(name);
    

### GetReleaseAsync(string, CallSettings)
    
    
    public virtual Task<Release> GetReleaseAsync(string name, CallSettings callSettings = null)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/releases/[RELEASE]";
    // Make the request
    Release response = await saasDeploymentsClient.GetReleaseAsync(name);
    

### GetReleaseAsync(string, CancellationToken)
    
    
    public virtual Task<Release> GetReleaseAsync(string name, CancellationToken cancellationToken)

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/releases/[RELEASE]";
    // Make the request
    Release response = await saasDeploymentsClient.GetReleaseAsync(name);
    

### GetSaas(GetSaasRequest, CallSettings)
    
    
    public virtual Saas GetSaas(GetSaasRequest request, CallSettings callSettings = null)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    GetSaasRequest request = new GetSaasRequest
    {
        SaasName = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]"),
    };
    // Make the request
    Saas response = saasDeploymentsClient.GetSaas(request);
    

### GetSaas(SaasName, CallSettings)
    
    
    public virtual Saas GetSaas(SaasName name, CallSettings callSettings = null)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SaasName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    SaasName name = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]");
    // Make the request
    Saas response = saasDeploymentsClient.GetSaas(name);
    

### GetSaas(string, CallSettings)
    
    
    public virtual Saas GetSaas(string name, CallSettings callSettings = null)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/saas/[SAAS]";
    // Make the request
    Saas response = saasDeploymentsClient.GetSaas(name);
    

### GetSaasAsync(GetSaasRequest, CallSettings)
    
    
    public virtual Task<Saas> GetSaasAsync(GetSaasRequest request, CallSettings callSettings = null)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetSaasRequest request = new GetSaasRequest
    {
        SaasName = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]"),
    };
    // Make the request
    Saas response = await saasDeploymentsClient.GetSaasAsync(request);
    

### GetSaasAsync(GetSaasRequest, CancellationToken)
    
    
    public virtual Task<Saas> GetSaasAsync(GetSaasRequest request, CancellationToken cancellationToken)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetSaasRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetSaasRequest request = new GetSaasRequest
    {
        SaasName = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]"),
    };
    // Make the request
    Saas response = await saasDeploymentsClient.GetSaasAsync(request);
    

### GetSaasAsync(SaasName, CallSettings)
    
    
    public virtual Task<Saas> GetSaasAsync(SaasName name, CallSettings callSettings = null)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SaasName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    SaasName name = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]");
    // Make the request
    Saas response = await saasDeploymentsClient.GetSaasAsync(name);
    

### GetSaasAsync(SaasName, CancellationToken)
    
    
    public virtual Task<Saas> GetSaasAsync(SaasName name, CancellationToken cancellationToken)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SaasName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    SaasName name = SaasName.FromProjectLocationSaas("[PROJECT]", "[LOCATION]", "[SAAS]");
    // Make the request
    Saas response = await saasDeploymentsClient.GetSaasAsync(name);
    

### GetSaasAsync(string, CallSettings)
    
    
    public virtual Task<Saas> GetSaasAsync(string name, CallSettings callSettings = null)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/saas/[SAAS]";
    // Make the request
    Saas response = await saasDeploymentsClient.GetSaasAsync(name);
    

### GetSaasAsync(string, CancellationToken)
    
    
    public virtual Task<Saas> GetSaasAsync(string name, CancellationToken cancellationToken)

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/saas/[SAAS]";
    // Make the request
    Saas response = await saasDeploymentsClient.GetSaasAsync(name);
    

### GetTenant(GetTenantRequest, CallSettings)
    
    
    public virtual Tenant GetTenant(GetTenantRequest request, CallSettings callSettings = null)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    GetTenantRequest request = new GetTenantRequest
    {
        TenantName = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]"),
    };
    // Make the request
    Tenant response = saasDeploymentsClient.GetTenant(request);
    

### GetTenant(TenantName, CallSettings)
    
    
    public virtual Tenant GetTenant(TenantName name, CallSettings callSettings = null)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    TenantName name = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]");
    // Make the request
    Tenant response = saasDeploymentsClient.GetTenant(name);
    

### GetTenant(string, CallSettings)
    
    
    public virtual Tenant GetTenant(string name, CallSettings callSettings = null)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/tenants/[TENANT]";
    // Make the request
    Tenant response = saasDeploymentsClient.GetTenant(name);
    

### GetTenantAsync(GetTenantRequest, CallSettings)
    
    
    public virtual Task<Tenant> GetTenantAsync(GetTenantRequest request, CallSettings callSettings = null)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetTenantRequest request = new GetTenantRequest
    {
        TenantName = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]"),
    };
    // Make the request
    Tenant response = await saasDeploymentsClient.GetTenantAsync(request);
    

### GetTenantAsync(GetTenantRequest, CancellationToken)
    
    
    public virtual Task<Tenant> GetTenantAsync(GetTenantRequest request, CancellationToken cancellationToken)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetTenantRequest request = new GetTenantRequest
    {
        TenantName = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]"),
    };
    // Make the request
    Tenant response = await saasDeploymentsClient.GetTenantAsync(request);
    

### GetTenantAsync(TenantName, CallSettings)
    
    
    public virtual Task<Tenant> GetTenantAsync(TenantName name, CallSettings callSettings = null)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    TenantName name = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]");
    // Make the request
    Tenant response = await saasDeploymentsClient.GetTenantAsync(name);
    

### GetTenantAsync(TenantName, CancellationToken)
    
    
    public virtual Task<Tenant> GetTenantAsync(TenantName name, CancellationToken cancellationToken)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    TenantName name = TenantName.FromProjectLocationTenant("[PROJECT]", "[LOCATION]", "[TENANT]");
    // Make the request
    Tenant response = await saasDeploymentsClient.GetTenantAsync(name);
    

### GetTenantAsync(string, CallSettings)
    
    
    public virtual Task<Tenant> GetTenantAsync(string name, CallSettings callSettings = null)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/tenants/[TENANT]";
    // Make the request
    Tenant response = await saasDeploymentsClient.GetTenantAsync(name);
    

### GetTenantAsync(string, CancellationToken)
    
    
    public virtual Task<Tenant> GetTenantAsync(string name, CancellationToken cancellationToken)

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/tenants/[TENANT]";
    // Make the request
    Tenant response = await saasDeploymentsClient.GetTenantAsync(name);
    

### GetUnit(GetUnitRequest, CallSettings)
    
    
    public virtual Unit GetUnit(GetUnitRequest request, CallSettings callSettings = null)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    GetUnitRequest request = new GetUnitRequest
    {
        UnitName = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]"),
    };
    // Make the request
    Unit response = saasDeploymentsClient.GetUnit(request);
    

### GetUnit(UnitName, CallSettings)
    
    
    public virtual Unit GetUnit(UnitName name, CallSettings callSettings = null)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitName name = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]");
    // Make the request
    Unit response = saasDeploymentsClient.GetUnit(name);
    

### GetUnit(string, CallSettings)
    
    
    public virtual Unit GetUnit(string name, CallSettings callSettings = null)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/units/[UNIT]";
    // Make the request
    Unit response = saasDeploymentsClient.GetUnit(name);
    

### GetUnitAsync(GetUnitRequest, CallSettings)
    
    
    public virtual Task<Unit> GetUnitAsync(GetUnitRequest request, CallSettings callSettings = null)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetUnitRequest request = new GetUnitRequest
    {
        UnitName = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]"),
    };
    // Make the request
    Unit response = await saasDeploymentsClient.GetUnitAsync(request);
    

### GetUnitAsync(GetUnitRequest, CancellationToken)
    
    
    public virtual Task<Unit> GetUnitAsync(GetUnitRequest request, CancellationToken cancellationToken)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetUnitRequest request = new GetUnitRequest
    {
        UnitName = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]"),
    };
    // Make the request
    Unit response = await saasDeploymentsClient.GetUnitAsync(request);
    

### GetUnitAsync(UnitName, CallSettings)
    
    
    public virtual Task<Unit> GetUnitAsync(UnitName name, CallSettings callSettings = null)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitName name = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]");
    // Make the request
    Unit response = await saasDeploymentsClient.GetUnitAsync(name);
    

### GetUnitAsync(UnitName, CancellationToken)
    
    
    public virtual Task<Unit> GetUnitAsync(UnitName name, CancellationToken cancellationToken)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitName name = UnitName.FromProjectLocationUnit("[PROJECT]", "[LOCATION]", "[UNIT]");
    // Make the request
    Unit response = await saasDeploymentsClient.GetUnitAsync(name);
    

### GetUnitAsync(string, CallSettings)
    
    
    public virtual Task<Unit> GetUnitAsync(string name, CallSettings callSettings = null)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/units/[UNIT]";
    // Make the request
    Unit response = await saasDeploymentsClient.GetUnitAsync(name);
    

### GetUnitAsync(string, CancellationToken)
    
    
    public virtual Task<Unit> GetUnitAsync(string name, CancellationToken cancellationToken)

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/units/[UNIT]";
    // Make the request
    Unit response = await saasDeploymentsClient.GetUnitAsync(name);
    

### GetUnitKind(GetUnitKindRequest, CallSettings)
    
    
    public virtual UnitKind GetUnitKind(GetUnitKindRequest request, CallSettings callSettings = null)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    GetUnitKindRequest request = new GetUnitKindRequest
    {
        UnitKindName = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]"),
    };
    // Make the request
    UnitKind response = saasDeploymentsClient.GetUnitKind(request);
    

### GetUnitKind(UnitKindName, CallSettings)
    
    
    public virtual UnitKind GetUnitKind(UnitKindName name, CallSettings callSettings = null)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitKindName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKindName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitKindName name = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]");
    // Make the request
    UnitKind response = saasDeploymentsClient.GetUnitKind(name);
    

### GetUnitKind(string, CallSettings)
    
    
    public virtual UnitKind GetUnitKind(string name, CallSettings callSettings = null)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitKinds/[UNITKIND]";
    // Make the request
    UnitKind response = saasDeploymentsClient.GetUnitKind(name);
    

### GetUnitKindAsync(GetUnitKindRequest, CallSettings)
    
    
    public virtual Task<UnitKind> GetUnitKindAsync(GetUnitKindRequest request, CallSettings callSettings = null)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetUnitKindRequest request = new GetUnitKindRequest
    {
        UnitKindName = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]"),
    };
    // Make the request
    UnitKind response = await saasDeploymentsClient.GetUnitKindAsync(request);
    

### GetUnitKindAsync(GetUnitKindRequest, CancellationToken)
    
    
    public virtual Task<UnitKind> GetUnitKindAsync(GetUnitKindRequest request, CancellationToken cancellationToken)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetUnitKindRequest request = new GetUnitKindRequest
    {
        UnitKindName = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]"),
    };
    // Make the request
    UnitKind response = await saasDeploymentsClient.GetUnitKindAsync(request);
    

### GetUnitKindAsync(UnitKindName, CallSettings)
    
    
    public virtual Task<UnitKind> GetUnitKindAsync(UnitKindName name, CallSettings callSettings = null)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitKindName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKindName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitKindName name = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]");
    // Make the request
    UnitKind response = await saasDeploymentsClient.GetUnitKindAsync(name);
    

### GetUnitKindAsync(UnitKindName, CancellationToken)
    
    
    public virtual Task<UnitKind> GetUnitKindAsync(UnitKindName name, CancellationToken cancellationToken)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitKindName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKindName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitKindName name = UnitKindName.FromProjectLocationUnitKind("[PROJECT]", "[LOCATION]", "[UNITKIND]");
    // Make the request
    UnitKind response = await saasDeploymentsClient.GetUnitKindAsync(name);
    

### GetUnitKindAsync(string, CallSettings)
    
    
    public virtual Task<UnitKind> GetUnitKindAsync(string name, CallSettings callSettings = null)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitKinds/[UNITKIND]";
    // Make the request
    UnitKind response = await saasDeploymentsClient.GetUnitKindAsync(name);
    

### GetUnitKindAsync(string, CancellationToken)
    
    
    public virtual Task<UnitKind> GetUnitKindAsync(string name, CancellationToken cancellationToken)

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitKinds/[UNITKIND]";
    // Make the request
    UnitKind response = await saasDeploymentsClient.GetUnitKindAsync(name);
    

### GetUnitOperation(GetUnitOperationRequest, CallSettings)
    
    
    public virtual UnitOperation GetUnitOperation(GetUnitOperationRequest request, CallSettings callSettings = null)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    GetUnitOperationRequest request = new GetUnitOperationRequest
    {
        UnitOperationName = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]"),
    };
    // Make the request
    UnitOperation response = saasDeploymentsClient.GetUnitOperation(request);
    

### GetUnitOperation(UnitOperationName, CallSettings)
    
    
    public virtual UnitOperation GetUnitOperation(UnitOperationName name, CallSettings callSettings = null)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitOperationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperationName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitOperationName name = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
    // Make the request
    UnitOperation response = saasDeploymentsClient.GetUnitOperation(name);
    

### GetUnitOperation(string, CallSettings)
    
    
    public virtual UnitOperation GetUnitOperation(string name, CallSettings callSettings = null)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitOperations/[UNITOPERATION]";
    // Make the request
    UnitOperation response = saasDeploymentsClient.GetUnitOperation(name);
    

### GetUnitOperationAsync(GetUnitOperationRequest, CallSettings)
    
    
    public virtual Task<UnitOperation> GetUnitOperationAsync(GetUnitOperationRequest request, CallSettings callSettings = null)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetUnitOperationRequest request = new GetUnitOperationRequest
    {
        UnitOperationName = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]"),
    };
    // Make the request
    UnitOperation response = await saasDeploymentsClient.GetUnitOperationAsync(request);
    

### GetUnitOperationAsync(GetUnitOperationRequest, CancellationToken)
    
    
    public virtual Task<UnitOperation> GetUnitOperationAsync(GetUnitOperationRequest request, CancellationToken cancellationToken)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    GetUnitOperationRequest request = new GetUnitOperationRequest
    {
        UnitOperationName = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]"),
    };
    // Make the request
    UnitOperation response = await saasDeploymentsClient.GetUnitOperationAsync(request);
    

### GetUnitOperationAsync(UnitOperationName, CallSettings)
    
    
    public virtual Task<UnitOperation> GetUnitOperationAsync(UnitOperationName name, CallSettings callSettings = null)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitOperationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperationName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitOperationName name = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
    // Make the request
    UnitOperation response = await saasDeploymentsClient.GetUnitOperationAsync(name);
    

### GetUnitOperationAsync(UnitOperationName, CancellationToken)
    
    
    public virtual Task<UnitOperation> GetUnitOperationAsync(UnitOperationName name, CancellationToken cancellationToken)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UnitOperationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperationName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitOperationName name = UnitOperationName.FromProjectLocationUnitOperation("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
    // Make the request
    UnitOperation response = await saasDeploymentsClient.GetUnitOperationAsync(name);
    

### GetUnitOperationAsync(string, CallSettings)
    
    
    public virtual Task<UnitOperation> GetUnitOperationAsync(string name, CallSettings callSettings = null)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitOperations/[UNITOPERATION]";
    // Make the request
    UnitOperation response = await saasDeploymentsClient.GetUnitOperationAsync(name);
    

### GetUnitOperationAsync(string, CancellationToken)
    
    
    public virtual Task<UnitOperation> GetUnitOperationAsync(string name, CancellationToken cancellationToken)

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/unitOperations/[UNITOPERATION]";
    // Make the request
    UnitOperation response = await saasDeploymentsClient.GetUnitOperationAsync(name);
    

### ListReleases(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListReleasesResponse, Release> ListReleases(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of releases.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the release.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesResponse)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A pageable sequence of [Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListReleasesResponse, Release> response = saasDeploymentsClient.ListReleases(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Release item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReleasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Release item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Release> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Release item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReleases(ListReleasesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListReleasesResponse, Release> ListReleases(ListReleasesRequest request, CallSettings callSettings = null)

Retrieve a collection of releases.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesResponse)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A pageable sequence of [Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ListReleasesRequest request = new ListReleasesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListReleasesResponse, Release> response = saasDeploymentsClient.ListReleases(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Release item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReleasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Release item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Release> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Release item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReleases(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListReleasesResponse, Release> ListReleases(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of releases.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the release.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesResponse)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A pageable sequence of [Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListReleasesResponse, Release> response = saasDeploymentsClient.ListReleases(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Release item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReleasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Release item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Release> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Release item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReleasesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReleasesResponse, Release> ListReleasesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of releases.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the release.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesResponse)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A pageable asynchronous sequence of [Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListReleasesResponse, Release> response = saasDeploymentsClient.ListReleasesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Release item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReleasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Release item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Release> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Release item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReleasesAsync(ListReleasesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReleasesResponse, Release> ListReleasesAsync(ListReleasesRequest request, CallSettings callSettings = null)

Retrieve a collection of releases.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesResponse)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A pageable asynchronous sequence of [Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ListReleasesRequest request = new ListReleasesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListReleasesResponse, Release> response = saasDeploymentsClient.ListReleasesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Release item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReleasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Release item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Release> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Release item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReleasesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReleasesResponse, Release> ListReleasesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of releases.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the release.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListReleasesResponse)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A pageable asynchronous sequence of [Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListReleasesResponse, Release> response = saasDeploymentsClient.ListReleasesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Release item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReleasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Release item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Release> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Release item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSaas(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSaasResponse, Saas> ListSaas(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the saas.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSaasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasResponse)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A pageable sequence of [Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListSaasResponse, Saas> response = saasDeploymentsClient.ListSaas(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Saas item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSaasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Saas item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Saas> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Saas item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSaas(ListSaasRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListSaasResponse, Saas> ListSaas(ListSaasRequest request, CallSettings callSettings = null)

Retrieve a collection of saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSaasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasResponse)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A pageable sequence of [Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ListSaasRequest request = new ListSaasRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListSaasResponse, Saas> response = saasDeploymentsClient.ListSaas(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Saas item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSaasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Saas item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Saas> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Saas item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSaas(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSaasResponse, Saas> ListSaas(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the saas.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSaasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasResponse)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A pageable sequence of [Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListSaasResponse, Saas> response = saasDeploymentsClient.ListSaas(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Saas item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSaasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Saas item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Saas> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Saas item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSaasAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSaasResponse, Saas> ListSaasAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the saas.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSaasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasResponse)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A pageable asynchronous sequence of [Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListSaasResponse, Saas> response = saasDeploymentsClient.ListSaasAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Saas item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSaasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Saas item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Saas> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Saas item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSaasAsync(ListSaasRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSaasResponse, Saas> ListSaasAsync(ListSaasRequest request, CallSettings callSettings = null)

Retrieve a collection of saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSaasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasResponse)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A pageable asynchronous sequence of [Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ListSaasRequest request = new ListSaasRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListSaasResponse, Saas> response = saasDeploymentsClient.ListSaasAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Saas item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSaasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Saas item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Saas> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Saas item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSaasAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSaasResponse, Saas> ListSaasAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of saas.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the saas.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSaasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListSaasResponse)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A pageable asynchronous sequence of [Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListSaasResponse, Saas> response = saasDeploymentsClient.ListSaasAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Saas item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSaasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Saas item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Saas> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Saas item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTenants(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTenantsResponse, Tenant> ListTenants(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of tenants.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the tenant.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTenantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsResponse)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A pageable sequence of [Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListTenantsResponse, Tenant> response = saasDeploymentsClient.ListTenants(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Tenant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTenantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tenant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tenant> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tenant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTenants(ListTenantsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListTenantsResponse, Tenant> ListTenants(ListTenantsRequest request, CallSettings callSettings = null)

Retrieve a collection of tenants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTenantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTenantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsResponse)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A pageable sequence of [Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ListTenantsRequest request = new ListTenantsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListTenantsResponse, Tenant> response = saasDeploymentsClient.ListTenants(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Tenant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTenantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tenant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tenant> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tenant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTenants(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTenantsResponse, Tenant> ListTenants(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of tenants.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the tenant.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTenantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsResponse)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A pageable sequence of [Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListTenantsResponse, Tenant> response = saasDeploymentsClient.ListTenants(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Tenant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTenantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tenant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tenant> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tenant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTenantsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTenantsResponse, Tenant> ListTenantsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of tenants.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the tenant.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTenantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsResponse)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A pageable asynchronous sequence of [Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListTenantsResponse, Tenant> response = saasDeploymentsClient.ListTenantsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Tenant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListTenantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tenant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tenant> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tenant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTenantsAsync(ListTenantsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTenantsResponse, Tenant> ListTenantsAsync(ListTenantsRequest request, CallSettings callSettings = null)

Retrieve a collection of tenants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTenantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTenantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsResponse)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A pageable asynchronous sequence of [Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ListTenantsRequest request = new ListTenantsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListTenantsResponse, Tenant> response = saasDeploymentsClient.ListTenantsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Tenant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListTenantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tenant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tenant> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tenant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTenantsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTenantsResponse, Tenant> ListTenantsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of tenants.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the tenant.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTenantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListTenantsResponse)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A pageable asynchronous sequence of [Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListTenantsResponse, Tenant> response = saasDeploymentsClient.ListTenantsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Tenant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListTenantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tenant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tenant> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tenant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitKinds(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitKindsResponse, UnitKind> ListUnitKinds(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit kinds.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit kind.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitKindsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsResponse)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A pageable sequence of [UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListUnitKindsResponse, UnitKind> response = saasDeploymentsClient.ListUnitKinds(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (UnitKind item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitKindsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitKind item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitKind> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitKind item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitKinds(ListUnitKindsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitKindsResponse, UnitKind> ListUnitKinds(ListUnitKindsRequest request, CallSettings callSettings = null)

Retrieve a collection of unit kinds.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUnitKindsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitKindsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsResponse)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A pageable sequence of [UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ListUnitKindsRequest request = new ListUnitKindsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListUnitKindsResponse, UnitKind> response = saasDeploymentsClient.ListUnitKinds(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (UnitKind item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitKindsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitKind item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitKind> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitKind item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitKinds(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitKindsResponse, UnitKind> ListUnitKinds(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit kinds.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit kind.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitKindsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsResponse)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A pageable sequence of [UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListUnitKindsResponse, UnitKind> response = saasDeploymentsClient.ListUnitKinds(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (UnitKind item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitKindsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitKind item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitKind> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitKind item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitKindsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitKindsResponse, UnitKind> ListUnitKindsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit kinds.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit kind.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitKindsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsResponse)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A pageable asynchronous sequence of [UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListUnitKindsResponse, UnitKind> response = saasDeploymentsClient.ListUnitKindsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (UnitKind item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitKindsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitKind item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitKind> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitKind item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitKindsAsync(ListUnitKindsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitKindsResponse, UnitKind> ListUnitKindsAsync(ListUnitKindsRequest request, CallSettings callSettings = null)

Retrieve a collection of unit kinds.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUnitKindsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitKindsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsResponse)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A pageable asynchronous sequence of [UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ListUnitKindsRequest request = new ListUnitKindsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListUnitKindsResponse, UnitKind> response = saasDeploymentsClient.ListUnitKindsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (UnitKind item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitKindsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitKind item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitKind> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitKind item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitKindsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitKindsResponse, UnitKind> ListUnitKindsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit kinds.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit kind.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitKindsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsResponse)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A pageable asynchronous sequence of [UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListUnitKindsResponse, UnitKind> response = saasDeploymentsClient.ListUnitKindsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (UnitKind item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitKindsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitKind item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitKind> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitKind item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitOperations(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitOperationsResponse, UnitOperation> ListUnitOperations(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit operations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit operation.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsResponse)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A pageable sequence of [UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListUnitOperationsResponse, UnitOperation> response = saasDeploymentsClient.ListUnitOperations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (UnitOperation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitOperationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitOperation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitOperation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitOperation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitOperations(ListUnitOperationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitOperationsResponse, UnitOperation> ListUnitOperations(ListUnitOperationsRequest request, CallSettings callSettings = null)

Retrieve a collection of unit operations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUnitOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsResponse)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A pageable sequence of [UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ListUnitOperationsRequest request = new ListUnitOperationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListUnitOperationsResponse, UnitOperation> response = saasDeploymentsClient.ListUnitOperations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (UnitOperation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitOperationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitOperation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitOperation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitOperation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitOperations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitOperationsResponse, UnitOperation> ListUnitOperations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit operations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit operation.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsResponse)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A pageable sequence of [UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListUnitOperationsResponse, UnitOperation> response = saasDeploymentsClient.ListUnitOperations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (UnitOperation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitOperationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitOperation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitOperation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitOperation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitOperationsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitOperationsResponse, UnitOperation> ListUnitOperationsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit operations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit operation.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsResponse)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A pageable asynchronous sequence of [UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListUnitOperationsResponse, UnitOperation> response = saasDeploymentsClient.ListUnitOperationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (UnitOperation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitOperationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitOperation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitOperation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitOperation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitOperationsAsync(ListUnitOperationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitOperationsResponse, UnitOperation> ListUnitOperationsAsync(ListUnitOperationsRequest request, CallSettings callSettings = null)

Retrieve a collection of unit operations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUnitOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsResponse)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A pageable asynchronous sequence of [UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ListUnitOperationsRequest request = new ListUnitOperationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListUnitOperationsResponse, UnitOperation> response = saasDeploymentsClient.ListUnitOperationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (UnitOperation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitOperationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitOperation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitOperation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitOperation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitOperationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitOperationsResponse, UnitOperation> ListUnitOperationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of unit operations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit operation.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitOperationsResponse)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A pageable asynchronous sequence of [UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListUnitOperationsResponse, UnitOperation> response = saasDeploymentsClient.ListUnitOperationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (UnitOperation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitOperationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (UnitOperation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<UnitOperation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (UnitOperation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnits(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitsResponse, Unit> ListUnits(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of units.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsResponse)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A pageable sequence of [Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListUnitsResponse, Unit> response = saasDeploymentsClient.ListUnits(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Unit item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Unit item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Unit> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Unit item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnits(ListUnitsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitsResponse, Unit> ListUnits(ListUnitsRequest request, CallSettings callSettings = null)

Retrieve a collection of units.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUnitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsResponse)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A pageable sequence of [Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    ListUnitsRequest request = new ListUnitsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListUnitsResponse, Unit> response = saasDeploymentsClient.ListUnits(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Unit item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Unit item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Unit> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Unit item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnits(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUnitsResponse, Unit> ListUnits(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of units.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUnitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsResponse)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A pageable sequence of [Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListUnitsResponse, Unit> response = saasDeploymentsClient.ListUnits(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Unit item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUnitsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Unit item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Unit> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Unit item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitsResponse, Unit> ListUnitsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of units.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the unit.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsResponse)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A pageable asynchronous sequence of [Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListUnitsResponse, Unit> response = saasDeploymentsClient.ListUnitsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Unit item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Unit item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Unit> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Unit item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitsAsync(ListUnitsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitsResponse, Unit> ListUnitsAsync(ListUnitsRequest request, CallSettings callSettings = null)

Retrieve a collection of units.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUnitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsResponse)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A pageable asynchronous sequence of [Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    ListUnitsRequest request = new ListUnitsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListUnitsResponse, Unit> response = saasDeploymentsClient.ListUnitsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Unit item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Unit item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Unit> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Unit item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUnitsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUnitsResponse, Unit> ListUnitsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of units.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the unit.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUnitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitsResponse)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A pageable asynchronous sequence of [Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit) resources.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListUnitsResponse, Unit> response = saasDeploymentsClient.ListUnitsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Unit item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUnitsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Unit item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Unit> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Unit item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient#Google_Cloud_SaasPlatform_SaasServiceMgmt_V1Beta1_SaasDeploymentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient#Google_Cloud_SaasPlatform_SaasServiceMgmt_V1Beta1_SaasDeploymentsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient#Google_Cloud_SaasPlatform_SaasServiceMgmt_V1Beta1_SaasDeploymentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.SaasDeploymentsClient#Google_Cloud_SaasPlatform_SaasServiceMgmt_V1Beta1_SaasDeploymentsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateRelease(Release, FieldMask, CallSettings)
    
    
    public virtual Release UpdateRelease(Release release, FieldMask updateMask, CallSettings callSettings = null)

Update a single release.

**Parameters**  
---  
**Name** | **Description**  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Release resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Release will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    Release release = new Release();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Release response = saasDeploymentsClient.UpdateRelease(release, updateMask);
    

### UpdateRelease(UpdateReleaseRequest, CallSettings)
    
    
    public virtual Release UpdateRelease(UpdateReleaseRequest request, CallSettings callSettings = null)

Update a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UpdateReleaseRequest request = new UpdateReleaseRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Release = new Release(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Release response = saasDeploymentsClient.UpdateRelease(request);
    

### UpdateReleaseAsync(Release, FieldMask, CallSettings)
    
    
    public virtual Task<Release> UpdateReleaseAsync(Release release, FieldMask updateMask, CallSettings callSettings = null)

Update a single release.

**Parameters**  
---  
**Name** | **Description**  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Release resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Release will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Release release = new Release();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Release response = await saasDeploymentsClient.UpdateReleaseAsync(release, updateMask);
    

### UpdateReleaseAsync(Release, FieldMask, CancellationToken)
    
    
    public virtual Task<Release> UpdateReleaseAsync(Release release, FieldMask updateMask, CancellationToken cancellationToken)

Update a single release.

**Parameters**  
---  
**Name** | **Description**  
`release` | `[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)`  
Required. The desired state for the release.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Release resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Release will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Release release = new Release();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Release response = await saasDeploymentsClient.UpdateReleaseAsync(release, updateMask);
    

### UpdateReleaseAsync(UpdateReleaseRequest, CallSettings)
    
    
    public virtual Task<Release> UpdateReleaseAsync(UpdateReleaseRequest request, CallSettings callSettings = null)

Update a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateReleaseRequest request = new UpdateReleaseRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Release = new Release(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Release response = await saasDeploymentsClient.UpdateReleaseAsync(request);
    

### UpdateReleaseAsync(UpdateReleaseRequest, CancellationToken)
    
    
    public virtual Task<Release> UpdateReleaseAsync(UpdateReleaseRequest request, CancellationToken cancellationToken)

Update a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Release)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateReleaseRequest request = new UpdateReleaseRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Release = new Release(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Release response = await saasDeploymentsClient.UpdateReleaseAsync(request);
    

### UpdateSaas(Saas, FieldMask, CallSettings)
    
    
    public virtual Saas UpdateSaas(Saas saas, FieldMask updateMask, CallSettings callSettings = null)

Update a single saas.

**Parameters**  
---  
**Name** | **Description**  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Saas resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Saas will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    Saas saas = new Saas();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Saas response = saasDeploymentsClient.UpdateSaas(saas, updateMask);
    

### UpdateSaas(UpdateSaasRequest, CallSettings)
    
    
    public virtual Saas UpdateSaas(UpdateSaasRequest request, CallSettings callSettings = null)

Update a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UpdateSaasRequest request = new UpdateSaasRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Saas = new Saas(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Saas response = saasDeploymentsClient.UpdateSaas(request);
    

### UpdateSaasAsync(Saas, FieldMask, CallSettings)
    
    
    public virtual Task<Saas> UpdateSaasAsync(Saas saas, FieldMask updateMask, CallSettings callSettings = null)

Update a single saas.

**Parameters**  
---  
**Name** | **Description**  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Saas resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Saas will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Saas saas = new Saas();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Saas response = await saasDeploymentsClient.UpdateSaasAsync(saas, updateMask);
    

### UpdateSaasAsync(Saas, FieldMask, CancellationToken)
    
    
    public virtual Task<Saas> UpdateSaasAsync(Saas saas, FieldMask updateMask, CancellationToken cancellationToken)

Update a single saas.

**Parameters**  
---  
**Name** | **Description**  
`saas` | `[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)`  
Required. The desired state for the saas.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Saas resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Saas will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Saas saas = new Saas();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Saas response = await saasDeploymentsClient.UpdateSaasAsync(saas, updateMask);
    

### UpdateSaasAsync(UpdateSaasRequest, CallSettings)
    
    
    public virtual Task<Saas> UpdateSaasAsync(UpdateSaasRequest request, CallSettings callSettings = null)

Update a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateSaasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSaasRequest request = new UpdateSaasRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Saas = new Saas(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Saas response = await saasDeploymentsClient.UpdateSaasAsync(request);
    

### UpdateSaasAsync(UpdateSaasRequest, CancellationToken)
    
    
    public virtual Task<Saas> UpdateSaasAsync(UpdateSaasRequest request, CancellationToken cancellationToken)

Update a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSaasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateSaasRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Saas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Saas)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSaasRequest request = new UpdateSaasRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Saas = new Saas(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Saas response = await saasDeploymentsClient.UpdateSaasAsync(request);
    

### UpdateTenant(Tenant, FieldMask, CallSettings)
    
    
    public virtual Tenant UpdateTenant(Tenant tenant, FieldMask updateMask, CallSettings callSettings = null)

Update a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Tenant resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Tenant will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    Tenant tenant = new Tenant();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Tenant response = saasDeploymentsClient.UpdateTenant(tenant, updateMask);
    

### UpdateTenant(UpdateTenantRequest, CallSettings)
    
    
    public virtual Tenant UpdateTenant(UpdateTenantRequest request, CallSettings callSettings = null)

Update a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UpdateTenantRequest request = new UpdateTenantRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Tenant = new Tenant(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Tenant response = saasDeploymentsClient.UpdateTenant(request);
    

### UpdateTenantAsync(Tenant, FieldMask, CallSettings)
    
    
    public virtual Task<Tenant> UpdateTenantAsync(Tenant tenant, FieldMask updateMask, CallSettings callSettings = null)

Update a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Tenant resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Tenant will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Tenant tenant = new Tenant();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Tenant response = await saasDeploymentsClient.UpdateTenantAsync(tenant, updateMask);
    

### UpdateTenantAsync(Tenant, FieldMask, CancellationToken)
    
    
    public virtual Task<Tenant> UpdateTenantAsync(Tenant tenant, FieldMask updateMask, CancellationToken cancellationToken)

Update a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`tenant` | `[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)`  
Required. The desired state for the tenant.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Tenant resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Tenant will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Tenant tenant = new Tenant();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Tenant response = await saasDeploymentsClient.UpdateTenantAsync(tenant, updateMask);
    

### UpdateTenantAsync(UpdateTenantRequest, CallSettings)
    
    
    public virtual Task<Tenant> UpdateTenantAsync(UpdateTenantRequest request, CallSettings callSettings = null)

Update a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateTenantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateTenantRequest request = new UpdateTenantRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Tenant = new Tenant(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Tenant response = await saasDeploymentsClient.UpdateTenantAsync(request);
    

### UpdateTenantAsync(UpdateTenantRequest, CancellationToken)
    
    
    public virtual Task<Tenant> UpdateTenantAsync(UpdateTenantRequest request, CancellationToken cancellationToken)

Update a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateTenantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tenant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Tenant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateTenantRequest request = new UpdateTenantRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Tenant = new Tenant(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Tenant response = await saasDeploymentsClient.UpdateTenantAsync(request);
    

### UpdateUnit(Unit, FieldMask, CallSettings)
    
    
    public virtual Unit UpdateUnit(Unit unit, FieldMask updateMask, CallSettings callSettings = null)

Update a single unit.

**Parameters**  
---  
**Name** | **Description**  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Unit resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Unit will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    Unit unit = new Unit();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Unit response = saasDeploymentsClient.UpdateUnit(unit, updateMask);
    

### UpdateUnit(UpdateUnitRequest, CallSettings)
    
    
    public virtual Unit UpdateUnit(UpdateUnitRequest request, CallSettings callSettings = null)

Update a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UpdateUnitRequest request = new UpdateUnitRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Unit = new Unit(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Unit response = saasDeploymentsClient.UpdateUnit(request);
    

### UpdateUnitAsync(Unit, FieldMask, CallSettings)
    
    
    public virtual Task<Unit> UpdateUnitAsync(Unit unit, FieldMask updateMask, CallSettings callSettings = null)

Update a single unit.

**Parameters**  
---  
**Name** | **Description**  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Unit resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Unit will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Unit unit = new Unit();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Unit response = await saasDeploymentsClient.UpdateUnitAsync(unit, updateMask);
    

### UpdateUnitAsync(Unit, FieldMask, CancellationToken)
    
    
    public virtual Task<Unit> UpdateUnitAsync(Unit unit, FieldMask updateMask, CancellationToken cancellationToken)

Update a single unit.

**Parameters**  
---  
**Name** | **Description**  
`unit` | `[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)`  
Required. The desired state for the unit.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Unit resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Unit will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    Unit unit = new Unit();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Unit response = await saasDeploymentsClient.UpdateUnitAsync(unit, updateMask);
    

### UpdateUnitAsync(UpdateUnitRequest, CallSettings)
    
    
    public virtual Task<Unit> UpdateUnitAsync(UpdateUnitRequest request, CallSettings callSettings = null)

Update a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUnitRequest request = new UpdateUnitRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Unit = new Unit(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Unit response = await saasDeploymentsClient.UpdateUnitAsync(request);
    

### UpdateUnitAsync(UpdateUnitRequest, CancellationToken)
    
    
    public virtual Task<Unit> UpdateUnitAsync(UpdateUnitRequest request, CancellationToken cancellationToken)

Update a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUnitRequest request = new UpdateUnitRequest
    {
        ValidateOnly = false,
        RequestId = "",
        Unit = new Unit(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Unit response = await saasDeploymentsClient.UpdateUnitAsync(request);
    

### UpdateUnitKind(UnitKind, FieldMask, CallSettings)
    
    
    public virtual UnitKind UpdateUnitKind(UnitKind unitKind, FieldMask updateMask, CallSettings callSettings = null)

Update a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitKind resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitKind will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitKind unitKind = new UnitKind();
    FieldMask updateMask = new FieldMask();
    // Make the request
    UnitKind response = saasDeploymentsClient.UpdateUnitKind(unitKind, updateMask);
    

### UpdateUnitKind(UpdateUnitKindRequest, CallSettings)
    
    
    public virtual UnitKind UpdateUnitKind(UpdateUnitKindRequest request, CallSettings callSettings = null)

Update a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UpdateUnitKindRequest request = new UpdateUnitKindRequest
    {
        ValidateOnly = false,
        RequestId = "",
        UnitKind = new UnitKind(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    UnitKind response = saasDeploymentsClient.UpdateUnitKind(request);
    

### UpdateUnitKindAsync(UnitKind, FieldMask, CallSettings)
    
    
    public virtual Task<UnitKind> UpdateUnitKindAsync(UnitKind unitKind, FieldMask updateMask, CallSettings callSettings = null)

Update a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitKind resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitKind will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitKind unitKind = new UnitKind();
    FieldMask updateMask = new FieldMask();
    // Make the request
    UnitKind response = await saasDeploymentsClient.UpdateUnitKindAsync(unitKind, updateMask);
    

### UpdateUnitKindAsync(UnitKind, FieldMask, CancellationToken)
    
    
    public virtual Task<UnitKind> UpdateUnitKindAsync(UnitKind unitKind, FieldMask updateMask, CancellationToken cancellationToken)

Update a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitKind resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitKind will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitKind unitKind = new UnitKind();
    FieldMask updateMask = new FieldMask();
    // Make the request
    UnitKind response = await saasDeploymentsClient.UpdateUnitKindAsync(unitKind, updateMask);
    

### UpdateUnitKindAsync(UpdateUnitKindRequest, CallSettings)
    
    
    public virtual Task<UnitKind> UpdateUnitKindAsync(UpdateUnitKindRequest request, CallSettings callSettings = null)

Update a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUnitKindRequest request = new UpdateUnitKindRequest
    {
        ValidateOnly = false,
        RequestId = "",
        UnitKind = new UnitKind(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    UnitKind response = await saasDeploymentsClient.UpdateUnitKindAsync(request);
    

### UpdateUnitKindAsync(UpdateUnitKindRequest, CancellationToken)
    
    
    public virtual Task<UnitKind> UpdateUnitKindAsync(UpdateUnitKindRequest request, CancellationToken cancellationToken)

Update a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitKind)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUnitKindRequest request = new UpdateUnitKindRequest
    {
        ValidateOnly = false,
        RequestId = "",
        UnitKind = new UnitKind(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    UnitKind response = await saasDeploymentsClient.UpdateUnitKindAsync(request);
    

### UpdateUnitOperation(UnitOperation, FieldMask, CallSettings)
    
    
    public virtual UnitOperation UpdateUnitOperation(UnitOperation unitOperation, FieldMask updateMask, CallSettings callSettings = null)

Update a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitOperation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitOperation will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UnitOperation unitOperation = new UnitOperation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    UnitOperation response = saasDeploymentsClient.UpdateUnitOperation(unitOperation, updateMask);
    

### UpdateUnitOperation(UpdateUnitOperationRequest, CallSettings)
    
    
    public virtual UnitOperation UpdateUnitOperation(UpdateUnitOperationRequest request, CallSettings callSettings = null)

Update a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | The RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.Create();
    // Initialize request argument(s)
    UpdateUnitOperationRequest request = new UpdateUnitOperationRequest
    {
        ValidateOnly = false,
        RequestId = "",
        UnitOperation = new UnitOperation(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    UnitOperation response = saasDeploymentsClient.UpdateUnitOperation(request);
    

### UpdateUnitOperationAsync(UnitOperation, FieldMask, CallSettings)
    
    
    public virtual Task<UnitOperation> UpdateUnitOperationAsync(UnitOperation unitOperation, FieldMask updateMask, CallSettings callSettings = null)

Update a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitOperation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitOperation will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitOperation unitOperation = new UnitOperation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    UnitOperation response = await saasDeploymentsClient.UpdateUnitOperationAsync(unitOperation, updateMask);
    

### UpdateUnitOperationAsync(UnitOperation, FieldMask, CancellationToken)
    
    
    public virtual Task<UnitOperation> UpdateUnitOperationAsync(UnitOperation unitOperation, FieldMask updateMask, CancellationToken cancellationToken)

Update a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitOperation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitOperation will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UnitOperation unitOperation = new UnitOperation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    UnitOperation response = await saasDeploymentsClient.UpdateUnitOperationAsync(unitOperation, updateMask);
    

### UpdateUnitOperationAsync(UpdateUnitOperationRequest, CallSettings)
    
    
    public virtual Task<UnitOperation> UpdateUnitOperationAsync(UpdateUnitOperationRequest request, CallSettings callSettings = null)

Update a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUnitOperationRequest request = new UpdateUnitOperationRequest
    {
        ValidateOnly = false,
        RequestId = "",
        UnitOperation = new UnitOperation(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    UnitOperation response = await saasDeploymentsClient.UpdateUnitOperationAsync(request);
    

### UpdateUnitOperationAsync(UpdateUnitOperationRequest, CancellationToken)
    
    
    public virtual Task<UnitOperation> UpdateUnitOperationAsync(UpdateUnitOperationRequest request, CancellationToken cancellationToken)

Update a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UnitOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UnitOperation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SaasDeploymentsClient saasDeploymentsClient = await SaasDeploymentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUnitOperationRequest request = new UpdateUnitOperationRequest
    {
        ValidateOnly = false,
        RequestId = "",
        UnitOperation = new UnitOperation(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    UnitOperation response = await saasDeploymentsClient.UpdateUnitOperationAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
