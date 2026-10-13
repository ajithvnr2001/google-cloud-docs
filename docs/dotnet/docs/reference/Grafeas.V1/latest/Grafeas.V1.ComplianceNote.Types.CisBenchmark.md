---
url: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types.CisBenchmark
title: Grafeas v1 API - Class ComplianceNote.Types.CisBenchmark (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:11.621118+00:00
---

# Grafeas v1 API - Class ComplianceNote.Types.CisBenchmark (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types.CisBenchmark

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Grafeas v1 API - Class ComplianceNote.Types.CisBenchmark (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ComplianceNote.Types.CisBenchmark : IMessage<ComplianceNote.Types.CisBenchmark>, IEquatable<ComplianceNote.Types.CisBenchmark>, IDeepCloneable<ComplianceNote.Types.CisBenchmark>, IBufferMessage, IMessage

Reference documentation and code samples for the Grafeas v1 API class ComplianceNote.Types.CisBenchmark.

A compliance check that is a CIS benchmark.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ComplianceNote.Types.CisBenchmark

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ComplianceNote](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types)[CisBenchmark](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types.CisBenchmark), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ComplianceNote](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types)[CisBenchmark](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types.CisBenchmark), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ComplianceNote](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types)[CisBenchmark](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types.CisBenchmark), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Grafeas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1)

## Assembly

Grafeas.V1.dll

## Constructors 

### CisBenchmark()
    
    
    public CisBenchmark()

### CisBenchmark(CisBenchmark)
    
    
    public CisBenchmark(ComplianceNote.Types.CisBenchmark other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ComplianceNote](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types)[CisBenchmark](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceNote.Types.CisBenchmark)`  
  
  
## Properties 

### ProfileLevel
    
    
    public int ProfileLevel { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Severity
    
    
    public Severity Severity { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[Severity](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Severity)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
