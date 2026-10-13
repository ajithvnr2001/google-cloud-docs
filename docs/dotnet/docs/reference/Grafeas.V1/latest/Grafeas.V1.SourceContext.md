---
url: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext
title: Grafeas v1 API - Class SourceContext (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:42.928823+00:00
---

# Grafeas v1 API - Class SourceContext (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Grafeas v1 API - Class SourceContext (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class SourceContext : IMessage<SourceContext>, IEquatable<SourceContext>, IDeepCloneable<SourceContext>, IBufferMessage, IMessage

Reference documentation and code samples for the Grafeas v1 API class SourceContext.

A SourceContext is a reference to a tree of files. A SourceContext together with a path point to a unique revision of a single file or directory.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SourceContext

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Grafeas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1)

## Assembly

Grafeas.V1.dll

## Constructors 

### SourceContext()
    
    
    public SourceContext()

### SourceContext(SourceContext)
    
    
    public SourceContext(SourceContext other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext)`  
  
  
## Properties 

### CloudRepo
    
    
    public CloudRepoSourceContext CloudRepo { get; set; }

A SourceContext referring to a revision in a Google Cloud Source Repo.

**Property Value**  
---  
**Type** | **Description**  
`[CloudRepoSourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.CloudRepoSourceContext)` |   
  
### ContextCase
    
    
    public SourceContext.ContextOneofCase ContextCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext)[ContextOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SourceContext.ContextOneofCase)` |   
  
### Gerrit
    
    
    public GerritSourceContext Gerrit { get; set; }

A SourceContext referring to a Gerrit project.

**Property Value**  
---  
**Type** | **Description**  
`[GerritSourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.GerritSourceContext)` |   
  
### Git
    
    
    public GitSourceContext Git { get; set; }

A SourceContext referring to any third party Git repo (e.g., GitHub).

**Property Value**  
---  
**Type** | **Description**  
`[GitSourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.GitSourceContext)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels with user defined metadata.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
