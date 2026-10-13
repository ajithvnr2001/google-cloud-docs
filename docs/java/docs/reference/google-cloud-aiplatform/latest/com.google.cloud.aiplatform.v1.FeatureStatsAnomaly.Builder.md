---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder
title: Class FeatureStatsAnomaly.Builder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:46.430780+00:00
---

# Class FeatureStatsAnomaly.Builder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FeatureStatsAnomaly.Builder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class FeatureStatsAnomaly.Builder extends GeneratedMessage.Builder<FeatureStatsAnomaly.Builder> implements FeatureStatsAnomalyOrBuilder

Stats and Anomaly generated at specific timestamp for specific Feature. The start_time and end_time are used to define the time range of the dataset that current stats belongs to, e.g. prediction traffic is bucketed into prediction datasets by time window. If the Dataset is not defined by time window, start_time = end_time. Timestamp of the stats and anomalies always refers to end_time. Raw stats and anomalies are stored in stats_uri or anomaly_uri in the tensorflow defined protos. Field data_stats contains almost identical information with the raw stats in Vertex AI defined proto, for UI to display.

Protobuf type `google.cloud.aiplatform.v1.FeatureStatsAnomaly`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > FeatureStatsAnomaly.Builder

## Implements

[FeatureStatsAnomalyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomalyOrBuilder)

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

### build()
    
    
    public FeatureStatsAnomaly build()

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly)` |   
  
### buildPartial()
    
    
    public FeatureStatsAnomaly buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly)` |   
  
### clear()
    
    
    public FeatureStatsAnomaly.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAnomalyDetectionThreshold()
    
    
    public FeatureStatsAnomaly.Builder clearAnomalyDetectionThreshold()

This is the threshold used when detecting anomalies. The threshold can be changed by user, so this one might be different from ThresholdConfig.value.

`double anomaly_detection_threshold = 9;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### clearAnomalyUri()
    
    
    public FeatureStatsAnomaly.Builder clearAnomalyUri()

Path of the anomaly file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/anomalies. Example: gs://monitoring_bucket/feature_name/anomalies. Stats are stored as binary format with Protobuf message Anoamlies are stored as binary format with Protobuf message [tensorflow.metadata.v0.AnomalyInfo](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/anomalies.proto).

`string anomaly_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### clearDistributionDeviation()
    
    
    public FeatureStatsAnomaly.Builder clearDistributionDeviation()

Deviation from the current stats to baseline stats.

  1. For categorical feature, the distribution distance is calculated by L-inifinity norm.
  2. For numerical feature, the distribution distance is calculated by Jensen–Shannon divergence.



`double distribution_deviation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### clearEndTime()
    
    
    public FeatureStatsAnomaly.Builder clearEndTime()

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### clearScore()
    
    
    public FeatureStatsAnomaly.Builder clearScore()

Feature importance score, only populated when cross-feature monitoring is enabled. For now only used to represent feature attribution score within range [0, 1] for ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_SKEW and ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_DRIFT.

`double score = 1;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### clearStartTime()
    
    
    public FeatureStatsAnomaly.Builder clearStartTime()

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### clearStatsUri()
    
    
    public FeatureStatsAnomaly.Builder clearStatsUri()

Path of the stats file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/stats. Example: gs://monitoring_bucket/feature_name/stats. Stats are stored as binary format with Protobuf message [tensorflow.metadata.v0.FeatureNameStatistics](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/statistics.proto).

`string stats_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### getAnomalyDetectionThreshold()
    
    
    public double getAnomalyDetectionThreshold()

This is the threshold used when detecting anomalies. The threshold can be changed by user, so this one might be different from ThresholdConfig.value.

`double anomaly_detection_threshold = 9;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The anomalyDetectionThreshold.  
  
### getAnomalyUri()
    
    
    public String getAnomalyUri()

Path of the anomaly file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/anomalies. Example: gs://monitoring_bucket/feature_name/anomalies. Stats are stored as binary format with Protobuf message Anoamlies are stored as binary format with Protobuf message [tensorflow.metadata.v0.AnomalyInfo](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/anomalies.proto).

`string anomaly_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The anomalyUri.  
  
### getAnomalyUriBytes()
    
    
    public ByteString getAnomalyUriBytes()

Path of the anomaly file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/anomalies. Example: gs://monitoring_bucket/feature_name/anomalies. Stats are stored as binary format with Protobuf message Anoamlies are stored as binary format with Protobuf message [tensorflow.metadata.v0.AnomalyInfo](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/anomalies.proto).

`string anomaly_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for anomalyUri.  
  
### getDefaultInstanceForType()
    
    
    public FeatureStatsAnomaly getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDistributionDeviation()
    
    
    public double getDistributionDeviation()

Deviation from the current stats to baseline stats.

  1. For categorical feature, the distribution distance is calculated by L-inifinity norm.
  2. For numerical feature, the distribution distance is calculated by Jensen–Shannon divergence.



`double distribution_deviation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The distributionDeviation.  
  
### getEndTime()
    
    
    public Timestamp getEndTime()

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeBuilder()
    
    
    public Timestamp.Builder getEndTimeBuilder()

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getEndTimeOrBuilder()
    
    
    public TimestampOrBuilder getEndTimeOrBuilder()

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getScore()
    
    
    public double getScore()

Feature importance score, only populated when cross-feature monitoring is enabled. For now only used to represent feature attribution score within range [0, 1] for ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_SKEW and ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_DRIFT.

`double score = 1;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The score.  
  
### getStartTime()
    
    
    public Timestamp getStartTime()

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeBuilder()
    
    
    public Timestamp.Builder getStartTimeBuilder()

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getStartTimeOrBuilder()
    
    
    public TimestampOrBuilder getStartTimeOrBuilder()

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStatsUri()
    
    
    public String getStatsUri()

Path of the stats file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/stats. Example: gs://monitoring_bucket/feature_name/stats. Stats are stored as binary format with Protobuf message [tensorflow.metadata.v0.FeatureNameStatistics](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/statistics.proto).

`string stats_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The statsUri.  
  
### getStatsUriBytes()
    
    
    public ByteString getStatsUriBytes()

Path of the stats file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/stats. Example: gs://monitoring_bucket/feature_name/stats. Stats are stored as binary format with Protobuf message [tensorflow.metadata.v0.FeatureNameStatistics](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/statistics.proto).

`string stats_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for statsUri.  
  
### hasEndTime()
    
    
    public boolean hasEndTime()

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasStartTime()
    
    
    public boolean hasStartTime()

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
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

### mergeEndTime(Timestamp value)
    
    
    public FeatureStatsAnomaly.Builder mergeEndTime(Timestamp value)

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### mergeFrom(FeatureStatsAnomaly other)
    
    
    public FeatureStatsAnomaly.Builder mergeFrom(FeatureStatsAnomaly other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FeatureStatsAnomaly](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public FeatureStatsAnomaly.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public FeatureStatsAnomaly.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeStartTime(Timestamp value)
    
    
    public FeatureStatsAnomaly.Builder mergeStartTime(Timestamp value)

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### setAnomalyDetectionThreshold(double value)
    
    
    public FeatureStatsAnomaly.Builder setAnomalyDetectionThreshold(double value)

This is the threshold used when detecting anomalies. The threshold can be changed by user, so this one might be different from ThresholdConfig.value.

`double anomaly_detection_threshold = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The anomalyDetectionThreshold to set.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### setAnomalyUri(String value)
    
    
    public FeatureStatsAnomaly.Builder setAnomalyUri(String value)

Path of the anomaly file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/anomalies. Example: gs://monitoring_bucket/feature_name/anomalies. Stats are stored as binary format with Protobuf message Anoamlies are stored as binary format with Protobuf message [tensorflow.metadata.v0.AnomalyInfo](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/anomalies.proto).

`string anomaly_uri = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The anomalyUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### setAnomalyUriBytes(ByteString value)
    
    
    public FeatureStatsAnomaly.Builder setAnomalyUriBytes(ByteString value)

Path of the anomaly file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/anomalies. Example: gs://monitoring_bucket/feature_name/anomalies. Stats are stored as binary format with Protobuf message Anoamlies are stored as binary format with Protobuf message [tensorflow.metadata.v0.AnomalyInfo](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/anomalies.proto).

`string anomaly_uri = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for anomalyUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### setDistributionDeviation(double value)
    
    
    public FeatureStatsAnomaly.Builder setDistributionDeviation(double value)

Deviation from the current stats to baseline stats.

  1. For categorical feature, the distribution distance is calculated by L-inifinity norm.
  2. For numerical feature, the distribution distance is calculated by Jensen–Shannon divergence.



`double distribution_deviation = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The distributionDeviation to set.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### setEndTime(Timestamp value)
    
    
    public FeatureStatsAnomaly.Builder setEndTime(Timestamp value)

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### setEndTime(Timestamp.Builder builderForValue)
    
    
    public FeatureStatsAnomaly.Builder setEndTime(Timestamp.Builder builderForValue)

The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).

`.google.protobuf.Timestamp end_time = 8;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### setScore(double value)
    
    
    public FeatureStatsAnomaly.Builder setScore(double value)

Feature importance score, only populated when cross-feature monitoring is enabled. For now only used to represent feature attribution score within range [0, 1] for ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_SKEW and ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_DRIFT.

`double score = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The score to set.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### setStartTime(Timestamp value)
    
    
    public FeatureStatsAnomaly.Builder setStartTime(Timestamp value)

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### setStartTime(Timestamp.Builder builderForValue)
    
    
    public FeatureStatsAnomaly.Builder setStartTime(Timestamp.Builder builderForValue)

The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval).

`.google.protobuf.Timestamp start_time = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` |   
  
### setStatsUri(String value)
    
    
    public FeatureStatsAnomaly.Builder setStatsUri(String value)

Path of the stats file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/stats. Example: gs://monitoring_bucket/feature_name/stats. Stats are stored as binary format with Protobuf message [tensorflow.metadata.v0.FeatureNameStatistics](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/statistics.proto).

`string stats_uri = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The statsUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
### setStatsUriBytes(ByteString value)
    
    
    public FeatureStatsAnomaly.Builder setStatsUriBytes(ByteString value)

Path of the stats file for current feature values in Cloud Storage bucket. Format: gs://<bucket_name>/<object_name>/stats. Example: gs://monitoring_bucket/feature_name/stats. Stats are stored as binary format with Protobuf message [tensorflow.metadata.v0.FeatureNameStatistics](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/statistics.proto).

`string stats_uri = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for statsUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureStatsAnomaly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureStatsAnomaly.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
