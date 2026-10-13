---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient
title: Compute Engine v1 API - Class AdviceClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:25:24.950026+00:00
---

# Compute Engine v1 API - Class AdviceClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AdviceClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class AdviceClient

Reference documentation and code samples for the Compute Engine v1 API class AdviceClient.

Advice client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AdviceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AdviceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

The Advice API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Advice service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Advice scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Advice scopes are:

  * <https://www.googleapis.com/auth/compute>
  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual Advice.AdviceClient GrpcClient { get; }

The underlying gRPC Advice client

**Property Value**  
---  
**Type** | **Description**  
`[Advice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice)[AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice.AdviceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### CalendarMode(CalendarModeAdviceRpcRequest, CallSettings)
    
    
    public virtual CalendarModeAdviceResponse CalendarMode(CalendarModeAdviceRpcRequest request, CallSettings callSettings = null)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = AdviceClient.Create();
    // Initialize request argument(s)
    CalendarModeAdviceRpcRequest request = new CalendarModeAdviceRpcRequest
    {
        Region = "",
        CalendarModeAdviceRequestResource = new CalendarModeAdviceRequest(),
        Project = "",
    };
    // Make the request
    CalendarModeAdviceResponse response = adviceClient.CalendarMode(request);
    

### CalendarMode(string, string, CalendarModeAdviceRequest, CallSettings)
    
    
    public virtual CalendarModeAdviceResponse CalendarMode(string project, string region, CalendarModeAdviceRequest calendarModeAdviceRequestResource, CallSettings callSettings = null)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`calendarModeAdviceRequestResource` | `[CalendarModeAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = AdviceClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CalendarModeAdviceRequest calendarModeAdviceRequestResource = new CalendarModeAdviceRequest();
    // Make the request
    CalendarModeAdviceResponse response = adviceClient.CalendarMode(project, region, calendarModeAdviceRequestResource);
    

### CalendarModeAsync(CalendarModeAdviceRpcRequest, CallSettings)
    
    
    public virtual Task<CalendarModeAdviceResponse> CalendarModeAsync(CalendarModeAdviceRpcRequest request, CallSettings callSettings = null)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    CalendarModeAdviceRpcRequest request = new CalendarModeAdviceRpcRequest
    {
        Region = "",
        CalendarModeAdviceRequestResource = new CalendarModeAdviceRequest(),
        Project = "",
    };
    // Make the request
    CalendarModeAdviceResponse response = await adviceClient.CalendarModeAsync(request);
    

### CalendarModeAsync(CalendarModeAdviceRpcRequest, CancellationToken)
    
    
    public virtual Task<CalendarModeAdviceResponse> CalendarModeAsync(CalendarModeAdviceRpcRequest request, CancellationToken cancellationToken)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    CalendarModeAdviceRpcRequest request = new CalendarModeAdviceRpcRequest
    {
        Region = "",
        CalendarModeAdviceRequestResource = new CalendarModeAdviceRequest(),
        Project = "",
    };
    // Make the request
    CalendarModeAdviceResponse response = await adviceClient.CalendarModeAsync(request);
    

### CalendarModeAsync(string, string, CalendarModeAdviceRequest, CallSettings)
    
    
    public virtual Task<CalendarModeAdviceResponse> CalendarModeAsync(string project, string region, CalendarModeAdviceRequest calendarModeAdviceRequestResource, CallSettings callSettings = null)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`calendarModeAdviceRequestResource` | `[CalendarModeAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CalendarModeAdviceRequest calendarModeAdviceRequestResource = new CalendarModeAdviceRequest();
    // Make the request
    CalendarModeAdviceResponse response = await adviceClient.CalendarModeAsync(project, region, calendarModeAdviceRequestResource);
    

### CalendarModeAsync(string, string, CalendarModeAdviceRequest, CancellationToken)
    
    
    public virtual Task<CalendarModeAdviceResponse> CalendarModeAsync(string project, string region, CalendarModeAdviceRequest calendarModeAdviceRequestResource, CancellationToken cancellationToken)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`calendarModeAdviceRequestResource` | `[CalendarModeAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CalendarModeAdviceRequest calendarModeAdviceRequestResource = new CalendarModeAdviceRequest();
    // Make the request
    CalendarModeAdviceResponse response = await adviceClient.CalendarModeAsync(project, region, calendarModeAdviceRequestResource);
    

### Capacity(CapacityAdviceRpcRequest, CallSettings)
    
    
    public virtual CapacityAdviceResponse Capacity(CapacityAdviceRpcRequest request, CallSettings callSettings = null)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = AdviceClient.Create();
    // Initialize request argument(s)
    CapacityAdviceRpcRequest request = new CapacityAdviceRpcRequest
    {
        Region = "",
        CapacityAdviceRequestResource = new CapacityAdviceRequest(),
        Project = "",
    };
    // Make the request
    CapacityAdviceResponse response = adviceClient.Capacity(request);
    

### Capacity(string, string, CapacityAdviceRequest, CallSettings)
    
    
    public virtual CapacityAdviceResponse Capacity(string project, string region, CapacityAdviceRequest capacityAdviceRequestResource, CallSettings callSettings = null)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`capacityAdviceRequestResource` | `[CapacityAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = AdviceClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CapacityAdviceRequest capacityAdviceRequestResource = new CapacityAdviceRequest();
    // Make the request
    CapacityAdviceResponse response = adviceClient.Capacity(project, region, capacityAdviceRequestResource);
    

### CapacityAsync(CapacityAdviceRpcRequest, CallSettings)
    
    
    public virtual Task<CapacityAdviceResponse> CapacityAsync(CapacityAdviceRpcRequest request, CallSettings callSettings = null)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    CapacityAdviceRpcRequest request = new CapacityAdviceRpcRequest
    {
        Region = "",
        CapacityAdviceRequestResource = new CapacityAdviceRequest(),
        Project = "",
    };
    // Make the request
    CapacityAdviceResponse response = await adviceClient.CapacityAsync(request);
    

### CapacityAsync(CapacityAdviceRpcRequest, CancellationToken)
    
    
    public virtual Task<CapacityAdviceResponse> CapacityAsync(CapacityAdviceRpcRequest request, CancellationToken cancellationToken)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    CapacityAdviceRpcRequest request = new CapacityAdviceRpcRequest
    {
        Region = "",
        CapacityAdviceRequestResource = new CapacityAdviceRequest(),
        Project = "",
    };
    // Make the request
    CapacityAdviceResponse response = await adviceClient.CapacityAsync(request);
    

### CapacityAsync(string, string, CapacityAdviceRequest, CallSettings)
    
    
    public virtual Task<CapacityAdviceResponse> CapacityAsync(string project, string region, CapacityAdviceRequest capacityAdviceRequestResource, CallSettings callSettings = null)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`capacityAdviceRequestResource` | `[CapacityAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CapacityAdviceRequest capacityAdviceRequestResource = new CapacityAdviceRequest();
    // Make the request
    CapacityAdviceResponse response = await adviceClient.CapacityAsync(project, region, capacityAdviceRequestResource);
    

### CapacityAsync(string, string, CapacityAdviceRequest, CancellationToken)
    
    
    public virtual Task<CapacityAdviceResponse> CapacityAsync(string project, string region, CapacityAdviceRequest capacityAdviceRequestResource, CancellationToken cancellationToken)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`capacityAdviceRequestResource` | `[CapacityAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CapacityAdviceRequest capacityAdviceRequestResource = new CapacityAdviceRequest();
    // Make the request
    CapacityAdviceResponse response = await adviceClient.CapacityAsync(project, region, capacityAdviceRequestResource);
    

### CapacityHistory(CapacityHistoryAdviceRequest, CallSettings)
    
    
    public virtual CapacityHistoryResponse CapacityHistory(CapacityHistoryAdviceRequest request, CallSettings callSettings = null)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryAdviceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = AdviceClient.Create();
    // Initialize request argument(s)
    CapacityHistoryAdviceRequest request = new CapacityHistoryAdviceRequest
    {
        Region = "",
        CapacityHistoryRequestResource = new CapacityHistoryRequest(),
        Project = "",
    };
    // Make the request
    CapacityHistoryResponse response = adviceClient.CapacityHistory(request);
    

### CapacityHistory(string, string, CapacityHistoryRequest, CallSettings)
    
    
    public virtual CapacityHistoryResponse CapacityHistory(string project, string region, CapacityHistoryRequest capacityHistoryRequestResource, CallSettings callSettings = null)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`capacityHistoryRequestResource` | `[CapacityHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = AdviceClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CapacityHistoryRequest capacityHistoryRequestResource = new CapacityHistoryRequest();
    // Make the request
    CapacityHistoryResponse response = adviceClient.CapacityHistory(project, region, capacityHistoryRequestResource);
    

### CapacityHistoryAsync(CapacityHistoryAdviceRequest, CallSettings)
    
    
    public virtual Task<CapacityHistoryResponse> CapacityHistoryAsync(CapacityHistoryAdviceRequest request, CallSettings callSettings = null)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryAdviceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    CapacityHistoryAdviceRequest request = new CapacityHistoryAdviceRequest
    {
        Region = "",
        CapacityHistoryRequestResource = new CapacityHistoryRequest(),
        Project = "",
    };
    // Make the request
    CapacityHistoryResponse response = await adviceClient.CapacityHistoryAsync(request);
    

### CapacityHistoryAsync(CapacityHistoryAdviceRequest, CancellationToken)
    
    
    public virtual Task<CapacityHistoryResponse> CapacityHistoryAsync(CapacityHistoryAdviceRequest request, CancellationToken cancellationToken)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryAdviceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    CapacityHistoryAdviceRequest request = new CapacityHistoryAdviceRequest
    {
        Region = "",
        CapacityHistoryRequestResource = new CapacityHistoryRequest(),
        Project = "",
    };
    // Make the request
    CapacityHistoryResponse response = await adviceClient.CapacityHistoryAsync(request);
    

### CapacityHistoryAsync(string, string, CapacityHistoryRequest, CallSettings)
    
    
    public virtual Task<CapacityHistoryResponse> CapacityHistoryAsync(string project, string region, CapacityHistoryRequest capacityHistoryRequestResource, CallSettings callSettings = null)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`capacityHistoryRequestResource` | `[CapacityHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CapacityHistoryRequest capacityHistoryRequestResource = new CapacityHistoryRequest();
    // Make the request
    CapacityHistoryResponse response = await adviceClient.CapacityHistoryAsync(project, region, capacityHistoryRequestResource);
    

### CapacityHistoryAsync(string, string, CapacityHistoryRequest, CancellationToken)
    
    
    public virtual Task<CapacityHistoryResponse> CapacityHistoryAsync(string project, string region, CapacityHistoryRequest capacityHistoryRequestResource, CancellationToken cancellationToken)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`capacityHistoryRequestResource` | `[CapacityHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AdviceClient adviceClient = await AdviceClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    CapacityHistoryRequest capacityHistoryRequestResource = new CapacityHistoryRequest();
    // Make the request
    CapacityHistoryResponse response = await adviceClient.CapacityHistoryAsync(project, region, capacityHistoryRequestResource);
    

### Create()
    
    
    public static AdviceClient Create()

Synchronously creates a [AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AdviceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient)` | The created [AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AdviceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AdviceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient)` | The task representing the created [AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient).  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient#Google_Cloud_Compute_V1_AdviceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient#Google_Cloud_Compute_V1_AdviceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient#Google_Cloud_Compute_V1_AdviceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient#Google_Cloud_Compute_V1_AdviceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
