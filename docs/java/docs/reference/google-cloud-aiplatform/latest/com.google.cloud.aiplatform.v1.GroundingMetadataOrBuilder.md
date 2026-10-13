---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingMetadataOrBuilder
title: Interface GroundingMetadataOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:18.620022+00:00
---

# Interface GroundingMetadataOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GroundingMetadataOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface GroundingMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getGoogleMapsWidgetContextToken()
    
    
    public abstract String getGoogleMapsWidgetContextToken()

Optional. Output only. Resource name of the Google Maps widget context token to be used with the PlacesContextElement widget to render contextual data. This is populated only for Google Maps grounding.

` optional string google_maps_widget_context_token = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The googleMapsWidgetContextToken.  
  
### getGoogleMapsWidgetContextTokenBytes()
    
    
    public abstract ByteString getGoogleMapsWidgetContextTokenBytes()

Optional. Output only. Resource name of the Google Maps widget context token to be used with the PlacesContextElement widget to render contextual data. This is populated only for Google Maps grounding.

` optional string google_maps_widget_context_token = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for googleMapsWidgetContextToken.  
  
### getGroundingChunks(int index)
    
    
    public abstract GroundingChunk getGroundingChunks(int index)

List of supporting references retrieved from specified grounding source.

`repeated .google.cloud.aiplatform.v1.GroundingChunk grounding_chunks = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundingChunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingChunk)` |   
  
### getGroundingChunksCount()
    
    
    public abstract int getGroundingChunksCount()

List of supporting references retrieved from specified grounding source.

`repeated .google.cloud.aiplatform.v1.GroundingChunk grounding_chunks = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getGroundingChunksList()
    
    
    public abstract List<GroundingChunk> getGroundingChunksList()

List of supporting references retrieved from specified grounding source.

`repeated .google.cloud.aiplatform.v1.GroundingChunk grounding_chunks = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GroundingChunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingChunk)>` |   
  
### getGroundingChunksOrBuilder(int index)
    
    
    public abstract GroundingChunkOrBuilder getGroundingChunksOrBuilder(int index)

List of supporting references retrieved from specified grounding source.

`repeated .google.cloud.aiplatform.v1.GroundingChunk grounding_chunks = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundingChunkOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingChunkOrBuilder)` |   
  
### getGroundingChunksOrBuilderList()
    
    
    public abstract List<? extends GroundingChunkOrBuilder> getGroundingChunksOrBuilderList()

List of supporting references retrieved from specified grounding source.

`repeated .google.cloud.aiplatform.v1.GroundingChunk grounding_chunks = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.GroundingChunkOrBuilder>` |   
  
### getGroundingSupports(int index)
    
    
    public abstract GroundingSupport getGroundingSupports(int index)

Optional. List of grounding support.

` repeated .google.cloud.aiplatform.v1.GroundingSupport grounding_supports = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundingSupport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingSupport)` |   
  
### getGroundingSupportsCount()
    
    
    public abstract int getGroundingSupportsCount()

Optional. List of grounding support.

` repeated .google.cloud.aiplatform.v1.GroundingSupport grounding_supports = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getGroundingSupportsList()
    
    
    public abstract List<GroundingSupport> getGroundingSupportsList()

Optional. List of grounding support.

` repeated .google.cloud.aiplatform.v1.GroundingSupport grounding_supports = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GroundingSupport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingSupport)>` |   
  
### getGroundingSupportsOrBuilder(int index)
    
    
    public abstract GroundingSupportOrBuilder getGroundingSupportsOrBuilder(int index)

Optional. List of grounding support.

` repeated .google.cloud.aiplatform.v1.GroundingSupport grounding_supports = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundingSupportOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingSupportOrBuilder)` |   
  
### getGroundingSupportsOrBuilderList()
    
    
    public abstract List<? extends GroundingSupportOrBuilder> getGroundingSupportsOrBuilderList()

Optional. List of grounding support.

` repeated .google.cloud.aiplatform.v1.GroundingSupport grounding_supports = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.GroundingSupportOrBuilder>` |   
  
### getRetrievalMetadata()
    
    
    public abstract RetrievalMetadata getRetrievalMetadata()

Optional. Output only. Retrieval metadata.

` optional .google.cloud.aiplatform.v1.RetrievalMetadata retrieval_metadata = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[RetrievalMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrievalMetadata)` | The retrievalMetadata.  
  
### getRetrievalMetadataOrBuilder()
    
    
    public abstract RetrievalMetadataOrBuilder getRetrievalMetadataOrBuilder()

Optional. Output only. Retrieval metadata.

` optional .google.cloud.aiplatform.v1.RetrievalMetadata retrieval_metadata = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[RetrievalMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrievalMetadataOrBuilder)` |   
  
### getRetrievalQueries(int index)
    
    
    public abstract String getRetrievalQueries(int index)

Optional. The queries that were executed by the retrieval tools. This field is populated only when the grounding source is a retrieval tool, such as Vertex AI Search.

`repeated string retrieval_queries = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The retrievalQueries at the given index.  
  
### getRetrievalQueriesBytes(int index)
    
    
    public abstract ByteString getRetrievalQueriesBytes(int index)

Optional. The queries that were executed by the retrieval tools. This field is populated only when the grounding source is a retrieval tool, such as Vertex AI Search.

`repeated string retrieval_queries = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the retrievalQueries at the given index.  
  
### getRetrievalQueriesCount()
    
    
    public abstract int getRetrievalQueriesCount()

Optional. The queries that were executed by the retrieval tools. This field is populated only when the grounding source is a retrieval tool, such as Vertex AI Search.

`repeated string retrieval_queries = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of retrievalQueries.  
  
### getRetrievalQueriesList()
    
    
    public abstract List<String> getRetrievalQueriesList()

Optional. The queries that were executed by the retrieval tools. This field is populated only when the grounding source is a retrieval tool, such as Vertex AI Search.

`repeated string retrieval_queries = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the retrievalQueries.  
  
### getSearchEntryPoint()
    
    
    public abstract SearchEntryPoint getSearchEntryPoint()

Optional. Google search entry for the following-up web searches.

` optional .google.cloud.aiplatform.v1.SearchEntryPoint search_entry_point = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchEntryPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchEntryPoint)` | The searchEntryPoint.  
  
### getSearchEntryPointOrBuilder()
    
    
    public abstract SearchEntryPointOrBuilder getSearchEntryPointOrBuilder()

Optional. Google search entry for the following-up web searches.

` optional .google.cloud.aiplatform.v1.SearchEntryPoint search_entry_point = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchEntryPointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchEntryPointOrBuilder)` |   
  
### getSourceFlaggingUris(int index)
    
    
    public abstract GroundingMetadata.SourceFlaggingUri getSourceFlaggingUris(int index)

List of source flagging uris. This is currently populated only for Google Maps grounding.

` repeated .google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUri source_flagging_uris = 9; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundingMetadata.SourceFlaggingUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUri)` |   
  
### getSourceFlaggingUrisCount()
    
    
    public abstract int getSourceFlaggingUrisCount()

List of source flagging uris. This is currently populated only for Google Maps grounding.

` repeated .google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUri source_flagging_uris = 9; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSourceFlaggingUrisList()
    
    
    public abstract List<GroundingMetadata.SourceFlaggingUri> getSourceFlaggingUrisList()

List of source flagging uris. This is currently populated only for Google Maps grounding.

` repeated .google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUri source_flagging_uris = 9; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SourceFlaggingUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUri)>` |   
  
### getSourceFlaggingUrisOrBuilder(int index)
    
    
    public abstract GroundingMetadata.SourceFlaggingUriOrBuilder getSourceFlaggingUrisOrBuilder(int index)

List of source flagging uris. This is currently populated only for Google Maps grounding.

` repeated .google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUri source_flagging_uris = 9; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundingMetadata.SourceFlaggingUriOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUriOrBuilder)` |   
  
### getSourceFlaggingUrisOrBuilderList()
    
    
    public abstract List<? extends GroundingMetadata.SourceFlaggingUriOrBuilder> getSourceFlaggingUrisOrBuilderList()

List of source flagging uris. This is currently populated only for Google Maps grounding.

` repeated .google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUri source_flagging_uris = 9; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.GroundingMetadata.SourceFlaggingUriOrBuilder>` |   
  
### getWebSearchQueries(int index)
    
    
    public abstract String getWebSearchQueries(int index)

Optional. Web search queries for the following-up web search.

`repeated string web_search_queries = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webSearchQueries at the given index.  
  
### getWebSearchQueriesBytes(int index)
    
    
    public abstract ByteString getWebSearchQueriesBytes(int index)

Optional. Web search queries for the following-up web search.

`repeated string web_search_queries = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the webSearchQueries at the given index.  
  
### getWebSearchQueriesCount()
    
    
    public abstract int getWebSearchQueriesCount()

Optional. Web search queries for the following-up web search.

`repeated string web_search_queries = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of webSearchQueries.  
  
### getWebSearchQueriesList()
    
    
    public abstract List<String> getWebSearchQueriesList()

Optional. Web search queries for the following-up web search.

`repeated string web_search_queries = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the webSearchQueries.  
  
### hasGoogleMapsWidgetContextToken()
    
    
    public abstract boolean hasGoogleMapsWidgetContextToken()

Optional. Output only. Resource name of the Google Maps widget context token to be used with the PlacesContextElement widget to render contextual data. This is populated only for Google Maps grounding.

` optional string google_maps_widget_context_token = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the googleMapsWidgetContextToken field is set.  
  
### hasRetrievalMetadata()
    
    
    public abstract boolean hasRetrievalMetadata()

Optional. Output only. Retrieval metadata.

` optional .google.cloud.aiplatform.v1.RetrievalMetadata retrieval_metadata = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the retrievalMetadata field is set.  
  
### hasSearchEntryPoint()
    
    
    public abstract boolean hasSearchEntryPoint()

Optional. Google search entry for the following-up web searches.

` optional .google.cloud.aiplatform.v1.SearchEntryPoint search_entry_point = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the searchEntryPoint field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
