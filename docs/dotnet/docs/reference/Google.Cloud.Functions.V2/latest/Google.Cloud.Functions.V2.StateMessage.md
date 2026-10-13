---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage
title: Cloud Functions v2 API - Class StateMessage (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:10.614380+00:00
---

# Cloud Functions v2 API - Class StateMessage (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2 API - Class StateMessage (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.7.0/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.6.0/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.5.0/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.4.0/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.3.0/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.2.0/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.1.0/Google.Cloud.Functions.V2.StateMessage)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.0.0/Google.Cloud.Functions.V2.StateMessage)


    
    
    public sealed class StateMessage : IMessage<StateMessage>, IEquatable<StateMessage>, IDeepCloneable<StateMessage>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v2 API class StateMessage.

Informational messages about the state of the Cloud Function or Operation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StateMessage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StateMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StateMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StateMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2)

## Assembly

Google.Cloud.Functions.V2.dll

## Constructors 

### StateMessage()
    
    
    public StateMessage()

### StateMessage(StateMessage)
    
    
    public StateMessage(StateMessage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StateMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage)`  
  
  
## Properties 

### Message
    
    
    public string Message { get; set; }

The message.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Severity
    
    
    public StateMessage.Types.Severity Severity { get; set; }

Severity of the state message.

**Property Value**  
---  
**Type** | **Description**  
`[StateMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage.Types)[Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.StateMessage.Types.Severity)` |   
  
### Type
    
    
    public string Type { get; set; }

One-word CamelCase type of the state message.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
