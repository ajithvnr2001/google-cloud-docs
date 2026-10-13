---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentConfig
title: Google Cloud Dialogflow v2 API - Class AutomatedAgentConfig (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:09.516687+00:00
---

# Google Cloud Dialogflow v2 API - Class AutomatedAgentConfig (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class AutomatedAgentConfig (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AutomatedAgentConfig : IMessage<AutomatedAgentConfig>, IEquatable<AutomatedAgentConfig>, IDeepCloneable<AutomatedAgentConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class AutomatedAgentConfig.

Defines the Automated Agent to connect to a conversation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutomatedAgentConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutomatedAgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutomatedAgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutomatedAgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### AutomatedAgentConfig()
    
    
    public AutomatedAgentConfig()

### AutomatedAgentConfig(AutomatedAgentConfig)
    
    
    public AutomatedAgentConfig(AutomatedAgentConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutomatedAgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentConfig)`  
  
  
## Properties 

### Agent
    
    
    public string Agent { get; set; }

Required. ID of the Dialogflow agent environment to use.

This project needs to either be the same project as the conversation or you need to grant `service-<Conversation Project Number>@gcp-sa-dialogflow.iam.gserviceaccount.com` the `Dialogflow API Service Agent` role in this project.

  * For ES agents, use format: `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID or '-'>`. If environment is not specified, the default `draft` environment is used. Refer to [DetectIntentRequest](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.DetectIntentRequest) for more details.

  * For CX agents, use format `projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID or '-'>`. If environment is not specified, the default `draft` environment is used.




**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AgentAsAgentName
    
    
    public AgentName AgentAsAgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentName)-typed view over the [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentConfig#Google_Cloud_Dialogflow_V2_AutomatedAgentConfig_Agent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentName)` |   
  
### SessionTtl
    
    
    public Duration SessionTtl { get; set; }

Optional. Configure lifetime of the Dialogflow session. By default, a Dialogflow CX session remains active and its data is stored for 30 minutes after the last request is sent for the session. This value should be no longer than 1 day.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
