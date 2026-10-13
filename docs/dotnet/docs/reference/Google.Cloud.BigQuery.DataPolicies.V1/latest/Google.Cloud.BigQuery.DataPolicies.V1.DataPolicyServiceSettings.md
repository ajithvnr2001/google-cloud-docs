---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings
title: BigQuery Data Policy v1 API - Class DataPolicyServiceSettings (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:01.500927+00:00
---

# BigQuery Data Policy v1 API - Class DataPolicyServiceSettings (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BigQuery Data Policy v1 API - Class DataPolicyServiceSettings (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.5.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.4.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.3.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.2.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.1.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.0.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)


    
    
    public sealed class DataPolicyServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the BigQuery Data Policy v1 API class DataPolicyServiceSettings.

Settings for [DataPolicyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > DataPolicyServiceSettings

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

[Google.Cloud.BigQuery.DataPolicies.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1)

## Assembly

Google.Cloud.BigQuery.DataPolicies.V1.dll

## Constructors 

### DataPolicyServiceSettings()
    
    
    public DataPolicyServiceSettings()

Constructs a new [DataPolicyServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings) object with default settings.

## Properties 

### CreateDataPolicySettings
    
    
    public CallSettings CreateDataPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.CreateDataPolicy` and `DataPolicyServiceClient.CreateDataPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### DeleteDataPolicySettings
    
    
    public CallSettings DeleteDataPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.DeleteDataPolicy` and `DataPolicyServiceClient.DeleteDataPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetDataPolicySettings
    
    
    public CallSettings GetDataPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.GetDataPolicy` and `DataPolicyServiceClient.GetDataPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetIamPolicySettings
    
    
    public CallSettings GetIamPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.GetIamPolicy` and `DataPolicyServiceClient.GetIamPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListDataPoliciesSettings
    
    
    public CallSettings ListDataPoliciesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.ListDataPolicies` and `DataPolicyServiceClient.ListDataPoliciesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### RenameDataPolicySettings
    
    
    public CallSettings RenameDataPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.RenameDataPolicy` and `DataPolicyServiceClient.RenameDataPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### SetIamPolicySettings
    
    
    public CallSettings SetIamPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.SetIamPolicy` and `DataPolicyServiceClient.SetIamPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### TestIamPermissionsSettings
    
    
    public CallSettings TestIamPermissionsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.TestIamPermissions` and `DataPolicyServiceClient.TestIamPermissionsAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### UpdateDataPolicySettings
    
    
    public CallSettings UpdateDataPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DataPolicyServiceClient.UpdateDataPolicy` and `DataPolicyServiceClient.UpdateDataPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public DataPolicyServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[DataPolicyServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)` | A deep clone of this [DataPolicyServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings) object.  
  
### GetDefault()
    
    
    public static DataPolicyServiceSettings GetDefault()

Get a new instance of the default [DataPolicyServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[DataPolicyServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings)` | A new instance of the default [DataPolicyServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
