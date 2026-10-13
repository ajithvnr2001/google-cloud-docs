---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition
title: Dialogflow v3 API - Class ParameterDefinition (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:27.176689+00:00
---

# Dialogflow v3 API - Class ParameterDefinition (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class ParameterDefinition (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ParameterDefinition : IMessage<ParameterDefinition>, IEquatable<ParameterDefinition>, IDeepCloneable<ParameterDefinition>, IBufferMessage, IMessage

Reference documentation and code samples for the Dialogflow v3 API class ParameterDefinition.

Defines the properties of a parameter. Used to define parameters used in the agent and the input / output parameters for each fulfillment.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ParameterDefinition

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ParameterDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ParameterDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ParameterDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Constructors 

### ParameterDefinition()
    
    
    public ParameterDefinition()

### ParameterDefinition(ParameterDefinition)
    
    
    public ParameterDefinition(ParameterDefinition other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ParameterDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition)`  
  
  
## Properties 

### Description
    
    
    public string Description { get; set; }

Human-readable description of the parameter. Limited to 300 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Name of parameter.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    [Obsolete]
    public ParameterDefinition.Types.ParameterType Type { get; set; }

Type of parameter.

**Property Value**  
---  
**Type** | **Description**  
`[ParameterDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition.Types)[ParameterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition.Types.ParameterType)` |   
  
### TypeSchema
    
    
    public TypeSchema TypeSchema { get; set; }

Optional. Type schema of parameter.

**Property Value**  
---  
**Type** | **Description**  
`[TypeSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TypeSchema)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
