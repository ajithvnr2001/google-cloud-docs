---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation
title: Google Cloud Recommender v1 API - Class Recommendation (3.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:13.658643+00:00
---

# Google Cloud Recommender v1 API - Class Recommendation (3.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Recommender v1 API - Class Recommendation (3.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.9.0 (latest)  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.8.0  2.7.0  2.6.0  2.5.0 
    
    
    public sealed class Recommendation : IMessage<Recommendation>, IEquatable<Recommendation>, IDeepCloneable<Recommendation>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Recommender v1 API class Recommendation.

A recommendation along with a suggested action. E.g., a rightsizing recommendation for an underutilized VM, IAM role recommendations, etc

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Recommendation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Recommendation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Recommendation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Recommendation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Recommender.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1)

## Assembly

Google.Cloud.Recommender.V1.dll

## Constructors 

### Recommendation()
    
    
    public Recommendation()

### Recommendation(Recommendation)
    
    
    public Recommendation(Recommendation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Recommendation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation)`  
  
  
## Properties 

### AdditionalImpact
    
    
    public RepeatedField<Impact> AdditionalImpact { get; }

Optional set of additional impact that this recommendation may have when trying to optimize for the primary category. These may be positive or negative.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Impact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Impact)` |   
  
### AssociatedInsights
    
    
    public RepeatedField<Recommendation.Types.InsightReference> AssociatedInsights { get; }

Insights that led to this recommendation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Recommendation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation.Types)[InsightReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation.Types.InsightReference)` |   
  
### Content
    
    
    public RecommendationContent Content { get; set; }

Content of the recommendation describing recommended changes to resources.

**Property Value**  
---  
**Type** | **Description**  
`[RecommendationContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommendationContent)` |   
  
### Description
    
    
    public string Description { get; set; }

Free-form human readable summary in English. The maximum length is 500 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Fingerprint of the Recommendation. Provides optimistic locking when updating states.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LastRefreshTime
    
    
    public Timestamp LastRefreshTime { get; set; }

Last time this recommendation was refreshed by the system that created it in the first place.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of recommendation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrimaryImpact
    
    
    public Impact PrimaryImpact { get; set; }

The primary impact that this recommendation can have while trying to optimize for one category.

**Property Value**  
---  
**Type** | **Description**  
`[Impact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Impact)` |   
  
### Priority
    
    
    public Recommendation.Types.Priority Priority { get; set; }

Recommendation's priority.

**Property Value**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation.Types)[Priority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation.Types.Priority)` |   
  
### RecommendationName
    
    
    public RecommendationName RecommendationName { get; set; }

[RecommendationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommendationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.Recommendation#Google_Cloud_Recommender_V1_Recommendation_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RecommendationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommendationName)` |   
  
### RecommenderSubtype
    
    
    public string RecommenderSubtype { get; set; }

Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender.

Examples: For recommender = "google.iam.policy.Recommender", recommender_subtype can be one of "REMOVE_ROLE"/"REPLACE_ROLE"

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StateInfo
    
    
    public RecommendationStateInfo StateInfo { get; set; }

Information for state. Contains state and metadata.

**Property Value**  
---  
**Type** | **Description**  
`[RecommendationStateInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommendationStateInfo)` |   
  
### TargetResources
    
    
    public RepeatedField<string> TargetResources { get; }

Fully qualified resource names that this recommendation is targeting.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### XorGroupId
    
    
    public string XorGroupId { get; set; }

Corresponds to a mutually exclusive group ID within a recommender. A non-empty ID indicates that the recommendation belongs to a mutually exclusive group. This means that only one recommendation within the group is suggested to be applied.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
