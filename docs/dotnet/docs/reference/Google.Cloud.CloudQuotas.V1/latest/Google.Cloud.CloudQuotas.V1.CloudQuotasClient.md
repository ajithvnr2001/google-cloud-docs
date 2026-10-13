---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient
title: Cloud Quotas v1 API - Class CloudQuotasClient (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:21.594677+00:00
---

# Cloud Quotas v1 API - Class CloudQuotasClient (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class CloudQuotasClient (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public abstract class CloudQuotasClient

Reference documentation and code samples for the Cloud Quotas v1 API class CloudQuotasClient.

CloudQuotas client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudQuotasClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CloudQuotasClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClientImpl)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Remarks

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.

  * List/Get the metadata and current status of the quotas for a service.
  * Create/Update quota preferencess that declare the preferred quota values.
  * Check the status of a quota preference request.
  * List/Get pending and historical quota preference.



## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CloudQuotas service, which is a host of "cloudquotas.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CloudQuotas scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CloudQuotas scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual CloudQuotas.CloudQuotasClient GrpcClient { get; }

The underlying gRPC CloudQuotas client

**Property Value**  
---  
**Type** | **Description**  
`[CloudQuotas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas)[CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static CloudQuotasClient Create()

Synchronously creates a [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudQuotasClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient)` | The created [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CloudQuotasClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudQuotasClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient)` | The task representing the created [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient).  
  
### CreateQuotaPreference(CreateQuotaPreferenceRequest, CallSettings)
    
    
    public virtual QuotaPreference CreateQuotaPreference(CreateQuotaPreferenceRequest request, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    CreateQuotaPreferenceRequest request = new CreateQuotaPreferenceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        QuotaPreferenceId = "",
        QuotaPreference = new QuotaPreference(),
        IgnoreSafetyChecks =
        {
            QuotaSafetyCheck.Unspecified,
        },
    };
    // Make the request
    QuotaPreference response = cloudQuotasClient.CreateQuotaPreference(request);
    

### CreateQuotaPreference(LocationName, QuotaPreference, CallSettings)
    
    
    public virtual QuotaPreference CreateQuotaPreference(LocationName parent, QuotaPreference quotaPreference, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    QuotaPreference quotaPreference = new QuotaPreference();
    // Make the request
    QuotaPreference response = cloudQuotasClient.CreateQuotaPreference(parent, quotaPreference);
    

### CreateQuotaPreference(LocationName, QuotaPreference, string, CallSettings)
    
    
    public virtual QuotaPreference CreateQuotaPreference(LocationName parent, QuotaPreference quotaPreference, string quotaPreferenceId, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    QuotaPreference quotaPreference = new QuotaPreference();
    string quotaPreferenceId = "";
    // Make the request
    QuotaPreference response = cloudQuotasClient.CreateQuotaPreference(parent, quotaPreference, quotaPreferenceId);
    

### CreateQuotaPreference(string, QuotaPreference, CallSettings)
    
    
    public virtual QuotaPreference CreateQuotaPreference(string parent, QuotaPreference quotaPreference, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    QuotaPreference quotaPreference = new QuotaPreference();
    // Make the request
    QuotaPreference response = cloudQuotasClient.CreateQuotaPreference(parent, quotaPreference);
    

### CreateQuotaPreference(string, QuotaPreference, string, CallSettings)
    
    
    public virtual QuotaPreference CreateQuotaPreference(string parent, QuotaPreference quotaPreference, string quotaPreferenceId, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    QuotaPreference quotaPreference = new QuotaPreference();
    string quotaPreferenceId = "";
    // Make the request
    QuotaPreference response = cloudQuotasClient.CreateQuotaPreference(parent, quotaPreference, quotaPreferenceId);
    

### CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, CallSettings)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest request, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    CreateQuotaPreferenceRequest request = new CreateQuotaPreferenceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        QuotaPreferenceId = "",
        QuotaPreference = new QuotaPreference(),
        IgnoreSafetyChecks =
        {
            QuotaSafetyCheck.Unspecified,
        },
    };
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(request);
    

### CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, CancellationToken)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest request, CancellationToken cancellationToken)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    CreateQuotaPreferenceRequest request = new CreateQuotaPreferenceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        QuotaPreferenceId = "",
        QuotaPreference = new QuotaPreference(),
        IgnoreSafetyChecks =
        {
            QuotaSafetyCheck.Unspecified,
        },
    };
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(request);
    

### CreateQuotaPreferenceAsync(LocationName, QuotaPreference, CallSettings)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(LocationName parent, QuotaPreference quotaPreference, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    QuotaPreference quotaPreference = new QuotaPreference();
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference);
    

### CreateQuotaPreferenceAsync(LocationName, QuotaPreference, string, CallSettings)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(LocationName parent, QuotaPreference quotaPreference, string quotaPreferenceId, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    QuotaPreference quotaPreference = new QuotaPreference();
    string quotaPreferenceId = "";
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference, quotaPreferenceId);
    

### CreateQuotaPreferenceAsync(LocationName, QuotaPreference, string, CancellationToken)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(LocationName parent, QuotaPreference quotaPreference, string quotaPreferenceId, CancellationToken cancellationToken)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    QuotaPreference quotaPreference = new QuotaPreference();
    string quotaPreferenceId = "";
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference, quotaPreferenceId);
    

### CreateQuotaPreferenceAsync(LocationName, QuotaPreference, CancellationToken)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(LocationName parent, QuotaPreference quotaPreference, CancellationToken cancellationToken)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    QuotaPreference quotaPreference = new QuotaPreference();
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference);
    

### CreateQuotaPreferenceAsync(string, QuotaPreference, CallSettings)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(string parent, QuotaPreference quotaPreference, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    QuotaPreference quotaPreference = new QuotaPreference();
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference);
    

### CreateQuotaPreferenceAsync(string, QuotaPreference, string, CallSettings)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(string parent, QuotaPreference quotaPreference, string quotaPreferenceId, CallSettings callSettings = null)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    QuotaPreference quotaPreference = new QuotaPreference();
    string quotaPreferenceId = "";
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference, quotaPreferenceId);
    

### CreateQuotaPreferenceAsync(string, QuotaPreference, string, CancellationToken)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(string parent, QuotaPreference quotaPreference, string quotaPreferenceId, CancellationToken cancellationToken)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    QuotaPreference quotaPreference = new QuotaPreference();
    string quotaPreferenceId = "";
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference, quotaPreferenceId);
    

### CreateQuotaPreferenceAsync(string, QuotaPreference, CancellationToken)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreferenceAsync(string parent, QuotaPreference quotaPreference, CancellationToken cancellationToken)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being created  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    QuotaPreference quotaPreference = new QuotaPreference();
    // Make the request
    QuotaPreference response = await cloudQuotasClient.CreateQuotaPreferenceAsync(parent, quotaPreference);
    

### GetQuotaInfo(GetQuotaInfoRequest, CallSettings)
    
    
    public virtual QuotaInfo GetQuotaInfo(GetQuotaInfoRequest request, CallSettings callSettings = null)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    GetQuotaInfoRequest request = new GetQuotaInfoRequest
    {
        QuotaInfoName = QuotaInfoName.FromProjectLocationServiceQuotaInfo("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]"),
    };
    // Make the request
    QuotaInfo response = cloudQuotasClient.GetQuotaInfo(request);
    

### GetQuotaInfo(QuotaInfoName, CallSettings)
    
    
    public virtual QuotaInfo GetQuotaInfo(QuotaInfoName name, CallSettings callSettings = null)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
Required. Identifier. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    QuotaInfoName name = QuotaInfoName.FromProjectLocationServiceQuotaInfo("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]");
    // Make the request
    QuotaInfo response = cloudQuotasClient.GetQuotaInfo(name);
    

### GetQuotaInfo(string, CallSettings)
    
    
    public virtual QuotaInfo GetQuotaInfo(string name, CallSettings callSettings = null)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/quotaInfos/[QUOTA_INFO]";
    // Make the request
    QuotaInfo response = cloudQuotasClient.GetQuotaInfo(name);
    

### GetQuotaInfoAsync(GetQuotaInfoRequest, CallSettings)
    
    
    public virtual Task<QuotaInfo> GetQuotaInfoAsync(GetQuotaInfoRequest request, CallSettings callSettings = null)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    GetQuotaInfoRequest request = new GetQuotaInfoRequest
    {
        QuotaInfoName = QuotaInfoName.FromProjectLocationServiceQuotaInfo("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]"),
    };
    // Make the request
    QuotaInfo response = await cloudQuotasClient.GetQuotaInfoAsync(request);
    

### GetQuotaInfoAsync(GetQuotaInfoRequest, CancellationToken)
    
    
    public virtual Task<QuotaInfo> GetQuotaInfoAsync(GetQuotaInfoRequest request, CancellationToken cancellationToken)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    GetQuotaInfoRequest request = new GetQuotaInfoRequest
    {
        QuotaInfoName = QuotaInfoName.FromProjectLocationServiceQuotaInfo("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]"),
    };
    // Make the request
    QuotaInfo response = await cloudQuotasClient.GetQuotaInfoAsync(request);
    

### GetQuotaInfoAsync(QuotaInfoName, CallSettings)
    
    
    public virtual Task<QuotaInfo> GetQuotaInfoAsync(QuotaInfoName name, CallSettings callSettings = null)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
Required. Identifier. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    QuotaInfoName name = QuotaInfoName.FromProjectLocationServiceQuotaInfo("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]");
    // Make the request
    QuotaInfo response = await cloudQuotasClient.GetQuotaInfoAsync(name);
    

### GetQuotaInfoAsync(QuotaInfoName, CancellationToken)
    
    
    public virtual Task<QuotaInfo> GetQuotaInfoAsync(QuotaInfoName name, CancellationToken cancellationToken)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
Required. Identifier. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    QuotaInfoName name = QuotaInfoName.FromProjectLocationServiceQuotaInfo("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]");
    // Make the request
    QuotaInfo response = await cloudQuotasClient.GetQuotaInfoAsync(name);
    

### GetQuotaInfoAsync(string, CallSettings)
    
    
    public virtual Task<QuotaInfo> GetQuotaInfoAsync(string name, CallSettings callSettings = null)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/quotaInfos/[QUOTA_INFO]";
    // Make the request
    QuotaInfo response = await cloudQuotasClient.GetQuotaInfoAsync(name);
    

### GetQuotaInfoAsync(string, CancellationToken)
    
    
    public virtual Task<QuotaInfo> GetQuotaInfoAsync(string name, CancellationToken cancellationToken)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/quotaInfos/[QUOTA_INFO]";
    // Make the request
    QuotaInfo response = await cloudQuotasClient.GetQuotaInfoAsync(name);
    

### GetQuotaPreference(GetQuotaPreferenceRequest, CallSettings)
    
    
    public virtual QuotaPreference GetQuotaPreference(GetQuotaPreferenceRequest request, CallSettings callSettings = null)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    GetQuotaPreferenceRequest request = new GetQuotaPreferenceRequest
    {
        QuotaPreferenceName = QuotaPreferenceName.FromProjectLocationQuotaPreference("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]"),
    };
    // Make the request
    QuotaPreference response = cloudQuotasClient.GetQuotaPreference(request);
    

### GetQuotaPreference(QuotaPreferenceName, CallSettings)
    
    
    public virtual QuotaPreference GetQuotaPreference(QuotaPreferenceName name, CallSettings callSettings = null)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName)`  
Required. Identifier. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    QuotaPreferenceName name = QuotaPreferenceName.FromProjectLocationQuotaPreference("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]");
    // Make the request
    QuotaPreference response = cloudQuotasClient.GetQuotaPreference(name);
    

### GetQuotaPreference(string, CallSettings)
    
    
    public virtual QuotaPreference GetQuotaPreference(string name, CallSettings callSettings = null)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/quotaPreferences/[QUOTA_PREFERENCE]";
    // Make the request
    QuotaPreference response = cloudQuotasClient.GetQuotaPreference(name);
    

### GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, CallSettings)
    
    
    public virtual Task<QuotaPreference> GetQuotaPreferenceAsync(GetQuotaPreferenceRequest request, CallSettings callSettings = null)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    GetQuotaPreferenceRequest request = new GetQuotaPreferenceRequest
    {
        QuotaPreferenceName = QuotaPreferenceName.FromProjectLocationQuotaPreference("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]"),
    };
    // Make the request
    QuotaPreference response = await cloudQuotasClient.GetQuotaPreferenceAsync(request);
    

### GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, CancellationToken)
    
    
    public virtual Task<QuotaPreference> GetQuotaPreferenceAsync(GetQuotaPreferenceRequest request, CancellationToken cancellationToken)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    GetQuotaPreferenceRequest request = new GetQuotaPreferenceRequest
    {
        QuotaPreferenceName = QuotaPreferenceName.FromProjectLocationQuotaPreference("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]"),
    };
    // Make the request
    QuotaPreference response = await cloudQuotasClient.GetQuotaPreferenceAsync(request);
    

### GetQuotaPreferenceAsync(QuotaPreferenceName, CallSettings)
    
    
    public virtual Task<QuotaPreference> GetQuotaPreferenceAsync(QuotaPreferenceName name, CallSettings callSettings = null)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName)`  
Required. Identifier. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    QuotaPreferenceName name = QuotaPreferenceName.FromProjectLocationQuotaPreference("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]");
    // Make the request
    QuotaPreference response = await cloudQuotasClient.GetQuotaPreferenceAsync(name);
    

### GetQuotaPreferenceAsync(QuotaPreferenceName, CancellationToken)
    
    
    public virtual Task<QuotaPreference> GetQuotaPreferenceAsync(QuotaPreferenceName name, CancellationToken cancellationToken)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName)`  
Required. Identifier. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    QuotaPreferenceName name = QuotaPreferenceName.FromProjectLocationQuotaPreference("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]");
    // Make the request
    QuotaPreference response = await cloudQuotasClient.GetQuotaPreferenceAsync(name);
    

### GetQuotaPreferenceAsync(string, CallSettings)
    
    
    public virtual Task<QuotaPreference> GetQuotaPreferenceAsync(string name, CallSettings callSettings = null)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/quotaPreferences/[QUOTA_PREFERENCE]";
    // Make the request
    QuotaPreference response = await cloudQuotasClient.GetQuotaPreferenceAsync(name);
    

### GetQuotaPreferenceAsync(string, CancellationToken)
    
    
    public virtual Task<QuotaPreference> GetQuotaPreferenceAsync(string name, CancellationToken cancellationToken)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/quotaPreferences/[QUOTA_PREFERENCE]";
    // Make the request
    QuotaPreference response = await cloudQuotasClient.GetQuotaPreferenceAsync(name);
    

### ListQuotaInfos(ListQuotaInfosRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> ListQuotaInfos(ListQuotaInfosRequest request, CallSettings callSettings = null)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A pageable sequence of [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    ListQuotaInfosRequest request = new ListQuotaInfosRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
    };
    // Make the request
    PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.ListQuotaInfos(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (QuotaInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListQuotaInfosResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaInfo> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaInfos(ServiceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> ListQuotaInfos(ServiceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName)`  
Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed. Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A pageable sequence of [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.ListQuotaInfos(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (QuotaInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListQuotaInfosResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaInfo> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaInfos(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> ListQuotaInfos(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed. Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A pageable sequence of [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.ListQuotaInfos(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (QuotaInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListQuotaInfosResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaInfo> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaInfosAsync(ListQuotaInfosRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> ListQuotaInfosAsync(ListQuotaInfosRequest request, CallSettings callSettings = null)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A pageable asynchronous sequence of [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    ListQuotaInfosRequest request = new ListQuotaInfosRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.ListQuotaInfosAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (QuotaInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListQuotaInfosResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaInfo> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaInfosAsync(ServiceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> ListQuotaInfosAsync(ServiceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName)`  
Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed. Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A pageable asynchronous sequence of [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.ListQuotaInfosAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (QuotaInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListQuotaInfosResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaInfo> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaInfosAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> ListQuotaInfosAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed. Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | A pageable asynchronous sequence of [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.ListQuotaInfosAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (QuotaInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListQuotaInfosResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaInfo> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaPreferences(ListQuotaPreferencesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> ListQuotaPreferences(ListQuotaPreferencesRequest request, CallSettings callSettings = null)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A pageable sequence of [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    ListQuotaPreferencesRequest request = new ListQuotaPreferencesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.ListQuotaPreferences(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (QuotaPreference item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListQuotaPreferencesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaPreference item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaPreference> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaPreference item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaPreferences(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> ListQuotaPreferences(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A pageable sequence of [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.ListQuotaPreferences(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (QuotaPreference item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListQuotaPreferencesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaPreference item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaPreference> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaPreference item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaPreferences(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> ListQuotaPreferences(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A pageable sequence of [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.ListQuotaPreferences(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (QuotaPreference item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListQuotaPreferencesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaPreference item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaPreference> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaPreference item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaPreferencesAsync(ListQuotaPreferencesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> ListQuotaPreferencesAsync(ListQuotaPreferencesRequest request, CallSettings callSettings = null)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A pageable asynchronous sequence of [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    ListQuotaPreferencesRequest request = new ListQuotaPreferencesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.ListQuotaPreferencesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (QuotaPreference item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListQuotaPreferencesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaPreference item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaPreference> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaPreference item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaPreferencesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> ListQuotaPreferencesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)`  
Required. Identifier. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A pageable asynchronous sequence of [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.ListQuotaPreferencesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (QuotaPreference item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListQuotaPreferencesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaPreference item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaPreference> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaPreference item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQuotaPreferencesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> ListQuotaPreferencesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A pageable asynchronous sequence of [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference) resources.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.ListQuotaPreferencesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (QuotaPreference item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListQuotaPreferencesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QuotaPreference item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QuotaPreference> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QuotaPreference item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateQuotaPreference(QuotaPreference, FieldMask, CallSettings)
    
    
    public virtual QuotaPreference UpdateQuotaPreference(QuotaPreference quotaPreference, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    QuotaPreference quotaPreference = new QuotaPreference();
    FieldMask updateMask = new FieldMask();
    // Make the request
    QuotaPreference response = cloudQuotasClient.UpdateQuotaPreference(quotaPreference, updateMask);
    

### UpdateQuotaPreference(UpdateQuotaPreferenceRequest, CallSettings)
    
    
    public virtual QuotaPreference UpdateQuotaPreference(UpdateQuotaPreferenceRequest request, CallSettings callSettings = null)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = CloudQuotasClient.Create();
    // Initialize request argument(s)
    UpdateQuotaPreferenceRequest request = new UpdateQuotaPreferenceRequest
    {
        UpdateMask = new FieldMask(),
        QuotaPreference = new QuotaPreference(),
        AllowMissing = false,
        ValidateOnly = false,
        IgnoreSafetyChecks =
        {
            QuotaSafetyCheck.Unspecified,
        },
    };
    // Make the request
    QuotaPreference response = cloudQuotasClient.UpdateQuotaPreference(request);
    

### UpdateQuotaPreferenceAsync(QuotaPreference, FieldMask, CallSettings)
    
    
    public virtual Task<QuotaPreference> UpdateQuotaPreferenceAsync(QuotaPreference quotaPreference, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    QuotaPreference quotaPreference = new QuotaPreference();
    FieldMask updateMask = new FieldMask();
    // Make the request
    QuotaPreference response = await cloudQuotasClient.UpdateQuotaPreferenceAsync(quotaPreference, updateMask);
    

### UpdateQuotaPreferenceAsync(QuotaPreference, FieldMask, CancellationToken)
    
    
    public virtual Task<QuotaPreference> UpdateQuotaPreferenceAsync(QuotaPreference quotaPreference, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    QuotaPreference quotaPreference = new QuotaPreference();
    FieldMask updateMask = new FieldMask();
    // Make the request
    QuotaPreference response = await cloudQuotasClient.UpdateQuotaPreferenceAsync(quotaPreference, updateMask);
    

### UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, CallSettings)
    
    
    public virtual Task<QuotaPreference> UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest request, CallSettings callSettings = null)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    UpdateQuotaPreferenceRequest request = new UpdateQuotaPreferenceRequest
    {
        UpdateMask = new FieldMask(),
        QuotaPreference = new QuotaPreference(),
        AllowMissing = false,
        ValidateOnly = false,
        IgnoreSafetyChecks =
        {
            QuotaSafetyCheck.Unspecified,
        },
    };
    // Make the request
    QuotaPreference response = await cloudQuotasClient.UpdateQuotaPreferenceAsync(request);
    

### UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, CancellationToken)
    
    
    public virtual Task<QuotaPreference> UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest request, CancellationToken cancellationToken)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudQuotasClient cloudQuotasClient = await CloudQuotasClient.CreateAsync();
    // Initialize request argument(s)
    UpdateQuotaPreferenceRequest request = new UpdateQuotaPreferenceRequest
    {
        UpdateMask = new FieldMask(),
        QuotaPreference = new QuotaPreference(),
        AllowMissing = false,
        ValidateOnly = false,
        IgnoreSafetyChecks =
        {
            QuotaSafetyCheck.Unspecified,
        },
    };
    // Make the request
    QuotaPreference response = await cloudQuotasClient.UpdateQuotaPreferenceAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
