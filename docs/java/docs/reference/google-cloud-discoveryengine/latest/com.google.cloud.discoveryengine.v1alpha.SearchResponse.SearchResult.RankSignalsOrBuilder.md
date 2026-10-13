---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignalsOrBuilder
title: Interface SearchResponse.SearchResult.RankSignalsOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:06.183292+00:00
---

# Interface SearchResponse.SearchResult.RankSignalsOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignalsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchResponse.SearchResult.RankSignalsOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface SearchResponse.SearchResult.RankSignalsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBoostingFactor()
    
    
    public abstract float getBoostingFactor()

Combined custom boosts for a doc.

`optional float boosting_factor = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The boostingFactor.  
  
### getCustomSignals(int index)
    
    
    public abstract SearchResponse.SearchResult.RankSignals.CustomSignal getCustomSignals(int index)

A list of custom clearbox signals.

` repeated .google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignal custom_signals = 33 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResponse.SearchResult.RankSignals.CustomSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignal)` |   
  
### getCustomSignalsCount()
    
    
    public abstract int getCustomSignalsCount()

A list of custom clearbox signals.

` repeated .google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignal custom_signals = 33 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCustomSignalsList()
    
    
    public abstract List<SearchResponse.SearchResult.RankSignals.CustomSignal> getCustomSignalsList()

A list of custom clearbox signals.

` repeated .google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignal custom_signals = 33 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CustomSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignal)>` |   
  
### getCustomSignalsOrBuilder(int index)
    
    
    public abstract SearchResponse.SearchResult.RankSignals.CustomSignalOrBuilder getCustomSignalsOrBuilder(int index)

A list of custom clearbox signals.

` repeated .google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignal custom_signals = 33 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResponse.SearchResult.RankSignals.CustomSignalOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignalOrBuilder)` |   
  
### getCustomSignalsOrBuilderList()
    
    
    public abstract List<? extends SearchResponse.SearchResult.RankSignals.CustomSignalOrBuilder> getCustomSignalsOrBuilderList()

A list of custom clearbox signals.

` repeated .google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignal custom_signals = 33 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.discoveryengine.v1alpha.SearchResponse.SearchResult.RankSignals.CustomSignalOrBuilder>` |   
  
### getDefaultRank()
    
    
    public abstract float getDefaultRank()

The default rank of the result.

`float default_rank = 32 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The defaultRank.  
  
### getDocumentAge()
    
    
    public abstract float getDocumentAge()

Age of the document in hours.

`optional float document_age = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The documentAge.  
  
### getKeywordSimilarityScore()
    
    
    public abstract float getKeywordSimilarityScore()

Keyword matching adjustment.

` optional float keyword_similarity_score = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The keywordSimilarityScore.  
  
### getPctrRank()
    
    
    public abstract float getPctrRank()

Predicted conversion rate adjustment as a rank.

`optional float pctr_rank = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pctrRank.  
  
### getRelevanceScore()
    
    
    public abstract float getRelevanceScore()

Semantic relevance adjustment.

`optional float relevance_score = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The relevanceScore.  
  
### getSemanticSimilarityScore()
    
    
    public abstract float getSemanticSimilarityScore()

Semantic similarity adjustment.

` optional float semantic_similarity_score = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The semanticSimilarityScore.  
  
### getTopicalityRank()
    
    
    public abstract float getTopicalityRank()

Topicality adjustment as a rank.

`optional float topicality_rank = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The topicalityRank.  
  
### hasBoostingFactor()
    
    
    public abstract boolean hasBoostingFactor()

Combined custom boosts for a doc.

`optional float boosting_factor = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the boostingFactor field is set.  
  
### hasDocumentAge()
    
    
    public abstract boolean hasDocumentAge()

Age of the document in hours.

`optional float document_age = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the documentAge field is set.  
  
### hasKeywordSimilarityScore()
    
    
    public abstract boolean hasKeywordSimilarityScore()

Keyword matching adjustment.

` optional float keyword_similarity_score = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the keywordSimilarityScore field is set.  
  
### hasPctrRank()
    
    
    public abstract boolean hasPctrRank()

Predicted conversion rate adjustment as a rank.

`optional float pctr_rank = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pctrRank field is set.  
  
### hasRelevanceScore()
    
    
    public abstract boolean hasRelevanceScore()

Semantic relevance adjustment.

`optional float relevance_score = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the relevanceScore field is set.  
  
### hasSemanticSimilarityScore()
    
    
    public abstract boolean hasSemanticSimilarityScore()

Semantic similarity adjustment.

` optional float semantic_similarity_score = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the semanticSimilarityScore field is set.  
  
### hasTopicalityRank()
    
    
    public abstract boolean hasTopicalityRank()

Topicality adjustment as a rank.

`optional float topicality_rank = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the topicalityRank field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
