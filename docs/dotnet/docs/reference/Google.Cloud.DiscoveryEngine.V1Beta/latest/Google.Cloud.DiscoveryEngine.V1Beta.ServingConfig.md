---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig
title: Discovery Engine v1beta API - Class ServingConfig (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:18.683175+00:00
---

# Discovery Engine v1beta API - Class ServingConfig (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class ServingConfig (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class ServingConfig : IMessage<ServingConfig>, IEquatable<ServingConfig>, IDeepCloneable<ServingConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class ServingConfig.

Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions). The ServingConfig is passed in the search and predict request and generates results.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServingConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### ServingConfig()
    
    
    public ServingConfig()

### ServingConfig(ServingConfig)
    
    
    public ServingConfig(ServingConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig)`  
  
  
## Properties 

### AnswerGenerationSpec
    
    
    public AnswerGenerationSpec AnswerGenerationSpec { get; set; }

Optional. The specification for answer generation.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerGenerationSpec)` |   
  
### BoostControlIds
    
    
    public RepeatedField<string> BoostControlIds { get; }

Boost controls to use in serving path. All triggered boost controls will be applied. Boost controls must be in the same data store as the serving config. Maximum of 20 boost controls.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. ServingConfig created timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. The human readable serving config display name. Used in Discovery UI.

This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DissociateControlIds
    
    
    public RepeatedField<string> DissociateControlIds { get; }

Condition do not associate specifications. If multiple do not associate conditions match, all matching do not associate controls in the list will execute. Order does not matter. Maximum number of specifications is 100.

Can only be set if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_SEARCH][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_SEARCH].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DiversityLevel
    
    
    public string DiversityLevel { get; set; }

How much diversity to use in recommendation model results e.g. `medium-diversity` or `high-diversity`. Currently supported values:

  * `no-diversity`
  * `low-diversity`
  * `medium-diversity`
  * `high-diversity`
  * `auto-diversity`



If not specified, we choose default based on recommendation model type. Default value: `no-diversity`.

Can only be set if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EmbeddingConfig
    
    
    public EmbeddingConfig EmbeddingConfig { get; set; }

Bring your own embedding config. The config is used for search semantic retrieval. The retrieval is based on the dot product of [SearchRequest.EmbeddingSpec.EmbeddingVector.vector][google.cloud.discoveryengine.v1beta.SearchRequest.EmbeddingSpec.EmbeddingVector.vector] and the document embeddings that are provided by this EmbeddingConfig. If [SearchRequest.EmbeddingSpec.EmbeddingVector.vector][google.cloud.discoveryengine.v1beta.SearchRequest.EmbeddingSpec.EmbeddingVector.vector] is provided, it overrides this [ServingConfig.embedding_config][google.cloud.discoveryengine.v1beta.ServingConfig.embedding_config].

**Property Value**  
---  
**Type** | **Description**  
`[EmbeddingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EmbeddingConfig)` |   
  
### FilterControlIds
    
    
    public RepeatedField<string> FilterControlIds { get; }

Filter controls to use in serving path. All triggered filter controls will be applied. Filter controls must be in the same data store as the serving config. Maximum of 20 filter controls.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GenericConfig
    
    
    public ServingConfig.Types.GenericConfig GenericConfig { get; set; }

The GenericConfig of the serving configuration.

**Property Value**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig.Types)[GenericConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig.Types.GenericConfig)` |   
  
### IgnoreControlIds
    
    
    public RepeatedField<string> IgnoreControlIds { get; }

Condition ignore specifications. If multiple ignore conditions match, all matching ignore controls in the list will execute. Order does not matter. Maximum number of specifications is 100.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MediaConfig
    
    
    public ServingConfig.Types.MediaConfig MediaConfig { get; set; }

The MediaConfig of the serving configuration.

**Property Value**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig.Types)[MediaConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig.Types.MediaConfig)` |   
  
### ModelId
    
    
    public string ModelId { get; set; }

The id of the model to use at serving time. Currently only RecommendationModels are supported. Can be changed but only to a compatible model (e.g. others-you-may-like CTR to others-you-may-like CVR).

Required when [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Immutable. Fully qualified name `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}/servingConfigs/{serving_config_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OnewaySynonymsControlIds
    
    
    public RepeatedField<string> OnewaySynonymsControlIds { get; }

Condition oneway synonyms specifications. If multiple oneway synonyms conditions match, all matching oneway synonyms controls in the list will execute. Maximum number of specifications is 100.

Can only be set if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_SEARCH][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_SEARCH].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PersonalizationSpec
    
    
    public SearchRequest.Types.PersonalizationSpec PersonalizationSpec { get; set; }

The specification for personalization spec.

Notice that if both [ServingConfig.personalization_spec][google.cloud.discoveryengine.v1beta.ServingConfig.personalization_spec] and [SearchRequest.personalization_spec][google.cloud.discoveryengine.v1beta.SearchRequest.personalization_spec] are set, [SearchRequest.personalization_spec][google.cloud.discoveryengine.v1beta.SearchRequest.personalization_spec] overrides [ServingConfig.personalization_spec][google.cloud.discoveryengine.v1beta.ServingConfig.personalization_spec].

**Property Value**  
---  
**Type** | **Description**  
`[SearchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchRequest.Types)[PersonalizationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchRequest.Types.PersonalizationSpec)` |   
  
### PromoteControlIds
    
    
    public RepeatedField<string> PromoteControlIds { get; }

Condition promote specifications.

Maximum number of specifications is 100.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RankingExpression
    
    
    public string RankingExpression { get; set; }

The ranking expression controls the customized ranking on retrieval documents. To leverage this, document embedding is required. The ranking expression setting in ServingConfig applies to all search requests served by the serving config. However, if `SearchRequest.ranking_expression` is specified, it overrides the ServingConfig ranking expression.

The ranking expression is a single function or multiple functions that are joined by "+".

  * ranking_expression = function, { " + ", function };



Supported functions:

  * double * relevance_score
  * double * dotProduct(embedding_field_path)



Function variables:

  * `relevance_score`: pre-defined keywords, used for measure relevance between query and document.
  * `embedding_field_path`: the document embedding field used with query embedding vector.
  * `dotProduct`: embedding function between embedding_field_path and query embedding vector.

Example ranking expression:

If document has an embedding field doc_embedding, the ranking expression could be `0.5 * relevance_score + 0.3 * dotProduct(doc_embedding)`.




**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RedirectControlIds
    
    
    public RepeatedField<string> RedirectControlIds { get; }

IDs of the redirect controls. Only the first triggered redirect action is applied, even if multiple apply. Maximum number of specifications is 100.

Can only be set if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_SEARCH][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_SEARCH].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReplacementControlIds
    
    
    public RepeatedField<string> ReplacementControlIds { get; }

Condition replacement specifications. Applied according to the order in the list. A previously replaced term can not be re-replaced. Maximum number of specifications is 100.

Can only be set if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_SEARCH][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_SEARCH].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServingConfigName
    
    
    public ServingConfigName ServingConfigName { get; set; }

[ServingConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig#Google_Cloud_DiscoveryEngine_V1Beta_ServingConfig_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServingConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName)` |   
  
### SolutionType
    
    
    public SolutionType SolutionType { get; set; }

Required. Immutable. Specifies the solution type that a serving config can be associated with.

**Property Value**  
---  
**Type** | **Description**  
`[SolutionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SolutionType)` |   
  
### SynonymsControlIds
    
    
    public RepeatedField<string> SynonymsControlIds { get; }

Condition synonyms specifications. If multiple synonyms conditions match, all matching synonyms controls in the list will execute. Maximum number of specifications is 100.

Can only be set if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_SEARCH][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_SEARCH].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. ServingConfig updated timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### VerticalConfigCase
    
    
    public ServingConfig.VerticalConfigOneofCase VerticalConfigCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig)[VerticalConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig.VerticalConfigOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
