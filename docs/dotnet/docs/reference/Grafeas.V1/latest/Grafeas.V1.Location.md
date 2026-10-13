---
url: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Location
title: Grafeas v1 API - Class Location (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:56.852411+00:00
---

# Grafeas v1 API - Class Location (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Location

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Grafeas v1 API - Class Location (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class Location : IMessage<Location>, IEquatable<Location>, IDeepCloneable<Location>, IBufferMessage, IMessage

Reference documentation and code samples for the Grafeas v1 API class Location.

An occurrence of a particular package installation found within a system's filesystem. E.g., glibc was found in `/var/lib/dpkg/status`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Location

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Location](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Location), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Location](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Location), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Location](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Location), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Grafeas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1)

## Assembly

Grafeas.V1.dll

## Constructors 

### Location()
    
    
    public Location()

### Location(Location)
    
    
    public Location(Location other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Location](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Location)`  
  
  
## Properties 

### CpeUri
    
    
    public string CpeUri { get; set; }

Deprecated. The CPE URI in [CPE format](https://cpe.mitre.org/specification/)

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Path
    
    
    public string Path { get; set; }

The path from which we gathered that this package/version is installed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Version
    
    
    public Version Version { get; set; }

Deprecated. The version installed at this location.

**Property Value**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Version)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
