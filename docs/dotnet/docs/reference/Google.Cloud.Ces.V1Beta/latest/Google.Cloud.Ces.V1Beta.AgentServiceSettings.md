---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings
title: Gemini Enterprise for Customer Experience v1beta API - Class AgentServiceSettings (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:49.897500+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class AgentServiceSettings (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class AgentServiceSettings (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class AgentServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class AgentServiceSettings.

Settings for [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > AgentServiceSettings

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

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### AgentServiceSettings()
    
    
    public AgentServiceSettings()

Constructs a new [AgentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings) object with default settings.

## Properties 

### BatchDeleteConversationsOperationsSettings
    
    
    public OperationsSettings BatchDeleteConversationsOperationsSettings { get; set; }

Long Running Operation settings for calls to `AgentServiceClient.BatchDeleteConversations` and `AgentServiceClient.BatchDeleteConversationsAsync`.

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



### BatchDeleteConversationsSettings
    
    
    public CallSettings BatchDeleteConversationsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.BatchDeleteConversations` and `AgentServiceClient.BatchDeleteConversationsAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateAgentSettings
    
    
    public CallSettings CreateAgentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateAgent` and `AgentServiceClient.CreateAgentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateAppOperationsSettings
    
    
    public OperationsSettings CreateAppOperationsSettings { get; set; }

Long Running Operation settings for calls to `AgentServiceClient.CreateApp` and `AgentServiceClient.CreateAppAsync`.

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



### CreateAppSettings
    
    
    public CallSettings CreateAppSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateApp` and `AgentServiceClient.CreateAppAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateAppVersionSettings
    
    
    public CallSettings CreateAppVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateAppVersion` and `AgentServiceClient.CreateAppVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateDeploymentSettings
    
    
    public CallSettings CreateDeploymentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateDeployment` and `AgentServiceClient.CreateDeploymentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateExampleSettings
    
    
    public CallSettings CreateExampleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateExample` and `AgentServiceClient.CreateExampleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateGuardrailSettings
    
    
    public CallSettings CreateGuardrailSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateGuardrail` and `AgentServiceClient.CreateGuardrailAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateToolSettings
    
    
    public CallSettings CreateToolSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateTool` and `AgentServiceClient.CreateToolAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### CreateToolsetSettings
    
    
    public CallSettings CreateToolsetSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.CreateToolset` and `AgentServiceClient.CreateToolsetAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteAgentSettings
    
    
    public CallSettings DeleteAgentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteAgent` and `AgentServiceClient.DeleteAgentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteAppOperationsSettings
    
    
    public OperationsSettings DeleteAppOperationsSettings { get; set; }

Long Running Operation settings for calls to `AgentServiceClient.DeleteApp` and `AgentServiceClient.DeleteAppAsync`.

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



### DeleteAppSettings
    
    
    public CallSettings DeleteAppSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteApp` and `AgentServiceClient.DeleteAppAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteAppVersionSettings
    
    
    public CallSettings DeleteAppVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteAppVersion` and `AgentServiceClient.DeleteAppVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteConversationSettings
    
    
    public CallSettings DeleteConversationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteConversation` and `AgentServiceClient.DeleteConversationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteDeploymentSettings
    
    
    public CallSettings DeleteDeploymentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteDeployment` and `AgentServiceClient.DeleteDeploymentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteExampleSettings
    
    
    public CallSettings DeleteExampleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteExample` and `AgentServiceClient.DeleteExampleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteGuardrailSettings
    
    
    public CallSettings DeleteGuardrailSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteGuardrail` and `AgentServiceClient.DeleteGuardrailAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteToolSettings
    
    
    public CallSettings DeleteToolSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteTool` and `AgentServiceClient.DeleteToolAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### DeleteToolsetSettings
    
    
    public CallSettings DeleteToolsetSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.DeleteToolset` and `AgentServiceClient.DeleteToolsetAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ExportAppOperationsSettings
    
    
    public OperationsSettings ExportAppOperationsSettings { get; set; }

Long Running Operation settings for calls to `AgentServiceClient.ExportApp` and `AgentServiceClient.ExportAppAsync`.

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



### ExportAppSettings
    
    
    public CallSettings ExportAppSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ExportApp` and `AgentServiceClient.ExportAppAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GenerateAppResourceOperationsSettings
    
    
    public OperationsSettings GenerateAppResourceOperationsSettings { get; set; }

Long Running Operation settings for calls to `AgentServiceClient.GenerateAppResource` and `AgentServiceClient.GenerateAppResourceAsync`.

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



### GenerateAppResourceSettings
    
    
    public CallSettings GenerateAppResourceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GenerateAppResource` and `AgentServiceClient.GenerateAppResourceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetAgentSettings
    
    
    public CallSettings GetAgentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetAgent` and `AgentServiceClient.GetAgentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetAppSettings
    
    
    public CallSettings GetAppSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetApp` and `AgentServiceClient.GetAppAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetAppVersionSettings
    
    
    public CallSettings GetAppVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetAppVersion` and `AgentServiceClient.GetAppVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetChangelogSettings
    
    
    public CallSettings GetChangelogSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetChangelog` and `AgentServiceClient.GetChangelogAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetConversationSettings
    
    
    public CallSettings GetConversationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetConversation` and `AgentServiceClient.GetConversationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetDeploymentSettings
    
    
    public CallSettings GetDeploymentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetDeployment` and `AgentServiceClient.GetDeploymentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetExampleSettings
    
    
    public CallSettings GetExampleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetExample` and `AgentServiceClient.GetExampleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetGuardrailSettings
    
    
    public CallSettings GetGuardrailSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetGuardrail` and `AgentServiceClient.GetGuardrailAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetSecuritySettingsSettings
    
    
    public CallSettings GetSecuritySettingsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetSecuritySettings` and `AgentServiceClient.GetSecuritySettingsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetToolSettings
    
    
    public CallSettings GetToolSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetTool` and `AgentServiceClient.GetToolAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### GetToolsetSettings
    
    
    public CallSettings GetToolsetSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.GetToolset` and `AgentServiceClient.GetToolsetAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ImportAppOperationsSettings
    
    
    public OperationsSettings ImportAppOperationsSettings { get; set; }

Long Running Operation settings for calls to `AgentServiceClient.ImportApp` and `AgentServiceClient.ImportAppAsync`.

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



### ImportAppSettings
    
    
    public CallSettings ImportAppSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ImportApp` and `AgentServiceClient.ImportAppAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListAgentsSettings
    
    
    public CallSettings ListAgentsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListAgents` and `AgentServiceClient.ListAgentsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListAppVersionsSettings
    
    
    public CallSettings ListAppVersionsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListAppVersions` and `AgentServiceClient.ListAppVersionsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListAppsSettings
    
    
    public CallSettings ListAppsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListApps` and `AgentServiceClient.ListAppsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListChangelogsSettings
    
    
    public CallSettings ListChangelogsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListChangelogs` and `AgentServiceClient.ListChangelogsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListConversationsSettings
    
    
    public CallSettings ListConversationsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListConversations` and `AgentServiceClient.ListConversationsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListDeploymentsSettings
    
    
    public CallSettings ListDeploymentsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListDeployments` and `AgentServiceClient.ListDeploymentsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListExamplesSettings
    
    
    public CallSettings ListExamplesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListExamples` and `AgentServiceClient.ListExamplesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListGuardrailsSettings
    
    
    public CallSettings ListGuardrailsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListGuardrails` and `AgentServiceClient.ListGuardrailsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListToolsSettings
    
    
    public CallSettings ListToolsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListTools` and `AgentServiceClient.ListToolsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### ListToolsetsSettings
    
    
    public CallSettings ListToolsetsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.ListToolsets` and `AgentServiceClient.ListToolsetsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### RestoreAppVersionOperationsSettings
    
    
    public OperationsSettings RestoreAppVersionOperationsSettings { get; set; }

Long Running Operation settings for calls to `AgentServiceClient.RestoreAppVersion` and `AgentServiceClient.RestoreAppVersionAsync`.

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



### RestoreAppVersionSettings
    
    
    public CallSettings RestoreAppVersionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.RestoreAppVersion` and `AgentServiceClient.RestoreAppVersionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateAgentSettings
    
    
    public CallSettings UpdateAgentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateAgent` and `AgentServiceClient.UpdateAgentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateAppSettings
    
    
    public CallSettings UpdateAppSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateApp` and `AgentServiceClient.UpdateAppAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateDeploymentSettings
    
    
    public CallSettings UpdateDeploymentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateDeployment` and `AgentServiceClient.UpdateDeploymentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateExampleSettings
    
    
    public CallSettings UpdateExampleSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateExample` and `AgentServiceClient.UpdateExampleAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateGuardrailSettings
    
    
    public CallSettings UpdateGuardrailSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateGuardrail` and `AgentServiceClient.UpdateGuardrailAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateSecuritySettingsSettings
    
    
    public CallSettings UpdateSecuritySettingsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateSecuritySettings` and `AgentServiceClient.UpdateSecuritySettingsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateToolSettings
    
    
    public CallSettings UpdateToolSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateTool` and `AgentServiceClient.UpdateToolAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



### UpdateToolsetSettings
    
    
    public CallSettings UpdateToolsetSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `AgentServiceClient.UpdateToolset` and `AgentServiceClient.UpdateToolsetAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded), [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable). 
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public AgentServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[AgentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings)` | A deep clone of this [AgentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings) object.  
  
### GetDefault()
    
    
    public static AgentServiceSettings GetDefault()

Get a new instance of the default [AgentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[AgentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings)` | A new instance of the default [AgentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
