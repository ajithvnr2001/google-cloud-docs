---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBindings.PolicyBindingsBase
title: Identity and Access Management (IAM) v3beta API - Class PolicyBindings.PolicyBindingsBase (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:24.776733+00:00
---

# Identity and Access Management (IAM) v3beta API - Class PolicyBindings.PolicyBindingsBase (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBindings.PolicyBindingsBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3beta API - Class PolicyBindings.PolicyBindingsBase (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    [BindServiceMethod(typeof(PolicyBindings), "BindService")]
    public abstract class PolicyBindings.PolicyBindingsBase

Reference documentation and code samples for the Identity and Access Management (IAM) v3beta API class PolicyBindings.PolicyBindingsBase.

Base class for server-side implementations of PolicyBindings

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PolicyBindings.PolicyBindingsBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta)

## Assembly

Google.Cloud.Iam.V3Beta.dll

## Methods 

### CreatePolicyBinding(CreatePolicyBindingRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreatePolicyBinding(CreatePolicyBindingRequest request, ServerCallContext context)

Creates a policy binding and returns a long-running operation. Callers will need the IAM permissions on both the policy and target. After the binding is created, the policy is applied to the target.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.CreatePolicyBindingRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeletePolicyBinding(DeletePolicyBindingRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeletePolicyBinding(DeletePolicyBindingRequest request, ServerCallContext context)

Deletes a policy binding and returns a long-running operation. Callers will need the IAM permissions on both the policy and target. After the binding is deleted, the policy no longer applies to the target.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.DeletePolicyBindingRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetPolicyBinding(GetPolicyBindingRequest, ServerCallContext)
    
    
    public virtual Task<PolicyBinding> GetPolicyBinding(GetPolicyBindingRequest request, ServerCallContext context)

Gets a policy binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.GetPolicyBindingRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding)` | The response to send back to the client (wrapped by a task).  
  
### ListPolicyBindings(ListPolicyBindingsRequest, ServerCallContext)
    
    
    public virtual Task<ListPolicyBindingsResponse> ListPolicyBindings(ListPolicyBindingsRequest request, ServerCallContext context)

Lists policy bindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPolicyBindingsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPolicyBindingsResponse)` | The response to send back to the client (wrapped by a task).  
  
### SearchTargetPolicyBindings(SearchTargetPolicyBindingsRequest, ServerCallContext)
    
    
    public virtual Task<SearchTargetPolicyBindingsResponse> SearchTargetPolicyBindings(SearchTargetPolicyBindingsRequest request, ServerCallContext context)

Search policy bindings by target. Returns all policy binding objects bound directly to target.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchTargetPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchTargetPolicyBindingsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchTargetPolicyBindingsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdatePolicyBinding(UpdatePolicyBindingRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdatePolicyBinding(UpdatePolicyBindingRequest request, ServerCallContext context)

Updates a policy binding and returns a long-running operation. Callers will need the IAM permissions on the policy and target in the binding to update. Target and policy are immutable and cannot be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdatePolicyBindingRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
