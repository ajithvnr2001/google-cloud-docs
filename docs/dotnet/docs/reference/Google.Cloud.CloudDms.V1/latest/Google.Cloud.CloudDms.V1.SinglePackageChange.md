---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SinglePackageChange
title: Database Migration v1 API - Class SinglePackageChange (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:41.447738+00:00
---

# Database Migration v1 API - Class SinglePackageChange (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SinglePackageChange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Migration v1 API - Class SinglePackageChange (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.5.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.4.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.3.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.2.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.1.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.0.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.2.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.1.0/Google.Cloud.CloudDms.V1.SinglePackageChange)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.0.0/Google.Cloud.CloudDms.V1.SinglePackageChange)


    
    
    public sealed class SinglePackageChange : IMessage<SinglePackageChange>, IEquatable<SinglePackageChange>, IDeepCloneable<SinglePackageChange>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Migration v1 API class SinglePackageChange.

Options to configure rule type SinglePackageChange. The rule is used to alter the sql code for a package entities.

The rule filter field can refer to one entity.

The rule scope can be: Package

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SinglePackageChange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SinglePackageChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SinglePackageChange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SinglePackageChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SinglePackageChange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SinglePackageChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SinglePackageChange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudDms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1)

## Assembly

Google.Cloud.CloudDms.V1.dll

## Constructors 

### SinglePackageChange()
    
    
    public SinglePackageChange()

### SinglePackageChange(SinglePackageChange)
    
    
    public SinglePackageChange(SinglePackageChange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SinglePackageChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SinglePackageChange)`  
  
  
## Properties 

### PackageBody
    
    
    public string PackageBody { get; set; }

Optional. Sql code for package body

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PackageDescription
    
    
    public string PackageDescription { get; set; }

Optional. Sql code for package description

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
