---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.InputConfigOrBuilder
title: Interface InputConfigOrBuilder (0.215.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:21.495963+00:00
---

# Interface InputConfigOrBuilder (0.215.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.InputConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InputConfigOrBuilder (0.215.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.215.0 (latest)  0.214.0  0.213.0  0.211.0  0.208.0  0.207.0  0.205.0  0.203.0  0.202.0  0.201.0  0.200.0  0.198.0  0.196.0  0.195.0  0.194.0  0.193.0  0.192.0  0.190.0  0.188.0  0.187.0  0.184.0  0.183.0  0.182.0  0.180.0  0.179.0  0.178.0  0.177.0  0.176.0  0.175.0  0.174.0  0.173.0  0.172.0  0.171.0  0.169.0  0.168.0  0.167.0  0.166.0  0.165.0  0.164.0  0.163.0  0.162.0  0.161.0  0.160.0  0.159.0  0.157.0  0.156.0  0.155.0  0.154.0  0.153.0  0.152.0  0.151.0  0.150.0  0.149.0  0.148.0  0.147.0  0.144.0  0.143.0  0.142.0  0.141.0  0.140.0  0.139.0  0.138.0  0.137.0  0.136.0  0.135.0  0.134.0  0.133.0  0.132.0  0.131.0  0.129.0  0.128.0  0.127.0  0.126.0  0.125.0  0.124.0  0.123.7  0.122.11 
    
    
    public interface InputConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAnnotationType()
    
    
    public abstract AnnotationType getAnnotationType()

Optional. The type of annotation to be performed on this data. You must specify this field if you are using this InputConfig in an EvaluationJob.

`.google.cloud.datalabeling.v1beta1.AnnotationType annotation_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotationType)` | The annotationType.  
  
### getAnnotationTypeValue()
    
    
    public abstract int getAnnotationTypeValue()

Optional. The type of annotation to be performed on this data. You must specify this field if you are using this InputConfig in an EvaluationJob.

`.google.cloud.datalabeling.v1beta1.AnnotationType annotation_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for annotationType.  
  
### getBigquerySource()
    
    
    public abstract BigQuerySource getBigquerySource()

Source located in BigQuery. You must specify this field if you are using this InputConfig in an EvaluationJob.

`.google.cloud.datalabeling.v1beta1.BigQuerySource bigquery_source = 5;`

**Returns**  
---  
**Type** | **Description**  
`[BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.BigQuerySource)` | The bigquerySource.  
  
### getBigquerySourceOrBuilder()
    
    
    public abstract BigQuerySourceOrBuilder getBigquerySourceOrBuilder()

Source located in BigQuery. You must specify this field if you are using this InputConfig in an EvaluationJob.

`.google.cloud.datalabeling.v1beta1.BigQuerySource bigquery_source = 5;`

**Returns**  
---  
**Type** | **Description**  
`[BigQuerySourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.BigQuerySourceOrBuilder)` |   
  
### getClassificationMetadata()
    
    
    public abstract ClassificationMetadata getClassificationMetadata()

Optional. Metadata about annotations for the input. You must specify this field if you are using this InputConfig in an EvaluationJob for a model version that performs classification.

`.google.cloud.datalabeling.v1beta1.ClassificationMetadata classification_metadata = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ClassificationMetadata)` | The classificationMetadata.  
  
### getClassificationMetadataOrBuilder()
    
    
    public abstract ClassificationMetadataOrBuilder getClassificationMetadataOrBuilder()

Optional. Metadata about annotations for the input. You must specify this field if you are using this InputConfig in an EvaluationJob for a model version that performs classification.

`.google.cloud.datalabeling.v1beta1.ClassificationMetadata classification_metadata = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ClassificationMetadataOrBuilder)` |   
  
### getDataType()
    
    
    public abstract DataType getDataType()

Required. Data type must be specifed when user tries to import data.

`.google.cloud.datalabeling.v1beta1.DataType data_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DataType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.DataType)` | The dataType.  
  
### getDataTypeMetadataCase()
    
    
    public abstract InputConfig.DataTypeMetadataCase getDataTypeMetadataCase()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig.DataTypeMetadataCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.InputConfig.DataTypeMetadataCase)` |   
  
### getDataTypeValue()
    
    
    public abstract int getDataTypeValue()

Required. Data type must be specifed when user tries to import data.

`.google.cloud.datalabeling.v1beta1.DataType data_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for dataType.  
  
### getGcsSource()
    
    
    public abstract GcsSource getGcsSource()

Source located in Cloud Storage.

`.google.cloud.datalabeling.v1beta1.GcsSource gcs_source = 2;`

**Returns**  
---  
**Type** | **Description**  
`[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.GcsSource)` | The gcsSource.  
  
### getGcsSourceOrBuilder()
    
    
    public abstract GcsSourceOrBuilder getGcsSourceOrBuilder()

Source located in Cloud Storage.

`.google.cloud.datalabeling.v1beta1.GcsSource gcs_source = 2;`

**Returns**  
---  
**Type** | **Description**  
`[GcsSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.GcsSourceOrBuilder)` |   
  
### getSourceCase()
    
    
    public abstract InputConfig.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.InputConfig.SourceCase)` |   
  
### getTextMetadata()
    
    
    public abstract TextMetadata getTextMetadata()

Required for text import, as language code must be specified.

`.google.cloud.datalabeling.v1beta1.TextMetadata text_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TextMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.TextMetadata)` | The textMetadata.  
  
### getTextMetadataOrBuilder()
    
    
    public abstract TextMetadataOrBuilder getTextMetadataOrBuilder()

Required for text import, as language code must be specified.

`.google.cloud.datalabeling.v1beta1.TextMetadata text_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TextMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.TextMetadataOrBuilder)` |   
  
### hasBigquerySource()
    
    
    public abstract boolean hasBigquerySource()

Source located in BigQuery. You must specify this field if you are using this InputConfig in an EvaluationJob.

`.google.cloud.datalabeling.v1beta1.BigQuerySource bigquery_source = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigquerySource field is set.  
  
### hasClassificationMetadata()
    
    
    public abstract boolean hasClassificationMetadata()

Optional. Metadata about annotations for the input. You must specify this field if you are using this InputConfig in an EvaluationJob for a model version that performs classification.

`.google.cloud.datalabeling.v1beta1.ClassificationMetadata classification_metadata = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the classificationMetadata field is set.  
  
### hasGcsSource()
    
    
    public abstract boolean hasGcsSource()

Source located in Cloud Storage.

`.google.cloud.datalabeling.v1beta1.GcsSource gcs_source = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsSource field is set.  
  
### hasTextMetadata()
    
    
    public abstract boolean hasTextMetadata()

Required for text import, as language code must be specified.

`.google.cloud.datalabeling.v1beta1.TextMetadata text_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the textMetadata field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
