---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder
title: Class CheckCompatibilityRequest.Builder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:06.240679+00:00
---

# Class CheckCompatibilityRequest.Builder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CheckCompatibilityRequest.Builder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public static final class CheckCompatibilityRequest.Builder extends GeneratedMessage.Builder<CheckCompatibilityRequest.Builder> implements CheckCompatibilityRequestOrBuilder

The request for compatibility information for a report's dimensions and metrics. Check compatibility provides a preview of the compatibility of a report; fields shared with the `runReport` request should be the same values as in your `runReport` request.

Protobuf type `google.analytics.data.v1beta.CheckCompatibilityRequest`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > CheckCompatibilityRequest.Builder

## Implements

[CheckCompatibilityRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequestOrBuilder)

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

### addAllDimensions(Iterable<? extends Dimension> values)
    
    
    public CheckCompatibilityRequest.Builder addAllDimensions(Iterable<? extends Dimension> values)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.analytics.data.v1beta.Dimension>`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addAllMetrics(Iterable<? extends Metric> values)
    
    
    public CheckCompatibilityRequest.Builder addAllMetrics(Iterable<? extends Metric> values)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.analytics.data.v1beta.Metric>`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addDimensions(Dimension value)
    
    
    public CheckCompatibilityRequest.Builder addDimensions(Dimension value)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Dimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addDimensions(Dimension.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder addDimensions(Dimension.Builder builderForValue)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Dimension.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addDimensions(int index, Dimension value)
    
    
    public CheckCompatibilityRequest.Builder addDimensions(int index, Dimension value)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Dimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addDimensions(int index, Dimension.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder addDimensions(int index, Dimension.Builder builderForValue)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Dimension.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addDimensionsBuilder()
    
    
    public Dimension.Builder addDimensionsBuilder()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Dimension.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension.Builder)` |   
  
### addDimensionsBuilder(int index)
    
    
    public Dimension.Builder addDimensionsBuilder(int index)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dimension.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension.Builder)` |   
  
### addMetrics(Metric value)
    
    
    public CheckCompatibilityRequest.Builder addMetrics(Metric value)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Metric](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addMetrics(Metric.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder addMetrics(Metric.Builder builderForValue)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Metric.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addMetrics(int index, Metric value)
    
    
    public CheckCompatibilityRequest.Builder addMetrics(int index, Metric value)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Metric](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addMetrics(int index, Metric.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder addMetrics(int index, Metric.Builder builderForValue)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Metric.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### addMetricsBuilder()
    
    
    public Metric.Builder addMetricsBuilder()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Metric.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric.Builder)` |   
  
### addMetricsBuilder(int index)
    
    
    public Metric.Builder addMetricsBuilder(int index)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Metric.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric.Builder)` |   
  
### build()
    
    
    public CheckCompatibilityRequest build()

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest)` |   
  
### buildPartial()
    
    
    public CheckCompatibilityRequest buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest)` |   
  
### clear()
    
    
    public CheckCompatibilityRequest.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCompatibilityFilter()
    
    
    public CheckCompatibilityRequest.Builder clearCompatibilityFilter()

Filters the dimensions and metrics in the response to just this compatibility. Commonly used as `”compatibilityFilter”: “COMPATIBLE”` to only return compatible dimensions & metrics.

`.google.analytics.data.v1beta.Compatibility compatibility_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` | This builder for chaining.  
  
### clearDimensionFilter()
    
    
    public CheckCompatibilityRequest.Builder clearDimensionFilter()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### clearDimensions()
    
    
    public CheckCompatibilityRequest.Builder clearDimensions()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### clearMetricFilter()
    
    
    public CheckCompatibilityRequest.Builder clearMetricFilter()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### clearMetrics()
    
    
    public CheckCompatibilityRequest.Builder clearMetrics()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### clearProperty()
    
    
    public CheckCompatibilityRequest.Builder clearProperty()

A Google Analytics property identifier whose events are tracked. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). `property` should be the same value as in your `runReport` request.

Example: properties/1234

`string property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` | This builder for chaining.  
  
### getCompatibilityFilter()
    
    
    public Compatibility getCompatibilityFilter()

Filters the dimensions and metrics in the response to just this compatibility. Commonly used as `”compatibilityFilter”: “COMPATIBLE”` to only return compatible dimensions & metrics.

`.google.analytics.data.v1beta.Compatibility compatibility_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Compatibility](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Compatibility)` | The compatibilityFilter.  
  
### getCompatibilityFilterValue()
    
    
    public int getCompatibilityFilterValue()

Filters the dimensions and metrics in the response to just this compatibility. Commonly used as `”compatibilityFilter”: “COMPATIBLE”` to only return compatible dimensions & metrics.

`.google.analytics.data.v1beta.Compatibility compatibility_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for compatibilityFilter.  
  
### getDefaultInstanceForType()
    
    
    public CheckCompatibilityRequest getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDimensionFilter()
    
    
    public FilterExpression getDimensionFilter()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)` | The dimensionFilter.  
  
### getDimensionFilterBuilder()
    
    
    public FilterExpression.Builder getDimensionFilterBuilder()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression.Builder)` |   
  
### getDimensionFilterOrBuilder()
    
    
    public FilterExpressionOrBuilder getDimensionFilterOrBuilder()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionOrBuilder)` |   
  
### getDimensions(int index)
    
    
    public Dimension getDimensions(int index)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension)` |   
  
### getDimensionsBuilder(int index)
    
    
    public Dimension.Builder getDimensionsBuilder(int index)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dimension.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension.Builder)` |   
  
### getDimensionsBuilderList()
    
    
    public List<Dimension.Builder> getDimensionsBuilderList()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension.Builder)>` |   
  
### getDimensionsCount()
    
    
    public int getDimensionsCount()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionsList()
    
    
    public List<Dimension> getDimensionsList()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Dimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension)>` |   
  
### getDimensionsOrBuilder(int index)
    
    
    public DimensionOrBuilder getDimensionsOrBuilder(int index)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionOrBuilder)` |   
  
### getDimensionsOrBuilderList()
    
    
    public List<? extends DimensionOrBuilder> getDimensionsOrBuilderList()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.DimensionOrBuilder>` |   
  
### getMetricFilter()
    
    
    public FilterExpression getMetricFilter()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)` | The metricFilter.  
  
### getMetricFilterBuilder()
    
    
    public FilterExpression.Builder getMetricFilterBuilder()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression.Builder)` |   
  
### getMetricFilterOrBuilder()
    
    
    public FilterExpressionOrBuilder getMetricFilterOrBuilder()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionOrBuilder)` |   
  
### getMetrics(int index)
    
    
    public Metric getMetrics(int index)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric)` |   
  
### getMetricsBuilder(int index)
    
    
    public Metric.Builder getMetricsBuilder(int index)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Metric.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric.Builder)` |   
  
### getMetricsBuilderList()
    
    
    public List<Metric.Builder> getMetricsBuilderList()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric.Builder)>` |   
  
### getMetricsCount()
    
    
    public int getMetricsCount()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetricsList()
    
    
    public List<Metric> getMetricsList()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric)>` |   
  
### getMetricsOrBuilder(int index)
    
    
    public MetricOrBuilder getMetricsOrBuilder(int index)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricOrBuilder)` |   
  
### getMetricsOrBuilderList()
    
    
    public List<? extends MetricOrBuilder> getMetricsOrBuilderList()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.MetricOrBuilder>` |   
  
### getProperty()
    
    
    public String getProperty()

A Google Analytics property identifier whose events are tracked. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). `property` should be the same value as in your `runReport` request.

Example: properties/1234

`string property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The property.  
  
### getPropertyBytes()
    
    
    public ByteString getPropertyBytes()

A Google Analytics property identifier whose events are tracked. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). `property` should be the same value as in your `runReport` request.

Example: properties/1234

`string property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for property.  
  
### hasDimensionFilter()
    
    
    public boolean hasDimensionFilter()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dimensionFilter field is set.  
  
### hasMetricFilter()
    
    
    public boolean hasMetricFilter()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metricFilter field is set.  
  
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

### mergeDimensionFilter(FilterExpression value)
    
    
    public CheckCompatibilityRequest.Builder mergeDimensionFilter(FilterExpression value)

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### mergeFrom(CheckCompatibilityRequest other)
    
    
    public CheckCompatibilityRequest.Builder mergeFrom(CheckCompatibilityRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CheckCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public CheckCompatibilityRequest.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public CheckCompatibilityRequest.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeMetricFilter(FilterExpression value)
    
    
    public CheckCompatibilityRequest.Builder mergeMetricFilter(FilterExpression value)

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### removeDimensions(int index)
    
    
    public CheckCompatibilityRequest.Builder removeDimensions(int index)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### removeMetrics(int index)
    
    
    public CheckCompatibilityRequest.Builder removeMetrics(int index)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setCompatibilityFilter(Compatibility value)
    
    
    public CheckCompatibilityRequest.Builder setCompatibilityFilter(Compatibility value)

Filters the dimensions and metrics in the response to just this compatibility. Commonly used as `”compatibilityFilter”: “COMPATIBLE”` to only return compatible dimensions & metrics.

`.google.analytics.data.v1beta.Compatibility compatibility_filter = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Compatibility](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Compatibility)`  
The compatibilityFilter to set.  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` | This builder for chaining.  
  
### setCompatibilityFilterValue(int value)
    
    
    public CheckCompatibilityRequest.Builder setCompatibilityFilterValue(int value)

Filters the dimensions and metrics in the response to just this compatibility. Commonly used as `”compatibilityFilter”: “COMPATIBLE”` to only return compatible dimensions & metrics.

`.google.analytics.data.v1beta.Compatibility compatibility_filter = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for compatibilityFilter to set.  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` | This builder for chaining.  
  
### setDimensionFilter(FilterExpression value)
    
    
    public CheckCompatibilityRequest.Builder setDimensionFilter(FilterExpression value)

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setDimensionFilter(FilterExpression.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder setDimensionFilter(FilterExpression.Builder builderForValue)

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[FilterExpression.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setDimensions(int index, Dimension value)
    
    
    public CheckCompatibilityRequest.Builder setDimensions(int index, Dimension value)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Dimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setDimensions(int index, Dimension.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder setDimensions(int index, Dimension.Builder builderForValue)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Dimension.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setMetricFilter(FilterExpression value)
    
    
    public CheckCompatibilityRequest.Builder setMetricFilter(FilterExpression value)

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setMetricFilter(FilterExpression.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder setMetricFilter(FilterExpression.Builder builderForValue)

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[FilterExpression.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setMetrics(int index, Metric value)
    
    
    public CheckCompatibilityRequest.Builder setMetrics(int index, Metric value)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Metric](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setMetrics(int index, Metric.Builder builderForValue)
    
    
    public CheckCompatibilityRequest.Builder setMetrics(int index, Metric.Builder builderForValue)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Metric.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` |   
  
### setProperty(String value)
    
    
    public CheckCompatibilityRequest.Builder setProperty(String value)

A Google Analytics property identifier whose events are tracked. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). `property` should be the same value as in your `runReport` request.

Example: properties/1234

`string property = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The property to set.  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` | This builder for chaining.  
  
### setPropertyBytes(ByteString value)
    
    
    public CheckCompatibilityRequest.Builder setPropertyBytes(ByteString value)

A Google Analytics property identifier whose events are tracked. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). `property` should be the same value as in your `runReport` request.

Example: properties/1234

`string property = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for property to set.  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
