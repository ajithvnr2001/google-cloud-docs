---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationshipOrBuilder
title: Interface DataDocumentationResult.SchemaRelationshipOrBuilder (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:31.929487+00:00
---

# Interface DataDocumentationResult.SchemaRelationshipOrBuilder (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationshipOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataDocumentationResult.SchemaRelationshipOrBuilder (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 
    
    
    public static interface DataDocumentationResult.SchemaRelationshipOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLeftSchemaPaths()
    
    
    public abstract DataDocumentationResult.SchemaRelationship.SchemaPaths getLeftSchemaPaths()

Output only. An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths left_schema_paths = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDocumentationResult.SchemaRelationship.SchemaPaths](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths)` | The leftSchemaPaths.  
  
### getLeftSchemaPathsOrBuilder()
    
    
    public abstract DataDocumentationResult.SchemaRelationship.SchemaPathsOrBuilder getLeftSchemaPathsOrBuilder()

Output only. An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths left_schema_paths = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDocumentationResult.SchemaRelationship.SchemaPathsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPathsOrBuilder)` |   
  
### getRightSchemaPaths()
    
    
    public abstract DataDocumentationResult.SchemaRelationship.SchemaPaths getRightSchemaPaths()

Output only. An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths right_schema_paths = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDocumentationResult.SchemaRelationship.SchemaPaths](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths)` | The rightSchemaPaths.  
  
### getRightSchemaPathsOrBuilder()
    
    
    public abstract DataDocumentationResult.SchemaRelationship.SchemaPathsOrBuilder getRightSchemaPathsOrBuilder()

Output only. An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths right_schema_paths = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDocumentationResult.SchemaRelationship.SchemaPathsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPathsOrBuilder)` |   
  
### getSources(int index)
    
    
    public abstract DataDocumentationResult.SchemaRelationship.Source getSources(int index)

Output only. Sources which generated the schema relation edge.

` repeated .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Source sources = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[DataDocumentationResult.SchemaRelationship.Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Source)` | The sources at the given index.  
  
### getSourcesCount()
    
    
    public abstract int getSourcesCount()

Output only. Sources which generated the schema relation edge.

` repeated .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Source sources = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of sources.  
  
### getSourcesList()
    
    
    public abstract List<DataDocumentationResult.SchemaRelationship.Source> getSourcesList()

Output only. Sources which generated the schema relation edge.

` repeated .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Source sources = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Source)>` | A list containing the sources.  
  
### getSourcesValue(int index)
    
    
    public abstract int getSourcesValue(int index)

Output only. Sources which generated the schema relation edge.

` repeated .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Source sources = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of sources at the given index.  
  
### getSourcesValueList()
    
    
    public abstract List<Integer> getSourcesValueList()

Output only. Sources which generated the schema relation edge.

` repeated .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Source sources = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for sources.  
  
### getType()
    
    
    public abstract DataDocumentationResult.SchemaRelationship.Type getType()

Output only. The type of relationship between the schema paths.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Type type = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDocumentationResult.SchemaRelationship.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Output only. The type of relationship between the schema paths.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.Type type = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasLeftSchemaPaths()
    
    
    public abstract boolean hasLeftSchemaPaths()

Output only. An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths left_schema_paths = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the leftSchemaPaths field is set.  
  
### hasRightSchemaPaths()
    
    
    public abstract boolean hasRightSchemaPaths()

Output only. An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list.

` .google.cloud.dataplex.v1.DataDocumentationResult.SchemaRelationship.SchemaPaths right_schema_paths = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rightSchemaPaths field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
