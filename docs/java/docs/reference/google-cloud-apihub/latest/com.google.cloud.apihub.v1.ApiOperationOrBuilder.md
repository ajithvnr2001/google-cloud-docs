---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperationOrBuilder
title: Interface ApiOperationOrBuilder (0.52.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:03.437439+00:00
---

# Interface ApiOperationOrBuilder (0.52.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ApiOperationOrBuilder (0.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.52.0 (latest)  0.48.0  0.47.0  0.46.0  0.44.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface ApiOperationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAttributes(String key)
    
    
    public abstract boolean containsAttributes(String key)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributes() (deprecated)
    
    
    public abstract Map<String,AttributeValues> getAttributes()

Use [#getAttributesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperationOrBuilder#com_google_cloud_apihub_v1_ApiOperationOrBuilder_getAttributesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)>` |   
  
### getAttributesCount()
    
    
    public abstract int getAttributesCount()

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributesMap()
    
    
    public abstract Map<String,AttributeValues> getAttributesMap()

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)>` |   
  
### getAttributesOrDefault(String key, AttributeValues defaultValue)
    
    
    public abstract AttributeValues getAttributesOrDefault(String key, AttributeValues defaultValue)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)` |   
  
### getAttributesOrThrow(String key)
    
    
    public abstract AttributeValues getAttributesOrThrow(String key)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time at which the operation was created.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time at which the operation was created.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDetails()
    
    
    public abstract OperationDetails getDetails()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OperationDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetails)` | The details.  
  
### getDetailsOrBuilder()
    
    
    public abstract OperationDetailsOrBuilder getDetailsOrBuilder()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OperationDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetailsOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The name of the operation.

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The name of the operation.

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSourceMetadata(int index)
    
    
    public abstract SourceMetadata getSourceMetadata(int index)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)` |   
  
### getSourceMetadataCount()
    
    
    public abstract int getSourceMetadataCount()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSourceMetadataList()
    
    
    public abstract List<SourceMetadata> getSourceMetadataList()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)>` |   
  
### getSourceMetadataOrBuilder(int index)
    
    
    public abstract SourceMetadataOrBuilder getSourceMetadataOrBuilder(int index)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SourceMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadataOrBuilder)` |   
  
### getSourceMetadataOrBuilderList()
    
    
    public abstract List<? extends SourceMetadataOrBuilder> getSourceMetadataOrBuilderList()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.apihub.v1.SourceMetadataOrBuilder>` |   
  
### getSpec()
    
    
    public abstract String getSpec()

Output only. The name of the spec will be of the format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` Note:The name of the spec will be empty if the operation is created via CreateApiOperation API.

` string spec = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The spec.  
  
### getSpecBytes()
    
    
    public abstract ByteString getSpecBytes()

Output only. The name of the spec will be of the format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` Note:The name of the spec will be empty if the operation is created via CreateApiOperation API.

` string spec = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for spec.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time at which the operation was last updated.

`.google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time at which the operation was last updated.

`.google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time at which the operation was created.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDetails()
    
    
    public abstract boolean hasDetails()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the details field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time at which the operation was last updated.

`.google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
