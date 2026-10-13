---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.SimilarControls
title: Cloud Security Compliance v1 API - Class SimilarControls (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:48.656512+00:00
---

# Cloud Security Compliance v1 API - Class SimilarControls (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.SimilarControls

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Security Compliance v1 API - Class SimilarControls (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta05 (latest)  1.0.0-beta04 
    
    
    public sealed class SimilarControls : IMessage<SimilarControls>, IEquatable<SimilarControls>, IDeepCloneable<SimilarControls>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Security Compliance v1 API class SimilarControls.

The similar controls.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SimilarControls

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SimilarControls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.SimilarControls), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SimilarControls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.SimilarControls), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SimilarControls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.SimilarControls), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudSecurityCompliance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1)

## Assembly

Google.Cloud.CloudSecurityCompliance.V1.dll

## Constructors 

### SimilarControls()
    
    
    public SimilarControls()

### SimilarControls(SimilarControls)
    
    
    public SimilarControls(SimilarControls other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SimilarControls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.SimilarControls)`  
  
  
## Properties 

### ControlId
    
    
    public string ControlId { get; set; }

The ID of the control.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Framework
    
    
    public string Framework { get; set; }

The name of the framework.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
