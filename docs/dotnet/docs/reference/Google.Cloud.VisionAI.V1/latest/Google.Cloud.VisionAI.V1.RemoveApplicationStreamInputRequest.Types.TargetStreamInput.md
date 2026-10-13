---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types.TargetStreamInput
title: Vision AI v1 API - Class RemoveApplicationStreamInputRequest.Types.TargetStreamInput (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:04.987552+00:00
---

# Vision AI v1 API - Class RemoveApplicationStreamInputRequest.Types.TargetStreamInput (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types.TargetStreamInput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class RemoveApplicationStreamInputRequest.Types.TargetStreamInput (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class RemoveApplicationStreamInputRequest.Types.TargetStreamInput : IMessage<RemoveApplicationStreamInputRequest.Types.TargetStreamInput>, IEquatable<RemoveApplicationStreamInputRequest.Types.TargetStreamInput>, IDeepCloneable<RemoveApplicationStreamInputRequest.Types.TargetStreamInput>, IBufferMessage, IMessage

Reference documentation and code samples for the Vision AI v1 API class RemoveApplicationStreamInputRequest.Types.TargetStreamInput.

Message about target streamInput to remove.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RemoveApplicationStreamInputRequest.Types.TargetStreamInput

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types)[TargetStreamInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types.TargetStreamInput), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types)[TargetStreamInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types.TargetStreamInput), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types)[TargetStreamInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types.TargetStreamInput), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### TargetStreamInput()
    
    
    public TargetStreamInput()

### TargetStreamInput(TargetStreamInput)
    
    
    public TargetStreamInput(RemoveApplicationStreamInputRequest.Types.TargetStreamInput other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types)[TargetStreamInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types.TargetStreamInput)`  
  
  
## Properties 

### Stream
    
    
    public string Stream { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StreamAsStreamName
    
    
    public StreamName StreamAsStreamName { get; set; }

[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.StreamName)-typed view over the [Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest.Types.TargetStreamInput#Google_Cloud_VisionAI_V1_RemoveApplicationStreamInputRequest_Types_TargetStreamInput_Stream) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.StreamName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
