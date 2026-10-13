---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient
title: Cloud Dataplex v1 API - Class DataScanServiceClient (3.15.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:03.884220+00:00
---

# Cloud Dataplex v1 API - Class DataScanServiceClient (3.15.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Dataplex v1 API - Class DataScanServiceClient (3.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.15.0 (latest)  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public abstract class DataScanServiceClient

Reference documentation and code samples for the Cloud Dataplex v1 API class DataScanServiceClient.

DataScanService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataScanServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DataScanServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClientImpl)

## Namespace

[Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1)

## Assembly

Google.Cloud.Dataplex.V1.dll

## Remarks

DataScanService manages DataScan resources which can be configured to run various types of data scanning workload and generate enriched metadata (e.g. Data Profile, Data Quality) for the data source.

## Properties 

### CreateDataScanOperationsClient
    
    
    public virtual OperationsClient CreateDataScanOperationsClient { get; }

The long-running operations client for `CreateDataScan`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DataScanService service, which is a host of "dataplex.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DataScanService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DataScanService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/cloud-platform.read-only>
  * <https://www.googleapis.com/auth/dataplex.read-write>
  * <https://www.googleapis.com/auth/dataplex.readonly>



### DeleteDataScanOperationsClient
    
    
    public virtual OperationsClient DeleteDataScanOperationsClient { get; }

The long-running operations client for `DeleteDataScan`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual DataScanService.DataScanServiceClient GrpcClient { get; }

The underlying gRPC DataScanService client

**Property Value**  
---  
**Type** | **Description**  
`[DataScanService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanService)[DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanService.DataScanServiceClient)` |   
  
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
  
### UpdateDataScanOperationsClient
    
    
    public virtual OperationsClient UpdateDataScanOperationsClient { get; }

The long-running operations client for `UpdateDataScan`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### CancelDataScanJob(CancelDataScanJobRequest, CallSettings)
    
    
    public virtual CancelDataScanJobResponse CancelDataScanJob(CancelDataScanJobRequest request, CallSettings callSettings = null)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelDataScanJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::CancelDataScanJobRequest request = new gcdv::CancelDataScanJobRequest
    {
        DataScanJobName = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]"),
    };
    // Make the request
    gcdv::CancelDataScanJobResponse response = dataScanServiceClient.CancelDataScanJob(request);
    

### CancelDataScanJob(DataScanJobName, CallSettings)
    
    
    public virtual CancelDataScanJobResponse CancelDataScanJob(DataScanJobName name, CallSettings callSettings = null)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJobName)`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DataScanJobName name = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
    // Make the request
    gcdv::CancelDataScanJobResponse response = dataScanServiceClient.CancelDataScanJob(name);
    

### CancelDataScanJob(string, CallSettings)
    
    
    public virtual CancelDataScanJobResponse CancelDataScanJob(string name, CallSettings callSettings = null)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]/jobs/[JOB]";
    // Make the request
    gcdv::CancelDataScanJobResponse response = dataScanServiceClient.CancelDataScanJob(name);
    

### CancelDataScanJobAsync(CancelDataScanJobRequest, CallSettings)
    
    
    public virtual Task<CancelDataScanJobResponse> CancelDataScanJobAsync(CancelDataScanJobRequest request, CallSettings callSettings = null)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelDataScanJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::CancelDataScanJobRequest request = new gcdv::CancelDataScanJobRequest
    {
        DataScanJobName = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]"),
    };
    // Make the request
    gcdv::CancelDataScanJobResponse response = await dataScanServiceClient.CancelDataScanJobAsync(request);
    

### CancelDataScanJobAsync(CancelDataScanJobRequest, CancellationToken)
    
    
    public virtual Task<CancelDataScanJobResponse> CancelDataScanJobAsync(CancelDataScanJobRequest request, CancellationToken cancellationToken)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelDataScanJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::CancelDataScanJobRequest request = new gcdv::CancelDataScanJobRequest
    {
        DataScanJobName = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]"),
    };
    // Make the request
    gcdv::CancelDataScanJobResponse response = await dataScanServiceClient.CancelDataScanJobAsync(request);
    

### CancelDataScanJobAsync(DataScanJobName, CallSettings)
    
    
    public virtual Task<CancelDataScanJobResponse> CancelDataScanJobAsync(DataScanJobName name, CallSettings callSettings = null)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJobName)`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanJobName name = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
    // Make the request
    gcdv::CancelDataScanJobResponse response = await dataScanServiceClient.CancelDataScanJobAsync(name);
    

### CancelDataScanJobAsync(DataScanJobName, CancellationToken)
    
    
    public virtual Task<CancelDataScanJobResponse> CancelDataScanJobAsync(DataScanJobName name, CancellationToken cancellationToken)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJobName)`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanJobName name = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
    // Make the request
    gcdv::CancelDataScanJobResponse response = await dataScanServiceClient.CancelDataScanJobAsync(name);
    

### CancelDataScanJobAsync(string, CallSettings)
    
    
    public virtual Task<CancelDataScanJobResponse> CancelDataScanJobAsync(string name, CallSettings callSettings = null)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]/jobs/[JOB]";
    // Make the request
    gcdv::CancelDataScanJobResponse response = await dataScanServiceClient.CancelDataScanJobAsync(name);
    

### CancelDataScanJobAsync(string, CancellationToken)
    
    
    public virtual Task<CancelDataScanJobResponse> CancelDataScanJobAsync(string name, CancellationToken cancellationToken)

Cancels a running/pending DataScan job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CancelDataScanJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelDataScanJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]/jobs/[JOB]";
    // Make the request
    gcdv::CancelDataScanJobResponse response = await dataScanServiceClient.CancelDataScanJobAsync(name);
    

### Create()
    
    
    public static DataScanServiceClient Create()

Synchronously creates a [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataScanServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient)` | The created [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DataScanServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataScanServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient)` | The task representing the created [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient).  
  
### CreateDataScan(LocationName, DataScan, string, CallSettings)
    
    
    public virtual Operation<DataScan, OperationMetadata> CreateDataScan(LocationName parent, DataScan dataScan, string dataScanId, CallSettings callSettings = null)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-".

  * Must contain only lowercase letters, numbers and hyphens.
  * Must start with a letter.
  * Must end with a number or a letter.
  * Must be between 1-63 characters.
  * Must be unique within the customer project / location.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcdv::DataScan dataScan = new gcdv::DataScan();
    string dataScanId = "";
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = dataScanServiceClient.CreateDataScan(parent, dataScan, dataScanId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceCreateDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScan(CreateDataScanRequest, CallSettings)
    
    
    public virtual Operation<DataScan, OperationMetadata> CreateDataScan(CreateDataScanRequest request, CallSettings callSettings = null)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::CreateDataScanRequest request = new gcdv::CreateDataScanRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DataScan = new gcdv::DataScan(),
        DataScanId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = dataScanServiceClient.CreateDataScan(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceCreateDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScan(string, DataScan, string, CallSettings)
    
    
    public virtual Operation<DataScan, OperationMetadata> CreateDataScan(string parent, DataScan dataScan, string dataScanId, CallSettings callSettings = null)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-".

  * Must contain only lowercase letters, numbers and hyphens.
  * Must start with a letter.
  * Must end with a number or a letter.
  * Must be between 1-63 characters.
  * Must be unique within the customer project / location.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcdv::DataScan dataScan = new gcdv::DataScan();
    string dataScanId = "";
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = dataScanServiceClient.CreateDataScan(parent, dataScan, dataScanId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceCreateDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScanAsync(LocationName, DataScan, string, CallSettings)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> CreateDataScanAsync(LocationName parent, DataScan dataScan, string dataScanId, CallSettings callSettings = null)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-".

  * Must contain only lowercase letters, numbers and hyphens.
  * Must start with a letter.
  * Must end with a number or a letter.
  * Must be between 1-63 characters.
  * Must be unique within the customer project / location.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcdv::DataScan dataScan = new gcdv::DataScan();
    string dataScanId = "";
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.CreateDataScanAsync(parent, dataScan, dataScanId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceCreateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScanAsync(LocationName, DataScan, string, CancellationToken)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> CreateDataScanAsync(LocationName parent, DataScan dataScan, string dataScanId, CancellationToken cancellationToken)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-".

  * Must contain only lowercase letters, numbers and hyphens.
  * Must start with a letter.
  * Must end with a number or a letter.
  * Must be between 1-63 characters.
  * Must be unique within the customer project / location.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcdv::DataScan dataScan = new gcdv::DataScan();
    string dataScanId = "";
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.CreateDataScanAsync(parent, dataScan, dataScanId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceCreateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScanAsync(CreateDataScanRequest, CallSettings)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> CreateDataScanAsync(CreateDataScanRequest request, CallSettings callSettings = null)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::CreateDataScanRequest request = new gcdv::CreateDataScanRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DataScan = new gcdv::DataScan(),
        DataScanId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.CreateDataScanAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceCreateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScanAsync(CreateDataScanRequest, CancellationToken)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> CreateDataScanAsync(CreateDataScanRequest request, CancellationToken cancellationToken)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::CreateDataScanRequest request = new gcdv::CreateDataScanRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DataScan = new gcdv::DataScan(),
        DataScanId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.CreateDataScanAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceCreateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScanAsync(string, DataScan, string, CallSettings)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> CreateDataScanAsync(string parent, DataScan dataScan, string dataScanId, CallSettings callSettings = null)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-".

  * Must contain only lowercase letters, numbers and hyphens.
  * Must start with a letter.
  * Must end with a number or a letter.
  * Must be between 1-63 characters.
  * Must be unique within the customer project / location.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcdv::DataScan dataScan = new gcdv::DataScan();
    string dataScanId = "";
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.CreateDataScanAsync(parent, dataScan, dataScanId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceCreateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataScanAsync(string, DataScan, string, CancellationToken)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> CreateDataScanAsync(string parent, DataScan dataScan, string dataScanId, CancellationToken cancellationToken)

Creates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-".

  * Must contain only lowercase letters, numbers and hyphens.
  * Must start with a letter.
  * Must end with a number or a letter.
  * Must be between 1-63 characters.
  * Must be unique within the customer project / location.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcdv::DataScan dataScan = new gcdv::DataScan();
    string dataScanId = "";
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.CreateDataScanAsync(parent, dataScan, dataScanId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceCreateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScan(DataScanName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDataScan(DataScanName name, CallSettings callSettings = null)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = dataScanServiceClient.DeleteDataScan(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceDeleteDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScan(DeleteDataScanRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDataScan(DeleteDataScanRequest request, CallSettings callSettings = null)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DeleteDataScanRequest request = new gcdv::DeleteDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = dataScanServiceClient.DeleteDataScan(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceDeleteDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScan(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDataScan(string name, CallSettings callSettings = null)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = dataScanServiceClient.DeleteDataScan(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceDeleteDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScanAsync(DataScanName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDataScanAsync(DataScanName name, CallSettings callSettings = null)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = await dataScanServiceClient.DeleteDataScanAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceDeleteDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScanAsync(DataScanName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDataScanAsync(DataScanName name, CancellationToken cancellationToken)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = await dataScanServiceClient.DeleteDataScanAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceDeleteDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScanAsync(DeleteDataScanRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDataScanAsync(DeleteDataScanRequest request, CallSettings callSettings = null)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DeleteDataScanRequest request = new gcdv::DeleteDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = await dataScanServiceClient.DeleteDataScanAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceDeleteDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScanAsync(DeleteDataScanRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDataScanAsync(DeleteDataScanRequest request, CancellationToken cancellationToken)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DeleteDataScanRequest request = new gcdv::DeleteDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = await dataScanServiceClient.DeleteDataScanAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceDeleteDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScanAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDataScanAsync(string name, CallSettings callSettings = null)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = await dataScanServiceClient.DeleteDataScanAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceDeleteDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDataScanAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDataScanAsync(string name, CancellationToken cancellationToken)

Deletes a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    Operation<Empty, gcdv::OperationMetadata> response = await dataScanServiceClient.DeleteDataScanAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceDeleteDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GenerateDataQualityRules(GenerateDataQualityRulesRequest, CallSettings)
    
    
    public virtual GenerateDataQualityRulesResponse GenerateDataQualityRules(GenerateDataQualityRulesRequest request, CallSettings callSettings = null)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDataQualityRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::GenerateDataQualityRulesRequest request = new gcdv::GenerateDataQualityRulesRequest { Name = "", };
    // Make the request
    gcdv::GenerateDataQualityRulesResponse response = dataScanServiceClient.GenerateDataQualityRules(request);
    

### GenerateDataQualityRules(string, CallSettings)
    
    
    public virtual GenerateDataQualityRulesResponse GenerateDataQualityRules(string name, CallSettings callSettings = null)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name must be one of the following:

  * The name of a data scan with at least one successful, completed data profiling job
  * The name of a successful, completed data profiling job (a data scan job where the job type is data profiling)

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcdv::GenerateDataQualityRulesResponse response = dataScanServiceClient.GenerateDataQualityRules(name);
    

### GenerateDataQualityRulesAsync(GenerateDataQualityRulesRequest, CallSettings)
    
    
    public virtual Task<GenerateDataQualityRulesResponse> GenerateDataQualityRulesAsync(GenerateDataQualityRulesRequest request, CallSettings callSettings = null)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDataQualityRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::GenerateDataQualityRulesRequest request = new gcdv::GenerateDataQualityRulesRequest { Name = "", };
    // Make the request
    gcdv::GenerateDataQualityRulesResponse response = await dataScanServiceClient.GenerateDataQualityRulesAsync(request);
    

### GenerateDataQualityRulesAsync(GenerateDataQualityRulesRequest, CancellationToken)
    
    
    public virtual Task<GenerateDataQualityRulesResponse> GenerateDataQualityRulesAsync(GenerateDataQualityRulesRequest request, CancellationToken cancellationToken)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDataQualityRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::GenerateDataQualityRulesRequest request = new gcdv::GenerateDataQualityRulesRequest { Name = "", };
    // Make the request
    gcdv::GenerateDataQualityRulesResponse response = await dataScanServiceClient.GenerateDataQualityRulesAsync(request);
    

### GenerateDataQualityRulesAsync(string, CallSettings)
    
    
    public virtual Task<GenerateDataQualityRulesResponse> GenerateDataQualityRulesAsync(string name, CallSettings callSettings = null)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name must be one of the following:

  * The name of a data scan with at least one successful, completed data profiling job
  * The name of a successful, completed data profiling job (a data scan job where the job type is data profiling)

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcdv::GenerateDataQualityRulesResponse response = await dataScanServiceClient.GenerateDataQualityRulesAsync(name);
    

### GenerateDataQualityRulesAsync(string, CancellationToken)
    
    
    public virtual Task<GenerateDataQualityRulesResponse> GenerateDataQualityRulesAsync(string name, CancellationToken cancellationToken)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name must be one of the following:

  * The name of a data scan with at least one successful, completed data profiling job
  * The name of a successful, completed data profiling job (a data scan job where the job type is data profiling)

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GenerateDataQualityRulesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcdv::GenerateDataQualityRulesResponse response = await dataScanServiceClient.GenerateDataQualityRulesAsync(name);
    

### GetDataScan(DataScanName, CallSettings)
    
    
    public virtual DataScan GetDataScan(DataScanName name, CallSettings callSettings = null)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    gcdv::DataScan response = dataScanServiceClient.GetDataScan(name);
    

### GetDataScan(GetDataScanRequest, CallSettings)
    
    
    public virtual DataScan GetDataScan(GetDataScanRequest request, CallSettings callSettings = null)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::GetDataScanRequest request = new gcdv::GetDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        View = gcdv::GetDataScanRequest.Types.DataScanView.Unspecified,
    };
    // Make the request
    gcdv::DataScan response = dataScanServiceClient.GetDataScan(request);
    

### GetDataScan(string, CallSettings)
    
    
    public virtual DataScan GetDataScan(string name, CallSettings callSettings = null)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    gcdv::DataScan response = dataScanServiceClient.GetDataScan(name);
    

### GetDataScanAsync(DataScanName, CallSettings)
    
    
    public virtual Task<DataScan> GetDataScanAsync(DataScanName name, CallSettings callSettings = null)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    gcdv::DataScan response = await dataScanServiceClient.GetDataScanAsync(name);
    

### GetDataScanAsync(DataScanName, CancellationToken)
    
    
    public virtual Task<DataScan> GetDataScanAsync(DataScanName name, CancellationToken cancellationToken)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    gcdv::DataScan response = await dataScanServiceClient.GetDataScanAsync(name);
    

### GetDataScanAsync(GetDataScanRequest, CallSettings)
    
    
    public virtual Task<DataScan> GetDataScanAsync(GetDataScanRequest request, CallSettings callSettings = null)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::GetDataScanRequest request = new gcdv::GetDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        View = gcdv::GetDataScanRequest.Types.DataScanView.Unspecified,
    };
    // Make the request
    gcdv::DataScan response = await dataScanServiceClient.GetDataScanAsync(request);
    

### GetDataScanAsync(GetDataScanRequest, CancellationToken)
    
    
    public virtual Task<DataScan> GetDataScanAsync(GetDataScanRequest request, CancellationToken cancellationToken)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::GetDataScanRequest request = new gcdv::GetDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        View = gcdv::GetDataScanRequest.Types.DataScanView.Unspecified,
    };
    // Make the request
    gcdv::DataScan response = await dataScanServiceClient.GetDataScanAsync(request);
    

### GetDataScanAsync(string, CallSettings)
    
    
    public virtual Task<DataScan> GetDataScanAsync(string name, CallSettings callSettings = null)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    gcdv::DataScan response = await dataScanServiceClient.GetDataScanAsync(name);
    

### GetDataScanAsync(string, CancellationToken)
    
    
    public virtual Task<DataScan> GetDataScanAsync(string name, CancellationToken cancellationToken)

Gets a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    gcdv::DataScan response = await dataScanServiceClient.GetDataScanAsync(name);
    

### GetDataScanJob(DataScanJobName, CallSettings)
    
    
    public virtual DataScanJob GetDataScanJob(DataScanJobName name, CallSettings callSettings = null)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJobName)`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DataScanJobName name = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
    // Make the request
    gcdv::DataScanJob response = dataScanServiceClient.GetDataScanJob(name);
    

### GetDataScanJob(GetDataScanJobRequest, CallSettings)
    
    
    public virtual DataScanJob GetDataScanJob(GetDataScanJobRequest request, CallSettings callSettings = null)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataScanJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::GetDataScanJobRequest request = new gcdv::GetDataScanJobRequest
    {
        DataScanJobName = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]"),
        View = gcdv::GetDataScanJobRequest.Types.DataScanJobView.Unspecified,
    };
    // Make the request
    gcdv::DataScanJob response = dataScanServiceClient.GetDataScanJob(request);
    

### GetDataScanJob(string, CallSettings)
    
    
    public virtual DataScanJob GetDataScanJob(string name, CallSettings callSettings = null)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]/jobs/[JOB]";
    // Make the request
    gcdv::DataScanJob response = dataScanServiceClient.GetDataScanJob(name);
    

### GetDataScanJobAsync(DataScanJobName, CallSettings)
    
    
    public virtual Task<DataScanJob> GetDataScanJobAsync(DataScanJobName name, CallSettings callSettings = null)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJobName)`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanJobName name = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
    // Make the request
    gcdv::DataScanJob response = await dataScanServiceClient.GetDataScanJobAsync(name);
    

### GetDataScanJobAsync(DataScanJobName, CancellationToken)
    
    
    public virtual Task<DataScanJob> GetDataScanJobAsync(DataScanJobName name, CancellationToken cancellationToken)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJobName)`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanJobName name = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
    // Make the request
    gcdv::DataScanJob response = await dataScanServiceClient.GetDataScanJobAsync(name);
    

### GetDataScanJobAsync(GetDataScanJobRequest, CallSettings)
    
    
    public virtual Task<DataScanJob> GetDataScanJobAsync(GetDataScanJobRequest request, CallSettings callSettings = null)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataScanJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::GetDataScanJobRequest request = new gcdv::GetDataScanJobRequest
    {
        DataScanJobName = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]"),
        View = gcdv::GetDataScanJobRequest.Types.DataScanJobView.Unspecified,
    };
    // Make the request
    gcdv::DataScanJob response = await dataScanServiceClient.GetDataScanJobAsync(request);
    

### GetDataScanJobAsync(GetDataScanJobRequest, CancellationToken)
    
    
    public virtual Task<DataScanJob> GetDataScanJobAsync(GetDataScanJobRequest request, CancellationToken cancellationToken)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataScanJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::GetDataScanJobRequest request = new gcdv::GetDataScanJobRequest
    {
        DataScanJobName = gcdv::DataScanJobName.FromProjectLocationDataScanJob("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]"),
        View = gcdv::GetDataScanJobRequest.Types.DataScanJobView.Unspecified,
    };
    // Make the request
    gcdv::DataScanJob response = await dataScanServiceClient.GetDataScanJobAsync(request);
    

### GetDataScanJobAsync(string, CallSettings)
    
    
    public virtual Task<DataScanJob> GetDataScanJobAsync(string name, CallSettings callSettings = null)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]/jobs/[JOB]";
    // Make the request
    gcdv::DataScanJob response = await dataScanServiceClient.GetDataScanJobAsync(name);
    

### GetDataScanJobAsync(string, CancellationToken)
    
    
    public virtual Task<DataScanJob> GetDataScanJobAsync(string name, CancellationToken cancellationToken)

Gets a DataScanJob resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]/jobs/[JOB]";
    // Make the request
    gcdv::DataScanJob response = await dataScanServiceClient.GetDataScanJobAsync(name);
    

### ListDataScanJobs(DataScanName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataScanJobsResponse, DataScanJob> ListDataScanJobs(DataScanName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScanJobs under the given DataScan.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the parent environment: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataScanJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsResponse)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A pageable sequence of [DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DataScanName parent = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    PagedEnumerable<gcdv::ListDataScanJobsResponse, gcdv::DataScanJob> response = dataScanServiceClient.ListDataScanJobs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcdv::DataScanJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcdv::ListDataScanJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScanJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScanJob> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScanJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScanJobs(ListDataScanJobsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataScanJobsResponse, DataScanJob> ListDataScanJobs(ListDataScanJobsRequest request, CallSettings callSettings = null)

Lists DataScanJobs under the given DataScan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataScanJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataScanJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsResponse)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A pageable sequence of [DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::ListDataScanJobsRequest request = new gcdv::ListDataScanJobsRequest
    {
        ParentAsDataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcdv::ListDataScanJobsResponse, gcdv::DataScanJob> response = dataScanServiceClient.ListDataScanJobs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcdv::DataScanJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcdv::ListDataScanJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScanJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScanJob> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScanJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScanJobs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataScanJobsResponse, DataScanJob> ListDataScanJobs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScanJobs under the given DataScan.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the parent environment: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataScanJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsResponse)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A pageable sequence of [DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    PagedEnumerable<gcdv::ListDataScanJobsResponse, gcdv::DataScanJob> response = dataScanServiceClient.ListDataScanJobs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcdv::DataScanJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcdv::ListDataScanJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScanJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScanJob> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScanJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScanJobsAsync(DataScanName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataScanJobsResponse, DataScanJob> ListDataScanJobsAsync(DataScanName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScanJobs under the given DataScan.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the parent environment: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataScanJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsResponse)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A pageable asynchronous sequence of [DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanName parent = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    PagedAsyncEnumerable<gcdv::ListDataScanJobsResponse, gcdv::DataScanJob> response = dataScanServiceClient.ListDataScanJobsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcdv::DataScanJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcdv::ListDataScanJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScanJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScanJob> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScanJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScanJobsAsync(ListDataScanJobsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataScanJobsResponse, DataScanJob> ListDataScanJobsAsync(ListDataScanJobsRequest request, CallSettings callSettings = null)

Lists DataScanJobs under the given DataScan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataScanJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataScanJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsResponse)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A pageable asynchronous sequence of [DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::ListDataScanJobsRequest request = new gcdv::ListDataScanJobsRequest
    {
        ParentAsDataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcdv::ListDataScanJobsResponse, gcdv::DataScanJob> response = dataScanServiceClient.ListDataScanJobsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcdv::DataScanJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcdv::ListDataScanJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScanJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScanJob> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScanJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScanJobsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataScanJobsResponse, DataScanJob> ListDataScanJobsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScanJobs under the given DataScan.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the parent environment: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataScanJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsResponse)[DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob)` | A pageable asynchronous sequence of [DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    PagedAsyncEnumerable<gcdv::ListDataScanJobsResponse, gcdv::DataScanJob> response = dataScanServiceClient.ListDataScanJobsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcdv::DataScanJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcdv::ListDataScanJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScanJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScanJob> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScanJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScans(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataScansResponse, DataScan> ListDataScans(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScans.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataScansResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansResponse)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A pageable sequence of [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<gcdv::ListDataScansResponse, gcdv::DataScan> response = dataScanServiceClient.ListDataScans(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcdv::DataScan item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcdv::ListDataScansResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScan item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScan> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScan item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScans(ListDataScansRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataScansResponse, DataScan> ListDataScans(ListDataScansRequest request, CallSettings callSettings = null)

Lists DataScans.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataScansRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataScansResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansResponse)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A pageable sequence of [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::ListDataScansRequest request = new gcdv::ListDataScansRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<gcdv::ListDataScansResponse, gcdv::DataScan> response = dataScanServiceClient.ListDataScans(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcdv::DataScan item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcdv::ListDataScansResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScan item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScan> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScan item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScans(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataScansResponse, DataScan> ListDataScans(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScans.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataScansResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansResponse)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A pageable sequence of [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<gcdv::ListDataScansResponse, gcdv::DataScan> response = dataScanServiceClient.ListDataScans(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcdv::DataScan item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcdv::ListDataScansResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScan item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScan> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScan item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScansAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataScansResponse, DataScan> ListDataScansAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScans.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataScansResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansResponse)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A pageable asynchronous sequence of [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<gcdv::ListDataScansResponse, gcdv::DataScan> response = dataScanServiceClient.ListDataScansAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcdv::DataScan item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcdv::ListDataScansResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScan item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScan> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScan item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScansAsync(ListDataScansRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataScansResponse, DataScan> ListDataScansAsync(ListDataScansRequest request, CallSettings callSettings = null)

Lists DataScans.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataScansRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataScansResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansResponse)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A pageable asynchronous sequence of [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::ListDataScansRequest request = new gcdv::ListDataScansRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcdv::ListDataScansResponse, gcdv::DataScan> response = dataScanServiceClient.ListDataScansAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcdv::DataScan item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcdv::ListDataScansResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScan item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScan> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScan item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataScansAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataScansResponse, DataScan> ListDataScansAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists DataScans.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataScansResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScansResponse)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)` | A pageable asynchronous sequence of [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan) resources.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<gcdv::ListDataScansResponse, gcdv::DataScan> response = dataScanServiceClient.ListDataScansAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcdv::DataScan item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcdv::ListDataScansResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcdv::DataScan item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcdv::DataScan> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcdv::DataScan item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateDataScan(string, CallSettings)
    
    
    public virtual Operation<DataScan, OperationMetadata> PollOnceCreateDataScan(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateDataScan`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateDataScanAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> PollOnceCreateDataScanAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateDataScan`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteDataScan(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteDataScan(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteDataScan`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteDataScanAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteDataScanAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteDataScan`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateDataScan(string, CallSettings)
    
    
    public virtual Operation<DataScan, OperationMetadata> PollOnceUpdateDataScan(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateDataScan`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateDataScanAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> PollOnceUpdateDataScanAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateDataScan`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RunDataScan(DataScanName, CallSettings)
    
    
    public virtual RunDataScanResponse RunDataScan(DataScanName name, CallSettings callSettings = null)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    gcdv::RunDataScanResponse response = dataScanServiceClient.RunDataScan(name);
    

### RunDataScan(RunDataScanRequest, CallSettings)
    
    
    public virtual RunDataScanResponse RunDataScan(RunDataScanRequest request, CallSettings callSettings = null)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::RunDataScanRequest request = new gcdv::RunDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
    };
    // Make the request
    gcdv::RunDataScanResponse response = dataScanServiceClient.RunDataScan(request);
    

### RunDataScan(string, CallSettings)
    
    
    public virtual RunDataScanResponse RunDataScan(string name, CallSettings callSettings = null)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    gcdv::RunDataScanResponse response = dataScanServiceClient.RunDataScan(name);
    

### RunDataScanAsync(DataScanName, CallSettings)
    
    
    public virtual Task<RunDataScanResponse> RunDataScanAsync(DataScanName name, CallSettings callSettings = null)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    gcdv::RunDataScanResponse response = await dataScanServiceClient.RunDataScanAsync(name);
    

### RunDataScanAsync(DataScanName, CancellationToken)
    
    
    public virtual Task<RunDataScanResponse> RunDataScanAsync(DataScanName name, CancellationToken cancellationToken)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName)`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScanName name = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]");
    // Make the request
    gcdv::RunDataScanResponse response = await dataScanServiceClient.RunDataScanAsync(name);
    

### RunDataScanAsync(RunDataScanRequest, CallSettings)
    
    
    public virtual Task<RunDataScanResponse> RunDataScanAsync(RunDataScanRequest request, CallSettings callSettings = null)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::RunDataScanRequest request = new gcdv::RunDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
    };
    // Make the request
    gcdv::RunDataScanResponse response = await dataScanServiceClient.RunDataScanAsync(request);
    

### RunDataScanAsync(RunDataScanRequest, CancellationToken)
    
    
    public virtual Task<RunDataScanResponse> RunDataScanAsync(RunDataScanRequest request, CancellationToken cancellationToken)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::RunDataScanRequest request = new gcdv::RunDataScanRequest
    {
        DataScanName = gcdv::DataScanName.FromProjectLocationDataScan("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
    };
    // Make the request
    gcdv::RunDataScanResponse response = await dataScanServiceClient.RunDataScanAsync(request);
    

### RunDataScanAsync(string, CallSettings)
    
    
    public virtual Task<RunDataScanResponse> RunDataScanAsync(string name, CallSettings callSettings = null)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    gcdv::RunDataScanResponse response = await dataScanServiceClient.RunDataScanAsync(name);
    

### RunDataScanAsync(string, CancellationToken)
    
    
    public virtual Task<RunDataScanResponse> RunDataScanAsync(string name, CancellationToken cancellationToken)

Runs an on-demand execution of a DataScan

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataScans/[DATASCAN]";
    // Make the request
    gcdv::RunDataScanResponse response = await dataScanServiceClient.RunDataScanAsync(name);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient#Google_Cloud_Dataplex_V1_DataScanServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient#Google_Cloud_Dataplex_V1_DataScanServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateDataScan(DataScan, FieldMask, CallSettings)
    
    
    public virtual Operation<DataScan, OperationMetadata> UpdateDataScan(DataScan dataScan, FieldMask updateMask, CallSettings callSettings = null)

Updates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource to be updated. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Mask of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::DataScan dataScan = new gcdv::DataScan();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = dataScanServiceClient.UpdateDataScan(dataScan, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceUpdateDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDataScan(UpdateDataScanRequest, CallSettings)
    
    
    public virtual Operation<DataScan, OperationMetadata> UpdateDataScan(UpdateDataScanRequest request, CallSettings callSettings = null)

Updates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = gcdv::DataScanServiceClient.Create();
    // Initialize request argument(s)
    gcdv::UpdateDataScanRequest request = new gcdv::UpdateDataScanRequest
    {
        DataScan = new gcdv::DataScan(),
        UpdateMask = new FieldMask(),
        ValidateOnly = false,
    };
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = dataScanServiceClient.UpdateDataScan(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = dataScanServiceClient.PollOnceUpdateDataScan(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDataScanAsync(DataScan, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> UpdateDataScanAsync(DataScan dataScan, FieldMask updateMask, CallSettings callSettings = null)

Updates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource to be updated. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Mask of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScan dataScan = new gcdv::DataScan();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.UpdateDataScanAsync(dataScan, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceUpdateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDataScanAsync(DataScan, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> UpdateDataScanAsync(DataScan dataScan, FieldMask updateMask, CancellationToken cancellationToken)

Updates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`dataScan` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)`  
Required. DataScan resource to be updated. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Mask of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::DataScan dataScan = new gcdv::DataScan();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.UpdateDataScanAsync(dataScan, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceUpdateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDataScanAsync(UpdateDataScanRequest, CallSettings)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> UpdateDataScanAsync(UpdateDataScanRequest request, CallSettings callSettings = null)

Updates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::UpdateDataScanRequest request = new gcdv::UpdateDataScanRequest
    {
        DataScan = new gcdv::DataScan(),
        UpdateMask = new FieldMask(),
        ValidateOnly = false,
    };
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.UpdateDataScanAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceUpdateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDataScanAsync(UpdateDataScanRequest, CancellationToken)
    
    
    public virtual Task<Operation<DataScan, OperationMetadata>> UpdateDataScanAsync(UpdateDataScanRequest request, CancellationToken cancellationToken)

Updates a DataScan resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcdv::DataScanServiceClient dataScanServiceClient = await gcdv::DataScanServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcdv::UpdateDataScanRequest request = new gcdv::UpdateDataScanRequest
    {
        DataScan = new gcdv::DataScan(),
        UpdateMask = new FieldMask(),
        ValidateOnly = false,
    };
    // Make the request
    Operation<gcdv::DataScan, gcdv::OperationMetadata> response = await dataScanServiceClient.UpdateDataScanAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcdv::DataScan, gcdv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcdv::DataScan result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcdv::DataScan, gcdv::OperationMetadata> retrievedResponse = await dataScanServiceClient.PollOnceUpdateDataScanAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcdv::DataScan retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
