---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ControlFamily
title: Cloud Security Compliance v1 API - Class ControlFamily (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:49.897183+00:00
---

# Cloud Security Compliance v1 API - Class ControlFamily (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ControlFamily

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Security Compliance v1 API - Class ControlFamily (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta05 (latest)  1.0.0-beta04 
    
    
    public sealed class ControlFamily : IMessage<ControlFamily>, IEquatable<ControlFamily>, IDeepCloneable<ControlFamily>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Security Compliance v1 API class ControlFamily.

The regulatory family of the control.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ControlFamily

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ControlFamily](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ControlFamily), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ControlFamily](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ControlFamily), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ControlFamily](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ControlFamily), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudSecurityCompliance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1)

## Assembly

Google.Cloud.CloudSecurityCompliance.V1.dll

## Constructors 

### ControlFamily()
    
    
    public ControlFamily()

### ControlFamily(ControlFamily)
    
    
    public ControlFamily(ControlFamily other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ControlFamily](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ControlFamily)`  
  
  
## Properties 

### DisplayName
    
    
    public string DisplayName { get; set; }

The friendly name for the regulatory control family.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FamilyId
    
    
    public string FamilyId { get; set; }

The identifier for the regulatory control family.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
