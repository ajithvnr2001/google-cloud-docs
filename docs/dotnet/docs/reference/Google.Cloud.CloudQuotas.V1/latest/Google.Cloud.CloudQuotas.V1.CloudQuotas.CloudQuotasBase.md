---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasBase
title: Cloud Quotas v1 API - Class CloudQuotas.CloudQuotasBase (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:21.153061+00:00
---

# Cloud Quotas v1 API - Class CloudQuotas.CloudQuotasBase (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class CloudQuotas.CloudQuotasBase (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    [BindServiceMethod(typeof(CloudQuotas), "BindService")]
    public abstract class CloudQuotas.CloudQuotasBase

Reference documentation and code samples for the Cloud Quotas v1 API class CloudQuotas.CloudQuotasBase.

Base class for server-side implementations of CloudQuotas

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudQuotas.CloudQuotasBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Methods 

### CreateQuotaPreference(CreateQuotaPreferenceRequest, ServerCallContext)
    
    
    public virtual Task<QuotaPreference> CreateQuotaPreference(CreateQuotaPreferenceRequest request, ServerCallContext context)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response to send back to the client (wrapped by a task).  
  
### GetQuotaInfo(GetQuotaInfoRequest, ServerCallContext)
    
    
    public virtual Task<QuotaInfo> GetQuotaInfo(GetQuotaInfoRequest request, ServerCallContext context)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The response to send back to the client (wrapped by a task).  
  
### GetQuotaPreference(GetQuotaPreferenceRequest, ServerCallContext)
    
    
    public virtual Task<QuotaPreference> GetQuotaPreference(GetQuotaPreferenceRequest request, ServerCallContext context)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response to send back to the client (wrapped by a task).  
  
### ListQuotaInfos(ListQuotaInfosRequest, ServerCallContext)
    
    
    public virtual Task<ListQuotaInfosResponse> ListQuotaInfos(ListQuotaInfosRequest request, ServerCallContext context)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListQuotaPreferences(ListQuotaPreferencesRequest, ServerCallContext)
    
    
    public virtual Task<ListQuotaPreferencesResponse> ListQuotaPreferences(ListQuotaPreferencesRequest request, ServerCallContext context)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateQuotaPreference(UpdateQuotaPreferenceRequest, ServerCallContext)
    
    
    public virtual Task<QuotaPreference> UpdateQuotaPreference(UpdateQuotaPreferenceRequest request, ServerCallContext context)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
