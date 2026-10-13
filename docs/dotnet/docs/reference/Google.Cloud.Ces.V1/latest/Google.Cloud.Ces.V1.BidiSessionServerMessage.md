---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage
title: Gemini Enterprise for Customer Experience v1 API - Class BidiSessionServerMessage (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:01.680154+00:00
---

# Gemini Enterprise for Customer Experience v1 API - Class BidiSessionServerMessage (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1 API - Class BidiSessionServerMessage (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta04 
    
    
    public sealed class BidiSessionServerMessage : IMessage<BidiSessionServerMessage>, IEquatable<BidiSessionServerMessage>, IDeepCloneable<BidiSessionServerMessage>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1 API class BidiSessionServerMessage.

The top-level message returned from [SessionService.BidiRunSession][google.cloud.ces.v1.SessionService.BidiRunSession] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BidiSessionServerMessage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BidiSessionServerMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BidiSessionServerMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BidiSessionServerMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1)

## Assembly

Google.Cloud.Ces.V1.dll

## Constructors 

### BidiSessionServerMessage()
    
    
    public BidiSessionServerMessage()

### BidiSessionServerMessage(BidiSessionServerMessage)
    
    
    public BidiSessionServerMessage(BidiSessionServerMessage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BidiSessionServerMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage)`  
  
  
## Properties 

### EndSession
    
    
    public EndSession EndSession { get; set; }

Optional. Indicates that the session has ended.

**Property Value**  
---  
**Type** | **Description**  
`[EndSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.EndSession)` |   
  
### GoAway
    
    
    public GoAway GoAway { get; set; }

Optional. Indicates that the server will disconnect soon and the client should half-close and restart the connection.

**Property Value**  
---  
**Type** | **Description**  
`[GoAway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.GoAway)` |   
  
### InterruptionSignal
    
    
    public InterruptionSignal InterruptionSignal { get; set; }

Optional. Indicates the agent's audio response has been interrupted.

**Property Value**  
---  
**Type** | **Description**  
`[InterruptionSignal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.InterruptionSignal)` |   
  
### MessageTypeCase
    
    
    public BidiSessionServerMessage.MessageTypeOneofCase MessageTypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BidiSessionServerMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage)[MessageTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.BidiSessionServerMessage.MessageTypeOneofCase)` |   
  
### RecognitionResult
    
    
    public RecognitionResult RecognitionResult { get; set; }

Optional. Realtime speech recognition result for the audio input.

**Property Value**  
---  
**Type** | **Description**  
`[RecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.RecognitionResult)` |   
  
### SessionOutput
    
    
    public SessionOutput SessionOutput { get; set; }

Optional. Processing result from the CES agent.

**Property Value**  
---  
**Type** | **Description**  
`[SessionOutput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.SessionOutput)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
