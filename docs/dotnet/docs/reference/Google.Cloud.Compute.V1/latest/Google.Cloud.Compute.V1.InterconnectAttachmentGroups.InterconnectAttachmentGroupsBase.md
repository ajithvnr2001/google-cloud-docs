---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase
title: Compute Engine v1 API - Class InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:47.851294+00:00
---

# Compute Engine v1 API - Class InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    [BindServiceMethod(typeof(InterconnectAttachmentGroups), "BindService")]
    public abstract class InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase

Reference documentation and code samples for the Compute Engine v1 API class InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase.

Base class for server-side implementations of InterconnectAttachmentGroups

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InterconnectAttachmentGroups.InterconnectAttachmentGroupsBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Methods 

### Delete(DeleteInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Delete(DeleteInterconnectAttachmentGroupRequest request, ServerCallContext context)

Deletes the specified InterconnectAttachmentGroup in the given scope

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### Get(GetInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<InterconnectAttachmentGroup> Get(GetInterconnectAttachmentGroupRequest request, ServerCallContext context)

Returns the specified InterconnectAttachmentGroup resource in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InterconnectAttachmentGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroup)` | The response to send back to the client (wrapped by a task).  
  
### GetIamPolicy(GetIamPolicyInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<Policy> GetIamPolicy(GetIamPolicyInterconnectAttachmentGroupRequest request, ServerCallContext context)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response to send back to the client (wrapped by a task).  
  
### GetOperationalStatus(GetOperationalStatusInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<InterconnectAttachmentGroupsGetOperationalStatusResponse> GetOperationalStatus(GetOperationalStatusInterconnectAttachmentGroupRequest request, ServerCallContext context)

Returns the InterconnectAttachmentStatuses for the specified InterconnectAttachmentGroup resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOperationalStatusInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetOperationalStatusInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InterconnectAttachmentGroupsGetOperationalStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroupsGetOperationalStatusResponse)` | The response to send back to the client (wrapped by a task).  
  
### Insert(InsertInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Insert(InsertInterconnectAttachmentGroupRequest request, ServerCallContext context)

Creates a InterconnectAttachmentGroup in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### List(ListInterconnectAttachmentGroupsRequest, ServerCallContext)
    
    
    public virtual Task<InterconnectAttachmentGroupsListResponse> List(ListInterconnectAttachmentGroupsRequest request, ServerCallContext context)

Lists the InterconnectAttachmentGroups for a project in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectAttachmentGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListInterconnectAttachmentGroupsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InterconnectAttachmentGroupsListResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroupsListResponse)` | The response to send back to the client (wrapped by a task).  
  
### Patch(PatchInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Patch(PatchInterconnectAttachmentGroupRequest request, ServerCallContext context)

Patches the specified InterconnectAttachmentGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetIamPolicy(SetIamPolicyInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<Policy> SetIamPolicy(SetIamPolicyInterconnectAttachmentGroupRequest request, ServerCallContext context)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response to send back to the client (wrapped by a task).  
  
### TestIamPermissions(TestIamPermissionsInterconnectAttachmentGroupRequest, ServerCallContext)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissions(TestIamPermissionsInterconnectAttachmentGroupRequest request, ServerCallContext context)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsInterconnectAttachmentGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
