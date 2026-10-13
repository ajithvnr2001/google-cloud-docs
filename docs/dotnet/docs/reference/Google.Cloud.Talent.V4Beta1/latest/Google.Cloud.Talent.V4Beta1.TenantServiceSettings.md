---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings
title: Google Cloud Talent Solution v4beta1 API - Class TenantServiceSettings (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:25.933211+00:00
---

# Google Cloud Talent Solution v4beta1 API - Class TenantServiceSettings (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Talent Solution v4beta1 API - Class TenantServiceSettings (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/3.0.0-beta06/Google.Cloud.Talent.V4Beta1.TenantServiceSettings)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/2.0.0-beta07/Google.Cloud.Talent.V4Beta1.TenantServiceSettings)


    
    
    public sealed class TenantServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Google Cloud Talent Solution v4beta1 API class TenantServiceSettings.

Settings for [TenantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > TenantServiceSettings

## Inherited Members

[ServiceSettingsBase.VersionHeaderBuilder](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_VersionHeaderBuilder)

[ServiceSettingsBase.CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_CallSettings)

[ServiceSettingsBase.Clock](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Clock)

[ServiceSettingsBase.Scheduler](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Scheduler)

[ServiceSettingsBase.Interceptor](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Interceptor)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Talent.V4Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1)

## Assembly

Google.Cloud.Talent.V4Beta1.dll

## Constructors 

### TenantServiceSettings()
    
    
    public TenantServiceSettings()

Constructs a new [TenantServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings) object with default settings.

## Properties 

### CreateTenantSettings
    
    
    public CallSettings CreateTenantSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `TenantServiceClient.CreateTenant` and `TenantServiceClient.CreateTenantAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 30 seconds.



### DeleteTenantSettings
    
    
    public CallSettings DeleteTenantSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `TenantServiceClient.DeleteTenant` and `TenantServiceClient.DeleteTenantAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 30 seconds.



### GetTenantSettings
    
    
    public CallSettings GetTenantSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `TenantServiceClient.GetTenant` and `TenantServiceClient.GetTenantAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 30 seconds.



### ListTenantsSettings
    
    
    public CallSettings ListTenantsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `TenantServiceClient.ListTenants` and `TenantServiceClient.ListTenantsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 30 seconds.



### UpdateTenantSettings
    
    
    public CallSettings UpdateTenantSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `TenantServiceClient.UpdateTenant` and `TenantServiceClient.UpdateTenantAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 30 seconds.



## Methods 

### Clone()
    
    
    public TenantServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[TenantServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings)` | A deep clone of this [TenantServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings) object.  
  
### GetDefault()
    
    
    public static TenantServiceSettings GetDefault()

Get a new instance of the default [TenantServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[TenantServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings)` | A new instance of the default [TenantServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.TenantServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
