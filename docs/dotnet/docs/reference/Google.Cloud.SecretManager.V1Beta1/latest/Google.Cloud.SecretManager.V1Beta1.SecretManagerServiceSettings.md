---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings
title: Secret Manager v1beta1 API - Class SecretManagerServiceSettings (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:56.295155+00:00
---

# Secret Manager v1beta1 API - Class SecretManagerServiceSettings (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Secret Manager v1beta1 API - Class SecretManagerServiceSettings (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/3.0.0-beta06/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/2.0.0-beta05/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings)


    
    
    public sealed class SecretManagerServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Secret Manager v1beta1 API class SecretManagerServiceSettings.

Settings for [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > SecretManagerServiceSettings

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

[Google.Cloud.SecretManager.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1)

## Assembly

Google.Cloud.SecretManager.V1Beta1.dll

## Constructors 

### SecretManagerServiceSettings()
    
    
    public SecretManagerServiceSettings()

Constructs a new [SecretManagerServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings) object with default settings.

## Properties 

### AccessSecretVersionSettings
    
    
    public CallSettings AccessSecretVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.AccessSecretVersion` and `SecretManagerServiceClient.AccessSecretVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable), [Unknown](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unknown). 
  * Timeout: 60 seconds.



### AddSecretVersionSettings
    
    
    public CallSettings AddSecretVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.AddSecretVersion` and `SecretManagerServiceClient.AddSecretVersionAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### CreateSecretSettings
    
    
    public CallSettings CreateSecretSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.CreateSecret` and `SecretManagerServiceClient.CreateSecretAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteSecretSettings
    
    
    public CallSettings DeleteSecretSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.DeleteSecret` and `SecretManagerServiceClient.DeleteSecretAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DestroySecretVersionSettings
    
    
    public CallSettings DestroySecretVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.DestroySecretVersion` and `SecretManagerServiceClient.DestroySecretVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DisableSecretVersionSettings
    
    
    public CallSettings DisableSecretVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.DisableSecretVersion` and `SecretManagerServiceClient.DisableSecretVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### EnableSecretVersionSettings
    
    
    public CallSettings EnableSecretVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.EnableSecretVersion` and `SecretManagerServiceClient.EnableSecretVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetIamPolicySettings
    
    
    public CallSettings GetIamPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.GetIamPolicy` and `SecretManagerServiceClient.GetIamPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetSecretSettings
    
    
    public CallSettings GetSecretSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.GetSecret` and `SecretManagerServiceClient.GetSecretAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetSecretVersionSettings
    
    
    public CallSettings GetSecretVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.GetSecretVersion` and `SecretManagerServiceClient.GetSecretVersionAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### ListSecretVersionsSettings
    
    
    public CallSettings ListSecretVersionsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.ListSecretVersions` and `SecretManagerServiceClient.ListSecretVersionsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### ListSecretsSettings
    
    
    public CallSettings ListSecretsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.ListSecrets` and `SecretManagerServiceClient.ListSecretsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### SetIamPolicySettings
    
    
    public CallSettings SetIamPolicySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.SetIamPolicy` and `SecretManagerServiceClient.SetIamPolicyAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### TestIamPermissionsSettings
    
    
    public CallSettings TestIamPermissionsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.TestIamPermissions` and `SecretManagerServiceClient.TestIamPermissionsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateSecretSettings
    
    
    public CallSettings UpdateSecretSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `SecretManagerServiceClient.UpdateSecret` and `SecretManagerServiceClient.UpdateSecretAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public SecretManagerServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings)` | A deep clone of this [SecretManagerServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings) object.  
  
### GetDefault()
    
    
    public static SecretManagerServiceSettings GetDefault()

Get a new instance of the default [SecretManagerServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings)` | A new instance of the default [SecretManagerServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretManagerServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
