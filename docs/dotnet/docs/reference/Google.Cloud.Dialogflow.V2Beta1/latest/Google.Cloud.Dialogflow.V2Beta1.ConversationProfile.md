---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile
title: Google Cloud Dialogflow v2beta1 API - Class ConversationProfile (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:12.762014+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class ConversationProfile (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class ConversationProfile (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class ConversationProfile : IMessage<ConversationProfile>, IEquatable<ConversationProfile>, IDeepCloneable<ConversationProfile>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class ConversationProfile.

Defines the services to connect to incoming Dialogflow conversations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConversationProfile

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConversationProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConversationProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConversationProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### ConversationProfile()
    
    
    public ConversationProfile()

### ConversationProfile(ConversationProfile)
    
    
    public ConversationProfile(ConversationProfile other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConversationProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile)`  
  
  
## Properties 

### AutomatedAgentConfig
    
    
    public AutomatedAgentConfig AutomatedAgentConfig { get; set; }

Configuration for an automated agent to use with this profile.

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedAgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AutomatedAgentConfig)` |   
  
### ConversationProfileName
    
    
    public ConversationProfileName ConversationProfileName { get; set; }

[ConversationProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfileName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile#Google_Cloud_Dialogflow_V2Beta1_ConversationProfile_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConversationProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfileName)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time of the conversation profile.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. Human readable name for this profile. Max length 1024 bytes.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HumanAgentAssistantConfig
    
    
    public HumanAgentAssistantConfig HumanAgentAssistantConfig { get; set; }

Configuration for agent assistance to use with this profile.

**Property Value**  
---  
**Type** | **Description**  
`[HumanAgentAssistantConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.HumanAgentAssistantConfig)` |   
  
### HumanAgentHandoffConfig
    
    
    public HumanAgentHandoffConfig HumanAgentHandoffConfig { get; set; }

Configuration for connecting to a live agent.

Currently, this feature is not general available, please contact Google to get access.

**Property Value**  
---  
**Type** | **Description**  
`[HumanAgentHandoffConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.HumanAgentHandoffConfig)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Language code for the conversation profile. If not specified, the language is en-US. Language at ConversationProfile should be set for all non en-us languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LoggingConfig
    
    
    public LoggingConfig LoggingConfig { get; set; }

Configuration for logging conversation lifecycle events.

**Property Value**  
---  
**Type** | **Description**  
`[LoggingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.LoggingConfig)` |   
  
### Name
    
    
    public string Name { get; set; }

The unique identifier of this conversation profile. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NewMessageEventNotificationConfig
    
    
    public NotificationConfig NewMessageEventNotificationConfig { get; set; }

Configuration for publishing new message events. Event will be sent in format of [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent]

**Property Value**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.NotificationConfig)` |   
  
### NewRecognitionResultNotificationConfig
    
    
    public NotificationConfig NewRecognitionResultNotificationConfig { get; set; }

Optional. Configuration for publishing transcription intermediate results. Event will be sent in format of [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent]. If configured, the following information will be populated as [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent] Pub/Sub message attributes:

  * "participant_id"
  * "participant_role"
  * "message_id"



**Property Value**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.NotificationConfig)` |   
  
### NotificationConfig
    
    
    public NotificationConfig NotificationConfig { get; set; }

Configuration for publishing conversation lifecycle events.

**Property Value**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.NotificationConfig)` |   
  
### SecuritySettings
    
    
    public string SecuritySettings { get; set; }

Name of the CX SecuritySettings reference for the agent. Format: `projects/<Project ID>/locations/<Location ID>/securitySettings/<Security Settings ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecuritySettingsAsCXSecuritySettingsName
    
    
    public CXSecuritySettingsName SecuritySettingsAsCXSecuritySettingsName { get; set; }

[CXSecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CXSecuritySettingsName)-typed view over the [SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationProfile#Google_Cloud_Dialogflow_V2Beta1_ConversationProfile_SecuritySettings) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CXSecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CXSecuritySettingsName)` |   
  
### SipConfig
    
    
    public SipConfig SipConfig { get; set; }

Optional. Configuration for SIP connections.

**Property Value**  
---  
**Type** | **Description**  
`[SipConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SipConfig)` |   
  
### SttConfig
    
    
    public SpeechToTextConfig SttConfig { get; set; }

Settings for speech transcription.

**Property Value**  
---  
**Type** | **Description**  
`[SpeechToTextConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig)` |   
  
### TimeZone
    
    
    public string TimeZone { get; set; }

The time zone of this conversational profile from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. Defaults to America/New_York.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TtsConfig
    
    
    public SynthesizeSpeechConfig TtsConfig { get; set; }

Configuration for Text-to-Speech synthesization.

Used by Phone Gateway to specify synthesization options. If agent defines synthesization options as well, agent settings overrides the option here.

**Property Value**  
---  
**Type** | **Description**  
`[SynthesizeSpeechConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SynthesizeSpeechConfig)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Update time of the conversation profile.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### UseBidiStreaming
    
    
    public bool UseBidiStreaming { get; set; }

Optional. Whether to use the bidi streaming API in telephony integration for the conversation profile.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
