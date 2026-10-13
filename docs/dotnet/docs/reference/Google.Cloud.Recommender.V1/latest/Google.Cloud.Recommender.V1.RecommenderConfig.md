---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig
title: Google Cloud Recommender v1 API - Class RecommenderConfig (3.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:21.871113+00:00
---

# Google Cloud Recommender v1 API - Class RecommenderConfig (3.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Recommender v1 API - Class RecommenderConfig (3.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.9.0 (latest)  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.8.0  2.7.0  2.6.0  2.5.0 
    
    
    public sealed class RecommenderConfig : IMessage<RecommenderConfig>, IEquatable<RecommenderConfig>, IDeepCloneable<RecommenderConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Recommender v1 API class RecommenderConfig.

Configuration for a Recommender.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RecommenderConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RecommenderConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RecommenderConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RecommenderConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Recommender.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1)

## Assembly

Google.Cloud.Recommender.V1.dll

## Constructors 

### RecommenderConfig()
    
    
    public RecommenderConfig()

### RecommenderConfig(RecommenderConfig)
    
    
    public RecommenderConfig(RecommenderConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RecommenderConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig)`  
  
  
## Properties 

### Annotations
    
    
    public MapField<string, string> Annotations { get; }

Allows clients to store small amounts of arbitrary data. Annotations must follow the Kubernetes syntax. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

A user-settable field to provide a human-readable name to be used in user interfaces.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Fingerprint of the RecommenderConfig. Provides optimistic locking when updating.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of recommender config. Eg, projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RecommenderConfigName
    
    
    public RecommenderConfigName RecommenderConfigName { get; set; }

[RecommenderConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfigName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig#Google_Cloud_Recommender_V1_RecommenderConfig_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RecommenderConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfigName)` |   
  
### RecommenderGenerationConfig
    
    
    public RecommenderGenerationConfig RecommenderGenerationConfig { get; set; }

RecommenderGenerationConfig which configures the Generation of recommendations for this recommender.

**Property Value**  
---  
**Type** | **Description**  
`[RecommenderGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderGenerationConfig)` |   
  
### RevisionId
    
    
    public string RevisionId { get; set; }

Output only. Immutable. The revision ID of the config. A new revision is committed whenever the config is changed in any way. The format is an 8-character hexadecimal string.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Last time when the config was updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
