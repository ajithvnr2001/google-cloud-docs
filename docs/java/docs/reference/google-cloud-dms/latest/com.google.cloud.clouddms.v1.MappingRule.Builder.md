---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder
title: Class MappingRule.Builder (2.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:48.342389+00:00
---

# Class MappingRule.Builder (2.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MappingRule.Builder (2.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.98.0 (latest)  2.94.0  2.93.0  2.92.0  2.90.0  2.87.0  2.86.0  2.84.0  2.82.0  2.81.0  2.80.0  2.79.0  2.77.0  2.75.0  2.74.0  2.73.0  2.72.0  2.71.0  2.69.0  2.67.0  2.66.0  2.63.0  2.62.0  2.61.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.8  2.1.9 
    
    
    public static final class MappingRule.Builder extends GeneratedMessage.Builder<MappingRule.Builder> implements MappingRuleOrBuilder

Definition of a transformation that is to be applied to a group of entities in the source schema. Several such transformations can be applied to an entity sequentially to define the corresponding entity in the target schema.

Protobuf type `google.cloud.clouddms.v1.MappingRule`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > MappingRule.Builder

## Implements

[MappingRuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRuleOrBuilder)

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
    
    
    public MappingRule build()

**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### buildPartial()
    
    
    public MappingRule buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### clear()
    
    
    public MappingRule.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearConditionalColumnSetValue()
    
    
    public MappingRule.Builder clearConditionalColumnSetValue()

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearConvertRowidColumn()
    
    
    public MappingRule.Builder clearConvertRowidColumn()

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearDetails()
    
    
    public MappingRule.Builder clearDetails()

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearDisplayName()
    
    
    public MappingRule.Builder clearDisplayName()

Optional. A human readable name

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### clearEntityMove()
    
    
    public MappingRule.Builder clearEntityMove()

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearFilter()
    
    
    public MappingRule.Builder clearFilter()

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearFilterTableColumns()
    
    
    public MappingRule.Builder clearFilterTableColumns()

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearMultiColumnDataTypeChange()
    
    
    public MappingRule.Builder clearMultiColumnDataTypeChange()

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearMultiEntityRename()
    
    
    public MappingRule.Builder clearMultiEntityRename()

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearName()
    
    
    public MappingRule.Builder clearName()

Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### clearRevisionCreateTime()
    
    
    public MappingRule.Builder clearRevisionCreateTime()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearRevisionId()
    
    
    public MappingRule.Builder clearRevisionId()

Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string.

`string revision_id = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### clearRuleOrder()
    
    
    public MappingRule.Builder clearRuleOrder()

Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden.

`int64 rule_order = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### clearRuleScope()
    
    
    public MappingRule.Builder clearRuleScope()

Required. The rule scope

` .google.cloud.clouddms.v1.DatabaseEntityType rule_scope = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### clearSetTablePrimaryKey()
    
    
    public MappingRule.Builder clearSetTablePrimaryKey()

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearSingleColumnChange()
    
    
    public MappingRule.Builder clearSingleColumnChange()

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearSingleEntityRename()
    
    
    public MappingRule.Builder clearSingleEntityRename()

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearSinglePackageChange()
    
    
    public MappingRule.Builder clearSinglePackageChange()

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearSourceSqlChange()
    
    
    public MappingRule.Builder clearSourceSqlChange()

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### clearState()
    
    
    public MappingRule.Builder clearState()

Optional. The mapping rule state

` .google.cloud.clouddms.v1.MappingRule.State state = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### getConditionalColumnSetValue()
    
    
    public ConditionalColumnSetValue getConditionalColumnSetValue()

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue)` | The conditionalColumnSetValue.  
  
### getConditionalColumnSetValueBuilder()
    
    
    public ConditionalColumnSetValue.Builder getConditionalColumnSetValueBuilder()

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)` |   
  
### getConditionalColumnSetValueOrBuilder()
    
    
    public ConditionalColumnSetValueOrBuilder getConditionalColumnSetValueOrBuilder()

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionalColumnSetValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValueOrBuilder)` |   
  
### getConvertRowidColumn()
    
    
    public ConvertRowIdToColumn getConvertRowidColumn()

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConvertRowIdToColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertRowIdToColumn)` | The convertRowidColumn.  
  
### getConvertRowidColumnBuilder()
    
    
    public ConvertRowIdToColumn.Builder getConvertRowidColumnBuilder()

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConvertRowIdToColumn.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertRowIdToColumn.Builder)` |   
  
### getConvertRowidColumnOrBuilder()
    
    
    public ConvertRowIdToColumnOrBuilder getConvertRowidColumnOrBuilder()

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConvertRowIdToColumnOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertRowIdToColumnOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public MappingRule getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDetailsCase()
    
    
    public MappingRule.DetailsCase getDetailsCase()

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.DetailsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.DetailsCase)` |   
  
### getDisplayName()
    
    
    public String getDisplayName()

Optional. A human readable name

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Optional. A human readable name

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEntityMove()
    
    
    public EntityMove getEntityMove()

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EntityMove](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.EntityMove)` | The entityMove.  
  
### getEntityMoveBuilder()
    
    
    public EntityMove.Builder getEntityMoveBuilder()

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EntityMove.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.EntityMove.Builder)` |   
  
### getEntityMoveOrBuilder()
    
    
    public EntityMoveOrBuilder getEntityMoveOrBuilder()

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EntityMoveOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.EntityMoveOrBuilder)` |   
  
### getFilter()
    
    
    public MappingRuleFilter getFilter()

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRuleFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRuleFilter)` | The filter.  
  
### getFilterBuilder()
    
    
    public MappingRuleFilter.Builder getFilterBuilder()

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRuleFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRuleFilter.Builder)` |   
  
### getFilterOrBuilder()
    
    
    public MappingRuleFilterOrBuilder getFilterOrBuilder()

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRuleFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRuleFilterOrBuilder)` |   
  
### getFilterTableColumns()
    
    
    public FilterTableColumns getFilterTableColumns()

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FilterTableColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FilterTableColumns)` | The filterTableColumns.  
  
### getFilterTableColumnsBuilder()
    
    
    public FilterTableColumns.Builder getFilterTableColumnsBuilder()

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FilterTableColumns.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FilterTableColumns.Builder)` |   
  
### getFilterTableColumnsOrBuilder()
    
    
    public FilterTableColumnsOrBuilder getFilterTableColumnsOrBuilder()

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FilterTableColumnsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FilterTableColumnsOrBuilder)` |   
  
### getMultiColumnDataTypeChange()
    
    
    public MultiColumnDatatypeChange getMultiColumnDataTypeChange()

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiColumnDatatypeChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiColumnDatatypeChange)` | The multiColumnDataTypeChange.  
  
### getMultiColumnDataTypeChangeBuilder()
    
    
    public MultiColumnDatatypeChange.Builder getMultiColumnDataTypeChangeBuilder()

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiColumnDatatypeChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiColumnDatatypeChange.Builder)` |   
  
### getMultiColumnDataTypeChangeOrBuilder()
    
    
    public MultiColumnDatatypeChangeOrBuilder getMultiColumnDataTypeChangeOrBuilder()

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiColumnDatatypeChangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiColumnDatatypeChangeOrBuilder)` |   
  
### getMultiEntityRename()
    
    
    public MultiEntityRename getMultiEntityRename()

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiEntityRename](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiEntityRename)` | The multiEntityRename.  
  
### getMultiEntityRenameBuilder()
    
    
    public MultiEntityRename.Builder getMultiEntityRenameBuilder()

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiEntityRename.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiEntityRename.Builder)` |   
  
### getMultiEntityRenameOrBuilder()
    
    
    public MultiEntityRenameOrBuilder getMultiEntityRenameOrBuilder()

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiEntityRenameOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiEntityRenameOrBuilder)` |   
  
### getName()
    
    
    public String getName()

Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRevisionCreateTime()
    
    
    public Timestamp getRevisionCreateTime()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The revisionCreateTime.  
  
### getRevisionCreateTimeBuilder()
    
    
    public Timestamp.Builder getRevisionCreateTimeBuilder()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getRevisionCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getRevisionCreateTimeOrBuilder()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getRevisionId()
    
    
    public String getRevisionId()

Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string.

`string revision_id = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The revisionId.  
  
### getRevisionIdBytes()
    
    
    public ByteString getRevisionIdBytes()

Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string.

`string revision_id = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for revisionId.  
  
### getRuleOrder()
    
    
    public long getRuleOrder()

Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden.

`int64 rule_order = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ruleOrder.  
  
### getRuleScope()
    
    
    public DatabaseEntityType getRuleScope()

Required. The rule scope

` .google.cloud.clouddms.v1.DatabaseEntityType rule_scope = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DatabaseEntityType)` | The ruleScope.  
  
### getRuleScopeValue()
    
    
    public int getRuleScopeValue()

Required. The rule scope

` .google.cloud.clouddms.v1.DatabaseEntityType rule_scope = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for ruleScope.  
  
### getSetTablePrimaryKey()
    
    
    public SetTablePrimaryKey getSetTablePrimaryKey()

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SetTablePrimaryKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SetTablePrimaryKey)` | The setTablePrimaryKey.  
  
### getSetTablePrimaryKeyBuilder()
    
    
    public SetTablePrimaryKey.Builder getSetTablePrimaryKeyBuilder()

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SetTablePrimaryKey.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SetTablePrimaryKey.Builder)` |   
  
### getSetTablePrimaryKeyOrBuilder()
    
    
    public SetTablePrimaryKeyOrBuilder getSetTablePrimaryKeyOrBuilder()

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SetTablePrimaryKeyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SetTablePrimaryKeyOrBuilder)` |   
  
### getSingleColumnChange()
    
    
    public SingleColumnChange getSingleColumnChange()

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SingleColumnChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleColumnChange)` | The singleColumnChange.  
  
### getSingleColumnChangeBuilder()
    
    
    public SingleColumnChange.Builder getSingleColumnChangeBuilder()

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SingleColumnChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleColumnChange.Builder)` |   
  
### getSingleColumnChangeOrBuilder()
    
    
    public SingleColumnChangeOrBuilder getSingleColumnChangeOrBuilder()

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SingleColumnChangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleColumnChangeOrBuilder)` |   
  
### getSingleEntityRename()
    
    
    public SingleEntityRename getSingleEntityRename()

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SingleEntityRename](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleEntityRename)` | The singleEntityRename.  
  
### getSingleEntityRenameBuilder()
    
    
    public SingleEntityRename.Builder getSingleEntityRenameBuilder()

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SingleEntityRename.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleEntityRename.Builder)` |   
  
### getSingleEntityRenameOrBuilder()
    
    
    public SingleEntityRenameOrBuilder getSingleEntityRenameOrBuilder()

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SingleEntityRenameOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleEntityRenameOrBuilder)` |   
  
### getSinglePackageChange()
    
    
    public SinglePackageChange getSinglePackageChange()

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SinglePackageChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SinglePackageChange)` | The singlePackageChange.  
  
### getSinglePackageChangeBuilder()
    
    
    public SinglePackageChange.Builder getSinglePackageChangeBuilder()

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SinglePackageChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SinglePackageChange.Builder)` |   
  
### getSinglePackageChangeOrBuilder()
    
    
    public SinglePackageChangeOrBuilder getSinglePackageChangeOrBuilder()

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SinglePackageChangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SinglePackageChangeOrBuilder)` |   
  
### getSourceSqlChange()
    
    
    public SourceSqlChange getSourceSqlChange()

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceSqlChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceSqlChange)` | The sourceSqlChange.  
  
### getSourceSqlChangeBuilder()
    
    
    public SourceSqlChange.Builder getSourceSqlChangeBuilder()

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceSqlChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceSqlChange.Builder)` |   
  
### getSourceSqlChangeOrBuilder()
    
    
    public SourceSqlChangeOrBuilder getSourceSqlChangeOrBuilder()

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceSqlChangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceSqlChangeOrBuilder)` |   
  
### getState()
    
    
    public MappingRule.State getState()

Optional. The mapping rule state

` .google.cloud.clouddms.v1.MappingRule.State state = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MappingRule.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.State)` | The state.  
  
### getStateValue()
    
    
    public int getStateValue()

Optional. The mapping rule state

` .google.cloud.clouddms.v1.MappingRule.State state = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasConditionalColumnSetValue()
    
    
    public boolean hasConditionalColumnSetValue()

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the conditionalColumnSetValue field is set.  
  
### hasConvertRowidColumn()
    
    
    public boolean hasConvertRowidColumn()

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the convertRowidColumn field is set.  
  
### hasEntityMove()
    
    
    public boolean hasEntityMove()

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the entityMove field is set.  
  
### hasFilter()
    
    
    public boolean hasFilter()

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filter field is set.  
  
### hasFilterTableColumns()
    
    
    public boolean hasFilterTableColumns()

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filterTableColumns field is set.  
  
### hasMultiColumnDataTypeChange()
    
    
    public boolean hasMultiColumnDataTypeChange()

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multiColumnDataTypeChange field is set.  
  
### hasMultiEntityRename()
    
    
    public boolean hasMultiEntityRename()

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multiEntityRename field is set.  
  
### hasRevisionCreateTime()
    
    
    public boolean hasRevisionCreateTime()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the revisionCreateTime field is set.  
  
### hasSetTablePrimaryKey()
    
    
    public boolean hasSetTablePrimaryKey()

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the setTablePrimaryKey field is set.  
  
### hasSingleColumnChange()
    
    
    public boolean hasSingleColumnChange()

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the singleColumnChange field is set.  
  
### hasSingleEntityRename()
    
    
    public boolean hasSingleEntityRename()

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the singleEntityRename field is set.  
  
### hasSinglePackageChange()
    
    
    public boolean hasSinglePackageChange()

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the singlePackageChange field is set.  
  
### hasSourceSqlChange()
    
    
    public boolean hasSourceSqlChange()

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceSqlChange field is set.  
  
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

### mergeConditionalColumnSetValue(ConditionalColumnSetValue value)
    
    
    public MappingRule.Builder mergeConditionalColumnSetValue(ConditionalColumnSetValue value)

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ConditionalColumnSetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeConvertRowidColumn(ConvertRowIdToColumn value)
    
    
    public MappingRule.Builder mergeConvertRowidColumn(ConvertRowIdToColumn value)

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ConvertRowIdToColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertRowIdToColumn)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeEntityMove(EntityMove value)
    
    
    public MappingRule.Builder mergeEntityMove(EntityMove value)

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EntityMove](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.EntityMove)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeFilter(MappingRuleFilter value)
    
    
    public MappingRule.Builder mergeFilter(MappingRuleFilter value)

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MappingRuleFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRuleFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeFilterTableColumns(FilterTableColumns value)
    
    
    public MappingRule.Builder mergeFilterTableColumns(FilterTableColumns value)

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FilterTableColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FilterTableColumns)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeFrom(MappingRule other)
    
    
    public MappingRule.Builder mergeFrom(MappingRule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public MappingRule.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public MappingRule.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeMultiColumnDataTypeChange(MultiColumnDatatypeChange value)
    
    
    public MappingRule.Builder mergeMultiColumnDataTypeChange(MultiColumnDatatypeChange value)

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MultiColumnDatatypeChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiColumnDatatypeChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeMultiEntityRename(MultiEntityRename value)
    
    
    public MappingRule.Builder mergeMultiEntityRename(MultiEntityRename value)

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MultiEntityRename](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiEntityRename)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeRevisionCreateTime(Timestamp value)
    
    
    public MappingRule.Builder mergeRevisionCreateTime(Timestamp value)

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeSetTablePrimaryKey(SetTablePrimaryKey value)
    
    
    public MappingRule.Builder mergeSetTablePrimaryKey(SetTablePrimaryKey value)

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SetTablePrimaryKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SetTablePrimaryKey)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeSingleColumnChange(SingleColumnChange value)
    
    
    public MappingRule.Builder mergeSingleColumnChange(SingleColumnChange value)

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SingleColumnChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleColumnChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeSingleEntityRename(SingleEntityRename value)
    
    
    public MappingRule.Builder mergeSingleEntityRename(SingleEntityRename value)

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SingleEntityRename](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleEntityRename)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeSinglePackageChange(SinglePackageChange value)
    
    
    public MappingRule.Builder mergeSinglePackageChange(SinglePackageChange value)

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SinglePackageChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SinglePackageChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### mergeSourceSqlChange(SourceSqlChange value)
    
    
    public MappingRule.Builder mergeSourceSqlChange(SourceSqlChange value)

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SourceSqlChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceSqlChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setConditionalColumnSetValue(ConditionalColumnSetValue value)
    
    
    public MappingRule.Builder setConditionalColumnSetValue(ConditionalColumnSetValue value)

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ConditionalColumnSetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setConditionalColumnSetValue(ConditionalColumnSetValue.Builder builderForValue)
    
    
    public MappingRule.Builder setConditionalColumnSetValue(ConditionalColumnSetValue.Builder builderForValue)

Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

` .google.cloud.clouddms.v1.ConditionalColumnSetValue conditional_column_set_value = 108 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ConditionalColumnSetValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConditionalColumnSetValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setConvertRowidColumn(ConvertRowIdToColumn value)
    
    
    public MappingRule.Builder setConvertRowidColumn(ConvertRowIdToColumn value)

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ConvertRowIdToColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertRowIdToColumn)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setConvertRowidColumn(ConvertRowIdToColumn.Builder builderForValue)
    
    
    public MappingRule.Builder setConvertRowidColumn(ConvertRowIdToColumn.Builder builderForValue)

Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

` .google.cloud.clouddms.v1.ConvertRowIdToColumn convert_rowid_column = 114 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ConvertRowIdToColumn.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertRowIdToColumn.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setDisplayName(String value)
    
    
    public MappingRule.Builder setDisplayName(String value)

Optional. A human readable name

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public MappingRule.Builder setDisplayNameBytes(ByteString value)

Optional. A human readable name

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setEntityMove(EntityMove value)
    
    
    public MappingRule.Builder setEntityMove(EntityMove value)

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EntityMove](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.EntityMove)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setEntityMove(EntityMove.Builder builderForValue)
    
    
    public MappingRule.Builder setEntityMove(EntityMove.Builder builderForValue)

Optional. Rule to specify how multiple entities should be relocated into a different schema.

` .google.cloud.clouddms.v1.EntityMove entity_move = 105 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EntityMove.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.EntityMove.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setFilter(MappingRuleFilter value)
    
    
    public MappingRule.Builder setFilter(MappingRuleFilter value)

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MappingRuleFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRuleFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setFilter(MappingRuleFilter.Builder builderForValue)
    
    
    public MappingRule.Builder setFilter(MappingRuleFilter.Builder builderForValue)

Required. The rule filter

` .google.cloud.clouddms.v1.MappingRuleFilter filter = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MappingRuleFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRuleFilter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setFilterTableColumns(FilterTableColumns value)
    
    
    public MappingRule.Builder setFilterTableColumns(FilterTableColumns value)

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FilterTableColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FilterTableColumns)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setFilterTableColumns(FilterTableColumns.Builder builderForValue)
    
    
    public MappingRule.Builder setFilterTableColumns(FilterTableColumns.Builder builderForValue)

Optional. Rule to specify the list of columns to include or exclude from a table.

` .google.cloud.clouddms.v1.FilterTableColumns filter_table_columns = 118 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[FilterTableColumns.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FilterTableColumns.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setMultiColumnDataTypeChange(MultiColumnDatatypeChange value)
    
    
    public MappingRule.Builder setMultiColumnDataTypeChange(MultiColumnDatatypeChange value)

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MultiColumnDatatypeChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiColumnDatatypeChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setMultiColumnDataTypeChange(MultiColumnDatatypeChange.Builder builderForValue)
    
    
    public MappingRule.Builder setMultiColumnDataTypeChange(MultiColumnDatatypeChange.Builder builderForValue)

Optional. Rule to specify how multiple columns should be converted to a different data type.

` .google.cloud.clouddms.v1.MultiColumnDatatypeChange multi_column_data_type_change = 107 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MultiColumnDatatypeChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiColumnDatatypeChange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setMultiEntityRename(MultiEntityRename value)
    
    
    public MappingRule.Builder setMultiEntityRename(MultiEntityRename value)

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MultiEntityRename](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiEntityRename)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setMultiEntityRename(MultiEntityRename.Builder builderForValue)
    
    
    public MappingRule.Builder setMultiEntityRename(MultiEntityRename.Builder builderForValue)

Optional. Rule to specify how multiple entities should be renamed.

` .google.cloud.clouddms.v1.MultiEntityRename multi_entity_rename = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MultiEntityRename.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MultiEntityRename.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setName(String value)
    
    
    public MappingRule.Builder setName(String value)

Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public MappingRule.Builder setNameBytes(ByteString value)

Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setRevisionCreateTime(Timestamp value)
    
    
    public MappingRule.Builder setRevisionCreateTime(Timestamp value)

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setRevisionCreateTime(Timestamp.Builder builderForValue)
    
    
    public MappingRule.Builder setRevisionCreateTime(Timestamp.Builder builderForValue)

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setRevisionId(String value)
    
    
    public MappingRule.Builder setRevisionId(String value)

Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string.

`string revision_id = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The revisionId to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setRevisionIdBytes(ByteString value)
    
    
    public MappingRule.Builder setRevisionIdBytes(ByteString value)

Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string.

`string revision_id = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for revisionId to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setRuleOrder(long value)
    
    
    public MappingRule.Builder setRuleOrder(long value)

Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden.

`int64 rule_order = 6 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The ruleOrder to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setRuleScope(DatabaseEntityType value)
    
    
    public MappingRule.Builder setRuleScope(DatabaseEntityType value)

Required. The rule scope

` .google.cloud.clouddms.v1.DatabaseEntityType rule_scope = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DatabaseEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DatabaseEntityType)`  
The ruleScope to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setRuleScopeValue(int value)
    
    
    public MappingRule.Builder setRuleScopeValue(int value)

Required. The rule scope

` .google.cloud.clouddms.v1.DatabaseEntityType rule_scope = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for ruleScope to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setSetTablePrimaryKey(SetTablePrimaryKey value)
    
    
    public MappingRule.Builder setSetTablePrimaryKey(SetTablePrimaryKey value)

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SetTablePrimaryKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SetTablePrimaryKey)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSetTablePrimaryKey(SetTablePrimaryKey.Builder builderForValue)
    
    
    public MappingRule.Builder setSetTablePrimaryKey(SetTablePrimaryKey.Builder builderForValue)

Optional. Rule to specify the primary key for a table

` .google.cloud.clouddms.v1.SetTablePrimaryKey set_table_primary_key = 115 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SetTablePrimaryKey.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SetTablePrimaryKey.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSingleColumnChange(SingleColumnChange value)
    
    
    public MappingRule.Builder setSingleColumnChange(SingleColumnChange value)

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SingleColumnChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleColumnChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSingleColumnChange(SingleColumnChange.Builder builderForValue)
    
    
    public MappingRule.Builder setSingleColumnChange(SingleColumnChange.Builder builderForValue)

Optional. Rule to specify how a single column is converted.

` .google.cloud.clouddms.v1.SingleColumnChange single_column_change = 106 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SingleColumnChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleColumnChange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSingleEntityRename(SingleEntityRename value)
    
    
    public MappingRule.Builder setSingleEntityRename(SingleEntityRename value)

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SingleEntityRename](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleEntityRename)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSingleEntityRename(SingleEntityRename.Builder builderForValue)
    
    
    public MappingRule.Builder setSingleEntityRename(SingleEntityRename.Builder builderForValue)

Optional. Rule to specify how a single entity should be renamed.

` .google.cloud.clouddms.v1.SingleEntityRename single_entity_rename = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SingleEntityRename.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SingleEntityRename.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSinglePackageChange(SinglePackageChange value)
    
    
    public MappingRule.Builder setSinglePackageChange(SinglePackageChange value)

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SinglePackageChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SinglePackageChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSinglePackageChange(SinglePackageChange.Builder builderForValue)
    
    
    public MappingRule.Builder setSinglePackageChange(SinglePackageChange.Builder builderForValue)

Optional. Rule to specify how a single package is converted.

` .google.cloud.clouddms.v1.SinglePackageChange single_package_change = 116 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SinglePackageChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SinglePackageChange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSourceSqlChange(SourceSqlChange value)
    
    
    public MappingRule.Builder setSourceSqlChange(SourceSqlChange value)

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SourceSqlChange](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceSqlChange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setSourceSqlChange(SourceSqlChange.Builder builderForValue)
    
    
    public MappingRule.Builder setSourceSqlChange(SourceSqlChange.Builder builderForValue)

Optional. Rule to change the sql code for an entity, for example, function, procedure.

` .google.cloud.clouddms.v1.SourceSqlChange source_sql_change = 117 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SourceSqlChange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SourceSqlChange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` |   
  
### setState(MappingRule.State value)
    
    
    public MappingRule.Builder setState(MappingRule.State value)

Optional. The mapping rule state

` .google.cloud.clouddms.v1.MappingRule.State state = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MappingRule.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public MappingRule.Builder setStateValue(int value)

Optional. The mapping rule state

` .google.cloud.clouddms.v1.MappingRule.State state = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
