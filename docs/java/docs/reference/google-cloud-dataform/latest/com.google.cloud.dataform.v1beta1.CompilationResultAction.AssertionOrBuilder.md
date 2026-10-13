---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResultAction.AssertionOrBuilder
title: Interface CompilationResultAction.AssertionOrBuilder (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:42.746773+00:00
---

# Interface CompilationResultAction.AssertionOrBuilder (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResultAction.AssertionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CompilationResultAction.AssertionOrBuilder (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public static interface CompilationResultAction.AssertionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDependencyTargets(int index)
    
    
    public abstract Target getDependencyTargets(int index)

A list of actions that this action depends on.

`repeated .google.cloud.dataform.v1beta1.Target dependency_targets = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Target](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Target)` |   
  
### getDependencyTargetsCount()
    
    
    public abstract int getDependencyTargetsCount()

A list of actions that this action depends on.

`repeated .google.cloud.dataform.v1beta1.Target dependency_targets = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDependencyTargetsList()
    
    
    public abstract List<Target> getDependencyTargetsList()

A list of actions that this action depends on.

`repeated .google.cloud.dataform.v1beta1.Target dependency_targets = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Target](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Target)>` |   
  
### getDependencyTargetsOrBuilder(int index)
    
    
    public abstract TargetOrBuilder getDependencyTargetsOrBuilder(int index)

A list of actions that this action depends on.

`repeated .google.cloud.dataform.v1beta1.Target dependency_targets = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TargetOrBuilder)` |   
  
### getDependencyTargetsOrBuilderList()
    
    
    public abstract List<? extends TargetOrBuilder> getDependencyTargetsOrBuilderList()

A list of actions that this action depends on.

`repeated .google.cloud.dataform.v1beta1.Target dependency_targets = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dataform.v1beta1.TargetOrBuilder>` |   
  
### getDisabled()
    
    
    public abstract boolean getDisabled()

Whether this action is disabled (i.e. should not be run).

`bool disabled = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disabled.  
  
### getParentAction()
    
    
    public abstract Target getParentAction()

The parent action of this assertion. Only set if this assertion was automatically generated.

`.google.cloud.dataform.v1beta1.Target parent_action = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Target](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Target)` | The parentAction.  
  
### getParentActionOrBuilder()
    
    
    public abstract TargetOrBuilder getParentActionOrBuilder()

The parent action of this assertion. Only set if this assertion was automatically generated.

`.google.cloud.dataform.v1beta1.Target parent_action = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TargetOrBuilder)` |   
  
### getRelationDescriptor()
    
    
    public abstract RelationDescriptor getRelationDescriptor()

Descriptor for the assertion's automatically-generated view and its columns.

`.google.cloud.dataform.v1beta1.RelationDescriptor relation_descriptor = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RelationDescriptor](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RelationDescriptor)` | The relationDescriptor.  
  
### getRelationDescriptorOrBuilder()
    
    
    public abstract RelationDescriptorOrBuilder getRelationDescriptorOrBuilder()

Descriptor for the assertion's automatically-generated view and its columns.

`.google.cloud.dataform.v1beta1.RelationDescriptor relation_descriptor = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RelationDescriptorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RelationDescriptorOrBuilder)` |   
  
### getSelectQuery()
    
    
    public abstract String getSelectQuery()

The SELECT query which must return zero rows in order for this assertion to succeed.

`string select_query = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selectQuery.  
  
### getSelectQueryBytes()
    
    
    public abstract ByteString getSelectQueryBytes()

The SELECT query which must return zero rows in order for this assertion to succeed.

`string select_query = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selectQuery.  
  
### getTags(int index)
    
    
    public abstract String getTags(int index)

Arbitrary, user-defined tags on this action.

`repeated string tags = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tags at the given index.  
  
### getTagsBytes(int index)
    
    
    public abstract ByteString getTagsBytes(int index)

Arbitrary, user-defined tags on this action.

`repeated string tags = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the tags at the given index.  
  
### getTagsCount()
    
    
    public abstract int getTagsCount()

Arbitrary, user-defined tags on this action.

`repeated string tags = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of tags.  
  
### getTagsList()
    
    
    public abstract List<String> getTagsList()

Arbitrary, user-defined tags on this action.

`repeated string tags = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the tags.  
  
### hasParentAction()
    
    
    public abstract boolean hasParentAction()

The parent action of this assertion. Only set if this assertion was automatically generated.

`.google.cloud.dataform.v1beta1.Target parent_action = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parentAction field is set.  
  
### hasRelationDescriptor()
    
    
    public abstract boolean hasRelationDescriptor()

Descriptor for the assertion's automatically-generated view and its columns.

`.google.cloud.dataform.v1beta1.RelationDescriptor relation_descriptor = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the relationDescriptor field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
