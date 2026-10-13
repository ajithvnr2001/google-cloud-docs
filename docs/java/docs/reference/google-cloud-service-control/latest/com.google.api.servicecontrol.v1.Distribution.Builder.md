---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder
title: Class Distribution.Builder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:24.404070+00:00
---

# Class Distribution.Builder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Distribution.Builder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.1.10 
    
    
    public static final class Distribution.Builder extends GeneratedMessage.Builder<Distribution.Builder> implements DistributionOrBuilder

Distribution represents a frequency distribution of double-valued sample points. It contains the size of the population of sample points plus additional optional information:

  * the arithmetic mean of the samples
  * the minimum and maximum of the samples
  * the sum-squared-deviation of the samples, used to compute variance
  * a histogram of the values of the sample points



Protobuf type `google.api.servicecontrol.v1.Distribution`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Distribution.Builder

## Implements

[DistributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.DistributionOrBuilder)

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

### addAllBucketCounts(Iterable<? extends Long> values)
    
    
    public Distribution.Builder addAllBucketCounts(Iterable<? extends Long> values)

The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.

The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.

Any suffix of trailing zeros may be omitted.

`repeated int64 bucket_counts = 6;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends java.lang.Long>`  
The bucketCounts to add.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### addAllExemplars(Iterable<? extends Distribution.Exemplar> values)
    
    
    public Distribution.Builder addAllExemplars(Iterable<? extends Distribution.Exemplar> values)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.api.Distribution.Exemplar>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### addBucketCounts(long value)
    
    
    public Distribution.Builder addBucketCounts(long value)

The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.

The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.

Any suffix of trailing zeros may be omitted.

`repeated int64 bucket_counts = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The bucketCounts to add.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### addExemplars(Distribution.Exemplar value)
    
    
    public Distribution.Builder addExemplars(Distribution.Exemplar value)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.api.Distribution.Exemplar`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### addExemplars(Distribution.Exemplar.Builder builderForValue)
    
    
    public Distribution.Builder addExemplars(Distribution.Exemplar.Builder builderForValue)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `com.google.api.Distribution.Exemplar.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### addExemplars(int index, Distribution.Exemplar value)
    
    
    public Distribution.Builder addExemplars(int index, Distribution.Exemplar value)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `com.google.api.Distribution.Exemplar`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### addExemplars(int index, Distribution.Exemplar.Builder builderForValue)
    
    
    public Distribution.Builder addExemplars(int index, Distribution.Exemplar.Builder builderForValue)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `com.google.api.Distribution.Exemplar.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### addExemplarsBuilder()
    
    
    public Distribution.Exemplar.Builder addExemplarsBuilder()

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Returns**  
---  
**Type** | **Description**  
`com.google.api.Distribution.Exemplar.Builder` |   
  
### addExemplarsBuilder(int index)
    
    
    public Distribution.Exemplar.Builder addExemplarsBuilder(int index)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.Distribution.Exemplar.Builder` |   
  
### build()
    
    
    public Distribution build()

**Returns**  
---  
**Type** | **Description**  
`[Distribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution)` |   
  
### buildPartial()
    
    
    public Distribution buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Distribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution)` |   
  
### clear()
    
    
    public Distribution.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearBucketCounts()
    
    
    public Distribution.Builder clearBucketCounts()

The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.

The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.

Any suffix of trailing zeros may be omitted.

`repeated int64 bucket_counts = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### clearBucketOption()
    
    
    public Distribution.Builder clearBucketOption()

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### clearCount()
    
    
    public Distribution.Builder clearCount()

The total number of samples in the distribution. Must be >= 0.

`int64 count = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### clearExemplars()
    
    
    public Distribution.Builder clearExemplars()

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### clearExplicitBuckets()
    
    
    public Distribution.Builder clearExplicitBuckets()

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### clearExponentialBuckets()
    
    
    public Distribution.Builder clearExponentialBuckets()

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### clearLinearBuckets()
    
    
    public Distribution.Builder clearLinearBuckets()

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### clearMaximum()
    
    
    public Distribution.Builder clearMaximum()

The maximum of the population of values. Ignored if `count` is zero.

`double maximum = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### clearMean()
    
    
    public Distribution.Builder clearMean()

The arithmetic mean of the samples in the distribution. If `count` is zero then this field must be zero.

`double mean = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### clearMinimum()
    
    
    public Distribution.Builder clearMinimum()

The minimum of the population of values. Ignored if `count` is zero.

`double minimum = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### clearSumOfSquaredDeviation()
    
    
    public Distribution.Builder clearSumOfSquaredDeviation()

The sum of squared deviations from the mean: Sum[i=1..count](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/\(x_i%20-%20mean)^2) where each x_i is a sample values. If `count` is zero then this field must be zero, otherwise validation of the request fails.

`double sum_of_squared_deviation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### getBucketCounts(int index)
    
    
    public long getBucketCounts(int index)

The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.

The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.

Any suffix of trailing zeros may be omitted.

`repeated int64 bucket_counts = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bucketCounts at the given index.  
  
### getBucketCountsCount()
    
    
    public int getBucketCountsCount()

The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.

The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.

Any suffix of trailing zeros may be omitted.

`repeated int64 bucket_counts = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of bucketCounts.  
  
### getBucketCountsList()
    
    
    public List<Long> getBucketCountsList()

The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.

The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.

Any suffix of trailing zeros may be omitted.

`repeated int64 bucket_counts = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the bucketCounts.  
  
### getBucketOptionCase()
    
    
    public Distribution.BucketOptionCase getBucketOptionCase()

**Returns**  
---  
**Type** | **Description**  
`[Distribution.BucketOptionCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.BucketOptionCase)` |   
  
### getCount()
    
    
    public long getCount()

The total number of samples in the distribution. Must be >= 0.

`int64 count = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count.  
  
### getDefaultInstanceForType()
    
    
    public Distribution getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Distribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getExemplars(int index)
    
    
    public Distribution.Exemplar getExemplars(int index)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.Distribution.Exemplar` |   
  
### getExemplarsBuilder(int index)
    
    
    public Distribution.Exemplar.Builder getExemplarsBuilder(int index)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.Distribution.Exemplar.Builder` |   
  
### getExemplarsBuilderList()
    
    
    public List<Distribution.Exemplar.Builder> getExemplarsBuilderList()

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.api.Distribution.Exemplar.Builder>` |   
  
### getExemplarsCount()
    
    
    public int getExemplarsCount()

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExemplarsList()
    
    
    public List<Distribution.Exemplar> getExemplarsList()

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.api.Distribution.Exemplar>` |   
  
### getExemplarsOrBuilder(int index)
    
    
    public Distribution.ExemplarOrBuilder getExemplarsOrBuilder(int index)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.Distribution.ExemplarOrBuilder` |   
  
### getExemplarsOrBuilderList()
    
    
    public List<? extends Distribution.ExemplarOrBuilder> getExemplarsOrBuilderList()

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.Distribution.ExemplarOrBuilder>` |   
  
### getExplicitBuckets()
    
    
    public Distribution.ExplicitBuckets getExplicitBuckets()

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.ExplicitBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExplicitBuckets)` | The explicitBuckets.  
  
### getExplicitBucketsBuilder()
    
    
    public Distribution.ExplicitBuckets.Builder getExplicitBucketsBuilder()

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.ExplicitBuckets.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExplicitBuckets.Builder)` |   
  
### getExplicitBucketsOrBuilder()
    
    
    public Distribution.ExplicitBucketsOrBuilder getExplicitBucketsOrBuilder()

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.ExplicitBucketsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExplicitBucketsOrBuilder)` |   
  
### getExponentialBuckets()
    
    
    public Distribution.ExponentialBuckets getExponentialBuckets()

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Returns**  
---  
**Type** | **Description**  
`[Distribution.ExponentialBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExponentialBuckets)` | The exponentialBuckets.  
  
### getExponentialBucketsBuilder()
    
    
    public Distribution.ExponentialBuckets.Builder getExponentialBucketsBuilder()

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Returns**  
---  
**Type** | **Description**  
`[Distribution.ExponentialBuckets.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExponentialBuckets.Builder)` |   
  
### getExponentialBucketsOrBuilder()
    
    
    public Distribution.ExponentialBucketsOrBuilder getExponentialBucketsOrBuilder()

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Returns**  
---  
**Type** | **Description**  
`[Distribution.ExponentialBucketsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExponentialBucketsOrBuilder)` |   
  
### getLinearBuckets()
    
    
    public Distribution.LinearBuckets getLinearBuckets()

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.LinearBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.LinearBuckets)` | The linearBuckets.  
  
### getLinearBucketsBuilder()
    
    
    public Distribution.LinearBuckets.Builder getLinearBucketsBuilder()

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.LinearBuckets.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.LinearBuckets.Builder)` |   
  
### getLinearBucketsOrBuilder()
    
    
    public Distribution.LinearBucketsOrBuilder getLinearBucketsOrBuilder()

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Distribution.LinearBucketsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.LinearBucketsOrBuilder)` |   
  
### getMaximum()
    
    
    public double getMaximum()

The maximum of the population of values. Ignored if `count` is zero.

`double maximum = 4;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maximum.  
  
### getMean()
    
    
    public double getMean()

The arithmetic mean of the samples in the distribution. If `count` is zero then this field must be zero.

`double mean = 2;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The mean.  
  
### getMinimum()
    
    
    public double getMinimum()

The minimum of the population of values. Ignored if `count` is zero.

`double minimum = 3;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The minimum.  
  
### getSumOfSquaredDeviation()
    
    
    public double getSumOfSquaredDeviation()

The sum of squared deviations from the mean: Sum[i=1..count](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/\(x_i%20-%20mean)^2) where each x_i is a sample values. If `count` is zero then this field must be zero, otherwise validation of the request fails.

`double sum_of_squared_deviation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sumOfSquaredDeviation.  
  
### hasExplicitBuckets()
    
    
    public boolean hasExplicitBuckets()

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the explicitBuckets field is set.  
  
### hasExponentialBuckets()
    
    
    public boolean hasExponentialBuckets()

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the exponentialBuckets field is set.  
  
### hasLinearBuckets()
    
    
    public boolean hasLinearBuckets()

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the linearBuckets field is set.  
  
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

### mergeExplicitBuckets(Distribution.ExplicitBuckets value)
    
    
    public Distribution.Builder mergeExplicitBuckets(Distribution.ExplicitBuckets value)

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Distribution.ExplicitBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExplicitBuckets)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### mergeExponentialBuckets(Distribution.ExponentialBuckets value)
    
    
    public Distribution.Builder mergeExponentialBuckets(Distribution.ExponentialBuckets value)

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Distribution.ExponentialBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExponentialBuckets)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### mergeFrom(Distribution other)
    
    
    public Distribution.Builder mergeFrom(Distribution other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Distribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Distribution.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Distribution.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeLinearBuckets(Distribution.LinearBuckets value)
    
    
    public Distribution.Builder mergeLinearBuckets(Distribution.LinearBuckets value)

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Distribution.LinearBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.LinearBuckets)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### removeExemplars(int index)
    
    
    public Distribution.Builder removeExemplars(int index)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setBucketCounts(int index, long value)
    
    
    public Distribution.Builder setBucketCounts(int index, long value)

The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.

The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.

Any suffix of trailing zeros may be omitted.

`repeated int64 bucket_counts = 6;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The bucketCounts to set.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### setCount(long value)
    
    
    public Distribution.Builder setCount(long value)

The total number of samples in the distribution. Must be >= 0.

`int64 count = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The count to set.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### setExemplars(int index, Distribution.Exemplar value)
    
    
    public Distribution.Builder setExemplars(int index, Distribution.Exemplar value)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `com.google.api.Distribution.Exemplar`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setExemplars(int index, Distribution.Exemplar.Builder builderForValue)
    
    
    public Distribution.Builder setExemplars(int index, Distribution.Exemplar.Builder builderForValue)

Example points. Must be in increasing order of `value` field.

`repeated .google.api.Distribution.Exemplar exemplars = 10;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `com.google.api.Distribution.Exemplar.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setExplicitBuckets(Distribution.ExplicitBuckets value)
    
    
    public Distribution.Builder setExplicitBuckets(Distribution.ExplicitBuckets value)

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Distribution.ExplicitBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExplicitBuckets)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setExplicitBuckets(Distribution.ExplicitBuckets.Builder builderForValue)
    
    
    public Distribution.Builder setExplicitBuckets(Distribution.ExplicitBuckets.Builder builderForValue)

Buckets with arbitrary user-provided width.

`.google.api.servicecontrol.v1.Distribution.ExplicitBuckets explicit_buckets = 9;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Distribution.ExplicitBuckets.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExplicitBuckets.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setExponentialBuckets(Distribution.ExponentialBuckets value)
    
    
    public Distribution.Builder setExponentialBuckets(Distribution.ExponentialBuckets value)

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Distribution.ExponentialBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExponentialBuckets)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setExponentialBuckets(Distribution.ExponentialBuckets.Builder builderForValue)
    
    
    public Distribution.Builder setExponentialBuckets(Distribution.ExponentialBuckets.Builder builderForValue)

Buckets with exponentially growing width.

`.google.api.servicecontrol.v1.Distribution.ExponentialBuckets exponential_buckets = 8; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Distribution.ExponentialBuckets.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.ExponentialBuckets.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setLinearBuckets(Distribution.LinearBuckets value)
    
    
    public Distribution.Builder setLinearBuckets(Distribution.LinearBuckets value)

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Distribution.LinearBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.LinearBuckets)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setLinearBuckets(Distribution.LinearBuckets.Builder builderForValue)
    
    
    public Distribution.Builder setLinearBuckets(Distribution.LinearBuckets.Builder builderForValue)

Buckets with constant width.

`.google.api.servicecontrol.v1.Distribution.LinearBuckets linear_buckets = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Distribution.LinearBuckets.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.LinearBuckets.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` |   
  
### setMaximum(double value)
    
    
    public Distribution.Builder setMaximum(double value)

The maximum of the population of values. Ignored if `count` is zero.

`double maximum = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The maximum to set.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### setMean(double value)
    
    
    public Distribution.Builder setMean(double value)

The arithmetic mean of the samples in the distribution. If `count` is zero then this field must be zero.

`double mean = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The mean to set.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### setMinimum(double value)
    
    
    public Distribution.Builder setMinimum(double value)

The minimum of the population of values. Ignored if `count` is zero.

`double minimum = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The minimum to set.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
### setSumOfSquaredDeviation(double value)
    
    
    public Distribution.Builder setSumOfSquaredDeviation(double value)

The sum of squared deviations from the mean: Sum[i=1..count](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/\(x_i%20-%20mean)^2) where each x_i is a sample values. If `count` is zero then this field must be zero, otherwise validation of the request fails.

`double sum_of_squared_deviation = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The sumOfSquaredDeviation to set.  
**Returns**  
---  
**Type** | **Description**  
`[Distribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Distribution.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
