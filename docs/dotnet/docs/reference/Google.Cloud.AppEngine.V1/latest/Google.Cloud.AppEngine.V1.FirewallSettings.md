---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings
title: App Engine v1 API - Class FirewallSettings (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:19.803477+00:00
---

# App Engine v1 API - Class FirewallSettings (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Engine v1 API - Class FirewallSettings (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.4.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.3.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.2.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.1.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.0.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.4.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.3.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.2.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.1.0/Google.Cloud.AppEngine.V1.FirewallSettings)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.0.0/Google.Cloud.AppEngine.V1.FirewallSettings)


    
    
    public sealed class FirewallSettings : ServiceSettingsBase

Reference documentation and code samples for the App Engine v1 API class FirewallSettings.

Settings for [FirewallClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > FirewallSettings

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

[Google.Cloud.AppEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1)

## Assembly

Google.Cloud.AppEngine.V1.dll

## Constructors 

### FirewallSettings()
    
    
    public FirewallSettings()

Constructs a new [FirewallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings) object with default settings.

## Properties 

### BatchUpdateIngressRulesSettings
    
    
    public CallSettings BatchUpdateIngressRulesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FirewallClient.BatchUpdateIngressRules` and `FirewallClient.BatchUpdateIngressRulesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### CreateIngressRuleSettings
    
    
    public CallSettings CreateIngressRuleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FirewallClient.CreateIngressRule` and `FirewallClient.CreateIngressRuleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteIngressRuleSettings
    
    
    public CallSettings DeleteIngressRuleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FirewallClient.DeleteIngressRule` and `FirewallClient.DeleteIngressRuleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetIngressRuleSettings
    
    
    public CallSettings GetIngressRuleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FirewallClient.GetIngressRule` and `FirewallClient.GetIngressRuleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### ListIngressRulesSettings
    
    
    public CallSettings ListIngressRulesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FirewallClient.ListIngressRules` and `FirewallClient.ListIngressRulesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateIngressRuleSettings
    
    
    public CallSettings UpdateIngressRuleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FirewallClient.UpdateIngressRule` and `FirewallClient.UpdateIngressRuleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public FirewallSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[FirewallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings)` | A deep clone of this [FirewallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings) object.  
  
### GetDefault()
    
    
    public static FirewallSettings GetDefault()

Get a new instance of the default [FirewallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings).

**Returns**  
---  
**Type** | **Description**  
`[FirewallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings)` | A new instance of the default [FirewallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.FirewallSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
