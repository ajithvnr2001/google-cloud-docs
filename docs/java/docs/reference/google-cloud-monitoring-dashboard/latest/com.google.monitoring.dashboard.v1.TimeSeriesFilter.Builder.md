---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder
title: Class TimeSeriesFilter.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:03.851884+00:00
---

# Class TimeSeriesFilter.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TimeSeriesFilter.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.0  2.3.0  2.2.6 
    
    
    public static final class TimeSeriesFilter.Builder extends GeneratedMessage.Builder<TimeSeriesFilter.Builder> implements TimeSeriesFilterOrBuilder

A filter that defines a subset of time series data that is displayed in a widget. Time series data is fetched using the [`ListTimeSeries`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

Protobuf type `google.monitoring.dashboard.v1.TimeSeriesFilter`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > TimeSeriesFilter.Builder

## Implements

[TimeSeriesFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilterOrBuilder)

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
    
    
    public TimeSeriesFilter build()

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter)` |   
  
### buildPartial()
    
    
    public TimeSeriesFilter buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter)` |   
  
### clear()
    
    
    public TimeSeriesFilter.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAggregation()
    
    
    public TimeSeriesFilter.Builder clearAggregation()

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### clearFilter()
    
    
    public TimeSeriesFilter.Builder clearFilter()

Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.

`string filter = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` | This builder for chaining.  
  
### clearOutputFilter()
    
    
    public TimeSeriesFilter.Builder clearOutputFilter()

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### clearPickTimeSeriesFilter()
    
    
    public TimeSeriesFilter.Builder clearPickTimeSeriesFilter()

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### clearSecondaryAggregation()
    
    
    public TimeSeriesFilter.Builder clearSecondaryAggregation()

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### clearStatisticalTimeSeriesFilter() (deprecated)
    
    
    public TimeSeriesFilter.Builder clearStatisticalTimeSeriesFilter()

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### getAggregation()
    
    
    public Aggregation getAggregation()

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Aggregation](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation)` | The aggregation.  
  
### getAggregationBuilder()
    
    
    public Aggregation.Builder getAggregationBuilder()

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Aggregation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation.Builder)` |   
  
### getAggregationOrBuilder()
    
    
    public AggregationOrBuilder getAggregationOrBuilder()

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AggregationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.AggregationOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public TimeSeriesFilter getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getFilter()
    
    
    public String getFilter()

Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.

`string filter = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public ByteString getFilterBytes()

Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.

`string filter = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getOutputFilterCase()
    
    
    public TimeSeriesFilter.OutputFilterCase getOutputFilterCase()

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.OutputFilterCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.OutputFilterCase)` |   
  
### getPickTimeSeriesFilter()
    
    
    public PickTimeSeriesFilter getPickTimeSeriesFilter()

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Returns**  
---  
**Type** | **Description**  
`[PickTimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.PickTimeSeriesFilter)` | The pickTimeSeriesFilter.  
  
### getPickTimeSeriesFilterBuilder()
    
    
    public PickTimeSeriesFilter.Builder getPickTimeSeriesFilterBuilder()

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Returns**  
---  
**Type** | **Description**  
`[PickTimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.PickTimeSeriesFilter.Builder)` |   
  
### getPickTimeSeriesFilterOrBuilder()
    
    
    public PickTimeSeriesFilterOrBuilder getPickTimeSeriesFilterOrBuilder()

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Returns**  
---  
**Type** | **Description**  
`[PickTimeSeriesFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.PickTimeSeriesFilterOrBuilder)` |   
  
### getSecondaryAggregation()
    
    
    public Aggregation getSecondaryAggregation()

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Aggregation](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation)` | The secondaryAggregation.  
  
### getSecondaryAggregationBuilder()
    
    
    public Aggregation.Builder getSecondaryAggregationBuilder()

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Aggregation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation.Builder)` |   
  
### getSecondaryAggregationOrBuilder()
    
    
    public AggregationOrBuilder getSecondaryAggregationOrBuilder()

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AggregationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.AggregationOrBuilder)` |   
  
### getStatisticalTimeSeriesFilter() (deprecated)
    
    
    public StatisticalTimeSeriesFilter getStatisticalTimeSeriesFilter()

**Deprecated.** _google.monitoring.dashboard.v1.TimeSeriesFilter.statistical_time_series_filter is deprecated. See google/monitoring/dashboard/v1/metrics.proto;l=89_

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter)` | The statisticalTimeSeriesFilter.  
  
### getStatisticalTimeSeriesFilterBuilder() (deprecated)
    
    
    public StatisticalTimeSeriesFilter.Builder getStatisticalTimeSeriesFilterBuilder()

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[StatisticalTimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.Builder)` |   
  
### getStatisticalTimeSeriesFilterOrBuilder() (deprecated)
    
    
    public StatisticalTimeSeriesFilterOrBuilder getStatisticalTimeSeriesFilterOrBuilder()

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[StatisticalTimeSeriesFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilterOrBuilder)` |   
  
### hasAggregation()
    
    
    public boolean hasAggregation()

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the aggregation field is set.  
  
### hasPickTimeSeriesFilter()
    
    
    public boolean hasPickTimeSeriesFilter()

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pickTimeSeriesFilter field is set.  
  
### hasSecondaryAggregation()
    
    
    public boolean hasSecondaryAggregation()

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the secondaryAggregation field is set.  
  
### hasStatisticalTimeSeriesFilter() (deprecated)
    
    
    public boolean hasStatisticalTimeSeriesFilter()

**Deprecated.** _google.monitoring.dashboard.v1.TimeSeriesFilter.statistical_time_series_filter is deprecated. See google/monitoring/dashboard/v1/metrics.proto;l=89_

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the statisticalTimeSeriesFilter field is set.  
  
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

### mergeAggregation(Aggregation value)
    
    
    public TimeSeriesFilter.Builder mergeAggregation(Aggregation value)

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Aggregation](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### mergeFrom(TimeSeriesFilter other)
    
    
    public TimeSeriesFilter.Builder mergeFrom(TimeSeriesFilter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public TimeSeriesFilter.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public TimeSeriesFilter.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergePickTimeSeriesFilter(PickTimeSeriesFilter value)
    
    
    public TimeSeriesFilter.Builder mergePickTimeSeriesFilter(PickTimeSeriesFilter value)

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PickTimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.PickTimeSeriesFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### mergeSecondaryAggregation(Aggregation value)
    
    
    public TimeSeriesFilter.Builder mergeSecondaryAggregation(Aggregation value)

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Aggregation](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### mergeStatisticalTimeSeriesFilter(StatisticalTimeSeriesFilter value) (deprecated)
    
    
    public TimeSeriesFilter.Builder mergeStatisticalTimeSeriesFilter(StatisticalTimeSeriesFilter value)

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setAggregation(Aggregation value)
    
    
    public TimeSeriesFilter.Builder setAggregation(Aggregation value)

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Aggregation](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setAggregation(Aggregation.Builder builderForValue)
    
    
    public TimeSeriesFilter.Builder setAggregation(Aggregation.Builder builderForValue)

By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.

`.google.monitoring.dashboard.v1.Aggregation aggregation = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Aggregation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setFilter(String value)
    
    
    public TimeSeriesFilter.Builder setFilter(String value)

Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.

`string filter = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The filter to set.  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` | This builder for chaining.  
  
### setFilterBytes(ByteString value)
    
    
    public TimeSeriesFilter.Builder setFilterBytes(ByteString value)

Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.

`string filter = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for filter to set.  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` | This builder for chaining.  
  
### setPickTimeSeriesFilter(PickTimeSeriesFilter value)
    
    
    public TimeSeriesFilter.Builder setPickTimeSeriesFilter(PickTimeSeriesFilter value)

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PickTimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.PickTimeSeriesFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setPickTimeSeriesFilter(PickTimeSeriesFilter.Builder builderForValue)
    
    
    public TimeSeriesFilter.Builder setPickTimeSeriesFilter(PickTimeSeriesFilter.Builder builderForValue)

Ranking based time series filter.

`.google.monitoring.dashboard.v1.PickTimeSeriesFilter pick_time_series_filter = 4; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PickTimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.PickTimeSeriesFilter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setSecondaryAggregation(Aggregation value)
    
    
    public TimeSeriesFilter.Builder setSecondaryAggregation(Aggregation value)

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Aggregation](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setSecondaryAggregation(Aggregation.Builder builderForValue)
    
    
    public TimeSeriesFilter.Builder setSecondaryAggregation(Aggregation.Builder builderForValue)

Apply a second aggregation after `aggregation` is applied.

`.google.monitoring.dashboard.v1.Aggregation secondary_aggregation = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Aggregation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Aggregation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setStatisticalTimeSeriesFilter(StatisticalTimeSeriesFilter value) (deprecated)
    
    
    public TimeSeriesFilter.Builder setStatisticalTimeSeriesFilter(StatisticalTimeSeriesFilter value)

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
### setStatisticalTimeSeriesFilter(StatisticalTimeSeriesFilter.Builder builderForValue) (deprecated)
    
    
    public TimeSeriesFilter.Builder setStatisticalTimeSeriesFilter(StatisticalTimeSeriesFilter.Builder builderForValue)

Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.

` .google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter statistical_time_series_filter = 5 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[StatisticalTimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.TimeSeriesFilter.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
