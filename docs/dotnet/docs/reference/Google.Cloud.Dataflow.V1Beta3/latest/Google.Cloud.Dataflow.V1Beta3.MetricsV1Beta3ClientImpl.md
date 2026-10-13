---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3ClientImpl
title: Dataflow v1beta3 API - Class MetricsV1Beta3ClientImpl (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:18.826108+00:00
---

# Dataflow v1beta3 API - Class MetricsV1Beta3ClientImpl (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3ClientImpl

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataflow v1beta3 API - Class MetricsV1Beta3ClientImpl (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta03 
    
    
    public sealed class MetricsV1Beta3ClientImpl : MetricsV1Beta3Client

Reference documentation and code samples for the Dataflow v1beta3 API class MetricsV1Beta3ClientImpl.

MetricsV1Beta3 client wrapper implementation, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client) > MetricsV1Beta3ClientImpl

## Inherited Members

[MetricsV1Beta3Client.DefaultEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_DefaultEndpoint)

[MetricsV1Beta3Client.DefaultScopes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_DefaultScopes)

[MetricsV1Beta3Client.ServiceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_ServiceMetadata)

[MetricsV1Beta3Client.CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_CreateAsync_System_Threading_CancellationToken_)

[MetricsV1Beta3Client.Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_Create)

[MetricsV1Beta3Client.ShutdownDefaultChannelsAsync()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_ShutdownDefaultChannelsAsync)

[MetricsV1Beta3Client.GetJobMetricsAsync(GetJobMetricsRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobMetricsAsync_Google_Cloud_Dataflow_V1Beta3_GetJobMetricsRequest_System_Threading_CancellationToken_)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3)

## Assembly

Google.Cloud.Dataflow.V1Beta3.dll

## Remarks

The Dataflow Metrics API lets you monitor the progress of Dataflow jobs.

## Constructors 

### MetricsV1Beta3ClientImpl(MetricsV1Beta3Client, MetricsV1Beta3Settings, ILogger)
    
    
    public MetricsV1Beta3ClientImpl(MetricsV1Beta3.MetricsV1Beta3Client grpcClient, MetricsV1Beta3Settings settings, ILogger logger)

Constructs a client wrapper for the MetricsV1Beta3 service, with the specified gRPC client and settings.

**Parameters**  
---  
**Name** | **Description**  
`grpcClient` | `[MetricsV1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3)[MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3.MetricsV1Beta3Client)`  
The underlying gRPC client.  
`settings` | `[MetricsV1Beta3Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Settings)`  
The base [MetricsV1Beta3Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Settings) used within this client.  
`logger` | `[ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger)`  
Optional [ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger) to use within this client.  
  
## Properties 

### GrpcClient
    
    
    public override MetricsV1Beta3.MetricsV1Beta3Client GrpcClient { get; }

The underlying gRPC MetricsV1Beta3 client

**Property Value**  
---  
**Type** | **Description**  
`[MetricsV1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3)[MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3.MetricsV1Beta3Client)` |   
**Overrides**

[MetricsV1Beta3Client.GrpcClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GrpcClient)

## Methods 

### GetJobExecutionDetails(GetJobExecutionDetailsRequest, CallSettings)
    
    
    public override PagedEnumerable<JobExecutionDetails, StageSummary> GetJobExecutionDetails(GetJobExecutionDetailsRequest request, CallSettings callSettings = null)

Request detailed information about the execution status of the job.

EXPERIMENTAL. This API is subject to change or removal without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobExecutionDetailsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[JobExecutionDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobExecutionDetails)[StageSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageSummary)` | A pageable sequence of [StageSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageSummary) resources.  
**Overrides**

[MetricsV1Beta3Client.GetJobExecutionDetails(GetJobExecutionDetailsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobExecutionDetails_Google_Cloud_Dataflow_V1Beta3_GetJobExecutionDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetJobExecutionDetailsAsync(GetJobExecutionDetailsRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<JobExecutionDetails, StageSummary> GetJobExecutionDetailsAsync(GetJobExecutionDetailsRequest request, CallSettings callSettings = null)

Request detailed information about the execution status of the job.

EXPERIMENTAL. This API is subject to change or removal without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobExecutionDetailsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[JobExecutionDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobExecutionDetails)[StageSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageSummary)` | A pageable asynchronous sequence of [StageSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageSummary) resources.  
**Overrides**

[MetricsV1Beta3Client.GetJobExecutionDetailsAsync(GetJobExecutionDetailsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobExecutionDetailsAsync_Google_Cloud_Dataflow_V1Beta3_GetJobExecutionDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetJobMetrics(GetJobMetricsRequest, CallSettings)
    
    
    public override JobMetrics GetJobMetrics(GetJobMetricsRequest request, CallSettings callSettings = null)

Request the job status.

To request the status of a job, we recommend using `projects.locations.jobs.getMetrics` with a [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.getMetrics` is not recommended, as you can only request the status of jobs that are running in `us-central1`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetJobMetricsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobMetricsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[JobMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobMetrics)` | The RPC response.  
**Overrides**

[MetricsV1Beta3Client.GetJobMetrics(GetJobMetricsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobMetrics_Google_Cloud_Dataflow_V1Beta3_GetJobMetricsRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetJobMetricsAsync(GetJobMetricsRequest, CallSettings)
    
    
    public override Task<JobMetrics> GetJobMetricsAsync(GetJobMetricsRequest request, CallSettings callSettings = null)

Request the job status.

To request the status of a job, we recommend using `projects.locations.jobs.getMetrics` with a [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.getMetrics` is not recommended, as you can only request the status of jobs that are running in `us-central1`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetJobMetricsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobMetricsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[JobMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobMetrics)` | A Task containing the RPC response.  
**Overrides**

[MetricsV1Beta3Client.GetJobMetricsAsync(GetJobMetricsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobMetricsAsync_Google_Cloud_Dataflow_V1Beta3_GetJobMetricsRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetStageExecutionDetails(GetStageExecutionDetailsRequest, CallSettings)
    
    
    public override PagedEnumerable<StageExecutionDetails, WorkerDetails> GetStageExecutionDetails(GetStageExecutionDetailsRequest request, CallSettings callSettings = null)

Request detailed information about the execution status of a stage of the job.

EXPERIMENTAL. This API is subject to change or removal without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStageExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetStageExecutionDetailsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[StageExecutionDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageExecutionDetails)[WorkerDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.WorkerDetails)` | A pageable sequence of [WorkerDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.WorkerDetails) resources.  
**Overrides**

[MetricsV1Beta3Client.GetStageExecutionDetails(GetStageExecutionDetailsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetStageExecutionDetails_Google_Cloud_Dataflow_V1Beta3_GetStageExecutionDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)

### GetStageExecutionDetailsAsync(GetStageExecutionDetailsRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<StageExecutionDetails, WorkerDetails> GetStageExecutionDetailsAsync(GetStageExecutionDetailsRequest request, CallSettings callSettings = null)

Request detailed information about the execution status of a stage of the job.

EXPERIMENTAL. This API is subject to change or removal without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStageExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetStageExecutionDetailsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[StageExecutionDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageExecutionDetails)[WorkerDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.WorkerDetails)` | A pageable asynchronous sequence of [WorkerDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.WorkerDetails) resources.  
**Overrides**

[MetricsV1Beta3Client.GetStageExecutionDetailsAsync(GetStageExecutionDetailsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetStageExecutionDetailsAsync_Google_Cloud_Dataflow_V1Beta3_GetStageExecutionDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
