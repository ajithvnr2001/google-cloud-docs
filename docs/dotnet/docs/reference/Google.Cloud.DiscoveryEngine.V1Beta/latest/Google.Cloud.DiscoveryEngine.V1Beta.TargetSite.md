---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite
title: Discovery Engine v1beta API - Class TargetSite (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:40.549785+00:00
---

# Discovery Engine v1beta API - Class TargetSite (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class TargetSite (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class TargetSite : IMessage<TargetSite>, IEquatable<TargetSite>, IDeepCloneable<TargetSite>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class TargetSite.

A target site for the SiteSearchEngine.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TargetSite

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TargetSite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TargetSite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TargetSite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### TargetSite()
    
    
    public TargetSite()

### TargetSite(TargetSite)
    
    
    public TargetSite(TargetSite other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TargetSite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite)`  
  
  
## Properties 

### ExactMatch
    
    
    public bool ExactMatch { get; set; }

Immutable. If set to false, a uri_pattern is generated to include all pages whose address contains the provided_uri_pattern. If set to true, an uri_pattern is generated to try to be an exact match of the provided_uri_pattern or just the specific page if the provided_uri_pattern is a specific one. provided_uri_pattern is always normalized to generate the URI pattern to be used by the search engine.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### FailureReason
    
    
    public TargetSite.Types.FailureReason FailureReason { get; set; }

Output only. Failure reason.

**Property Value**  
---  
**Type** | **Description**  
`[TargetSite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite.Types)[FailureReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite.Types.FailureReason)` |   
  
### GeneratedUriPattern
    
    
    public string GeneratedUriPattern { get; set; }

Output only. This is system-generated based on the provided_uri_pattern.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IndexingStatus
    
    
    public TargetSite.Types.IndexingStatus IndexingStatus { get; set; }

Output only. Indexing status.

**Property Value**  
---  
**Type** | **Description**  
`[TargetSite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite.Types)[IndexingStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite.Types.IndexingStatus)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The fully qualified resource name of the target site. `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}` The `target_site_id` is system-generated.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProvidedUriPattern
    
    
    public string ProvidedUriPattern { get; set; }

Required. Input only. The user provided URI pattern from which the `generated_uri_pattern` is generated.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RootDomainUri
    
    
    public string RootDomainUri { get; set; }

Output only. Root domain of the provided_uri_pattern.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SiteVerificationInfo
    
    
    public SiteVerificationInfo SiteVerificationInfo { get; set; }

Output only. Site ownership and validity verification status.

**Property Value**  
---  
**Type** | **Description**  
`[SiteVerificationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SiteVerificationInfo)` |   
  
### TargetSiteName
    
    
    public TargetSiteName TargetSiteName { get; set; }

[TargetSiteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSiteName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite#Google_Cloud_DiscoveryEngine_V1Beta_TargetSite_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TargetSiteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSiteName)` |   
  
### Type
    
    
    public TargetSite.Types.Type Type { get; set; }

The type of the target site, e.g., whether the site is to be included or excluded.

**Property Value**  
---  
**Type** | **Description**  
`[TargetSite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite.Types)[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TargetSite.Types.Type)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The target site's last updated time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
