---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase
title: Identity and Access Management (IAM) v3 API - Class PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:33.023114+00:00
---

# Identity and Access Management (IAM) v3 API - Class PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3 API - Class PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    [BindServiceMethod(typeof(PrincipalAccessBoundaryPolicies), "BindService")]
    public abstract class PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase

Reference documentation and code samples for the Identity and Access Management (IAM) v3 API class PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase.

Base class for server-side implementations of PrincipalAccessBoundaryPolicies

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3)

## Assembly

Google.Cloud.Iam.V3.dll

## Methods 

### CreatePrincipalAccessBoundaryPolicy(CreatePrincipalAccessBoundaryPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreatePrincipalAccessBoundaryPolicy(CreatePrincipalAccessBoundaryPolicyRequest request, ServerCallContext context)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.CreatePrincipalAccessBoundaryPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeletePrincipalAccessBoundaryPolicy(DeletePrincipalAccessBoundaryPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeletePrincipalAccessBoundaryPolicy(DeletePrincipalAccessBoundaryPolicyRequest request, ServerCallContext context)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.DeletePrincipalAccessBoundaryPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetPrincipalAccessBoundaryPolicy(GetPrincipalAccessBoundaryPolicyRequest, ServerCallContext)
    
    
    public virtual Task<PrincipalAccessBoundaryPolicy> GetPrincipalAccessBoundaryPolicy(GetPrincipalAccessBoundaryPolicyRequest request, ServerCallContext context)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PrincipalAccessBoundaryPolicy)` | The response to send back to the client (wrapped by a task).  
  
### ListPrincipalAccessBoundaryPolicies(ListPrincipalAccessBoundaryPoliciesRequest, ServerCallContext)
    
    
    public virtual Task<ListPrincipalAccessBoundaryPoliciesResponse> ListPrincipalAccessBoundaryPolicies(ListPrincipalAccessBoundaryPoliciesRequest request, ServerCallContext context)

Lists principal access boundary policies.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.ListPrincipalAccessBoundaryPoliciesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.ListPrincipalAccessBoundaryPoliciesResponse)` | The response to send back to the client (wrapped by a task).  
  
### SearchPrincipalAccessBoundaryPolicyBindings(SearchPrincipalAccessBoundaryPolicyBindingsRequest, ServerCallContext)
    
    
    public virtual Task<SearchPrincipalAccessBoundaryPolicyBindingsResponse> SearchPrincipalAccessBoundaryPolicyBindings(SearchPrincipalAccessBoundaryPolicyBindingsRequest request, ServerCallContext context)

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchPrincipalAccessBoundaryPolicyBindingsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchPrincipalAccessBoundaryPolicyBindingsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdatePrincipalAccessBoundaryPolicy(UpdatePrincipalAccessBoundaryPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdatePrincipalAccessBoundaryPolicy(UpdatePrincipalAccessBoundaryPolicyRequest request, ServerCallContext context)

Updates a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.UpdatePrincipalAccessBoundaryPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-08 UTC."],[],[]] 
