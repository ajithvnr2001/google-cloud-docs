---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile
title: Gemini Enterprise for Customer Experience v1beta API - Class ChannelProfile (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:47.533703+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class ChannelProfile (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class ChannelProfile (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class ChannelProfile : IMessage<ChannelProfile>, IEquatable<ChannelProfile>, IDeepCloneable<ChannelProfile>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class ChannelProfile.

A ChannelProfile configures the agent's behavior for a specific communication channel, such as web UI or telephony.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ChannelProfile

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### ChannelProfile()
    
    
    public ChannelProfile()

### ChannelProfile(ChannelProfile)
    
    
    public ChannelProfile(ChannelProfile other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)`  
  
  
## Properties 

### ChannelType
    
    
    public ChannelProfile.Types.ChannelType ChannelType { get; set; }

Optional. The type of the channel profile.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types)[ChannelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.ChannelType)` |   
  
### DisableBargeInControl
    
    
    public bool DisableBargeInControl { get; set; }

Optional. Whether to disable user barge-in control in the conversation.

  * **true** : User interruptions are disabled while the agent is speaking.
  * **false** : The agent retains automatic control over when the user can interrupt.



**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### DisableDtmf
    
    
    public bool DisableDtmf { get; set; }

Optional. Whether to disable DTMF (dual-tone multi-frequency).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstagramConfig
    
    
    public ChannelProfile.Types.InstagramConfig InstagramConfig { get; set; }

Optional. Configuration specific to Instagram deployments.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types)[InstagramConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.InstagramConfig)` |   
  
### NoiseSuppressionLevel
    
    
    public string NoiseSuppressionLevel { get; set; }

Optional. The noise suppression level of the channel profile. Available values are "low", "moderate", "high", "very_high".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PersonaProperty
    
    
    public ChannelProfile.Types.PersonaProperty PersonaProperty { get; set; }

Optional. The persona property of the channel profile.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types)[PersonaProperty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.PersonaProperty)` |   
  
### ProfileId
    
    
    public string ProfileId { get; set; }

Optional. The unique identifier of the channel profile.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WebWidgetConfig
    
    
    public ChannelProfile.Types.WebWidgetConfig WebWidgetConfig { get; set; }

Optional. The configuration for the web widget.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types)[WebWidgetConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WebWidgetConfig)` |   
  
### WhatsappConfig
    
    
    public ChannelProfile.Types.WhatsAppConfig WhatsappConfig { get; set; }

Optional. Configuration specific to WhatsApp deployments.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types)[WhatsAppConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WhatsAppConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
