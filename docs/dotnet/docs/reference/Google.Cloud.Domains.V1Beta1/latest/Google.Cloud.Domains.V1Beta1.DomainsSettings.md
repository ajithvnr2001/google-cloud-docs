---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings
title: Cloud Domains v1beta1 API - Class DomainsSettings (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:21.250709+00:00
---

# Cloud Domains v1beta1 API - Class DomainsSettings (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1beta1 API - Class DomainsSettings (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/2.0.0-beta05/Google.Cloud.Domains.V1Beta1.DomainsSettings)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/1.0.0-beta04/Google.Cloud.Domains.V1Beta1.DomainsSettings)


    
    
    public sealed class DomainsSettings : ServiceSettingsBase

Reference documentation and code samples for the Cloud Domains v1beta1 API class DomainsSettings.

Settings for [DomainsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > DomainsSettings

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

[Google.Cloud.Domains.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1)

## Assembly

Google.Cloud.Domains.V1Beta1.dll

## Constructors 

### DomainsSettings()
    
    
    public DomainsSettings()

Constructs a new [DomainsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings) object with default settings.

## Properties 

### ConfigureContactSettingsOperationsSettings
    
    
    public OperationsSettings ConfigureContactSettingsOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.ConfigureContactSettings` and `DomainsClient.ConfigureContactSettingsAsync`.

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



### ConfigureContactSettingsSettings
    
    
    public CallSettings ConfigureContactSettingsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.ConfigureContactSettings` and `DomainsClient.ConfigureContactSettingsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ConfigureDnsSettingsOperationsSettings
    
    
    public OperationsSettings ConfigureDnsSettingsOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.ConfigureDnsSettings` and `DomainsClient.ConfigureDnsSettingsAsync`.

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



### ConfigureDnsSettingsSettings
    
    
    public CallSettings ConfigureDnsSettingsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.ConfigureDnsSettings` and `DomainsClient.ConfigureDnsSettingsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ConfigureManagementSettingsOperationsSettings
    
    
    public OperationsSettings ConfigureManagementSettingsOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.ConfigureManagementSettings` and `DomainsClient.ConfigureManagementSettingsAsync`.

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



### ConfigureManagementSettingsSettings
    
    
    public CallSettings ConfigureManagementSettingsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.ConfigureManagementSettings` and `DomainsClient.ConfigureManagementSettingsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### DeleteRegistrationOperationsSettings
    
    
    public OperationsSettings DeleteRegistrationOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.DeleteRegistration` and `DomainsClient.DeleteRegistrationAsync`.

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



### DeleteRegistrationSettings
    
    
    public CallSettings DeleteRegistrationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.DeleteRegistration` and `DomainsClient.DeleteRegistrationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ExportRegistrationOperationsSettings
    
    
    public OperationsSettings ExportRegistrationOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.ExportRegistration` and `DomainsClient.ExportRegistrationAsync`.

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



### ExportRegistrationSettings
    
    
    public CallSettings ExportRegistrationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.ExportRegistration` and `DomainsClient.ExportRegistrationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetRegistrationSettings
    
    
    public CallSettings GetRegistrationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.GetRegistration` and `DomainsClient.GetRegistrationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ListRegistrationsSettings
    
    
    public CallSettings ListRegistrationsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.ListRegistrations` and `DomainsClient.ListRegistrationsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### RegisterDomainOperationsSettings
    
    
    public OperationsSettings RegisterDomainOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.RegisterDomain` and `DomainsClient.RegisterDomainAsync`.

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



### RegisterDomainSettings
    
    
    public CallSettings RegisterDomainSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.RegisterDomain` and `DomainsClient.RegisterDomainAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ResetAuthorizationCodeSettings
    
    
    public CallSettings ResetAuthorizationCodeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.ResetAuthorizationCode` and `DomainsClient.ResetAuthorizationCodeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### RetrieveAuthorizationCodeSettings
    
    
    public CallSettings RetrieveAuthorizationCodeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.RetrieveAuthorizationCode` and `DomainsClient.RetrieveAuthorizationCodeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### RetrieveRegisterParametersSettings
    
    
    public CallSettings RetrieveRegisterParametersSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.RetrieveRegisterParameters` and `DomainsClient.RetrieveRegisterParametersAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### RetrieveTransferParametersSettings
    
    
    public CallSettings RetrieveTransferParametersSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.RetrieveTransferParameters` and `DomainsClient.RetrieveTransferParametersAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### SearchDomainsSettings
    
    
    public CallSettings SearchDomainsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.SearchDomains` and `DomainsClient.SearchDomainsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### TransferDomainOperationsSettings
    
    
    public OperationsSettings TransferDomainOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.TransferDomain` and `DomainsClient.TransferDomainAsync`.

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



### TransferDomainSettings
    
    
    public CallSettings TransferDomainSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.TransferDomain` and `DomainsClient.TransferDomainAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### UpdateRegistrationOperationsSettings
    
    
    public OperationsSettings UpdateRegistrationOperationsSettings { get; set; }

Long Running Operation settings for calls to `DomainsClient.UpdateRegistration` and `DomainsClient.UpdateRegistrationAsync`.

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



### UpdateRegistrationSettings
    
    
    public CallSettings UpdateRegistrationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `DomainsClient.UpdateRegistration` and `DomainsClient.UpdateRegistrationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



## Methods 

### Clone()
    
    
    public DomainsSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[DomainsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings)` | A deep clone of this [DomainsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings) object.  
  
### GetDefault()
    
    
    public static DomainsSettings GetDefault()

Get a new instance of the default [DomainsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings).

**Returns**  
---  
**Type** | **Description**  
`[DomainsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings)` | A new instance of the default [DomainsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DomainsSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
