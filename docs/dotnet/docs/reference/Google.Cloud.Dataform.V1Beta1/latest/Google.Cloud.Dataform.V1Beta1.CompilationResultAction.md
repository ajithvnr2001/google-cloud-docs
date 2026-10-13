---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction
title: Dataform v1beta1 API - Class CompilationResultAction (1.0.0-beta15) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:26.504683+00:00
---

# Dataform v1beta1 API - Class CompilationResultAction (1.0.0-beta15)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1beta1 API - Class CompilationResultAction (1.0.0-beta15) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta15 (latest)  1.0.0-beta14 
    
    
    public sealed class CompilationResultAction : IMessage<CompilationResultAction>, IEquatable<CompilationResultAction>, IDeepCloneable<CompilationResultAction>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataform v1beta1 API class CompilationResultAction.

Represents a single Dataform action in a compilation result.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompilationResultAction

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1)

## Assembly

Google.Cloud.Dataform.V1Beta1.dll

## Constructors 

### CompilationResultAction()
    
    
    public CompilationResultAction()

### CompilationResultAction(CompilationResultAction)
    
    
    public CompilationResultAction(CompilationResultAction other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)`  
  
  
## Properties 

### Assertion
    
    
    public CompilationResultAction.Types.Assertion Assertion { get; set; }

The assertion executed by this action.

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types)[Assertion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types.Assertion)` |   
  
### CanonicalTarget
    
    
    public Target CanonicalTarget { get; set; }

The action's identifier if the project had been compiled without any overrides configured. Unique within the compilation result.

**Property Value**  
---  
**Type** | **Description**  
`[Target](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Target)` |   
  
### CompiledObjectCase
    
    
    public CompilationResultAction.CompiledObjectOneofCase CompiledObjectCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)[CompiledObjectOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.CompiledObjectOneofCase)` |   
  
### DataPreparation
    
    
    public CompilationResultAction.Types.DataPreparation DataPreparation { get; set; }

The data preparation executed by this action.

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types)[DataPreparation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types.DataPreparation)` |   
  
### Declaration
    
    
    public CompilationResultAction.Types.Declaration Declaration { get; set; }

The declaration declared by this action.

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types)[Declaration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types.Declaration)` |   
  
### FilePath
    
    
    public string FilePath { get; set; }

The full path including filename in which this action is located, relative to the workspace root.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasInternalMetadata
    
    
    public bool HasInternalMetadata { get; }

Gets whether the "internal_metadata" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InternalMetadata
    
    
    public string InternalMetadata { get; set; }

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Notebook
    
    
    public CompilationResultAction.Types.Notebook Notebook { get; set; }

The notebook executed by this action.

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types)[Notebook](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types.Notebook)` |   
  
### Operations
    
    
    public CompilationResultAction.Types.Operations Operations { get; set; }

The database operations executed by this action.

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types)[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types.Operations)` |   
  
### Relation
    
    
    public CompilationResultAction.Types.Relation Relation { get; set; }

The database relation created/updated by this action.

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types)[Relation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultAction.Types.Relation)` |   
  
### Target
    
    
    public Target Target { get; set; }

This action's identifier. Unique within the compilation result.

**Property Value**  
---  
**Type** | **Description**  
`[Target](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Target)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
