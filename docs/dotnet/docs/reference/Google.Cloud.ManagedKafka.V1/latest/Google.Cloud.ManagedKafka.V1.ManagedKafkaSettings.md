---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings
title: Managed Service for Apache Kafka API v1 API - Class ManagedKafkaSettings (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:21.540096+00:00
---

# Managed Service for Apache Kafka API v1 API - Class ManagedKafkaSettings (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class ManagedKafkaSettings (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings)


    
    
    public sealed class ManagedKafkaSettings : ServiceSettingsBase

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class ManagedKafkaSettings.

Settings for [ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > ManagedKafkaSettings

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

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Constructors 

### ManagedKafkaSettings()
    
    
    public ManagedKafkaSettings()

Constructs a new [ManagedKafkaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings) object with default settings.

## Properties 

### AddAclEntrySettings
    
    
    public CallSettings AddAclEntrySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.AddAclEntry` and `ManagedKafkaClient.AddAclEntryAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### CreateAclSettings
    
    
    public CallSettings CreateAclSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.CreateAcl` and `ManagedKafkaClient.CreateAclAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### CreateClusterOperationsSettings
    
    
    public OperationsSettings CreateClusterOperationsSettings { get; set; }

Long Running Operation settings for calls to `ManagedKafkaClient.CreateCluster` and `ManagedKafkaClient.CreateClusterAsync`.

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



### CreateClusterSettings
    
    
    public CallSettings CreateClusterSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.CreateCluster` and `ManagedKafkaClient.CreateClusterAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### CreateTopicSettings
    
    
    public CallSettings CreateTopicSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.CreateTopic` and `ManagedKafkaClient.CreateTopicAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteAclSettings
    
    
    public CallSettings DeleteAclSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.DeleteAcl` and `ManagedKafkaClient.DeleteAclAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### DeleteClusterOperationsSettings
    
    
    public OperationsSettings DeleteClusterOperationsSettings { get; set; }

Long Running Operation settings for calls to `ManagedKafkaClient.DeleteCluster` and `ManagedKafkaClient.DeleteClusterAsync`.

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



### DeleteClusterSettings
    
    
    public CallSettings DeleteClusterSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.DeleteCluster` and `ManagedKafkaClient.DeleteClusterAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteConsumerGroupSettings
    
    
    public CallSettings DeleteConsumerGroupSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.DeleteConsumerGroup` and `ManagedKafkaClient.DeleteConsumerGroupAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteTopicSettings
    
    
    public CallSettings DeleteTopicSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.DeleteTopic` and `ManagedKafkaClient.DeleteTopicAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetAclSettings
    
    
    public CallSettings GetAclSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.GetAcl` and `ManagedKafkaClient.GetAclAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetClusterSettings
    
    
    public CallSettings GetClusterSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.GetCluster` and `ManagedKafkaClient.GetClusterAsync`.

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



### GetConsumerGroupSettings
    
    
    public CallSettings GetConsumerGroupSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.GetConsumerGroup` and `ManagedKafkaClient.GetConsumerGroupAsync`.

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



### GetTopicSettings
    
    
    public CallSettings GetTopicSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.GetTopic` and `ManagedKafkaClient.GetTopicAsync`.

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



### ListAclsSettings
    
    
    public CallSettings ListAclsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.ListAcls` and `ManagedKafkaClient.ListAclsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ListClustersSettings
    
    
    public CallSettings ListClustersSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.ListClusters` and `ManagedKafkaClient.ListClustersAsync`.

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



### ListConsumerGroupsSettings
    
    
    public CallSettings ListConsumerGroupsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.ListConsumerGroups` and `ManagedKafkaClient.ListConsumerGroupsAsync`.

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



### ListTopicsSettings
    
    
    public CallSettings ListTopicsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.ListTopics` and `ManagedKafkaClient.ListTopicsAsync`.

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



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### RemoveAclEntrySettings
    
    
    public CallSettings RemoveAclEntrySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.RemoveAclEntry` and `ManagedKafkaClient.RemoveAclEntryAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### UpdateAclSettings
    
    
    public CallSettings UpdateAclSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.UpdateAcl` and `ManagedKafkaClient.UpdateAclAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### UpdateClusterOperationsSettings
    
    
    public OperationsSettings UpdateClusterOperationsSettings { get; set; }

Long Running Operation settings for calls to `ManagedKafkaClient.UpdateCluster` and `ManagedKafkaClient.UpdateClusterAsync`.

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



### UpdateClusterSettings
    
    
    public CallSettings UpdateClusterSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.UpdateCluster` and `ManagedKafkaClient.UpdateClusterAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateConsumerGroupSettings
    
    
    public CallSettings UpdateConsumerGroupSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.UpdateConsumerGroup` and `ManagedKafkaClient.UpdateConsumerGroupAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateTopicSettings
    
    
    public CallSettings UpdateTopicSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ManagedKafkaClient.UpdateTopic` and `ManagedKafkaClient.UpdateTopicAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public ManagedKafkaSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings)` | A deep clone of this [ManagedKafkaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings) object.  
  
### GetDefault()
    
    
    public static ManagedKafkaSettings GetDefault()

Get a new instance of the default [ManagedKafkaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings).

**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings)` | A new instance of the default [ManagedKafkaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
