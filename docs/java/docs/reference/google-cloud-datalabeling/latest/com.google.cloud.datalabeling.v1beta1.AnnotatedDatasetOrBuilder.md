---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotatedDatasetOrBuilder
title: Interface AnnotatedDatasetOrBuilder (0.215.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:40.700729+00:00
---

# Interface AnnotatedDatasetOrBuilder (0.215.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotatedDatasetOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AnnotatedDatasetOrBuilder (0.215.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.215.0 (latest)  0.214.0  0.213.0  0.211.0  0.208.0  0.207.0  0.205.0  0.203.0  0.202.0  0.201.0  0.200.0  0.198.0  0.196.0  0.195.0  0.194.0  0.193.0  0.192.0  0.190.0  0.188.0  0.187.0  0.184.0  0.183.0  0.182.0  0.180.0  0.179.0  0.178.0  0.177.0  0.176.0  0.175.0  0.174.0  0.173.0  0.172.0  0.171.0  0.169.0  0.168.0  0.167.0  0.166.0  0.165.0  0.164.0  0.163.0  0.162.0  0.161.0  0.160.0  0.159.0  0.157.0  0.156.0  0.155.0  0.154.0  0.153.0  0.152.0  0.151.0  0.150.0  0.149.0  0.148.0  0.147.0  0.144.0  0.143.0  0.142.0  0.141.0  0.140.0  0.139.0  0.138.0  0.137.0  0.136.0  0.135.0  0.134.0  0.133.0  0.132.0  0.131.0  0.129.0  0.128.0  0.127.0  0.126.0  0.125.0  0.124.0  0.123.7  0.122.11 
    
    
    public interface AnnotatedDatasetOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAnnotationSource()
    
    
    public abstract AnnotationSource getAnnotationSource()

Output only. Source of the annotation.

`.google.cloud.datalabeling.v1beta1.AnnotationSource annotation_source = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotationSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotationSource)` | The annotationSource.  
  
### getAnnotationSourceValue()
    
    
    public abstract int getAnnotationSourceValue()

Output only. Source of the annotation.

`.google.cloud.datalabeling.v1beta1.AnnotationSource annotation_source = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for annotationSource.  
  
### getAnnotationType()
    
    
    public abstract AnnotationType getAnnotationType()

Output only. Type of the annotation. It is specified when starting labeling task.

`.google.cloud.datalabeling.v1beta1.AnnotationType annotation_type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotationType)` | The annotationType.  
  
### getAnnotationTypeValue()
    
    
    public abstract int getAnnotationTypeValue()

Output only. Type of the annotation. It is specified when starting labeling task.

`.google.cloud.datalabeling.v1beta1.AnnotationType annotation_type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for annotationType.  
  
### getBlockingResources(int index)
    
    
    public abstract String getBlockingResources(int index)

Output only. The names of any related resources that are blocking changes to the annotated dataset.

`repeated string blocking_resources = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The blockingResources at the given index.  
  
### getBlockingResourcesBytes(int index)
    
    
    public abstract ByteString getBlockingResourcesBytes(int index)

Output only. The names of any related resources that are blocking changes to the annotated dataset.

`repeated string blocking_resources = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the blockingResources at the given index.  
  
### getBlockingResourcesCount()
    
    
    public abstract int getBlockingResourcesCount()

Output only. The names of any related resources that are blocking changes to the annotated dataset.

`repeated string blocking_resources = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of blockingResources.  
  
### getBlockingResourcesList()
    
    
    public abstract List<String> getBlockingResourcesList()

Output only. The names of any related resources that are blocking changes to the annotated dataset.

`repeated string blocking_resources = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the blockingResources.  
  
### getCompletedExampleCount()
    
    
    public abstract long getCompletedExampleCount()

Output only. Number of examples that have annotation in the annotated dataset.

`int64 completed_example_count = 5;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The completedExampleCount.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time the AnnotatedDataset was created.

`.google.protobuf.Timestamp create_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time the AnnotatedDataset was created.

`.google.protobuf.Timestamp create_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Output only. The description of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 10000 characters.

`string description = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Output only. The description of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 10000 characters.

`string description = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Output only. The display name of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 64 characters.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Output only. The display name of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 64 characters.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getExampleCount()
    
    
    public abstract long getExampleCount()

Output only. Number of examples in the annotated dataset.

`int64 example_count = 4;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The exampleCount.  
  
### getLabelStats()
    
    
    public abstract LabelStats getLabelStats()

Output only. Per label statistics.

`.google.cloud.datalabeling.v1beta1.LabelStats label_stats = 6;`

**Returns**  
---  
**Type** | **Description**  
`[LabelStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.LabelStats)` | The labelStats.  
  
### getLabelStatsOrBuilder()
    
    
    public abstract LabelStatsOrBuilder getLabelStatsOrBuilder()

Output only. Per label statistics.

`.google.cloud.datalabeling.v1beta1.LabelStats label_stats = 6;`

**Returns**  
---  
**Type** | **Description**  
`[LabelStatsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.LabelStatsOrBuilder)` |   
  
### getMetadata()
    
    
    public abstract AnnotatedDatasetMetadata getMetadata()

Output only. Additional information about AnnotatedDataset.

`.google.cloud.datalabeling.v1beta1.AnnotatedDatasetMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotatedDatasetMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotatedDatasetMetadata)` | The metadata.  
  
### getMetadataOrBuilder()
    
    
    public abstract AnnotatedDatasetMetadataOrBuilder getMetadataOrBuilder()

Output only. Additional information about AnnotatedDataset.

`.google.cloud.datalabeling.v1beta1.AnnotatedDatasetMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotatedDatasetMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotatedDatasetMetadataOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. AnnotatedDataset resource name in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id}

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. AnnotatedDataset resource name in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id}

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time the AnnotatedDataset was created.

`.google.protobuf.Timestamp create_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasLabelStats()
    
    
    public abstract boolean hasLabelStats()

Output only. Per label statistics.

`.google.cloud.datalabeling.v1beta1.LabelStats label_stats = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the labelStats field is set.  
  
### hasMetadata()
    
    
    public abstract boolean hasMetadata()

Output only. Additional information about AnnotatedDataset.

`.google.cloud.datalabeling.v1beta1.AnnotatedDatasetMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metadata field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
