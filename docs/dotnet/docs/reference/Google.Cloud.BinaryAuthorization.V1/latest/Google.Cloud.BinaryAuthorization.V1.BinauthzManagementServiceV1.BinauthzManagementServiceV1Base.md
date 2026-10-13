---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1.BinauthzManagementServiceV1Base
title: Binary Authorization v1 API - Class BinauthzManagementServiceV1.BinauthzManagementServiceV1Base (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:53.890794+00:00
---

# Binary Authorization v1 API - Class BinauthzManagementServiceV1.BinauthzManagementServiceV1Base (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1.BinauthzManagementServiceV1Base

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1 API - Class BinauthzManagementServiceV1.BinauthzManagementServiceV1Base (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.0 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    [BindServiceMethod(typeof(BinauthzManagementServiceV1), "BindService")]
    public abstract class BinauthzManagementServiceV1.BinauthzManagementServiceV1Base

Reference documentation and code samples for the Binary Authorization v1 API class BinauthzManagementServiceV1.BinauthzManagementServiceV1Base.

Base class for server-side implementations of BinauthzManagementServiceV1

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BinauthzManagementServiceV1.BinauthzManagementServiceV1Base

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1)

## Assembly

Google.Cloud.BinaryAuthorization.V1.dll

## Methods 

### CreateAttestor(CreateAttestorRequest, ServerCallContext)
    
    
    public virtual Task<Attestor> CreateAttestor(CreateAttestorRequest request, ServerCallContext context)

Creates an [attestor][google.cloud.binaryauthorization.v1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1.Attestor]. Returns `NOT_FOUND` if the project does not exist, `INVALID_ARGUMENT` if the request is malformed, `ALREADY_EXISTS` if the [attestor][google.cloud.binaryauthorization.v1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.CreateAttestorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAttestor(DeleteAttestorRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteAttestor(DeleteAttestorRequest request, ServerCallContext context)

Deletes an [attestor][google.cloud.binaryauthorization.v1.Attestor]. Returns `NOT_FOUND` if the [attestor][google.cloud.binaryauthorization.v1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.DeleteAttestorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetAttestor(GetAttestorRequest, ServerCallContext)
    
    
    public virtual Task<Attestor> GetAttestor(GetAttestorRequest request, ServerCallContext context)

Gets an [attestor][google.cloud.binaryauthorization.v1.Attestor]. Returns `NOT_FOUND` if the [attestor][google.cloud.binaryauthorization.v1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.GetAttestorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor)` | The response to send back to the client (wrapped by a task).  
  
### GetPolicy(GetPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Policy> GetPolicy(GetPolicyRequest request, ServerCallContext context)

A [policy][google.cloud.binaryauthorization.v1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.GetPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Policy)` | The response to send back to the client (wrapped by a task).  
  
### ListAttestors(ListAttestorsRequest, ServerCallContext)
    
    
    public virtual Task<ListAttestorsResponse> ListAttestors(ListAttestorsRequest request, ServerCallContext context)

Lists [attestors][google.cloud.binaryauthorization.v1.Attestor]. Returns `INVALID_ARGUMENT` if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateAttestor(UpdateAttestorRequest, ServerCallContext)
    
    
    public virtual Task<Attestor> UpdateAttestor(UpdateAttestorRequest request, ServerCallContext context)

Updates an [attestor][google.cloud.binaryauthorization.v1.Attestor]. Returns `NOT_FOUND` if the [attestor][google.cloud.binaryauthorization.v1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.UpdateAttestorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor)` | The response to send back to the client (wrapped by a task).  
  
### UpdatePolicy(UpdatePolicyRequest, ServerCallContext)
    
    
    public virtual Task<Policy> UpdatePolicy(UpdatePolicyRequest request, ServerCallContext context)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns `NOT_FOUND` if the project does not exist, `INVALID_ARGUMENT` if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.UpdatePolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Policy)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
