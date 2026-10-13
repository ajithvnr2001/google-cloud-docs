---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment
title: Google Cloud Dialogflow v2 API - Class Environment (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:03.899570+00:00
---

# Google Cloud Dialogflow v2 API - Class Environment (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class Environment (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class Environment : IMessage<Environment>, IEquatable<Environment>, IDeepCloneable<Environment>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class Environment.

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the [versions and environments guide](https://cloud.google.com/dialogflow/docs/agents-versions).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Environment

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### Environment()
    
    
    public Environment()

### Environment(Environment)
    
    
    public Environment(Environment other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment)`  
  
  
## Properties 

### AgentVersion
    
    
    public string AgentVersion { get; set; }

Optional. The agent version loaded into this environment. Supported formats:

  * `projects/<Project ID>/agent/versions/<Version ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AgentVersionAsVersionName
    
    
    public VersionName AgentVersionAsVersionName { get; set; }

[VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.VersionName)-typed view over the [AgentVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment#Google_Cloud_Dialogflow_V2_Environment_AgentVersion) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.VersionName)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. The developer-provided description for this environment. The maximum length is 500 characters. If exceeded, the request is rejected.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnvironmentName
    
    
    public EnvironmentName EnvironmentName { get; set; }

[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EnvironmentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment#Google_Cloud_Dialogflow_V2_Environment_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EnvironmentName)` |   
  
### Fulfillment
    
    
    public Fulfillment Fulfillment { get; set; }

Optional. The fulfillment settings to use for this environment.

**Property Value**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Fulfillment)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The unique identifier of this agent environment. Supported formats:

  * `projects/<Project ID>/agent/environments/<Environment ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`



The environment ID for the default environment is `-`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public Environment.Types.State State { get; set; }

Output only. The state of this environment. This field is read-only, i.e., it cannot be set by create and update methods.

**Property Value**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Environment.Types.State)` |   
  
### TextToSpeechSettings
    
    
    public TextToSpeechSettings TextToSpeechSettings { get; set; }

Optional. Text to speech settings for this environment.

**Property Value**  
---  
**Type** | **Description**  
`[TextToSpeechSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.TextToSpeechSettings)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The last update time of this environment. This field is read-only, i.e., it cannot be set by create and update methods.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
