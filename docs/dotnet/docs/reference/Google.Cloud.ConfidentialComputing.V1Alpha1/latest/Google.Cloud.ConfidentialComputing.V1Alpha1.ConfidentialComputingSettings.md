---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings
title: Confidential Computing v1alpha1 API - Class ConfidentialComputingSettings (1.0.0-alpha06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:04.285140+00:00
---

# Confidential Computing v1alpha1 API - Class ConfidentialComputingSettings (1.0.0-alpha06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Confidential Computing v1alpha1 API - Class ConfidentialComputingSettings (1.0.0-alpha06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-alpha06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings)
  * [ 1.0.0-alpha05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/1.0.0-alpha05/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings)


    
    
    public sealed class ConfidentialComputingSettings : ServiceSettingsBase

Reference documentation and code samples for the Confidential Computing v1alpha1 API class ConfidentialComputingSettings.

Settings for [ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > ConfidentialComputingSettings

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

[Google.Cloud.ConfidentialComputing.V1Alpha1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1)

## Assembly

Google.Cloud.ConfidentialComputing.V1Alpha1.dll

## Constructors 

### ConfidentialComputingSettings()
    
    
    public ConfidentialComputingSettings()

Constructs a new [ConfidentialComputingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings) object with default settings.

## Properties 

### CreateChallengeSettings
    
    
    public CallSettings CreateChallengeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ConfidentialComputingClient.CreateChallenge` and `ConfidentialComputingClient.CreateChallengeAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### VerifyAttestationSettings
    
    
    public CallSettings VerifyAttestationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ConfidentialComputingClient.VerifyAttestation` and `ConfidentialComputingClient.VerifyAttestationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public ConfidentialComputingSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[ConfidentialComputingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings)` | A deep clone of this [ConfidentialComputingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings) object.  
  
### GetDefault()
    
    
    public static ConfidentialComputingSettings GetDefault()

Get a new instance of the default [ConfidentialComputingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings).

**Returns**  
---  
**Type** | **Description**  
`[ConfidentialComputingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings)` | A new instance of the default [ConfidentialComputingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1Alpha1/latest/Google.Cloud.ConfidentialComputing.V1Alpha1.ConfidentialComputingSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
