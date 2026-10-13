---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage
title: Google Cloud Dialogflow v2beta1 API - Class ResponseMessage (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:14.183248+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class ResponseMessage (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class ResponseMessage (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class ResponseMessage : IMessage<ResponseMessage>, IEquatable<ResponseMessage>, IDeepCloneable<ResponseMessage>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class ResponseMessage.

Response messages from an automated agent.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResponseMessage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### ResponseMessage()
    
    
    public ResponseMessage()

### ResponseMessage(ResponseMessage)
    
    
    public ResponseMessage(ResponseMessage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage)`  
  
  
## Properties 

### EndInteraction
    
    
    public ResponseMessage.Types.EndInteraction EndInteraction { get; set; }

A signal that indicates the interaction with the Dialogflow agent has ended.

**Property Value**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types)[EndInteraction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types.EndInteraction)` |   
  
### LiveAgentHandoff
    
    
    public ResponseMessage.Types.LiveAgentHandoff LiveAgentHandoff { get; set; }

Hands off conversation to a live agent.

**Property Value**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types)[LiveAgentHandoff](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types.LiveAgentHandoff)` |   
  
### MessageCase
    
    
    public ResponseMessage.MessageOneofCase MessageCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage)[MessageOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.MessageOneofCase)` |   
  
### MixedAudio
    
    
    public ResponseMessage.Types.MixedAudio MixedAudio { get; set; }

An audio response message composed of both the synthesized Dialogflow agent responses and the audios hosted in places known to the client.

**Property Value**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types)[MixedAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types.MixedAudio)` |   
  
### Payload
    
    
    public Struct Payload { get; set; }

Returns a response containing a custom, platform-specific payload.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### TelephonyTransferCall
    
    
    public ResponseMessage.Types.TelephonyTransferCall TelephonyTransferCall { get; set; }

A signal that the client should transfer the phone call connected to this agent to a third-party endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types)[TelephonyTransferCall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types.TelephonyTransferCall)` |   
  
### Text
    
    
    public ResponseMessage.Types.Text Text { get; set; }

Returns a text response.

**Property Value**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types)[Text](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ResponseMessage.Types.Text)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
