---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder
title: Class ClassificationEvaluationMetrics.Builder (2.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:56.202580+00:00
---

# Class ClassificationEvaluationMetrics.Builder (2.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClassificationEvaluationMetrics.Builder (2.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.95.0 (latest)  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.18  2.2.3  2.1.23 
    
    
    public static final class ClassificationEvaluationMetrics.Builder extends GeneratedMessage.Builder<ClassificationEvaluationMetrics.Builder> implements ClassificationEvaluationMetricsOrBuilder

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of "segment_classification" type.

Protobuf type `google.cloud.automl.v1.ClassificationEvaluationMetrics`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ClassificationEvaluationMetrics.Builder

## Implements

[ClassificationEvaluationMetricsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetricsOrBuilder)

## Inherited Members

[AbstractMessage.Builder.findInitializationErrors()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_findInitializationErrors__)

[AbstractMessage.Builder.getInitializationErrorString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_getInitializationErrorString__)

[AbstractMessage.Builder.internalMergeFrom(AbstractMessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_internalMergeFrom_com_google_protobuf_AbstractMessageLite_)

[AbstractMessage.Builder.mergeFrom(byte[])](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___)

[AbstractMessage.Builder.mergeFrom(byte[],ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(ByteString)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_)

[AbstractMessage.Builder.mergeFrom(ByteString,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(Message)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

[AbstractMessage.Builder.mergeFrom(InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_)

[AbstractMessage.Builder.mergeFrom(InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.newUninitializedMessageException(Message)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_newUninitializedMessageException_com_google_protobuf_Message_)

[AbstractMessage.Builder.toString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_toString__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,Collection<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_Collection___super_T__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,List<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.Builder.internalMergeFrom(MessageType)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_internalMergeFrom_MessageType_)

[AbstractMessageLite.Builder.mergeDelimitedFrom(InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeDelimitedFrom_java_io_InputStream_)

[AbstractMessageLite.Builder.mergeDelimitedFrom(InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeDelimitedFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessageLite.Builder.mergeFrom(MessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeFrom_com_google_protobuf_MessageLite_)

[AbstractMessageLite.Builder.newUninitializedMessageException(MessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_newUninitializedMessageException_com_google_protobuf_MessageLite_)

[GeneratedMessage.Builder.addRepeatedField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessage.Builder.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

[GeneratedMessage.Builder.clearField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.clearOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.clone()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clone__)

[GeneratedMessage.Builder.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getAllFields__)

[GeneratedMessage.Builder.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

[GeneratedMessage.Builder.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.getFieldBuilder(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.getParentForChildren()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getParentForChildren__)

[GeneratedMessage.Builder.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.Builder.getRepeatedFieldBuilder(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.Builder.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

com.google.protobuf.GeneratedMessage.Builder.getUnknownFieldSetBuilder()

[GeneratedMessage.Builder.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getUnknownFields__)

[GeneratedMessage.Builder.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

[GeneratedMessage.Builder.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetMapField_int_)

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

[GeneratedMessage.Builder.internalGetMutableMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetMutableMapField_int_)

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

[GeneratedMessage.Builder.isClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isClean__)

[GeneratedMessage.Builder.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

[GeneratedMessage.Builder.markClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_markClean__)

[GeneratedMessage.Builder.mergeUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessage.Builder.mergeUnknownLengthDelimitedField(int,com.google.protobuf.ByteString)

com.google.protobuf.GeneratedMessage.Builder.mergeUnknownVarintField(int,int)

[GeneratedMessage.Builder.newBuilderForField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_newBuilderForField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.onBuilt()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_onBuilt__)

[GeneratedMessage.Builder.onChanged()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_onChanged__)

com.google.protobuf.GeneratedMessage.Builder.parseUnknownField(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessage.Builder.setField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessage.Builder.setRepeatedField(Descriptors.FieldDescriptor,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

com.google.protobuf.GeneratedMessage.Builder.setUnknownFieldSetBuilder(com.google.protobuf.UnknownFieldSet.Builder)

[GeneratedMessage.Builder.setUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessage.Builder.setUnknownFieldsProto3(com.google.protobuf.UnknownFieldSet)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
## Methods 

### addAllAnnotationSpecId(Iterable<String> values)
    
    
    public ClassificationEvaluationMetrics.Builder addAllAnnotationSpecId(Iterable<String> values)

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The annotationSpecId to add.  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### addAllConfidenceMetricsEntry(Iterable<? extends ClassificationEvaluationMetrics.ConfidenceMetricsEntry> values)
    
    
    public ClassificationEvaluationMetrics.Builder addAllConfidenceMetricsEntry(Iterable<? extends ClassificationEvaluationMetrics.ConfidenceMetricsEntry> values)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### addAnnotationSpecId(String value)
    
    
    public ClassificationEvaluationMetrics.Builder addAnnotationSpecId(String value)

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The annotationSpecId to add.  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### addAnnotationSpecIdBytes(ByteString value)
    
    
    public ClassificationEvaluationMetrics.Builder addAnnotationSpecIdBytes(ByteString value)

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the annotationSpecId to add.  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### addConfidenceMetricsEntry(ClassificationEvaluationMetrics.ConfidenceMetricsEntry value)
    
    
    public ClassificationEvaluationMetrics.Builder addConfidenceMetricsEntry(ClassificationEvaluationMetrics.ConfidenceMetricsEntry value)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClassificationEvaluationMetrics.ConfidenceMetricsEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### addConfidenceMetricsEntry(ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder builderForValue)
    
    
    public ClassificationEvaluationMetrics.Builder addConfidenceMetricsEntry(ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder builderForValue)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### addConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry value)
    
    
    public ClassificationEvaluationMetrics.Builder addConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry value)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ClassificationEvaluationMetrics.ConfidenceMetricsEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### addConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder builderForValue)
    
    
    public ClassificationEvaluationMetrics.Builder addConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder builderForValue)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### addConfidenceMetricsEntryBuilder()
    
    
    public ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder addConfidenceMetricsEntryBuilder()

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder)` |   
  
### addConfidenceMetricsEntryBuilder(int index)
    
    
    public ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder addConfidenceMetricsEntryBuilder(int index)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder)` |   
  
### build()
    
    
    public ClassificationEvaluationMetrics build()

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics)` |   
  
### buildPartial()
    
    
    public ClassificationEvaluationMetrics buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics)` |   
  
### clear()
    
    
    public ClassificationEvaluationMetrics.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAnnotationSpecId()
    
    
    public ClassificationEvaluationMetrics.Builder clearAnnotationSpecId()

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### clearAuPrc()
    
    
    public ClassificationEvaluationMetrics.Builder clearAuPrc()

Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation.

`float au_prc = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### clearAuRoc()
    
    
    public ClassificationEvaluationMetrics.Builder clearAuRoc()

Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation.

`float au_roc = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### clearConfidenceMetricsEntry()
    
    
    public ClassificationEvaluationMetrics.Builder clearConfidenceMetricsEntry()

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### clearConfusionMatrix()
    
    
    public ClassificationEvaluationMetrics.Builder clearConfusionMatrix()

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### clearLogLoss()
    
    
    public ClassificationEvaluationMetrics.Builder clearLogLoss()

Output only. The Log Loss metric.

`float log_loss = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### getAnnotationSpecId(int index)
    
    
    public String getAnnotationSpecId(int index)

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The annotationSpecId at the given index.  
  
### getAnnotationSpecIdBytes(int index)
    
    
    public ByteString getAnnotationSpecIdBytes(int index)

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the annotationSpecId at the given index.  
  
### getAnnotationSpecIdCount()
    
    
    public int getAnnotationSpecIdCount()

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of annotationSpecId.  
  
### getAnnotationSpecIdList()
    
    
    public ProtocolStringList getAnnotationSpecIdList()

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the annotationSpecId.  
  
### getAuPrc()
    
    
    public float getAuPrc()

Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation.

`float au_prc = 1;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The auPrc.  
  
### getAuRoc()
    
    
    public float getAuRoc()

Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation.

`float au_roc = 6;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The auRoc.  
  
### getConfidenceMetricsEntry(int index)
    
    
    public ClassificationEvaluationMetrics.ConfidenceMetricsEntry getConfidenceMetricsEntry(int index)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfidenceMetricsEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)` |   
  
### getConfidenceMetricsEntryBuilder(int index)
    
    
    public ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder getConfidenceMetricsEntryBuilder(int index)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder)` |   
  
### getConfidenceMetricsEntryBuilderList()
    
    
    public List<ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder> getConfidenceMetricsEntryBuilderList()

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder)>` |   
  
### getConfidenceMetricsEntryCount()
    
    
    public int getConfidenceMetricsEntryCount()

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConfidenceMetricsEntryList()
    
    
    public List<ClassificationEvaluationMetrics.ConfidenceMetricsEntry> getConfidenceMetricsEntryList()

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ConfidenceMetricsEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)>` |   
  
### getConfidenceMetricsEntryOrBuilder(int index)
    
    
    public ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder getConfidenceMetricsEntryOrBuilder(int index)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder)` |   
  
### getConfidenceMetricsEntryOrBuilderList()
    
    
    public List<? extends ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder> getConfidenceMetricsEntryOrBuilderList()

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder>` |   
  
### getConfusionMatrix()
    
    
    public ClassificationEvaluationMetrics.ConfusionMatrix getConfusionMatrix()

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfusionMatrix](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix)` | The confusionMatrix.  
  
### getConfusionMatrixBuilder()
    
    
    public ClassificationEvaluationMetrics.ConfusionMatrix.Builder getConfusionMatrixBuilder()

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfusionMatrix.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix.Builder)` |   
  
### getConfusionMatrixOrBuilder()
    
    
    public ClassificationEvaluationMetrics.ConfusionMatrixOrBuilder getConfusionMatrixOrBuilder()

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.ConfusionMatrixOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrixOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public ClassificationEvaluationMetrics getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getLogLoss()
    
    
    public float getLogLoss()

Output only. The Log Loss metric.

`float log_loss = 7;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The logLoss.  
  
### hasConfusionMatrix()
    
    
    public boolean hasConfusionMatrix()

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the confusionMatrix field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeConfusionMatrix(ClassificationEvaluationMetrics.ConfusionMatrix value)
    
    
    public ClassificationEvaluationMetrics.Builder mergeConfusionMatrix(ClassificationEvaluationMetrics.ConfusionMatrix value)

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClassificationEvaluationMetrics.ConfusionMatrix](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### mergeFrom(ClassificationEvaluationMetrics other)
    
    
    public ClassificationEvaluationMetrics.Builder mergeFrom(ClassificationEvaluationMetrics other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClassificationEvaluationMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ClassificationEvaluationMetrics.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ClassificationEvaluationMetrics.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeConfidenceMetricsEntry(int index)
    
    
    public ClassificationEvaluationMetrics.Builder removeConfidenceMetricsEntry(int index)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### setAnnotationSpecId(int index, String value)
    
    
    public ClassificationEvaluationMetrics.Builder setAnnotationSpecId(int index, String value)

Output only. The annotation spec ids used for this evaluation.

`repeated string annotation_spec_id = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The annotationSpecId to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### setAuPrc(float value)
    
    
    public ClassificationEvaluationMetrics.Builder setAuPrc(float value)

Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation.

`float au_prc = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The auPrc to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### setAuRoc(float value)
    
    
    public ClassificationEvaluationMetrics.Builder setAuRoc(float value)

Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation.

`float au_roc = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The auRoc to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
### setConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry value)
    
    
    public ClassificationEvaluationMetrics.Builder setConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry value)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ClassificationEvaluationMetrics.ConfidenceMetricsEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### setConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder builderForValue)
    
    
    public ClassificationEvaluationMetrics.Builder setConfidenceMetricsEntry(int index, ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder builderForValue)

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

` repeated .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry confidence_metrics_entry = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### setConfusionMatrix(ClassificationEvaluationMetrics.ConfusionMatrix value)
    
    
    public ClassificationEvaluationMetrics.Builder setConfusionMatrix(ClassificationEvaluationMetrics.ConfusionMatrix value)

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClassificationEvaluationMetrics.ConfusionMatrix](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### setConfusionMatrix(ClassificationEvaluationMetrics.ConfusionMatrix.Builder builderForValue)
    
    
    public ClassificationEvaluationMetrics.Builder setConfusionMatrix(ClassificationEvaluationMetrics.ConfusionMatrix.Builder builderForValue)

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

` .google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix confusion_matrix = 4; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClassificationEvaluationMetrics.ConfusionMatrix.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` |   
  
### setLogLoss(float value)
    
    
    public ClassificationEvaluationMetrics.Builder setLogLoss(float value)

Output only. The Log Loss metric.

`float log_loss = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The logLoss to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ClassificationEvaluationMetrics.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
