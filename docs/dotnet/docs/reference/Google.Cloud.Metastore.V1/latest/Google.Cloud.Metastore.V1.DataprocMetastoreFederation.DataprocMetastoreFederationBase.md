---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase
title: Dataproc Metastore v1 API - Class DataprocMetastoreFederation.DataprocMetastoreFederationBase (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:53.018214+00:00
---

# Dataproc Metastore v1 API - Class DataprocMetastoreFederation.DataprocMetastoreFederationBase (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1 API - Class DataprocMetastoreFederation.DataprocMetastoreFederationBase (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.9.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.8.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.7.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.6.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.5.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.4.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.3.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.2.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.1.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.0.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.1.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.0.0/Google.Cloud.Metastore.V1.DataprocMetastoreFederation.DataprocMetastoreFederationBase)


    
    
    [BindServiceMethod(typeof(DataprocMetastoreFederation), "BindService")]
    public abstract class DataprocMetastoreFederation.DataprocMetastoreFederationBase

Reference documentation and code samples for the Dataproc Metastore v1 API class DataprocMetastoreFederation.DataprocMetastoreFederationBase.

Base class for server-side implementations of DataprocMetastoreFederation

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataprocMetastoreFederation.DataprocMetastoreFederationBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1)

## Assembly

Google.Cloud.Metastore.V1.dll

## Methods 

### CreateFederation(CreateFederationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateFederation(CreateFederationRequest request, ServerCallContext context)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.CreateFederationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteFederation(DeleteFederationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteFederation(DeleteFederationRequest request, ServerCallContext context)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DeleteFederationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetFederation(GetFederationRequest, ServerCallContext)
    
    
    public virtual Task<Federation> GetFederation(GetFederationRequest request, ServerCallContext context)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.GetFederationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.Federation)` | The response to send back to the client (wrapped by a task).  
  
### ListFederations(ListFederationsRequest, ServerCallContext)
    
    
    public virtual Task<ListFederationsResponse> ListFederations(ListFederationsRequest request, ServerCallContext context)

Lists federations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFederationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListFederationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListFederationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListFederationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateFederation(UpdateFederationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateFederation(UpdateFederationRequest request, ServerCallContext context)

Updates the fields of a federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.UpdateFederationRequest)`  
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
