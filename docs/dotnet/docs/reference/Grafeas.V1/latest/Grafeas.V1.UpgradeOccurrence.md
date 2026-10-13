---
url: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeOccurrence
title: Grafeas v1 API - Class UpgradeOccurrence (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:39.670464+00:00
---

# Grafeas v1 API - Class UpgradeOccurrence (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeOccurrence

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Grafeas v1 API - Class UpgradeOccurrence (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class UpgradeOccurrence : IMessage<UpgradeOccurrence>, IEquatable<UpgradeOccurrence>, IDeepCloneable<UpgradeOccurrence>, IBufferMessage, IMessage

Reference documentation and code samples for the Grafeas v1 API class UpgradeOccurrence.

An Upgrade Occurrence represents that a specific resource_url could install a specific upgrade. This presence is supplied via local sources (i.e. it is present in the mirror and the running system has noticed its availability). For Windows, both distribution and windows_update contain information for the Windows update.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpgradeOccurrence

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpgradeOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeOccurrence), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpgradeOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeOccurrence), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpgradeOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeOccurrence), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Grafeas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1)

## Assembly

Grafeas.V1.dll

## Constructors 

### UpgradeOccurrence()
    
    
    public UpgradeOccurrence()

### UpgradeOccurrence(UpgradeOccurrence)
    
    
    public UpgradeOccurrence(UpgradeOccurrence other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpgradeOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeOccurrence)`  
  
  
## Properties 

### Distribution
    
    
    public UpgradeDistribution Distribution { get; set; }

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

**Property Value**  
---  
**Type** | **Description**  
`[UpgradeDistribution](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeDistribution)` |   
  
### Package
    
    
    public string Package { get; set; }

Required for non-Windows OS. The package this Upgrade is for.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParsedVersion
    
    
    public Version ParsedVersion { get; set; }

Required for non-Windows OS. The version of the package in a machine + human readable form.

**Property Value**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Version)` |   
  
### WindowsUpdate
    
    
    public WindowsUpdate WindowsUpdate { get; set; }

Required for Windows OS. Represents the metadata about the Windows update.

**Property Value**  
---  
**Type** | **Description**  
`[WindowsUpdate](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.WindowsUpdate)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
