---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter
title: Integration Connectors v1 API - Class RuntimeActionSchema.Types.InputParameter (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:15.855393+00:00
---

# Integration Connectors v1 API - Class RuntimeActionSchema.Types.InputParameter (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Integration Connectors v1 API - Class RuntimeActionSchema.Types.InputParameter (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.3.0/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.2.0/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.1.0/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.0.0/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter)


    
    
    public sealed class RuntimeActionSchema.Types.InputParameter : IMessage<RuntimeActionSchema.Types.InputParameter>, IEquatable<RuntimeActionSchema.Types.InputParameter>, IDeepCloneable<RuntimeActionSchema.Types.InputParameter>, IBufferMessage, IMessage

Reference documentation and code samples for the Integration Connectors v1 API class RuntimeActionSchema.Types.InputParameter.

Metadata of an input parameter.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RuntimeActionSchema.Types.InputParameter

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RuntimeActionSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types)[InputParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RuntimeActionSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types)[InputParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RuntimeActionSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types)[InputParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Connectors.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1)

## Assembly

Google.Cloud.Connectors.V1.dll

## Constructors 

### InputParameter()
    
    
    public InputParameter()

### InputParameter(InputParameter)
    
    
    public InputParameter(RuntimeActionSchema.Types.InputParameter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RuntimeActionSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types)[InputParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.RuntimeActionSchema.Types.InputParameter)`  
  
  
## Properties 

### DataType
    
    
    public DataType DataType { get; set; }

The data type of the Parameter.

**Property Value**  
---  
**Type** | **Description**  
`[DataType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.DataType)` |   
  
### DefaultValue
    
    
    public Value DefaultValue { get; set; }

The following field specifies the default value of the Parameter provided by the external system if a value is not provided.

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)` |   
  
### Description
    
    
    public string Description { get; set; }

A brief description of the Parameter.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Nullable
    
    
    public bool Nullable { get; set; }

Specifies whether a null value is allowed.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Parameter
    
    
    public string Parameter { get; set; }

Name of the Parameter.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
