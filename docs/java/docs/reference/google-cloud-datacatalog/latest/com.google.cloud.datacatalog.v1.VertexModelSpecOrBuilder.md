---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.VertexModelSpecOrBuilder
title: Interface VertexModelSpecOrBuilder (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:21.838619+00:00
---

# Interface VertexModelSpecOrBuilder (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.VertexModelSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface VertexModelSpecOrBuilder (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public interface VertexModelSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContainerImageUri()
    
    
    public abstract String getContainerImageUri()

URI of the Docker image to be used as the custom container for serving predictions.

`string container_image_uri = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The containerImageUri.  
  
### getContainerImageUriBytes()
    
    
    public abstract ByteString getContainerImageUriBytes()

URI of the Docker image to be used as the custom container for serving predictions.

`string container_image_uri = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for containerImageUri.  
  
### getVersionAliases(int index)
    
    
    public abstract String getVersionAliases(int index)

User provided version aliases so that a model version can be referenced via alias

`repeated string version_aliases = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The versionAliases at the given index.  
  
### getVersionAliasesBytes(int index)
    
    
    public abstract ByteString getVersionAliasesBytes(int index)

User provided version aliases so that a model version can be referenced via alias

`repeated string version_aliases = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the versionAliases at the given index.  
  
### getVersionAliasesCount()
    
    
    public abstract int getVersionAliasesCount()

User provided version aliases so that a model version can be referenced via alias

`repeated string version_aliases = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of versionAliases.  
  
### getVersionAliasesList()
    
    
    public abstract List<String> getVersionAliasesList()

User provided version aliases so that a model version can be referenced via alias

`repeated string version_aliases = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the versionAliases.  
  
### getVersionDescription()
    
    
    public abstract String getVersionDescription()

The description of this version.

`string version_description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The versionDescription.  
  
### getVersionDescriptionBytes()
    
    
    public abstract ByteString getVersionDescriptionBytes()

The description of this version.

`string version_description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for versionDescription.  
  
### getVersionId()
    
    
    public abstract String getVersionId()

The version ID of the model.

`string version_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The versionId.  
  
### getVersionIdBytes()
    
    
    public abstract ByteString getVersionIdBytes()

The version ID of the model.

`string version_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for versionId.  
  
### getVertexModelSourceInfo()
    
    
    public abstract VertexModelSourceInfo getVertexModelSourceInfo()

Source of a Vertex model.

`.google.cloud.datacatalog.v1.VertexModelSourceInfo vertex_model_source_info = 4;`

**Returns**  
---  
**Type** | **Description**  
`[VertexModelSourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.VertexModelSourceInfo)` | The vertexModelSourceInfo.  
  
### getVertexModelSourceInfoOrBuilder()
    
    
    public abstract VertexModelSourceInfoOrBuilder getVertexModelSourceInfoOrBuilder()

Source of a Vertex model.

`.google.cloud.datacatalog.v1.VertexModelSourceInfo vertex_model_source_info = 4;`

**Returns**  
---  
**Type** | **Description**  
`[VertexModelSourceInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.VertexModelSourceInfoOrBuilder)` |   
  
### hasVertexModelSourceInfo()
    
    
    public abstract boolean hasVertexModelSourceInfo()

Source of a Vertex model.

`.google.cloud.datacatalog.v1.VertexModelSourceInfo vertex_model_source_info = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vertexModelSourceInfo field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
