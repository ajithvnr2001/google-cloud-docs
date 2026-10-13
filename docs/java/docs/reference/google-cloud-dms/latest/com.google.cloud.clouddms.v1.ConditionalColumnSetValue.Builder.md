---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder
title: Class ConditionalColumnSetValue.Builder (2.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:34.549390+00:00
---

# Class ConditionalColumnSetValue.Builder (2.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConditionalColumnSetValue.Builder (2.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.98.0 (latest)  2.94.0  2.93.0  2.92.0  2.90.0  2.87.0  2.86.0  2.84.0  2.82.0  2.81.0  2.80.0  2.79.0  2.77.0  2.75.0  2.74.0  2.73.0  2.72.0  2.71.0  2.69.0  2.67.0  2.66.0  2.63.0  2.62.0  2.61.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.8  2.1.9 
    
    
    public static final class ConditionalColumnSetValue.Builder extends GeneratedMessage.Builder<ConditionalColumnSetValue.Builder> implements ConditionalColumnSetValueOrBuilder

Options to configure rule type ConditionalColumnSetValue. The rule is used to transform the data which is being replicated/migrated.

The rule filter field can refer to one or more entities.

The rule scope can be one of: Column.

Protobuf type `google.cloud.clouddms.v1.ConditionalColumnSetValue`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ConditionalColumnSetValue.Builder

## Implements

[ConditionalColumnSetValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValueOrBuilder)

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
    
    
    public ConditionalColumnSetValue build()

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue)` |   
  
### buildPartial()
    
    
    public ConditionalColumnSetValue buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue)` |   
  
### clear()
    
    
    public ConditionalColumnSetValue.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCustomFeatures()
    
    
    public ConditionalColumnSetValue.Builder clearCustomFeatures()

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### clearSourceFilter()
    
    
    public ConditionalColumnSetValue.Builder clearSourceFilter()

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### clearSourceNumericFilter()
    
    
    public ConditionalColumnSetValue.Builder clearSourceNumericFilter()

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### clearSourceTextFilter()
    
    
    public ConditionalColumnSetValue.Builder clearSourceTextFilter()

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### clearValueTransformation()
    
    
    public ConditionalColumnSetValue.Builder clearValueTransformation()

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### getCustomFeatures()
    
    
    public Struct getCustomFeatures()

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The customFeatures.  
  
### getCustomFeaturesBuilder()
    
    
    public Struct.Builder getCustomFeaturesBuilder()

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.Builder.html)` |   
  
### getCustomFeaturesOrBuilder()
    
    
    public StructOrBuilder getCustomFeaturesOrBuilder()

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ConditionalColumnSetValue getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getSourceFilterCase()
    
    
    public ConditionalColumnSetValue.SourceFilterCase getSourceFilterCase()

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.SourceFilterCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.SourceFilterCase)` |   
  
### getSourceNumericFilter()
    
    
    public SourceNumericFilter getSourceNumericFilter()

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceNumericFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceNumericFilter)` | The sourceNumericFilter.  
  
### getSourceNumericFilterBuilder()
    
    
    public SourceNumericFilter.Builder getSourceNumericFilterBuilder()

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceNumericFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceNumericFilter.Builder)` |   
  
### getSourceNumericFilterOrBuilder()
    
    
    public SourceNumericFilterOrBuilder getSourceNumericFilterOrBuilder()

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceNumericFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceNumericFilterOrBuilder)` |   
  
### getSourceTextFilter()
    
    
    public SourceTextFilter getSourceTextFilter()

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceTextFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceTextFilter)` | The sourceTextFilter.  
  
### getSourceTextFilterBuilder()
    
    
    public SourceTextFilter.Builder getSourceTextFilterBuilder()

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceTextFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceTextFilter.Builder)` |   
  
### getSourceTextFilterOrBuilder()
    
    
    public SourceTextFilterOrBuilder getSourceTextFilterOrBuilder()

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceTextFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceTextFilterOrBuilder)` |   
  
### getValueTransformation()
    
    
    public ValueTransformation getValueTransformation()

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ValueTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformation)` | The valueTransformation.  
  
### getValueTransformationBuilder()
    
    
    public ValueTransformation.Builder getValueTransformationBuilder()

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ValueTransformation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformation.Builder)` |   
  
### getValueTransformationOrBuilder()
    
    
    public ValueTransformationOrBuilder getValueTransformationOrBuilder()

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ValueTransformationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformationOrBuilder)` |   
  
### hasCustomFeatures()
    
    
    public boolean hasCustomFeatures()

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customFeatures field is set.  
  
### hasSourceNumericFilter()
    
    
    public boolean hasSourceNumericFilter()

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceNumericFilter field is set.  
  
### hasSourceTextFilter()
    
    
    public boolean hasSourceTextFilter()

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceTextFilter field is set.  
  
### hasValueTransformation()
    
    
    public boolean hasValueTransformation()

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the valueTransformation field is set.  
  
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

### mergeCustomFeatures(Struct value)
    
    
    public ConditionalColumnSetValue.Builder mergeCustomFeatures(Struct value)

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### mergeFrom(ConditionalColumnSetValue other)
    
    
    public ConditionalColumnSetValue.Builder mergeFrom(ConditionalColumnSetValue other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConditionalColumnSetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ConditionalColumnSetValue.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ConditionalColumnSetValue.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeSourceNumericFilter(SourceNumericFilter value)
    
    
    public ConditionalColumnSetValue.Builder mergeSourceNumericFilter(SourceNumericFilter value)

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SourceNumericFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceNumericFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### mergeSourceTextFilter(SourceTextFilter value)
    
    
    public ConditionalColumnSetValue.Builder mergeSourceTextFilter(SourceTextFilter value)

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SourceTextFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceTextFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### mergeValueTransformation(ValueTransformation value)
    
    
    public ConditionalColumnSetValue.Builder mergeValueTransformation(ValueTransformation value)

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ValueTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setCustomFeatures(Struct value)
    
    
    public ConditionalColumnSetValue.Builder setCustomFeatures(Struct value)

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setCustomFeatures(Struct.Builder builderForValue)
    
    
    public ConditionalColumnSetValue.Builder setCustomFeatures(Struct.Builder builderForValue)

Optional. Custom engine specific features.

`.google.protobuf.Struct custom_features = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setSourceNumericFilter(SourceNumericFilter value)
    
    
    public ConditionalColumnSetValue.Builder setSourceNumericFilter(SourceNumericFilter value)

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SourceNumericFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceNumericFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setSourceNumericFilter(SourceNumericFilter.Builder builderForValue)
    
    
    public ConditionalColumnSetValue.Builder setSourceNumericFilter(SourceNumericFilter.Builder builderForValue)

Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

` .google.cloud.clouddms.v1.SourceNumericFilter source_numeric_filter = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SourceNumericFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceNumericFilter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setSourceTextFilter(SourceTextFilter value)
    
    
    public ConditionalColumnSetValue.Builder setSourceTextFilter(SourceTextFilter value)

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SourceTextFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceTextFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setSourceTextFilter(SourceTextFilter.Builder builderForValue)
    
    
    public ConditionalColumnSetValue.Builder setSourceTextFilter(SourceTextFilter.Builder builderForValue)

Optional. Optional filter on source column length. Used for text based data types like varchar.

` .google.cloud.clouddms.v1.SourceTextFilter source_text_filter = 100 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SourceTextFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceTextFilter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setValueTransformation(ValueTransformation value)
    
    
    public ConditionalColumnSetValue.Builder setValueTransformation(ValueTransformation value)

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ValueTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### setValueTransformation(ValueTransformation.Builder builderForValue)
    
    
    public ConditionalColumnSetValue.Builder setValueTransformation(ValueTransformation.Builder builderForValue)

Required. Description of data transformation during migration.

` .google.cloud.clouddms.v1.ValueTransformation value_transformation = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ValueTransformation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
