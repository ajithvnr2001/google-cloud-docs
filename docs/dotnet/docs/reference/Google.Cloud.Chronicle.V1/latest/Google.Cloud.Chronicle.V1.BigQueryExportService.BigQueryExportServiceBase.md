---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceBase
title: Chronicle v1 API - Class BigQueryExportService.BigQueryExportServiceBase (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:41.325320+00:00
---

# Chronicle v1 API - Class BigQueryExportService.BigQueryExportServiceBase (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class BigQueryExportService.BigQueryExportServiceBase (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    [BindServiceMethod(typeof(BigQueryExportService), "BindService")]
    public abstract class BigQueryExportService.BigQueryExportServiceBase

Reference documentation and code samples for the Chronicle v1 API class BigQueryExportService.BigQueryExportServiceBase.

Base class for server-side implementations of BigQueryExportService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigQueryExportService.BigQueryExportServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Methods 

### GetBigQueryExport(GetBigQueryExportRequest, ServerCallContext)
    
    
    public virtual Task<BigQueryExport> GetBigQueryExport(GetBigQueryExportRequest request, ServerCallContext context)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response to send back to the client (wrapped by a task).  
  
### ProvisionBigQueryExport(ProvisionBigQueryExportRequest, ServerCallContext)
    
    
    public virtual Task<BigQueryExport> ProvisionBigQueryExport(ProvisionBigQueryExportRequest request, ServerCallContext context)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response to send back to the client (wrapped by a task).  
  
### UpdateBigQueryExport(UpdateBigQueryExportRequest, ServerCallContext)
    
    
    public virtual Task<BigQueryExport> UpdateBigQueryExport(UpdateBigQueryExportRequest request, ServerCallContext context)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
