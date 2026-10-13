---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig
title: Vertex AI v1beta1 API - Class ModelMonitoringAlertConfig (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:26.454298+00:00
---

# Vertex AI v1beta1 API - Class ModelMonitoringAlertConfig (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ModelMonitoringAlertConfig (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ModelMonitoringAlertConfig : IMessage<ModelMonitoringAlertConfig>, IEquatable<ModelMonitoringAlertConfig>, IDeepCloneable<ModelMonitoringAlertConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class ModelMonitoringAlertConfig.

The alert config for model monitoring.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ModelMonitoringAlertConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ModelMonitoringAlertConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ModelMonitoringAlertConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ModelMonitoringAlertConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ModelMonitoringAlertConfig()
    
    
    public ModelMonitoringAlertConfig()

### ModelMonitoringAlertConfig(ModelMonitoringAlertConfig)
    
    
    public ModelMonitoringAlertConfig(ModelMonitoringAlertConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ModelMonitoringAlertConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig)`  
  
  
## Properties 

### AlertCase
    
    
    public ModelMonitoringAlertConfig.AlertOneofCase AlertCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ModelMonitoringAlertConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig)[AlertOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig.AlertOneofCase)` |   
  
### EmailAlertConfig
    
    
    public ModelMonitoringAlertConfig.Types.EmailAlertConfig EmailAlertConfig { get; set; }

Email alert config.

**Property Value**  
---  
**Type** | **Description**  
`[ModelMonitoringAlertConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig.Types)[EmailAlertConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig.Types.EmailAlertConfig)` |   
  
### EnableLogging
    
    
    public bool EnableLogging { get; set; }

Dump the anomalies to Cloud Logging. The anomalies will be put to json payload encoded from proto [google.cloud.aiplatform.logging.ModelMonitoringAnomaliesLogEntry][]. This can be further sinked to Pub/Sub or any other services supported by Cloud Logging.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### NotificationChannels
    
    
    public RepeatedField<string> NotificationChannels { get; }

Resource names of the NotificationChannels to send alert. Must be of the format `projects/<project_id_or_number>/notificationChannels/<channel_id>`

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NotificationChannelsAsNotificationChannelNames
    
    
    public ResourceNameList<NotificationChannelName> NotificationChannelsAsNotificationChannelNames { get; }

[NotificationChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotificationChannelName)-typed view over the [NotificationChannels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringAlertConfig#Google_Cloud_AIPlatform_V1Beta1_ModelMonitoringAlertConfig_NotificationChannels) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[NotificationChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotificationChannelName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
