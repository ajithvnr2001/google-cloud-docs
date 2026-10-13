---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient
title: Compute Engine v1 API - Class RegionSslCertificatesClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:39.170195+00:00
---

# Compute Engine v1 API - Class RegionSslCertificatesClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class RegionSslCertificatesClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class RegionSslCertificatesClient

Reference documentation and code samples for the Compute Engine v1 API class RegionSslCertificatesClient.

RegionSslCertificates client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RegionSslCertificatesClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[RegionSslCertificatesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

The RegionSslCertificates API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the RegionSslCertificates service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default RegionSslCertificates scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default RegionSslCertificates scopes are:

  * <https://www.googleapis.com/auth/compute>
  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteOperationsClient
    
    
    public virtual OperationsClient DeleteOperationsClient { get; }

The long-running operations client for `Delete`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual RegionSslCertificates.RegionSslCertificatesClient GrpcClient { get; }

The underlying gRPC RegionSslCertificates client

**Property Value**  
---  
**Type** | **Description**  
`[RegionSslCertificates](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificates)[RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificates.RegionSslCertificatesClient)` |   
  
### InsertOperationsClient
    
    
    public virtual OperationsClient InsertOperationsClient { get; }

The long-running operations client for `Insert`.

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
  
## Methods 

### Create()
    
    
    public static RegionSslCertificatesClient Create()

Synchronously creates a [RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [RegionSslCertificatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient)` | The created [RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<RegionSslCertificatesClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [RegionSslCertificatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient)` | The task representing the created [RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient).  
  
### Delete(DeleteRegionSslCertificateRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(DeleteRegionSslCertificateRequest request, CallSettings callSettings = null)

Deletes the specified SslCertificate resource in the region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    DeleteRegionSslCertificateRequest request = new DeleteRegionSslCertificateRequest
    {
        RequestId = "",
        SslCertificate = "",
        Region = "",
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = regionSslCertificatesClient.Delete(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = regionSslCertificatesClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Delete(string, string, string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(string project, string region, string sslCertificate, CallSettings callSettings = null)

Deletes the specified SslCertificate resource in the region.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificate` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the SslCertificate resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string sslCertificate = "";
    // Make the request
    lro::Operation<Operation, Operation> response = regionSslCertificatesClient.Delete(project, region, sslCertificate);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = regionSslCertificatesClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteRegionSslCertificateRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteRegionSslCertificateRequest request, CallSettings callSettings = null)

Deletes the specified SslCertificate resource in the region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    DeleteRegionSslCertificateRequest request = new DeleteRegionSslCertificateRequest
    {
        RequestId = "",
        SslCertificate = "",
        Region = "",
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteRegionSslCertificateRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteRegionSslCertificateRequest request, CancellationToken cancellationToken)

Deletes the specified SslCertificate resource in the region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    DeleteRegionSslCertificateRequest request = new DeleteRegionSslCertificateRequest
    {
        RequestId = "",
        SslCertificate = "",
        Region = "",
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string region, string sslCertificate, CallSettings callSettings = null)

Deletes the specified SslCertificate resource in the region.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificate` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the SslCertificate resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string sslCertificate = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.DeleteAsync(project, region, sslCertificate);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string region, string sslCertificate, CancellationToken cancellationToken)

Deletes the specified SslCertificate resource in the region.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificate` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the SslCertificate resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string sslCertificate = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.DeleteAsync(project, region, sslCertificate);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Get(GetRegionSslCertificateRequest, CallSettings)
    
    
    public virtual SslCertificate Get(GetRegionSslCertificateRequest request, CallSettings callSettings = null)

Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    GetRegionSslCertificateRequest request = new GetRegionSslCertificateRequest
    {
        SslCertificate = "",
        Region = "",
        Project = "",
    };
    // Make the request
    SslCertificate response = regionSslCertificatesClient.Get(request);
    

### Get(string, string, string, CallSettings)
    
    
    public virtual SslCertificate Get(string project, string region, string sslCertificate, CallSettings callSettings = null)

Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificate` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the SslCertificate resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string sslCertificate = "";
    // Make the request
    SslCertificate response = regionSslCertificatesClient.Get(project, region, sslCertificate);
    

### GetAsync(GetRegionSslCertificateRequest, CallSettings)
    
    
    public virtual Task<SslCertificate> GetAsync(GetRegionSslCertificateRequest request, CallSettings callSettings = null)

Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    GetRegionSslCertificateRequest request = new GetRegionSslCertificateRequest
    {
        SslCertificate = "",
        Region = "",
        Project = "",
    };
    // Make the request
    SslCertificate response = await regionSslCertificatesClient.GetAsync(request);
    

### GetAsync(GetRegionSslCertificateRequest, CancellationToken)
    
    
    public virtual Task<SslCertificate> GetAsync(GetRegionSslCertificateRequest request, CancellationToken cancellationToken)

Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    GetRegionSslCertificateRequest request = new GetRegionSslCertificateRequest
    {
        SslCertificate = "",
        Region = "",
        Project = "",
    };
    // Make the request
    SslCertificate response = await regionSslCertificatesClient.GetAsync(request);
    

### GetAsync(string, string, string, CallSettings)
    
    
    public virtual Task<SslCertificate> GetAsync(string project, string region, string sslCertificate, CallSettings callSettings = null)

Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificate` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the SslCertificate resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string sslCertificate = "";
    // Make the request
    SslCertificate response = await regionSslCertificatesClient.GetAsync(project, region, sslCertificate);
    

### GetAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<SslCertificate> GetAsync(string project, string region, string sslCertificate, CancellationToken cancellationToken)

Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificate` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the SslCertificate resource to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string sslCertificate = "";
    // Make the request
    SslCertificate response = await regionSslCertificatesClient.GetAsync(project, region, sslCertificate);
    

### Insert(InsertRegionSslCertificateRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(InsertRegionSslCertificateRequest request, CallSettings callSettings = null)

Creates a SslCertificate resource in the specified project and region using the data included in the request

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    InsertRegionSslCertificateRequest request = new InsertRegionSslCertificateRequest
    {
        RequestId = "",
        Region = "",
        SslCertificateResource = new SslCertificate(),
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = regionSslCertificatesClient.Insert(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = regionSslCertificatesClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Insert(string, string, SslCertificate, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(string project, string region, SslCertificate sslCertificateResource, CallSettings callSettings = null)

Creates a SslCertificate resource in the specified project and region using the data included in the request

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificateResource` | `[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    SslCertificate sslCertificateResource = new SslCertificate();
    // Make the request
    lro::Operation<Operation, Operation> response = regionSslCertificatesClient.Insert(project, region, sslCertificateResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = regionSslCertificatesClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertRegionSslCertificateRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertRegionSslCertificateRequest request, CallSettings callSettings = null)

Creates a SslCertificate resource in the specified project and region using the data included in the request

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    InsertRegionSslCertificateRequest request = new InsertRegionSslCertificateRequest
    {
        RequestId = "",
        Region = "",
        SslCertificateResource = new SslCertificate(),
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertRegionSslCertificateRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertRegionSslCertificateRequest request, CancellationToken cancellationToken)

Creates a SslCertificate resource in the specified project and region using the data included in the request

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertRegionSslCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertRegionSslCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    InsertRegionSslCertificateRequest request = new InsertRegionSslCertificateRequest
    {
        RequestId = "",
        Region = "",
        SslCertificateResource = new SslCertificate(),
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, string, SslCertificate, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, string region, SslCertificate sslCertificateResource, CallSettings callSettings = null)

Creates a SslCertificate resource in the specified project and region using the data included in the request

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificateResource` | `[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    SslCertificate sslCertificateResource = new SslCertificate();
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.InsertAsync(project, region, sslCertificateResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, string, SslCertificate, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, string region, SslCertificate sslCertificateResource, CancellationToken cancellationToken)

Creates a SslCertificate resource in the specified project and region using the data included in the request

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`sslCertificateResource` | `[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    SslCertificate sslCertificateResource = new SslCertificate();
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSslCertificatesClient.InsertAsync(project, region, sslCertificateResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSslCertificatesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### List(ListRegionSslCertificatesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SslCertificateList, SslCertificate> List(ListRegionSslCertificatesRequest request, CallSettings callSettings = null)

Retrieves the list of SslCertificate resources available to the specified project in the specified region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRegionSslCertificatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListRegionSslCertificatesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SslCertificateList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificateList)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A pageable sequence of [SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate) resources.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    ListRegionSslCertificatesRequest request = new ListRegionSslCertificatesRequest
    {
        Region = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<SslCertificateList, SslCertificate> response = regionSslCertificatesClient.List(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SslCertificate item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SslCertificateList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SslCertificate item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SslCertificate> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SslCertificate item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### List(string, string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SslCertificateList, SslCertificate> List(string project, string region, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of SslCertificate resources available to the specified project in the specified region.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SslCertificateList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificateList)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A pageable sequence of [SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate) resources.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = RegionSslCertificatesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    PagedEnumerable<SslCertificateList, SslCertificate> response = regionSslCertificatesClient.List(project, region);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SslCertificate item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SslCertificateList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SslCertificate item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SslCertificate> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SslCertificate item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(ListRegionSslCertificatesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SslCertificateList, SslCertificate> ListAsync(ListRegionSslCertificatesRequest request, CallSettings callSettings = null)

Retrieves the list of SslCertificate resources available to the specified project in the specified region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRegionSslCertificatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListRegionSslCertificatesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SslCertificateList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificateList)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A pageable asynchronous sequence of [SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate) resources.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    ListRegionSslCertificatesRequest request = new ListRegionSslCertificatesRequest
    {
        Region = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<SslCertificateList, SslCertificate> response = regionSslCertificatesClient.ListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SslCertificate item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SslCertificateList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SslCertificate item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SslCertificate> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SslCertificate item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(string, string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SslCertificateList, SslCertificate> ListAsync(string project, string region, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of SslCertificate resources available to the specified project in the specified region.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region scoping this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SslCertificateList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificateList)[SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate)` | A pageable asynchronous sequence of [SslCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificate) resources.  
**Example**
    
    
    // Create client
    RegionSslCertificatesClient regionSslCertificatesClient = await RegionSslCertificatesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    PagedAsyncEnumerable<SslCertificateList, SslCertificate> response = regionSslCertificatesClient.ListAsync(project, region);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SslCertificate item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SslCertificateList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SslCertificate item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SslCertificate> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SslCertificate item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceDelete(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceDelete(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Delete`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOnceDeleteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceDeleteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Delete` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### PollOnceInsert(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceInsert(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Insert`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOnceInsertAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceInsertAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Insert` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient#Google_Cloud_Compute_V1_RegionSslCertificatesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient#Google_Cloud_Compute_V1_RegionSslCertificatesClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient#Google_Cloud_Compute_V1_RegionSslCertificatesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient#Google_Cloud_Compute_V1_RegionSslCertificatesClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
