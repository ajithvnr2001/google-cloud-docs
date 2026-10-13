---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase
title: Compute Engine v1 API - Class ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:22.190629+00:00
---

# Compute Engine v1 API - Class ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    [BindServiceMethod(typeof(ZoneVmExtensionPolicies), "BindService")]
    public abstract class ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase

Reference documentation and code samples for the Compute Engine v1 API class ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase.

Base class for server-side implementations of ZoneVmExtensionPolicies

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ZoneVmExtensionPolicies.ZoneVmExtensionPoliciesBase

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

### Delete(DeleteZoneVmExtensionPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Delete(DeleteZoneVmExtensionPolicyRequest request, ServerCallContext context)

Deletes a specified zone VM extension policy within a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteZoneVmExtensionPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### Get(GetZoneVmExtensionPolicyRequest, ServerCallContext)
    
    
    public virtual Task<VmExtensionPolicy> Get(GetZoneVmExtensionPolicyRequest request, ServerCallContext context)

Retrieves details of a specific zone VM extension policy within a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetZoneVmExtensionPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VmExtensionPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VmExtensionPolicy)` | The response to send back to the client (wrapped by a task).  
  
### Insert(InsertZoneVmExtensionPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Insert(InsertZoneVmExtensionPolicyRequest request, ServerCallContext context)

Creates a new zone-level VM extension policy within a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertZoneVmExtensionPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### List(ListZoneVmExtensionPoliciesRequest, ServerCallContext)
    
    
    public virtual Task<VmExtensionPolicyList> List(ListZoneVmExtensionPoliciesRequest request, ServerCallContext context)

Lists all VM extension policies within a specific zone for a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListZoneVmExtensionPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListZoneVmExtensionPoliciesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VmExtensionPolicyList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VmExtensionPolicyList)` | The response to send back to the client (wrapped by a task).  
  
### Update(UpdateZoneVmExtensionPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Update(UpdateZoneVmExtensionPolicyRequest request, ServerCallContext context)

Modifies an existing zone VM extension policy within a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UpdateZoneVmExtensionPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
