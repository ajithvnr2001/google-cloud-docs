---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget
title: Google Cloud Data Loss Prevention v2 API - Class CloudSqlDiscoveryTarget (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:39.557215+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class CloudSqlDiscoveryTarget (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class CloudSqlDiscoveryTarget (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class CloudSqlDiscoveryTarget : IMessage<CloudSqlDiscoveryTarget>, IEquatable<CloudSqlDiscoveryTarget>, IDeepCloneable<CloudSqlDiscoveryTarget>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class CloudSqlDiscoveryTarget.

Target used to match against for discovery with Cloud SQL tables.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudSqlDiscoveryTarget

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### CloudSqlDiscoveryTarget()
    
    
    public CloudSqlDiscoveryTarget()

### CloudSqlDiscoveryTarget(CloudSqlDiscoveryTarget)
    
    
    public CloudSqlDiscoveryTarget(CloudSqlDiscoveryTarget other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget)`  
  
  
## Properties 

### CadenceCase
    
    
    public CloudSqlDiscoveryTarget.CadenceOneofCase CadenceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget)[CadenceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget.CadenceOneofCase)` |   
  
### Conditions
    
    
    public DiscoveryCloudSqlConditions Conditions { get; set; }

In addition to matching the filter, these conditions must be true before a profile is generated.

**Property Value**  
---  
**Type** | **Description**  
`[DiscoveryCloudSqlConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlConditions)` |   
  
### Disabled
    
    
    public Disabled Disabled { get; set; }

Disable profiling for database resources that match this filter.

**Property Value**  
---  
**Type** | **Description**  
`[Disabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Disabled)` |   
  
### Filter
    
    
    public DiscoveryCloudSqlFilter Filter { get; set; }

Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table.

**Property Value**  
---  
**Type** | **Description**  
`[DiscoveryCloudSqlFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlFilter)` |   
  
### GenerationCadence
    
    
    public DiscoveryCloudSqlGenerationCadence GenerationCadence { get; set; }

How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.

**Property Value**  
---  
**Type** | **Description**  
`[DiscoveryCloudSqlGenerationCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlGenerationCadence)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
