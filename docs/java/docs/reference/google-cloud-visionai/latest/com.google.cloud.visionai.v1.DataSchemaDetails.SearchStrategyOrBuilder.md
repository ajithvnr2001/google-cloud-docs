---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategyOrBuilder
title: Interface DataSchemaDetails.SearchStrategyOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:16.529300+00:00
---

# Interface DataSchemaDetails.SearchStrategyOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataSchemaDetails.SearchStrategyOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface DataSchemaDetails.SearchStrategyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConfidenceScoreIndexConfig()
    
    
    public abstract DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig getConfidenceScoreIndexConfig()

Optional. Configs the path to the confidence score, and the threshold. Only if the score is greater than the threshold, current field will be built into the index. Only applies to leaf nodes using EXACT_SEARCH or SMART_SEARCH.

` .google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig confidence_score_index_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig)` | The confidenceScoreIndexConfig.  
  
### getConfidenceScoreIndexConfigOrBuilder()
    
    
    public abstract DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfigOrBuilder getConfidenceScoreIndexConfigOrBuilder()

Optional. Configs the path to the confidence score, and the threshold. Only if the score is greater than the threshold, current field will be built into the index. Only applies to leaf nodes using EXACT_SEARCH or SMART_SEARCH.

` .google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig confidence_score_index_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfigOrBuilder)` |   
  
### getSearchStrategyType()
    
    
    public abstract DataSchemaDetails.SearchStrategy.SearchStrategyType getSearchStrategyType()

The type of search strategy to be applied on the `key` above. The allowed `search_strategy_type` is different for different data types, which is documented in the DataSchemaDetails.DataType. Specifying unsupported `search_strategy_type` for data types will result in INVALID_ARGUMENT error.

` optional .google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.SearchStrategyType search_strategy_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.SearchStrategy.SearchStrategyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.SearchStrategyType)` | The searchStrategyType.  
  
### getSearchStrategyTypeValue()
    
    
    public abstract int getSearchStrategyTypeValue()

The type of search strategy to be applied on the `key` above. The allowed `search_strategy_type` is different for different data types, which is documented in the DataSchemaDetails.DataType. Specifying unsupported `search_strategy_type` for data types will result in INVALID_ARGUMENT error.

` optional .google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.SearchStrategyType search_strategy_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for searchStrategyType.  
  
### hasConfidenceScoreIndexConfig()
    
    
    public abstract boolean hasConfidenceScoreIndexConfig()

Optional. Configs the path to the confidence score, and the threshold. Only if the score is greater than the threshold, current field will be built into the index. Only applies to leaf nodes using EXACT_SEARCH or SMART_SEARCH.

` .google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig confidence_score_index_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the confidenceScoreIndexConfig field is set.  
  
### hasSearchStrategyType()
    
    
    public abstract boolean hasSearchStrategyType()

The type of search strategy to be applied on the `key` above. The allowed `search_strategy_type` is different for different data types, which is documented in the DataSchemaDetails.DataType. Specifying unsupported `search_strategy_type` for data types will result in INVALID_ARGUMENT error.

` optional .google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy.SearchStrategyType search_strategy_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the searchStrategyType field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
