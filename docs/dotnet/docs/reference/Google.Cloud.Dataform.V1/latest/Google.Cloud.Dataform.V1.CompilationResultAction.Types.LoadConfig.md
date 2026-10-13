---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig
title: Dataform v1 API - Class CompilationResultAction.Types.LoadConfig (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:35.300930+00:00
---

# Dataform v1 API - Class CompilationResultAction.Types.LoadConfig (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1 API - Class CompilationResultAction.Types.LoadConfig (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class CompilationResultAction.Types.LoadConfig : IMessage<CompilationResultAction.Types.LoadConfig>, IEquatable<CompilationResultAction.Types.LoadConfig>, IDeepCloneable<CompilationResultAction.Types.LoadConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataform v1 API class CompilationResultAction.Types.LoadConfig.

Simplified load configuration for actions

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompilationResultAction.Types.LoadConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[LoadConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[LoadConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[LoadConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1)

## Assembly

Google.Cloud.Dataform.V1.dll

## Constructors 

### LoadConfig()
    
    
    public LoadConfig()

### LoadConfig(LoadConfig)
    
    
    public LoadConfig(CompilationResultAction.Types.LoadConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[LoadConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig)`  
  
  
## Properties 

### Append
    
    
    public CompilationResultAction.Types.SimpleLoadMode Append { get; set; }

Append into destination table

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[SimpleLoadMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.SimpleLoadMode)` |   
  
### Maximum
    
    
    public CompilationResultAction.Types.IncrementalLoadMode Maximum { get; set; }

Insert records where the value exceeds the previous maximum value for a column in the destination table

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[IncrementalLoadMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.IncrementalLoadMode)` |   
  
### ModeCase
    
    
    public CompilationResultAction.Types.LoadConfig.ModeOneofCase ModeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[LoadConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig)[ModeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.LoadConfig.ModeOneofCase)` |   
  
### Replace
    
    
    public CompilationResultAction.Types.SimpleLoadMode Replace { get; set; }

Replace destination table

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[SimpleLoadMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.SimpleLoadMode)` |   
  
### Unique
    
    
    public CompilationResultAction.Types.IncrementalLoadMode Unique { get; set; }

Insert records where the value of a column is not already present in the destination table

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types)[IncrementalLoadMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.CompilationResultAction.Types.IncrementalLoadMode)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
