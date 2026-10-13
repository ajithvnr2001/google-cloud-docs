---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase
title: Cloud Quotas v1beta API - Class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase (1.0.0-beta04) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:18.838265+00:00
---

# Cloud Quotas v1beta API - Class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase (1.0.0-beta04)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1beta API - Class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase (1.0.0-beta04) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta04 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/1.0.0-beta03/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase)


    
    
    [BindServiceMethod(typeof(QuotaAdjusterSettingsManager), "BindService")]
    public abstract class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase

Reference documentation and code samples for the Cloud Quotas v1beta API class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase.

Base class for server-side implementations of QuotaAdjusterSettingsManager

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta)

## Assembly

Google.Cloud.CloudQuotas.V1Beta.dll

## Methods 

### GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest, ServerCallContext)
    
    
    public virtual Task<QuotaAdjusterSettings> GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest request, ServerCallContext context)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettings)` | The response to send back to the client (wrapped by a task).  
  
### UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest, ServerCallContext)
    
    
    public virtual Task<QuotaAdjusterSettings> UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest request, ServerCallContext context)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaAdjusterSettingsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettings)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
