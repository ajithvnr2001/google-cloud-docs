---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNodeOrBuilder
title: Interface PlanNodeOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:16.388073+00:00
---

# Interface PlanNodeOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNodeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PlanNodeOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface PlanNodeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChildLinks(int index)
    
    
    public abstract PlanNode.ChildLink getChildLinks(int index)

List of child node `index`es and their relationship to this parent.

`repeated .google.spanner.v1.PlanNode.ChildLink child_links = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlanNode.ChildLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNode.ChildLink)` |   
  
### getChildLinksCount()
    
    
    public abstract int getChildLinksCount()

List of child node `index`es and their relationship to this parent.

`repeated .google.spanner.v1.PlanNode.ChildLink child_links = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getChildLinksList()
    
    
    public abstract List<PlanNode.ChildLink> getChildLinksList()

List of child node `index`es and their relationship to this parent.

`repeated .google.spanner.v1.PlanNode.ChildLink child_links = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ChildLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNode.ChildLink)>` |   
  
### getChildLinksOrBuilder(int index)
    
    
    public abstract PlanNode.ChildLinkOrBuilder getChildLinksOrBuilder(int index)

List of child node `index`es and their relationship to this parent.

`repeated .google.spanner.v1.PlanNode.ChildLink child_links = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlanNode.ChildLinkOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNode.ChildLinkOrBuilder)` |   
  
### getChildLinksOrBuilderList()
    
    
    public abstract List<? extends PlanNode.ChildLinkOrBuilder> getChildLinksOrBuilderList()

List of child node `index`es and their relationship to this parent.

`repeated .google.spanner.v1.PlanNode.ChildLink child_links = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.spanner.v1.PlanNode.ChildLinkOrBuilder>` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

The display name for the node.

`string display_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

The display name for the node.

`string display_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getExecutionStats()
    
    
    public abstract Struct getExecutionStats()

The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc.

`.google.protobuf.Struct execution_stats = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The executionStats.  
  
### getExecutionStatsOrBuilder()
    
    
    public abstract StructOrBuilder getExecutionStatsOrBuilder()

The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc.

`.google.protobuf.Struct execution_stats = 7;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getIndex()
    
    
    public abstract int getIndex()

The `PlanNode`'s index in node list.

`int32 index = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The index.  
  
### getKind()
    
    
    public abstract PlanNode.Kind getKind()

Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a SCALAR node, it will have a condensed representation which can be used to directly embed a description of the node in its parent.

`.google.spanner.v1.PlanNode.Kind kind = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PlanNode.Kind](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNode.Kind)` | The kind.  
  
### getKindValue()
    
    
    public abstract int getKindValue()

Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a SCALAR node, it will have a condensed representation which can be used to directly embed a description of the node in its parent.

`.google.spanner.v1.PlanNode.Kind kind = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for kind.  
  
### getMetadata()
    
    
    public abstract Struct getMetadata()

Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata:

{ "parameter_reference": "param1", "parameter_type": "array" }

`.google.protobuf.Struct metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The metadata.  
  
### getMetadataOrBuilder()
    
    
    public abstract StructOrBuilder getMetadataOrBuilder()

Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata:

{ "parameter_reference": "param1", "parameter_type": "array" }

`.google.protobuf.Struct metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getShortRepresentation()
    
    
    public abstract PlanNode.ShortRepresentation getShortRepresentation()

Condensed representation for SCALAR nodes.

`.google.spanner.v1.PlanNode.ShortRepresentation short_representation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[PlanNode.ShortRepresentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNode.ShortRepresentation)` | The shortRepresentation.  
  
### getShortRepresentationOrBuilder()
    
    
    public abstract PlanNode.ShortRepresentationOrBuilder getShortRepresentationOrBuilder()

Condensed representation for SCALAR nodes.

`.google.spanner.v1.PlanNode.ShortRepresentation short_representation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[PlanNode.ShortRepresentationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PlanNode.ShortRepresentationOrBuilder)` |   
  
### hasExecutionStats()
    
    
    public abstract boolean hasExecutionStats()

The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc.

`.google.protobuf.Struct execution_stats = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the executionStats field is set.  
  
### hasMetadata()
    
    
    public abstract boolean hasMetadata()

Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata:

{ "parameter_reference": "param1", "parameter_type": "array" }

`.google.protobuf.Struct metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metadata field is set.  
  
### hasShortRepresentation()
    
    
    public abstract boolean hasShortRepresentation()

Condensed representation for SCALAR nodes.

`.google.spanner.v1.PlanNode.ShortRepresentation short_representation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shortRepresentation field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
