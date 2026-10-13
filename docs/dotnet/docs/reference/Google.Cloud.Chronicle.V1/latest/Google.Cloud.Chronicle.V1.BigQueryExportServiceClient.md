---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient
title: Chronicle v1 API - Class BigQueryExportServiceClient (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:41.545007+00:00
---

# Chronicle v1 API - Class BigQueryExportServiceClient (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class BigQueryExportServiceClient (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public abstract class BigQueryExportServiceClient

Reference documentation and code samples for the Chronicle v1 API class BigQueryExportServiceClient.

BigQueryExportService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigQueryExportServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[BigQueryExportServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClientImpl)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Remarks

Service for managing BigQuery export configurations for Chronicle instances.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the BigQueryExportService service, which is a host of "chronicle.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default BigQueryExportService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default BigQueryExportService scopes are:

  * <https://www.googleapis.com/auth/chronicle>
  * <https://www.googleapis.com/auth/chronicle.readonly>
  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual BigQueryExportService.BigQueryExportServiceClient GrpcClient { get; }

The underlying gRPC BigQueryExportService client

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryExportService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService)[BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static BigQueryExportServiceClient Create()

Synchronously creates a [BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BigQueryExportServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient)` | The created [BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<BigQueryExportServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BigQueryExportServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient)` | The task representing the created [BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient).  
  
### GetBigQueryExport(BigQueryExportName, CallSettings)
    
    
    public virtual BigQueryExport GetBigQueryExport(BigQueryExportName name, CallSettings callSettings = null)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BigQueryExportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportName)`  
Required. The resource name of the BigqueryExport to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    BigQueryExportName name = BigQueryExportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.GetBigQueryExport(name);
    

### GetBigQueryExport(GetBigQueryExportRequest, CallSettings)
    
    
    public virtual BigQueryExport GetBigQueryExport(GetBigQueryExportRequest request, CallSettings callSettings = null)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    GetBigQueryExportRequest request = new GetBigQueryExportRequest
    {
        BigQueryExportName = BigQueryExportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.GetBigQueryExport(request);
    

### GetBigQueryExport(string, CallSettings)
    
    
    public virtual BigQueryExport GetBigQueryExport(string name, CallSettings callSettings = null)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the BigqueryExport to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/bigQueryExport";
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.GetBigQueryExport(name);
    

### GetBigQueryExportAsync(BigQueryExportName, CallSettings)
    
    
    public virtual Task<BigQueryExport> GetBigQueryExportAsync(BigQueryExportName name, CallSettings callSettings = null)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BigQueryExportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportName)`  
Required. The resource name of the BigqueryExport to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    BigQueryExportName name = BigQueryExportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.GetBigQueryExportAsync(name);
    

### GetBigQueryExportAsync(BigQueryExportName, CancellationToken)
    
    
    public virtual Task<BigQueryExport> GetBigQueryExportAsync(BigQueryExportName name, CancellationToken cancellationToken)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BigQueryExportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportName)`  
Required. The resource name of the BigqueryExport to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    BigQueryExportName name = BigQueryExportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.GetBigQueryExportAsync(name);
    

### GetBigQueryExportAsync(GetBigQueryExportRequest, CallSettings)
    
    
    public virtual Task<BigQueryExport> GetBigQueryExportAsync(GetBigQueryExportRequest request, CallSettings callSettings = null)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetBigQueryExportRequest request = new GetBigQueryExportRequest
    {
        BigQueryExportName = BigQueryExportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.GetBigQueryExportAsync(request);
    

### GetBigQueryExportAsync(GetBigQueryExportRequest, CancellationToken)
    
    
    public virtual Task<BigQueryExport> GetBigQueryExportAsync(GetBigQueryExportRequest request, CancellationToken cancellationToken)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetBigQueryExportRequest request = new GetBigQueryExportRequest
    {
        BigQueryExportName = BigQueryExportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.GetBigQueryExportAsync(request);
    

### GetBigQueryExportAsync(string, CallSettings)
    
    
    public virtual Task<BigQueryExport> GetBigQueryExportAsync(string name, CallSettings callSettings = null)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the BigqueryExport to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/bigQueryExport";
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.GetBigQueryExportAsync(name);
    

### GetBigQueryExportAsync(string, CancellationToken)
    
    
    public virtual Task<BigQueryExport> GetBigQueryExportAsync(string name, CancellationToken cancellationToken)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the BigqueryExport to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/bigQueryExport";
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.GetBigQueryExportAsync(name);
    

### ProvisionBigQueryExport(InstanceName, CallSettings)
    
    
    public virtual BigQueryExport ProvisionBigQueryExport(InstanceName parent, CallSettings callSettings = null)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The instance for which BigQuery export is being provisioned. Format: projects/{project}/locations/{location}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.ProvisionBigQueryExport(parent);
    

### ProvisionBigQueryExport(ProvisionBigQueryExportRequest, CallSettings)
    
    
    public virtual BigQueryExport ProvisionBigQueryExport(ProvisionBigQueryExportRequest request, CallSettings callSettings = null)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    ProvisionBigQueryExportRequest request = new ProvisionBigQueryExportRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.ProvisionBigQueryExport(request);
    

### ProvisionBigQueryExport(string, CallSettings)
    
    
    public virtual BigQueryExport ProvisionBigQueryExport(string parent, CallSettings callSettings = null)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance for which BigQuery export is being provisioned. Format: projects/{project}/locations/{location}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.ProvisionBigQueryExport(parent);
    

### ProvisionBigQueryExportAsync(InstanceName, CallSettings)
    
    
    public virtual Task<BigQueryExport> ProvisionBigQueryExportAsync(InstanceName parent, CallSettings callSettings = null)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The instance for which BigQuery export is being provisioned. Format: projects/{project}/locations/{location}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.ProvisionBigQueryExportAsync(parent);
    

### ProvisionBigQueryExportAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<BigQueryExport> ProvisionBigQueryExportAsync(InstanceName parent, CancellationToken cancellationToken)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The instance for which BigQuery export is being provisioned. Format: projects/{project}/locations/{location}/instances/{instance}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.ProvisionBigQueryExportAsync(parent);
    

### ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest, CallSettings)
    
    
    public virtual Task<BigQueryExport> ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest request, CallSettings callSettings = null)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProvisionBigQueryExportRequest request = new ProvisionBigQueryExportRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.ProvisionBigQueryExportAsync(request);
    

### ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest, CancellationToken)
    
    
    public virtual Task<BigQueryExport> ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest request, CancellationToken cancellationToken)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProvisionBigQueryExportRequest request = new ProvisionBigQueryExportRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.ProvisionBigQueryExportAsync(request);
    

### ProvisionBigQueryExportAsync(string, CallSettings)
    
    
    public virtual Task<BigQueryExport> ProvisionBigQueryExportAsync(string parent, CallSettings callSettings = null)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance for which BigQuery export is being provisioned. Format: projects/{project}/locations/{location}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.ProvisionBigQueryExportAsync(parent);
    

### ProvisionBigQueryExportAsync(string, CancellationToken)
    
    
    public virtual Task<BigQueryExport> ProvisionBigQueryExportAsync(string parent, CancellationToken cancellationToken)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance for which BigQuery export is being provisioned. Format: projects/{project}/locations/{location}/instances/{instance}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.ProvisionBigQueryExportAsync(parent);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient#Google_Cloud_Chronicle_V1_BigQueryExportServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient#Google_Cloud_Chronicle_V1_BigQueryExportServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient#Google_Cloud_Chronicle_V1_BigQueryExportServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportServiceClient#Google_Cloud_Chronicle_V1_BigQueryExportServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateBigQueryExport(BigQueryExport, FieldMask, CallSettings)
    
    
    public virtual BigQueryExport UpdateBigQueryExport(BigQueryExport bigQueryExport, FieldMask updateMask, CallSettings callSettings = null)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)`  
Required. The BigQueryExport settings to update. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    BigQueryExport bigQueryExport = new BigQueryExport();
    FieldMask updateMask = new FieldMask();
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.UpdateBigQueryExport(bigQueryExport, updateMask);
    

### UpdateBigQueryExport(UpdateBigQueryExportRequest, CallSettings)
    
    
    public virtual BigQueryExport UpdateBigQueryExport(UpdateBigQueryExportRequest request, CallSettings callSettings = null)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = BigQueryExportServiceClient.Create();
    // Initialize request argument(s)
    UpdateBigQueryExportRequest request = new UpdateBigQueryExportRequest
    {
        BigQueryExport = new BigQueryExport(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    BigQueryExport response = bigQueryExportServiceClient.UpdateBigQueryExport(request);
    

### UpdateBigQueryExportAsync(BigQueryExport, FieldMask, CallSettings)
    
    
    public virtual Task<BigQueryExport> UpdateBigQueryExportAsync(BigQueryExport bigQueryExport, FieldMask updateMask, CallSettings callSettings = null)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)`  
Required. The BigQueryExport settings to update. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    BigQueryExport bigQueryExport = new BigQueryExport();
    FieldMask updateMask = new FieldMask();
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.UpdateBigQueryExportAsync(bigQueryExport, updateMask);
    

### UpdateBigQueryExportAsync(BigQueryExport, FieldMask, CancellationToken)
    
    
    public virtual Task<BigQueryExport> UpdateBigQueryExportAsync(BigQueryExport bigQueryExport, FieldMask updateMask, CancellationToken cancellationToken)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)`  
Required. The BigQueryExport settings to update. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    BigQueryExport bigQueryExport = new BigQueryExport();
    FieldMask updateMask = new FieldMask();
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.UpdateBigQueryExportAsync(bigQueryExport, updateMask);
    

### UpdateBigQueryExportAsync(UpdateBigQueryExportRequest, CallSettings)
    
    
    public virtual Task<BigQueryExport> UpdateBigQueryExportAsync(UpdateBigQueryExportRequest request, CallSettings callSettings = null)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateBigQueryExportRequest request = new UpdateBigQueryExportRequest
    {
        BigQueryExport = new BigQueryExport(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.UpdateBigQueryExportAsync(request);
    

### UpdateBigQueryExportAsync(UpdateBigQueryExportRequest, CancellationToken)
    
    
    public virtual Task<BigQueryExport> UpdateBigQueryExportAsync(UpdateBigQueryExportRequest request, CancellationToken cancellationToken)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BigQueryExportServiceClient bigQueryExportServiceClient = await BigQueryExportServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateBigQueryExportRequest request = new UpdateBigQueryExportRequest
    {
        BigQueryExport = new BigQueryExport(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    BigQueryExport response = await bigQueryExportServiceClient.UpdateBigQueryExportAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
