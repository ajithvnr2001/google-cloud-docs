---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger
title: Google.Apps.Script.Type - Class ComposeTrigger (2.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:04.892622+00:00
---

# Google.Apps.Script.Type - Class ComposeTrigger (2.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Apps.Script.Type - Class ComposeTrigger (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/2.3.0/Google.Apps.Script.Type.Gmail.ComposeTrigger)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/2.2.0/Google.Apps.Script.Type.Gmail.ComposeTrigger)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/2.1.0/Google.Apps.Script.Type.Gmail.ComposeTrigger)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/2.0.0/Google.Apps.Script.Type.Gmail.ComposeTrigger)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/1.1.0/Google.Apps.Script.Type.Gmail.ComposeTrigger)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/1.0.0/Google.Apps.Script.Type.Gmail.ComposeTrigger)


    
    
    public sealed class ComposeTrigger : IMessage<ComposeTrigger>, IEquatable<ComposeTrigger>, IDeepCloneable<ComposeTrigger>, IBufferMessage, IMessage

Reference documentation and code samples for the Google.Apps.Script.Type class ComposeTrigger.

A trigger that activates when user is composing an email.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ComposeTrigger

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ComposeTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ComposeTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ComposeTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Apps.Script.Type.Gmail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail)

## Assembly

Google.Apps.Script.Type.dll

## Constructors 

### ComposeTrigger()
    
    
    public ComposeTrigger()

### ComposeTrigger(ComposeTrigger)
    
    
    public ComposeTrigger(ComposeTrigger other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ComposeTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger)`  
  
  
## Properties 

### Actions
    
    
    public RepeatedField<MenuItemExtensionPoint> Actions { get; }

Defines the set of actions for compose time add-on. These are actions that user can trigger on a compose time addon.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MenuItemExtensionPoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.MenuItemExtensionPoint)` |   
  
### DraftAccess
    
    
    public ComposeTrigger.Types.DraftAccess DraftAccess { get; set; }

Define the level of data access when a compose time addon is triggered.

**Property Value**  
---  
**Type** | **Description**  
`[ComposeTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger.Types)[DraftAccess](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apps.Script.Type/latest/Google.Apps.Script.Type.Gmail.ComposeTrigger.Types.DraftAccess)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
