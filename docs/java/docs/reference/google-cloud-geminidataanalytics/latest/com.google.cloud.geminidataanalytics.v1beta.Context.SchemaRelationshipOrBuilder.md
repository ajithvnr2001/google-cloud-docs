---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationshipOrBuilder
title: Interface Context.SchemaRelationshipOrBuilder (0.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:09.027117+00:00
---

# Interface Context.SchemaRelationshipOrBuilder (0.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationshipOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Context.SchemaRelationshipOrBuilder (0.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.0 (latest)  0.23.0  0.22.0  0.21.0  0.19.0  0.16.0  0.15.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface Context.SchemaRelationshipOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConfidenceScore()
    
    
    public abstract float getConfidenceScore()

Optional. A confidence score for the suggested relationship. Manually added edges have the highest confidence score.

`float confidence_score = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The confidenceScore.  
  
### getLeftSchemaPaths()
    
    
    public abstract Context.SchemaRelationship.SchemaPaths getLeftSchemaPaths()

An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list.

` .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths left_schema_paths = 1; `

**Returns**  
---  
**Type** | **Description**  
`[Context.SchemaRelationship.SchemaPaths](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths)` | The leftSchemaPaths.  
  
### getLeftSchemaPathsOrBuilder()
    
    
    public abstract Context.SchemaRelationship.SchemaPathsOrBuilder getLeftSchemaPathsOrBuilder()

An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list.

` .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths left_schema_paths = 1; `

**Returns**  
---  
**Type** | **Description**  
`[Context.SchemaRelationship.SchemaPathsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPathsOrBuilder)` |   
  
### getRightSchemaPaths()
    
    
    public abstract Context.SchemaRelationship.SchemaPaths getRightSchemaPaths()

An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list.

` .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths right_schema_paths = 2; `

**Returns**  
---  
**Type** | **Description**  
`[Context.SchemaRelationship.SchemaPaths](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths)` | The rightSchemaPaths.  
  
### getRightSchemaPathsOrBuilder()
    
    
    public abstract Context.SchemaRelationship.SchemaPathsOrBuilder getRightSchemaPathsOrBuilder()

An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list.

` .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths right_schema_paths = 2; `

**Returns**  
---  
**Type** | **Description**  
`[Context.SchemaRelationship.SchemaPathsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPathsOrBuilder)` |   
  
### getSources(int index)
    
    
    public abstract Context.SchemaRelationship.Source getSources(int index)

Optional. Sources which generated the schema relation edge.

` repeated .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.Source sources = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Context.SchemaRelationship.Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.Source)` | The sources at the given index.  
  
### getSourcesCount()
    
    
    public abstract int getSourcesCount()

Optional. Sources which generated the schema relation edge.

` repeated .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.Source sources = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of sources.  
  
### getSourcesList()
    
    
    public abstract List<Context.SchemaRelationship.Source> getSourcesList()

Optional. Sources which generated the schema relation edge.

` repeated .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.Source sources = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.Source)>` | A list containing the sources.  
  
### getSourcesValue(int index)
    
    
    public abstract int getSourcesValue(int index)

Optional. Sources which generated the schema relation edge.

` repeated .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.Source sources = 3 [(.google.api.field_behavior) = OPTIONAL]; `

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

Optional. Sources which generated the schema relation edge.

` repeated .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.Source sources = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for sources.  
  
### hasLeftSchemaPaths()
    
    
    public abstract boolean hasLeftSchemaPaths()

An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list.

` .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths left_schema_paths = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the leftSchemaPaths field is set.  
  
### hasRightSchemaPaths()
    
    
    public abstract boolean hasRightSchemaPaths()

An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list.

` .google.cloud.geminidataanalytics.v1beta.Context.SchemaRelationship.SchemaPaths right_schema_paths = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rightSchemaPaths field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
