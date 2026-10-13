---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionAlias
title: Cloud Document AI v1beta3 API - Class ProcessorVersionAlias (2.0.0-beta30) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:17.059299+00:00
---

# Cloud Document AI v1beta3 API - Class ProcessorVersionAlias (2.0.0-beta30)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionAlias

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1beta3 API - Class ProcessorVersionAlias (2.0.0-beta30) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta30 (latest)  2.0.0-beta29  1.0.0-beta04 
    
    
    public sealed class ProcessorVersionAlias : IMessage<ProcessorVersionAlias>, IEquatable<ProcessorVersionAlias>, IDeepCloneable<ProcessorVersionAlias>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Document AI v1beta3 API class ProcessorVersionAlias.

Contains the alias and the aliased resource name of processor version.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProcessorVersionAlias

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ProcessorVersionAlias](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionAlias), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProcessorVersionAlias](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionAlias), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ProcessorVersionAlias](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionAlias), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3)

## Assembly

Google.Cloud.DocumentAI.V1Beta3.dll

## Constructors 

### ProcessorVersionAlias()
    
    
    public ProcessorVersionAlias()

### ProcessorVersionAlias(ProcessorVersionAlias)
    
    
    public ProcessorVersionAlias(ProcessorVersionAlias other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProcessorVersionAlias](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionAlias)`  
  
  
## Properties 

### Alias
    
    
    public string Alias { get; set; }

The alias in the form of `processor_version` resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProcessorVersion
    
    
    public string ProcessorVersion { get; set; }

The resource name of aliased processor version.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProcessorVersionAsProcessorVersionName
    
    
    public ProcessorVersionName ProcessorVersionAsProcessorVersionName { get; set; }

[ProcessorVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionName)-typed view over the [ProcessorVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionAlias#Google_Cloud_DocumentAI_V1Beta3_ProcessorVersionAlias_ProcessorVersion) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProcessorVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessorVersionName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
