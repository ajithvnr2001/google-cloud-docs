---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient
title: Google Cloud Key Management Service v1 API - Class AutokeyAdminClient (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:55.051468+00:00
---

# Google Cloud Key Management Service v1 API - Class AutokeyAdminClient (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class AutokeyAdminClient (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public abstract class AutokeyAdminClient

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class AutokeyAdminClient.

AutokeyAdmin client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutokeyAdminClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AutokeyAdminClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClientImpl)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Remarks

Provides interfaces for managing [Cloud KMS Autokey](https://cloud.google.com/kms/help/autokey) folder-level or project-level configurations. A configuration is inherited by all descendent folders and projects. A configuration at a folder or project overrides any other configurations in its ancestry. Setting a configuration on a folder is a prerequisite for Cloud KMS Autokey, so that users working in a descendant project can request provisioned [CryptoKeys][google.cloud.kms.v1.CryptoKey], ready for Customer Managed Encryption Key (CMEK) use, on-demand when using the dedicated key project mode. This is not required when using the delegated key management mode for same-project keys.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AutokeyAdmin service, which is a host of "cloudkms.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AutokeyAdmin scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AutokeyAdmin scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/cloudkms>



### GrpcClient
    
    
    public virtual AutokeyAdmin.AutokeyAdminClient GrpcClient { get; }

The underlying gRPC AutokeyAdmin client

**Property Value**  
---  
**Type** | **Description**  
`[AutokeyAdmin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin)[AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminClient)` |   
  
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
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static AutokeyAdminClient Create()

Synchronously creates a [AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AutokeyAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient)` | The created [AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AutokeyAdminClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AutokeyAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient)` | The task representing the created [AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient).  
  
### GetAutokeyConfig(AutokeyConfigName, CallSettings)
    
    
    public virtual AutokeyConfig GetAutokeyConfig(AutokeyConfigName name, CallSettings callSettings = null)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AutokeyConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfigName)`  
Required. Name of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    AutokeyConfigName name = AutokeyConfigName.FromFolder("[FOLDER]");
    // Make the request
    AutokeyConfig response = autokeyAdminClient.GetAutokeyConfig(name);
    

### GetAutokeyConfig(GetAutokeyConfigRequest, CallSettings)
    
    
    public virtual AutokeyConfig GetAutokeyConfig(GetAutokeyConfigRequest request, CallSettings callSettings = null)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    GetAutokeyConfigRequest request = new GetAutokeyConfigRequest
    {
        AutokeyConfigName = AutokeyConfigName.FromFolder("[FOLDER]"),
    };
    // Make the request
    AutokeyConfig response = autokeyAdminClient.GetAutokeyConfig(request);
    

### GetAutokeyConfig(string, CallSettings)
    
    
    public virtual AutokeyConfig GetAutokeyConfig(string name, CallSettings callSettings = null)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/autokeyConfig";
    // Make the request
    AutokeyConfig response = autokeyAdminClient.GetAutokeyConfig(name);
    

### GetAutokeyConfigAsync(AutokeyConfigName, CallSettings)
    
    
    public virtual Task<AutokeyConfig> GetAutokeyConfigAsync(AutokeyConfigName name, CallSettings callSettings = null)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AutokeyConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfigName)`  
Required. Name of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    AutokeyConfigName name = AutokeyConfigName.FromFolder("[FOLDER]");
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.GetAutokeyConfigAsync(name);
    

### GetAutokeyConfigAsync(AutokeyConfigName, CancellationToken)
    
    
    public virtual Task<AutokeyConfig> GetAutokeyConfigAsync(AutokeyConfigName name, CancellationToken cancellationToken)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AutokeyConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfigName)`  
Required. Name of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    AutokeyConfigName name = AutokeyConfigName.FromFolder("[FOLDER]");
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.GetAutokeyConfigAsync(name);
    

### GetAutokeyConfigAsync(GetAutokeyConfigRequest, CallSettings)
    
    
    public virtual Task<AutokeyConfig> GetAutokeyConfigAsync(GetAutokeyConfigRequest request, CallSettings callSettings = null)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetAutokeyConfigRequest request = new GetAutokeyConfigRequest
    {
        AutokeyConfigName = AutokeyConfigName.FromFolder("[FOLDER]"),
    };
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.GetAutokeyConfigAsync(request);
    

### GetAutokeyConfigAsync(GetAutokeyConfigRequest, CancellationToken)
    
    
    public virtual Task<AutokeyConfig> GetAutokeyConfigAsync(GetAutokeyConfigRequest request, CancellationToken cancellationToken)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetAutokeyConfigRequest request = new GetAutokeyConfigRequest
    {
        AutokeyConfigName = AutokeyConfigName.FromFolder("[FOLDER]"),
    };
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.GetAutokeyConfigAsync(request);
    

### GetAutokeyConfigAsync(string, CallSettings)
    
    
    public virtual Task<AutokeyConfig> GetAutokeyConfigAsync(string name, CallSettings callSettings = null)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/autokeyConfig";
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.GetAutokeyConfigAsync(name);
    

### GetAutokeyConfigAsync(string, CancellationToken)
    
    
    public virtual Task<AutokeyConfig> GetAutokeyConfigAsync(string name, CancellationToken cancellationToken)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/autokeyConfig";
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.GetAutokeyConfigAsync(name);
    

### ShowEffectiveAutokeyConfig(ProjectName, CallSettings)
    
    
    public virtual ShowEffectiveAutokeyConfigResponse ShowEffectiveAutokeyConfig(ProjectName parent, CallSettings callSettings = null)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = autokeyAdminClient.ShowEffectiveAutokeyConfig(parent);
    

### ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest, CallSettings)
    
    
    public virtual ShowEffectiveAutokeyConfigResponse ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest request, CallSettings callSettings = null)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    ShowEffectiveAutokeyConfigRequest request = new ShowEffectiveAutokeyConfigRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = autokeyAdminClient.ShowEffectiveAutokeyConfig(request);
    

### ShowEffectiveAutokeyConfig(string, CallSettings)
    
    
    public virtual ShowEffectiveAutokeyConfigResponse ShowEffectiveAutokeyConfig(string parent, CallSettings callSettings = null)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = autokeyAdminClient.ShowEffectiveAutokeyConfig(parent);
    

### ShowEffectiveAutokeyConfigAsync(ProjectName, CallSettings)
    
    
    public virtual Task<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(ProjectName parent, CallSettings callSettings = null)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = await autokeyAdminClient.ShowEffectiveAutokeyConfigAsync(parent);
    

### ShowEffectiveAutokeyConfigAsync(ProjectName, CancellationToken)
    
    
    public virtual Task<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(ProjectName parent, CancellationToken cancellationToken)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = await autokeyAdminClient.ShowEffectiveAutokeyConfigAsync(parent);
    

### ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest, CallSettings)
    
    
    public virtual Task<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest request, CallSettings callSettings = null)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    ShowEffectiveAutokeyConfigRequest request = new ShowEffectiveAutokeyConfigRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = await autokeyAdminClient.ShowEffectiveAutokeyConfigAsync(request);
    

### ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest, CancellationToken)
    
    
    public virtual Task<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest request, CancellationToken cancellationToken)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    ShowEffectiveAutokeyConfigRequest request = new ShowEffectiveAutokeyConfigRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = await autokeyAdminClient.ShowEffectiveAutokeyConfigAsync(request);
    

### ShowEffectiveAutokeyConfigAsync(string, CallSettings)
    
    
    public virtual Task<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(string parent, CallSettings callSettings = null)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = await autokeyAdminClient.ShowEffectiveAutokeyConfigAsync(parent);
    

### ShowEffectiveAutokeyConfigAsync(string, CancellationToken)
    
    
    public virtual Task<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(string parent, CancellationToken cancellationToken)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    ShowEffectiveAutokeyConfigResponse response = await autokeyAdminClient.ShowEffectiveAutokeyConfigAsync(parent);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient#Google_Cloud_Kms_V1_AutokeyAdminClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient#Google_Cloud_Kms_V1_AutokeyAdminClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient#Google_Cloud_Kms_V1_AutokeyAdminClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient#Google_Cloud_Kms_V1_AutokeyAdminClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateAutokeyConfig(AutokeyConfig, FieldMask, CallSettings)
    
    
    public virtual AutokeyConfig UpdateAutokeyConfig(AutokeyConfig autokeyConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`autokeyConfig` | `[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)`  
Required. [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] with values to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Masks which fields of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] to update, e.g. `keyProject`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    AutokeyConfig autokeyConfig = new AutokeyConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    AutokeyConfig response = autokeyAdminClient.UpdateAutokeyConfig(autokeyConfig, updateMask);
    

### UpdateAutokeyConfig(UpdateAutokeyConfigRequest, CallSettings)
    
    
    public virtual AutokeyConfig UpdateAutokeyConfig(UpdateAutokeyConfigRequest request, CallSettings callSettings = null)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.Create();
    // Initialize request argument(s)
    UpdateAutokeyConfigRequest request = new UpdateAutokeyConfigRequest
    {
        AutokeyConfig = new AutokeyConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    AutokeyConfig response = autokeyAdminClient.UpdateAutokeyConfig(request);
    

### UpdateAutokeyConfigAsync(AutokeyConfig, FieldMask, CallSettings)
    
    
    public virtual Task<AutokeyConfig> UpdateAutokeyConfigAsync(AutokeyConfig autokeyConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`autokeyConfig` | `[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)`  
Required. [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] with values to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Masks which fields of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] to update, e.g. `keyProject`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    AutokeyConfig autokeyConfig = new AutokeyConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.UpdateAutokeyConfigAsync(autokeyConfig, updateMask);
    

### UpdateAutokeyConfigAsync(AutokeyConfig, FieldMask, CancellationToken)
    
    
    public virtual Task<AutokeyConfig> UpdateAutokeyConfigAsync(AutokeyConfig autokeyConfig, FieldMask updateMask, CancellationToken cancellationToken)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`autokeyConfig` | `[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)`  
Required. [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] with values to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Masks which fields of the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] to update, e.g. `keyProject`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    AutokeyConfig autokeyConfig = new AutokeyConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.UpdateAutokeyConfigAsync(autokeyConfig, updateMask);
    

### UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest, CallSettings)
    
    
    public virtual Task<AutokeyConfig> UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest request, CallSettings callSettings = null)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAutokeyConfigRequest request = new UpdateAutokeyConfigRequest
    {
        AutokeyConfig = new AutokeyConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.UpdateAutokeyConfigAsync(request);
    

### UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest, CancellationToken)
    
    
    public virtual Task<AutokeyConfig> UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest request, CancellationToken cancellationToken)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyAdminClient autokeyAdminClient = await AutokeyAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAutokeyConfigRequest request = new UpdateAutokeyConfigRequest
    {
        AutokeyConfig = new AutokeyConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    AutokeyConfig response = await autokeyAdminClient.UpdateAutokeyConfigAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
