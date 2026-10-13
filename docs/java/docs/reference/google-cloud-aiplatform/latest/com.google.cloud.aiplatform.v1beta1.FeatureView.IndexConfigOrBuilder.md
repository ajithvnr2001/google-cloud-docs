---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfigOrBuilder
title: Interface FeatureView.IndexConfigOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:55.844428+00:00
---

# Interface FeatureView.IndexConfigOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FeatureView.IndexConfigOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface FeatureView.IndexConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAlgorithmConfigCase()
    
    
    public abstract FeatureView.IndexConfig.AlgorithmConfigCase getAlgorithmConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[FeatureView.IndexConfig.AlgorithmConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.AlgorithmConfigCase)` |   
  
### getBruteForceConfig()
    
    
    public abstract FeatureView.IndexConfig.BruteForceConfig getBruteForceConfig()

Optional. Configuration options for using brute force search, which simply implements the standard linear search in the database for each query. It is primarily meant for benchmarking and to generate the ground truth for approximate search.

` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.BruteForceConfig brute_force_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FeatureView.IndexConfig.BruteForceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.BruteForceConfig)` | The bruteForceConfig.  
  
### getBruteForceConfigOrBuilder()
    
    
    public abstract FeatureView.IndexConfig.BruteForceConfigOrBuilder getBruteForceConfigOrBuilder()

Optional. Configuration options for using brute force search, which simply implements the standard linear search in the database for each query. It is primarily meant for benchmarking and to generate the ground truth for approximate search.

` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.BruteForceConfig brute_force_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FeatureView.IndexConfig.BruteForceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.BruteForceConfigOrBuilder)` |   
  
### getCrowdingColumn()
    
    
    public abstract String getCrowdingColumn()

Optional. Column of crowding. This column contains crowding attribute which is a constraint on a neighbor list produced by FeatureOnlineStoreService.SearchNearestEntities to diversify search results. If NearestNeighborQuery.per_crowding_attribute_neighbor_count is set to K in SearchNearestEntitiesRequest, it's guaranteed that no more than K entities of the same crowding attribute are returned in the response.

`string crowding_column = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The crowdingColumn.  
  
### getCrowdingColumnBytes()
    
    
    public abstract ByteString getCrowdingColumnBytes()

Optional. Column of crowding. This column contains crowding attribute which is a constraint on a neighbor list produced by FeatureOnlineStoreService.SearchNearestEntities to diversify search results. If NearestNeighborQuery.per_crowding_attribute_neighbor_count is set to K in SearchNearestEntitiesRequest, it's guaranteed that no more than K entities of the same crowding attribute are returned in the response.

`string crowding_column = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for crowdingColumn.  
  
### getDistanceMeasureType()
    
    
    public abstract FeatureView.IndexConfig.DistanceMeasureType getDistanceMeasureType()

Optional. The distance measure used in nearest neighbor search.

` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.DistanceMeasureType distance_measure_type = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FeatureView.IndexConfig.DistanceMeasureType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.DistanceMeasureType)` | The distanceMeasureType.  
  
### getDistanceMeasureTypeValue()
    
    
    public abstract int getDistanceMeasureTypeValue()

Optional. The distance measure used in nearest neighbor search.

` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.DistanceMeasureType distance_measure_type = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for distanceMeasureType.  
  
### getEmbeddingColumn()
    
    
    public abstract String getEmbeddingColumn()

Optional. Column of embedding. This column contains the source data to create index for vector search. embedding_column must be set when using vector search.

`string embedding_column = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The embeddingColumn.  
  
### getEmbeddingColumnBytes()
    
    
    public abstract ByteString getEmbeddingColumnBytes()

Optional. Column of embedding. This column contains the source data to create index for vector search. embedding_column must be set when using vector search.

`string embedding_column = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for embeddingColumn.  
  
### getEmbeddingDimension()
    
    
    public abstract int getEmbeddingDimension()

Optional. The number of dimensions of the input embedding.

`optional int32 embedding_dimension = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The embeddingDimension.  
  
### getFilterColumns(int index)
    
    
    public abstract String getFilterColumns(int index)

Optional. Columns of features that're used to filter vector search results.

`repeated string filter_columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filterColumns at the given index.  
  
### getFilterColumnsBytes(int index)
    
    
    public abstract ByteString getFilterColumnsBytes(int index)

Optional. Columns of features that're used to filter vector search results.

`repeated string filter_columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the filterColumns at the given index.  
  
### getFilterColumnsCount()
    
    
    public abstract int getFilterColumnsCount()

Optional. Columns of features that're used to filter vector search results.

`repeated string filter_columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of filterColumns.  
  
### getFilterColumnsList()
    
    
    public abstract List<String> getFilterColumnsList()

Optional. Columns of features that're used to filter vector search results.

`repeated string filter_columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the filterColumns.  
  
### getTreeAhConfig()
    
    
    public abstract FeatureView.IndexConfig.TreeAHConfig getTreeAhConfig()

Optional. Configuration options for the tree-AH algorithm (Shallow tree

  * Asymmetric Hashing). Please refer to this paper for more details: <https://arxiv.org/abs/1908.10396>



` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.TreeAHConfig tree_ah_config = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FeatureView.IndexConfig.TreeAHConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.TreeAHConfig)` | The treeAhConfig.  
  
### getTreeAhConfigOrBuilder()
    
    
    public abstract FeatureView.IndexConfig.TreeAHConfigOrBuilder getTreeAhConfigOrBuilder()

Optional. Configuration options for the tree-AH algorithm (Shallow tree

  * Asymmetric Hashing). Please refer to this paper for more details: <https://arxiv.org/abs/1908.10396>



` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.TreeAHConfig tree_ah_config = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FeatureView.IndexConfig.TreeAHConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.TreeAHConfigOrBuilder)` |   
  
### hasBruteForceConfig()
    
    
    public abstract boolean hasBruteForceConfig()

Optional. Configuration options for using brute force search, which simply implements the standard linear search in the database for each query. It is primarily meant for benchmarking and to generate the ground truth for approximate search.

` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.BruteForceConfig brute_force_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bruteForceConfig field is set.  
  
### hasEmbeddingDimension()
    
    
    public abstract boolean hasEmbeddingDimension()

Optional. The number of dimensions of the input embedding.

`optional int32 embedding_dimension = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the embeddingDimension field is set.  
  
### hasTreeAhConfig()
    
    
    public abstract boolean hasTreeAhConfig()

Optional. Configuration options for the tree-AH algorithm (Shallow tree

  * Asymmetric Hashing). Please refer to this paper for more details: <https://arxiv.org/abs/1908.10396>



` .google.cloud.aiplatform.v1beta1.FeatureView.IndexConfig.TreeAHConfig tree_ah_config = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the treeAhConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
