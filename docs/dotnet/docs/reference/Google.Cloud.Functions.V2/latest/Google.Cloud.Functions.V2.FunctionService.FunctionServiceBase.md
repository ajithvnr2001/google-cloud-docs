---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase
title: Cloud Functions v2 API - Class FunctionService.FunctionServiceBase (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:43.045721+00:00
---

# Cloud Functions v2 API - Class FunctionService.FunctionServiceBase (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2 API - Class FunctionService.FunctionServiceBase (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.7.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.6.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.5.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.4.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.3.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.2.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.1.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.0.0/Google.Cloud.Functions.V2.FunctionService.FunctionServiceBase)


    
    
    [BindServiceMethod(typeof(FunctionService), "BindService")]
    public abstract class FunctionService.FunctionServiceBase

Reference documentation and code samples for the Cloud Functions v2 API class FunctionService.FunctionServiceBase.

Base class for server-side implementations of FunctionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FunctionService.FunctionServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2)

## Assembly

Google.Cloud.Functions.V2.dll

## Methods 

### CreateFunction(CreateFunctionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateFunction(CreateFunctionRequest request, ServerCallContext context)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.CreateFunctionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteFunction(DeleteFunctionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteFunction(DeleteFunctionRequest request, ServerCallContext context)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.DeleteFunctionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GenerateDownloadUrl(GenerateDownloadUrlRequest, ServerCallContext)
    
    
    public virtual Task<GenerateDownloadUrlResponse> GenerateDownloadUrl(GenerateDownloadUrlRequest request, ServerCallContext context)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlResponse)` | The response to send back to the client (wrapped by a task).  
  
### GenerateUploadUrl(GenerateUploadUrlRequest, ServerCallContext)
    
    
    public virtual Task<GenerateUploadUrlResponse> GenerateUploadUrl(GenerateUploadUrlRequest request, ServerCallContext context)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlResponse)` | The response to send back to the client (wrapped by a task).  
  
### GetFunction(GetFunctionRequest, ServerCallContext)
    
    
    public virtual Task<Function> GetFunction(GetFunctionRequest request, ServerCallContext context)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GetFunctionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | The response to send back to the client (wrapped by a task).  
  
### ListFunctions(ListFunctionsRequest, ServerCallContext)
    
    
    public virtual Task<ListFunctionsResponse> ListFunctions(ListFunctionsRequest request, ServerCallContext context)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListRuntimes(ListRuntimesRequest, ServerCallContext)
    
    
    public virtual Task<ListRuntimesResponse> ListRuntimes(ListRuntimesRequest request, ServerCallContext context)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateFunction(UpdateFunctionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateFunction(UpdateFunctionRequest request, ServerCallContext context)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.UpdateFunctionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
