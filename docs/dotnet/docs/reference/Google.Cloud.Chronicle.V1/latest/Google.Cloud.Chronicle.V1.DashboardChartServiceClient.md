---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient
title: Chronicle v1 API - Class DashboardChartServiceClient (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:04.369803+00:00
---

# Chronicle v1 API - Class DashboardChartServiceClient (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class DashboardChartServiceClient (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public abstract class DashboardChartServiceClient

Reference documentation and code samples for the Chronicle v1 API class DashboardChartServiceClient.

DashboardChartService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DashboardChartServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DashboardChartServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClientImpl)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Remarks

A service providing functionality for managing dashboards' charts.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DashboardChartService service, which is a host of "chronicle.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DashboardChartService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DashboardChartService scopes are:

  * <https://www.googleapis.com/auth/chronicle>
  * <https://www.googleapis.com/auth/chronicle.readonly>
  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual DashboardChartService.DashboardChartServiceClient GrpcClient { get; }

The underlying gRPC DashboardChartService client

**Property Value**  
---  
**Type** | **Description**  
`[DashboardChartService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService)[DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService.DashboardChartServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### BatchGetDashboardCharts(BatchGetDashboardChartsRequest, CallSettings)
    
    
    public virtual BatchGetDashboardChartsResponse BatchGetDashboardCharts(BatchGetDashboardChartsRequest request, CallSettings callSettings = null)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDashboardChartsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = DashboardChartServiceClient.Create();
    // Initialize request argument(s)
    BatchGetDashboardChartsRequest request = new BatchGetDashboardChartsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        DashboardChartNames =
        {
            DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
        },
    };
    // Make the request
    BatchGetDashboardChartsResponse response = dashboardChartServiceClient.BatchGetDashboardCharts(request);
    

### BatchGetDashboardCharts(InstanceName, IEnumerable<DashboardChartName>, CallSettings)
    
    
    public virtual BatchGetDashboardChartsResponse BatchGetDashboardCharts(InstanceName parent, IEnumerable<DashboardChartName> names, CallSettings callSettings = null)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent resource shared by all dashboard charts being retrieved. Format: projects/{project}/locations/{location}/instances/{instance} If this is set, the parent of all of the dashboard charts specified in `names` must match this field.  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[DashboardChartName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartName)`  
Required. The names of the dashboard charts to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = DashboardChartServiceClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    IEnumerable<DashboardChartName> names = new DashboardChartName[]
    {
        DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
    };
    // Make the request
    BatchGetDashboardChartsResponse response = dashboardChartServiceClient.BatchGetDashboardCharts(parent, names);
    

### BatchGetDashboardCharts(string, IEnumerable<string>, CallSettings)
    
    
    public virtual BatchGetDashboardChartsResponse BatchGetDashboardCharts(string parent, IEnumerable<string> names, CallSettings callSettings = null)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource shared by all dashboard charts being retrieved. Format: projects/{project}/locations/{location}/instances/{instance} If this is set, the parent of all of the dashboard charts specified in `names` must match this field.  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The names of the dashboard charts to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = DashboardChartServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    IEnumerable<string> names = new string[]
    {
        "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/dashboardCharts/[CHART]",
    };
    // Make the request
    BatchGetDashboardChartsResponse response = dashboardChartServiceClient.BatchGetDashboardCharts(parent, names);
    

### BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest, CallSettings)
    
    
    public virtual Task<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest request, CallSettings callSettings = null)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDashboardChartsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchGetDashboardChartsRequest request = new BatchGetDashboardChartsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        DashboardChartNames =
        {
            DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
        },
    };
    // Make the request
    BatchGetDashboardChartsResponse response = await dashboardChartServiceClient.BatchGetDashboardChartsAsync(request);
    

### BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest, CancellationToken)
    
    
    public virtual Task<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest request, CancellationToken cancellationToken)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDashboardChartsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchGetDashboardChartsRequest request = new BatchGetDashboardChartsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        DashboardChartNames =
        {
            DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
        },
    };
    // Make the request
    BatchGetDashboardChartsResponse response = await dashboardChartServiceClient.BatchGetDashboardChartsAsync(request);
    

### BatchGetDashboardChartsAsync(InstanceName, IEnumerable<DashboardChartName>, CallSettings)
    
    
    public virtual Task<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(InstanceName parent, IEnumerable<DashboardChartName> names, CallSettings callSettings = null)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent resource shared by all dashboard charts being retrieved. Format: projects/{project}/locations/{location}/instances/{instance} If this is set, the parent of all of the dashboard charts specified in `names` must match this field.  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[DashboardChartName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartName)`  
Required. The names of the dashboard charts to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    IEnumerable<DashboardChartName> names = new DashboardChartName[]
    {
        DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
    };
    // Make the request
    BatchGetDashboardChartsResponse response = await dashboardChartServiceClient.BatchGetDashboardChartsAsync(parent, names);
    

### BatchGetDashboardChartsAsync(InstanceName, IEnumerable<DashboardChartName>, CancellationToken)
    
    
    public virtual Task<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(InstanceName parent, IEnumerable<DashboardChartName> names, CancellationToken cancellationToken)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent resource shared by all dashboard charts being retrieved. Format: projects/{project}/locations/{location}/instances/{instance} If this is set, the parent of all of the dashboard charts specified in `names` must match this field.  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[DashboardChartName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartName)`  
Required. The names of the dashboard charts to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    IEnumerable<DashboardChartName> names = new DashboardChartName[]
    {
        DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
    };
    // Make the request
    BatchGetDashboardChartsResponse response = await dashboardChartServiceClient.BatchGetDashboardChartsAsync(parent, names);
    

### BatchGetDashboardChartsAsync(string, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(string parent, IEnumerable<string> names, CallSettings callSettings = null)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource shared by all dashboard charts being retrieved. Format: projects/{project}/locations/{location}/instances/{instance} If this is set, the parent of all of the dashboard charts specified in `names` must match this field.  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The names of the dashboard charts to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    IEnumerable<string> names = new string[]
    {
        "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/dashboardCharts/[CHART]",
    };
    // Make the request
    BatchGetDashboardChartsResponse response = await dashboardChartServiceClient.BatchGetDashboardChartsAsync(parent, names);
    

### BatchGetDashboardChartsAsync(string, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(string parent, IEnumerable<string> names, CancellationToken cancellationToken)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource shared by all dashboard charts being retrieved. Format: projects/{project}/locations/{location}/instances/{instance} If this is set, the parent of all of the dashboard charts specified in `names` must match this field.  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The names of the dashboard charts to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    IEnumerable<string> names = new string[]
    {
        "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/dashboardCharts/[CHART]",
    };
    // Make the request
    BatchGetDashboardChartsResponse response = await dashboardChartServiceClient.BatchGetDashboardChartsAsync(parent, names);
    

### Create()
    
    
    public static DashboardChartServiceClient Create()

Synchronously creates a [DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DashboardChartServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient)` | The created [DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DashboardChartServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DashboardChartServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient)` | The task representing the created [DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient).  
  
### GetDashboardChart(DashboardChartName, CallSettings)
    
    
    public virtual DashboardChart GetDashboardChart(DashboardChartName name, CallSettings callSettings = null)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DashboardChartName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartName)`  
Required. The name of the dashboardChart to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/dashboardCharts/{chart}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | The RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = DashboardChartServiceClient.Create();
    // Initialize request argument(s)
    DashboardChartName name = DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]");
    // Make the request
    DashboardChart response = dashboardChartServiceClient.GetDashboardChart(name);
    

### GetDashboardChart(GetDashboardChartRequest, CallSettings)
    
    
    public virtual DashboardChart GetDashboardChart(GetDashboardChartRequest request, CallSettings callSettings = null)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardChartRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDashboardChartRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | The RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = DashboardChartServiceClient.Create();
    // Initialize request argument(s)
    GetDashboardChartRequest request = new GetDashboardChartRequest
    {
        DashboardChartName = DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
    };
    // Make the request
    DashboardChart response = dashboardChartServiceClient.GetDashboardChart(request);
    

### GetDashboardChart(string, CallSettings)
    
    
    public virtual DashboardChart GetDashboardChart(string name, CallSettings callSettings = null)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the dashboardChart to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/dashboardCharts/{chart}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | The RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = DashboardChartServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/dashboardCharts/[CHART]";
    // Make the request
    DashboardChart response = dashboardChartServiceClient.GetDashboardChart(name);
    

### GetDashboardChartAsync(DashboardChartName, CallSettings)
    
    
    public virtual Task<DashboardChart> GetDashboardChartAsync(DashboardChartName name, CallSettings callSettings = null)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DashboardChartName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartName)`  
Required. The name of the dashboardChart to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/dashboardCharts/{chart}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    DashboardChartName name = DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]");
    // Make the request
    DashboardChart response = await dashboardChartServiceClient.GetDashboardChartAsync(name);
    

### GetDashboardChartAsync(DashboardChartName, CancellationToken)
    
    
    public virtual Task<DashboardChart> GetDashboardChartAsync(DashboardChartName name, CancellationToken cancellationToken)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DashboardChartName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartName)`  
Required. The name of the dashboardChart to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/dashboardCharts/{chart}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    DashboardChartName name = DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]");
    // Make the request
    DashboardChart response = await dashboardChartServiceClient.GetDashboardChartAsync(name);
    

### GetDashboardChartAsync(GetDashboardChartRequest, CallSettings)
    
    
    public virtual Task<DashboardChart> GetDashboardChartAsync(GetDashboardChartRequest request, CallSettings callSettings = null)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardChartRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDashboardChartRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDashboardChartRequest request = new GetDashboardChartRequest
    {
        DashboardChartName = DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
    };
    // Make the request
    DashboardChart response = await dashboardChartServiceClient.GetDashboardChartAsync(request);
    

### GetDashboardChartAsync(GetDashboardChartRequest, CancellationToken)
    
    
    public virtual Task<DashboardChart> GetDashboardChartAsync(GetDashboardChartRequest request, CancellationToken cancellationToken)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardChartRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDashboardChartRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDashboardChartRequest request = new GetDashboardChartRequest
    {
        DashboardChartName = DashboardChartName.FromProjectLocationInstanceChart("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[CHART]"),
    };
    // Make the request
    DashboardChart response = await dashboardChartServiceClient.GetDashboardChartAsync(request);
    

### GetDashboardChartAsync(string, CallSettings)
    
    
    public virtual Task<DashboardChart> GetDashboardChartAsync(string name, CallSettings callSettings = null)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the dashboardChart to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/dashboardCharts/{chart}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/dashboardCharts/[CHART]";
    // Make the request
    DashboardChart response = await dashboardChartServiceClient.GetDashboardChartAsync(name);
    

### GetDashboardChartAsync(string, CancellationToken)
    
    
    public virtual Task<DashboardChart> GetDashboardChartAsync(string name, CancellationToken cancellationToken)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the dashboardChart to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/dashboardCharts/{chart}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DashboardChartServiceClient dashboardChartServiceClient = await DashboardChartServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/dashboardCharts/[CHART]";
    // Make the request
    DashboardChart response = await dashboardChartServiceClient.GetDashboardChartAsync(name);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient#Google_Cloud_Chronicle_V1_DashboardChartServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient#Google_Cloud_Chronicle_V1_DashboardChartServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient#Google_Cloud_Chronicle_V1_DashboardChartServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartServiceClient#Google_Cloud_Chronicle_V1_DashboardChartServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
