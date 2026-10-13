---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings
title: Google Cloud Error Reporting v1beta1 API - Class ReportErrorsServiceSettings (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:02.681725+00:00
---

# Google Cloud Error Reporting v1beta1 API - Class ReportErrorsServiceSettings (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Error Reporting v1beta1 API - Class ReportErrorsServiceSettings (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/3.0.0-beta05/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/2.0.0-beta05/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings)


    
    
    public sealed class ReportErrorsServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Google Cloud Error Reporting v1beta1 API class ReportErrorsServiceSettings.

Settings for [ReportErrorsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > ReportErrorsServiceSettings

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

[Google.Cloud.ErrorReporting.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1)

## Assembly

Google.Cloud.ErrorReporting.V1Beta1.dll

## Constructors 

### ReportErrorsServiceSettings()
    
    
    public ReportErrorsServiceSettings()

Constructs a new [ReportErrorsServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings) object with default settings.

## Properties 

### ReportErrorEventSettings
    
    
    public CallSettings ReportErrorEventSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ReportErrorsServiceClient.ReportErrorEvent` and `ReportErrorsServiceClient.ReportErrorEventAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



## Methods 

### Clone()
    
    
    public ReportErrorsServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[ReportErrorsServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings)` | A deep clone of this [ReportErrorsServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings) object.  
  
### GetDefault()
    
    
    public static ReportErrorsServiceSettings GetDefault()

Get a new instance of the default [ReportErrorsServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[ReportErrorsServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings)` | A new instance of the default [ReportErrorsServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
