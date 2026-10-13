---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction
title: Google Cloud Dialogflow v2 API - Class AgentCoachingInstruction (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:56.932425+00:00
---

# Google Cloud Dialogflow v2 API - Class AgentCoachingInstruction (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class AgentCoachingInstruction (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AgentCoachingInstruction : IMessage<AgentCoachingInstruction>, IEquatable<AgentCoachingInstruction>, IDeepCloneable<AgentCoachingInstruction>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class AgentCoachingInstruction.

Agent Coaching instructions that customer can configure.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentCoachingInstruction

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AgentCoachingInstruction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AgentCoachingInstruction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AgentCoachingInstruction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### AgentCoachingInstruction()
    
    
    public AgentCoachingInstruction()

### AgentCoachingInstruction(AgentCoachingInstruction)
    
    
    public AgentCoachingInstruction(AgentCoachingInstruction other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AgentCoachingInstruction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction)`  
  
  
## Properties 

### AgentAction
    
    
    public string AgentAction { get; set; }

Optional. The action that human agent should take. For example, "apologize for the slow shipping". If the users only want to use agent coaching for intent detection, agent_action can be empty

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Condition
    
    
    public string Condition { get; set; }

Optional. The condition of the instruction. For example, "the customer wants to cancel an order". If the users want the instruction to be triggered unconditionally, the condition can be empty.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayDetails
    
    
    public string DisplayDetails { get; set; }

Optional. The detailed description of this instruction.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. Display name for the instruction.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DuplicateCheckResult
    
    
    public AgentCoachingInstruction.Types.DuplicateCheckResult DuplicateCheckResult { get; set; }

Output only. Duplication check for the AgentCoachingInstruction.

**Property Value**  
---  
**Type** | **Description**  
`[AgentCoachingInstruction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction.Types)[DuplicateCheckResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction.Types.DuplicateCheckResult)` |   
  
### SystemAction
    
    
    public string SystemAction { get; set; }

Optional. The action that system should take. For example, "call GetOrderTime with order_number={order number provided by the customer}". If the users don't have plugins or don't want to trigger plugins, the system_action can be empty

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TriggeringEvent
    
    
    public AgentCoachingInstruction.Types.TriggerEvent TriggeringEvent { get; set; }

Optional. The event that should trigger this instruction. If UNSPECIFIED, the instruction triggering will be same as the generator's trigger_event.

**Property Value**  
---  
**Type** | **Description**  
`[AgentCoachingInstruction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction.Types)[TriggerEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentCoachingInstruction.Types.TriggerEvent)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
