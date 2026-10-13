---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminBase
title: Google Cloud Key Management Service v1 API - Class AutokeyAdmin.AutokeyAdminBase (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:54.575928+00:00
---

# Google Cloud Key Management Service v1 API - Class AutokeyAdmin.AutokeyAdminBase (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class AutokeyAdmin.AutokeyAdminBase (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    [BindServiceMethod(typeof(AutokeyAdmin), "BindService")]
    public abstract class AutokeyAdmin.AutokeyAdminBase

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class AutokeyAdmin.AutokeyAdminBase.

Base class for server-side implementations of AutokeyAdmin

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutokeyAdmin.AutokeyAdminBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Methods 

### GetAutokeyConfig(GetAutokeyConfigRequest, ServerCallContext)
    
    
    public virtual Task<AutokeyConfig> GetAutokeyConfig(GetAutokeyConfigRequest request, ServerCallContext context)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The response to send back to the client (wrapped by a task).  
  
### ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest, ServerCallContext)
    
    
    public virtual Task<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest request, ServerCallContext context)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateAutokeyConfig(UpdateAutokeyConfigRequest, ServerCallContext)
    
    
    public virtual Task<AutokeyConfig> UpdateAutokeyConfig(UpdateAutokeyConfigRequest request, ServerCallContext context)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
