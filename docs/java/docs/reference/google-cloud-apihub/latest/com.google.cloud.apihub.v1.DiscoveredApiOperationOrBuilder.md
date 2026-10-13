---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DiscoveredApiOperationOrBuilder
title: Interface DiscoveredApiOperationOrBuilder (0.52.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:05.596935+00:00
---

# Interface DiscoveredApiOperationOrBuilder (0.52.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DiscoveredApiOperationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DiscoveredApiOperationOrBuilder (0.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.52.0 (latest)  0.48.0  0.47.0  0.46.0  0.44.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface DiscoveredApiOperationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getClassification()
    
    
    public abstract DiscoveredApiOperation.Classification getClassification()

Output only. The classification of the discovered API operation.

` .google.cloud.apihub.v1.DiscoveredApiOperation.Classification classification = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveredApiOperation.Classification](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DiscoveredApiOperation.Classification)` | The classification.  
  
### getClassificationValue()
    
    
    public abstract int getClassificationValue()

Output only. The classification of the discovered API operation.

` .google.cloud.apihub.v1.DiscoveredApiOperation.Classification classification = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for classification.  
  
### getCount()
    
    
    public abstract long getCount()

Optional. The number of occurrences of this API Operation.

`int64 count = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Create time stamp of the discovered API operation in API Hub.

`.google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Create time stamp of the discovered API operation in API Hub.

`.google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getFirstSeenTime()
    
    
    public abstract Timestamp getFirstSeenTime()

Optional. First seen time stamp

`.google.protobuf.Timestamp first_seen_time = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The firstSeenTime.  
  
### getFirstSeenTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getFirstSeenTimeOrBuilder()

Optional. First seen time stamp

`.google.protobuf.Timestamp first_seen_time = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getHttpOperation()
    
    
    public abstract HttpOperationDetails getHttpOperation()

Optional. An HTTP Operation.

` .google.cloud.apihub.v1.HttpOperationDetails http_operation = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[HttpOperationDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.HttpOperationDetails)` | The httpOperation.  
  
### getHttpOperationOrBuilder()
    
    
    public abstract HttpOperationDetailsOrBuilder getHttpOperationOrBuilder()

Optional. An HTTP Operation.

` .google.cloud.apihub.v1.HttpOperationDetails http_operation = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[HttpOperationDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.HttpOperationDetailsOrBuilder)` |   
  
### getLastSeenTime()
    
    
    public abstract Timestamp getLastSeenTime()

Optional. Last seen time stamp

`.google.protobuf.Timestamp last_seen_time = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastSeenTime.  
  
### getLastSeenTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastSeenTimeOrBuilder()

Optional. Last seen time stamp

`.google.protobuf.Timestamp last_seen_time = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getMatchResults(int index)
    
    
    public abstract DiscoveredApiOperation.MatchResult getMatchResults(int index)

Output only. The list of matched results for the discovered API operation. This will be populated only if the classification is known. The current usecase is for a single match. Keeping it repeated to support multiple matches in future.

` repeated .google.cloud.apihub.v1.DiscoveredApiOperation.MatchResult match_results = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredApiOperation.MatchResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DiscoveredApiOperation.MatchResult)` |   
  
### getMatchResultsCount()
    
    
    public abstract int getMatchResultsCount()

Output only. The list of matched results for the discovered API operation. This will be populated only if the classification is known. The current usecase is for a single match. Keeping it repeated to support multiple matches in future.

` repeated .google.cloud.apihub.v1.DiscoveredApiOperation.MatchResult match_results = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMatchResultsList()
    
    
    public abstract List<DiscoveredApiOperation.MatchResult> getMatchResultsList()

Output only. The list of matched results for the discovered API operation. This will be populated only if the classification is known. The current usecase is for a single match. Keeping it repeated to support multiple matches in future.

` repeated .google.cloud.apihub.v1.DiscoveredApiOperation.MatchResult match_results = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MatchResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DiscoveredApiOperation.MatchResult)>` |   
  
### getMatchResultsOrBuilder(int index)
    
    
    public abstract DiscoveredApiOperation.MatchResultOrBuilder getMatchResultsOrBuilder(int index)

Output only. The list of matched results for the discovered API operation. This will be populated only if the classification is known. The current usecase is for a single match. Keeping it repeated to support multiple matches in future.

` repeated .google.cloud.apihub.v1.DiscoveredApiOperation.MatchResult match_results = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredApiOperation.MatchResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DiscoveredApiOperation.MatchResultOrBuilder)` |   
  
### getMatchResultsOrBuilderList()
    
    
    public abstract List<? extends DiscoveredApiOperation.MatchResultOrBuilder> getMatchResultsOrBuilderList()

Output only. The list of matched results for the discovered API operation. This will be populated only if the classification is known. The current usecase is for a single match. Keeping it repeated to support multiple matches in future.

` repeated .google.cloud.apihub.v1.DiscoveredApiOperation.MatchResult match_results = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.apihub.v1.DiscoveredApiOperation.MatchResultOrBuilder>` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The name of the discovered API Operation.

Format: `projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}/discoveredApiOperations/{discovered_api_operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The name of the discovered API Operation.

Format: `projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}/discoveredApiOperations/{discovered_api_operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOperationCase()
    
    
    public abstract DiscoveredApiOperation.OperationCase getOperationCase()

**Returns**  
---  
**Type** | **Description**  
`[DiscoveredApiOperation.OperationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DiscoveredApiOperation.OperationCase)` |   
  
### getSourceMetadata()
    
    
    public abstract SourceMetadata getSourceMetadata()

Output only. The metadata of the source from which the api operation was collected.

` .google.cloud.apihub.v1.SourceMetadata source_metadata = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)` | The sourceMetadata.  
  
### getSourceMetadataOrBuilder()
    
    
    public abstract SourceMetadataOrBuilder getSourceMetadataOrBuilder()

Output only. The metadata of the source from which the api operation was collected.

` .google.cloud.apihub.v1.SourceMetadata source_metadata = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadataOrBuilder)` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Update time stamp of the discovered API operation in API Hub.

`.google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Update time stamp of the discovered API operation in API Hub.

`.google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Create time stamp of the discovered API operation in API Hub.

`.google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasFirstSeenTime()
    
    
    public abstract boolean hasFirstSeenTime()

Optional. First seen time stamp

`.google.protobuf.Timestamp first_seen_time = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the firstSeenTime field is set.  
  
### hasHttpOperation()
    
    
    public abstract boolean hasHttpOperation()

Optional. An HTTP Operation.

` .google.cloud.apihub.v1.HttpOperationDetails http_operation = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the httpOperation field is set.  
  
### hasLastSeenTime()
    
    
    public abstract boolean hasLastSeenTime()

Optional. Last seen time stamp

`.google.protobuf.Timestamp last_seen_time = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastSeenTime field is set.  
  
### hasSourceMetadata()
    
    
    public abstract boolean hasSourceMetadata()

Output only. The metadata of the source from which the api operation was collected.

` .google.cloud.apihub.v1.SourceMetadata source_metadata = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceMetadata field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Update time stamp of the discovered API operation in API Hub.

`.google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
