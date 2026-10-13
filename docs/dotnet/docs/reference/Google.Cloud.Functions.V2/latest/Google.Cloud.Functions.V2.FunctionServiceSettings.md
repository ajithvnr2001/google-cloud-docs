---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings
title: Cloud Functions v2 API - Class FunctionServiceSettings (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:44.402781+00:00
---

# Cloud Functions v2 API - Class FunctionServiceSettings (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2 API - Class FunctionServiceSettings (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.7.0/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.6.0/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.5.0/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.4.0/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.3.0/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.2.0/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.1.0/Google.Cloud.Functions.V2.FunctionServiceSettings)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.0.0/Google.Cloud.Functions.V2.FunctionServiceSettings)


    
    
    public sealed class FunctionServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Cloud Functions v2 API class FunctionServiceSettings.

Settings for [FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > FunctionServiceSettings

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

[Google.Cloud.Functions.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2)

## Assembly

Google.Cloud.Functions.V2.dll

## Constructors 

### FunctionServiceSettings()
    
    
    public FunctionServiceSettings()

Constructs a new [FunctionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings) object with default settings.

## Properties 

### CreateFunctionOperationsSettings
    
    
    public OperationsSettings CreateFunctionOperationsSettings { get; set; }

Long Running Operation settings for calls to `FunctionServiceClient.CreateFunction` and `FunctionServiceClient.CreateFunctionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### CreateFunctionSettings
    
    
    public CallSettings CreateFunctionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.CreateFunction` and `FunctionServiceClient.CreateFunctionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### DeleteFunctionOperationsSettings
    
    
    public OperationsSettings DeleteFunctionOperationsSettings { get; set; }

Long Running Operation settings for calls to `FunctionServiceClient.DeleteFunction` and `FunctionServiceClient.DeleteFunctionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### DeleteFunctionSettings
    
    
    public CallSettings DeleteFunctionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.DeleteFunction` and `FunctionServiceClient.DeleteFunctionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GenerateDownloadUrlSettings
    
    
    public CallSettings GenerateDownloadUrlSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.GenerateDownloadUrl` and `FunctionServiceClient.GenerateDownloadUrlAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GenerateUploadUrlSettings
    
    
    public CallSettings GenerateUploadUrlSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.GenerateUploadUrl` and `FunctionServiceClient.GenerateUploadUrlAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetFunctionSettings
    
    
    public CallSettings GetFunctionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.GetFunction` and `FunctionServiceClient.GetFunctionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### IAMPolicySettings
    
    
    public IAMPolicySettings IAMPolicySettings { get; set; }

The settings to use for the [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicySettings.html)` |   
  
### ListFunctionsSettings
    
    
    public CallSettings ListFunctionsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.ListFunctions` and `FunctionServiceClient.ListFunctionsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ListRuntimesSettings
    
    
    public CallSettings ListRuntimesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.ListRuntimes` and `FunctionServiceClient.ListRuntimesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### UpdateFunctionOperationsSettings
    
    
    public OperationsSettings UpdateFunctionOperationsSettings { get; set; }

Long Running Operation settings for calls to `FunctionServiceClient.UpdateFunction` and `FunctionServiceClient.UpdateFunctionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### UpdateFunctionSettings
    
    
    public CallSettings UpdateFunctionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `FunctionServiceClient.UpdateFunction` and `FunctionServiceClient.UpdateFunctionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



## Methods 

### Clone()
    
    
    public FunctionServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[FunctionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings)` | A deep clone of this [FunctionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings) object.  
  
### GetDefault()
    
    
    public static FunctionServiceSettings GetDefault()

Get a new instance of the default [FunctionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[FunctionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings)` | A new instance of the default [FunctionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
