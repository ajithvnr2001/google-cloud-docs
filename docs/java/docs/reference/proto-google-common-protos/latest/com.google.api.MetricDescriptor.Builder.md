---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder
title: Class MetricDescriptor.Builder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:44.865224+00:00
---

# Class MetricDescriptor.Builder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MetricDescriptor.Builder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public static final class MetricDescriptor.Builder extends GeneratedMessage.Builder<MetricDescriptor.Builder> implements MetricDescriptorOrBuilder

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

Protobuf type `google.api.MetricDescriptor`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > MetricDescriptor.Builder

## Implements

[MetricDescriptorOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptorOrBuilder)

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

### addAllLabels(Iterable<? extends LabelDescriptor> values)
    
    
    public MetricDescriptor.Builder addAllLabels(Iterable<? extends LabelDescriptor> values)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.api.LabelDescriptor>`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### addAllMonitoredResourceTypes(Iterable<String> values)
    
    
    public MetricDescriptor.Builder addAllMonitoredResourceTypes(Iterable<String> values)

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The monitoredResourceTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### addLabels(LabelDescriptor value)
    
    
    public MetricDescriptor.Builder addLabels(LabelDescriptor value)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LabelDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### addLabels(LabelDescriptor.Builder builderForValue)
    
    
    public MetricDescriptor.Builder addLabels(LabelDescriptor.Builder builderForValue)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[LabelDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### addLabels(int index, LabelDescriptor value)
    
    
    public MetricDescriptor.Builder addLabels(int index, LabelDescriptor value)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[LabelDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### addLabels(int index, LabelDescriptor.Builder builderForValue)
    
    
    public MetricDescriptor.Builder addLabels(int index, LabelDescriptor.Builder builderForValue)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[LabelDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### addLabelsBuilder()
    
    
    public LabelDescriptor.Builder addLabelsBuilder()

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Returns**  
---  
**Type** | **Description**  
`[LabelDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor.Builder)` |   
  
### addLabelsBuilder(int index)
    
    
    public LabelDescriptor.Builder addLabelsBuilder(int index)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor.Builder)` |   
  
### addMonitoredResourceTypes(String value)
    
    
    public MetricDescriptor.Builder addMonitoredResourceTypes(String value)

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The monitoredResourceTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### addMonitoredResourceTypesBytes(ByteString value)
    
    
    public MetricDescriptor.Builder addMonitoredResourceTypesBytes(ByteString value)

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the monitoredResourceTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### build()
    
    
    public MetricDescriptor build()

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor)` |   
  
### buildPartial()
    
    
    public MetricDescriptor buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor)` |   
  
### clear()
    
    
    public MetricDescriptor.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearDescription()
    
    
    public MetricDescriptor.Builder clearDescription()

A detailed description of the metric, which can be used in documentation.

`string description = 6;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearDisplayName()
    
    
    public MetricDescriptor.Builder clearDisplayName()

A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.

`string display_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearLabels()
    
    
    public MetricDescriptor.Builder clearLabels()

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### clearLaunchStage()
    
    
    public MetricDescriptor.Builder clearLaunchStage()

Optional. The launch stage of the metric definition.

`.google.api.LaunchStage launch_stage = 12;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearMetadata()
    
    
    public MetricDescriptor.Builder clearMetadata()

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### clearMetricKind()
    
    
    public MetricDescriptor.Builder clearMetricKind()

Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.MetricKind metric_kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearMonitoredResourceTypes()
    
    
    public MetricDescriptor.Builder clearMonitoredResourceTypes()

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public MetricDescriptor.Builder clearName()

The resource name of the metric descriptor.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearType()
    
    
    public MetricDescriptor.Builder clearType()

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:

"custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies"

`string type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearUnit()
    
    
    public MetricDescriptor.Builder clearUnit()

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)

  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)

  * `m` milli (10^-3)

  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)

  * `Ki` kibi (2^10)

  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar**

The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).

  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:

Expression = Component { "." Component } { "/" Component } ;

Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ] | Annotation | "1" ;

Annotation = "{" NAME "}" ;

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.

  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").



`string unit = 5;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### clearValueType()
    
    
    public MetricDescriptor.Builder clearValueType()

Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.ValueType value_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### getDefaultInstanceForType()
    
    
    public MetricDescriptor getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor)` |   
  
### getDescription()
    
    
    public String getDescription()

A detailed description of the metric, which can be used in documentation.

`string description = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

A detailed description of the metric, which can be used in documentation.

`string description = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDisplayName()
    
    
    public String getDisplayName()

A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.

`string display_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.

`string display_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getLabels(int index)
    
    
    public LabelDescriptor getLabels(int index)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor)` |   
  
### getLabelsBuilder(int index)
    
    
    public LabelDescriptor.Builder getLabelsBuilder(int index)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor.Builder)` |   
  
### getLabelsBuilderList()
    
    
    public List<LabelDescriptor.Builder> getLabelsBuilderList()

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor.Builder)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsList()
    
    
    public List<LabelDescriptor> getLabelsList()

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LabelDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor)>` |   
  
### getLabelsOrBuilder(int index)
    
    
    public LabelDescriptorOrBuilder getLabelsOrBuilder(int index)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelDescriptorOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptorOrBuilder)` |   
  
### getLabelsOrBuilderList()
    
    
    public List<? extends LabelDescriptorOrBuilder> getLabelsOrBuilderList()

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.LabelDescriptorOrBuilder>` |   
  
### getLaunchStage()
    
    
    public LaunchStage getLaunchStage()

Optional. The launch stage of the metric definition.

`.google.api.LaunchStage launch_stage = 12;`

**Returns**  
---  
**Type** | **Description**  
`[LaunchStage](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LaunchStage)` | The launchStage.  
  
### getLaunchStageValue()
    
    
    public int getLaunchStageValue()

Optional. The launch stage of the metric definition.

`.google.api.LaunchStage launch_stage = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for launchStage.  
  
### getMetadata()
    
    
    public MetricDescriptor.MetricDescriptorMetadata getMetadata()

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.MetricDescriptorMetadata](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricDescriptorMetadata)` | The metadata.  
  
### getMetadataBuilder()
    
    
    public MetricDescriptor.MetricDescriptorMetadata.Builder getMetadataBuilder()

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.MetricDescriptorMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricDescriptorMetadata.Builder)` |   
  
### getMetadataOrBuilder()
    
    
    public MetricDescriptor.MetricDescriptorMetadataOrBuilder getMetadataOrBuilder()

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.MetricDescriptorMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricDescriptorMetadataOrBuilder)` |   
  
### getMetricKind()
    
    
    public MetricDescriptor.MetricKind getMetricKind()

Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.MetricKind metric_kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.MetricKind](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricKind)` | The metricKind.  
  
### getMetricKindValue()
    
    
    public int getMetricKindValue()

Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.MetricKind metric_kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for metricKind.  
  
### getMonitoredResourceTypes(int index)
    
    
    public String getMonitoredResourceTypes(int index)

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The monitoredResourceTypes at the given index.  
  
### getMonitoredResourceTypesBytes(int index)
    
    
    public ByteString getMonitoredResourceTypesBytes(int index)

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the monitoredResourceTypes at the given index.  
  
### getMonitoredResourceTypesCount()
    
    
    public int getMonitoredResourceTypesCount()

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of monitoredResourceTypes.  
  
### getMonitoredResourceTypesList()
    
    
    public ProtocolStringList getMonitoredResourceTypesList()

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the monitoredResourceTypes.  
  
### getName()
    
    
    public String getName()

The resource name of the metric descriptor.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The resource name of the metric descriptor.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getType()
    
    
    public String getType()

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:

"custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies"

`string type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public ByteString getTypeBytes()

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:

"custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies"

`string type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### getUnit()
    
    
    public String getUnit()

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)

  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)

  * `m` milli (10^-3)

  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)

  * `Ki` kibi (2^10)

  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar**

The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).

  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:

Expression = Component { "." Component } { "/" Component } ;

Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ] | Annotation | "1" ;

Annotation = "{" NAME "}" ;

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.

  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").



`string unit = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unit.  
  
### getUnitBytes()
    
    
    public ByteString getUnitBytes()

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)

  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)

  * `m` milli (10^-3)

  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)

  * `Ki` kibi (2^10)

  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar**

The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).

  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:

Expression = Component { "." Component } { "/" Component } ;

Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ] | Annotation | "1" ;

Annotation = "{" NAME "}" ;

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.

  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").



`string unit = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for unit.  
  
### getValueType()
    
    
    public MetricDescriptor.ValueType getValueType()

Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.ValueType value_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.ValueType](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.ValueType)` | The valueType.  
  
### getValueTypeValue()
    
    
    public int getValueTypeValue()

Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.ValueType value_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for valueType.  
  
### hasMetadata()
    
    
    public boolean hasMetadata()

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metadata field is set.  
  
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

### mergeFrom(MetricDescriptor other)
    
    
    public MetricDescriptor.Builder mergeFrom(MetricDescriptor other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MetricDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public MetricDescriptor.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public MetricDescriptor.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeMetadata(MetricDescriptor.MetricDescriptorMetadata value)
    
    
    public MetricDescriptor.Builder mergeMetadata(MetricDescriptor.MetricDescriptorMetadata value)

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MetricDescriptor.MetricDescriptorMetadata](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricDescriptorMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### removeLabels(int index)
    
    
    public MetricDescriptor.Builder removeLabels(int index)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### setDescription(String value)
    
    
    public MetricDescriptor.Builder setDescription(String value)

A detailed description of the metric, which can be used in documentation.

`string description = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public MetricDescriptor.Builder setDescriptionBytes(ByteString value)

A detailed description of the metric, which can be used in documentation.

`string description = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setDisplayName(String value)
    
    
    public MetricDescriptor.Builder setDisplayName(String value)

A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.

`string display_name = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public MetricDescriptor.Builder setDisplayNameBytes(ByteString value)

A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.

`string display_name = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setLabels(int index, LabelDescriptor value)
    
    
    public MetricDescriptor.Builder setLabels(int index, LabelDescriptor value)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[LabelDescriptor](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### setLabels(int index, LabelDescriptor.Builder builderForValue)
    
    
    public MetricDescriptor.Builder setLabels(int index, LabelDescriptor.Builder builderForValue)

The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.

`repeated .google.api.LabelDescriptor labels = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[LabelDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LabelDescriptor.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### setLaunchStage(LaunchStage value)
    
    
    public MetricDescriptor.Builder setLaunchStage(LaunchStage value)

Optional. The launch stage of the metric definition.

`.google.api.LaunchStage launch_stage = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LaunchStage](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.LaunchStage)`  
The launchStage to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setLaunchStageValue(int value)
    
    
    public MetricDescriptor.Builder setLaunchStageValue(int value)

Optional. The launch stage of the metric definition.

`.google.api.LaunchStage launch_stage = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for launchStage to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setMetadata(MetricDescriptor.MetricDescriptorMetadata value)
    
    
    public MetricDescriptor.Builder setMetadata(MetricDescriptor.MetricDescriptorMetadata value)

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MetricDescriptor.MetricDescriptorMetadata](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricDescriptorMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### setMetadata(MetricDescriptor.MetricDescriptorMetadata.Builder builderForValue)
    
    
    public MetricDescriptor.Builder setMetadata(MetricDescriptor.MetricDescriptorMetadata.Builder builderForValue)

Optional. Metadata which can be used to guide usage of the metric.

`.google.api.MetricDescriptor.MetricDescriptorMetadata metadata = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MetricDescriptor.MetricDescriptorMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricDescriptorMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` |   
  
### setMetricKind(MetricDescriptor.MetricKind value)
    
    
    public MetricDescriptor.Builder setMetricKind(MetricDescriptor.MetricKind value)

Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.MetricKind metric_kind = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MetricDescriptor.MetricKind](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.MetricKind)`  
The metricKind to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setMetricKindValue(int value)
    
    
    public MetricDescriptor.Builder setMetricKindValue(int value)

Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.MetricKind metric_kind = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for metricKind to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setMonitoredResourceTypes(int index, String value)
    
    
    public MetricDescriptor.Builder setMonitoredResourceTypes(int index, String value)

Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.

`repeated string monitored_resource_types = 13;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The monitoredResourceTypes to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public MetricDescriptor.Builder setName(String value)

The resource name of the metric descriptor.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public MetricDescriptor.Builder setNameBytes(ByteString value)

The resource name of the metric descriptor.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setType(String value)
    
    
    public MetricDescriptor.Builder setType(String value)

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:

"custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies"

`string type = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The type to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setTypeBytes(ByteString value)
    
    
    public MetricDescriptor.Builder setTypeBytes(ByteString value)

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:

"custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies"

`string type = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for type to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setUnit(String value)
    
    
    public MetricDescriptor.Builder setUnit(String value)

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)

  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)

  * `m` milli (10^-3)

  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)

  * `Ki` kibi (2^10)

  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar**

The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).

  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:

Expression = Component { "." Component } { "/" Component } ;

Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ] | Annotation | "1" ;

Annotation = "{" NAME "}" ;

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.

  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").



`string unit = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The unit to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setUnitBytes(ByteString value)
    
    
    public MetricDescriptor.Builder setUnitBytes(ByteString value)

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)

  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)

  * `m` milli (10^-3)

  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)

  * `Ki` kibi (2^10)

  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar**

The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).

  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:

Expression = Component { "." Component } { "/" Component } ;

Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ] | Annotation | "1" ;

Annotation = "{" NAME "}" ;

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.

  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").



`string unit = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for unit to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setValueType(MetricDescriptor.ValueType value)
    
    
    public MetricDescriptor.Builder setValueType(MetricDescriptor.ValueType value)

Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.ValueType value_type = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MetricDescriptor.ValueType](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.ValueType)`  
The valueType to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
### setValueTypeValue(int value)
    
    
    public MetricDescriptor.Builder setValueTypeValue(int value)

Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.

`.google.api.MetricDescriptor.ValueType value_type = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for valueType to set.  
**Returns**  
---  
**Type** | **Description**  
`[MetricDescriptor.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MetricDescriptor.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
